# Laguna Genealogies — a digital edition of Parsons 1923

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21637900.svg)](https://doi.org/10.5281/zenodo.21637900)

**https://pueblogenealogy.github.io/**

A machine-readable, searchable edition of the genealogical plates published with
Elsie Clews Parsons, *"Laguna Genealogies"*, **Anthropological Papers of the
American Museum of Natural History**, vol. 19, pt. 5 (1923), pp. 133–292.

| Plate | | |
|---|---|---|
| [Table 1 — Genealogy I](https://pueblogenealogy.github.io/genealogy-i/) | 104 individuals · 5 generations · 27 marriages · 80 parent–child links | founding couples 1+2, 54+55 |
| [Table 4 — Genealogy IV](https://pueblogenealogy.github.io/genealogy-iv/) | 73 individuals · 4 generations · 14 marriages · 58 parent–child links | founding couples 1+2, 59+60 |
| Table 2 — Genealogy II | in preparation | |
| Table 3 — Genealogy III | in preparation | |

The plates are transcribed character by character, including the Americanist
phonetic diacritics, and redrawn as text you can search, copy and cite. Nothing
is corrected, normalised or filled in: misprints are reproduced and annotated
rather than silently fixed, and where Parsons recorded no name the entry stays
blank.

## The privacy boundary

**The published edition is the 1923 transcription only** — no English names, no
census matches, no identification of living people. This is enforced by
structure, not by memory:

- `data/` and `build/` are git-ignored, so research never enters git history.
- The public build reads `scripts/transcription*.py`, which contain nothing but
  the 1923 baseline. There is no code path from the spreadsheet to `docs/`.
- `make_chart.py --public` scans its own output for research chips and aborts,
  deleting the file, if any appear. Verified by injecting one deliberately.

Git history is permanent — deleting a file later does not remove it, and any
clone made in the meantime keeps it. Run `git status` and confirm no `.xlsx` is
listed **before** your first commit.

## Files

| Path | What it is | Published? |
|---|---|---|
| `scripts/make_chart.py` | The renderer: layout, CSS, JS, metadata. Everything visual lives here | Yes |
| `scripts/transcription.py`, `transcription_iv.py` | The 1923 baseline as data. Immutable | Yes |
| `docs/` | The public website. **Generated — never edit by hand** | **Yes** |
| `assets/og-cover.jpg` | Social preview card, derived from the plate scan | Yes |
| `sources/` | Source scans (Table 1 is 16172 × 11798 px) | In repo, not served |
| `vendor/gentium/` | SIL Gentium (OFL) plus the generated subset | Subset only, inside the page |
| `data/parsons_genealogy_I.xlsx` | Transcription plus private research columns | No — git-ignored |
| `build/` | Local build including research columns | No — git-ignored |

## Build

```bash
python3 scripts/transcription.py          # structural self-check
python3 scripts/make_chart.py --public    # the published site -> docs/
python3 scripts/make_chart.py             # private build -> build/ (needs data/*.xlsx)
```

`--public` regenerates the chart pages, the landing page, `404.html`,
`robots.txt`, `sitemap.xml`, `.nojekyll`, `og-cover.jpg` and
`docs/fonts/OFL.txt`. **Everything in `docs/` is output.** To change the design,
edit `make_chart.py`.

Preview locally on port 4173:

```bash
python3 -m http.server 4173 --directory docs
```

## Things worth knowing about these plates

- **Clan descent is matrilineal.** Every sibling group carries its mother's
  clan. This held across all unions and was used to verify the bracket
  readings — it is what caught errors during Table 1, and it is why the
  structure can be trusted. If a sibling group is attached to the wrong mother,
  the clans disagree and the check fails.
- **Person 8 (Yu˙si) appears twice** on Table 1 — as husband of 7 and 73 in the
  upper half, and as a son of 58+59 in the lower half. He is the link between
  the two founding lines. The chart draws him once, with a cross-reference
  standing in for the repeat, exactly as the plate does.
- **Misprint at 76 (Table 1).** The `+` line under 76 is numbered *68* but names
  Shuwaiʼᶦri, Turkey — person **67**. Person 67's own cross-reference confirms
  it. The chart **prints 68, as the plate does**, ringed in red, links it to 67,
  and sets *(misprint, click here to see notes)* on the row beneath, which jumps
  to the editorial note. The reading is recorded on union `U23` and declared in
  `PLATE_NUMBER_MISPRINTS`.
- **Persons 12 and 73** have further spouses and offspring in Genealogies II and
  III, not yet transcribed. Their cross-references are preserved verbatim.
- **Blank names.** A dash on the plate means Parsons recorded no name; these are
  stored as empty `name_as_printed`, not as a dash.
- **`d.`** means the person had already died when Parsons recorded the
  genealogy, during her fieldwork of 1918–19. `d.` alone means she did not
  record the year; `d. 1913` that she did. A number after a name is that
  person's age when the data was collected.
- **Dates of record.** Genealogy I was taken in February 1918; Parsons returned
  in June 1919 for Genealogies II, III and IV, and revised Genealogy I on that
  visit, chiefly the spelling of the names.
- **English names in parentheses on Table 4** (Hugh, Frank, Paul and Joe
  Johnson, and Mana) are *printed on the plate*. They are transcription, not
  additions to it.

## Matching to census records

`name_ascii` is a diacritic-free lowercase key derived from `name_as_printed`
(`Kiwaʼd˙yuwi` → `kiwadyuwi`). Use it to join against census spellings, which
vary widely from Parsons' Americanist transcription.

## Provenance and use

This is Laguna Pueblo material. Parsons's Laguna fieldwork is itself contested:
she published information that members of the community regarded as restricted.
This edition transcribes an already published source and adds no new information
about the community. It is offered as a finding aid for the printed record.

The 1923 publication is in the public domain in the United States. The
transcription, encoding and layout are by Elizabeth Heger-Vlahovic and are
released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please
cite both this edition and Parsons — see [`CITATION.cff`](CITATION.cff).

Each release is archived at Zenodo. Cite
[**10.5281/zenodo.21637900**](https://doi.org/10.5281/zenodo.21637900), which
always resolves to the current version; a citation made against it keeps working
when Tables 2 and 3 are added. Individual releases also carry their own DOI if
you need to pin one — v1.0.0 is
[10.5281/zenodo.21637901](https://doi.org/10.5281/zenodo.21637901).

Corrections are welcome and are recorded as dated commits, so the edition carries
its own revision history.

## Adding a plate

`make_chart.py` is table-agnostic. Add an entry to `TABLES`, remove the matching
`PENDING` entry, write `scripts/transcription_<n>.py` on the same schema, then
run `--public`. Counts in the page copy are computed from the data, never typed.

Two documents govern this, for two different readers:

- **[METHOD.md](METHOD.md)** — the editorial method. Why readings are made the
  way they are, what the structural checks prove, what is and is not published.
  Read this to judge whether the edition is trustworthy.
- **`.claude/skills/transcribe-plate/SKILL.md`** — the working procedure, run
  with `/transcribe-plate`. A sequence of gates, each of which must pass before
  the next.

Cross-references already point at `Gen. II` / `Gen. III` ids; when those tables
are transcribed, prefix ids by table (e.g. `II-158`) so they resolve.
