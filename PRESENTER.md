# Running the talk

The reveal.js successor to `PRESENTER-README.md` on the WebSlides branch.

Most of what `presenter.js` provided by hand is native here, so this is a
shorter document than its predecessor. The one thing reveal has no concept of
is a **section**, and this deck is built on seven of them, so
`plugin/seminar/seminar.js` adds those back and nothing else.

## Pre-flight

1. **Serve it.** `python3 -m http.server 8000`, then
   `http://localhost:8000/presentation/`. Not `file://` — mermaid and the
   speaker view both need a real origin.
2. **Check the media is in place.** `static/images/` and `static/videos/` are
   gitignored; a fresh clone has neither. If you see grey captioned boxes,
   those are placeholders from `tools/make-placeholders.py`, not the figures.
3. **`revealOverflowingSlides()`** in the console. Content past the bottom of
   the slide box is invisible to the room. Unlike the WebSlides version this
   only needs running once — the result no longer depends on zoom or on which
   display you are using.
4. Fullscreen on the projector (`f`), share **Screen** in Teams (not Window —
   macOS fullscreen windows share unreliably). Speaker view stays on the
   MacBook.

**No ⌘0 step.** That is gone. reveal scales the deck to the display, so
browser zoom and the Pavilion's resolution setting no longer change what fits.

## Starting

1. Open the deck, press **s**. The speaker view opens in a second window.
2. Drag the *original* window to the projector, click it, press **f**.
3. Drive everything from the speaker window.

The talk clock starts by itself the first time you leave slide 1.

## Keys

| Key | |
|---|---|
| `→` `space` `PgDn` | next slide |
| `←` `PgUp` | previous |
| `s` | speaker view |
| `o` or `Esc` | overview grid — click a tile to jump |
| `f` | fullscreen — press on the *audience* window |
| `b` or `.` | black the audience screen |
| `h` | pin the section name on the audience screen (off by default) |
| `g` then a number | jump to slide |
| `?` | reveal's own shortcut list |

Every slide also has a stable id, so `#/frost`, `#/populations-map`,
`#/vision-headline` all work as anchors — a table-of-contents slide is just a
list of those links, and renumbering the deck never breaks one.

## Reading the speaker view

Top half is reveal's: current slide, next slide, talk clock, and a pacing
readout driven by `totalTime: 2700` and the per-slide `data-timing` budgets
the converter derived from `data-minutes`.

Below it, the **Section** panel added by `plugin/seminar`:

```
SECTION
D. UAV phenomics & the LMI — under review
  6:41   left of 11:00   slide 4 of 13 in this block
  ▓▓▓▓▓▓░░░░░░░░░░
  Next slide opens: E. Genetics of the LMI — in preparation  (7 min)
```

- The countdown is **green**, **amber** under 25% remaining, **red** and
  negative once over — the same thresholds `presenter.js` used.
- Section time accrues per slide and is summed over the section, so jumping
  back to re-explain something charges the section correctly.
- The amber line only appears when the *next* slide crosses into a new block,
  so a transition never arrives unannounced.
- Blocks without a budget — the 31 backup slides — show elapsed time instead
  of a countdown.

## While rehearsing

`revealTimings()` in the console returns where the time actually went: slide
number, id, section, title, time spent, budget, and how far over. Run it after
a practice pass to find the slide that ate four minutes.

`revealOverflowingSlides()` lists any slide whose content is taller than the
1080px slide box, with how much is hanging off the bottom.

Both are defined on the deck window and mirrored onto the speaker window,
since that is where you actually have a console open during rehearsal.

## Backup slides

The 31 backup slides are a section like any other, at the end. They carry no
minute budget, so the section panel shows elapsed rather than remaining time.

During Q&A, `o` for the overview and click, or type the slide's id into the
URL. The overview is the faster of the two once you have seen the grid once.

## Exporting a PDF

Append `?print-pdf` to the URL and print to PDF from Chrome:

```
http://localhost:8000/presentation/?print-pdf
```

Set margins to None and enable background graphics. Speaker notes are excluded
by default; add `showNotes: true` to the config if you want them on the export.

## If something looks wrong

- **Blank or unstyled slides** — `webslides-1920.css` failed to load. Check the
  console; the deck depends on it for all in-slide typography and layout.
- **Notes visible on the projector** — should be impossible (they are hidden
  in `webslides-compat.css` with `!important`), but if it happens, stop
  sharing and check that file loaded.
- **A mermaid diagram is blank** — they render lazily on first visit to their
  slide, and need a served origin. Visit the slide once before going live.
- **The section panel is missing but the rest of the speaker view works** —
  the injection in `plugin/seminar/seminar.js` failed, probably after a
  reveal.js upgrade. Everything else, including notes and pacing, is
  unaffected; the panel is additive.
