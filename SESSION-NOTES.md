# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**. A design session on `/search/`, **published and
verified live**. Three edits the user asked for, all measured; two of the three
went **upstream** into `laguna-search`, at **`ac33d95`**, pushed.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the three `/search/` edits, the three defects
   found while measuring, and the one thing deliberately not done.
3. Only if you are touching `/search/`: `CLAUDE.md` → *The search page is
   vendored, not generated here*, which gained four blocks today.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **A narrow-viewport check needs a fixed-width iframe,
not `resize_window`** — the pane widens to the content and there is no pan to
photograph. See `CLAUDE.md` → *Preview*.

## State

**Nothing is half-finished, both repos are committed and pushed, and the site is
live.**

**The deployed content is `2313ac4`'s `docs/`** (PR #47, squash-merged),
verified by SHA-256: all seven pages plus `search/search.js` and
`search/search-index.json`, every path 200, sitemap 5 `<loc>` against a build
count of 7 (correct), identity grep 0. A `--public` rebuild reproduces `docs/`
byte-identical, so `scripts/` and `docs/` agree.

**`laguna-search` is at `ac33d95`, pushed, level with origin** — the two layout
changes, 96/65 in `src/search.css` (`dist/` is gitignored there, so that is the
whole commit). `vendor/search/` was verified byte-for-byte against that commit's
`dist/`, all three files, and `SOURCE.md` names the SHA. Its post-publish
`--refresh` is done: `re-fetched`, seven gates green, all three files still
byte-identical. Namesake gate unchanged at **3 pairs, 1 open** (`II-182 /
IV-69`).

`main` may sit above the deployed commit on records-only commits — this handoff
and the changelog. Check `git diff 2313ac4 HEAD -- docs vendor scripts`, which
was empty when this was written. And take publication state from the repo, never
from this file:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

A `--public` build exits 0: 7 pages, 10 JSON-LD blocks valid, leak gate clear.
`leak_report()` was run by hand over all three vendored files — clean. All seven
of `laguna-search`'s gates pass; namesake gate unchanged at **3 pairs, 1 open**
(`II-182 / IV-69`).

All four plates published, 713 entries, no reading question open.

## The open thread — check `/search/` on a phone in Safari

**Needs you, and it is cheap.** `/search/` now pans the **document** sideways
below 672px. That is the **first horizontal document scroll this site has ever
had**, it went live today, and it has only ever been measured in Chromium —
where the preview pane cannot even simulate it, since the pane widens to the
content rather than panning (use a fixed-width iframe; see `CLAUDE.md` →
*Preview*).

Two reasons this is worth a minute rather than nothing:

- The plate's `.scroll` region carries an **unresolved Safari freeze**, and the
  three WebKit facts behind it are all about scroll containers and focus. A
  second scrolling surface is exactly the sort of thing that interacts with it.
- The one thing that would be a real defect is the **sticky column header**
  losing its grip while the page pans. It is sticky by design so the column
  names follow the reader down 634 rows, and the pan was deliberately given to
  the document rather than an inner scroller to protect that. Verified sticky in
  Chromium at every width; unverified in WebKit.

What to look for: pan `/search/` sideways on a phone, scroll down the list, and
say whether the header still follows and whether the gesture ever locks up.

If it is fine, this closes and the substantive thread below is next.

**A rebuild on a later day dirties `docs/` with dates alone.** If tomorrow's
first `--public` shows six pages moving on `dateModified` / "Last updated" /
`lastmod` and nothing else, that is the clock, not a content change.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Bracket placement on I and III, never read against the scan** | needs you | **Still the substantive open thread.** IV·20 shipped wrong on 2026-07-31 and survived four `self_check()`s, every publish gate and ten days live. Nothing structural can find the next one. Method: crop the bracket-column strip at native resolution, 260–320px wide, and **count the leaders entering each vertical before counting the lines in the block**. A spouse whose line carries no rule had no recorded issue. The data-driven audit (426 checks, `_GROUPS` → named leader → bracket start) is done and clean — it cannot catch data and rendering agreeing with each other and disagreeing with the plate |
| Widen `/search/`'s Name column | small, needs you | Names still wrap at their editorial `<wbr>` seams — 8 of the first 60 rows, 59.3px against 56px. Widest name measures **196px** against a 116px column. Widening removes the wrapping and moves the pan threshold from 672px to ~756px. Declined today because `nowrap` would truncate a transcribed name |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged. No branch build; the fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** That separates *the plate eats the gesture* from *the document is locked*. Unverified and stays so — it was last reported clear on the *live* site, which never carried it |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **Host CSS supplies what the widget lacks; layout goes upstream.** The test is
  whether the widget *standing alone* would want the change. The h1 size is
  host-specific (its own site should keep its big heading) and is injected here;
  the one-line control row and the columnar list are that widget's layout
  however it is served, and both live in `src/search.css`. If a host override is
  ever unavoidable, **anchor it to the vendored rule and fail the build when
  that rule moves** — that anchor is what caught the control-row override the
  moment it became redundant.
- **`/search/`'s All People list is a table at every width and pans below
  672px.** The user chose this over two alternatives. The pan is the
  **document's**, not an inner scroller's: an inner scroller captures the sticky
  header's scroll container and the column names stop following the reader down
  634 rows. It also keeps the site to one horizontal scroller while the plate's
  `.scroll` has an open Safari symptom.
- **Names wrap, and that is editorial, not a styling gap.** Seams are decided in
  `build.py` and ratified 2026-08-08. `nowrap` truncates a transcribed name.
- **The `/search/` h1 is derived, never restated** — all three declarations read
  out of `CSS`'s h1 rule; the build aborts if one leaves it.
- **A column is as narrow as its CONTROL allows**, never as its values look. Sex
  is set by its `select` (which sizes to its widest *option*), Clan by its
  disclosure at 76px.
- **Everything from the previous session still stands**: a row's height is
  stated, not inferred (`height:var(--lh)`; **do not** simplify back to
  `line-height`); the 1px overlap on abutting rules was tried and reverted; the
  Scale control is innocent; IV's 5/+6/+7 is not the `LEADER_ON_SPOUSE_ROW`
  shape; the `/search/` link sits outside the contents `<ol>` and says
  *entries*; Search sits in `.mast-right` and its phone cost is measured; three
  apparatus sections fold and two do not; one theme storage key, no bridge;
  `laguna-search` stays a separate private repo; `/search/` is absent from
  `sitemap.xml`; the twelve unattested cross-plate joins are the edition's.

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
- **`laguna-search`'s join count** — corrected 2026-08-09. Eight name-match
  joins.
