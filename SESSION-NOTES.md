# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-17**, at the end of a session that read **Genealogy I
against its plate** and built the rig that made it cheap.

## Start here in a new chat

1. This file — the open thread is *Genealogy III*, below, and it is now the
   **only** plate no human has read against its scan.
2. `scripts/plate_audit/README.md` **before running anything in it**. The
   calibration section is not optional; an uncalibrated run produces confident
   flags that are the tool's own noise.
3. `CHANGELOG.md`'s newest entry — this session. The one before it is the
   2026-08-16 debug report and the publish that followed.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **The pane caches `/search/` hard** — bust it with
`location.replace('/search/?v=' + Date.now())`. A narrow-viewport check needs a
**fixed-width iframe**, not `resize_window`. `await document.fonts.ready`
inside the iframe before measuring anything about text.

## State

**Nothing is half-finished.** Working tree clean, no open PRs, `main` at
**`ef143ad`** and 0/0 with origin before this session's handoff branch.
`--public` exits 0 — 7 pages, 713 drawn, 10 JSON-LD blocks valid — and a
rebuild reproduces `docs/` **byte-identically**, not even date drift.

**Take that from the repo, not from here** — it is the least reliable sentence
in this file, and `/wrap-session` writes it before the last PR merges:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

**Nothing in the edition changed this session.** No transcription, no
`make_chart.py`, no `docs/`. What landed is a verification, a new tool under
`scripts/plate_audit/`, and three documentation fixes.

## Genealogy I is read, and this is exactly what that means

**The user read the printed number against all 76 of its bracket stubs on
2026-08-17 and every number matched.** Before that, the plate's ink was
measured at 1:1 and reconciled with `_GROUPS`: 24 groups, child counts group
for group, groups in the claimed column and order, every leader on its mother's
line within 9px of a 146.6px row.

So **Genealogy I joins II (2026-07-30) and IV's 5/6/7 (2026-08-10)** as read
against the scan by a human. It does **not** mean the whole edition is checked.

## THE OPEN THREAD — Genealogy III, the last unread plate

**261 people, 72 unions, seven generations, two descent blocks, the second
indented.** No human has read it against its scan. It is the site's largest
remaining correctness risk, and the risk is specific: Genealogy IV shipped with
20 on the wrong marriage and survived four `self_check()`s, every publish gate
and ten days live, because 19 and 20 are both Bear like their mother and the
counts close either way.

**The rig is built and the method is proven — what is left is calibrating it
for III's scan and then the user's reading.** In order:

1. **Calibrate.** `sips -s format bmp sources/parsons-1923-table-3.jpg` to
   scratch, run `brackets.py` over candidate bands, and check the
   **stub-to-stub gap distribution is bimodal**. Table 3 is 3770 × 5503 — a
   ninth of Table 1's pixel count — so expect different thresholds, and expect
   this to take a round or two. Do not skip to step 2 on an unbimodal
   distribution.
2. **Measure the columns by eye, once.** Pass them to `audit.py` explicitly.
   Auto-clustering returns the fold crease and a column of type among the real
   columns and silently calls the crease a generation. **III's second descent
   block is indented**, so its columns may not line up with the first block's —
   that is a real complication Table 1 did not have, and it may need the two
   blocks audited separately.
3. **Note `LEADER_ON_SPOUSE_ROW`.** III·43 has two husbands with issue by both,
   printed once, and its bracket hangs off the **'+' spouse's** line. `audit.py`
   reads that declaration, but it is the one place the "leader is on the
   mother's line" rule does not hold.
4. **Then the user reads crops.** `crop.py`, native resolution, one strip per
   column per block, ~2300px wide so number, name and clan are all legible —
   1760px cut the clan off on Table 1. They asked for **a batch per descent
   block**.

**Their reading wins on placement. Present the crop and the evidence; never
change a transcription unilaterally.**

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy III** | large, needs you | The open thread above. Nothing else competes with it |
| `/search/` #5 — the Death filter | small, **needs a decision** | Accepts letters where Birth strips them, both labelled *Year*. Either strip like Birth, or relabel `Year or d.` and keep the power. `?d=d.` returns all 115 people with a recorded death. Upstream |
| `/search/` #6a — `?open=` | small | Can name a row that is not open, so a shared URL reopens a row the sender was not looking at. Upstream |
| The `sic` tooltip could name the reading | tiny | `data-reading` exists now, so *"the edition reads F"* beats *"the edition's reading differs"*. Upstream copy change, never raised with the user |
| The `/search/` provenance line's home | small, needs you | Offered three times, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered three times |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name; its numbers are stale again |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — one settled the turned-comma question after the scan could not. `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **Genealogy IV was not touched, and its eight audit flags are noise.** The
  uncalibrated rig flagged eight leaders on IV, four at a constant ~+176px
  against a nominal 146px row. That is the rig's own fragmented stub detection
  corrupting the row pitch, not eight plate errors. IV stands as the user
  checked it on 2026-08-10. **Do not "fix" anything on the strength of those
  flags** — recalibrate first, or leave it.
- **The plate audit cannot read type, by design.** It decides counts, column,
  order and leader row. A group of the right size whose members are misnumbered
  passes silently. Do not report a clean audit as "the plate is verified".
- **Calibration is per plate.** Table 1's parameters fragment Table 4's stubs.
  Check the gap distribution before believing a flag.
- **The misprint display stays the plate's.** `/search/` and the chart both show
  the misprinted `M.`/`Bager`, ringed; `data-reading` publishes the edition's
  reading beside it without changing what is shown.
- **`/search/` panning at phone widths is the decision, not the defect.** The
  bar sliding off while panned was the real half of that report and **is
  fixed** — `body{width:fit-content;min-width:100%}`, no rule in the bar
  changed. `max-content` is the wrong tool that looks right.
- **Find matches the printed number, and the id is only the fallback.** The
  datalist `value` stays the **id**.
- **The upstream-vs-host test decides where a `/search/` change goes.** Would
  the widget standing alone want it?
- **Everything from the previous sessions still stands**: the list is a table at
  every width and the document pans; names wrap at editorial `<wbr>` seams; the
  default palette is light and CSS is what says so; Theme sits at the foot; a
  row's height is stated, not inferred; `laguna-search` stays a separate private
  repo; `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **Genealogy I's placement** — read stub by stub against the scan on
  2026-08-17, all 76 matched. Do not re-audit it.
- **De-indexing** — closed 2026-08-08. Not important, nothing to be done.
- **Wikidata** — removed 2026-08-08. Do not reconstruct it or offer it.
- **Custom domain** — closed 2026-07-31. `pueblogenealogy.github.io`
  permanently; durability beats portability.
- **Releases and Zenodo** — closed 2026-08-08. A doi reappearing is a
  regression.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD,
  published. Do not re-crop the scan. *(Its bracket placement is a different
  question and is the open thread.)*
- **Genealogy II's placements** — the user re-checked their full list on
  2026-07-30 and reported no remaining errors.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
