# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-17**, at the end of a session that took in an outside
debug report and fixed **seven of its nine findings**, all published and
verified live.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — it is this whole session, and its last two
   sections are the deploy block and what is still open.
3. Only if you are touching `/search/`: `CLAUDE.md` → *The search page is
   vendored, not generated here* (now **four** re-vendor shapes) and the
   `/search/` **All People** block under *Design invariants*.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **The pane caches `/search/` hard** — bust it with
`location.replace('/search/?v=' + Date.now())`, or a `?v=` on an iframe's
`src`. A narrow-viewport check needs a **fixed-width iframe**, not
`resize_window`; the pane widens to the content. And **`await
document.fonts.ready` inside the iframe** before measuring anything about text.

## State

**Nothing is half-finished, and this time that is checked rather than
asserted.** Working tree clean, no open PRs, `main` at the wrap commit and 0/0
with origin. `--public` exits 0 — 7 pages, 713 drawn, 10 JSON-LD blocks valid —
a rebuild reproduces `docs/` byte-identically from the committed source, and all
four `self_check()`s pass.

**The publish is complete and verified live**: all seven pages plus `search.js`
and `search-index.json` by SHA-256, sitemap 5 `<loc>` with `/search/` absent,
stale-identity count 0, and Juana live as `sex: "F", sexPrinted: "M"`.

**Gate 8 is done and it validated the one risky thing in it.** That vendor drop
was built from a **hand-seeded cache**, not from the live site — the change the
index needed (`data-reading`) was in pages that were not yet live. The
post-publish `--refresh` re-fetched genuinely and produced **all three files
byte-identical** to what was vendored, so the shortcut is confirmed for this
instance. It stays a shortcut, not a habit: `CLAUDE.md` records when it is
admissible.

Three build gates are newer than the last handoff, and all three were proved by
feeding them bad input and confirming exit 1: the sitemap/`noindex` agreement
check and `check_editorial_marks()` here, and `gate 1`'s ringed-reading check
upstream.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Bracket placement on Genealogy I and III** | large, needs you | **DEFERRED FOUR TIMES now, not closed** — the largest correctness risk on the site. Method in full below. Nothing else on this list competes with it |
| `/search/` #5 — the Death filter | small, **needs a decision** | Accepts letters where Birth strips them, both labelled *Year*. Either make it strip like Birth, or relabel it `Year or d.` and keep the power. Side effect worth knowing: `?d=d.` returns all 115 people with a recorded death. Upstream |
| `/search/` #6a — `?open=` | small | Can name a row that is not open, so a shared URL reopens a row the sender was not looking at. Clear `this.open` when the index is past what has rendered, or render up to it. Upstream |
| The `sic` tooltip could name the reading | tiny | Now that `data-reading` exists, *"the edition reads F"* beats *"the edition's reading differs"*. Upstream copy change, never raised with the user |
| The `/search/` provenance line's home | small, needs you | Offered three times, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | Kept deliberately — the only moment a reader can see no control to undo. Offered three times |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name; its numbers are stale again |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |

## Deferred, not closed — bracket placement on Genealogy I and III

**Kept in full because it is the site's largest correctness risk and the method
is expensive to re-derive.** Deprioritised four times now. It has not been done
and it has not been struck.

Genealogy IV shipped on 2026-07-31 with person 20 attached to the wrong
marriage, and it survived four `self_check()`s, every publish gate and ten days
live. **Nothing structural can find the next one**: 19 and 20 are both Bear,
exactly like their mother, so clan descent cannot discriminate, and the counts
close either way.

Checked by a human against the scan: **Genealogy II** (the user's full list,
2026-07-30) and **Genealogy IV's 5/6/7** (2026-08-10). **I and III have not
been.** III is the largest and most intricate — 261 people, seven generations,
two descent blocks, 72 unions.

The method, and it is cheap:

- Crop the **bracket-column strip** at native resolution — 260–320px wide, so
  the vertical and every stub entering it are the only things in frame. Never
  read structure off a downscale.
- **Count the leaders entering each vertical before counting the lines in the
  block.** One leader means one group however many `+` lines sit above it. That
  single question is what IV·20 turned on.
- A spouse whose line carries **no rule** had no recorded issue.

The automated half is done and clean: a data-driven audit reading `_GROUPS`,
taking each union's mother (or its `LEADER_ON_SPOUSE_ROW` spouse), and asserting
the bracket starts on that named person's line — 426 checks, all four plates.
**It cannot catch a group whose data and rendering agree with each other and
disagree with the plate**, which is the whole remaining risk.

Their reading wins on placement; present the crop and the evidence, and do not
change a transcription unilaterally.

## Decisions already made — don't re-litigate

- **The misprint display stays the plate's.** `/search/` and the chart both show
  the misprinted `M.`/`Bager`, ringed; `data-reading` publishes the edition's
  reading beside it without changing what is shown. The 2026-08-16 report
  contradicts itself on this — #1's Verify wants the panel to read `Sex F.`,
  #2's Change says leave display alone — and **#2 was followed**, because the
  hard rule is that a misprint is annotated, not corrected. Changing it would
  make `/search/` disagree with the chart.
- **`/search/` panning at phone widths is the decision, not the defect.** That
  report reads it as "unusable on every phone" and prescribes an inner
  scroller. Re-raised, checked, and it stands. Its `SEARCH THE TA…` claim is
  also wrong: the page's only `text-overflow:ellipsis` is on the clan filter's
  button. The bar sliding off while panned was the real half, and it is fixed.
- **Find matches the printed number, and the id is only the fallback.** Two of
  Genealogy III's people can no longer be reached by typing their id directly —
  typing `258` goes to 256, first in plate order, with the note as the one-click
  route to the other. Deliberate. And the datalist `value` stays the **id**:
  making it the printed number would break the dropdown-pick path for exactly
  these people.
- **The wording of a filter option is a layout input**, and the dash's
  accessibility cost was raised and the change asked for anyway. Not an
  oversight; the repair, if ever wanted, is a shorter *word*.
- **The upstream-vs-host test decides where a `/search/` change goes.** Would
  the widget standing alone want it? Table typography, a control's width and a
  filter's copy are the widget's; the bar's metrics, the title block's type and
  the default-light palette exist only to match *this* site.
- **The host bar's metrics are read out of `CSS` under the SITE's token names**,
  and `.lg-host-bar,.lg-host-bar *{box-sizing:border-box}` is load-bearing.
- **`Clear all` is gone and `Clear filters` stays.** Not an oversight.
- **Everything from the previous sessions still stands**: the list is a table at
  every width and the document pans; names wrap at editorial `<wbr>` seams; the
  default palette is light and CSS is what says so; Theme sits at the foot; the
  pills carry the numeral alone with the word kept in the accessible name; a
  row's height is stated, not inferred; `laguna-search` stays a separate private
  repo; `/search/` is absent from `sitemap.xml`.

## Three ways an audit lied this session — all cheap to repeat

- **Canvas `measureText` cannot see an input's caret inset.** It reported the
  Find placeholder fitting with 16px to spare when it overflowed by 5. Measure a
  field by putting the string in it as a **value** and comparing `scrollWidth`
  to `clientWidth`.
- **`location.hash` in a loop hits Chrome's ~200 same-document navigation
  throttle.** A finder audit reported 300+ failures that were entirely the
  harness's; Genealogy I and IV passed only because they are smaller than the
  limit. Reload the frame every ~120 checks.
- **`git checkout <file>` reverts a file, not an edit.** Used to undo a
  deliberately-corrupted input after proving a gate fires, it discarded three
  uncommitted fixes in the same file. Revert an experiment with a **file copy**
  when the file carries other uncommitted work.

And one about GitHub rather than about measuring: **when a Pages deployment is
stuck `queued` during an outage, a later push clears it and a re-run does not.**
The stuck job sat at 1h18m and never started; the next merge triggered a fresh
deployment that succeeded in under 25 seconds and carried the blocked commit
with it, because Pages deploys whatever `main` holds. `gh api -X POST
.../pages/builds` returned the same 503 as everything else. Don't rescue the run
— land something.

## Closed — do not re-raise

These are settled. Listing one as pending invites a decided question to be
re-taken.

- **De-indexing** — closed 2026-08-08 by the user. Not important, nothing to be
  done.
- **Wikidata** — removed 2026-08-08. No item, payload deleted, do not
  reconstruct it and do not offer it as an easy win.
- **Custom domain** — closed 2026-07-31. `pueblogenealogy.github.io`
  permanently; durability beats portability.
- **Releases and Zenodo** — closed 2026-08-08. No GitHub Release, no deposit,
  ever, unless the user says otherwise. A doi reappearing is a regression.
- **The second sort on Genealogy III** — settled at all five instances, U+02BD,
  published. Do not re-crop the scan.
- **Genealogy II's placements** — the user re-checked their full list on
  2026-07-30 and reported no remaining errors.
- **Phonetic glyph rendering** — proven from the cmap and checked on device.
