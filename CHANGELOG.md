# Changelog

What changed, when, and anything a future session would otherwise re-derive.
Newest first.

## 2026-07-28 — DOI minted; table pages reworked for readability and reach

- **Archived at Zenodo; the edition has a DOI.** Concept doi
  `10.5281/zenodo.21637900`, first release `v1.0.0`. Zenodo's webhook is on the
  repo, so **cutting a GitHub release now mints a new version doi
  automatically** — that is a side effect worth knowing before tagging
  casually. `.zenodo.json` controls the record and is read from the **tagged
  commit**, so it must be on `main` before a release is cut; without it Zenodo
  titles the deposit after the repo. The doi is in `CITATION.cff`, the README
  badge, the citation block on every table page, and as JSON-LD `identifier`
  (`Dataset` on table pages, `CollectionPage` on the landing page, which is the
  entity the deposit actually corresponds to). Always the **concept** doi, never
  a version doi: a version doi on the page would rot every printed citation at
  the next release.
- **The chart key and the plate caption were removed** from the table pages.
  `key_html()` and the `.key` CSS are kept but **unreferenced**, deliberately,
  as the starting point for a redesign. Consequence to fix when that lands:
  three notations — `+` for spouse, `F.`/`M.` for sex, and the leader rule — are
  now explained nowhere on the page. The rest survive in the footer apparatus.
- **Toolbar, typography and navigation reworked.** `--tap` floors every hit area
  (32px mouse, 44px coarse pointer) and `--bar-h` derives from it. Table links
  became labelled buttons with the current page a filled inversion, not a colour
  shift, so it survives both themes and colour blindness. The apparatus moved
  from 14px to fluid 16–18px, cutting the measure from ~96 to ~64 characters.
  Generation columns are spelled out. The whole printed line now opens a
  person's card, guarded so a text selection stays a copy gesture. `see above` /
  `see below` are links, targeted from the union whose children the note stands
  in for — never by parsing the English.
- **Colour was tried three ways and ended flat.** Sex-coloured names (blue/pink)
  and 13 per-clan colours were both built and both **reverted**. The
  measurements are the reason, and are worth not re-deriving: two colours that
  must each clear 4.5:1 on the same paper cannot differ from each other by much,
  so the sex pair sat at **1.05:1** — hue-only, and unreadable under
  deuteranopia. The 13-clan palette was chosen by optimisation, not by eye, and
  its closest pairs still fell to about **one just-noticeable difference** under
  deuteranopia. All text on a table page is now `--ink` via `body.chart`
  redefining `--muted`; `--rule` is untouched, because the brackets and leader
  rules are drawn structure, not text.
- **Phonetic glyph coverage proven without a device.** Reading the shipped woff2
  binaries with fontTools, all 85 characters in the transcription and all 94
  rendered on Genealogy I are in the cmap of both faces. The faces are base64
  data URIs, so nothing is fetched and nothing can 404, and no combining marks
  are used. Tofu is ruled out by construction. Note macOS substitutes for any
  font, so **no on-screen comparison here can demonstrate absence of
  substitution — read the cmap, do not measure widths**. Live rendering on
  Windows and Android is still unchecked.
- **Custom domain considered and declined for now.** `pueblogenealogy.github.io`
  is a GitHub subdomain, not an owned domain. The doi is now the durable citable
  identifier and resolves independently of the host, which removes the strongest
  argument for buying one. If that changes, do it **before** seeding inbound
  links, since those point permanently at whatever host is chosen.
- **Session handoff made structural, not remembered.** Three pieces, because
  the record kept depending on someone thinking of it: `SESSION-NOTES.md` is a
  **rolling** handoff — overwrite it, never append, or it becomes a second
  changelog and stops answering "what do I pick up?"; `/wrap-session` writes it
  and backfills this file; and a `SessionStart` hook
  (`.claude/hooks/session-start.sh`) reads it into a new session automatically,
  so nothing has to be linked by hand. The hook also flags the two silent
  failures — notes older than the last `scripts/`/`docs/` commit, and an
  unclean tree — and fails open, exiting 0 with no output on any error.
  **What a hook cannot do:** `prompt` and `agent` hook types are restricted to
  tool events, so session-event hooks are shell commands only and can never
  author a changelog entry. Reading is automatic; writing still needs the
  skill. `Stop` was the wrong event — it fires after every assistant turn, not
  at session end.
- **`CLAUDE.md` gained a Design invariants section.** Four rules that read as
  styling preferences and are not: the root font size is pinned at 16px because
  `GEOM` states the plate grid in rem against it; a selected `.line` may change
  `background`, `box-shadow` and `outline` and nothing else, or the sibling
  bracket leaves its `mother_row`; `--rule` is excluded from the `body.chart`
  text flattening because brackets are drawn structure, not text; and `--tap` /
  `--bar-h` are stated once and derived. It also names the two things that look
  like bugs and are deliberate — the unreferenced `key_html()`, and the
  visually-hidden "Genealogy" in the table pills below 26rem.
- **This changelog was itself the thing that went missing.** Five PRs merged
  before anyone noticed the entry stopped at the previous day, because the
  session merged PRs directly instead of running `/publish`, whose last gate is
  *record it*. `/publish` now also says that publishing and releasing are
  different acts — pushing deploys the site, but cutting a GitHub release mints
  a new Zenodo version doi.
- **Deleting `prettyph3nom/laguna-genealogy` is blocked on a token scope**, not
  on work: `gh` holds `gist, read:org, repo, workflow` and repo deletion needs
  `delete_repo`, granted through a browser flow no agent can drive. It is empty
  and is **not** the v1 repo — v1 was `laguna-genealogy-tables`, which 404s
  under both owners. Carried in `SESSION-NOTES.md` with a note not to retry it
  blind.
- Zero column drift held at every step; re-measured after each change.

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
