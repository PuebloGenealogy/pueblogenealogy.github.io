# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-21**, at the end of a short second session that **closed
the two owed publish checks** — the user ran both from the Mac and both came
back clean, so the 2026-08-21 publish is verified rather than deployed —
recorded the remote egress block as a standing property of the environment
(`CLAUDE.md`, PR #63), and deleted the two merged branches. It ran **remotely**,
like the session before it, and wrote no code: nothing in `scripts/` or `docs/`
moved. The session before it read Genealogy III block 1's **orthography** — the
last reading owed on any plate, and it needed no correction — fixed
`/search/`'s **Death filter**, and published both.

**There is no open thread.** Nothing is owed on any plate, nothing is in
flight, and every item on the list below needs the user.

## Start here in a new chat

1. This file.
2. `scripts/plate_audit/README.md` **before running anything in it**. All three
   plates it has been pointed at are calibrated now — Table 1, Table 3 and
   Table 4 — and each set of parameters is per plate.
3. `CHANGELOG.md`'s two newest entries.
4. **If this session is running remotely** — Claude Code on the web rather than
   the Mac — read `CLAUDE.md` → *Environment* first. There may be no route to
   the published site at all, which removes `/publish` gate 6, and a
   delete-push may be refused; in exchange Pillow and a headless Chromium are
   available, which the Mac does not have.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug; fix with `resize_window` at an
explicit `1280x900`. To see something far down the page, translate it into view
with `document.body.style.transform` rather than scrolling. **The pane caches
`/search/` hard** — bust it with `location.replace('/search/?v=' + Date.now())`.

## State

**Published and VERIFIED 2026-08-21. `main` at `92b9984` plus this wrap's own
commit, working tree clean, and `docs/` reproduces byte-identically from
`--public`** — run at the end of this session, exit 0, 7 pages, 10 JSON-LD
blocks valid, no date drift because the publish was the same day. The publish
itself was `8a092d5` — Genealogy III block 1's orthography (docs of record
only) and the `/search/` Death filter (upstream + re-vendor). Everything after
it is docs of record.

**Both owed checks were run from the Mac and both came back clean** (user,
2026-08-21): Gate 6's page-by-page SHA-256 comparison against the live site,
and `laguna-search`'s post-publish `build.py --refresh`. So the publish is
**verified**, not merely deployed, and no re-vendor was due. The commands, for
the next publish:

```bash
(cd docs && find . -name '*.html' | sed 's|^\./||') | while read -r f; do
  live=$(curl -s "https://pueblogenealogy.github.io/$f" | shasum -a 256 | cut -d' ' -f1)
  [ "$live" = "$(shasum -a 256 "docs/$f" | cut -d' ' -f1)" ] && echo "OK   $f" || echo "DIFF $f"
done
python3 build.py --refresh          # in the laguna-search checkout
```

Two things about that pair worth keeping. The `--refresh` run's first line must
say **`re-fetched`** and not `cached in cache/`, or its gates pass against the
site as it was. And **`docs/` had not moved since the publish commit** —
everything after `8a092d5` touched only `CLAUDE.md`, `CHANGELOG.md` and this
file — so the hash check ran straight off a fresh `git pull` with no need to
check out the published commit. Check that with
`git diff --stat <publish-sha> main -- docs/` before assuming it again.

`laguna-search` is at **`58965e5`** on its **`main`**, merged and pushed
2026-08-21 — the same build the site is serving, confirmed by the `--refresh`.

**Take all of that from the repo, not from here** — it is the least reliable
paragraph in this file, and this session proved it again: `laguna-search`'s two
commits were sitting local with a clean `git status` until the end.

```bash
gh pr list --state open      # remotely there is no gh: use the GitHub MCP tools
git rev-list --left-right --count origin/main...HEAD
```

Both came back clean at the end of this session — no open PRs, `0 1` before the
wrap branch was merged.

Counts unchanged: 713 entries, 620 distinct people, 261/72/192 on III.

### Branches — one deletion is owed, and it is the only thing owed at all

**`claude/gracious-hawking-fuklkp` is on `origin`, merged, and should be
deleted.** It carries this wrap and nothing else once that merges; a remote
session cannot delete it, so:

```bash
git push origin --delete claude/gracious-hawking-fuklkp
```

Nothing is at risk while it sits there — it holds no unique commit — but it is
the shape `CLAUDE.md` warns turns into a revert if anything is branched off it
or `main` moves far enough. **Verify with `git ls-remote --heads origin`, not
by ancestry**: PRs here are squash-merged, so a branch's own commit is never an
ancestor of `main` and `--no-merged` reports merged work as unmerged. The proof
that a squash landed is the tree: `git rev-parse <branch>^{tree}` against
`main^{tree}`, which matched for both of this session's merges.

**Keep `handoff-2026-08-09-search-link-safari-scroll`** (at `d260b72`). It is
**not** stale and must not be swept: it is the only thing keeping **`938b8e8`**
— the unverified Safari scroll fix — reachable. See the Safari row below.

**`claude/resume-jntfyn` is gone from both repos**, and so was
`claude/gracious-hawking-fuklkp` until this wrap re-created it — deleted from
the Mac on 2026-08-21 after two remote sessions had a delete-push refused with
**HTTP 403** while ordinary pushes went through. That is egress policy, not a
permissions problem at GitHub.

**Delete one command at a time, never batched**: a batch
`git push origin --delete a b c` fails whole if any one ref is already gone,
deletes nothing, and reads exactly like a permissions problem.

Everything else was cleaned up on 2026-08-18: `plate-audit-w31-leader-row` and
`search-sic-reading-open-param` were deleted after `git merge-base
--is-ancestor` confirmed both were fully reachable from `main`, and PR #62's
branch was deleted by GitHub on merge. **If a future sweep makes you re-check
one of these, the test is the ancestor check, not the diff**: `git diff main
<branch>` reported 1154 and 492 lines for those two and they contained nothing
unique — the lines were deletions, meaning the branch was *behind* `main`.

## The open thread — there isn't one

The two checks the 2026-08-21 publish could not run were run and both came back
clean; see *State*. Nothing is in flight, and no reading is owed on any plate:

**Genealogy III's block 1 was read for ORTHOGRAPHY on 2026-08-21, and nothing
changed.** All 229 entries of ids 1–229 held against the scan — name, sex
letter, age, clan, vital note and cross-reference — read column by column at 4x
with 6–7x re-crops on nine mark-dense names. That was the last reading owed on
any plate, so **there is no open thread**; the list below is all there is, and
every item on it needs the user.

The crop commands are kept below: they are what a future reading of this plate
starts from, and the scratchpad does not survive a session.

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

**None of that works remotely — there is no `sips` — and the replacement is
better for reading TYPE, so keep it.** `pip3 install pillow`, then crop
straight from the JPEG with `Image.crop().resize(..., Image.NEAREST)`, which
invents nothing, exactly as `crop.py` does not. What made the 2026-08-21
orthography pass tractable was **not** eyeballing where the lines are:

- **Plan the tiles from an ink-row profile**, one generation band at a time —
  count dark pixels per row inside the band's x range, group runs of ≥6 into
  text lines, then pack lines into tiles ≤420 native px tall. It found 276 text
  lines in block 1, which reconciles against 229 people plus their
  cross-reference rows, 155's four continuation lines, `(Sister of 10)`, the
  six second-occurrence lines and the plate title. **A reconciling count is
  what licenses trusting the rest**, the same argument as the `_diag.html`
  DOM tally.
- **Two magnifications, not one.** 380 native px at **4x** (1520px, which is
  as much as a vision read carries) over the number-sex-name field, and 2.8x
  over the tail for age, clan and cross-reference. Re-crop a name at **6–7x**
  the moment a mark is ambiguous — that is what settled 60's `Kʼapokaʼă`,
  where 4x read the second apostrophe as a raised dot.
- Generation columns for Table 3, native x of the right-aligned number:
  g1 145 · g2 755 · g3 1293 · g4 1833 · g5 2377 · g6 2920 · g7 3467. Band
  x from `col − 60`; a full line runs about 370px.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
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

- **Genealogy III block 1** — PLACEMENT read 2026-08-17, right at every group,
  all 15 audit problems explained; **ORTHOGRAPHY read 2026-08-21**, all 229
  entries, no corrections. Nothing is owed on this plate.
- **85/86/87 (Gen. III) and 5/+6/+7 (Gen. IV)** — re-checked 2026-08-17, both
  stand. **Do not re-justify either as "a spouse with no leader had no issue".**
- **The plate-audit rig for Table 4** — calibrated 2026-08-18; its 10 problems
  are all explained. **Do not re-derive `--row`**: 145.8.
- **`/search/`'s sic tooltip and `?open=`** — fixed upstream and published
  2026-08-18.
- **Genealogy III block 2's parentage** — read and published 2026-08-17.
- **Genealogy I's placement** — read stub by stub 2026-08-17, all 76 matched.
- **`/search/` #5, the Death filter** — closed 2026-08-21 by the user: relabel,
  do not strip. It ships as placeholder `Year/d.` with the sentence in the
  spoken label, and `inputmode` split so a phone can type the `d`. Stripping
  letters was rejected on measurement — `d` is the only route to the 103
  entries recorded as dead with no year printed.
- **De-indexing** — closed 2026-08-08. Nothing to be done.
- **Wikidata** — removed 2026-08-08. Do not reconstruct it or offer it.
- **Custom domain** — closed 2026-07-31. Durability beats portability.
- **Releases and Zenodo** — closed 2026-08-08. A doi reappearing is a
  regression.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD.
- **Genealogy II's placements** — no remaining errors, 2026-07-30.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
