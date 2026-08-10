# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-09**. The `/search/` link is **published and verified
live**. One thing is deliberately parked, unmerged: the Safari scroll fix.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s newest entry — the split publish, and why the scroll fix
   stayed behind.
3. Only if you are touching the plate's scroll behaviour: `CLAUDE.md` →
   *Preview*, which records why this preview cannot settle a Safari question,
   plus the two WebKit facts it cost to learn.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`. **If a screenshot comes back blank, read `innerWidth`
first** — a zero-sized viewport, not a scroll bug. See `CLAUDE.md` → *Preview*.

## State

**`main` is at `5495819`, pushed and live** — the landing page's contents block
carries the `.c-across` row to `/search/`. It reached `main` as a **cherry-pick
of `59328e2`**, not by merging PR #43. All seven pages verified by SHA-256
against `docs/`; sitemap 5 `<loc>` against a build count of 7 (correct);
identity grep 0; both `/search/` links serving. A `--public` rebuild on `main`
leaves `docs/` byte-identical, so `scripts/` and `docs/` agree.

**PR #43 is still open, still a draft, and holds one commit's worth of code —
`938b8e8`, the unverified Safari scroll fix.** The search link it also carries
is already on `main` by cherry-pick, so on `scripts/` and `docs/` the branch is
purely **additive**: +22 lines in `make_chart.py`, +22 in each table page, no
deletions.

**But it is BEHIND `main` on `CHANGELOG.md` and `SESSION-NOTES.md`, and merging
it as-is would revert them** to their state before this session's records were
written. That is the stale-PR-becomes-a-revert mechanic in `CLAUDE.md` →
*Environment*, in miniature, and it appeared *after* the branch was parked —
`main` moved, the branch did not. It is harmless while the PR sits unmerged.
Before ever merging it, bring `main` into the branch first, then read the
direction of the diff — deletions mean behind:

```bash
git diff --stat main origin/handoff-2026-08-09-search-link-safari-scroll
```

**`laguna-search` is clean at `44e3d7b`** and its post-publish `--refresh` is
done — `re-fetched`, all seven gates pass, all three vendored files
byte-identical, no re-vendor due. Its namesake gate still reports 3 pairs, 1
open (`II-182 / IV-69`).

All four plates published, all 713 entries, no reading question open on any
plate.

## The open thread — the Safari scroll freeze, now known to be intermittent

**Do not treat `938b8e8` as a fix. Do not merge it on the evidence below.**

The user reported the freeze "seems fixed for now" — **on the live site, which
does not carry `938b8e8`**. So the symptom cleared on a build with no fix in it.
That establishes one thing and refutes nothing: **the freeze is intermittent**,
so its absence is not evidence for the focus hypothesis, and the commit is
exactly as unverified as when it was written.

**The symptom, in the user's words:** scrolling with the mouse wheel inside a
table stops, and a reload is needed. Vertical dies while sideways panning still
works; it follows **a click anywhere on the table**, including the inert space
between names. Safari.

**What is established, by measurement** (unchanged — see `CLAUDE.md` →
*Preview*): `.scroll` computes `overflow-y:auto` though only `overflow-x` is
authored, so the plate is a vertical scroll container with zero range; pinning
that axis was measurably inert and was **reverted, not shipped**; the region is
`tabindex="0"`, and focus is the only click-persistent state on it, which is
what `938b8e8` acts on.

**What would actually settle it, and it needs the user:** the next time the
plate freezes in Safari, be on a **branch build** — not the live site — and try
the fix there. Ask the same diagnostic either way: **does clicking the prose
below the plate free it?** That answer separates *the plate is eating the
gesture* (focus — what `938b8e8` addresses) from *the document itself is
locked*, which points at Safari's popover handling and needs a different fix.

**If it turns out to be wrong, close PR #43 and drop the branch.** Nothing else
is riding on it.

**PR #43 stays parked — decided by the user 2026-08-09.** Not rebased, not
closed: the branch is what the Safari test build comes from when the freeze next
appears. Parked is safe; **merging it without first bringing `main` into it is
not** — see *State* for the two files it is now behind on. Nothing on `main`
depends on the branch: the CLAUDE.md paragraph on the Chromium/WebKit asymmetry
and the record of both scroll attempts were carried over during the wrap, so if
the branch is eventually closed unmerged, nothing measured is lost with it.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Before touching the search page

1. **`vendor/search/` and `docs/search/` are BOTH generated.** Hand-edit either
   and the change is gone on the next re-vendor or build, silently.
2. **The font injection has no downstream guard.** `search.css` declares no
   `@font-face`; `write_search()` supplies it. `subset_font.py`'s coverage check
   reads the *text* of built pages, and the names arrive from JSON at runtime,
   so it sees an effectively empty page. Drop the injection and the page keeps
   working, silently substituting.
3. **The leak sweep never opens `search.js` or `search-index.json`.** Both were
   hand-checked clean on 2026-08-09 and are byte-identical to the current
   `laguna-search` output, so that check still holds. Redo it on the next
   re-vendor.
4. **`--refresh` after a publish, always** — done for this one. It is a separate
   obligation from re-vendoring: it stops that tool's gates passing against a
   cache of the site as it was. **Decide a re-vendor from the register-markup
   diff, never from `meta.generated`**, which is date-granular and will differ
   by that one field on any later day. That diff was **0** for this publish —
   only the landing page and `404.html` moved.

## Decisions already made — don't re-litigate

- **The `/search/` link sits outside the contents `<ol>`**, not as a fifth
  numbered plate — the list is the edition's plates in Parsons's order. Its
  count is computed, and it says **entries**, not people: the search page's own
  line reads "620 people, drawn 713 times".
- **The `overflow-y` pin on `.scroll` was tried and reverted.** Measurably
  inert, wrong axis. Don't re-propose it as an obvious first move.
- **Search sits in `.mast-right` beside Theme**, moved there by the user
  2026-08-09. It costs a row on a phone — **375px 109px → 157px, three rows**;
  1280px unchanged at 49px — and that cost was measured before and after and
  agreed. **Don't shave gaps to buy it back**: `--tap` is `2rem`, and `2.75rem`
  under `(pointer:coarse)`, so the phone floor is 44px with nothing to reclaim.
  The wordmark's row is where it goes if it is ever moved back.
- **Three apparatus sections fold; two do not.** *The record* and *Navigating
  this chart* stay open. **Do not fold *Navigating this chart* later** — it is
  the only place `+`, `F.`/`M.` and the leader rule are decoded, and hiding it
  re-opens the defect that removing the on-page chart key was meant to close.
- **One theme storage key, not two.** The widget takes `storageKey`; the host
  declares `window.LAGUNA_THEME_KEY` once. **Do not reintroduce a bridge** — a
  second key is the defect, not the starting condition. If the widget ever needs
  another host-side value, ask for an option before writing a patch of that
  shape.
- **`laguna-search` stays a separate, private repo.** Only its output is
  published. Merging it in would publish the repo, put its gates on this publish
  path, and destroy the independence that makes its `validate.py` worth
  anything — it checks this edition by parsing the *published pages*.
- **The twelve unattested cross-plate joins are the edition's**, documented in
  METHOD.md's *Identity across plates*, marked **NOT PRINTED** wherever they
  appear, and confined to the search page.
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
