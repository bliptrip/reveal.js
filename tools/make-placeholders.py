#!/usr/bin/env python3
"""
make-placeholders.py -- stand-in media, so the port can be reviewed before the
real figures are in place.

The seminar's images and videos come to ~826 MB and are deliberately not in
git (see .gitignore). That is the right call, but it means a fresh clone shows
78 slides full of broken-image icons, and you cannot tell a layout regression
from a missing file.

This writes a labelled grey placeholder for every image the deck references
that is not already on disk, at the reference's own path. Each placeholder
carries its filename, so a slide that looks wrong tells you which figure it is
waiting for. Real files are never overwritten: drop your static/images tree in
on top and the placeholders it covers simply stop being used.

    python3 tools/make-placeholders.py                 # fill the gaps
    python3 tools/make-placeholders.py --clean         # remove placeholders

Videos are not generated -- three background videos, and an empty <video> is
harmless. Those slides will show their dark gradient until you add the files.
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("make-placeholders: needs Pillow  ->  pip install Pillow")

DECK = Path(__file__).resolve().parent.parent / "presentation" / "index.html"
ROOT = DECK.parent
MARKER = b"ggruvitis-placeholder"

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def referenced_images():
    """Every local image path the deck references, as (relative-ref, abspath)."""
    html = DECK.read_text(encoding="utf-8")
    refs = set(re.findall(r'(?:src=|url\()["\']?(\.\./static/[^"\')\s]+)', html))
    out = []
    for ref in sorted(refs):
        if Path(ref).suffix.lower() in IMAGE_EXT:
            out.append((ref, (ROOT / ref).resolve()))
    return out


def is_placeholder(path: Path) -> bool:
    try:
        with open(path, "rb") as fh:
            return MARKER in fh.read(4096)
    except OSError:
        return False


def make(path: Path, label: str, width=1400, height=900):
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (width, height), (238, 238, 238))
    d = ImageDraw.Draw(img)

    # a soft frame and a diagonal, so it reads as "absent" at a glance
    d.rectangle([8, 8, width - 9, height - 9], outline=(200, 200, 200), width=3)
    d.line([8, 8, width - 9, height - 9], fill=(226, 226, 226), width=2)
    d.line([8, height - 9, width - 9, 8], fill=(226, 226, 226), width=2)

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        small = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except OSError:
        font = small = ImageFont.load_default()

    box = d.textbbox((0, 0), label, font=font)
    d.text(((width - (box[2] - box[0])) / 2, height / 2 - 40),
           label, fill=(90, 90, 90), font=font)

    note = "placeholder - real figure not in git"
    box = d.textbbox((0, 0), note, font=small)
    d.text(((width - (box[2] - box[0])) / 2, height / 2 + 20),
           note, fill=(150, 150, 150), font=small)

    # PNG comment chunk, so --clean can recognise its own work
    img.save(path, "PNG", pnginfo=_marker_info())


def _marker_info():
    from PIL.PngImagePlugin import PngInfo
    meta = PngInfo()
    meta.add_text("Comment", MARKER.decode())
    return meta


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clean", action="store_true",
                    help="delete generated placeholders instead of creating them")
    args = ap.parse_args()

    if not DECK.is_file():
        sys.exit(f"make-placeholders: deck not found at {DECK}")

    refs = referenced_images()
    made = skipped = removed = 0

    for ref, abspath in refs:
        if args.clean:
            if abspath.exists() and is_placeholder(abspath):
                abspath.unlink()
                removed += 1
            continue

        if abspath.exists():
            skipped += 1
            continue

        # .svg references get a .svg-named PNG; browsers sniff content, and
        # the deck only uses them as <img src>, so this renders fine.
        make(abspath, Path(ref).name)
        made += 1

    if args.clean:
        print(f"make-placeholders: removed {removed} placeholder(s)")
    else:
        print(f"make-placeholders: created {made}, left {skipped} real file(s) alone")
        if made:
            print("                   run with --clean once the real media is in place")


if __name__ == "__main__":
    main()
