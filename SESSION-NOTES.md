# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

**It points at `CLAUDE.md`; it does not restate it.** Anything permanent that
turns up in a session belongs there, not here — this file is designed to be
thrown away, and the plate-reading method rode in it for two wraps before being
moved on 2026-08-22.

Last updated **2026-08-22**. That session **wrote no code**: it moved the
plate-reading method into `CLAUDE.md` and shortened this file by a third. The
session before it, on **2026-08-21**, closed the `/search/` provenance line
where it stands; the two before that closed the owed publish checks (both clean,
from the Mac) and published Genealogy III block 1's orthography plus the
`/search/` Death filter. Nothing in `scripts/` or `docs/` has moved since
`8a092d5`.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s two newest entries.
3. `scripts/plate_audit/README.md` **before running anything in it**. Table 1,
   Table 3 and Table 4 are calibrated; the parameters are per plate and do not
   transfer.
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

The live site is `8a092d5`, published **and verified** 2026-08-21: the user ran
Gate 6's page-by-page SHA-256 comparison and `laguna-search`'s post-publish
`build.py --refresh` from the Mac, and both came back clean. `laguna-search` is
at `58965e5` on its `main` — the same build the site serves.

Re-checked at the end of this session: working tree clean, `--public` exits 0
(7 pages, 10 JSON-LD blocks valid, leak gate clear), and the only diff a rebuild
now produces is the **date** — `dateModified`, the "Last updated" line,
`sitemap.xml`'s `lastmod` — which was reverted, not committed. Everything
committed after `8a092d5` touches only `CLAUDE.md`, `CHANGELOG.md` and this
file.

Counts unchanged: 713 entries, 620 distinct people, 261/72/192 on III.

**Take the publication state from the repo, not from here** — `CLAUDE.md` says
why, and this session proved it a third way: the branch deletion the last
handoff called owed had already happened.

```bash
gh pr list --state open      # remotely there is no gh: use the GitHub MCP tools
git rev-list --left-right --count origin/main...HEAD
git ls-remote --heads origin
```

At the end of this session: **PR #66 open** (this wrap and the closure above,
docs of record only), two commits ahead of `origin/main`, nothing behind.

For the next publish, the two checks a remote session cannot run:

```bash
(cd docs && find . -name '*.html' | sed 's|^\./||') | while read -r f; do
  live=$(curl -s "https://pueblogenealogy.github.io/$f" | shasum -a 256 | cut -d' ' -f1)
  [ "$live" = "$(shasum -a 256 "docs/$f" | cut -d' ' -f1)" ] && echo "OK   $f" || echo "DIFF $f"
done
python3 build.py --refresh          # in the laguna-search checkout
```

The `--refresh` run's first line must say **`re-fetched`**, not `cached in
cache/`, or its gates pass against the site as it was. And check
`git diff --stat <publish-sha> main -- docs/` before running the hashes off a
plain `git pull`: it worked this time only because `docs/` had not moved since
the publish commit.

### Branches — nothing is owed

`origin` carries three refs: `main`, this session's `claude/resume-b6s8bz`, and
**`handoff-2026-08-09-search-link-safari-scroll`** — a keeper, not stale. It is
the only thing holding `938b8e8`, the unverified Safari scroll fix, reachable.
**Do not sweep it.**

`claude/gracious-hawking-fuklkp` went with GitHub's auto-delete when PR #65
merged, so the deletion the last handoff recorded as outstanding is done. Verify
branch state with `ls-remote`, never by ancestry — `CLAUDE.md` has the reason
(squash merges) and the two deletion traps.

## The open thread — there isn't one

No reading is owed on any plate, nothing is in flight, and every item below
needs the user. Genealogy III block 1 was the last one open: its placement was
read 2026-08-17 and its orthography 2026-08-21, all 229 entries, no corrections.

**How to read a plate for type** — tile planning, the two magnifications, and
Table 3's crop coordinates — is now in `CLAUDE.md` → *Facts worth knowing*,
beside the magnification floor. It used to live here, which is why it moved.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered four times |
| Widen `/search/`'s Name column | small, needs you | **Re-measured 2026-08-22 across all 620 rows; the numbers are in `CLAUDE.md`.** A 200px track ends all name wrapping and moves the pan threshold 651 → 735px window, 1:1 with the track floor. It buys **nothing** on row height — that is the Clan column, not this one. The `nowrap` objection is also weaker than recorded: Chromium breaks at `<wbr>` through it (WebKit untested) |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. Cherry-pick `938b8e8` onto a fresh branch off current `main` when it next appears — never revive the parked branch itself. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **`W31` is a reading, not a rule.** Some single-marriage leaders hang off the
  husband, some off the wife, ten rows apart. **Do not sweep for more by
  pattern**; each is read off the ink.
- **"A spouse with no leader had no recorded issue" is FALSE.** 58 has no leader
  on her own line and two children. Gen. III's 85/86/87 and Gen. IV's 5/+6/+7
  both stand, on the bases recorded in `CLAUDE.md` and in `V04`'s note — **do
  not re-justify either with that sentence.**
- **The plate-audit rig: the row pitch is rarely what is wrong.** It is the
  band, which must hold the rule plus the 110px stub reach on **both** sides.
  `--overshoot` widens the left side only. Calibration is per plate.
- **The audit pairs a bracket to the group whose mother stands on its leader**,
  which makes the leader test tautological on purpose — pairing by `_GROUPS`
  order is what hid block 2's two real errors. **Do not "restore" it.** A
  pairing made by position is labelled a guess, and those guesses are where
  every false alarm came from.
- **The misprint display stays the plate's**, in the chart and on `/search/`.
  `data-reading` publishes the reading beside it; the tooltip names it.
- **`/search/` panning at phone widths is the decision, not the defect**, and
  the **upstream-vs-host test** decides where a `/search/` change goes: would
  the widget standing alone want it?
- **Everything from previous sessions still stands**: the list is a table at
  every width; names wrap at editorial `<wbr>` seams; the default palette is
  light and CSS is what says so; Theme sits at the foot; a row's height is
  stated, not inferred; `laguna-search` stays a separate private repo;
  `/search/` is absent from `sitemap.xml`.

## Closed — do not re-raise

- **The `/search/` provenance line's home** — closed 2026-08-21 by the user:
  **leave it exactly where it is**, the second `.foot-note` in that page's own
  footer, which *is* that page's provenance block. Offered four times before
  this; **do not offer a fifth.** Why the move would have been wrong is in
  `CLAUDE.md` beside the paragraph that explains the line.
- **`/search/` #5, the Death filter** — closed 2026-08-21: relabel, do not
  strip. `d` is the only route to the 103 entries recorded as dead with no year.
- **Genealogy III block 1** — placement read 2026-08-17, orthography 2026-08-21,
  no corrections. **Nothing is owed on this plate.**
- **Genealogy III block 2's parentage** (2026-08-17), **Genealogy I's
  placement** (stub by stub, all 76 matched), **Genealogy II's placements**
  (2026-07-30) — all read and published.
- **The plate-audit rig for Table 4** — calibrated 2026-08-18, its 10 problems
  all explained. **Do not re-derive `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream, published
  2026-08-18.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
- **De-indexing**, **Wikidata**, **the custom domain**, **releases and Zenodo** —
  all closed, with the reasoning in `CLAUDE.md`. A doi reappearing is a
  regression.
