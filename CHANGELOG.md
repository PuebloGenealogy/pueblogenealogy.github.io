# Changelog

What changed, when, and anything a future session would otherwise re-derive.
Newest first.

## 2026-07-27 — Search Console verified, fieldwork notes recovered from v1

- **Google Search Console ownership verified** on the URL-prefix property for
  `https://pueblogenealogy.github.io/`. The token is in
  `GOOGLE_SITE_VERIFICATION` in `make_chart.py`; blanking it drops the tag on
  the next build and ownership lapses. A Domain property cannot work here —
  `github.io` is on the Public Suffix List.
- **Recovered two editorial additions from v1.** Fable's clone sat 5 commits
  behind v1's `main`, so this edition never had them. Three of the five were a
  chart key that Fable had independently rebuilt; the other two were content:
  the dates of record (Genealogy I taken February 1918, Parsons returning June
  1919 for II–IV and revising I, chiefly name spellings) and what `d.` asserts
  (already dead *at time of recording*, year given when known). Both are now on
  the landing page, in each table's reading notes, and in METHOD.md/README.md.
- **Search Console and Bing both verified**; sitemap submitted (3 URLs). The
  dead v1 property was removed from Search Console. Bing was set up by importing
  from Search Console — the v2 property only.
- **v1 deleted.** `prettyph3nom/laguna-genealogy-tables` is gone and
  `prettyph3nom.github.io/laguna-genealogy-tables/` now 404s. This edition is
  the only one. Verified after the fact: repo 404, site 404, v2 unaffected.
- **Structured data corrected twice**, both found by Search Console rather than
  by the build. First: the landing page's `hasPart` entries were name-and-url
  stubs, and a nested Dataset is validated as a Dataset in its own right, so
  both failed the required `description`. Second: `isPartOf: {"@type":
  "WebSite"}` is valid schema.org but Google's Dataset validator rejects it —
  the collection relation it accepts is `includedInDataCatalog` +
  `DataCatalog`. `check_structured_data()` now guards both classes of failure
  and fails the build with exit 1. **Validating against schema.org is not the
  same as validating against Google**, and the check encodes only the rules we
  have actually been told about.
- **v1 mirrored before deletion** to
  `_backup-v1-laguna-genealogy-tables-2026-07-27/` — bare mirror plus working
  copy, `git fsck` clean, 19 commits over 4 refs, test-restored successfully.
  Deleting the repo itself is still outstanding; it needs `delete_repo` scope,
  which `gh auth refresh` cannot obtain non-interactively.

**Lesson worth keeping:** mirror before you delete. The two recovered notes
would have been lost silently, and nothing in the working tree hinted they
existed.

## 2026-07-27 — v2 published at pueblogenealogy.github.io

**The site moved to its own org, repo and root URL.**

- New home: `https://pueblogenealogy.github.io/`, from
  `PuebloGenealogy/pueblogenealogy.github.io`, Pages on `main` / `/docs`.
- Fresh git history. The previous folder was a one-commit shallow clone of the
  v1 repo (`prettyph3nom/laguna-genealogy-tables`) carrying the entire
  interactive redesign as *uncommitted* working-tree changes — roughly 2,850
  lines, never pushed. That work is now the initial commit here.
- Identity is two constants, `SITE` and `REPO` at the top of
  `scripts/make_chart.py`. Masthead and table links were already relative, so
  moving from a `/laguna-genealogy-tables/` subdirectory to a root URL needed no
  link rewrites at all.
- The v1 site is untouched and still live. Retiring it is an open task.

**SEO.**

- `og:image` / `twitter:image`: a 1200×630 band of the actual Table 1 plate,
  derived once with `sips` and committed at `assets/og-cover.jpg`. Not generated
  per build — the source scan is 33 MB and `sips` is macOS-only. `write_site()`
  copies it into `docs/`. Cards are `summary_large_image`.
- One `social_meta()` emits the Open Graph / Twitter block for every page.
- `FAQPage` structured data over five questions, with answers rendered as
  ordinary page text.
- `BreadcrumbList` on each table page.
- `Dataset` gained keywords, spatial and temporal coverage, `inLanguage`
  `["en","kjq"]`, and the Parsons citation. `KEYWORDS` and `SITE_DESCRIPTION`
  are single-sourced so meta, card and structured data cannot drift apart.
- `docs/404.html`, styled like the site.
- Landing copy now names the journal, volume and pages, and Kawaika.

**Workflow.**

- `.claude/launch.json` — `preview_start` config named `site`, serves `docs/` on
  port 4173.
- `.claude/skills/publish/` — `/publish`, the gated release procedure.
- `CLAUDE.md` rewritten for v2; this changelog started.

**Verified this session.** Both structural self-checks pass (104/27/80 and
73/14/58). The public build reproduces `docs/` byte-identically from
`scripts/`, confirming nothing in `docs/` was hand-edited. Column drift measured
**0 px at all five generations** of Genealogy I in the browser. All five live
routes return 200. All JSON-LD blocks parse.

**Gotcha worth remembering.** Creating the repo auto-enabled Pages from the repo
*root*, which served the rendered README at `/` and 404'd every subpath.
Repointing the source to `/docs` does **not** trigger a rebuild on its own — an
explicit `POST .../pages/builds` is required. Documented in the publish skill.
