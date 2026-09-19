# GGRU Vitis Seminar — reveal.js deck

A port of the WebSlides seminar deck
([bliptrip/WebSlides @ `ggruvitis_seminar_2026`](https://github.com/bliptrip/WebSlides/tree/ggruvitis_seminar_2026))
onto [reveal.js](https://github.com/hakimel/reveal.js) 6.0.2.

This branch sits on top of unmodified reveal.js history, so upstream releases
still merge cleanly:

```bash
git fetch upstream && git merge upstream/master
```

The WebSlides deck is untouched and remains the reference copy. Content is
identical — same 78 slides, same speaker notes, same minute budgets, same
figures. What changed is the framework underneath, and the port is mechanical
and repeatable rather than a rewrite (see [Regenerating](#regenerating)).

## Running it

```bash
python3 -m http.server 8000
# http://localhost:8000/presentation/
```

Serve it — do not open the file directly. The mermaid diagrams need a real
origin, and so does the speaker view.

`s` opens the speaker view · `o` the overview grid · `f` fullscreen ·
`b` black the audience screen · `h` pins the section name.
Everything else is in [`PRESENTER.md`](PRESENTER.md).

## The media is not in this repository

Same policy as the WebSlides branch, and for the same reason: the seminar's
figures and videos come to ~826 MB, two of the videos are over 50 MB, and git
would carry all of it forever. `static/images/` and `static/videos/` are
gitignored.

The port deliberately keeps the **identical asset paths**, so:

```bash
cp -r /path/to/WebSlides/static/images  static/
cp -r /path/to/WebSlides/static/videos  static/
```

and every one of the 51 references resolves. Nothing to rewrite.

To review the deck *before* doing that, generate labelled stand-ins:

```bash
python3 tools/make-placeholders.py           # grey boxes captioned with the filename
python3 tools/make-placeholders.py --clean   # remove them once the real media is in
```

Placeholders are gitignored and never overwrite a real file.

## What changed, and what didn't

| WebSlides | reveal.js | Notes |
|---|---|---|
| `<aside class="notes">` | `<aside class="notes">` | Identical markup. All 56 notes carried over untouched. |
| `presenter.js` (`p`) | built-in speaker view (`s`) | Notes, next-slide preview, talk clock and pacing are all native. |
| `data-minutes="1.5"` | `data-timing="90"` + `data-minutes` | Both kept. reveal reads seconds; the original attribute stays for reference. |
| `<ws-section name= minutes=>` | `data-section*` on every slide | reveal has no sections. `plugin/seminar` rebuilds them. |
| section countdown | `plugin/seminar` | Injected into the speaker view. Same green/amber/red thresholds. |
| slide grid (`-`) | overview (`o`) | Native. |
| outline (`o`) | `#/slide-id` links | Every slide now has a stable id from its old `slide_name`. |
| `#slide=24` anchors | `#/populations-map` | Renumbering no longer breaks a link. |
| `wsOverflowingSlides()` | `revealOverflowingSlides()` | See below — this one gets meaningfully better. |
| `wsTimings()` | `revealTimings()` | Same rehearsal report. |
| `webslides.css` | `webslides.css` | **Unchanged, still doing the work.** See below. |

### WebSlides' stylesheet is still the theme

No reveal theme is loaded. `presentation/css/webslides.css` is upstream
WebSlides, unmodified, and it still owns everything inside a slide: the
typography scale, `.wrap` / `.grid` / `.column`, `.card-50`, `.bg-apple`, the
`.background` / `.dark` / `.ddark` overlays — including the overlay opacities
tuned on 9 Sep, which keep their exact values.

`presentation/css/webslides-compat.css` is the treaty between the two
frameworks. reveal owns the *deck* (which slide, transitions, scaling, speaker
view); WebSlides owns the *slide*. The shim stops each from reaching into the
other's territory and is commented rule by rule.

### Browser zoom stopped mattering

The old pre-flight checklist opened with ⌘0 in both windows, because WebSlides
is fluid — a section *was* the viewport, so at 133% zoom the deck went from 5
overflowing slides to 10.

reveal lays slides out at a fixed logical 1920×1080 and scales the whole thing
with a transform to fit whatever it is projected onto. Zoom level, display
resolution and the Pavilion's scaling mode no longer change what fits. Overflow
is now a property of the deck rather than of the machine showing it: run
`revealOverflowingSlides()` once, fix what it lists, and it stays fixed.

The one consequence is that `vh` units had to move. Inside a scaled slide a raw
`vh` still measures the browser window, so the converter rewrites `58vh` to
`calc(58 * var(--wsvh))`, where `--wsvh` is one hundredth of the slide box.
Same number, correct frame of reference.

## Layout

```
presentation/
  index.html                  the deck — generated, see below
  css/
    webslides.css             upstream WebSlides (MIT), unmodified
    extend.css, mermaid.css, svg-icons.css   carried over unchanged
    webslides-compat.css      hand-written: the WebSlides/reveal treaty
    seminar.css               generated: the deck's old inline <style> block
plugin/seminar/seminar.js     sections, section countdown, rehearsal helpers
tools/
  ws2reveal.py                the converter
  make-placeholders.py        stand-in figures
static/                       media (gitignored) + favicons (tracked)
dist/, plugin/, js/, ...      upstream reveal.js, untouched
```

Hand-written: `webslides-compat.css`, `plugin/seminar/seminar.js`, the two
tools, and this file. Generated: `presentation/index.html` and
`presentation/css/seminar.css`. Everything else is upstream.

## Regenerating

The port is a script, not a one-off edit, so the WebSlides deck can keep being
the place you write slides if you want it to be:

```bash
python3 tools/ws2reveal.py \
    --src   ../WebSlides/presentation/presentation.html \
    --out   presentation/index.html \
    --style presentation/css/seminar.css
```

It reports what it did — slide count, notes, budgets, sections — so a
regression in the source deck shows up immediately:

```
ws2reveal: 78 slides -> presentation/index.html
           56 with speaker notes, 47 with a time budget, 78 with stable ids
           8 sections:
               3 slides     3 min  A. Opening
               3 slides     4 min  B. Cranberry as a model system
              11 slides     9 min  C. Meta-QTL synthesis — Maule et al. 2024 + Clare et al. 2026
              13 slides    11 min  D. UAV phenomics & the LMI — under review
               7 slides     7 min  E. Genetics of the LMI — in preparation
               7 slides     9 min  F. Vision for GGRU
               3 slides     2 min  G. Close
              31 slides     ? min  Backup — Q&A
```

Do not hand-edit `index.html` or `seminar.css` unless you have decided to stop
regenerating them. Edit `webslides-compat.css` freely — it is not generated.

Note that the seven lettered blocks total 47 slides here, not the 45 the
WebSlides README quotes; the counts drifted during the 9 Sep restructure. The
minute budgets are unchanged and still sum to 45.

## Known gaps

- **Not yet rendered against the real figures.** The port was validated
  structurally (78 slides, 56 notes, 47 budgets, all non-media references
  resolving) and with a headless run confirming reveal initialises and the
  section model reports correctly. It has not been looked at with the actual
  826 MB of media in place. Do that before the talk, and run
  `revealOverflowingSlides()`.
- **The speaker-view section panel is an injection.** reveal's notes plugin
  keeps its window handle private, so `plugin/seminar` captures it at
  `window.open` time. Every branch fails soft — if reveal's internals change,
  the deck and the stock speaker view keep working and only the section panel
  goes missing. Worth a glance after any reveal upgrade.
- **Background videos keep WebSlides' stretched framing.** `object-fit: cover`
  only applied under `.fullscreen` in WebSlides, and that behaviour was
  preserved deliberately rather than quietly improved.

## Credits and licensing

- [reveal.js](https://github.com/hakimel/reveal.js) — Hakim El Hattab, MIT.
- [WebSlides](https://github.com/webslides/WebSlides) — José Luis Antúnez, MIT.
  `presentation/css/webslides.css` is redistributed here unmodified under that
  licence.

Both licences permit this; the reveal.js `LICENSE` at the repository root is
upstream's.
