# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**, at the end of a session that published the
`/search/` redesign.

**Everything is live and both repos are pushed.** That reverses the previous
handoff's headline, and it is still the least reliable sentence in this file —
take it from the repo, not from here:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

At the moment of writing: on **`main`**, clean, **0 ahead and 0 behind**, **no
open PRs**, and `laguna-search`'s `main` likewise at `6eaedb0` with nothing
unpushed. PR #50 was squash-merged as **`21454f7`** and its branch deleted; the
publish's own records went up as `5819f1b`. The wrap that revised this file
is a PR of its own, so expect exactly one open — and note that this is the
case `CLAUDE.md` warns the `SessionStart` hook cannot flag, because notes
committed alongside a build always look current.

**There is no open thread.** The work the last two sessions were asked for is
done, measured, published and verified. What is left is the list below, and its
first item has been deferred twice.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s two newest entries — the fourth records the publish and the
   dash; the third is the redesign it published, and is superseded in two
   places that the fourth names.
3. Only if you are touching `/search/`: `CLAUDE.md` → *The search page is
   vendored, not generated here* (six injections) and the `/search/` **All
   People** block under *Design invariants*.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **The pane caches `/search/` hard** — bust it with
`location.replace('/search/?v=' + Date.now())`, or a `?v=` on an iframe's
`src`. A narrow-viewport check needs a **fixed-width iframe**, not
`resize_window`; the pane widens to the content. And **`await
document.fonts.ready` inside the iframe** before measuring anything about text.

## State

**Nothing is half-finished.** `--public` exits 0 — 7 pages, 713 drawn, 10
JSON-LD blocks valid — and a rebuild reproduces `docs/` byte-identically from
the committed source. All four `self_check()`s pass.

The publish verified further than the gates require, and the two extra checks
are the ones worth repeating:

- **Live by SHA-256 including `search/search.js` and `search-index.json`.**
  `check_published_pages()` only ever opens `.html`, so those two are never
  swept by the build and never compared by the standard loop.
- **Gate 8's `--refresh` genuinely re-fetched** — the first line read
  `re-fetched`, not `cached in cache/` — and all three vendored files came back
  **byte-identical**. So "no re-vendor is due" is confirmed here rather than
  inferred from a diff.

One thing from the last session is now wrong and has been corrected in
`CLAUDE.md`: **the pan threshold is 651px, not 675px.** Shortening the Sex
filter's unrecorded option to a dash took 124px of column down to 80px, the
narrow grid gave up 24px, and the threshold moved by exactly that. The wider
lesson is in `CHANGELOG.md`: the threshold is the **whole grid's** minimum, so
any column's floor moves it — not only the Name column's, which is what the
previous entry concluded.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Bracket placement on Genealogy I and III** | large, needs you | **DEFERRED THREE TIMES now, not closed** — the largest correctness risk on the site. Method in full below. Nothing else on this list competes with it |
| The `/search/` provenance line's home | small, needs you | The All People standfirst went into `/search/`'s own footer note. The user said "put it in provenance"; that page's footer note is one reading, the landing page's *Provenance and use* the other. Offered twice, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | `Clear all` went from the section head; this one was kept deliberately — it is the only moment a reader can see no control to undo. Offered twice, not taken up |
| Widen `/search/`'s Name column | small, needs you | Declined because `nowrap` would truncate a transcribed name. **Its numbers went stale again**: the whole grid narrowed by 24px this session, so the 196px and the +84px shift both need re-measuring before this is worth anything |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |

## Deferred, not closed — bracket placement on Genealogy I and III

**Kept in full because it is the site's largest correctness risk and the method
is expensive to re-derive.** Deprioritised three times now, all on 2026-08-10,
in favour of `/search/` work. It has not been done and it has not been struck.

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

- **The wording of a filter option is a layout input.** A `select` sizes to its
  widest OPTION, not to its column, so the Sex column's 124/124/104px across
  three breakpoints was set by the string *Not recorded*. It is one **80px** at
  all three now. `title` carries the wording on hover; **`label` would replace
  the dash rather than describe it** — do not reach for it.
- **The dash's accessibility cost was raised and the change was asked for
  anyway.** A screen reader announces `—` as "dash" or as nothing, and `title`
  on an `<option>` is not reliably announced, so that one option's meaning now
  depends on sight; the select's `aria-label` is unchanged, so the control is
  still named. **A decision, not an oversight** — do not propose reverting it as
  a fix. If it is ever revisited the answer is a shorter *word*, since going
  back to *Not recorded* puts 44px into the column and the threshold back to
  675px.
- **The upstream-vs-host test decided everything in these two sessions**, six to
  three the first time and both halves upstream this time. The test is whether
  the widget standing alone would want the change. Table typography, a control's
  width and a filter's copy are the widget's; the bar's metrics, the
  standfirst's size and the rule under the title exist only to match *this*
  site.
- **The host bar's metrics are read out of `CSS` and emitted under the SITE's
  token names**, so every rule in it is the masthead's text with only selectors
  and colour tokens changed. A build guard aborts if `vendor/search/` ever
  declares one of those names. **Do not re-namespace them.**
- **`.lg-host-bar,.lg-host-bar *{box-sizing:border-box}` is load-bearing.** The
  widget scopes its reset to `.laguna-search *` and the bar is outside it;
  without this line the masthead's own declarations build a 65px bar.
- **`Clear all` is gone and `Clear filters` stays.** Not an oversight.
- **The count beside `Index` keeps `role="status"`.** It is a live readout.
- **`--lg-tap` is the search card's floor.** The controls are written as the
  token, not as 44px, to say that this is as compact as the card may get.
- **Everything from the previous sessions still stands**: the list is a table at
  every width and the document pans; names wrap at editorial `<wbr>` seams; the
  default palette is light and CSS is what says so; Theme sits at the foot; the
  pills carry the numeral alone with the word kept in the accessible name; a
  row's height is stated, not inferred; `laguna-search` stays a separate private
  repo; `/search/` is absent from `sitemap.xml`.

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
