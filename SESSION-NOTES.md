# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-10**. Two publishes today, both verified live. A
placement error on Genealogy IV was found and corrected; every bracket on every
plate was misaligned in Safari and now is not.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the IV·20 correction and the WebKit row-box
   fix, including the two wrong turns taken first.
3. Only if you are touching row heights, brackets or anything a reader sees in
   Safari: `CLAUDE.md` → *A row's height is stated* and *Preview*.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug. See `CLAUDE.md` → *Preview*.

## State

**The deployed content is `c362028`'s `docs/`**, verified live by SHA-256: all
seven pages plus `search/search-index.json`, every path 200, sitemap 5 `<loc>`
against a build count of 7 (correct), identity grep 0. A `--public` rebuild
reproduces `docs/` byte-identical, so `scripts/` and `docs/` agree.

**`main`'s HEAD sits above that on records-only commits** — this handoff, and
the changelog. Don't read the two as disagreeing: check
`git diff c362028 HEAD -- docs vendor scripts`, which was empty when this was
written. **And take the publication state from the repo, never from this file** —
`/wrap-session` writes before the branch is pushed, so these notes are one step
behind themselves by construction:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

**No PR is open.** #45 (this session's records) merged; **#43 was closed
unmerged** — see the table below.

**`laguna-search` is clean at `44e3d7b`**, level with its origin, and its
`dist/` is what `vendor/search/` now holds. Its post-publish `--refresh` is done
(`re-fetched`, all seven gates pass). Namesake gate unchanged at **3 pairs, 1
open** (`II-182 / IV-69`) — correcting 20's father moved no fold collision.

**Nothing is half-finished.** `docs/_diag.html`, the throwaway self-measuring
diagnostic, is deleted; the method it proved is written into `CLAUDE.md` →
*Preview* and should be rebuilt from there rather than recovered from git.

All four plates published, 713 entries, no reading question open.

## The open thread — bracket placement on I and III has never been read against the scan

**This is new, and it is the lesson of 2026-08-10.** Genealogy IV shipped on
2026-07-31 with person 20 attached to the wrong marriage, and it survived four
`self_check()`s, every publish gate, and ten days live. The plate draws **one**
vertical over 19 and 20 with a **single** leader from 6's line; the
transcription had split it into two unions, so the chart asserted a paternity
Parsons does not state.

**Nothing structural can find the next one.** 19 and 20 are both Bear, exactly
like their mother, so clan descent cannot discriminate; the counts close either
way. `CLAUDE.md` is explicit that `self_check()` cannot see whether a person is
attached to the right parents.

What has been checked by a human against the scan: **Genealogy II** (the user's
full list, 2026-07-30) and **Genealogy IV's 5/6/7** (2026-08-10). **Genealogy I
and Genealogy III have not been.** III is the largest and most intricate — 261
people, seven generations, two descent blocks, 72 unions.

The method that worked, and it is cheap:

- Crop the **bracket-column strip** at native resolution — 260–320px wide, so
  the vertical and every stub entering it are the only things in frame. Never
  read structure off a downscale.
- **Count the leaders entering each vertical before counting the lines in the
  block.** One leader means one group however many `+` lines sit above it. That
  single question is what IV·20 turned on.
- A spouse whose line carries **no rule** had no recorded issue.

The automated half is already done and passes: a data-driven audit that reads
`_GROUPS`, takes each union's mother (or its `LEADER_ON_SPOUSE_ROW` spouse), and
asserts the bracket starts on that named person's line — 426 checks, all four
plates, clean. **It cannot catch a group whose data and rendering agree with
each other and disagree with the plate**, which is the whole remaining risk.

**Needs the user for adjudication.** Their reading wins on placement; present
the crop and the evidence, do not change a transcription unilaterally.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **The Safari scroll freeze** | needs you, awaiting recurrence | Still open as a *symptom*; **PR #43 was closed unmerged 2026-08-10**, so there is no branch build any more. The fix attempt survives as commit **`938b8e8`**, reachable by SHA — cherry-pick it onto a fresh branch off current `main` when the freeze next appears, which also tests it against a build that has the row-box fix. It is **unverified and stays so**: the freeze was last reported clear on the *live* site, which never carried it. Ask first, before writing any code: **does clicking the prose below the plate free it?** That separates *the plate eats the gesture* (focus, what `938b8e8` addresses) from *the document is locked*, which needs a different fix. Both attempts' reasoning is on `main` in `CHANGELOG.md` under 2026-08-09 |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Decisions already made — don't re-litigate

- **A row's height is stated, not inferred** — `height:var(--lh)` on `.line` and
  `.sic-row`, `min-height` on `.xref`. WebKit quantises a line box to a whole
  pixel (24.000px measured) while keeping margins at 24.796875px, so every row
  of offset lost 0.796875px and accumulated. **Do not simplify these back to
  `line-height` alone.** `.xref` keeps `min-height` on purpose: it is the only
  `white-space:normal` row, and `height` would make a wrapped reference overlap
  the row below instead of merely mis-budgeting it.
- **The 1px overlap on abutting rules was tried and reverted.** The "break" at
  III·113 → 204 was a **vertical** 0.8px step, not a horizontal paint seam;
  only-child groups have no bracket vertical to hide it. Don't re-propose it.
- **The Scale control is innocent.** The row-normalised error was identical at
  100%, 85% and 70%. If it ever looks guilty again, check you are not mixing
  `getComputedStyle` (unzoomed under CSS `zoom`) with `getBoundingClientRect`
  (zoomed) — that fabricates exactly 1.86px at 85% and 3.72px at 70%.
- **Genealogy IV's 5 / +6 / +7 is not the `LEADER_ON_SPOUSE_ROW` shape.** It
  looks like it — two husbands, three lines — but the plate draws one bracket
  off 6's line and gives 7 no rule at all. Tables 1, 2 and 4 still declare none.
- **The `/search/` link sits outside the contents `<ol>`**, count computed, and
  it says **entries**, not people.
- **Search sits in `.mast-right` beside Theme**, moved there by the user
  2026-08-09; it costs a row on a phone (375px 109px → 157px) and that was
  measured before and after. **Don't shave gaps to buy it back** — `--tap` is
  2.75rem under `(pointer:coarse)`, so there is nothing to reclaim.
- **Three apparatus sections fold; two do not.** *The record* and *Navigating
  this chart* stay open — the latter is the only place `+`, `F.`/`M.` and the
  leader rule are decoded.
- **One theme storage key, not two.** The widget takes `storageKey`; the host
  declares `window.LAGUNA_THEME_KEY` once. **Do not reintroduce a bridge.**
- **`laguna-search` stays a separate, private repo.** Only its output is
  published. Its independence is what makes its `validate.py` worth anything.
- **`/search/` is absent from `sitemap.xml`** because the page ships
  `robots=noindex`. Not a de-indexing measure.
- **The twelve unattested cross-plate joins are the edition's**, documented in
  METHOD.md, marked **NOT PRINTED**, and confined to the search page.

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
