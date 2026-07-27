# Laguna Genealogies — project context

A digital edition of the genealogical plates published with Elsie Clews Parsons,
**"Laguna Genealogies"**, *Anthropological Papers of the American Museum of
Natural History*, vol. 19, pt. 5 (1923), pp. 133–292.

**Live:** https://prettyph3nom.github.io/laguna-genealogy-tables/
**Repo:** https://github.com/prettyph3nom/laguna-genealogy-tables (public)

Table 1, "Genealogy I", is transcribed and published: 104 individuals, 27
marriages, 80 parent–child links, 5 generations, two founding couples (1+2 and
54+55). Tables 2 and 3 are not yet transcribed.

---

## The one thing to get right

**The published edition is the 1923 transcription only.** No English names, no
census matches, ever. Some people identifiable through that research have living
descendants, the repo is public, and git history is permanent.

This is enforced structurally, and must stay that way:

- Research columns live in `data/parsons_genealogy_I.xlsx`, which is git-ignored
- The public build reads `scripts/transcription.py`, which has no research
  columns to read — there is no code path from workbook to `docs/`
- `make_chart.py --public` greps its own output for `class="eng"` /
  `class="census"` and **deletes the file** rather than write one

Before any first commit of new material, confirm `git status` lists no `.xlsx`
and nothing under `build/`.

## Hard rules

| Never | Why |
|---|---|
| Re-run `scripts/build_workbook.py` | Overwrites the workbook, discarding research columns |
| Hand-edit anything in `docs/` | Generated; overwritten every build |
| Run OCR on a plate | Drops the diacritics and discards the bracket geometry |
| "Correct" a misprint in the data | The edition reproduces the plate; misprints are annotated, not fixed |
| Alter names, diacritics, numbering, clans or cross-references | Accuracy is the whole point |

## Commands

```bash
python3 scripts/transcription.py          # structural self-check
python3 scripts/make_chart.py             # private build -> build/ (may show research data)
python3 scripts/make_chart.py --public    # published build -> docs/ + landing page, sitemap
python3 scripts/subset_font.py            # only when the data gains new characters
```

## Layout

The chart reproduces the plate's column grid. Every `.node` is
`[.block][.kidcol]` and each nested node adds exactly one `--stub` plus one
`--col`-wide block, so generation *d* lands at `d × (--col + --stub)` on every
path. **Column drift must measure 0 px at every generation.** If it doesn't,
something broke that invariant — don't patch it with per-element margins.

Sibling brackets hang off the **mother's** line, not the top of a block, and the
leader rules use the same `mother_row` index. Getting this wrong looks like a
styling detail while actually asserting a different genealogy.

Verify layout by measuring in the browser, not by eye.

## Adding a plate

`make_chart.py` is table-agnostic. Add an entry to `TABLES`, remove the matching
`PENDING` entry, write `scripts/transcription_<n>.py` on the same schema, then
`--public --table <n>`. Counts in the page copy are computed from the data —
never typed.

Full procedure: **`/transcribe-plate`** (`.claude/skills/transcribe-plate/`).
Editorial reasoning: **`METHOD.md`**.

## Facts worth knowing

- **Clan descent is matrilineal**, so a child's clan must equal its mother's.
  This is an independent check on every bracket reading and is what caught
  errors in Table 1. A clan mismatch means the reading is wrong, not the rule.
- **Person 8 (Yu˙si) appears twice** on the plate; drawn once, with a
  cross-reference standing in for the repeat.
- **Misprint at 76:** the `+` line is numbered 68 but names person 67. Recorded
  as 67, documented on union U23.
- **Person 90** is printed "Heʼsa (Hazel)" — "Hazel" is *plate data*
  (`alt_name`), not a research addition.
- The plate is captioned "TABLE 1 / GENEALOGY I"; verified from the scan.
- The dashed divider between the two families is the only visual editorial mark
  inside the plate frame. The 2026 apparatus around it — generation ruler,
  person-number anchors (`#p{n}`), the register — is disclosed in the footer's
  editorial notes; the line text itself is exactly as printed.

## Environment

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom`. **No Homebrew, no
ImageMagick, no PIL** — use `sips` for image work. Pages deploys from
`main` / `/docs`, HTTPS enforced.

## State

Merged on `main`: the edition, the URL fix, the method docs, the table-agnostic
renderer.

**Open:** PR #2, `search-console-hook` — adds `GOOGLE_SITE_VERIFICATION` to
`make_chart.py`. Inert until a token is pasted in; output is byte-identical
while empty.

**Outstanding:**
- Submit the sitemap in Google Search Console. Needs a URL-prefix property for
  `https://prettyph3nom.github.io/laguna-genealogy-tables/` (not Domain —
  `github.io` is a public suffix) and the HTML-tag token. Google retired the
  sitemap ping endpoint in 2023, so the console is the only route.
- Phonetic glyphs unverified on **Windows and Android**. The embedded font
  subset should make this a non-issue, but it has not been checked on a device.
- Tables 2 and 3 await scans.

## Working style

Report what was measured, not what was attempted. Flag uncertain readings
explicitly rather than burying them. The source scan in `sources/` is usually
the fastest authority — faster than catalog records, which describe
publications rather than plates.
