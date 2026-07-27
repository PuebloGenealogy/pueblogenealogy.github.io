"""
Subset SIL Gentium to the glyphs this edition actually uses.

    python3 scripts/subset_font.py

Reads vendor/gentium/Gentium-{Regular,Italic}.ttf and writes
vendor/gentium/laguna-serif-{regular,italic}.woff2 -- a few kB each instead of
~1 MB. make_chart.py base64-inlines those so the published page carries its own
font and renders the phonetic diacritics identically everywhere.

Why this exists at all: the names use Americanist phonetic characters --
U+1DA6 ᶦ, U+1D58 ᵘ, U+1D43 ᵃ from Unicode's Phonetic Extensions -- which are
absent from Georgia, Palatino and every other face in the CSS fallback stack.
They render on this Mac only because macOS silently substitutes. Elsewhere they
may show as empty boxes, which would corrupt the transcription visually.

LICENCE. Gentium is under the SIL Open Font License 1.1. Subsetting is
modification, which the OFL permits (OFL-FAQ 2.6), but "Gentium" is a Reserved
Font Name, so a modified version must not carry it. This script therefore
rewrites the name table to "Laguna Serif". vendor/gentium/OFL.txt travels with
the repo and is copied to docs/fonts/OFL.txt for the published site.

Run this only when the transcription gains characters it did not have before;
the output is committed, so a normal chart build needs no font tooling.
"""

import importlib
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# Every registered plate, not just Table 1. The font is shared by all the
# published pages, so a plate whose transcription introduces a diacritic the
# subset lacks would ship a page that renders it as an empty box -- silently,
# because nothing else would fail.
from make_chart import TABLES  # noqa: E402

VENDOR = ROOT / "vendor" / "gentium"
FAMILY = "Laguna Serif"

# Characters the page template contributes on top of the transcribed data:
# ASCII, plus the typographic punctuation the header, footer and brackets use.
TEMPLATE_CHARS = set(
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "—–’‘“” éñ…·→"
)


def used_chars():
    """Every character appearing in any registered plate's transcription."""
    chars = set(TEMPLATE_CHARS)
    for key in sorted(TABLES):
        T = importlib.import_module(TABLES[key]["module"])
        for table in (T.PERSONS, T.UNIONS, T.CHILDREN, T.PLATE_NOTES):
            for row in table:
                for field in row:
                    if isinstance(field, str):
                        chars.update(field)
    return chars


def report_coverage():
    """Per-plate character counts, so a new plate's contribution is visible."""
    base = set(TEMPLATE_CHARS)
    for key in sorted(TABLES):
        spec = TABLES[key]
        T = importlib.import_module(spec["module"])
        chars = set()
        for table in (T.PERSONS, T.UNIONS, T.CHILDREN, T.PLATE_NOTES):
            for row in table:
                for field in row:
                    if isinstance(field, str):
                        chars.update(field)
        new = sorted(c for c in chars - base if c.strip())
        base |= chars
        extra = ("".join(new) if new else "none")
        print(f"  {spec['plate']:>8} ({spec['module']}): {len(chars)} chars, "
              f"new to the subset: {extra}")


def rename(font, style):
    """
    Replace every Gentium name record with the neutral family name.

    Required by the OFL's Reserved Font Name clause: a modified font may not be
    distributed under the reserved name. nameIDs 1/4/6 are family, full name and
    PostScript name; 16/17 are the typographic family/subfamily.
    """
    full = f"{FAMILY} {style}"
    ps = f"{FAMILY.replace(' ', '')}-{style}"
    for rec in font["name"].names:
        if rec.nameID in (1, 16):
            rec.string = FAMILY
        elif rec.nameID in (2, 17):
            rec.string = style
        elif rec.nameID == 4:
            rec.string = full
        elif rec.nameID == 6:
            rec.string = ps
        elif rec.nameID == 3:  # unique id
            rec.string = f"{ps};subset for pueblogenealogy.github.io"


def build(src, style, out):
    chars = used_chars()
    font = TTFont(src)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.desubroutinize = True
    opts.layout_features = ["kern", "liga", "ccmp", "mark", "mkmk"]
    opts.notdef_outline = True
    # Keep the name table so the rename below survives into the output.
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.name_languages = ["*"]

    subsetter = subset.Subsetter(options=opts)
    subsetter.populate(text="".join(sorted(chars)))
    subsetter.subset(font)
    rename(font, style)
    font.flavor = "woff2"
    font.save(out)
    return len(chars), out.stat().st_size


def main():
    if not VENDOR.exists():
        print(f"missing {VENDOR}")
        return 1
    report_coverage()
    for style, src_name in (("Regular", "Gentium-Regular.ttf"),
                            ("Italic", "Gentium-Italic.ttf")):
        src = VENDOR / src_name
        if not src.exists():
            print(f"missing {src}")
            return 1
        out = VENDOR / f"laguna-serif-{style.lower()}.woff2"
        n, size = build(src, style, out)
        print(f"{out.name}: {n} chars, {size:,} bytes "
              f"(from {src.stat().st_size:,})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
