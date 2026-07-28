# Changelog

What changed, when, and anything a future session would otherwise re-derive.
Newest first.

## 2026-07-28 — the person card gets its own format

- **The card was rendering the register's format.** It clones the register
  entry — one source of truth, which is right — but it was also inheriting a
  layout built for scanning 104 stacked entries. As a single card it now sets
  its own: the printed line is the title at `--t-lg` (a new 1.125rem step,
  added because the ramp stopped at `--t-md`) and underlined; the relation rows
  keep the register's 1.4rem indent instead of having it zeroed; each label
  gains a colon; each related person is a rounded chip.
- **Scoping is the whole trick, and the next change here must keep it.** Every
  CSS rule is under `.pcard` and every DOM edit is made on the *clone* in
  `openCard`, never in `rel_row` or `rel_link`. The register renders the same
  markup and must keep its dense list — verified after the change: its links
  still compute `display:inline`, its entry titles still 16px.
- **Chips are `.reg-rel > a`, direct children only.** A cross-reference row is
  *also* a `.reg-rel`, but its links sit inside an `<em>` of running prose —
  "For second wife and offspring see below, 76, 90-3". A descendant selector
  turns those into buttons mid-sentence. This is the trap in this markup.
- **Three edits to the clone, each with a reason not to do it the obvious way.**
  The colon and the number's point are written as real text, not CSS `::after`,
  so they survive a copy out of the card. The middot between relations is
  *collapsed to a space*, not deleted — deleting the text node also closes the
  gap after the label, and the space is what keeps copied text readable. Both
  text edits are idempotent, so reopening a card cannot accumulate `56..`.
- **Measured:** 4px radius chips, 26.6px tall, matching the 24px floor the
  card's action buttons already use rather than `--tap`; checked in both
  palettes and at 375px, where the card is the bottom sheet — chips wrap, no
  overflow, no horizontal body scroll.
- **Not done, and worth deciding:** the register's own relation lists still read
  `56 Weʼdyumă` without the point, while its entry titles carry it. The card
  just lost that inconsistency; the register still has it. One line in
  `rel_link` if it should match.

## 2026-07-28 — the person card drops the misprint note

- **The card repeated an annotation the reader was already looking at.** Opening
  the person card from the misnumbered `+` line under 76 appended
  *(misprint, click here to see notes)* directly under the card's first line —
  the same sentence, in the same red, as the `SIC_ROW` sitting on the chart row
  the card was opened from and anchored to. Two statements of one fact in a
  single glance. The card now carries **the number and nothing else**.
- **The number swap stayed.** `data-printed` on the link still makes the card
  read 68 from that line and 67 from person 67's other lines. That is plate
  fidelity, not annotation, and it is the half of this that must not be
  "simplified" away later. `.pcard-sic` and its CSS are deleted.
- **Where the misprint is still explained:** the chart's own annotation row, and
  the footer note at `#note-misprint`. Those are the only two places, by
  decision — same shape as the rule that keeps `+`, `F.`/`M.` and the leader
  rule decoded once, in the footer.
- **A person-level variant was built first and rejected by the user**, so don't
  rebuild it: the misprint was made a fact about the person (`Chart.sic` →
  `data-sic` on the register entry → note on *every* one of that person's
  cards). It worked — measured across all 214 chart lines, exactly the two
  occurrences of 67 carried it and no one else — but it multiplied the
  redundancy rather than removing it. Take it from git if it is ever wanted.

## 2026-07-28 — the theme button's static label said Auto

- **Fixing a miss from the entry below.** The Auto state was removed from the
  theme control, but the button still shipped `Theme: Auto` as its literal
  markup; `applyTheme()` overwrote it on the first tick, so it was only visible
  in the moment before the script ran. The static label is now bare `Theme`,
  which is all the server can honestly say — it cannot know which palette a
  reader resolves to.
- **Worth recording is how it was missed.** The check that passed was
  `!document.body.textContent.includes('Auto')`, run in the browser *after* the
  script had already rewritten the label. Testing rendered state cannot see what
  the HTML ships; for anything that exists in the markup, grep the built file.

## 2026-07-28 — selection highlights move off the text

- **The highlight no longer sits on the words it highlights.** All three of them
  — the selected chart row, the register entry, and a targeted footer note —
  used `box-shadow: inset 4px 0 0`, which paints a bar over the first glyphs,
  plus an outline hugging the text at `outline-offset:-1px`. Every part of the
  treatment is now drawn **outside** the border box: the leading rule is a
  shadow offset `-.3rem` with no spread, the halo a `.3rem` spread behind it,
  the ring an outline at a matching `+.3rem`.
- **Still layout-neutral, which is the constraint that matters.** Shadows and
  outlines take no space, so nothing moves: the selected row measures 25px,
  exactly as an unselected one does, all 24 child groups still sit on their
  mothers' lines, and column drift is 0px at every generation. Invariant 2
  permits `background`, `box-shadow` and `outline` on a selected `.line` and
  this uses only those three.

## 2026-07-28 — the misprint annotation gets its own row, and a colour

Refines the entry below, same day.

- **The annotation moved off the printed line.** It was sitting inline between
  the number and the name — inside the transcription, in other words. It is now
  *(misprint, click here to see notes)* on its **own row directly beneath** the
  Shuwaiʼᶦri line, so the printed line contains only what the plate prints.
- **`+ 68.` is ringed in red.** The ring is an `outline`, never a border or
  padding: a border widens the row and throws the sibling bracket off its
  `mother_row`, which is the failure this project has documented twice.
- **`--sic`, a new colour, and the only thing on a table page that is not
  `--ink`.** It is text, so it has to clear 4.5:1 on both papers by itself:
  `#B3261E` measures **6.43:1** on the light paper, `#FF8A80` **7.19:1** on the
  dark. Declared in all five theme blocks.
- **The person card follows the line it was opened from.** From the misprinted
  line it titles the card *68.* and repeats the red note under the first line;
  from person 67's three other lines it still says *67.*, and the register entry
  always says 67. Carried on `data-printed`, so the card is told rather than
  left to guess — verified in all three states.
- **The layout proof, because this added a row to the chart.** All **24** child
  groups were walked before and after: every sibling bracket still sits on its
  mother's line, 0 mismatches both times, and column drift is still 0px at every
  generation. The annotation row is exactly one `--lh` tall (25px, same as a
  `.line`) and is counted with `row += 1` like a cross-reference row, which is
  what keeps everything below it on the grid.
- Clicking the note from inside the card closes the card and lands on the
  highlighted note, clear of the sticky bar. Table 4 emits none of this markup.

## 2026-07-28 — the misprint is printed as printed; footer goes two-column

- **The plate's misprint is reproduced again, which is the point of the
  edition.** The `+` line under 76 on Table 1 is numbered **68** on the plate but
  names Shuwaiʼᶦri, Turkey = person 67. The chart had been drawing it as *67* —
  a silent correction, and a direct breach of the rule that misprints are
  annotated and not fixed. It now prints **68**, links to `#p67`, and carries a
  *misprint* marker that jumps to `#note-misprint` in the editorial notes, which
  is highlighted on arrival. Declared as data in `transcription.py`'s new
  `PLATE_NUMBER_MISPRINTS`, read through `union["printed_number"]` with
  `getattr`, so Table 4 needs no entry and the renderer stays table-agnostic —
  Table 1's numbering must not leak into it.
- **The footer apparatus is a two-column grid** of `.app-sec` sections at
  `--measure-wide`, one column below 56rem. Font size unchanged. Grid, not CSS
  multicolumn: multicolumn will happily break an `h2` away from the `ul` it
  introduces. Side effect worth having — the footer now shares a left edge with
  the register above it, closing one of the four-left-edges findings recorded
  two entries below.
- **Person references in the apparatus are links.** `1+2`, `54+55`, `Person 8`,
  `58+59`, `76`, `person 67`, and Table 4's `3`, `4`, `59+60`, `36-43`, `50-53`,
  `19`, `20`, `73` all resolve to `#pN`. Done with a `_p()` helper at each call
  site, **never a regex over the prose** — the apparatus is thick with numbers
  that are not people (1923, vol. 19, pp. 133–292, U23), and a pattern loose
  enough to catch `58+59` would link those too. Ranges point at their first
  member, the rule `linkify_xref` already uses.
- **The theme control lost its Auto state.** It toggles Light ↔ Dark, so the
  button always names a real palette. The system preference is still honoured —
  it is what a first visit resolves to, and nothing is written to storage until
  the reader presses the button, so an untouched control keeps following the OS.
- **The statistics line is back under the table title**, in the landing page's
  grey and a step larger (16px against `.c-stats`' 14px). That needed
  `--muted-fixed`: the real `--muted` captured at `:root`, because `body.chart`
  redefines `--muted` to `--ink` and a `var()` takes the value of the element it
  is declared on. `.imprint` is the only user, deliberately. Contrast measured
  **6.15:1 light, 6.73:1 dark**. The title block also drops to `--measure-wide`
  on table pages — it no longer holds a citation, and the line does not fit in a
  40rem measure at 16px.
- Measured after: column drift **0px at every generation** on both tables, no
  dangling `#` anchors in either footer, footer one column at 375px with no
  horizontal overflow, no console errors, build exit 0 with 6 JSON-LD blocks
  valid, structural self-checks pass on both tables.

## 2026-07-28 — toolbar splits left/right; the table title pages are cut back

- **Find goes hard left, Scale hard right**, spanning the plate bar. The push is
  an auto start-margin on `#scale-mount`, **not** `justify-content:space-between`
  — `#find` carries `[hidden]` until the script unhides it, so with
  space-between a reader without JavaScript would get the scale buttons stranded
  on the left of an otherwise empty bar. Verified in that state: with `#find`
  hidden the buttons still measure flush to the bar's right edge. On a phone the
  row wraps, find above and scale right-aligned below.
- **The table title pages lose the source citation and the statistics line.**
  `<div class="cite">` and `<p class="imprint">` are gone from Genealogy I and
  IV; a table page's title block is now the plate label, the numeral and the
  double rule. The landing page keeps its citation — the removal was scoped to
  the table pages.
- **The doi is untouched by that.** It was never in the title-page citation: it
  lives in `cite_html()`, the footer's *Citation* block, and in the JSON-LD
  `identifier`. Both table pages still carry it twice. Checked, because the
  title-page block and the footer block read alike and cutting the wrong one
  would have rotted every printed citation.
- The now-unused `.imprint` CSS and the `imprint` local were deleted rather than
  left dangling. `CITE` stays — the landing page still renders it.
- Measured after: column drift **0px at every generation** on both tables, find
  flush left and scale flush right to the bar's content box on both, build exit
  0 with 6 JSON-LD blocks valid, no console errors.

## 2026-07-28 — the key comes back off the page; the notation moves to the footer

Same day as the entry below, and it partly reverses it. Read the two together.

- **The on-page chart key was removed again, by decision, and its code deleted.**
  `key_html()`, the `.key`/`.key-d` CSS and the print overrides are gone rather
  than left unreferenced — keeping them uncalled last time is exactly what
  produced the "looks like a bug but isn't" note in `CLAUDE.md` that then had to
  be corrected twice. Recoverable from git if it is ever wanted back.
- **The three notations did not go with it.** `+` (spouse), `F.`/`M.` (sex) and
  the leader rule are now the first three items of the footer's **Navigating
  this chart** list, which is therefore the only place on the page they are
  decoded. `navigating_html()` says so in its docstring. This is the third time
  these three have moved; do not thin them out.
- **The plate caption lost its provenance sentence.** "Redrawn from the plate as
  printed; brackets, columns and leader rules reproduce the 1923 layout" is
  removed — the footer's editorial notes already make that claim. The caption now
  carries only the pan hint, so **`.plate-caption` is what hides above 1400px and
  in print**, not `.pan-hint`: hiding only the span left an empty figcaption
  holding its own bottom padding open. Measured 0px above the breakpoint and 0px
  under the print rules.
- **Footer order changed:** *Navigating this chart* moved up to sit directly
  under *The record*, ahead of *Editorial notes*, *Provenance* and *Citation*.
  How to read the thing now precedes the scholarly apparatus about it.
- **Glyph rendering on Windows and Android was verified on device** and is no
  longer an open question. Recorded under Facts worth knowing, with the cmap
  reasoning kept as the durable evidence.
- Measured after the change: column drift **0px at every generation** on both
  tables, no horizontal overflow at 375px, masthead still two rows, no console
  errors, build exit 0 with 6 JSON-LD blocks valid.
- **Audited but not changed** — recorded so the next session does not re-derive
  it. The page has four left edges at full width: masthead 8px, plate 59px,
  chrome (toolbar, caption, register) 115px, prose 371px. The plate and the
  chrome that controls it are 56px apart because the scroller is full-bleed
  while its chrome is capped at `--measure-wide`. Below ~1400px they converge,
  which is why it is easy to miss. Left alone deliberately this round.

## 2026-07-28 — the chart key returns, as a disclosure

- **The key is back and the open design thread is closed.** Since the
  always-visible band was removed earlier the same day, three notations had been
  explained nowhere on the page — `+` for a spouse, `F.`/`M.` for sex, and the
  leader rule. `key_html()` now renders a **closed `<details>`** between the
  title page and the plate bar: **34px collapsed** against the old band's
  ~100px, for material a reader decodes once. `key_html()` and the `.key` CSS
  are therefore **no longer unreferenced** — the note in `CLAUDE.md` saying so
  has been replaced.
- **Why `<details>` and not a popover:** the key has to work with JavaScript
  off. Nothing in the page script touches it — verified by grepping the shipped
  script, which references `details`/`summary` only in two pre-existing places,
  one of them the line-click guard that already excluded `summary` and so does
  not hijack the disclosure.
- **The key sits outside `.plate-tools`, deliberately.** The print rule hides
  that span; a key parked in the toolbar would have vanished from printed
  sheets, and the old band printed. `@media print` forces the disclosure open
  using **both** mechanisms — the legacy `summary~*{display:block}` and
  `::details-content` — because engines disagree. Measured in Chrome 148: with
  the disclosure closed, only `::details-content` fires (34px → 106px); the
  legacy selector alone was **inert**. Do not delete either one on the grounds
  that it looks redundant.
- **Chrome is `.register-d`'s**, so the site has one disclosure look, not two.
  The default triangle marker is kept rather than the landing page's `+`/`–`
  marker: `+` is chart notation for a spouse and the key explains it two lines
  below, which would have been a genuine collision.
- **The summary's padding is solved from `--tap`, not floored by it.** With the
  line-height pinned, `calc((var(--tap) - 1.4em) / 2)` makes the hit area
  measure exactly `--tap` at both pointer sizes with the label centred; a bare
  `min-block-size` cleared the floor but left the label sitting high on a coarse
  pointer. Measured 32px. The floor is kept as the guarantee.
- **Measured, not assumed:** column drift **0px at every generation** on both
  tables (I: 5 generations, IV: 4); no horizontal overflow at 375px with the key
  open, items wrapping to 7 rows; masthead still two rows; no console errors.
- The editorial-apparatus note now names the key alongside the generation ruler,
  the person numbers and the register — it is 2026 apparatus, not the plate.

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
