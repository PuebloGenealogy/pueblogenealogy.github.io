# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-09**. **Nothing from this session is live.** The last
commit on `main` is still `bc73e6d`; two commits sit on an unpushed branch.

## State — read this before trusting anything else

**Two commits are finished, verified and NOT published**, on branch
`search-theme-storagekey`:

| | |
|---|---|
| `291e4dc` | the theme bridge retired for the widget's own `storageKey` |
| `b9fa181` | Search moved beside Theme; Editorial notes / Provenance / Citation fold |

**And a third commit is unpushed in the OTHER repo** — `laguna-search`
`9974d55`, which `vendor/search/SOURCE.md` names. The two are a pair: this
branch vendors that commit's `dist/`. Pushing one without the other leaves the
recorded provenance pointing at a commit nobody else can fetch.

Working tree clean, no open PRs, and a `--public` rebuild leaves `docs/`
byte-identical to what is committed. All four plates published, all 713
entries, no reading question open on any plate.

## Start here in a new chat

1. This file.
2. `CHANGELOG.md`'s two newest 2026-08-09 entries — the detail for both commits.
3. `CLAUDE.md` → *The search page is vendored, not generated here* (the theme
   key), the masthead paragraph, and the footer apparatus paragraph. All three
   were rewritten this session; the first two previously said the opposite.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`.

## The open thread

**Decide whether to publish, and if so publish both repos together.**

`/publish` for this branch. The `laguna-search` push is separate and manual —
its remote is `PuebloGenealogy/laguna-search`, private.

Two things settled during the work, so nobody re-checks them:

- **Gate 8 is NOT due.** The test is a diff, not a memory: filtering all four
  table pages' diff for `.reg`, `.reg-rel`, `.num`, `.xref` and `sic-ring`
  gives **0**. The whole diff is 68 added / 5 removed lines per page, and the
  removals are the moved Search link plus four headings that went inside a
  `<summary>`. The index was rebuilt anyway with `--refresh` and came back
  identical apart from `meta.generated`.
- **The hand leak check is done.** `leak_report()` was run over
  `docs/search/search.js` and `search-index.json` — the two files
  `check_published_pages()` never opens, because it globs `*.html`. Both clean.
  Redo it only on the next re-vendor.

**One gap in this session's verification, and it is the only thing an eye would
catch that a measurement did not.** Screenshots came back blank at any scroll
position other than 0, so **the folded footer was never seen, only measured** —
marker glyph, heading sizes against the two unfolded sections, cursor, grid
columns, left edge against the register, fold heights. The masthead *was* seen,
at 375px and 1280px. If the footer's appearance matters before it ships, open
the preview and scroll to it.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Publish the branch + push `laguna-search` | small | The open thread. Both, or neither |
| Correct `laguna-search`'s README: eight name-match joins, not nine | tiny, other repo | Its `INFERRED_IDENTITIES` tuples are the authority; METHOD.md already says eight |
| Link `/search/` from the landing page's contents list | small | Additive. The masthead reaches it from every page, so this is not a gap |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Before touching the search page

1. **`vendor/search/` and `docs/search/` are BOTH generated.** Hand-edit either
   and the change is gone on the next re-vendor or build, silently.
2. **The font injection has no downstream guard.** `search.css` declares no
   `@font-face`; `write_search()` supplies it. `subset_font.py`'s coverage check
   reads the *text* of built pages, and the names arrive from JSON at runtime,
   so it sees an effectively empty page. Drop the injection and the page keeps
   working, silently substituting.
3. **The leak sweep never opens `search.js` or `search-index.json`.** Re-check
   by hand whenever `vendor/search/` is re-vendored.
4. **`--refresh` is not optional** on the first `build.py` run after a publish,
   or its gates pass against a cache of the site as it was before the push.

## Decisions already made — don't re-litigate

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
