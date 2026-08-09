# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-09**. `6a882ee` (PR #39) is now the last commit to touch
a built page, superseding `5441abc`.

**The cross-plate search page is live at `/search/`.** The `laguna-search`
finding aid is part of this site: its `dist/` is vendored into `vendor/search/`,
and `write_search()` in `make_chart.py` turns that into `docs/search/`. **That
repo itself stays private** — only its build output is published. `--public`
now builds **7 pages**; the sitemap carries **5**, and that gap is correct.

Verified live by SHA-256 across all seven pages, sitemap 5 locs, stale-identity
grep 0. `?q=awie` returns the II·230 / III·228 join on the deployed page.

## Start here in a new chat

1. This file.
2. `CLAUDE.md` → *The search page is vendored, not generated here* — the new
   section, and where every rule from this session lives.
3. `CHANGELOG.md`'s 2026-08-09 entry for the detail.

Preview: `preview_start`, config name `site`, serves `docs/` on
`http://localhost:4173`.

## State

**Nothing is half-finished, and that is meant literally** — clean tree, no open
PRs, no unmerged branches, and a rebuild leaves `docs/` byte-identical to what
is committed. All four plates published, all 713 entries, no reading question
open on any plate.

The one thing that is *deliberately* not done: `laguna-search`'s README says
nine of its joins rest on an exact name match; counting its tuples it is
**eight**. That is in the other repo and uncorrected there. It is a
documentation slip, not a data error — the fourteen joins themselves are right,
and METHOD.md states eight.

## The open thread

**There isn't one.** Nothing is pending here, and the next session is more
likely to be started by something you want than by something left behind.

If you want the nearest thing to unfinished business, it is the **`storageKey`
option in `laguna-search`'s widget**. This site stores the palette under
`lg-theme` and the widget under `laguna-theme`, and both drive
`html[data-theme]`, so `write_search()` injects a bridge to keep them in step.
The bridge is tested and works both directions; a `storageKey` option would
delete it outright. **Ask for one before adding a second patch of that shape** —
that is the trigger, not the bridge itself, which is fine as it stands.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| `storageKey` in the widget, retiring the theme bridge | small, other repo | Cleanup, not a fix. The bridge works |
| Correct `laguna-search`'s README: eight, not nine | tiny, other repo | Its `INFERRED_IDENTITIES` tuples are the authority |
| Link `/search/` from the landing page's contents list | small | The masthead already reaches it from every page; this is additive, not a gap |
| A better AMNH scan | needs you | `2246/158`. **Ask for a photograph first** — that is what settled the second sort. `digitallibrary.amnh.org` 403s automated fetches |

## Before touching the search page

Three things that will not announce themselves:

1. **`vendor/search/` and `docs/search/` are BOTH generated.** Hand-edit either
   and the change is gone on the next re-vendor or build, silently.
2. **The font injection has no downstream guard.** `search.css` declares no
   `@font-face`; `write_search()` supplies it. `subset_font.py`'s coverage check
   reads the *text* of built pages, and the names arrive from JSON at runtime,
   so it sees an effectively empty page. Drop the injection and the page keeps
   working, silently substituting.
3. **The leak sweep never opens `search.js` or `search-index.json`** —
   `check_published_pages()` globs `*.html`. Both were checked by hand at
   publish. Re-check by hand whenever `vendor/search/` is re-vendored.

And if the register's markup moves, `/publish` **Gate 8** applies:
`python3 build.py --refresh` in the `laguna-search` checkout, re-vendor,
rebuild, publish. **`--refresh` is not optional** — without it that build
re-parses a cache of this site as it was before the push, and every gate passes
against the old pages. Whether the gate is due is settled by a **diff**, not by
memory: filter the publish's diff of a table page for `.reg`, `.reg-rel`,
`.num`, `.xref`, `sic-ring` and count. It was 0 on 2026-08-09.

## Decisions already made — don't re-litigate

- **SUPERSEDED 2026-08-09 — the user moved Search into `.mast-right` beside
  Theme.** The phone bar is now three rows / 157px, exactly the cost recorded
  below; 1280px is unchanged at 49px. The entry is kept because the rest of it
  still stands: don't shave gaps to buy the row back, and the wordmark's row is
  where it goes if it is ever moved back. See `CLAUDE.md`.
- ~~**The masthead's Search link sits beside the wordmark.**~~ Measured, not
  chosen: in `.mast-right` it takes the phone bar from two rows to three,
  109px → 157px. Don't tidy it, and don't shave gaps to buy the row back —
  44px is `--tap`.
- **`/search/` is absent from `sitemap.xml`** because the page ships
  `robots=noindex`. Not a de-indexing measure.
- **`laguna-search` stays a separate, private repo.** Only its output is
  published. Considered and declined 2026-08-09: merging it in would publish
  the repo, put its gates on this publish path, and destroy the independence
  that makes its `validate.py` worth anything — it checks this edition by
  parsing the *published pages*, not the transcription modules.
- **The twelve unattested cross-plate joins are the edition's**, documented in
  METHOD.md's *Identity across plates*, marked **NOT PRINTED** wherever they
  appear, and confined to the search page. The chart and register are untouched.

## Closed — do not re-raise

These are settled. Listing one as pending invites a decided question to be
re-taken.

- **De-indexing** — closed 2026-08-08 by the user. Not important, nothing to be
  done. `robots.txt`, `sitemap.xml` and the JSON-LD stay as the build emits
  them.
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
