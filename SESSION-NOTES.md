# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-17**, at the end of a session that read **Genealogy III's
block 1** against the scan, found the transcription right at every group, and
published one change.

## Start here in a new chat

1. This file. **There is no open thread on any plate** — see *State*.
2. `scripts/plate_audit/README.md` before running anything in it. Table 3 is
   calibrated; **Table 4 still is not**.
3. `CHANGELOG.md`'s newest entry — this session.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug; fix with `resize_window` at an
explicit `1280x900`. To see something far down the page, translate it into view
with `document.body.style.transform` rather than scrolling. **The pane caches
`/search/` hard** — bust it with `location.replace('/search/?v=' + Date.now())`.

## State

**Nothing is half-finished.** Working tree clean, `main` at **`bac9c4f`**, and
the change is **live and verified page by page by SHA-256**, all seven pages
`OK`, stale-identity count 0, sitemap 5 `<loc>`.

**Take that from the repo, not from here** — it is the least reliable sentence
in this file:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

Counts unchanged: 261 persons, 72 unions, 192 child links on III; 713 entries,
620 distinct people overall.

`laguna-search` is clean at `44e3d7b` and **was re-run with `--refresh` after
the publish** — cache re-fetched, all seven of its gates passed, and all three
of its `dist/` files came back **byte-identical** to `vendor/search/`. No
re-vendor was due, and that was established twice: the publish's diff of the
table page carried **0** register-bearing changes.

## What was read, and what it settled

**Genealogy III's block 1 — 4300 of the plate's 5503px — had never been read by
a human. It has now been, group by group, and the transcription is right at
every group.** All 15 of the calibrated audit's problems are explained and none
is a defect; the full account is in `CHANGELOG.md` and the short version in
`scripts/plate_audit/README.md`. In brief: the six "bracketless" groups are real
brackets the fold crease hides, the four count disagreements are the rig losing
a stub across a tall *See Gen.* row, and three of the four leader flags are its
row model tripping over the same rows.

**The 15 are now a known-clean baseline.** A 16th problem, or a change in which
W-ids appear, is the signal — re-run and **diff the list**, don't read it fresh.

**The one real finding was about the ink, not the reading:** the plate hangs
58 + 59 → 143, 144 off the **husband's** line. `W31` joined `W26` in
`LEADER_ON_SPOUSE_ROW` — presentational only, parentage untouched — and shipped.
**The plate is not consistent about it**: 60 + 61 → 145 is the identical shape
with the leader on 60's own line. Both are now drawn as printed. Do not
generalise `W31` into a rule.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Block 1's orthography** | large, needs you | The one half not done. This pass read membership, stub numbers and clan descent — **not** names, ages or diacritics |
| Calibrate the rig for **Table 4** | medium | Still uncalibrated; its eight old flags were the rig's own noise. `--row` is the first thing to measure |
| `/search/` #5 — the Death filter | small, **needs a decision** | Accepts letters where Birth strips them, both labelled *Year*. Either strip like Birth, or relabel `Year or d.`. Upstream |
| `/search/` #6a — `?open=` | small | Can name a row that is not open, so a shared URL reopens a row the sender was not looking at. Upstream |
| The `sic` tooltip could name the reading | tiny | `data-reading` exists, so *"the edition reads F"* beats *"the edition's reading differs"*. Upstream copy, never raised with the user |
| The `/search/` provenance line's home | small, needs you | Offered four times, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately. Offered four times |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`** — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** **What keeps it reachable is the branch `handoff-2026-08-09-search-link-safari-scroll`, local and on origin. Do not delete that branch in a stale-branch sweep** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — one settled the turned-comma question after the scan could not. `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **`W31` is a reading, not a rule.** The plate hangs some single-marriage
  leaders off the husband and some off the wife, ten rows apart. Each is read
  off the ink; don't sweep for more by pattern.
- **The audit pairs a bracket to the group whose mother stands on its leader**,
  which makes the leader test tautological on purpose. Pairing by `_GROUPS`
  order is what hid 2026-08-17's two block-2 errors. **Do not "restore" the
  leader check by reverting the pairing.**
- **A pairing made by position is labelled as a guess in the output**, and the
  label is load-bearing — all four of block 1's count disagreements were the rig
  being wrong, exactly as the label warned.
- **Calibration is per plate and the numbers do not transfer.** Table 3 needs
  `--row=24.75 --track=1 --maxthick=6 --ongrid=0.25 --gapmax=10 --overshoot=18`;
  Table 1's defaults are unchanged and must keep reading 24 groups / 20
  verticals / 76 stubs / no disagreement.
- **`--skew` exists and fits nothing.** Table 3 bows rather than skews.
  `--track` is the one that works.
- **`--overshoot` widens the LEFT side only.** Widening the right breaks correct
  child counts — measured, 33 problems to 37.
- **The misprint display stays the plate's.** `/search/` and the chart both show
  the misprinted `M.`/`Bager`/`Chapparral Cock`, ringed.
- **`/search/` panning at phone widths is the decision, not the defect.**
- **Find matches the printed number**, and the id is only the fallback.
- **The upstream-vs-host test decides where a `/search/` change goes.** Would
  the widget standing alone want it?
- **Everything from previous sessions still stands**: the list is a table at
  every width and the document pans; names wrap at editorial `<wbr>` seams; the
  default palette is light and CSS is what says so; Theme sits at the foot; a
  row's height is stated, not inferred; `laguna-search` stays a separate private
  repo; `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **Genealogy III block 1** — read against the scan 2026-08-17. The
  transcription is right at every group; all 15 audit problems explained.
- **85/86/87 (Gen. III) and 5/+6/+7 (Gen. IV)** — both re-checked against the
  scans 2026-08-17 after `W31` disproved the rule they leaned on, and **both
  readings stand**. Measured in each case: the mother's row carries a solid
  rule, **both husbands' rows are bare**, so the one leader names no father by
  itself. 85/86/87 is settled by Gen. III's own 43; 5/+6/+7 has no such example
  on Table 4 and its basis is **cross-plate**, propped up locally by the bracket
  being drawn inside 5's block. Bases are recorded in `CLAUDE.md` and in V04's
  note. **Do not re-justify either as "a spouse with no leader had no issue".**
- **Genealogy III block 2's parentage** — read and published 2026-08-17. Do not
  re-open 230+231, 232+233 or 236+237.
- **Genealogy I's placement** — read stub by stub 2026-08-17, all 76 matched.
- **De-indexing** — closed 2026-08-08. Not important, nothing to be done.
- **Wikidata** — removed 2026-08-08. Do not reconstruct it or offer it.
- **Custom domain** — closed 2026-07-31. `pueblogenealogy.github.io`
  permanently; durability beats portability.
- **Releases and Zenodo** — closed 2026-08-08. A doi reappearing is a
  regression.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD,
  published. Do not re-crop the scan.
- **Genealogy II's placements** — the user re-checked their full list on
  2026-07-30 and reported no remaining errors.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
