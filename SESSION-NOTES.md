# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**, at the end of a session that redesigned `/search/`.

**Nothing from that session is live, and both branches are unpushed.** That is
the one thing to establish before anything else, and this file is the least
reliable place to read it from — take it from the repo:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
git log --oneline origin/$(git branch --show-current)..HEAD
```

At the moment of writing: **6 commits unpushed here**, **6 unpushed in
`laguna-search`**, and **PR #50 open** on this branch carrying only the previous
session's handoff. The wrap commit that adds this file makes 7.

**The open thread is publishing.** The design work the last session was asked
for is done and measured; what it has not had is a `/publish`.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the seven `/search/` changes, the
   upstream-vs-host split as a worked table, and the four measurements that
   cost something to get.
3. Only if you are touching `/search/`: `CLAUDE.md` → *The search page is
   vendored, not generated here* (now **six** injections, not five) and the
   `/search/` **All People** block under *Design invariants*.
4. Only if you are publishing: `/publish`'s own gates, and `CLAUDE.md` →
   *The re-vendor loop is `/publish` Gate 8*.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **The pane caches `/search/` hard** — a rebuild does
not show until you bust it (`location.replace('/search/?v=' + Date.now())`, or
a `?v=` on an iframe's `src`). This cost two false readings in the last
session, both of them "the change did not apply".

**A narrow-viewport check needs a fixed-width iframe, not `resize_window`** —
the pane widens to the content. And **`await document.fonts.ready` inside the
iframe before measuring anything about text**; see *State*.

## State

**Nothing is half-finished. Everything committed builds, and the build
reproduces `docs/` byte-identically.** `--public` exits 0: 7 pages, 713 people
drawn, 10 JSON-LD blocks valid, no research prose. `leak_report()` was run by
hand over all three vendored files after every re-vendor — clean each time.

What was done, in one line each: the list's names are smaller; the list is
headed **`Index`** with `620 people` beside it and no `Clear all`; the host bar
on `/search/` **is** the masthead, Search included; the title block's
standfirst and rule are the plates'; the search card is 26px shorter with every
box sharing an edge; and the number field's note is reworded.

**`search-index.json` was byte-identical through all six upstream commits, so
no `--refresh` was owed and none was run.** Nothing that gets parsed into the
index moved. This still leaves the **post-publish** `--refresh` obligation
untouched — that one is not optional and is not the same thing.

Three things learned that are now in `CLAUDE.md` rather than only here:

- **The pan threshold is 675px**, measured. Both previously recorded numbers
  were wrong, and `641` was a different quantity — the document's `scrollWidth`
  at phone widths.
- **The name's size is not a lever on that threshold.** Fixed 116px track.
- **Measure text with the font loaded.** A cold iframe reported 11 wrapped rows
  where the truth is 2. Plausible, silent, wrong by 5×.

## The open thread — publish it

Nothing is blocking. The work is measured and the repo is clean; it needs
`/publish`, which will merge PR #50 (or a fresh PR — see below) and push
`laguna-search`.

Four things specific to this publish:

- **PR #50 is the previous session's handoff PR and today's work is stacked on
  it.** Re-read its direction at the moment of merging, not from this file:
  `git diff origin/main origin/handoff-2026-08-10-search-browse-priority`, and
  read **deletions** as "the branch is behind `main`". It was purely additive
  when last measured, and a parked branch acquires drift in days.
- **`laguna-search` must be pushed too** — 6 commits on `main` there, and
  `vendor/search/SOURCE.md` names `499a3b4` as the vendored commit. A SHA in
  `SOURCE.md` that exists only in a local clone is the failure to avoid.
- **Gate 8's diff test will say no re-vendor is due**, and that is right: the
  register-bearing markup on the table pages did not move this session. The
  publish still owes the `--refresh` run afterwards.
- **Verify `/search/` live by SHA-256 including `search.js`**, which
  `check_published_pages()` never opens.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Publish the `/search/` redesign** | medium | The open thread above. Two branches, one PR, one `--refresh` after |
| **Bracket placement on Genealogy I and III** | large, needs you | **DEFERRED 2026-08-10 for the second time, not closed** — still the largest correctness risk on the site. Method in full below |
| The `/search/` provenance line's home | small, needs you | The All People standfirst went into `/search/`'s own footer note. The user said "put it in provenance"; that page's footer note is one reading, the landing page's *Provenance and use* the other. Offered, not taken up |
| Remove the empty state's `Clear filters` | small, needs you | `Clear all` went from the section head; this one was kept deliberately — it is the only moment a reader can see no control to undo. Offered, not taken up |
| Widen `/search/`'s Name column | small, needs you | Declined earlier because `nowrap` would truncate a transcribed name. **Its numbers are now stale**: the name is 1.2rem/1.05rem, so the 196px and the +84px shift both need re-measuring before this is worth anything |
| The masthead no longer names the edition | needs you | A consequence of "Home", not a defect. Flagged, not objected to |
| **The Safari scroll freeze** | needs you, awaiting recurrence | Unchanged and untested. The fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick onto a fresh branch off current `main` when it next appears. Ask first: **does clicking the prose below the plate free it?** |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first.** `digitallibrary.amnh.org` 403s automated fetches |

## Deferred, not closed — bracket placement on Genealogy I and III

**Kept in full because it is the site's largest correctness risk and the method
is expensive to re-derive.** Deprioritised twice now, on 2026-08-10 both times,
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

- **The upstream-vs-host test decided nine changes this session, six to three.**
  Upstream: anything about the widget's own copy, captions, control layout or
  typography. Host: the bar's metrics, the standfirst's size, the rule under the
  title — the three things that exist only to match *this* site. The test is
  whether the widget standing alone would want it.
- **The host bar's metrics are read out of `CSS` and emitted under the SITE's
  token names**, so every rule in it is the masthead's text with only selectors
  and colour tokens changed. A build guard aborts if `vendor/search/` ever
  declares one of those names. **Do not re-namespace them** — the point is that
  a diff between the two bars shows selectors and colours and nothing else.
- **`.lg-host-bar,.lg-host-bar *{box-sizing:border-box}` is load-bearing.** The
  widget scopes its reset to `.laguna-search *` and the bar is outside it;
  without this line the masthead's own declarations build a 65px bar.
- **`Clear all` is gone and `Clear filters` stays.** Not an oversight.
- **The count beside `Index` keeps `role="status"`.** It is a live readout.
- **The `tableHint` after the note's em dash stays.** It is the only place the
  selected-tables state is written down.
- **`--lg-tap` is the search card's floor.** The controls are written as the
  token, not as 44px, to say that this is as compact as the card may get.
- **Everything from the previous session still stands**: the list is a table at
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
