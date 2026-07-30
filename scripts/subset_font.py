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

ORDER MATTERS, AND THIS SCRIPT IS NOT DETERMINISTIC. fontTools writes a fresh
`head.modified` timestamp on every run, so each run produces a different woff2
even when the character set has not changed by one glyph -- and make_chart.py
base64-INLINES the woff2 into every page. So:

  1. run this, then 2. run make_chart.py --public.

Backwards, and the pages carry the base64 of the previous font while a different
woff2 sits in vendor/. Nothing fails; the two just disagree, and the next
person to check "does a rebuild produce a diff?" gets a misleading answer.
For the same reason, re-running this dirties every published page, so don't
re-run it to see whether anything changed -- read the coverage report, which
names each plate's new characters, or "none".

Verify the two agree with:
    python3 -c "import base64,pathlib; \
      raw=pathlib.Path('vendor/gentium/laguna-serif-regular.woff2').read_bytes(); \
      print(base64.b64encode(raw).decode() in \
        open('docs/genealogy-i/index.html').read())"
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
#
# † and › WERE MISSING UNTIL 2026-07-29, on both published pages, and had
# been from the day each shipped. Both are set from the page's own SCRIPT --
# m.textContent="†" for the editorial-attribution marker on a person card,
# c.textContent="›" for the card's chevron -- so neither appears in any HTML
# template string a reader of this file would scan, and this list was written by
# scanning those. The dagger is not decorative: it marks the one thing this
# edition asserts that the plate does not (Genealogy I, 83-85). It rendered
# anyway, because macOS substitutes silently for a missing glyph -- the exact
# trap this whole script exists to avoid. check_against_build() is what caught
# it, and is why that function reads docs/ instead of trusting this list.
TEMPLATE_CHARS = set(
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "—–’‘“” éñ…·→†›"
)


# PERSONS' last field is plate_note, which is EDITORIAL COMMENTARY and inert in
# the renderer -- make_chart.py reads it once, only to test for "braced". So it
# must not drive the subset. It used to: Genealogy II's notes describe rejected
# readings in prose, and quoting a glyph in order to say it is NOT on the plate
# put that glyph in the shipped font (U+02D1 from two withdrawal notes, U+00EF
# from 190's fold-crease note). Harmless in bytes and wrong in principle -- the
# subset should be what the pages render, and nothing else.
#
# Everything else is kept, deliberately. UNIONS' and CHILDREN's notes DO reach
# the page -- Table 1's misprint annotation is one -- and the failure mode on
# this side is the bad one: a glyph left out renders as an empty box, silently,
# because nothing else fails. Hence check_against_build() below, which is the
# real guarantee: it reads the built pages and demands every character in them
# be in the subset. Narrowing this scan without that check would be a guess.
PLATE_NOTE_INDEX = 10


def _plate_chars(T):
    """Every character of one plate's transcription that can reach a page."""
    chars = set()
    for row in T.PERSONS:
        for i, field in enumerate(row):
            if isinstance(field, str) and i != PLATE_NOTE_INDEX:
                chars.update(field)
    for table in (T.UNIONS, T.CHILDREN, T.PLATE_NOTES):
        for row in table:
            for field in row:
                if isinstance(field, str):
                    chars.update(field)
    return chars


def used_chars():
    """Every character appearing in any registered plate's transcription."""
    chars = set(TEMPLATE_CHARS)
    for key in sorted(TABLES):
        chars |= _plate_chars(importlib.import_module(TABLES[key]["module"]))
    return chars


def report_coverage():
    """Per-plate character counts, so a new plate's contribution is visible."""
    base = set(TEMPLATE_CHARS)
    for key in sorted(TABLES):
        spec = TABLES[key]
        chars = _plate_chars(importlib.import_module(spec["module"]))
        new = sorted(c for c in chars - base if c.strip())
        base |= chars
        extra = ("".join(new) if new else "none")
        print(f"  {spec['plate']:>8} ({spec['module']}): {len(chars)} chars, "
              f"new to the subset: {extra}")


def check_against_build(chars):
    """
    Hold the subset against the pages that actually shipped.

    The scan above reasons from the data about what OUGHT to render. This reads
    docs/ and asks what DOES. It is the check that matters, because the
    dangerous direction is omission -- a missing glyph is an empty box on
    someone else's machine and nothing here fails to say so.

    Skipped, not failed, when docs/ has not been built: the subset has to be
    generated before the build that uses it, so on a first run for a new plate
    there is legitimately nothing to compare against. Re-run after building.
    """
    pages = sorted((ROOT / "docs").rglob("*.html"))
    if not pages:
        print("  docs/ not built -- coverage against the pages not checked")
        return True
    missing = {}
    for page in pages:
        for ch in set(page.read_text(encoding="utf-8")):
            if ord(ch) > 0x7E and ch not in chars and ch.strip():
                missing.setdefault(ch, []).append(page.name)
    if missing:
        for ch, where in sorted(missing.items(), key=lambda kv: ord(kv[0])):
            print(f"  MISSING from the subset: U+{ord(ch):04X} {ch!r} "
                  f"in {', '.join(sorted(set(where)))}")
        return False
    print(f"  every non-ASCII character in {len(pages)} built pages is in the subset")
    return True


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
    chars = used_chars()
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
    return 0 if check_against_build(chars) else 1


if __name__ == "__main__":
    raise SystemExit(main())
