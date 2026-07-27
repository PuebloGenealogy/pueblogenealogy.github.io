# Changelog

What changed, when, and anything a future session would otherwise re-derive.
Newest first.

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
