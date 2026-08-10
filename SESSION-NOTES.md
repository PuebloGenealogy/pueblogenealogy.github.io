# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**, after the publish. The six site-chrome edits are
**live**: PR #49 merged as **`863e60b`** and all seven pages verified against
`docs/` by SHA-256. `laguna-search` is at **`321f814`**, pushed, and its
post-publish `--refresh` has been run — clean, no re-vendor owed.

**Nothing is outstanding from that work.** Take the publication state from the
repo anyway, never from this file:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

**The next priority is set, and it is not the plates.** The user asked for
design work on `/search/`'s *Browse the complete edition* section, starting by
**reducing the font size of the names in the table**. Bracket placement on
Genealogy I and III is **deferred, not closed** — it is still the largest
correctness risk here, and it is written out in full below so deferring it costs
nothing later.

## Start here in a new chat

1. This file.
2. `CLAUDE.md` → *The search page is vendored, not generated here*, and the
   `/search/` **All People** block under *Design invariants*. Both are required
   reading for the open thread, not optional: they carry the upstream-vs-host
   test, the two specificity traps, the pan-into-view rule and the three
   re-vendor shapes.
3. `CHANGELOG.md`'s newest two entries — the publish, then the six edits and the
   Clan-menu defect that had been live since the filter header was built.
4. Only if you are touching the theme or the masthead: `CLAUDE.md` →
   *The theme control has no Auto state* (the default is now light, and CSS is
   what says so) and the *numeral-only pills* note under *Design invariants*.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **A narrow-viewport check needs a fixed-width iframe,
not `resize_window`** — the pane widens to the content and there is no pan to
photograph. See `CLAUDE.md` → *Preview*. Note the pane also paints at a width
that disagrees with the `innerWidth` it reports; read `innerWidth` before
believing a screenshot, and prefer measuring to looking.

## State

**Nothing is half-finished, nothing is unpublished, and no PR is open.** `main`
is at **`863e60b`** and the live site serves it. Both repos are committed and
level with their remotes.

The publish was clean end to end. What is worth carrying forward from it:

- **All seven pages verified live by SHA-256**, plus `search.js` and
  `search-index.json` — the two files `check_published_pages()` never opens.
  Status codes 200 on everything but `/fonts/`, which 404s harmlessly; sitemap 5
  `<loc>` against 7 built pages, which is the correct count; stale-identity grep
  0.
- **Publishing was merging.** The branch already carried a same-day `--public`
  build, so the post-merge rebuild reproduced `docs/` byte-identically and Gates
  3–5 had nothing to commit. A clean `git status` there is the confirmation, not
  a warning.
- **The post-publish `--refresh` is DONE**, and it genuinely re-fetched — first
  line `4 table pages, re-fetched`, not `cached in cache/`. All seven of that
  tool's gates pass, and all three `dist/` files came back **byte-identical** to
  `vendor/search/`, so no re-vendor was owed.
- **`307 KB` vs `308 KB` is not drift.** One file of 315,224 bytes = 307.8 KiB;
  `make_chart.py` floors it and `build.py` rounds it. Do not go looking.

`laguna-search` is at **`321f814`**, pushed, level with origin — the Clan menu
fix, the menu's pan-into-view, the two search halves on one line, the theme
control at the foot, the All People standfirst moved into the footer note, and
`color-scheme` following `[data-theme]`. `vendor/search/` is vendored from that
commit and `SOURCE.md` names the SHA.

All four plates published, 713 entries, no reading question open.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, `sitemap.xml` `lastmod`. If tomorrow's first `--public`
shows pages moving on those and nothing else, that is the clock, not a content
change: `git checkout -- docs/` and move on. It is now the *only* thing a
`docs/` diff on a clean tree can mean, since `main` and the deployed build no
longer differ.

## The open thread — design edits to `/search/`'s *Browse the complete edition*

**Set by the user 2026-08-10, and it is the top priority.** The section is the
All People card on `/search/` — the kicker `Browse the complete edition` is
written by `search.js:1451`, so grepping the HTML for that string finds nothing;
it is built at runtime.

**Start with the one thing named: make the NAMES IN THE TABLE smaller.** The
lever is `.laguna-search .cell.name`, and there are **two** declarations of it in
the vendored stylesheet, not one:

| Where | Today |
|---|---|
| `vendor/search/index.html:718` — the base rule | `font-size: 1.45rem`, `font-weight:700`, `line-height:1.12` |
| `vendor/search/index.html:1254` — inside the narrow media query | `font-size: 1.15rem` |

**Change one and the other silently disagrees at the width nobody checked.**
Decide what each should be, and say which width you measured at.

Four things to have in hand before touching it:

- **Apply the upstream-vs-host test first, and expect it to say UPSTREAM.** The
  test is whether the widget *standing alone* would want the change. Table
  typography is that widget's own layout, so this most likely belongs in
  `src/search.css` in `laguna-search` — not injected here. The h1 size is the
  counter-example that went host-side, and it went there because it had to sit
  on *this* site's type ramp; a name cell has no such tie. **Ask before writing
  a host override**, and if one is truly unavoidable, anchor it to the vendored
  rule so the build fails when that rule moves.
- **Shrinking the name changes the pan threshold, and that is a feature the user
  may or may not want.** Names wrap at their editorial `<wbr>` seams — 8 of the
  first 60 rows run 59.3px against 56px — because the widest name measures 196px
  against a 116px Name column. A smaller name narrows that 196px, so some
  wrapping will disappear on its own and the page will start panning at a
  narrower width. **Measure the new threshold; do not predict it.**
- **The recorded threshold numbers disagree with each other**, so trust neither
  without measuring: `CLAUDE.md` says widening the Name column moves it from
  **672px to ~756px**, this file said **641px to ~725px**. Both record the same
  +84px shift from a different base. Settle it by measurement and correct
  whichever is wrong.
- **A narrow check needs a fixed-width iframe.** `resize_window` widens the pane
  to the content, so there is no pan to photograph and `innerWidth` lies. See
  *Start here* above.

**Then the re-vendor.** If the change lands upstream, rebuild `dist/` there,
re-vendor the three files, update the SHA and date in `vendor/search/SOURCE.md`,
rebuild here and publish. Expect the **second re-vendor shape**: a stylesheet-only
change moves `index.html` alone, because that is where the CSS is inlined, while
`search.js` and `search-index.json` come back byte-identical. A byte-identical
index means **no `--refresh` obligation** — but `leak_report()` over all three
vendored files is due every time regardless.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Bracket placement on Genealogy I and III** | large, needs you | **DEFERRED 2026-08-10, not closed** — the user set the `/search/` design work above it. Still the largest correctness risk on the site; see the section below, which is kept in full because re-deriving it is expensive |
| The `/search/` provenance line's home | small, needs you | The All People standfirst went into `/search/`'s own footer note, beside "A read-only finding aid…". The user said "put it in provenance" and that page's footer note is its provenance block — but the landing page's *Provenance and use* is the other reading. Offered and not taken up; ask before moving it |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. On a chart page nothing in the chrome says *Laguna Genealogies*; it survives in the `<title>`, the citation and the landing page. Flagged, not objected to |
| Widen `/search/`'s Name column | small, needs you | Names still wrap at their editorial `<wbr>` seams — 8 of the first 60 rows, 59.3px against 56px. Widest name measures **196px** against a 116px column. Declined 2026-08-10 because `nowrap` would truncate a transcribed name. **Now coupled to the open thread**: a smaller name font changes the same measurement, so do this one second or not at all |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. No branch build; the fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** That separates *the plate eats the gesture* from *the document is locked*. It was last reported clear on the *live* site, which never carried the fix |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Deferred, not closed — bracket placement on Genealogy I and III

**Kept in full because it is the site's largest correctness risk and the method
is expensive to re-derive.** The user deprioritised it on 2026-08-10 in favour
of the `/search/` design work; it has not been done, and it has not been struck.

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

- **The default palette is LIGHT, and CSS is what says so.** Not the script.
  `:root{color-scheme:light}` makes `light-dark()` resolve light, and the
  `prefers-color-scheme` palette block is **deleted** — dark is reachable only
  through `[data-theme="dark"]`. **Do not reintroduce that block**: it restores
  OS-follows-you behaviour in exactly the no-JS case nobody looks at. A stored
  choice still wins, and nothing is written to storage until the reader presses
  the control. `/search/` gets the same default from a host-side declaration in
  `THEME_KEY_DECL`, deliberately not from another widget option.
- **The pills carry the numeral alone, and the word stays in the markup.**
  `.masthead nav .nav-word` hides "Genealogy " visually at every width; the
  accessible name is still "Genealogy I". **Do not delete the span.** The
  `≤26rem` rule is now `.mast-right .nav-word` and hides the Search label only —
  two selectors on purpose.
- **The wordmark reads "Home".** The bar is a way back, not a nameplate.
- **Theme sits at the foot of every page**, one `THEME_FOOT` string for all
  three page types, and it is named in `@media print` because hiding
  `.masthead` no longer covers it.
- **Upstream vs host was applied four more times, and split three to one.**
  Upstream: the Clan menu fix, its pan-into-view, the two search halves on one
  line, the theme control's move, `color-scheme` on `[data-theme]`. Host-side:
  the light default. The test is whether the widget *standing alone* would want
  the change.
- **`min-width: 0` contributes NOTHING to a track's minimum.** This bit twice in
  one day, one level apart: the search card first resolved to 345.6px with a
  190px name box inside a 161.8px column, and `.laguna-search` itself needed
  `min-width:min-content` or the two cards took different widths.
- **A menu on a panning page brings itself into view horizontally, not with
  `scrollIntoView`** — which would drag a sticky-headed page vertically to reach
  a menu already in view.
- **Everything from the previous session still stands**: `/search/`'s All People
  list is a table at every width and the document pans (confirmed on device
  2026-08-10, on a build that carried it); names wrap and that is editorial; the
  `/search/` h1 is derived from `CSS`'s h1 rule and the build aborts if it
  moves; a row's height is stated, not inferred (`height:var(--lh)`; **do not**
  simplify back to `line-height`); the 1px overlap on abutting rules was tried
  and reverted; the Scale control is innocent; IV's 5/+6/+7 is not the
  `LEADER_ON_SPOUSE_ROW` shape; the `/search/` link on the landing page sits
  outside the contents `<ol>` and says *entries*; `laguna-search` stays a
  separate private repo; `/search/` is absent from `sitemap.xml`; the twelve
  unattested cross-plate joins are the edition's.

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
