---
name: transcribe-plate
description: Transcribe a scanned Parsons genealogy plate into a verified digital edition — tile-by-tile vision reading, the PERSONS/UNIONS/CHILDREN schema, structural self-checks, and the published chart. Use when the user supplies a new genealogy plate scan (Genealogy II, III, or any similar bracket-diagram plate) and wants it added to this project in the same form as Table 1.
---

# Transcribing a genealogy plate

This reproduces the method used for Table 1, "Genealogy I". It is written as a
sequence of gates: **do not proceed past a gate until it passes.** The gates are
what make the edition trustworthy, and skipping one produces a chart that looks
right and is wrong.

Read `METHOD.md` in the repo root first. It states the editorial rules — what
counts as a faithful reading, how misprints are handled, why nothing is
silently corrected. This file is the procedure; that file is the reasoning.

---

## Gate 0 — Establish the source

The scan must be legible at native resolution. Table 1 was 16172 × 11798 px.

```bash
sips -g pixelWidth -g pixelHeight <scan>
```

Store it as `sources/parsons-<year>-table-<n>.jpg`. Record its sha256 — the
transcription is only auditable against a known file.

**Never run OCR.** It was tried and it fails on this material: the Americanist
diacritics (`ʼ ˙ ᶦ ᵘ ᵃ` and the breves) are dropped or mangled, and bracket
geometry carries the genealogical relationships, which OCR discards entirely.
Read the image with vision, at native resolution.

---

## Gate 1 — Read the plate, tile by tile

1. Downscale the whole plate to ~1600 px wide for orientation. Identify the
   caption, the generation columns, and the founding couples.
2. Crop tiles at **native resolution** and read each one. Table 1 took ~45 tiles.
   `sips` is the only image tool on this machine — no ImageMagick, no PIL:

   ```bash
   sips -c <height> <width> --cropOffset <top> <left> <scan> --out tile.jpg
   ```

   Work in the scratchpad, not the project folder.
3. Where a glyph is uncertain, crop it tighter and look again. Six glyphs in
   Table 1 needed this. Do not guess: a wrong diacritic is a wrong reading, and
   it will be cited.
4. Record each person as a tuple, keeping the plate's own numbering.

**Orthography.** Use these exact codepoints — see `ORTHOGRAPHY` in
`scripts/transcription.py`, which is the authority:

| Glyph | Codepoint | Meaning |
|---|---|---|
| `ʼ` | U+02BC | modifier letter apostrophe (glottal stop) |
| `˙` | U+02D9 | dot above — aspiration or length |
| `ă ĕ ĭ ŭ Ă` | U+0103 0115 012D 016D 0102 | breves |
| `ᶦ ᵘ ᵃ` | U+1DA6 1D58 1D43 | superscript i / u / a |
| `ñ` | U+00F1 | as printed in "Zuñi" |

A raised dot after a vowel is U+02D9, **not** a diaeresis. This distinction was
misread once during Table 1 and had to be corrected.

**Plate conventions.**
- A dash where a name should be means Parsons recorded no name. Store an empty
  string, not a dash.
- `d.` alone means died, date unknown.
- Braces `{ }` join two names for one person; note it in `plate_note`.
- Parenthesised English names (e.g. "Hazel") are **plate data** — they belong in
  `alt_name`, not in a research column.
- **Reproduce misprints; do not fix them.** Record the correct reading and
  document the discrepancy in the union's `note`. Table 1 has one: the `+` line
  under 76 is numbered 68 but names person 67.
- Copy cross-references verbatim, including their line breaks and page pointers.

---

## Gate 2 — Encode to the schema

Write `scripts/transcription_<n>.py` modelled exactly on `scripts/transcription.py`.
Do not invent a new shape; the renderer depends on these tuples.

```python
PERSONS  = [(id, generation, sex, name_as_printed, alt_name, age, clan,
             vital_note, origin, cross_ref, plate_note), ...]
UNIONS   = [(union_id, wife_id, husband_id, wife_order, husband_order, note), ...]
CHILDREN = [(union_id, mother_id, father_id, child_id, note), ...]
```

Also carry `PLATE_NOTES`, `CLANS`, `ORTHOGRAPHY`, `fold()` and `self_check()`.

**Copy `_FOLD` verbatim from an existing module — never write a fresh one.**
The four maps are deliberately identical (`CLAUDE.md`, *The four `_FOLD` maps
are one map*); a per-plate map is how two names ended up unfoldable by their own
plate. If this plate brings a character new to a *name*, add it to **all** the
maps, not just this one.

- A child whose paternity the plate does not assign gets `union_id=""` and
  `father_id=0`; it will hang off the mother's line alone.
- A person appearing twice on the plate is stored once. The second appearance
  becomes a cross-reference.

**If ids collide with Table 1** (both plates number from 1), keep the plate's
own numbering inside the module and prefix on output — `II-158` — as
`README.md` describes. Never renumber the plate.

---

## Gate 3 — Structural verification ⛔

```bash
python3 scripts/transcription_<n>.py
```

Must print `all structural checks pass`. The checks are:

- ids are exactly `1..N`, each once
- **every child's clan equals its mother's clan** — Laguna descent is
  matrilineal, so this is an independent check on every bracket you read. All
  27 unions in Table 1 passed it, and that is the single strongest piece of
  evidence that the structure is right
- no person is a child twice
- no person is orphaned (neither child nor spouse)

Then check the arithmetic: **child entries + spouse-only entries = total
persons.** Table 1: 80 + 24 = 104.

If a clan mismatch appears, **the reading is wrong, not the rule.** Go back to
the tile and look again.

---

## Gate 4 — Render

`make_chart.py` is already table-agnostic. Register the plate in the `TABLES`
dict near the top — that is the only edit the renderer needs:

```python
"ii": {
    "numeral": "II",
    "plate": "Table 2",
    "module": "transcription_ii",   # your new module
    "roots": [...],                  # the founding women, in plate order
    "slug": "genealogy-ii",
    "blurb": "One sentence for the landing-page card.",
},
```

Then remove the matching entry from `PENDING`, so the plate stops advertising
itself as untranscribed. Counts in the page copy (individuals, marriages,
generations) are computed from the data — never type them.

```bash
python3 scripts/make_chart.py --public --table ii
```

`--public` rebuilds **every** registered table plus the landing page and
sitemap, so those can never describe a stale set.

Do not copy the script, and keep `Chart`, `person_line()` and the CSS untouched
— the layout is already correct and was verified by measurement.

Then build and verify **in the browser, by measuring**, not by eye:

| Check | Requirement |
|---|---|
| Column drift | **0 px** at every generation |
| Sibling brackets | every group sits on its **mother's** row |
| Leader rules | on mother lines only, whether she is the primary or a `+` spouse |
| Block overflow | no block wider than `--col` at generations 1..n−1 |
| Body scroll | the page body must not scroll sideways |
| Persons drawn | all of them |

The column grid holds because every `.node` contributes exactly one `--stub` of
padding plus one `--col`-wide block, so generation *d* lands at
`d × (--col + --stub)` on every path. If drift appears, something broke that
invariant — do not fix it with per-element margins.

If the transcription introduces characters the font subset lacks:

```bash
python3 scripts/subset_font.py
```

---

## Gate 5 — Publish ⛔ privacy

**The published edition is the transcription only.** No English names, no census
matches, ever. This is structural, not a matter of care:

- research data lives in the git-ignored workbook; `docs/` is built from the
  transcription module, which has no research columns to read
- `make_chart.py --public` greps its own output for research chips and **deletes
  the file** rather than write one

Before the first commit of any new material, confirm `git status` lists no
`.xlsx` and nothing under `build/`. Git history is permanent; a later deletion
does not remove it, and any clone or fork made meanwhile keeps it.

```bash
python3 scripts/make_chart.py --public   # regenerates docs/ including the landing page
```

Add the new table to the landing page cards, `sitemap.xml`, and `CITATION.cff`.
Never hand-edit anything under `docs/` — it is overwritten on every build.

---

## What to tell the user

Report what was **measured**, not what was attempted: glyph counts, the
structural check output, the column drift, the persons-drawn count. Flag every
uncertain reading explicitly rather than burying it. If a plate detail cannot be
verified from the scan, say so and leave it flagged — the scan is usually the
fastest authority, faster than catalog records, which describe publications
rather than plates.
