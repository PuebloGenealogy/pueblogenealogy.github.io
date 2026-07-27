# Laguna Genealogies — project context

A digital edition of the genealogical plates published with Elsie Clews Parsons,
**"Laguna Genealogies"**, *Anthropological Papers of the American Museum of
Natural History*, vol. 19, pt. 5 (1923), pp. 133–292.

**Live:** https://pueblogenealogy.github.io/
**Repo:** https://github.com/PuebloGenealogy/pueblogenealogy.github.io (public)
**Pages:** deploys from `main` / `/docs`, HTTPS enforced.

Published: **Genealogy I** (Table 1) — 104 individuals, 27 marriages, 80
parent–child links, 5 generations, founding couples 1+2 and 54+55. **Genealogy
IV** (Table 4) — 73 individuals, 14 marriages, 58 parent–child links, 4
generations, founding couples 1+2 and 59+60. Tables 2 and 3 await scans.

> This is the **v2 site**. A first, simpler edition was published from
> `prettyph3nom/laguna-genealogy-tables` at
> `https://prettyph3nom.github.io/laguna-genealogy-tables/`. The two are separate
> repos with separate histories. Retiring v1 is an open task — see **State**.

---

## The one thing to get right

**The published edition is the 1923 transcription only.** No English names, no
census matches, ever. Some people identifiable through that research have living
descendants, the repo is public, and git history is permanent.

This is enforced structurally, and must stay that way:

- Research columns live in `data/parsons_genealogy_I.xlsx`, which is git-ignored
- The public build reads `scripts/transcription*.py`, which have no research
  columns to read — there is no code path from workbook to `docs/`
- `make_chart.py --public` greps its own output for `class="eng"` /
  `class="census"` and **deletes the file** rather than write one

Before any first commit of new material, confirm `git status` lists no `.xlsx`
and nothing under `build/`. `/publish` runs this gate for you.

## Hard rules

| Never | Why |
|---|---|
| **Hand-edit anything in `docs/`** | Generated; overwritten every build. Edit `scripts/make_chart.py` instead |
| Re-run `scripts/build_workbook.py` | Overwrites the workbook, discarding research columns |
| Run OCR on a plate | Drops the diacritics and discards the bracket geometry |
| "Correct" a misprint in the data | The edition reproduces the plate; misprints are annotated, not fixed |
| Alter names, diacritics, numbering, clans or cross-references | Accuracy is the whole point |

## Commands

```bash
python3 scripts/transcription.py          # structural self-check, Table 1
python3 scripts/transcription_iv.py       # structural self-check, Table 4
python3 scripts/make_chart.py --public    # published build -> docs/ (this is the one you want)
python3 scripts/make_chart.py             # private build -> build/ (needs data/*.xlsx; not in this clone)
python3 scripts/subset_font.py            # only when the data gains new characters
```

**Local preview:** `preview_start` with the config name `site`
(`.claude/launch.json`) serves `docs/` at `http://localhost:4173`.
The design loop is: edit `make_chart.py` → rerun `--public` → reload the page.

**Publishing:** `/publish` (`.claude/skills/publish/`) — gated build, privacy
check, commit, push, live verification.

## Where things are

| Path | What |
|---|---|
| `scripts/make_chart.py` | **The whole renderer.** CSS, JS, HTML, SEO, layout. Everything visual is here |
| `scripts/transcription.py`, `transcription_iv.py` | The 1923 baseline as data. Immutable |
| `docs/` | Generated site. Never hand-edit |
| `assets/og-cover.jpg` | Social card, derived once from the plate scan (see `OG_IMAGE`) |
| `sources/` | Source scans, in repo but not served |
| `METHOD.md` | Editorial method — why readings are made as they are |

Identity lives in two constants at the top of `make_chart.py`: `SITE` and
`REPO`. Every canonical URL, sitemap entry and card derives from them.

## Layout

The chart reproduces the plate's column grid. Every `.node` is
`[.block][.kidcol]` and each nested node adds exactly one `--stub` plus one
`--col`-wide block, so generation *d* lands at `d × (--col + --stub)` on every
path. **Column drift must measure 0 px at every generation.** If it doesn't,
something broke that invariant — don't patch it with per-element margins.

Sibling brackets hang off the **mother's** line, not the top of a block, and the
leader rules use the same `mother_row` index. Getting this wrong looks like a
styling detail while actually asserting a different genealogy.

Verify layout by measuring in the browser, not by eye — walk `.node` depth and
compare each `.block`'s left offset.

## Adding a plate

`make_chart.py` is table-agnostic. Add an entry to `TABLES`, remove the matching
`PENDING` entry, write `scripts/transcription_<n>.py` on the same schema, then
`--public`. Counts in the page copy are computed from the data — never typed.

Full procedure: **`/transcribe-plate`** (`.claude/skills/transcribe-plate/`).

## Facts worth knowing

- **Clan descent is matrilineal**, so a child's clan must equal its mother's.
  This is an independent check on every bracket reading and is what caught
  errors in Table 1. A clan mismatch means the reading is wrong, not the rule.
- **Person 8 (Yu˙si) appears twice** on the Table 1 plate; drawn once, with a
  cross-reference standing in for the repeat.
- **Misprint at 76 (Table 1):** the `+` line is numbered 68 but names person 67.
  Recorded as 67, documented on union U23.
- **Person 90** is printed "Heʼsa (Hazel)" — "Hazel" is *plate data*
  (`alt_name`), not a research addition. Likewise the English names on Table 4.
- The plates are captioned "TABLE 1 / GENEALOGY I" and "TABLE 4 / GENEALOGY IV";
  verified from the scans.
- The dashed divider between the two families is the only visual editorial mark
  inside the plate frame. The 2026 apparatus around it — generation ruler,
  person-number anchors (`#p{n}`), the register — is disclosed in the footer's
  editorial notes; the line text itself is exactly as printed.

## Environment

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom` (owner of the
`PuebloGenealogy` org). **No Homebrew, no ImageMagick, no PIL** — use `sips` for
image work.

The repo lives under Google Drive. Drive's sync daemon can touch `.git` mid-write;
if git reports object corruption, that is the likely cause.

## State

See `CHANGELOG.md` for what changed when.

**Outstanding:**
- **Google Search Console** — create a **URL-prefix** property for
  `https://pueblogenealogy.github.io/` (not Domain — `github.io` is a public
  suffix), paste the token into `GOOGLE_SITE_VERIFICATION` in `make_chart.py`,
  rebuild, submit the sitemap. Google retired the sitemap ping endpoint in 2023,
  so the console is the only route. Same again for Bing Webmaster Tools.
- **Retire the v1 site.** Until then both sites carry near-identical content and
  split their own ranking; v1 is older and already indexed, so it likely
  outranks v2. Short of deleting it, adding `rel=canonical` on v1's pages
  pointing at the v2 equivalents hands the accumulated ranking over.
- **Inbound links** — a fresh `*.github.io` has no authority. Zenodo archive for
  a DOI (`CITATION.cff` already exists), then the Wikipedia *Elsie Clews
  Parsons* external links.
- **Custom domain** — the strongest remaining SEO upgrade; drops onto this repo
  via a `CNAME` file.
- Tables 2 and 3 await scans.
- Phonetic glyphs unverified on **Windows and Android**. The embedded font
  subset should make this a non-issue, but it has not been checked on a device.

## Working style

Report what was measured, not what was attempted. Flag uncertain readings
explicitly rather than burying them. The source scans in `sources/` are usually
the fastest authority — faster than catalog records, which describe publications
rather than plates.
