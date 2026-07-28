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
3. **`SESSION-NOTES.md` is where the last session stopped** — read it first.
   It names the open thread and the decisions not to re-litigate. Rolling, not
   a history; `/wrap-session` overwrites it.
4. `CHANGELOG.md` has the history. Read it instead of asking what changed.

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

**Finish a session:** `/wrap-session` — backfills `CHANGELOG.md`, rewrites
`SESSION-NOTES.md` as a handoff, and checks this file for claims the session
falsified. Run it before stopping, not after.

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
| `.zenodo.json` | Metadata for the archived deposit. Read from the **tagged commit**, so it must land on `main` before a release is cut |
| `CITATION.cff` | How to cite. Carries the concept doi plus both dois under `identifiers` |

Identity is three constants at the top of `make_chart.py`: `SITE`, `REPO` and
`DOI`. Every canonical, sitemap entry and card derives from them. `DOI` is the
Zenodo **concept** doi, which always resolves to the newest release — never
hard-code a version doi here, or every citation printed on the site rots at the
next release.

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

## Design invariants

Four rules that look like styling preferences and are not:

1. **The root font size is pinned at 16px.** `GEOM` states the plate grid in rem
   against it, so changing the root rescales `--col` and `--stub` and breaks the
   drift invariant. The `--t-*` ramp exists to size **chrome and prose only** —
   nothing inside `.sheet` is sized from it.
2. **A selected or hovered `.line` may change `background`, `box-shadow` and
   `outline` — nothing else.** Padding, border or height there moves the row and
   throws the sibling bracket off its `mother_row`. That reads as a styling
   detail while actually asserting a different genealogy.
3. **`--rule` is not text.** `body.chart` flattens all text to `--ink` by
   redefining `--muted`; the brackets and leader rules are deliberately excluded,
   because they carry the genealogy's structure.
4. **`--tap` floors every hit area** in the site chrome, and `--bar-h` derives
   from it so anchor `scroll-margin` tracks the bar. Don't restate either.

Two things that will look like bugs and aren't: `key_html()` and the `.key` CSS
are **unreferenced on purpose** (see Outstanding), and below 26rem the word
"Genealogy" in the table pills is visually hidden but kept in the accessible
name, so the sticky bar stays two rows on a phone.

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

**Archived at Zenodo**, concept doi `10.5281/zenodo.21637900`, first release
`v1.0.0` (2026-07-28). The doi appears in `CITATION.cff`, the README badge, the
citation block on every table page, and as `identifier` in the JSON-LD —
`Dataset` on the table pages, `CollectionPage` on the landing page, which is
the entity the deposit actually corresponds to. Archiving is automatic from now
on: Zenodo's webhook is on the repo, so **cutting a GitHub release mints a new
version doi**. `.zenodo.json` controls the record's metadata; without it Zenodo
would title the deposit after the repo.

**Outstanding:**
- **Redesign the chart key** — the open design thread. The old always-visible
  band was removed; `key_html()` and the `.key` CSS are kept, unreferenced, as
  its starting point. Three notations are currently explained **nowhere** on the
  page: `+` for spouse, `F.`/`M.` for sex, and the leader rule. Constraints
  worth knowing before starting: it should work without JavaScript (`<details>`
  does, a popover does not), and the print rule hides `.plate-tools`, so a key
  parked in the toolbar silently vanishes from printed sheets unless forced open
  in `@media print`.
- **Inbound links** — a fresh `*.github.io` has no authority, and no on-page
  work substitutes. Zenodo is done and is itself the first such link. Next, by
  effort-to-return: a **Wikidata** item (heavily crawled, feeds Knowledge Graph,
  none of Wikipedia's conflict-of-interest friction), then the Wikipedia *Elsie
  Clews Parsons* external links — **propose on the Talk page**, since adding a
  link to one's own work is a COI and tends to be reverted — then the AMNH
  Digital Library, which hosts the original and could also supply the handle
  `.zenodo.json` currently omits from `related_identifiers`.
- **Custom domain** — **decide this before seeding any inbound links.** Every
  link and citation placed from now on points permanently at whatever host is
  chosen, and most will never be updated. Note the old framing of this as "the
  strongest SEO upgrade" overstated it: Google treats `github.io` as a public
  suffix, so no authority is inherited from it and none is lost by leaving. The
  real argument is citation permanence and portability — a domain you own can
  change hosts without breaking a doi-adjacent link — which is an argument for
  doing it first or not at all. Drops onto this repo via a `CNAME` file.
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
