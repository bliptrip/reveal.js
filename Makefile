# Makefile -- speaker-notes workflow for the TPGRDRU coffee seminar deck.
#
# Every target is a thin wrapper around tools/speaker_notes.py. The deck is
# edited as text: only the <aside class="notes"> blocks (and, for timing
# targets, the <section> timing attributes and reveal's totalTime) change.
#
# Three kinds of notes live in this folder:
#
#   CUES     short bullets in each slide's <aside class="notes"> (the lines
#            shown first in the speaker view, `s` in the browser). In the
#            prep doc they are the "- " lines directly under each
#            **[`slide-id`](...)** · N min heading, up to the first blank line.
#   SCRIPTS  the full spoken paragraphs -- the "> " quoted lines under each
#            heading in the prep doc. In the deck they sit below the cues,
#            after a dashed amber rule, in an amber box labelled FULL SCRIPT.
#            list / extract / check ignore them; update keeps them.
#   MINUTES  per-slide timing: data-minutes on each <section>, and "· N min"
#            on each prep-doc heading. restamp derives data-timing,
#            data-section-* and reveal's totalTime from data-minutes.
#
# The prep doc is the usual source of truth: edit it, then `make sync`.
# Nothing here commits to git; `git diff` shows what a target changed and
# `git checkout -- <file>` undoes it.
#
# Override any variable on the command line, e.g.
#   make list DECK=../other/presentation/index.html
#   make notes-md NOTES_MD=/tmp/notes.md

PYTHON   ?= python3
TOOL     := tools/speaker_notes.py
DECK     ?= presentation/index.html
PREP     ?= TPGRDRU_Seminar_Prep.md
NOTES_MD ?= Speaker_Notes.md

SN := $(PYTHON) $(TOOL) --deck $(DECK)

.DEFAULT_GOAL := help
.PHONY: help list check \
        notes-md notes-to-prep \
        prep-to-deck-dry prep-to-deck prep-to-deck-minutes md-to-deck \
        scripts scripts-remove restamp sync

## help: print this list of targets
help:
	@echo "Speaker-notes targets (DECK=$(DECK)  PREP=$(PREP)  NOTES_MD=$(NOTES_MD))"
	@grep -E '^## ' $(MAKEFILE_LIST) | sed -e 's/^## /  make /' -e 's/: /\t/' | expand -t 30

# ---------------------------------------------------------------------------
# Read-only
# ---------------------------------------------------------------------------

## list: slides, minutes, cue word counts, section end-times (read-only)
#   in:  $(DECK)
#   out: table on stdout. Writes nothing.
list:
	$(SN) list

## check: cue round-trip test HTML -> Markdown -> HTML (read-only)
#   in:  $(DECK)
#   out: report on stdout; exits non-zero if any slide's cues would not
#        survive an extract/update round-trip. Writes nothing.
check:
	$(SN) check

## prep-to-deck-dry: preview prep-to-deck as a diff (read-only)
#   in:  $(PREP) cue lines and "· N min" headings, $(DECK)
#   out: unified diff on stdout of what prep-to-deck-minutes would change.
#        Writes nothing.
prep-to-deck-dry:
	$(SN) update --from $(PREP) --apply-minutes --dry-run

# ---------------------------------------------------------------------------
# Deck -> Markdown
# ---------------------------------------------------------------------------

## notes-md: dump every slide's cues to $(NOTES_MD)
#   in:  $(DECK)
#   out: OVERWRITES $(NOTES_MD) (default Speaker_Notes.md) with one heading +
#        cue bullets per slide, grouped by section. Scripts are not included.
#        Edit it and bring it back with `make md-to-deck`.
notes-md:
	$(SN) extract -o $(NOTES_MD)

## notes-to-prep: copy the deck's cues (and minutes) into the prep doc
#   in:  $(DECK)
#   out: REWRITES $(PREP) in place -- for every slide heading already in the
#        prep doc, the heading's "· N min" and the cue bullets under it are
#        replaced from the deck. Scripts ("> " lines), tables and all other
#        text are left alone. Slides with no heading in the prep doc are
#        skipped (add the heading first). Use after editing notes in the deck.
notes-to-prep:
	$(SN) extract --into $(PREP)

# ---------------------------------------------------------------------------
# Markdown -> deck
# ---------------------------------------------------------------------------

## prep-to-deck: copy the prep doc's cue bullets into the deck
#   in:  $(PREP) (cue lines under each slide heading)
#   out: REWRITES $(DECK) in place -- the cue part of each <aside> for every
#        slide that has cue lines in the prep doc. Slides not in the prep doc
#        keep their cues; every slide keeps its FULL SCRIPT box and minutes.
prep-to-deck:
	$(SN) update --from $(PREP)

## prep-to-deck-minutes: as prep-to-deck, and apply the prep doc's minutes
#   in:  $(PREP) cue lines and "· N min" headings
#   out: REWRITES $(DECK) in place -- cues as above, data-minutes from the
#        headings, then a restamp (data-timing, data-section-*, totalTime).
prep-to-deck-minutes:
	$(SN) update --from $(PREP) --apply-minutes

## md-to-deck: copy cues from $(NOTES_MD) into the deck
#   in:  $(NOTES_MD) (made by `make notes-md`, then edited)
#   out: REWRITES $(DECK) in place -- cues of the slides listed in
#        $(NOTES_MD); scripts and minutes unchanged.
md-to-deck:
	$(SN) update --from $(NOTES_MD)

## scripts: copy the prep doc's spoken scripts into the deck (FULL SCRIPT box)
#   in:  $(PREP) "> " quoted lines under each slide heading
#   out: REWRITES $(DECK) in place -- replaces (or adds) the dashed rule +
#        amber FULL SCRIPT box after the cues of every slide that has a script
#        in the prep doc. Cues and minutes unchanged. Safe to rerun.
scripts:
	$(SN) scripts --from $(PREP)

## scripts-remove: strip every FULL SCRIPT box from the deck
#   in:  $(DECK)
#   out: REWRITES $(DECK) in place -- cues only, as before the scripts were
#        added. `make scripts` puts them back.
scripts-remove:
	$(SN) scripts --remove

# ---------------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------------

## restamp: recompute timing attributes from data-minutes
#   in:  $(DECK) data-minutes on each <section>
#   out: REWRITES $(DECK) in place -- data-timing, data-section-index,
#        data-section-count, data-section-minutes and reveal's totalTime.
#        Run after adding, removing, moving or retiming slides by hand.
restamp:
	$(SN) restamp

# ---------------------------------------------------------------------------
# Everyday
# ---------------------------------------------------------------------------

## sync: prep doc -> deck (cues, minutes, scripts), then check
#   in:  $(PREP)
#   out: REWRITES $(DECK) in place (prep-to-deck-minutes, then scripts), then
#        runs check. $(PREP) is not modified. The one to run after editing
#        the prep doc.
sync: prep-to-deck-minutes scripts check
