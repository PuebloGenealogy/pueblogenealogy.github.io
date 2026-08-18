# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-17**, at the end of a session that calibrated the plate
audit for Genealogy III, found **two placement errors** in its block 2, and
published them.

## Start here in a new chat

1. This file — the open thread is *Genealogy III block 1*, below.
2. `scripts/plate_audit/README.md` **before running anything in it**. Table 3
   is calibrated there now and **Table 4 still is not**.
3. `CHANGELOG.md`'s newest entry — this session.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **The pane caches `/search/` hard** — bust it with
`location.replace('/search/?v=' + Date.now())`. A narrow-viewport check needs a
**fixed-width iframe**, not `resize_window`. `await document.fonts.ready`
inside the iframe before measuring anything about text.

## State

**Nothing is half-finished.** Working tree clean, no open PRs, `main` at
**`c1a73c0`**, and `--public` exits 0 with `docs/` reproducing
**byte-identically** — no date drift.

**Take that from the repo, not from here** — it is the least reliable sentence
in this file:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

**The edition changed and is live**, verified page by page by SHA-256, with the
search index re-vendored and re-verified. Counts are unchanged — 261 persons,
72 unions, 192 child links on III; 713 entries, 620 distinct people overall.

## What was corrected, and what it means

**Genealogy III's block 2 gave up two placement errors, both on one bracket
column, both settled by the user reading the scan at 1:1:**

- **238 and 8 are 230+231's sons**, not 236+237's.
- **243, 245 and 246 are 236+237's**, not 232+233's.

Every person involved is **Parrot**, so clan descent was blind, and the counts
closed identically on the wrong readings — all four `self_check()`s passed
before and after. That is the third such case, after IV's Bear and II's Water.

**Person 8's generation had been contradicting the old reading in plain sight**
— already 3, when a child of 236 would be 4. Nothing compared the two.

## THE OPEN THREAD — Genealogy III block 1, and column 6 above all

**Block 1 is 4300 of the plate's 5503px and no human has read it.** The
calibrated audit produced **no new finding there**, which is not the same as
correct:

- the audit **cannot read type**, so a group of the right size whose members
  are misnumbered passes silently — and a misnumbering is exactly what today's
  two corrections were *not*, so nothing rules it out;
- **column 6's six groups sit under the third fold crease** and are invisible
  to the tool altogether. **This is the batch worth the user's time**, at
  x ≈ 2790–2870.

### Regenerating the crops — the scratchpad is gone

```bash
sips -s format bmp sources/parsons-1923-table-3.jpg --out /tmp/t3.bmp
# block 1, three chunks x two overlapping strips; native resolution
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0  150 2300 1480 /tmp/b1-1.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470  150 2300 1480 /tmp/b1-1r.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 1590 2300 1480 /tmp/b1-2.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 1590 2300 1480 /tmp/b1-2r.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 3030 2300 1450 /tmp/b1-3.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 3030 2300 1450 /tmp/b1-3r.png
# block 2, already read
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 4440 2300 1080 /tmp/b2-1.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 4440 2300 1080 /tmp/b2-1r.png
```

Eight images cover the whole plate at 1:1 with 830px of horizontal overlap.
**Native scale is legible and anything taller than ~1500px gets downscaled on
display**, which is what makes it illegible — chunk rather than magnify.

### Re-running the audit

```bash
python3 scripts/plate_audit/brackets.py /tmp/t3.bmp '[[0,3770]]' 12 \
    --row=24.75 --track=1 --maxthick=6 --ongrid=0.25 --gapmax=10 \
    --overshoot=18 > /tmp/t3.json
python3 scripts/plate_audit/audit.py transcription_iii.py /tmp/t3.json \
    2:673,3:1213,4:1740,5:2270,6:2830,7:3400 75 --row=24.75
```

**15 problems today, and none is a new finding.** Read them in this order:

- **W13** — the only count disagreement matched by *identity*, and already
  explained: 22's vertical is over-drawn past 82 to reach 83, who is 25's
  child. Confirmed 2026-07-31, noted on both persons. **Not a defect.**
- **W12, W37, W40, W52** — count disagreements, all **paired by position**,
  which the output labels. Treat as guesses; that is the basis that produced
  today's false alarms.
- **W53, W54, W55, W58, W60, W71** — bracketless, all column 6, all crease.
- **W19, W31, W69, W47** — leader flags, all on positional pairs, so evidence
  about the guess and not about the plate.

**The count is 15, and this file said 14 for an hour** because the figure was
read off a `tail -14` that had truncated the list rather than counted it.
`grep -cE "^  - "` is the count; anything else is the terminal's opinion.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy III block 1** | large, needs you | The open thread. Column 6 first — the tool cannot see it |
| Calibrate the rig for **Table 4** | medium | Still uncalibrated; its eight old flags were the rig's own noise. `--row` is the first thing to measure |
| `/search/` #5 — the Death filter | small, **needs a decision** | Accepts letters where Birth strips them, both labelled *Year*. Either strip like Birth, or relabel `Year or d.`. `?d=d.` returns all 115 with a recorded death. Upstream |
| `/search/` #6a — `?open=` | small | Can name a row that is not open, so a shared URL reopens a row the sender was not looking at. Upstream |
| The `sic` tooltip could name the reading | tiny | `data-reading` exists, so *"the edition reads F"* beats *"the edition's reading differs"*. Upstream copy, never raised with the user |
| The `/search/` provenance line's home | small, needs you | Offered four times, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name; its numbers are stale again |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`** — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** **What keeps it reachable is the branch `handoff-2026-08-09-search-link-safari-scroll`, local and on origin.** **Do not delete that branch in a stale-branch sweep** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — one settled the turned-comma question after the scan could not. `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **The audit pairs a bracket to the group whose mother stands on its leader**,
  and that makes the leader test tautological on purpose. Pairing by `_GROUPS`
  order is what hid both of today's errors. What it buys is three tests with
  teeth — mismatched counts, an unclaimed bracket, a bracketless group. **Do
  not "restore" the leader check by reverting the pairing.**
- **A pairing made by position is labelled as a guess in the output.** That
  label is load-bearing: three of today's four count disagreements carry it,
  and acting on one unlabelled is how the second real error was nearly missed.
- **Calibration is per plate and the numbers do not transfer.** Table 3 needed
  `--row=24.75 --track=1 --maxthick=6 --ongrid=0.25 --gapmax=10
  --overshoot=18`; Table 1's defaults are unchanged and Table 1 must keep
  reading 24 groups / 20 verticals / 76 stubs / no disagreement.
- **`--skew` exists and fits nothing.** Table 3 bows rather than skews; the
  linear model was built, measured at −0.0051, and kept only as the model that
  does not work. `--track` is the one that does.
- **`--overshoot` widens the LEFT side only.** Widening the right picks up the
  last stub of the group above and breaks correct child counts — measured, 33
  problems to 37.
- **The misprint display stays the plate's.** `/search/` and the chart both
  show the misprinted `M.`/`Bager`, ringed; `data-reading` publishes the
  edition's reading beside it without changing what is shown.
- **`/search/` panning at phone widths is the decision, not the defect**, and
  the bar sliding off while panned is fixed —
  `body{width:fit-content;min-width:100%}`.
- **Find matches the printed number**, and the id is only the fallback.
- **The upstream-vs-host test decides where a `/search/` change goes.** Would
  the widget standing alone want it?
- **Everything from previous sessions still stands**: the list is a table at
  every width and the document pans; names wrap at editorial `<wbr>` seams; the
  default palette is light and CSS is what says so; Theme sits at the foot; a
  row's height is stated, not inferred; `laguna-search` stays a separate
  private repo; `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **Genealogy III block 2's parentage** — read against the scan and published
  2026-08-17. Do not re-open 230+231, 232+233 or 236+237.
- **Genealogy I's placement** — read stub by stub on 2026-08-17, all 76
  matched.
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
