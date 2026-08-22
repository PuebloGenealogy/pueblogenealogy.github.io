# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

**It points at `CLAUDE.md`; it does not restate it.** Anything permanent that
turns up in a session belongs there, not here — this file is designed to be
thrown away.

Last updated **2026-08-22**, at the end of a third session that day. It merged
**PR #69** (`a5edc8a`) — the Table 2 plate-audit calibration the first session
of the day wrote and never pushed — and gave the **bracket bench** a strip for
the last seven groups that had none. The first session of the day moved the
plate-reading method into `CLAUDE.md`; the second re-measured `/search/`'s Name
column. **Nothing in `docs/` or `vendor/` has moved since `8a092d5`.**

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the 2026-08-22 block, three subsections.
3. `scripts/plate_audit/README.md` **before running anything in it**, and its
   Table 2 section before quoting any number from a Table 2 run. Tables 1, 3
   and 4 are calibrated; Table 2's **ink** is and its **pairing is not**.
4. **If this session is running remotely** — Claude Code on the web rather than
   the Mac — `CLAUDE.md` → *Environment*. There may be no route to the published
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
`docs/`: `a5edc8a` is `scripts/plate_audit/` plus one docstring. Re-checked at
the end of this session — working tree clean, `--public` exits 0 (7 pages, 10
JSON-LD blocks valid, leak gate clear), and the only rebuild diff is the
**date**, which was reverted rather than committed.

Counts unchanged: 713 entries, 620 distinct people, 261/72/192 on III.

**Take the publication state from the repo, not from here** — `CLAUDE.md` says
why, and this file is written before its own branch merges, so it is wrong about
itself by construction. As of writing: `main` is `a5edc8a`, no PR open.

```bash
gh pr list --state open      # remotely there is no gh: use the GitHub MCP tools
git rev-list --left-right --count origin/main...HEAD
git ls-remote --heads origin
```

### Branches — one deletion owed to the Mac

`origin` carries **`main`**, **`handoff-2026-08-09-search-link-safari-scroll`**
(a keeper — the only thing holding `938b8e8`, the unverified Safari scroll fix,
reachable; **do not sweep it**) and **`claude/confident-sagan-gpuzr6`**, whose
content is fully in `main` via #69 and which should be deleted:

```bash
git push origin --delete claude/confident-sagan-gpuzr6
```

A remote session cannot do it — HTTP 403, standing egress policy, not a GitHub
permission. **GitHub's auto-delete did not fire on #69**, as it did not on #66
or #67; it has now failed three times in four merges, so check `ls-remote` after
every merge rather than assuming.

## The open thread — read the bench

**The bracket bench is complete and the read has not started.** It is a
published artifact, not a repo file:

**https://claude.ai/code/artifact/6de9c0bf-5513-4b22-8821-097dd62ddc48**

All **52** of Genealogy II's groups sit beside a native-resolution crop of the
bracket column they belong to, with ✓ / ⚑ per group kept in the reader's own
browser. Genealogy II is the one transcribed plate whose brackets have never
been read group by group against the scan — the thing that let Genealogy IV ship
with 20 on the wrong marriage for ten days. **Only the user can do this**: the
rig cannot read type, so a group of the right size whose members are misnumbered
passes it silently.

Block 1's generations 4 and 5 hold 21 of the 52, so that is the bulk of it.

**Two groups look answerable on sight, and were deliberately left unticked:**

- **U60** — its strip shows 3 stubs over 270, 271, 272 and 2 stubs over 273,
  274. U60 claims 270–272 and U61 claims 273–274, so the rig gave U60's bracket
  to U61 by position. Confirming it closes two of the run's 23 problems.
- **U46** — its strip shows a 2-stub bracket over 207 and 208, which is its
  claim. The rig detected that vertical (y 8747–8818) and could not attach it,
  because 173 married in from Genealogy I and has no stub of her own.

**Before starting:** the tags on each card are the **rig's opinion, not
evidence** — *counts disagree* was wrong on both groups checked in block 1
generation 6. And where a mother and the alternative share a clan, **no
structural check is watching at all**; the stub is the only evidence.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Feed verdicts back** | small per correction, **needs the read first** | As groups are flagged, correct `transcription_ii.py`, re-run `self_check()`, rebuild. Nothing to do until the bench has verdicts in it |
| Shrink the rig's 23 | half a session | Teach `audit.py` the twice-printed people (169 has two unions and one row) and the continuation rows beyond cross-references. Would turn the list into a diffable baseline like Table 3's 15 and Table 4's 10. **Competes with the read rather than helping it** |
| `--xrefrow` for Tables 1, 3 and 4 | small | Turn it on and re-baseline. It should only ever **remove** flags; if it adds one, the assumption is wrong for that plate. Moves three documented baselines, so do it deliberately |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, needs you | Measured across all 620 rows 2026-08-22; numbers in `CLAUDE.md`. A 200px track ends all name wrapping and moves the pan threshold 651 → 735px window, 1:1 with the track floor. Buys **nothing** on row height — that is the Clan column |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. Cherry-pick `938b8e8` onto a fresh branch off current `main` when it next appears — never revive the parked branch. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |
| Rider | — | The vendored `search.css` still states the pre-Sex-column threshold (675px, now 636 client / 651 window). The claim holds; only the figures are superseded. Fix **upstream** on the next re-vendor |
| Rider | — | One finding is Chromium-only and wants Safari: that `white-space: nowrap` does not suppress a `<wbr>` break. Matters only if the Name column is widened |

## Decisions already made — don't re-litigate

- **Table 2's threshold, band and column calibration is settled and committed.**
  `--thresh=140`, per-block `--yband`, `--row=52`, `--track=1`, `--xmerge=15`,
  `--maxthick=8`, `minrun=40`, and `--gapmax=30` for block 2 only. The README
  carries the reasoning for each.
- **The 23 problems are not findings and not a baseline.** They are mostly
  groups paired by position, and on this plate that fallback reaches across
  descent blocks. Do not report one as a defect in the transcription, and do not
  diff the list as though it were Table 3's 15.
- **A bracketless group is bounded by its leader-matched neighbours**, never by
  the positional ones — the bench's four new strips are cut that way, and
  `CLAUDE.md` says why.
- **The bench is a deliverable, not a source.** Its generator lived in a
  scratchpad and died with the container; re-cutting the strips meant re-running
  the whole pipeline and recovering the x windows by correlation. Those windows
  are now recorded in `CLAUDE.md` (gen 5 x 4590 w 1290, gen 6 x 5750 w 1250).
- **A tall row on `/search/` is a CLAN-column question, not a Name one.**
- **`W31` is a reading, not a rule.** Do not sweep for more by pattern.
- **"A spouse with no leader had no recorded issue" is FALSE.** 58 has no leader
  on her own line and two children.
- **The audit pairs a bracket to the group whose mother stands on its leader**,
  which makes the leader test tautological on purpose. **Do not "restore"**
  pairing by `_GROUPS` order — it is what hid block 2's two real errors.
- **The misprint display stays the plate's**, in the chart and on `/search/`.
- **`/search/` panning at phone widths is the decision, not the defect**, and
  the **upstream-vs-host test** decides where a `/search/` change goes.
- **Everything from previous sessions still stands**: the list is a table at
  every width; names wrap at editorial `<wbr>` seams; the default palette is
  light and CSS is what says so; Theme sits at the foot; a row's height is
  stated, not inferred; `laguna-search` stays a separate private repo;
  `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **The `/search/` provenance line's home** — closed 2026-08-21: leave it where
  it is. Offered four times before that; **do not offer a fifth.**
- **`/search/` #5, the Death filter** — closed 2026-08-21: relabel, do not strip.
- **Genealogy III block 1** — placement read 2026-08-17, orthography 2026-08-21,
  no corrections. **Nothing is owed on this plate.**
- **Genealogy III block 2's parentage** (2026-08-17), **Genealogy I's placement**
  (all 76 stubs matched), **Genealogy II's placements as the user listed them**
  (2026-07-30) — read and published. Note the last of those is *the list the
  user raised*, not the plate group by group, which is what the bench is for.
- **The plate-audit rig for Tables 3 and 4** — calibrated, their 15 and 10
  problems all explained. **Do not re-derive Table 4's `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream, published
  2026-08-18.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
- **De-indexing**, **Wikidata**, **the custom domain**, **releases and Zenodo** —
  all closed, with the reasoning in `CLAUDE.md`. A doi reappearing is a
  regression.
