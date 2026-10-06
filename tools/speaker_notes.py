#!/usr/bin/env python3
"""
speaker_notes.py -- extract, edit and write back the speaker notes of a
reveal.js seminar deck (presentation/index.html).

Every slide in the deck is a <section id="..."> carrying at most one
<aside class="notes">. This tool moves those notes to and from Markdown so
they can be edited, reviewed and diffed as prose, and keeps the deck's
per-slide timing attributes consistent.

The Markdown format is the one the seminar prep documents already use, so a
prep doc can itself be the source of the notes:

    **[`slide-id`](http://localhost:8000/presentation/#/slide-id)** · 1.25 min
    - A bullet becomes <li>.   **bold** -> <strong>,  *italic* -> <em>
    A line that is not a bullet becomes a <p>.
    <sub>, <sup>, <br>, <code>, <small>, <span>, <a> pass through as HTML.

    > Anything after the first blank line (e.g. a quoted spoken script)
    > is ignored -- only the lines directly under the heading are notes.

Commands
--------
    list      table of slides: section, minutes, words of notes; section and
              talk totals (a quick pacing check)
    extract   write every slide's notes as Markdown (-o FILE, default stdout)
              --into PREP.md rewrites the note bullets under each slide
              heading already present in a prep doc, leaving the rest of the
              doc (spoken scripts, tables) untouched
    update    --from FILE.md  write the notes found in FILE.md back into the
              deck. Slides not mentioned in FILE.md keep their notes.
              --apply-minutes also takes "· N min" from each heading and
              updates data-minutes / data-timing, then restamps (below).
              --dry-run reports what would change without writing.
    restamp   recompute data-timing (from data-minutes), data-section-index,
              data-section-count, data-section-minutes and reveal's totalTime
              after slides are added, removed, reordered or retimed
    check     round-trip every slide's notes HTML -> Markdown -> HTML and
              report any slide whose notes would not survive unchanged
    scripts   --from PREP.md  copy each slide's spoken script (the "> " quoted
              lines under its heading) into the deck notes, below the cues,
              after a dashed rule and in a highlighted box. --remove strips
              them again. The script block is invisible to list / extract /
              check, and update keeps it, so the cue round-trip is unchanged.
    prettify  re-indent every <aside class="notes"> (one block element per
              line, nested by depth) and wrap its text at --wrap columns
              (default 120, counting the indent). Only whitespace HTML ignores
              is changed, so the speaker view and extract / check / update
              read the notes exactly as before. --dry-run shows the diff.

    update, scripts and restamp also take --prettify [--wrap N], which runs
    prettify on the deck before it is written (and before update's
    --dry-run diff). Without it they write the <aside> blocks they change on
    one line, as before. extract never needs it: it reads a prettified deck
    and a one-line deck the same way.

Examples
--------
    python3 tools/speaker_notes.py list
    python3 tools/speaker_notes.py extract -o Speaker_Notes.md
    python3 tools/speaker_notes.py update --from Seminar_Prep.md
    python3 tools/speaker_notes.py extract --into Seminar_Prep.md
    python3 tools/speaker_notes.py restamp
    python3 tools/speaker_notes.py scripts --from Seminar_Prep.md
    python3 tools/speaker_notes.py prettify --wrap 100
    python3 tools/speaker_notes.py update --from Seminar_Prep.md --prettify

The deck is edited as text, slide by slide: nothing outside the <aside> (or,
for restamp, the <section> start tags and totalTime) is re-serialised, so
diffs stay small and hand formatting survives.

Only the Python standard library and BeautifulSoup (bs4) are required.
"""

import argparse
import datetime as _dt
import difflib
import html
import re
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:  # pragma: no cover
    sys.exit("speaker_notes.py needs BeautifulSoup: pip install beautifulsoup4")

HERE = Path(__file__).resolve().parent
DEFAULT_DECK = HERE.parent / "presentation" / "index.html"
BASE_URL = "http://localhost:8000/presentation/#/"

# Spoken-script block appended to a slide's notes (below the cues). Inline
# styles, because the notes are shown in reveal's speaker window, which does
# not load the deck's CSS.
SCRIPT_MARK = '<hr class="notes-script-rule"'
SCRIPT_RULE = ('<hr class="notes-script-rule" style="border:0;border-top:3px dashed #d08c00;'
               'margin:16px 0 10px;">')
SCRIPT_BOX = ('<div class="notes-script" style="background:#fff3cd;color:#2b2100;'
              'border-left:6px solid #e0a100;border-radius:4px;padding:8px 12px;line-height:1.45;">')
SCRIPT_LABEL = ('<p style="margin:0 0 6px;font-size:0.75em;font-weight:bold;letter-spacing:0.08em;'
                'color:#9a6700;">FULL SCRIPT</p>')

SECTION_RE = re.compile(r'(<section\b[^>]*>)(.*?)(</section>)', re.S)
ID_RE = re.compile(r'\bid="([^"]+)"')
NOTES_RE = re.compile(r'<aside\s+class="notes"\s*>(.*?)</aside>', re.S)
HEAD_RE = re.compile(
    r'^\*\*\[`(?P<id>[A-Za-z0-9_.:-]+)`\]\([^)]*\)\*\*'
    r'(?:\s*·\s*(?P<min>\d+(?:\.\d+)?)\s*min)?')
# inline HTML allowed to pass through Markdown untouched
RAW_TAG_RE = re.compile(
    r'</?(?:sub|sup|br|code|small|span|a|u|s|mark|kbd)\b[^>]*?/?>', re.I)


# --------------------------------------------------------------------------
# attribute helpers (operate on a section start tag, as text)
# --------------------------------------------------------------------------

def get_attr(tag, name):
    m = re.search(r'\b%s="([^"]*)"' % re.escape(name), tag)
    return html.unescape(m.group(1)) if m else None


def set_attr(tag, name, value):
    """Set (or add, before the closing '>') an attribute on a start tag."""
    value = html.escape(str(value), quote=True)
    pat = re.compile(r'(\b%s=")[^"]*(")' % re.escape(name))
    if pat.search(tag):
        return pat.sub(lambda m: m.group(1) + value + m.group(2), tag, count=1)
    return tag[:-1] + ' %s="%s">' % (name, value)


def del_attr(tag, name):
    return re.sub(r'\s+%s="[^"]*"' % re.escape(name), '', tag, count=1)


def fmt_minutes(x):
    s = ('%.2f' % x).rstrip('0').rstrip('.')
    return s or '0'


# --------------------------------------------------------------------------
# deck model
# --------------------------------------------------------------------------

class Slide:
    def __init__(self, m):
        self.match = m
        self.start_tag, self.body, self.end_tag = m.group(1), m.group(2), m.group(3)
        idm = ID_RE.search(self.start_tag)
        self.id = idm.group(1) if idm else None

    @property
    def section(self):
        return get_attr(self.start_tag, 'data-section')

    @property
    def minutes(self):
        v = get_attr(self.start_tag, 'data-minutes')
        return float(v) if v not in (None, '') else None

    @property
    def notes_all(self):
        m = NOTES_RE.search(self.body)
        return m.group(1) if m else None

    @property
    def notes_html(self):
        """The cue notes only (the spoken-script block, if any, is excluded)."""
        a = self.notes_all
        if a is None:
            return None
        i = a.find(SCRIPT_MARK)
        return a if i < 0 else a[:i].rstrip()

    @property
    def script_tail(self):
        a = self.notes_all or ''
        i = a.find(SCRIPT_MARK)
        return '' if i < 0 else a[i:]

    def text(self):
        return self.start_tag + self.body + self.end_tag


def load(deck):
    src = Path(deck).read_text(encoding='utf-8')
    slides = [Slide(m) for m in SECTION_RE.finditer(src)]
    return src, slides


def rebuild(src, slides):
    out, pos = [], 0
    for s in slides:
        out.append(src[pos:s.match.start()])
        out.append(s.text())
        pos = s.match.end()
    out.append(src[pos:])
    return ''.join(out)


# --------------------------------------------------------------------------
# notes HTML <-> Markdown
# --------------------------------------------------------------------------

def _inline_md(node):
    if isinstance(node, NavigableString):
        return re.sub(r'\s+', ' ', str(node))
    if not isinstance(node, Tag):
        return ''
    inner = ''.join(_inline_md(c) for c in node.children)
    name = node.name.lower()
    if name in ('strong', 'b'):
        return '**%s**' % inner if inner.strip() else inner
    if name in ('em', 'i'):
        return '*%s*' % inner if inner.strip() else inner
    if name == 'br':
        return '<br/>'
    attrs = ''.join(' %s="%s"' % (k, html.escape(' '.join(v) if isinstance(v, list) else v, quote=True))
                    for k, v in node.attrs.items())
    return '<%s%s>%s</%s>' % (name, attrs, inner, name)


def notes_to_md(notes_html):
    """Notes <aside> inner HTML -> list of Markdown lines."""
    if notes_html is None:
        return []
    soup = BeautifulSoup(notes_html, 'html.parser')
    lines, loose = [], []

    def flush():
        t = ''.join(loose).strip()
        if t:
            lines.append(t)
        loose.clear()

    for child in soup.children:
        if isinstance(child, Tag) and child.name in ('ul', 'ol'):
            flush()
            for li in child.find_all('li', recursive=False):
                lines.append('- ' + ''.join(_inline_md(c) for c in li.children).strip())
        elif isinstance(child, Tag) and child.name == 'p':
            flush()
            t = ''.join(_inline_md(c) for c in child.children).strip()
            if t:
                lines.append(t)
        else:
            loose.append(_inline_md(child))
    flush()
    return lines


def _inline_html(text):
    parts = RAW_TAG_RE.split(text)
    tags = RAW_TAG_RE.findall(text)
    out = []
    for i, p in enumerate(parts):
        out.append(html.escape(p, quote=False))
        if i < len(tags):
            out.append(tags[i])
    s = ''.join(out)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\*\w])\*(?![\s\*])(.+?)(?<![\s\*])\*(?![\*\w])', r'<em>\1</em>', s)
    return s


def md_to_notes(lines):
    """List of Markdown lines -> notes <aside> inner HTML."""
    out, items = [], []

    def flush():
        if items:
            out.append('<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>')
            items.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if re.match(r'^\s*[-*]\s+', line):
            items.append(_inline_html(re.sub(r'^\s*[-*]\s+', '', line).strip()))
        else:
            flush()
            out.append('<p>%s</p>' % _inline_html(line.strip()))
    flush()
    return ''.join(out)


def set_notes(slide, inner, tail=None):
    """Replace the cue notes; the spoken-script block is kept unless tail is given."""
    if tail is None:
        tail = slide.script_tail
    new_aside = '<aside class="notes">%s%s</aside>' % (inner, tail)
    if NOTES_RE.search(slide.body):
        slide.body = NOTES_RE.sub(lambda m: new_aside, slide.body, count=1)
    else:
        # insert before the closing tag, matching the deck's indentation
        indent = re.search(r'\n([ \t]*)$', slide.body)
        pad = indent.group(1) if indent else '        '
        slide.body = slide.body.rstrip() + '\n' + pad + new_aside + '\n' + pad


# --------------------------------------------------------------------------
# Markdown files
# --------------------------------------------------------------------------

def parse_md(path):
    """Return {slide_id: (minutes or None, [note lines])} from a notes/prep doc."""
    result, cur, buf, mins = {}, None, [], None
    started = False

    def close():
        if cur is not None:
            result[cur] = (mins, list(buf))

    for line in Path(path).read_text(encoding='utf-8').splitlines():
        m = HEAD_RE.match(line.strip())
        if m:
            close()
            cur, buf, started = m.group('id'), [], False
            mins = float(m.group('min')) if m.group('min') else None
            continue
        if cur is None:
            continue
        if not line.strip():
            if started:          # first blank line after the notes ends them
                close()
                cur = None
            continue
        if line.lstrip().startswith(('>', '#', '|', '---')):
            close()
            cur = None
            continue
        started = True
        buf.append(line)
    close()
    return result


def heading(slide):
    mins = slide.minutes
    h = '**[`%s`](%s%s)**' % (slide.id, BASE_URL, slide.id)
    if mins is not None:
        h += ' · %s min' % fmt_minutes(mins)
    return h


def deck_title(src):
    m = re.search(r'<title>(.*?)</title>', src, re.S)
    return html.unescape(m.group(1).strip()) if m else 'seminar deck'


def to_markdown(src, slides, deck_path):
    today = _dt.date.today().isoformat()
    out = ['# Speaker notes — %s' % deck_title(src), '',
           '_Extracted from `%s` by `tools/speaker_notes.py` on %s. Edit the lines under each '
           'slide heading, then run `python3 tools/speaker_notes.py update --from <this file>`. '
           'A blank line ends a slide\'s notes._' % (Path(deck_path).name, today), '']
    last = object()
    for s in slides:
        if not s.id:
            continue
        if s.section != last:
            out += ['## %s' % (s.section or '(no section)'), '']
            last = s.section
        out.append(heading(s))
        out += notes_to_md(s.notes_html) or ['_(no notes)_']
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


# --------------------------------------------------------------------------
# restamp
# --------------------------------------------------------------------------

def restamp(src, slides):
    order, members = [], {}
    for s in slides:
        sec = s.section
        if sec is None:
            continue
        if sec not in members:
            order.append(sec)
            members[sec] = []
        members[sec].append(s)
    total = 0.0
    for sec in order:
        group = members[sec]
        timed = [s.minutes for s in group if s.minutes is not None]
        sec_min = sum(timed)
        for i, s in enumerate(group, 1):
            t = s.start_tag
            t = set_attr(t, 'data-section-index', i)
            t = set_attr(t, 'data-section-count', len(group))
            if timed:
                t = set_attr(t, 'data-section-minutes', fmt_minutes(sec_min))
            else:
                t = del_attr(t, 'data-section-minutes')
            if s.minutes is not None:
                t = set_attr(t, 'data-timing', int(round(s.minutes * 60)))
            s.start_tag = t
        total += sec_min
    new = rebuild(src, slides)
    new = re.sub(r'(totalTime:\s*)\d+', lambda m: m.group(1) + str(int(round(total * 60))), new, count=1)
    return new, total


# --------------------------------------------------------------------------
# prettify: re-indent and wrap the <aside class="notes"> blocks
# --------------------------------------------------------------------------
# Only whitespace changes, and only where HTML ignores it: next to block
# tags, and a run of spaces inside text may become a newline + indent. No
# whitespace is added between two things that were touching, tags are
# copied verbatim, and nothing outside the notes is touched -- so the
# speaker view renders the same and extract / check / update see the same
# notes either way. Each rewritten <aside> is verified before it is kept.

DEFAULT_WRAP = 120
INDENT = '  '
WRAPPER_TAGS = {'ul', 'ol', 'dl', 'div', 'table', 'thead', 'tbody', 'tfoot', 'tr',
                'blockquote', 'section', 'figure', 'details'}
TEXT_TAGS = {'li', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'th', 'dt', 'dd',
             'figcaption', 'caption', 'summary'}
VOID_BLOCK_TAGS = {'hr'}
BLOCK_TAGS = WRAPPER_TAGS | TEXT_TAGS | VOID_BLOCK_TAGS
HTML_WS = '[ \t\n\r\f]+'           # HTML whitespace; not \s, which would eat U+00A0
RAW_TEXT_RE = re.compile(r'<(?:pre|textarea|script|style)\b', re.I)
TOKEN_RE = re.compile(r'<!--.*?-->|<(?:[^>"\']|"[^"]*"|\'[^\']*\')*>|[^<]+|<', re.S)
TAGNAME_RE = re.compile(r'<(/?)([A-Za-z][A-Za-z0-9]*)')
BLOCK_EDGE_RE = re.compile(r'(?:%s)?(</?(?:%s)\b[^>]*>)(?:%s)?'
                           % (HTML_WS, '|'.join(sorted(BLOCK_TAGS)), HTML_WS), re.I)


def squash(h):
    """Notes HTML without layout whitespace: equal for a one-line and a prettified <aside>."""
    return BLOCK_EDGE_RE.sub(r'\1', re.sub(HTML_WS, ' ', h or '')).strip(' ')


def pretty_notes(inner, indent, width=DEFAULT_WRAP):
    """Notes <aside> inner HTML -> list of indented, wrapped lines."""
    lines, run = [], []            # run: pieces of the current text line; None = a space
    level = 0
    run_indent = cont_indent = indent

    def ind(n):
        return indent + INDENT * n

    def add(piece):
        nonlocal run_indent, cont_indent
        if not run:
            run_indent = cont_indent = ind(level)
        run.append(piece)

    def flush():
        while run and run[0] is None:
            run.pop(0)
        while run and run[-1] is None:
            run.pop()
        if not run:
            return
        words, cur = [], ''
        for piece in run:          # pieces with no space between them never split
            if piece is None:
                if cur:
                    words.append(cur)
                cur = ''
            else:
                cur += piece
        if cur:
            words.append(cur)
        line = run_indent + words[0]
        for w in words[1:]:
            if len(line) + 1 + len(w) > width:
                lines.append(line)
                line = cont_indent + w
            else:
                line += ' ' + w
        lines.append(line)
        run.clear()

    for tok in TOKEN_RE.findall(inner):
        m = TAGNAME_RE.match(tok)
        name = m.group(2).lower() if m else None
        closing = bool(m and m.group(1))
        if name in WRAPPER_TAGS:
            flush()
            if closing:
                level = max(level - 1, 0)
            lines.append(ind(level) + tok)
            if not closing and not tok.endswith('/>'):
                level += 1
        elif name in TEXT_TAGS:
            if closing:
                level = max(level - 1, 0)
                while run and run[-1] is None:
                    run.pop()
                add(tok)
                flush()
            else:
                flush()
                add(tok)
                level += 1
                cont_indent = ind(level)
        elif name in VOID_BLOCK_TAGS:
            flush()
            lines.append(ind(level) + tok)
        elif tok.startswith('<') and len(tok) > 1:
            add(tok)                # inline tag or comment: part of the text
        else:
            for part in re.split('(%s)' % HTML_WS, tok):
                if not part:
                    continue
                if re.fullmatch(HTML_WS, part):
                    if run and run[-1] is not None:
                        run.append(None)
                else:
                    add(part)
    flush()
    return lines


def _cue_part(inner):
    i = inner.find(SCRIPT_MARK)
    return inner if i < 0 else inner[:i]


def _same_notes(a, b):
    # squash() equal => only ignorable whitespace differs; the Markdown test
    # guards extract / update, which read the cues as text
    return squash(a) == squash(b) and notes_to_md(_cue_part(a)) == notes_to_md(_cue_part(b))


def prettify_deck(src, width=DEFAULT_WRAP):
    """Return (new src, number of <aside> blocks reformatted, ids/positions skipped)."""
    done, skipped = [0], []

    def repl(m):
        inner = m.group(1)
        if not inner.strip() or RAW_TEXT_RE.search(inner):
            return m.group(0)
        line_start = src.rfind('\n', 0, m.start()) + 1
        base = re.match(r'[ \t]*', src[line_start:m.start()]).group(0)
        new_inner = '\n' + '\n'.join(pretty_notes(inner, base + INDENT, width)) + '\n' + base
        if not _same_notes(inner, new_inner):
            skipped.append('line %d' % (src.count('\n', 0, m.start()) + 1))
            return m.group(0)
        if new_inner != inner:
            done[0] += 1
        start_tag = m.group(0)[:m.start(1) - m.start(0)]
        return start_tag + new_inner + '</aside>'

    new = NOTES_RE.sub(repl, src)
    for where in skipped:
        print('warning: notes at %s left as they were (prettify would have changed them)' % where,
              file=sys.stderr)
    return new, done[0], skipped


def maybe_prettify(args, src):
    """Apply prettify when the command was given --prettify."""
    if not getattr(args, 'prettify', False):
        return src
    new, n, _ = prettify_deck(src, args.wrap)
    if n:
        print('prettified notes on %d slides (wrap %d)' % (n, args.wrap))
    return new


def cmd_prettify(args):
    src = Path(args.deck).read_text(encoding='utf-8')
    new, n, skipped = prettify_deck(src, args.wrap)
    if args.dry_run:
        diff = difflib.unified_diff(src.splitlines(), new.splitlines(), 'before', 'after', lineterm='', n=0)
        print('\n'.join(diff))
        print('%d <aside> blocks would change (wrap %d)' % (n, args.wrap))
        return
    if new != src:
        Path(args.deck).write_text(new, encoding='utf-8')
    print('prettified notes on %d slides (wrap %d)%s' % (
        n, args.wrap, '; %d left unchanged' % len(skipped) if skipped else ''))
    sys.exit(1 if skipped else 0)


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def cmd_list(args):
    src, slides = load(args.deck)
    cur, sec_total, grand = None, 0.0, 0.0
    print('%-4s %-34s %6s %6s  %s' % ('#', 'slide', 'min', 'words', 'section'))
    for n, s in enumerate(slides, 1):
        words = len(re.sub(r'<[^>]+>', ' ', s.notes_html or '').split())
        print('%-4d %-34s %6s %6d  %s' % (n, s.id or '?', fmt_minutes(s.minutes) if s.minutes is not None else '-',
                                          words, s.section or ''))
        if s.minutes:
            grand += s.minutes
    by = {}
    for s in slides:
        if s.minutes is not None:
            by[s.section] = by.get(s.section, 0) + s.minutes
    print('\nTimed minutes by section:')
    run = 0.0
    for sec, m in by.items():
        run += m
        print('  %6s  (ends ≈ min %s)  %s' % (fmt_minutes(m), fmt_minutes(run), sec))
    print('  %6s  total' % fmt_minutes(grand))
    tt = re.search(r'totalTime:\s*(\d+)', src)
    if tt:
        print('  reveal totalTime = %s s (%s min)' % (tt.group(1), fmt_minutes(int(tt.group(1)) / 60)))


def cmd_extract(args):
    src, slides = load(args.deck)
    if args.into:
        prep = Path(args.into)
        lines = prep.read_text(encoding='utf-8').splitlines()
        by_id = {s.id: s for s in slides if s.id}
        out, i, n_done = [], 0, 0
        while i < len(lines):
            m = HEAD_RE.match(lines[i].strip())
            if m and m.group('id') in by_id:
                s = by_id[m.group('id')]
                out.append(heading(s) + lines[i].strip()[len(m.group(0)):])
                i += 1
                # skip the old note block (up to the first blank / quote / heading)
                while i < len(lines) and lines[i].strip() and not HEAD_RE.match(lines[i].strip()) \
                        and not lines[i].lstrip().startswith(('>', '#', '|', '---')):
                    i += 1
                out += notes_to_md(s.notes_html)
                n_done += 1
                continue
            out.append(lines[i])
            i += 1
        prep.write_text('\n'.join(out) + '\n', encoding='utf-8')
        print('updated notes for %d slides in %s' % (n_done, prep))
        return
    md = to_markdown(src, slides, args.deck)
    if args.output:
        Path(args.output).write_text(md, encoding='utf-8')
        print('wrote %s (%d slides)' % (args.output, sum(1 for s in slides if s.id)))
    else:
        sys.stdout.write(md)


def cmd_update(args):
    src, slides = load(args.deck)
    notes = parse_md(args.source)
    by_id = {s.id: s for s in slides if s.id}
    unknown = [k for k in notes if k not in by_id]
    changed, retimed = [], []
    for sid, (mins, lines) in notes.items():
        s = by_id.get(sid)
        if s is None:
            continue
        if lines and lines != ['_(no notes)_']:
            inner = md_to_notes(lines)
            if squash(inner) != squash(s.notes_html):
                changed.append(sid)
                set_notes(s, inner)
        if args.apply_minutes and mins is not None and mins != s.minutes:
            retimed.append('%s %s→%s' % (sid, s.minutes, fmt_minutes(mins)))
            s.start_tag = set_attr(s.start_tag, 'data-minutes', fmt_minutes(mins))
    new = rebuild(src, slides)
    if retimed:
        src2, slides2 = new, [Slide(m) for m in SECTION_RE.finditer(new)]
        new, total = restamp(src2, slides2)
        print('retimed: ' + ', '.join(retimed) + ' (talk now %s min)' % fmt_minutes(total))
    new = maybe_prettify(args, new)
    for k in unknown:
        print('warning: %s is not a slide id in %s' % (k, args.deck), file=sys.stderr)
    print('%d slides with new notes%s' % (len(changed), (': ' + ', '.join(changed)) if changed else ''))
    if args.dry_run:
        diff = difflib.unified_diff(src.splitlines(), new.splitlines(), 'before', 'after', lineterm='', n=0)
        print('\n'.join(list(diff)[:400]))
        return
    if new != src:
        Path(args.deck).write_text(new, encoding='utf-8')
        print('wrote %s' % args.deck)


def cmd_restamp(args):
    src, slides = load(args.deck)
    new, total = restamp(src, slides)
    new = maybe_prettify(args, new)
    if new != src:
        Path(args.deck).write_text(new, encoding='utf-8')
    print('restamped %d slides; timed talk = %s min' % (len(slides), fmt_minutes(total)))


def _text(h):
    return re.sub(r'\s+', ' ', BeautifulSoup(h or '', 'html.parser').get_text()).strip()


def parse_scripts(path):
    """Return {slide_id: [paragraph, ...]} from the '> ' quoted lines under each heading."""
    result, cur, paras, buf = {}, None, [], []

    def flush_para():
        t = ' '.join(x.strip() for x in buf).strip()
        if t:
            paras.append(t)
        buf.clear()

    def close():
        flush_para()
        if cur is not None and paras:
            result[cur] = list(paras)
        paras.clear()

    for line in Path(path).read_text(encoding='utf-8').splitlines():
        st = line.strip()
        m = HEAD_RE.match(st)
        if m or st.startswith('#'):
            close()
            cur = m.group('id') if m else None
            continue
        if cur is None:
            continue
        if st.startswith('>'):
            t = st[1:].strip()
            if t:
                buf.append(t)
            else:
                flush_para()
        else:
            flush_para()
    close()
    return result


def script_html(paras):
    out = [SCRIPT_RULE, SCRIPT_BOX, SCRIPT_LABEL]
    for i, para in enumerate(paras):
        h = _inline_html(para)
        h = h.replace('<em>[', '<em style="color:#8a6a1f;">[')   # stage directions
        margin = '0' if i == len(paras) - 1 else '0 0 8px'
        out.append('<p style="margin:%s;">%s</p>' % (margin, h))
    out.append('</div>')
    return ''.join(out)


def cmd_scripts(args):
    src, slides = load(args.deck)
    by_id = {s.id: s for s in slides if s.id}
    done = []
    if args.remove:
        for s in slides:
            if s.script_tail:
                set_notes(s, s.notes_html or '', tail='')
                done.append(s.id)
    else:
        scripts = parse_scripts(args.source)
        for sid, paras in scripts.items():
            s = by_id.get(sid)
            if s is None:
                print('warning: %s is not a slide id' % sid, file=sys.stderr)
                continue
            set_notes(s, s.notes_html or '', tail=script_html(paras))
            done.append(sid)
    new = maybe_prettify(args, rebuild(src, slides))
    if new != src:
        Path(args.deck).write_text(new, encoding='utf-8')
    print('%s scripts on %d slides' % ('removed' if args.remove else 'wrote', len(done)))


def cmd_check(args):
    src, slides = load(args.deck)
    bad = 0
    for s in slides:
        if s.notes_html is None:
            continue
        md1 = notes_to_md(s.notes_html)
        h2 = md_to_notes(md1)
        md2 = notes_to_md(h2)
        if md1 != md2 or _text(squash(s.notes_html)) != _text(squash(h2)):
            bad += 1
            print('✗ %s' % s.id)
            for d in difflib.unified_diff(md1, md2, lineterm='', n=0):
                print('   ' + d)
    missing = [s.id for s in slides if s.notes_html is None]
    print('%d slides, %d with notes, %d without%s; %d round-trip problems' % (
        len(slides), len(slides) - len(missing), len(missing),
        (' (' + ', '.join(missing) + ')') if missing and len(missing) < 15 else '', bad))
    sys.exit(1 if bad else 0)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split('\n\n')[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--deck', default=str(DEFAULT_DECK), help='deck HTML (default: presentation/index.html)')
    sub = p.add_subparsers(dest='cmd', required=True)

    def wrap_opt(sp):
        sp.add_argument('--wrap', type=int, default=DEFAULT_WRAP, metavar='COLS',
                        help='prettify: wrap notes text at COLS columns, indent included '
                             '(default %d)' % DEFAULT_WRAP)

    def pretty_opts(sp):
        sp.add_argument('--prettify', action='store_true',
                        help='re-indent and wrap the notes before writing the deck')
        wrap_opt(sp)

    sub.add_parser('list', help='slides, minutes and note lengths').set_defaults(func=cmd_list)
    e = sub.add_parser('extract', help='notes -> Markdown')
    e.add_argument('-o', '--output', help='write to FILE instead of stdout')
    e.add_argument('--into', metavar='PREP.md', help='rewrite the note bullets inside an existing prep doc')
    e.set_defaults(func=cmd_extract)
    u = sub.add_parser('update', help='Markdown -> notes in the deck')
    u.add_argument('--from', dest='source', required=True, metavar='FILE.md')
    u.add_argument('--apply-minutes', action='store_true', help='also apply "· N min" from headings')
    u.add_argument('--dry-run', action='store_true')
    pretty_opts(u)
    u.set_defaults(func=cmd_update)
    r = sub.add_parser('restamp', help='recompute timing and section attributes')
    pretty_opts(r)
    r.set_defaults(func=cmd_restamp)
    sub.add_parser('check', help='round-trip test of every slide\'s notes').set_defaults(func=cmd_check)
    sc = sub.add_parser('scripts', help='prep-doc spoken scripts -> highlighted block below the cues')
    g = sc.add_mutually_exclusive_group(required=True)
    g.add_argument('--from', dest='source', metavar='PREP.md')
    g.add_argument('--remove', action='store_true')
    pretty_opts(sc)
    sc.set_defaults(func=cmd_scripts)
    pr = sub.add_parser('prettify', help='re-indent and wrap every <aside class="notes"> in place')
    wrap_opt(pr)
    pr.add_argument('--dry-run', action='store_true', help='print the diff instead of writing')
    pr.set_defaults(func=cmd_prettify)
    args = p.parse_args(argv)
    args.func(args)


if __name__ == '__main__':
    main()
