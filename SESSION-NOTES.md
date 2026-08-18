# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-18**, at the end of a session that read Genealogy III's
**block 1**, re-checked the two readings `W31` had undermined, calibrated the
plate-audit rig for **Table 4**, and published two changes.

## Start here in a new chat

1. This file.
2. `scripts/plate_audit/README.md` **before running anything in it**. All three
   plates it has been pointed at are calibrated now — Table 1, Table 3 and
   Table 4 — and each set of parameters is per plate.
3. `CHANGELOG.md`'s two newest entries.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug; fix with `resize_window` at an
explicit `1280x900`. To see something far down the page, translate it into view
with `document.body.style.transform` rather than scrolling. **The pane caches
`/search/` hard** — bust it with `location.replace('/search/?v=' + Date.now())`.

## State

**Nothing is half-finished.** Working tree clean, `docs/` reproduces
byte-identically from `--public`, and everything this session did is **live and
verified page by page by SHA-256** — all seven pages `OK`, plus `search.js` and
`search-index.json` checked by hand, because the build's leak sweep only opens
`.html` and those two were exactly what changed. Sitemap 5 `<loc>`,
stale-identity count 0.

`laguna-search` is at **`80e0d2d`**, pushed. The post-publish `--refresh`
reported `re-fetched`, passed all seven of its gates, and returned all three
`dist/` files **byte-identical** to `vendor/search/`.

**Take all of that from the repo, not from here** — it is the least reliable
paragraph in this file, and this session proved it again: `laguna-search`'s two
commits were sitting local with a clean `git status` until the end.

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

Counts unchanged: 713 entries, 620 distinct people, 261/72/192 on III.

## The open thread — block 1's orthography

**Genealogy III's block 1 has been read for PLACEMENT and not for
ORTHOGRAPHY.** That distinction is the whole of what is known, and it is easy
to lose: the 2026-08-17 pass checked which stubs hang off which bracket, the
number printed against each stub, and every group's clan against its mother.
It did **not** re-read names, ages or diacritics. That is the one reading still
owed on this plate, and block 1 is 4300 of its 5503px.

Three things that would otherwise surface late:

- **Never run OCR.** It drops the diacritics, which are the object of this pass.
- **Crops read cleanly to ~5–8x; past that the upscaler invents letterform.**
  If a mark will not resolve, **ask for a photograph** — that is what settled
  the turned-comma question after the scan could not, and it is hours rather
  than weeks. Measure marks, don't eyeball them: height in rows, horizontal
  centroid of the bottom third minus the top third, and ink mass top vs bottom.
- **A character new to a name is not a one-line edit.** Four `_FOLD` maps here,
  plus `NAME_VOWELS` **or** `NAME_MARKS` and the `FOLD` map in `laguna-search`
  — and it can create a fourth namesake collision that stops their build. That
  gate is deliberately noisy; expect to adjudicate a pair.

The crops are regenerated with the commands in *Regenerating the crops* below.

## Regenerating the crops

The scratchpad does not survive a session. Table 3, block 1 in three chunks x
two overlapping strips, plus block 2 — native resolution, 830px of horizontal
overlap, and **chunk rather than magnify**: anything taller than ~1500px is
downscaled on display, which is what makes it illegible.

```bash
sips -s format bmp sources/parsons-1923-table-3.jpg --out /tmp/t3.bmp
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0  150 2300 1480 /tmp/b1-1.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470  150 2300 1480 /tmp/b1-1r.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 1590 2300 1480 /tmp/b1-2.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 1590 2300 1480 /tmp/b1-2r.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 3030 2300 1450 /tmp/b1-3.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 3030 2300 1450 /tmp/b1-3r.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp    0 4440 2300 1080 /tmp/b2-1.png
python3 scripts/plate_audit/crop.py /tmp/t3.bmp 1470 4440 2300 1080 /tmp/b2-1r.png
```

**A column-6 strip carrying the mother's column beside it** is what settled the
six groups the crease hides — `crop.py /tmp/t3.bmp 2250 <y> 1150 1450` at
y = 150, 1550, 2950 and (h=1100) 4400.

Table 4 is `sips -s format bmp sources/parsons-1923-table-4.jpg`; it is
12255 x 8409, so crop at native and chunk hard.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Block 1's orthography** | large, needs you | The open thread, above |
| `/search/` #5 — the Death filter | small, **needs a decision** | Accepts letters where Birth strips them, both labelled *Year*. Either strip like Birth, or relabel `Year or d.`. Upstream |
| The `/search/` provenance line's home | small, needs you | Offered four times, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name; its numbers are stale again |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`** — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** **What keeps it reachable is the branch `handoff-2026-08-09-search-link-safari-scroll`, local and on origin. Do not delete that branch in a stale-branch sweep** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **`W31` is a reading, not a rule.** The plate hangs some single-marriage
  leaders off the husband and some off the wife, ten rows apart (58+59 against
  60+61). Each is read off the ink; **do not sweep for more by pattern.**
- **"A spouse with no leader had no recorded issue" is FALSE** and must not be
  restated. 58 has no leader on her own line and two children. Where it was
  used — Gen. III's 85/86/87 and Gen. IV's 5/+6/+7 — both readings were
  re-measured and **both stand**, on the bases now recorded in `CLAUDE.md` and
  in `V04`'s note.
- **The row pitch is rarely what is wrong with an uncalibrated plate.** Table 4
  measured 145.8 against Table 1's 146.6. It was **the band**: a full-width one
  reads that plate's printed borders as brackets, and a band must hold the rule
  plus the 110px stub reach on **both** sides.
- **`--overshoot` widens the LEFT side only**, so it cannot rescue a stub above
  a rule's detected top. That is Table 4's `V01`, and it cascades into four of
  its ten problems.
- **The audit pairs a bracket to the group whose mother stands on its leader**,
  which makes the leader test tautological on purpose. **Do not "restore" the
  leader check by reverting the pairing** — pairing by `_GROUPS` order is what
  hid block 2's two real errors.
- **A pairing made by position is labelled a guess in the output**, and the
  label is load-bearing: every one of block 1's four count disagreements, and
  Table 4's, was the rig being wrong.
- **Calibration is per plate and the numbers do not transfer.**
- **The misprint display stays the plate's**, in the chart and on `/search/`.
  `data-reading` publishes the reading beside it; the tooltip now names it.
- **`/search/` panning at phone widths is the decision, not the defect.**
- **The upstream-vs-host test decides where a `/search/` change goes.** Would
  the widget standing alone want it?
- **Everything from previous sessions still stands**: the list is a table at
  every width; names wrap at editorial `<wbr>` seams; the default palette is
  light and CSS is what says so; Theme sits at the foot; a row's height is
  stated, not inferred; `laguna-search` stays a separate private repo;
  `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **Genealogy III block 1's PLACEMENT** — read 2026-08-17, right at every
  group; all 15 audit problems explained. Its orthography is the open thread.
- **85/86/87 (Gen. III) and 5/+6/+7 (Gen. IV)** — re-checked 2026-08-17, both
  stand. **Do not re-justify either as "a spouse with no leader had no issue".**
- **The plate-audit rig for Table 4** — calibrated 2026-08-18; its 10 problems
  are all explained. **Do not re-derive `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream and published
  2026-08-18.
- **Genealogy III block 2's parentage** — read and published 2026-08-17.
- **Genealogy I's placement** — read stub by stub 2026-08-17, all 76 matched.
- **De-indexing** — closed 2026-08-08. Nothing to be done.
- **Wikidata** — removed 2026-08-08. Do not reconstruct it or offer it.
- **Custom domain** — closed 2026-07-31. Durability beats portability.
- **Releases and Zenodo** — closed 2026-08-08. A doi reappearing is a
  regression.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Genealogy II's placements** — no remaining errors, 2026-07-30.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
