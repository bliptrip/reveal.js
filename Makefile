# Makefile -- speaker-notes workflow for a reveal.js seminar deck.
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
# Layout of the notes: with PRETTIFY=1 (the default) every target that
# writes the deck re-indents each <aside class="notes"> one block element per
# line and wraps its text at NOTES_WRAP columns (default 120, indent
# included). Only whitespace HTML ignores changes, so the speaker view and
# the Markdown targets see the same notes either way. PRETTIFY=0 writes
# changed <aside> blocks on one line, as the tool did before; `make prettify`
# reformats the whole deck on demand.
#
# The prep doc is the usual source of truth: edit it, then `make sync`.
# Nothing here commits to git; `git diff` shows what a target changed and
# `git checkout -- <file>` undoes it.
#
# Override any variable on the command line, e.g.
#   make list DECK=../other/presentation/index.html
#   make notes-md NOTES_MD=/tmp/notes.md
#   make sync NOTES_WRAP=100        make prep-to-deck PRETTIFY=0
#   make upload REMOTE=me@otherhost RPATH=/srv/talks/

PYTHON   ?= python3
TOOL     := tools/speaker_notes.py
DECK     ?= presentation/index.html
PREP     ?= $(firstword $(wildcard *_Prep.md))
NOTES_MD ?= Speaker_Notes.md

# Notes layout (see above). PRETTIFY: 1/yes/true = on; anything else = off.
PRETTIFY   ?= 1
NOTES_WRAP ?= 120

SN     := $(PYTHON) $(TOOL) --deck $(DECK)
PRETTY := $(if $(filter 1 yes true,$(PRETTIFY)),--prettify --wrap $(NOTES_WRAP))

# Upload (see the Upload section at the end)
RSYNC         ?= rsync
REMOTE        ?= andrew@amanita.walnut.casa
RPATH         ?= /data/andrew/
RSYNC_FLAGS   ?= -av --partial --progress --delete
RSYNC_EXCLUDE ?= .git/ node_modules/ .DS_Store __pycache__/ .idea/

.DEFAULT_GOAL := help
.PHONY: help list check \
        notes-md notes-to-prep \
        prep-to-deck-dry prep-to-deck prep-to-deck-minutes md-to-deck \
        scripts scripts-remove restamp prettify prettify-dry sync \
        upload upload-dry

## help: print this list of targets
help:
	@echo "Speaker-notes targets (DECK=$(DECK)  PREP=$(PREP)  NOTES_MD=$(NOTES_MD))"
	@echo "  notes layout: PRETTIFY=$(PRETTIFY)  NOTES_WRAP=$(NOTES_WRAP)"
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
#   out: unified diff on stdout of what prep-to-deck-minutes would change
#        (including any re-wrapping of the notes, if PRETTIFY is on).
#        Writes nothing.
prep-to-deck-dry:
	$(SN) update --from $(PREP) --apply-minutes --dry-run $(PRETTY)

## prettify-dry: preview `make prettify` as a diff (read-only)
#   in:  $(DECK)
#   out: unified diff on stdout of the re-indented / re-wrapped notes.
#        Writes nothing.
prettify-dry:
	$(SN) prettify --wrap $(NOTES_WRAP) --dry-run

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
#        Reads prettified and one-line notes alike; $(DECK) is not modified.
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
#        Notes re-wrapped at $(NOTES_WRAP) if PRETTIFY is on.
prep-to-deck:
	$(SN) update --from $(PREP) $(PRETTY)

## prep-to-deck-minutes: as prep-to-deck, and apply the prep doc's minutes
#   in:  $(PREP) cue lines and "· N min" headings
#   out: REWRITES $(DECK) in place -- cues as above, data-minutes from the
#        headings, then a restamp (data-timing, data-section-*, totalTime).
prep-to-deck-minutes:
	$(SN) update --from $(PREP) --apply-minutes $(PRETTY)

## md-to-deck: copy cues from $(NOTES_MD) into the deck
#   in:  $(NOTES_MD) (made by `make notes-md`, then edited)
#   out: REWRITES $(DECK) in place -- cues of the slides listed in
#        $(NOTES_MD); scripts and minutes unchanged.
md-to-deck:
	$(SN) update --from $(NOTES_MD) $(PRETTY)

## scripts: copy the prep doc's spoken scripts into the deck (FULL SCRIPT box)
#   in:  $(PREP) "> " quoted lines under each slide heading
#   out: REWRITES $(DECK) in place -- replaces (or adds) the dashed rule +
#        amber FULL SCRIPT box after the cues of every slide that has a script
#        in the prep doc. Cues and minutes unchanged. Safe to rerun.
scripts:
	$(SN) scripts --from $(PREP) $(PRETTY)

## scripts-remove: strip every FULL SCRIPT box from the deck
#   in:  $(DECK)
#   out: REWRITES $(DECK) in place -- cues only, as before the scripts were
#        added. `make scripts` puts them back.
scripts-remove:
	$(SN) scripts --remove $(PRETTY)

# ---------------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------------

## restamp: recompute timing attributes from data-minutes
#   in:  $(DECK) data-minutes on each <section>
#   out: REWRITES $(DECK) in place -- data-timing, data-section-index,
#        data-section-count, data-section-minutes and reveal's totalTime.
#        Run after adding, removing, moving or retiming slides by hand.
restamp:
	$(SN) restamp $(PRETTY)

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

## prettify: re-indent and wrap every speaker-notes <aside> in the deck
#   in:  $(DECK)
#   out: REWRITES $(DECK) in place -- each <aside class="notes"> gets one
#        block element per line, nested by depth, text wrapped at
#        $(NOTES_WRAP) columns. Whitespace only; nothing outside the notes
#        changes. Runs whatever PRETTIFY is set to. Safe to rerun.
prettify:
	$(SN) prettify --wrap $(NOTES_WRAP)

# ---------------------------------------------------------------------------
# Everyday
# ---------------------------------------------------------------------------

## sync: prep doc -> deck (cues, minutes, scripts), then check
#   in:  $(PREP)
#   out: REWRITES $(DECK) in place (prep-to-deck-minutes, then scripts), then
#        runs check. $(PREP) is not modified. Notes prettified if PRETTIFY is
#        on. The one to run after editing the prep doc.
sync: prep-to-deck-minutes scripts check

# ---------------------------------------------------------------------------
# Upload
# ---------------------------------------------------------------------------
# The source is this folder with NO trailing slash, so rsync recreates it by
# name under $(RPATH): $(RPATH)<this folder's name>/. Only files whose size or
# mtime differ are examined, and only their changed blocks cross the wire.
# Nothing on the remote is deleted. Needs rsync on both ends and SSH access.

## upload: rsync this deck folder to $(REMOTE):$(RPATH), changes only
#   in:  this folder, minus $(RSYNC_EXCLUDE)
#   out: new/changed files copied to $(REMOTE):$(RPATH)<folder name>/.
#        Remote files missing locally are left alone. Local files unchanged.
upload:
	$(RSYNC) $(RSYNC_FLAGS) --stats $(addprefix --exclude=,$(RSYNC_EXCLUDE)) \
		"$$(realpath .)" "$(REMOTE):$(RPATH)"

uploadm:
	$(RSYNC) $(RSYNC_FLAGS) --stats $(addprefix --exclude=,$(RSYNC_EXCLUDE)) \
		"$$(realpath .)/" "$(REMOTE):/data/andrew/Maule_2026_10_TPGRDRUSeminar/"
	ssh andrew@amanita.walnut.casa sudo chmod -R 777 /data/andrew

## upload-dry: list what `make upload` would send (read-only)
#   in:  this folder, $(REMOTE):$(RPATH)
#   out: itemized list of files that would be sent, on stdout. Writes nothing.
upload-dry:
	$(RSYNC) $(RSYNC_FLAGS) --dry-run --itemize-changes $(addprefix --exclude=,$(RSYNC_EXCLUDE)) \
		"$$(realpath .)" "$(REMOTE):$(RPATH)"
