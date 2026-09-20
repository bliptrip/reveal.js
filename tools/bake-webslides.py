#!/usr/bin/env python3
"""
bake-webslides.py -- evaluate webslides.css's media queries at a fixed size.

WebSlides is a fluid framework: its type scale, .wrap width, .grid/.column
behaviour and section padding all switch on @media queries keyed to the
browser window (568 / 768 / 1024 / 1200 / 1280 px, plus aspect-ratio and
orientation). That was right when a section *was* the viewport.

Under reveal.js a slide is a fixed logical box (1920x1080 for this deck) that
reveal scales with a CSS transform to fit whatever it is shown on. Media
queries do not see the transform -- they still measure the window -- so a
1280px-wide laptop window, or the 400px preview iframes in the speaker view,
would get WebSlides' tablet or phone layout while reveal scales it up, and
nothing would look like the original deck.

This script resolves that once, ahead of time. Every @media block is
evaluated against the logical slide size:

    true   -> its rules are emitted unwrapped (always apply)
    false  -> its rules are dropped
    print  -> left exactly as written

so the output stylesheet describes WebSlides at exactly 1920x1080, whatever
the window does. Upstream webslides.css is left untouched; regenerate the
baked copy whenever it changes:

    python3 tools/bake-webslides.py \\
        --src presentation/css/webslides.css \\
        --out presentation/css/webslides-1920.css
"""

import argparse
import re
import sys
from fractions import Fraction

# --------------------------------------------------------------------------
# A very small CSS block parser. Enough for Sass output: comments, strings,
# nested at-rules. Not a general CSS parser and does not try to be.
# --------------------------------------------------------------------------

COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)


def strip_comments(text):
    return COMMENT_RE.sub("", text)


# Upstream webslides.css ships with one syntax error: inside the
# @media (min-width: 768px) card block, `.card-20 figure { width: 20%;` has
# no closing brace. Browsers recover per CSS Syntax Level 3 by treating
# everything up to the next bare `}` as garbage declarations of that rule --
# which discards every rule from `.card-30 figure` through
# `.fullscreen [class*='card'] .flex-content { padding: 6.4rem }`, and then
# leaves the @media block open so the rest of the file nests inside it (a
# no-op at >= 768px).
#
# The deck was authored and tuned against that recovered rendering, so the
# bake reproduces it rather than "fixing" upstream: close the brace where the
# browser effectively did, and drop the rules the browser dropped. The match
# is exact; if upstream ever changes, the guard below fails the run instead
# of silently baking something different.
UPSTREAM_REPAIRS = [
    (
        re.compile(
            r"(\.card-20 figure \{\s*width: 20%;)\s*"          # keep, then close
            r"\.card-30 figure,.*?"                             # drop ...
            r"\.fullscreen \[class\*='card'\] blockquote \{\s*"
            r"padding: 6\.4rem; \}",                            # ... through here
            re.S,
        ),
        r"\1 }",
    ),
]


def repair_upstream(text):
    for pattern, replacement in UPSTREAM_REPAIRS:
        text, n = pattern.subn(replacement, text, count=1)
        if n != 1:
            raise SystemExit(
                "bake-webslides: upstream webslides.css no longer matches a known "
                "repair -- review UPSTREAM_REPAIRS against the new source."
            )
    return text


def find_matching_brace(text, start):
    """text[start] == '{'. Return index of the matching '}'."""
    depth = 0
    i = start
    n = len(text)
    quote = None
    while i < n:
        c = text[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "'\"":
            quote = c
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError(f"unbalanced braces after: {text[start-80:start]!r}")


def parse_blocks(text):
    """Yield (prelude, body) pairs from a stylesheet or a block body that
    contains nested rules. prelude is the selector / at-rule text, body the
    text between its braces (exclusive)."""
    i = 0
    n = len(text)
    while i < n:
        # Statement-style at-rules (@import, @charset) end at ';' without
        # a block. Look for whichever comes first.
        j_open = text.find("{", i)
        j_semi = text.find(";", i)
        if j_open == -1:
            break
        if j_semi != -1 and j_semi < j_open and text[i:j_semi].lstrip().startswith("@"):
            yield (text[i:j_semi + 1].strip(), None)
            i = j_semi + 1
            continue
        j_close = find_matching_brace(text, j_open)
        yield (text[i:j_open].strip(), text[j_open + 1:j_close])
        i = j_close + 1


# --------------------------------------------------------------------------
# Media query evaluation
# --------------------------------------------------------------------------

LENGTH_RE = re.compile(r"^\s*([\d.]+)\s*(px|em|rem)?\s*$")
RATIO_RE = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")


class Undecidable(Exception):
    """The query depends on something we do not model (print)."""


def parse_length(value):
    m = LENGTH_RE.match(value)
    if not m:
        raise ValueError(f"cannot parse length {value!r}")
    num = float(m.group(1))
    unit = m.group(2) or "px"
    if unit in ("em", "rem"):
        num *= 16  # media queries use the initial font size, not html{}
    return num


def eval_feature(name, value, width, height):
    name = name.strip().lower()
    aspect = Fraction(width, height)
    if name == "min-width":
        return width >= parse_length(value)
    if name == "max-width":
        return width <= parse_length(value)
    if name == "min-height":
        return height >= parse_length(value)
    if name == "max-height":
        return height <= parse_length(value)
    if name == "width":
        return width == parse_length(value)
    if name == "height":
        return height == parse_length(value)
    if name in ("min-aspect-ratio", "max-aspect-ratio", "aspect-ratio"):
        m = RATIO_RE.match(value)
        if not m:
            raise ValueError(f"cannot parse ratio {value!r}")
        r = Fraction(int(m.group(1)), int(m.group(2)))
        if name == "min-aspect-ratio":
            return aspect >= r
        if name == "max-aspect-ratio":
            return aspect <= r
        return aspect == r
    if name == "orientation":
        v = value.strip().lower()
        if v == "portrait":
            return height >= width
        if v == "landscape":
            return width > height
    raise ValueError(f"unsupported media feature {name!r}")


def eval_query(query, width, height):
    """True / False, or raise Undecidable."""
    for alt in query.split(","):
        result = True
        for term in re.split(r"\s+and\s+", alt.strip(), flags=re.I):
            term = term.strip()
            if not term:
                continue
            m = re.match(r"^\(\s*([\w-]+)\s*:\s*(.+?)\s*\)$", term)
            if m:
                if not eval_feature(m.group(1), m.group(2), width, height):
                    result = False
                    break
                continue
            t = term.lower()
            if t in ("screen", "all"):
                continue
            if t == "print":
                raise Undecidable(query)
            if t.startswith("not ") or t.startswith("only "):
                raise ValueError(f"unsupported media query {query!r}")
            raise ValueError(f"unsupported media term {term!r}")
        if result:
            return True
    return False


# --------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------

def reindent(body):
    lines = [ln.rstrip() for ln in body.strip("\n").splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    # normalise leading whitespace to two spaces
    return "\n".join("  " + ln.strip() for ln in lines if ln.strip())


def bake(text, width, height, stats, depth=0):
    out = []
    for prelude, body in parse_blocks(text):
        if body is None:                      # @import / @charset
            out.append(prelude)
            continue
        if prelude.lower().startswith("@media"):
            query = prelude[len("@media"):].strip()
            try:
                verdict = eval_query(query, width, height)
            except Undecidable:
                stats["kept"] += 1
                out.append(f"{prelude} {{\n{reindent(body)}\n}}")
                continue
            if verdict:
                stats["unwrapped"] += 1
                out.append(f"/* baked: {prelude} */")
                out.append(bake(body, width, height, stats, depth + 1))
            else:
                stats["dropped"] += 1
            continue
        if prelude.startswith("@"):           # @font-face, @keyframes, ...
            out.append(f"{prelude} {{{body}}}")
            continue
        out.append(f"{prelude} {{\n{reindent(body)}\n}}")
    return "\n\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="upstream webslides.css")
    ap.add_argument("--out", required=True, help="baked stylesheet to write")
    ap.add_argument("--width", type=int, default=1920, help="logical slide width (px)")
    ap.add_argument("--height", type=int, default=1080, help="logical slide height (px)")
    args = ap.parse_args()

    with open(args.src, encoding="utf-8") as f:
        src = f.read()

    stats = {"unwrapped": 0, "dropped": 0, "kept": 0}
    src = repair_upstream(strip_comments(src))
    body = bake(src, args.width, args.height, stats)

    header = (
        "/* GENERATED by tools/bake-webslides.py -- do not edit.\n"
        f"   Source: {args.src}\n"
        f"   Media queries evaluated at {args.width}x{args.height}: "
        f"{stats['unwrapped']} unwrapped, {stats['dropped']} dropped, "
        f"{stats['kept']} kept (print).\n"
        "   Upstream WebSlides is MIT licensed, (c) Jose Luis Antunez. */\n\n"
    )
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(header + body + "\n")

    print(f"bake-webslides: {args.src} -> {args.out} @ {args.width}x{args.height}")
    print(f"                {stats['unwrapped']} @media unwrapped, "
          f"{stats['dropped']} dropped, {stats['kept']} kept")
    return 0


if __name__ == "__main__":
    sys.exit(main())
