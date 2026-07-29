# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-29**, after a session of **transcribing Genealogy II**.
Half the plate is read. Nothing is published.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch table-ii-transcription`.** The work is on a branch, not `main`.
2. Read `scripts/transcription_ii.py` — top to bottom. It is the work in
   progress and it carries its own state block, the confirmed bracket structure,
   and both editorial decisions. It is the primary handoff; this file is the map.
3. Read `CLAUDE.md` — **The one thing to get right** and **Design invariants**.
4. Read the top of `CHANGELOG.md`.
5. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-29**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing.

**Four habits this project keeps re-learning:**

- **Measure, don't look.** Drift, contrast, row heights, bracket alignment.
- **Grep the built file, not the rendered DOM.**
- **Read the staged diff before committing.**
- **Ask what *clears* a state, not only what sets it.**

And one this session added, at some cost:

- **Judge structure at native resolution.** The 1470px overview appeared to show
  three founding couples in Genealogy II's left column. There is one. At native
  resolution 5 and 7 sit in the same column as 3, all carried by a single rule
  off person 1's row. An overview is for orientation and tile planning, never
  for a reading.

## State

**Half-finished, deliberately, and safe.** `main` is untouched and clean. No
open PRs. `docs/` is byte-identical to its committed state — a rebuild on
2026-07-29 produced no diff, and `--public` exits 0 reporting 104 and 73 persons
across 4 pages. **Nothing about Genealogy II is registered or rendered.** The
live site is exactly as it was.

Branch `table-ii-transcription`, two commits: `c1aa97f` (the read and the
findings), `de42460` (the decisions).

What exists: `scripts/transcription_ii.py` with **plate numbers 1–171 and
232–233** — 174 records, no gaps in what it claims, no id collisions.
`PERSONS` only.

What does not: **101 plate numbers are unread** — 172–231 and 234–274. And
`UNIONS` / `CHILDREN` are **empty stubs for the whole plate**, including the
part already read. The bracket structure traced so far is a comment block in
that file and needs encoding, not re-deriving.

**The numbering runs to 274, not 269.** The first orientation pass missed
270–274 at the far right of the lower block.

## The open thread

**Finish Genealogy II.** In this order:

1. **Read the remaining 101.** The module's `STATE` block lists the native
   pixel coordinates to resume from, column by column. Tile ~1450 × 1200 at
   native resolution — that reads cleanly with no downscaling. Write each
   tile's rows into the module *before* reading the next one, and commit every
   few tiles; this plate is too big to hold a read in conversation safely.
2. **Encode `UNIONS` and `CHILDREN`** for the whole plate. Upper-block
   generations 1–4 and part of the lower block are already traced — see
   `STRUCTURE CONFIRMED SO FAR`. Generations 4→5, 5→6 and most of the lower
   block still need it.
3. **Resolve the readings marked `SEE TODO`** — about a dozen, each a tighter
   crop's work.
4. **Gate 3**, then font subset, then register in `TABLES` and render.

Constraints that will surface late if you don't know them:

- **The two blocks are one genealogy.** 13, 14, 53, 54, 125 and 126 are drawn
  in the upper block and reappear in the lower with "see above"; 169 repeats
  inside the lower block. **Store each once** — the ids already exist, so a
  second record is a duplicate, not a new person.
- **Three founding couples**, not two: 1+2, 154+155, 232+233. The third is
  printed at a child's indent and is only distinguishable by the absence of a
  leader rule, plus its clan.
- **The plate's own numbering is not a unique key.** Two people are numbered
  101. The decision is taken (internal id, printed number, both rows show 101);
  it is not implemented, and `self_check()`'s `ids == range(1, N+1)` test has to
  accommodate it.
- **Genealogy III is referenced but not transcribed.** Persons 160 and 163 both
  point into it. A link must not promise content — `#pending-3` exists for this,
  and nothing may link to Genealogy III until it ships.
- **Editing Table 1's apparatus is part of this job.** The cross-reference
  finding goes on Table 1's `#note-misprint` as well as Table 2's. That page is
  published and cited — re-verify after building, and route every person
  reference through `_p()`, never a regex over the prose.
- **Table 2 is six generations.** Table 1 is five. `NUMBER_WORDS` covers 3–7 so
  the copy is fine, but nothing in the layout has been measured at six columns.
  Column drift must still be **0 px at every generation**.
- **One unresolved discrepancy**: person 13 reads `Dzia˙ʼyotsʼa` in the upper
  block and `Tsiaiutsa` in the lower. Both tiles were legible. Re-read both
  before Gate 3.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Table 3** | Large, and harder than Table 2 | Scan is in `sources/` at 3770 × 5503 — **a ninth of Table 1's pixel count**. Do not start it in the same session as anything else |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable now, so this is the open item with a correctness edge |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| Wikidata item | ~10 min, **needs the user** | Payload ready at `wikidata-quickstatements.txt`, 18 ids verified. Not urgent |
| AMNH Digital Library | Slow, **needs the user** | No longer needed as a source for the plates, but still a strong inbound link and the handle `.zenodo.json` omits |

**Do not cut a GitHub release** until Genealogy II actually lands. Zenodo's
webhook mints a version doi from it, and that doi is worth spending on a new
plate rather than on a half-read one.

## Decisions already made — don't re-litigate

**From this session:**

- **Duplicate 101: internal id for addressing, printed number for display.**
  Both rows print 101, because the chart prints what the plate prints.
  `101a`/`101b` was considered and rejected for exactly that reason.
- **The cross-reference offset is noted on both published pages**, Table 2's
  apparatus and Table 1's `#note-misprint`. It is a claim about Parsons's
  numbering, not about any person, so the privacy boundary is not in play.
- **Genealogy II has one founding couple.** 1+2, whose daughters are 3, 5 and 7.
  If a later reading suggests three couples, it is reading the overview.
- **Illegible passages: the user supplies the reading, and it is used as given** —
  no footer note, no chart marker. The reason goes in `plate_note`, which is
  inert in the renderer (read once, only to test for `"braced"`). **If a reading
  comes from the census research, its source must not be named anywhere in the
  repo** — that file is public and git history is permanent.
- **A half-read plate is not registered.** `TABLES` stays untouched until
  `self_check()` passes, so `--public` can never render a partial genealogy.

**Standing, from earlier sessions:**

- **A chart row's highlight is class-driven wherever the card script runs.**
  Re-enabling `:target` alongside `.is-selected` re-opens the bug it fixed.
- **The plate bar has no max-width, on purpose** — it aligns to the plate.
- **The ruler's height is load-bearing.** It holds the identity chip off the
  generation labels.
- **The person card carries the number, never the annotation.**
- **No per-clan colours, and no colour-coding of sex.** Both built and reverted.
  Three colours on a table page are not `--ink`: `--sic`, `--muted-fixed`,
  `--clan`. A fourth needs the same evidence.
- **No on-page chart key.** Built twice, removed twice.
- **The plate's misprint is reproduced, not corrected.** Table 1 prints **68**.
  This session found independent corroboration that 68 is Parsons's own number.
- **The edition asserts one thing the plate does not** — the paternity of 83–85.
  Read `METHOD.md` → *Editorial attribution* before adding another.
- **Research evidence never enters the repo.** The gate protects `docs/` only,
  reads prose as well as markup, and fails closed.
- **No custom domain** for now.
- **Publishing goes through `/publish`.**

## Closed — do not re-raise

- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file.
- **Tables 2 and 3 are no longer blocked on scans.** Both are in `sources/`.
  The design-settling argument for holding them back has been overtaken by the
  user's decision to transcribe Table 2 now.
- **Genealogy II's font coverage.** `ŏ` U+014F, `ˑ` U+02D1 and `ᵉ` U+1D49 are
  all in both master Gentium faces, checked against the cmap. Nothing to source;
  Gate 4 is a `subset_font.py` re-run. Do not re-open this by looking at
  rendered text — macOS substitutes silently.
