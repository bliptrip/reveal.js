#!/usr/bin/env python3
"""
ws2reveal.py -- convert the GGRU WebSlides deck into a reveal.js deck.

This is a mechanical port, not a rewrite. Slide *bodies* are carried across
untouched; what changes is the wrapper, the slide-level attributes and the
handful of CSS units that do not survive reveal's fixed-size scaled layout.

Run it again whenever the WebSlides deck changes upstream:

    python3 tools/ws2reveal.py \
        --src   ../WebSlides/presentation/presentation.html \
        --out   presentation/index.html \
        --style presentation/css/seminar.css

What it does, in order:

1.  Lifts the deck-specific <style> block out of <head> into its own
    stylesheet (seminar.css) so the deck HTML stays readable.
2.  Flattens <ws-section name= minutes=> wrappers, stamping every slide with
    data-section / data-section-minutes / data-section-index /
    data-section-count. reveal has no notion of sections; plugin/seminar
    rebuilds one from these attributes.
3.  Translates data-minutes="1.5" into reveal's native data-timing="90"
    (seconds), so the built-in speaker view's pacing display works without
    any custom code.
4.  Turns slide_name="foo" into id="foo", which gives every slide a stable
    #/foo URL. This replaces WebSlides' #slide=N anchors and is strictly
    better: renumbering the deck no longer breaks a link.
5.  Rewrites vh/vw units to calc() against reveal's --slide-height /
    --slide-width custom properties. This is the one change that is not
    cosmetic -- see the comment on VH_RE below.
6.  Emits the reveal scaffold: <div class="reveal"><div class="slides">.

Speaker notes (<aside class="notes">) need no conversion at all -- WebSlides'
presenter.js and reveal.js happen to use the identical markup.
"""

import argparse
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Viewport units
# ---------------------------------------------------------------------------
# WebSlides is a fluid framework: a section is min-height:100vh and the deck
# is sized by the browser window, which is why the original deck's pre-flight
# checklist is so anxious about browser zoom (at 133% the deck went from 5
# overflowing slides to 10).
#
# reveal.js works the opposite way: slides are laid out at a fixed logical
# size (here 1920x1080) and the whole thing is scaled with a CSS transform to
# fit whatever it is projected onto. That is a real improvement for this deck
# -- zoom level and display resolution stop mattering -- but it breaks every
# vh/vw unit, because those still resolve against the *real* viewport rather
# than the 1920x1080 slide box.
#
# reveal publishes the slide box as --slide-width / --slide-height on the
# viewport element, so 58vh becomes calc(58 * var(--wsvh)) where --wsvh is one
# hundredth of the slide height. Same number, right reference frame.
VH_RE = re.compile(r"(?<![\w.-])(\d+(?:\.\d+)?)vh\b")
VW_RE = re.compile(r"(?<![\w.-])(\d+(?:\.\d+)?)vw\b")


def fix_viewport_units(text: str) -> str:
    """Rewrite Nvh/Nvw to calc() against reveal's slide-box custom properties."""
    if not text:
        return text
    text = VH_RE.sub(lambda m: f"calc({m.group(1)} * var(--wsvh))", text)
    text = VW_RE.sub(lambda m: f"calc({m.group(1)} * var(--wsvw))", text)
    return text


# ---------------------------------------------------------------------------
# Slide-level conversion
# ---------------------------------------------------------------------------

def minutes_to_seconds(value: str):
    """data-minutes='1.5' -> 90. Returns None if unparseable."""
    try:
        return int(round(float(value) * 60))
    except (TypeError, ValueError):
        return None


def slugify(name: str) -> str:
    """slide_name -> a valid, URL-safe HTML id."""
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", name.strip()).strip("-")
    if not slug or not re.match(r"^[A-Za-z]", slug):
        slug = "s-" + slug
    return slug.lower()


def collect_slides(article):
    """
    Walk the WebSlides <article id="webslides"> and return a flat list of
    (section_tag, section_name, section_minutes) in document order.

    <ws-section> wrappers group consecutive slides; slides outside any wrapper
    belong to no section. This mirrors presenter.js's wrapper form. The
    attribute form (data-section on the slide itself) is honoured too, so a
    deck that mixes both converts correctly.
    """
    slides = []
    for child in article.find_all(["ws-section", "section"], recursive=False):
        if child.name == "ws-section":
            name = child.get("name", "").strip()
            minutes = child.get("minutes", "").strip()
            for sec in child.find_all("section", recursive=False):
                slides.append((sec, name, minutes))
        else:
            slides.append(
                (
                    child,
                    child.get("data-section", "").strip(),
                    child.get("data-section-minutes", "").strip(),
                )
            )
    return slides


def convert_slide(sec, name, minutes, index_in_section, count_in_section, seen_ids):
    """Rewrite one WebSlides <section> in place into a reveal slide."""

    # -- per-slide budget -> reveal's native pacing attribute ---------------
    if sec.has_attr("data-minutes"):
        seconds = minutes_to_seconds(sec["data-minutes"])
        if seconds is not None:
            sec["data-timing"] = str(seconds)

    # -- section membership, denormalised onto every slide ------------------
    # presenter.js carried section state forward at runtime. Stamping it on
    # each slide instead means the plugin needs no ordering assumptions and a
    # slide keeps its section if the deck is ever reordered.
    if name:
        sec["data-section"] = name
        if minutes:
            sec["data-section-minutes"] = minutes
        sec["data-section-index"] = str(index_in_section)
        sec["data-section-count"] = str(count_in_section)

    # -- slide_name -> id, for stable #/slide-name deep links ---------------
    if sec.has_attr("slide_name"):
        slug = slugify(sec["slide_name"])
        original = slug
        bump = 2
        while slug in seen_ids:           # ids must be unique; the source deck
            slug = f"{original}-{bump}"   # reuses a couple of slide_names
            bump += 1
        seen_ids.add(slug)
        sec["id"] = slug
        del sec["slide_name"]

    # -- WebSlides' .slide-name is a JS hook, not a style; drop it ----------
    classes = sec.get("class", [])
    classes = [c for c in classes if c != "slide-name"]
    if classes:
        sec["class"] = classes
    elif sec.has_attr("class"):
        del sec["class"]

    # -- viewport units inside inline styles --------------------------------
    for el in [sec] + sec.find_all(style=True):
        if el.has_attr("style"):
            el["style"] = fix_viewport_units(el["style"])

    return sec


# ---------------------------------------------------------------------------
# Output scaffold
# ---------------------------------------------------------------------------

HEAD = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{title}</title>
    <meta name="description" content="{description}">

    <!-- Google Fonts: unchanged from the WebSlides deck -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,700,700i%7CMaitree:200,300,400,600,700&amp;subset=latin-ext" rel="stylesheet">

    <!-- reveal.js core. No theme is loaded: WebSlides' own stylesheet is the
         theme, and a reveal theme would fight it for every heading. -->
    <link rel="stylesheet" href="../dist/reveal.css">

    <!-- WebSlides' stylesheet (MIT), with its @media queries evaluated at the
         deck's logical 1920x1080 by tools/bake-webslides.py. This is what
         makes the port a port: .wrap, .grid, .column, .card-50, .bg-apple,
         the typography scale and the background/overlay classes all still
         mean what they meant -- and mean it regardless of window size, which
         the un-baked upstream file (css/webslides.css, kept for reference)
         could not, because reveal scales slides with a transform that media
         queries never see. -->
    <link rel="stylesheet" href="css/webslides-1920.css">
    <link rel="stylesheet" href="css/svg-icons.css">
    <link rel="stylesheet" href="css/mermaid.css">
    <link rel="stylesheet" href="css/extend.css">

    <!-- The shim: neutralises the parts of WebSlides that assume it owns the
         page, and re-establishes them inside a reveal slide. Must come after
         webslides-1920.css. -->
    <link rel="stylesheet" href="css/webslides-compat.css">

    <!-- Deck-specific styles, lifted verbatim out of the WebSlides deck's
         inline <style> block by tools/ws2reveal.py. -->
    <link rel="stylesheet" href="css/seminar.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.0/css/all.min.css" integrity="sha512-DxV+EoADOkOygM4IR9yXP8Sb2qwgidEmeqAEmDKIOfPRQZOWbXCzLC6vjbZyy0vPisbH2SyW27+ddLVCN+OMzQ==" crossorigin="anonymous" referrerpolicy="no-referrer">

    <link rel="shortcut icon" sizes="16x16" href="../static/images/favicons/favicon.png">
    <link rel="shortcut icon" sizes="32x32" href="../static/images/favicons/favicon-32.png">
    <link rel="apple-touch-icon icon" sizes="180x180" href="../static/images/favicons/favicon-180.png">
    <meta name="theme-color" content="#333333">
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
"""

TAIL = """      </div>
    </div>

    <script src="../dist/reveal.js"></script>
    <script src="../dist/plugin/notes.js"></script>
    <script src="../dist/plugin/zoom.js"></script>
    <script src="../plugin/seminar/seminar.js"></script>
    <script>
      Reveal.initialize({{
        // The WebSlides deck was written for a 1920x1080 projector and its
        // type scale assumes it (1rem = 10px, h1 = 7.2rem = 72px). Declaring
        // that as the logical slide size lets reveal scale the whole deck to
        // any display -- which is what retires the deck's old browser-zoom
        // pre-flight step.
        width: 1920,
        height: 1080,
        margin: 0,
        minScale: 0.2,
        maxScale: 2.0,

        // WebSlides sections centre their own content with flexbox
        // (justify-content:center, plus .slide-top / .slide-bottom to
        // override). reveal's centring would fight that, so it stays off.
        center: false,

        // reveal writes the display value inline on every slide it shows,
        // and its default 'block' would beat WebSlides' `section {
        // display: flex }` from any stylesheet. Flex is what makes the
        // vertical centring, .slide-top and .slide-bottom work at all.
        display: 'flex',

        hash: true,
        slideNumber: 'c/t',
        transition: 'slide',
        backgroundTransition: 'fade',

        // Total talk length and the per-slide budgets converted from
        // data-minutes. Drives the pacing readout in the speaker view.
        totalTime: {total_seconds},

        plugins: [ RevealNotes, RevealZoom, RevealSeminar ]
      }});
    </script>

    <!-- Font Awesome (SVG-with-JS build), as in the WebSlides deck -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.0/js/all.min.js" integrity="sha512-gBYquPLlR76UWqCwD06/xwal4so02RjIR0oyG1TIhSGwmBTRrIkQbaPehPF8iwuY9jFikDHMGEelt0DtY7jtvQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <!-- Mermaid. The WebSlides version watched for a 'current' class with a
         MutationObserver; reveal fires real events, so this listens for those
         instead. Diagrams render lazily, on first visit to their slide. -->
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.10.1/+esm';
      mermaid.initialize({{
        startOnLoad: false,
        themeVariables: {{
          fontFamily: "'Roboto', helvetica, arial, sans-serif",
          fontSize: "28px"
        }}
      }});

      function unescapeHtmlWithParser(escapedHtml) {{
        const parser = new DOMParser();
        const doc = parser.parseFromString(escapedHtml, 'text/html');
        return doc.documentElement.textContent;
      }}

      let counter = 0;
      async function renderMermaidIn(slide) {{
        if (!slide) return;
        for (const el of slide.querySelectorAll('.mermaid')) {{
          if (el.querySelector('svg')) continue;   // already rendered
          const source = unescapeHtmlWithParser(el.innerHTML);
          try {{
            const {{ svg }} = await mermaid.render('mmd-' + (counter++), source);
            el.innerHTML = svg;
            Reveal.layout();
          }} catch (err) {{
            console.error('mermaid render failed:', err);
          }}
        }}
      }}

      Reveal.on('ready',        e => renderMermaidIn(e.currentSlide));
      Reveal.on('slidechanged', e => renderMermaidIn(e.currentSlide));
      // The speaker view's preview iframe and the overview both want the
      // diagram present before the slide is "current".
      Reveal.on('overviewshown', () => {{
        Reveal.getSlides().forEach(renderMermaidIn);
      }});
    </script>
  </body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="WebSlides presentation.html")
    ap.add_argument("--out", required=True, help="reveal.js index.html to write")
    ap.add_argument("--style", required=True, help="where to write the lifted <style> block")
    ap.add_argument("--total-minutes", type=float, default=45.0,
                    help="talk length for the speaker view's pacing bar (default 45)")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_file():
        sys.exit(f"ws2reveal: no such file: {src}")

    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")

    article = soup.find(id="webslides")
    if article is None:
        sys.exit("ws2reveal: could not find <article id='webslides'> in the source deck")

    title = soup.title.get_text(strip=True) if soup.title else "Seminar"
    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "") if desc_tag else ""

    # -- 1. lift the deck-specific <style> block ----------------------------
    style_blocks = [s.get_text() for s in soup.head.find_all("style")] if soup.head else []
    lifted = "\n\n".join(style_blocks).strip()
    style_out = Path(args.style)
    style_out.parent.mkdir(parents=True, exist_ok=True)
    style_out.write_text(
        "/* ------------------------------------------------------------------\n"
        " * seminar.css -- deck-specific styles.\n"
        " *\n"
        " * Lifted verbatim from the inline <style> block of the WebSlides deck\n"
        " * by tools/ws2reveal.py, with one systematic change: vh/vw units are\n"
        " * rewritten to calc() against reveal's --slide-height / --slide-width,\n"
        " * because inside a scaled reveal slide a raw vh still measures the\n"
        " * browser window rather than the 1920x1080 slide box.\n"
        " *\n"
        " * Regenerate rather than hand-edit, unless you have also updated the\n"
        " * WebSlides source deck.\n"
        " * ------------------------------------------------------------------ */\n\n"
        + fix_viewport_units(lifted)
        + "\n",
        encoding="utf-8",
    )

    # -- 2..5. convert the slides -------------------------------------------
    entries = collect_slides(article)

    # how many slides in each named section, for "slide 3 of 10 in this section"
    counts = {}
    for _, name, _m in entries:
        if name:
            counts[name] = counts.get(name, 0) + 1

    seen_ids = set()
    running = {}
    out_slides = []
    for sec, name, minutes in entries:
        if name:
            running[name] = running.get(name, 0) + 1
            idx, total = running[name], counts[name]
        else:
            idx, total = 0, 0
        out_slides.append(
            convert_slide(sec, name, minutes, idx, total, seen_ids)
        )

    # -- 6. emit -------------------------------------------------------------
    body = "\n\n".join(str(s) for s in out_slides)
    # indent the slide markup two levels to sit inside .reveal > .slides
    body = "\n".join(("        " + line) if line.strip() else line
                     for line in body.splitlines())

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        HEAD.format(title=title, description=description)
        + body
        + "\n"
        + TAIL.format(total_seconds=int(round(args.total_minutes * 60))),
        encoding="utf-8",
    )

    # -- report --------------------------------------------------------------
    n_notes = sum(1 for s in out_slides if s.find("aside", class_="notes"))
    n_timed = sum(1 for s in out_slides if s.has_attr("data-timing"))
    n_ids = sum(1 for s in out_slides if s.has_attr("id"))
    sections = list(counts.items())

    print(f"ws2reveal: {len(out_slides)} slides -> {out}")
    print(f"           {n_notes} with speaker notes, {n_timed} with a time budget, "
          f"{n_ids} with stable ids")
    print(f"           {len(sections)} sections:")
    for name, n in sections:
        mins = next((m for _s, nm, m in entries if nm == name and m), "?")
        print(f"             {n:>3} slides  {mins:>4} min  {name}")
    print(f"           styles -> {style_out}")


if __name__ == "__main__":
    main()
