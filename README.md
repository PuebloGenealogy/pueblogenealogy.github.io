# Parsons 1923 — Genealogy I

A machine-readable, editable reconstruction of **Table 1, "Genealogy I"** from
Elsie Clews Parsons, *"Laguna Genealogies"*, Anthropological Papers
of the American Museum of Natural History, vol. 19 (1923).

104 individuals · 27 marriages · 80 parent–child links · 5 generation columns ·
two founding couples (1+2 and 54+55).

## Files

| Path | What it is | Published? |
|---|---|---|
| `data/parsons_genealogy_I.xlsx` | **Edit this.** The transcription plus your research columns. | No — git-ignored |
| `build/genealogy-i-private.html` | Local chart, includes your research columns. | No — git-ignored |
| `docs/` | Everything that goes on the public website. **Generated — never edit by hand.** | **Yes** |
| `sources/parsons-1923-table-1.jpg` | Source scan, 16172 × 11798 px. | In repo, not served |
| `scripts/transcription.py` | The 1923 baseline as data. Immutable. | Yes |
| `scripts/build_workbook.py` | Creates the workbook. **Overwrites your edits — don't re-run.** | Yes |
| `scripts/make_chart.py` | Rebuilds the chart. Safe to re-run. | Yes |
| `scripts/subset_font.py` | Rebuilds the embedded font subset. Rarely needed. | Yes |
| `vendor/gentium/` | SIL Gentium (OFL) plus the generated subset. | Subset only, inside the page |

## The two builds

```bash
python3 scripts/make_chart.py            # private -> build/  (may show research data)
python3 scripts/make_chart.py --public   # published -> docs/ (1923 baseline only)
```

The public build reads `scripts/transcription.py`, never the workbook. Before it
writes anything it greps its own output for English-name and census chips and
deletes the file if it finds either — so a leak fails loudly instead of sitting
in `docs/` waiting to be committed.

`--public` also regenerates `docs/index.html`, `robots.txt`, `sitemap.xml`,
`.nojekyll` and `docs/fonts/OFL.txt`.

### The privacy boundary

The public edition is **the 1923 transcription only** — no English names, no
census matches. This is enforced by structure, not by memory:

- `data/` and `build/` are git-ignored, so your research never enters git history.
- The public build reads `scripts/transcription.py`, which contains nothing but
  the 1923 baseline. There is no code path from the spreadsheet to `docs/`.
- `make_chart.py --public` scans its own output for research chips and aborts,
  deleting the file, if any appear. Verified by injecting one deliberately.

Git history is permanent — deleting a file later does not remove it. Run
`git status` and confirm no `.xlsx` is listed **before** your first commit.

## Workflow

Add English names, census matches and notes in the **green** columns of the
`PERSONS` sheet (`english_name`, `census_name`, `census_year`,
`match_confidence`, `notes`). Then:

```bash
python3 scripts/make_chart.py
```

The chart shows filled-in English names as highlighted chips and census matches
as blue chips, next to the Keresan name.

Grey columns are the 1923 transcription — leave them alone so the data stays
auditable against the plate. Blue columns are lookup formulas.

## Matching to census records

`name_ascii` is a diacritic-free lowercase key derived from `name_as_printed`
(`Kiwaʼd˙yuwi` → `kiwadyuwi`). Use it to join against census spellings, which
vary widely from Parsons' Americanist transcription.

## Things worth knowing about this plate

- **Clan descent is matrilineal.** Every sibling group carries its mother's clan.
  This held for all 27 unions and was used to verify the bracket readings.
- **Person 8 (Yu˙si) appears twice** — as husband of 7 and 73 in the upper half,
  and as a son of 58+59 in the lower half. He is the link between the two
  founding lines. The chart draws him once, with a cross-reference standing in
  for the repeated sibling group, exactly as the plate does.
- **Misprint at 76.** The `+` line under 76 is numbered *68* but names
  Shuwaiʼᶦri, Turkey — that is person **67**. Person 67's own cross-reference
  ("For second wife and offspring see below, 76, 90-3") confirms it. Recorded as
  67, with the misprint documented on union `U23`.
- **Persons 12 and 73** have further spouses and offspring in Genealogy II and
  III (Tables 2 and 3 of the same publication), not transcribed here. Their
  cross-references are preserved verbatim.
- **Blank names.** A dash on the plate means Parsons recorded no name; these are
  stored as empty `name_as_printed`, not as a dash.
- **`d.` alone** means died, date unknown.

## Adding another plate

Two documents govern this, for two different readers:

- **[METHOD.md](METHOD.md)** — the editorial method. Why readings are made the
  way they are, what the structural checks prove, what is and is not published.
  Read this to judge whether the edition is trustworthy.
- **`.claude/skills/transcribe-plate/SKILL.md`** — the working procedure, for
  Claude Code. Invoke it with `/transcribe-plate` when you have a new plate
  scan. It runs as a sequence of gates, each of which must pass before the next.

The single most useful thing to know: **clan descent is matrilineal, so clan
membership independently verifies every bracket you read.** If a sibling group
is attached to the wrong mother, the clans will disagree and the check fails.
That is what caught errors during Table 1, and it is why the structure can be
trusted.

## Adding Genealogy II and III

The schema already carries a `genealogy` dimension in spirit: `cross_ref` values
point at `Gen. II` / `Gen. III` ids. To merge those tables later, transcribe them
the same way and prefix ids by table (e.g. `II-158`) so cross-references resolve.
