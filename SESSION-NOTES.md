# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

**It points at `CLAUDE.md`; it does not restate it.** Anything permanent that
turns up in a session belongs there, not here — this file is designed to be
thrown away.

Last updated **2026-08-23** (second session that day). It settled
`TABLE2-BENCH.md`'s only open flag — **Genealogy II·248 and 249's medial
marks** — corrected 248, published it, re-vendored the search index, and had
the two owed checks run from the Mac. **Everything is merged, deployed and
hash-verified.** `main` is `7f1a277`.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the *248's medial marks* block.
3. `scripts/plate_audit/TABLE2-BENCH.md` before touching Genealogy II's
   brackets or the rig's 23, and `scripts/plate_audit/README.md` before running
   anything in that directory.
4. **If this session is running remotely** — `CLAUDE.md` → *Environment*. That
   section was substantially rewritten this session: a remote session can now
   run the whole publish loop **including gate 8's re-vendor** (`laguna-search`
   attaches with `add_repo`), and only `/publish` gate 6 and `build.py
   --refresh` are out of reach.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. Its three traps — a blank screenshot is a zero-sized
viewport, `/search/` is served from cache, and the pane widens to content
rather than simulating a narrow one — are in `CLAUDE.md` under *Commands*.

## State

**Nothing is broken and nothing is half-finished.**

`main` is `7f1a277`, working tree clean, no open PRs, and the only remote
branches are `main` and the deliberate keeper
`handoff-2026-08-09-search-link-safari-scroll`. `--public` exits 0 (7 pages, 10
JSON-LD blocks valid, leak gate clear) and rebuilds `docs/` byte-identical to
what is committed.

**The live site is verified, not assumed**: all 7 pages match by SHA-256 and
the sitemap carries 5 `<loc>` entries. The search index is current — the Mac's
`build.py --refresh` re-fetched the four pages, passed all seven of that
project's gates, and returned all three files byte-identical to what is
vendored. Nothing is owed.

Counts unchanged: 713 entries, 620 distinct people, 275/61/214 on II.

**Take the publication state from the repo, not from here** — this file is
written before its own branch merges, so it is wrong about itself by
construction.

```bash
gh pr list --state open      # remotely there is no gh: use the GitHub MCP tools
git rev-list --left-right --count origin/main...HEAD
git ls-remote --heads origin
```

## The open thread — Genealogy II's orthography, now with a reason

**Placement is read on all four plates. Orthography is read on III only.**

Genealogy II has had a placement pass and nothing else. This session read
**two** of its 275 entries and **one of the two was wrong** — 248 carried an
apostrophe where the plate sets a raised dot, and was missing a second
apostrophe entirely. That is not evidence the plate is riddled with errors, but
it is the first direct evidence that its orthography has never been checked,
and it is the argument for doing the pass. Budget about a session for 275
people.

**The method that settled it is cheaper than the one the flag prescribed.**
The flag said the marks were undecidable at 6.5x and asked for a photograph.
They were decidable **at 1:1**: flood-fill each blob in the name's band and
record height, ink, fill and the drift of the bottom third's centroid against
the top third's. On Table 2 the two sorts do not overlap — `ʼ` is h12–17 with
drift −0.9 to −4.4, `˙` and every i-tittle is h6–8 with drift ≈ 0. Full
numbers and the controls are in `TABLE2-BENCH.md`'s *Settled* section and in
`CLAUDE.md` under the magnification floor.

**Before starting:**

- **Take controls from the same plate and the same row band**, and reconcile
  the mark inventory against what the transcription predicts. A count that
  reconciles is what licenses trusting the rest.
- **Check the fold key before assuming a cost.** 248's stayed `oyoyai`, so no
  `_FOLD` map, no namesake gate and no font subset moved. A change that *does*
  move a fold key costs four maps here and two places in `laguna-search`, and
  may stop its build until a namesake pair is adjudicated.
- **Any data change owes a re-vendor**, and after that a `--refresh` from a
  machine that can reach the site.
- Past ~8x the resampler invents letterform. A photograph is for the case where
  the scan holds no usable ink — not for a choice between two known sorts.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy II orthography** | a session | The open thread above. 273 entries still unread |
| `--xrefrow` for Tables 1, 3 and 4 | small | Turn it on and re-baseline. It should only ever **remove** flags; if it adds one, the assumption is wrong for that plate. Moves three documented baselines, so do it deliberately |
| Shrink the rig's 23 | half a session | Teach `audit.py` the twice-printed people (169 has two unions and one row) and the continuation rows. **Worth less than it was** — the 23 are explained and diffable now, so this buys tidiness, not signal |
| Remove `/search/`'s empty-state `Clear filters` | small, **needs you** | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, **needs you** | Measured across all 620 rows 2026-08-22; numbers in `CLAUDE.md`. A 200px track ends all name wrapping and moves the pan threshold 651 → 735px window, 1:1 with the track floor. Buys **nothing** on row height — that is the Clan column |
| The masthead no longer names the edition | **needs you** | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | **needs you**, awaiting recurrence | Unchanged and untested. Cherry-pick `938b8e8` onto a fresh branch off current `main` when it next appears — never revive the parked branch. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | **needs you** | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |
| Rider | — | The vendored `search.css` still states the pre-Sex-column threshold (675px, now 636 client / 651 window). The claim holds; only its figures are superseded. Fix **upstream** on the next re-vendor |
| Rider | — | One finding is Chromium-only and wants Safari: that `white-space: nowrap` does not suppress a `<wbr>` break. Matters only if the Name column is widened |

## Decisions already made — don't re-litigate

- **248 reads `Oyo˙ʼʼy˙ăi` and 249 is right as transcribed.** Measured, with
  controls, at 1:1. Published in PR #74. Do not re-read them.
- **The edition annotates a misprint; it does not correct one.** 248 is not a
  misprint — it was a transcription error, and correcting it is what the
  edition is *for*. Do not confuse the two: a `sic`-ringed value stays as the
  plate sets it.
- **`--ongrid` is the wrong tool for Table 2.** Tested at 0.25, 0.35 and 0.45
  and rejected. **Do not try it again** — the crease and the plate's real
  second-pitch stubs sit at the same 1.58-row offset, so no tolerance separates
  them, and the falling problem count is ink being deleted.
- **Table 2's 23 problems ARE a baseline.** Diff the list; do not read it
  fresh, and do not report one as a defect in the transcription.
- **Table 2's threshold, band and column calibration is settled**:
  `--thresh=140`, per-block `--yband`, `--row=52`, `--track=1`, `--xmerge=15`,
  `--maxthick=8`, `minrun=40`, and `--gapmax=30` for block 2 only.
- **U53's plate shows 6 stubs against 5 transcribed children and the
  transcription is right** — the sixth enters 255, the `+` line, and is not
  descent.
- **U46's leader ends in mid-air** and that is the plate, measured, not a fault.
- **The audit pairs a bracket to the group whose mother stands on its leader**,
  which makes the leader test tautological on purpose. **Do not "restore"**
  pairing by `_GROUPS` order — it is what hid block 2's two real errors.
- **A bracketless group is bounded by its leader-matched neighbours**, never by
  the positional ones.
- **The bench is a deliverable, not a source**, and its 52 cards were never
  ticked — `TABLE2-BENCH.md` is the verdict record.
- **A tall row on `/search/` is a CLAN-column question, not a Name one.**
- **`W31` is a reading, not a rule.** Do not sweep for more by pattern.
- **"A spouse with no leader had no recorded issue" is FALSE.** 58 has no
  leader on her own line and two children.
- **`/search/` panning at phone widths is the decision, not the defect**, and
  the **upstream-vs-host test** decides where a `/search/` change goes.
- **Everything from previous sessions still stands**: the list is a table at
  every width; names wrap at editorial `<wbr>` seams; the default palette is
  light and CSS is what says so; Theme sits at the foot; a row's height is
  stated, not inferred; `laguna-search` stays a separate private repo;
  `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **248 and 249's medial marks** — settled 2026-08-23, published. This was
  `TABLE2-BENCH.md`'s only open flag and that section is now empty.
- **Genealogy II's placement** — all 52 groups read against the scan
  2026-08-23, no correction owed. **Placement is read on all four plates.**
- **"Feed the bench verdicts back"** — there are none to feed.
- **The `/search/` provenance line's home** — closed 2026-08-21: leave it where
  it is. Offered four times before that; **do not offer a fifth.**
- **`/search/` #5, the Death filter** — closed 2026-08-21: relabel, do not
  strip.
- **Genealogy III block 1** — placement read 2026-08-17, orthography
  2026-08-21, no corrections. **Nothing is owed on this plate.**
- **Genealogy III block 2's parentage** (2026-08-17) and **Genealogy I's
  placement** (all 76 stubs matched) — read and published.
- **The plate-audit rig for Tables 3 and 4** — calibrated, their 15 and 10
  problems all explained. **Do not re-derive Table 4's `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream, published
  2026-08-18.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
- **De-indexing**, **Wikidata**, **the custom domain**, **releases and
  Zenodo** — all closed, with the reasoning in `CLAUDE.md`. A doi reappearing
  is a regression.
