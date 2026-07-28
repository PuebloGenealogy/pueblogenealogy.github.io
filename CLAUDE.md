# Laguna Genealogies — project context

A digital edition of the genealogical plates published with Elsie Clews Parsons,
**"Laguna Genealogies"**, *Anthropological Papers of the American Museum of
Natural History*, vol. 19, pt. 5 (1923), pp. 133–292.

**Live:** https://pueblogenealogy.github.io/ · **Repo:**
`PuebloGenealogy/pueblogenealogy.github.io` (public) · Pages from `main` /
`/docs`, HTTPS enforced.

Published: **Genealogy I** (Table 1) — 104 individuals, 27 marriages, 80
parent–child links, 5 generations. **Genealogy IV** (Table 4) — 73 individuals,
14 marriages, 58 parent–child links, 4 generations. Tables 2 and 3 await scans.

## Start here

1. **`docs/` is generated.** All design, copy and markup live in
   `scripts/make_chart.py` (~2,200 lines). Editing `docs/` is discarded silently
   on the next build.
2. **The edition publishes the 1923 transcription only** — never research
   columns. See below; this is the thing that must not go wrong.
3. `CHANGELOG.md` has the history. Read it instead of asking what changed.

---

## The one thing to get right

**No English names, no census matches, ever.** Some people identifiable through
that research have living descendants, the repo is public, and git history is
permanent — a leak cannot be undone by a later commit.

Enforced structurally, and must stay that way:

- Research columns live in `data/parsons_genealogy_I.xlsx`, which is git-ignored
- The public build reads `scripts/transcription*.py`, which have no research
  columns to read — there is no code path from workbook to `docs/`
- `make_chart.py --public` greps its own output for `class="eng"` /
  `class="census"` and **deletes the file** rather than write one

Before committing new material, confirm `git status` lists no `.xlsx` and
nothing under `build/` or `data/`. `/publish` runs this gate.

## Hard rules

| Never | Why |
|---|---|
| **Hand-edit anything in `docs/`** | Generated; overwritten every build. Edit `make_chart.py` |
| Blank `GOOGLE_SITE_VERIFICATION` | The tag is emitted by the build; blanking it lapses Search Console ownership |
| Re-run `scripts/build_workbook.py` | Overwrites the workbook, discarding research columns |
| Run OCR on a plate | Drops the diacritics and discards the bracket geometry |
| "Correct" a misprint in the data | The edition reproduces the plate; misprints are annotated, not fixed |
| Alter names, diacritics, numbering, clans or cross-references | Accuracy is the whole point |

## Commands

```bash
python3 scripts/transcription.py          # structural self-check, Table 1
python3 scripts/transcription_iv.py       # structural self-check, Table 4
python3 scripts/make_chart.py --public    # the published build -> docs/
python3 scripts/subset_font.py            # only when the data gains new characters
```

`--public` must end `N JSON-LD blocks valid` and **exit 0**. It exits 1 on
invalid structured data or a research-data leak. `make_chart.py` with no flag is
the private build; it needs `data/*.xlsx`, which is not in this clone.

**Preview:** `preview_start`, config name `site` — serves `docs/` on
`http://localhost:4173`. Loop: edit `make_chart.py` → rerun `--public` → reload.

**Publish:** `/publish` — gated build, privacy check, push, live verification.

**New plate:** `/transcribe-plate`. `make_chart.py` is table-agnostic: add a
`TABLES` entry, drop the matching `PENDING` one, write
`scripts/transcription_<n>.py` on the same schema. Counts in the page copy are
computed from data, never typed.

## Where things are

| Path | What |
|---|---|
| `scripts/make_chart.py` | **The whole renderer** — CSS, JS, HTML, SEO, layout |
| `scripts/transcription*.py` | The 1923 baseline as data. Immutable |
| `docs/` | Generated site. Never hand-edit |
| `assets/og-cover.jpg` | Social card, derived once from the plate scan (see `OG_IMAGE`) |
| `sources/` | Source scans, in repo but not served |
| `METHOD.md` | Editorial method — why readings are made as they are |

Identity is two constants at the top of `make_chart.py`: `SITE` and `REPO`.
Every canonical, sitemap entry and card derives from them.

## Layout

The chart reproduces the plate's column grid. Every `.node` is
`[.block][.kidcol]`; each nested node adds exactly one `--stub` plus one
`--col`-wide block, so generation *d* lands at `d × (--col + --stub)` on every
path. **Column drift must measure 0 px at every generation.** If it doesn't,
that invariant broke — don't patch it with per-element margins.

Sibling brackets hang off the **mother's** line, not the top of a block, and the
leader rules use the same `mother_row` index. Getting this wrong looks like a
styling detail while actually asserting a different genealogy.

Measure in the browser, don't judge by eye: walk `.node` depth and compare each
`.block`'s left offset.

## Facts worth knowing

- **Clan descent is matrilineal**, so a child's clan must equal its mother's.
  This independently checks every bracket reading and is what caught errors in
  Table 1. A clan mismatch means the reading is wrong, not the rule.
- **Person 8 (Yu˙si) appears twice** on Table 1; drawn once, with a
  cross-reference standing in for the repeat.
- **Misprint at 76 (Table 1):** the `+` line is numbered 68 but names person 67.
  Recorded as 67, documented on union U23.
- **English names in parentheses are plate data**, not research additions —
  person 90 "Heʼsa (Hazel)" on Table 1, and the Johnsons and Mana on Table 4.
- **`d.`** means the person had already died when Parsons recorded the
  genealogy, during her fieldwork of 1918–19; the year is given where known. A
  number after a name is their age at recording.
- Google's structured-data validator is **stricter than schema.org** — valid
  schema.org has been rejected twice here. `check_structured_data()` guards the
  rules we have been told about, not all of them; a Search Console report
  outranks the build's opinion.

## Environment

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom`, owner of the
`PuebloGenealogy` org. **No Homebrew, no ImageMagick, no PIL** — use `sips`.

The repo lives under Google Drive, whose sync daemon can touch `.git` mid-write;
if git reports object corruption, that is the likely cause.

`_backup-v1-laguna-genealogy-tables-2026-07-27/`, one level up, is the **sole
surviving copy** of the deleted v1 repo. Do not clean it up as stale.

## State

Site live and indexed-submitted; Search Console and Bing both verified;
structured data valid and guarded at build time. v1 is deleted.

**Outstanding:**
- **Inbound links** — a fresh `*.github.io` has no authority, and no on-page
  work substitutes. Zenodo archive for a DOI (`CITATION.cff` exists), then the
  Wikipedia *Elsie Clews Parsons* external links.
- **Custom domain** — the strongest remaining SEO upgrade; drops onto this repo
  via a `CNAME` file.
- Tables 2 and 3 await scans.
- Phonetic glyphs: **font coverage proven, live device rendering still
  unchecked.** Reading the shipped woff2 binaries with fontTools, every one of
  the 85 characters in the transcription — and all 94 rendered on Genealogy I —
  is in the cmap of both faces; `ᶦ` U+1DA6, `ᵘ` U+1D58, `ᵃ` U+1D43, `ʼ` U+02BC
  and `˙` U+02D9 included. The faces are base64 data URIs, so nothing is
  fetched and nothing can 404, and no combining marks are used, so there is no
  mark positioning to vary by platform. Tofu is therefore ruled out by
  construction. What is still unknown on **Windows and Android**: whether a
  browser honours the embedded face at all (data-saver, forced-font settings),
  how the `--font-ui` chrome stack resolves there (Segoe UI / Roboto change
  metrics, not glyphs, and could move where the masthead wraps), and diacritic
  quality at small sizes on low-DPI screens. Appearance risks, not corruption.
  Note macOS substitutes for any font, so no on-screen comparison here can
  demonstrate the absence of substitution — read the cmap, don't measure widths.

## Working style

Report what was measured, not what was attempted. Flag uncertain readings
explicitly rather than burying them. The source scans in `sources/` are usually
the fastest authority — faster than catalog records, which describe publications
rather than plates.
