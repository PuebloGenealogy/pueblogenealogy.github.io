# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-09**. **Something is half-finished, deliberately** — see
*State*. The live site is unchanged from the last publish.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the `/search/` link, and the two failed
   attempts at the Safari scroll bug.
3. Only if you are touching the plate's scroll behaviour: `CLAUDE.md` →
   *Preview*, which now records why this preview cannot settle a Safari
   question, plus the two WebKit facts it cost to learn.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug.

## State

**PR #43 is open, a draft, and must not be merged as one.** Two commits on
`handoff-2026-08-09-search-link-safari-scroll`, both pushed:

- **`59328e2` — the `/search/` link on the landing page. Finished and
  verified.** Stands on its own and can be merged alone.
- **`938b8e8` — the Safari scroll fix. UNVERIFIED.** It may be right; nothing
  available here can say.

Pages deploys from `main`/`docs`, so **merging is publishing** — which is why
this is a draft and why nothing below is live. `main` is untouched and matches
the last publish.

**`laguna-search` is clean and pushed**, at `44e3d7b` — its README and
ANALYSIS.md said nine name-match joins where `INFERRED_IDENTITIES` holds eight
(8 name-match + 4 differing-spelling + 2 identified by the edition through a
second husband = 14; nine totalled fifteen). The ninth came from counting the
five siblings' *mother* into the first group, and she is one of the four
spelling cases, so "with their mother and father" was corrected to "with their
father" in the same sentence. Nothing computed was ever wrong — that tool
reports the count from `len(INFERRED_IDENTITIES)` — and nothing in this
edition's METHOD.md or published pages was affected.

All four plates published, all 713 entries, no reading question open on any
plate.

## The open thread — the Safari scroll freeze, still unresolved

**The user closed the session with this deliberately unresolved.** Do not treat
`938b8e8` as a fix; treat it as a hypothesis that has been written down.

**The symptom, in the user's words:** scrolling with the mouse wheel inside a
table stops, and a reload is needed. Refined across two rounds — *vertical dies
while sideways panning still works*, and it follows **a click anywhere on the
table**, including the inert space between names. Safari.

**What is established, by measurement:**

- `.scroll` computes `overflow-y: auto` though only `overflow-x` is authored —
  the propagation rule promotes a `visible` axis whenever the other one
  scrolls. So the plate is a vertical scroll container with **zero range**
  (`scrollHeight` == `clientHeight`, both 6164 on Genealogy II). A written
  `overflow-y:clip` computes to `hidden` here for the same reason.
- Pinning that axis **changed nothing** and was measurably inert
  (`clientW/scrollW/clientH/scrollH` unchanged at 1250/2504/6164/6164). It was
  **reverted, not shipped** — the consuming axis is the horizontal one.
- The region is `tabindex="0"` (arrow-key panning, and the "Skip to chart"
  target), and a click on inert plate space does nothing else at all. Focus is
  the only click-persistent state on that element, which is what `938b8e8` acts
  on.

**Why it is unverified, and why that will not change here:** the preview is
Chromium, which does not route the wheel to a focused scroll region, so it can
neither reproduce the symptom nor demonstrate the cure. Chromium *can* confirm
the change is otherwise sound, and does: a click on inert space leaves focus on
`BODY`, a click on person 1's line still opens the card and selects `p1`, and
`tabindex` is restored either way. Arrow-key panning could not be exercised —
the harness's key input was unreliable all session.

**The one question that moves this forward, and it needs the user:** with the
branch built and served, click the plate in Safari and scroll. If it is still
stuck, ask whether clicking the **prose below the plate** frees it. That single
answer separates *the plate is eating the gesture* (focus — the current
hypothesis) from *the document itself is locked*, which would point at Safari's
popover handling and needs a different fix entirely.

**If it turns out to be wrong, drop `938b8e8` and merge `59328e2` alone.**

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Merge `59328e2` (the `/search/` link) and publish | small | Ready. Splitting it out of #43 is the point of the two-commit split |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Before touching anything

1. **PR #43 is open and unmerged. Do not branch new work off `main` and merge
   past it.** `CLAUDE.md` → *Environment* records how a stale open PR turns into
   a **revert**: squash-merge something branched later, and #43 would propose to
   undo it. Merge it, close it, or rebase it — but decide about it first.
2. **`vendor/search/` and `docs/search/` are BOTH generated.** Hand-edit either
   and the change is gone on the next re-vendor or build, silently.
3. **The leak sweep never opens `search.js` or `search-index.json`.** Both were
   hand-checked clean on 2026-08-09 and are byte-identical to the current
   `laguna-search` output, so that check still holds. Redo it on the next
   re-vendor.
4. **`--refresh` after a publish, always** — done for the last one. Decide a
   re-vendor from the register-markup diff, never from `meta.generated`. That
   diff was **0** for everything in #43, so no re-vendor is due for it.

## Decisions already made — don't re-litigate

- **The `/search/` link sits outside the contents `<ol>`**, not as a fifth
  numbered plate — the list is the edition's plates in Parsons's order. Its
  count is computed, and it says **entries**, not people: the search page's own
  line reads "620 people, drawn 713 times".
- **The `overflow-y` pin on `.scroll` was tried and reverted.** Measurably
  inert, wrong axis. Don't re-propose it as an obvious first move.
- **Search sits in `.mast-right` beside Theme**, moved there by the user
  2026-08-09. It costs a row on a phone — 375px 109px → 157px — and that cost
  was measured before and after and agreed. **Don't shave gaps to buy it back.**
- **Three apparatus sections fold; two do not.** *The record* and *Navigating
  this chart* stay open. **Do not fold *Navigating this chart* later.**
- **One theme storage key, not two.** The widget takes `storageKey`; the host
  declares `window.LAGUNA_THEME_KEY` once. **Do not reintroduce a bridge.**
- **`laguna-search` stays a separate, private repo.** Only its output is
  published.
- **The twelve unattested cross-plate joins are the edition's**, documented in
  METHOD.md's *Identity across plates*, marked **NOT PRINTED**, and confined to
  the search page.
- **`/search/` is absent from `sitemap.xml`** because the page ships
  `robots=noindex`. Not a de-indexing measure.

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
- **`laguna-search`'s join count** — corrected 2026-08-09 in that repo,
  committed and pushed. Eight name-match joins.
