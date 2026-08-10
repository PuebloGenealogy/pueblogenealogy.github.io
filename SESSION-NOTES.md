# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**. A site-chrome session: six edits the user asked
for, all built and measured, committed on a branch and **NOT published**. Two of
them were upstream, in `laguna-search` at **`321f814`**, pushed.

**These notes were written before the branch was pushed and the PR opened, so
they understate what is done — that is the usual direction of this error. Take
the publication state from the repo, not from here.**

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the six edits, the Clan-menu defect that had
   been live since the filter header was built, and what was checked before
   committing.
3. Only if you are touching the theme or the masthead: `CLAUDE.md` →
   *The theme control has no Auto state* (rewritten — the default is now light,
   and CSS is what says so) and the *numeral-only pills* note under
   *Design invariants*.
4. Only if you are touching `/search/`: `CLAUDE.md` → *The search page is
   vendored, not generated here*, which now carries the second declaration in
   `THEME_KEY_DECL`, the two specificity traps, the pan-into-view rule and the
   third re-vendor shape.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **A narrow-viewport check needs a fixed-width iframe,
not `resize_window`** — the pane widens to the content and there is no pan to
photograph. See `CLAUDE.md` → *Preview*. Note the pane also paints at a width
that disagrees with the `innerWidth` it reports; read `innerWidth` before
believing a screenshot, and prefer measuring to looking.

## State

**Nothing is half-finished. Both repos are committed. The site is live on the
PREVIOUS build.**

**This session's work is on a branch and a PR; the DEPLOYED content is still
`2313ac4`'s `docs/`.** That is the one thing to establish before anything else,
because it is the gap a cold start will not see: `--public` reproduces `docs/`
byte-identically from `scripts/`, so the repo looks entirely consistent while
the public site shows the old masthead, the old theme default and the broken
Clan menu. **`/publish` is the whole of what is outstanding**, once the PR is
merged.

Take publication state from the repo, never from this file:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

`laguna-search` is at **`321f814`**, pushed, level with origin — the Clan menu
fix, the menu's pan-into-view, the two search halves on one line, the theme
control at the foot, the All People standfirst moved into the footer note, and
`color-scheme` following `[data-theme]`. `vendor/search/` was re-vendored from
that commit and `SOURCE.md` names the SHA.

A `--public` build exits 0: 7 pages, 10 JSON-LD blocks valid, leak gate clear.
`leak_report()` was run by hand over all three vendored files — clean.
Gate 8's diff test was **0 register-bearing lines on all four plates**, and
`search-index.json` came back byte-identical, so no `--refresh` was owed for the
re-vendor. **The post-publish `--refresh` run is still owed** — that is a
separate obligation and it is never optional.

All four plates published, 713 entries, no reading question open.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, `sitemap.xml` `lastmod`. If tomorrow's first `--public`
shows pages moving on those and nothing else, that is the clock, not a content
change: `git checkout -- docs/` and move on. **This matters more than usual
right now**, because `main` and the deployed build genuinely differ — a date-only
diff must not be mistaken for that difference, or for its resolution.

## The open thread — publish, then the plates

**Publish first. It is small and it is blocking.** Six user-requested changes
sit on `main` unseen, including a defect fix: on the live site the Clan filter
on `/search/` still draws a column of black squares with no clan names on any
window under 860px. `/publish` is the whole of it. Then run
`python3 build.py --refresh` in the `laguna-search` checkout — its gates
otherwise pass against a cache of the site as it was.

**Then the standing thread returns: bracket placement on Genealogy I and III,
never read against the scan.** **Needs you.** Genealogy IV shipped on
2026-07-31 with person 20 attached to the wrong marriage, and it survived four
`self_check()`s, every publish gate and ten days live. **Nothing structural can
find the next one**: 19 and 20 are both Bear, exactly like their mother, so clan
descent cannot discriminate, and the counts close either way.

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

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Publish** | small, blocking | See the open thread. `main` is six changes ahead of the live site, one of them a defect fix. Then `--refresh` over there |
| The `/search/` provenance line's home | small, needs you | The All People standfirst went into `/search/`'s own footer note, beside "A read-only finding aid…". The user said "put it in provenance" and that page's footer note is its provenance block — but the landing page's *Provenance and use* is the other reading. Offered and not taken up; ask before moving it |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. On a chart page nothing in the chrome says *Laguna Genealogies*; it survives in the `<title>`, the citation and the landing page. Flagged, not objected to |
| Widen `/search/`'s Name column | small, needs you | Names still wrap at their editorial `<wbr>` seams — 8 of the first 60 rows, 59.3px against 56px. Widest name measures **196px** against a 116px column. Widening removes the wrapping and moves the pan threshold from 641px to ~725px. Declined 2026-08-10 because `nowrap` would truncate a transcribed name |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. No branch build; the fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** That separates *the plate eats the gesture* from *the document is locked*. It was last reported clear on the *live* site, which never carried the fix |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

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
