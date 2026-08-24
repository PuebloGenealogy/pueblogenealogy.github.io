# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

**It points at `CLAUDE.md`; it does not restate it.** Anything permanent that
turns up in a session belongs there, not here — this file is designed to be
thrown away.

Last updated **2026-08-23**. The session read **Genealogy II's brackets, all 52
groups, against the scan** and found **no correction owed** (PR #72,
`4120f9c`), then tested `--ongrid` against the resulting baseline and rejected
it. It also merged PR #71, the previous session's handoff correction. **Nothing
in `docs/` or `vendor/` has moved since `8a092d5`.**

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the 2026-08-23 block.
3. **`scripts/plate_audit/TABLE2-BENCH.md`** before touching anything to do with
   Genealogy II's brackets or the rig's 23, and `scripts/plate_audit/README.md`
   before running anything in that directory.
4. **If this session is running remotely** — Claude Code on the web rather than
   the Mac — `reference/environment-notes.md` (on-demand; not auto-loaded). There may be no route to the published
   site, which removes `/publish` gate 6, and a delete-push may be refused; in
   exchange there is Pillow and a headless Chromium, which the Mac has not.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. Its three traps — a blank screenshot is a zero-sized
viewport, `/search/` is served from cache, and the pane widens to content rather
than simulating a narrow one — are in `CLAUDE.md` under *Commands*.

## State

**Nothing is broken and nothing is half-finished.**

The live site is `8a092d5`, published and verified 2026-08-21 from the Mac.
**Nothing has been published since**, and nothing on `main` since then touches
`docs/`. Re-checked at the end of this session: working tree clean, `--public`
exits 0 (7 pages, 10 JSON-LD blocks valid, leak gate clear), and the only
rebuild diff is the **date**, reverted rather than committed.

Counts unchanged: 713 entries, 620 distinct people, 261/72/192 on III.

**Take the publication state from the repo, not from here** — `CLAUDE.md` says
why, and this file is written before its own branch merges, so it is wrong about
itself by construction.

```bash
gh pr list --state open      # remotely there is no gh: use the GitHub MCP tools
git rev-list --left-right --count origin/main...HEAD
git ls-remote --heads origin
```

### Branches

At the time of writing `origin` carries **`main`** and
**`handoff-2026-08-09-search-link-safari-scroll`** — a keeper, the only thing
holding `938b8e8`, the unverified Safari scroll fix, reachable. **Do not sweep
it.** Both of this session's working branches were cleared by the user from the
Mac; a remote session still cannot delete a ref (HTTP 403, egress policy, no API
route).

**GitHub's auto-delete has now failed six times in seven merges**, so check
`ls-remote` after every merge rather than assuming. And note the trap this
session walked into: **merging a handoff correction recreated the very ref it
said was gone**, because that PR's own head branch was the one being cleaned up.
A handoff can be falsified by the act of merging it.

## The open thread — Genealogy II's orthography

**Placement is now read on all four plates. Orthography is not.**

Genealogy II has had a placement pass and only that. Genealogy III took the two
separately — placement 2026-08-17, orthography 2026-08-21, all 229 of block 1's
entries read at 4x with 6–7x confirmation on mark-dense names — and this plate
should have the same. It is **275 people**, so budget about a session.

**The one concrete open item** is `TABLE2-BENCH.md`'s flag: **248 and 249's
medial marks**. At 6.5x, 248 reads `Oyo` + a raised dot + what may be **two**
apostrophes before the `y`, against the transcription's `Oyo˙ʼyʼăi` — one before
and one after. 249 is the same shape. Both are plausible as transcribed and
neither is confirmed.

**Before starting:**

- **`stubs.py` transfers directly** and is what makes this affordable — see
  `.claude/rules/plate-audit.md` (loads automatically once you open a file
  under `scripts/plate_audit/`). It is twenty lines in a scratchpad; rebuild
  it, don't hunt for it.
- **Past ~8x the resampler invents letterform.** If the scan cannot settle a
  mark, the answer is **a photograph of the page**, not a bigger crop — that is
  what closed Genealogy III's five U+02BD instances after a week of being told
  it needed AMNH.
- **A new character in a name costs four `_FOLD` maps here and two more places
  in `laguna-search`**, and may create a fourth namesake collision that stops
  its build. Expect to adjudicate; the failure is a feature.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy II orthography** | a session | The open thread above |
| `--xrefrow` for Tables 1, 3 and 4 | small | Turn it on and re-baseline. It should only ever **remove** flags; if it adds one, the assumption is wrong for that plate. Moves three documented baselines, so do it deliberately |
| Shrink the rig's 23 | half a session | Teach `audit.py` the twice-printed people (169 has two unions and one row) and the continuation rows. **Worth less than it was** — the 23 are explained and diffable now, so this buys tidiness, not signal |
| Remove `/search/`'s empty-state `Clear filters` | small, **needs you** | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, **needs you** | Measured across all 620 rows 2026-08-22; numbers in `reference/history/search-pan-threshold.md`. A 200px track ends all name wrapping and moves the pan threshold 651 → 735px window, 1:1 with the track floor. Buys **nothing** on row height — that is the Clan column |
| The masthead no longer names the edition | **needs you** | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | **needs you**, awaiting recurrence | Unchanged and untested. Cherry-pick `938b8e8` onto a fresh branch off current `main` when it next appears — never revive the parked branch. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | **needs you** | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |
| Rider | — | The vendored `search.css` still states the pre-Sex-column threshold (675px, now 636 client / 651 window). The claim holds; only the figures are superseded. Fix **upstream** on the next re-vendor |
| Rider | — | One finding is Chromium-only and wants Safari: that `white-space: nowrap` does not suppress a `<wbr>` break. Matters only if the Name column is widened |

## Decisions already made — don't re-litigate

- **`--ongrid` is the wrong tool for Table 2.** Tested at 0.25, 0.35 and 0.45
  and rejected; the reasoning is in `.claude/rules/plate-audit.md` and the
  changelog. **Do not try it again** — the crease and the plate's real second-pitch stubs sit at the
  same 1.58-row offset, so no tolerance separates them, and the falling problem
  count is ink being deleted.
- **Table 2's 23 problems ARE a baseline now.** Diff the list; do not read it
  fresh, and do not report one as a defect in the transcription.
- **Table 2's threshold, band and column calibration is settled**: `--thresh=140`,
  per-block `--yband`, `--row=52`, `--track=1`, `--xmerge=15`, `--maxthick=8`,
  `minrun=40`, and `--gapmax=30` for block 2 only.
- **U53's plate shows 6 stubs against 5 transcribed children and the
  transcription is right** — the sixth enters 255, the `+` line, and is not
  descent. The one group where stub-counting alone would convict a sound
  reading.
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
- **"A spouse with no leader had no recorded issue" is FALSE.** 58 has no leader
  on her own line and two children.
- **The misprint display stays the plate's**, in the chart and on `/search/`.
- **`/search/` panning at phone widths is the decision, not the defect**, and
  the **upstream-vs-host test** decides where a `/search/` change goes.
- **Everything from previous sessions still stands**: the list is a table at
  every width; names wrap at editorial `<wbr>` seams; the default palette is
  light and CSS is what says so; Theme sits at the foot; a row's height is
  stated, not inferred; `laguna-search` stays a separate private repo;
  `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **Genealogy II's placement** — all 52 groups read against the scan 2026-08-23,
  no correction owed. **Placement is now read on all four plates.**
- **"Feed the bench verdicts back"** — there are none to feed.
- **The `/search/` provenance line's home** — closed 2026-08-21: leave it where
  it is. Offered four times before that; **do not offer a fifth.**
- **`/search/` #5, the Death filter** — closed 2026-08-21: relabel, do not strip.
- **Genealogy III block 1** — placement read 2026-08-17, orthography 2026-08-21,
  no corrections. **Nothing is owed on this plate.**
- **Genealogy III block 2's parentage** (2026-08-17) and **Genealogy I's
  placement** (all 76 stubs matched) — read and published.
- **The plate-audit rig for Tables 3 and 4** — calibrated, their 15 and 10
  problems all explained. **Do not re-derive Table 4's `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream, published
  2026-08-18.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
- **De-indexing**, **Wikidata**, **the custom domain**, **releases and Zenodo** —
  all closed, with the reasoning in `reference/history/zenodo-and-exposure-posture.md`
  (conclusions in `memory/standing-decisions.md`). A doi reappearing is a
  regression.
