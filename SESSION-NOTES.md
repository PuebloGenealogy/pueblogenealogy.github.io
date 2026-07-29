# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-28**, after a session that rebuilt the **person card**,
made the edition's **first editorial attribution**, and **closed a hole in the
privacy gate**.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. Read `CLAUDE.md` — **The one thing to get right** and **Design invariants**.
   Both encode failures that already happened.
2. Read the top of `CHANGELOG.md`, newest first. 2026-07-28 is long; stop when
   the entries stop mattering.
3. Preview: `preview_start`, config name `site`, serves `docs/` on
   `http://localhost:4173`.
4. Loop: edit `scripts/make_chart.py` → `python3 scripts/make_chart.py --public`
   → reload. **Never hand-edit `docs/`**; it is regenerated and your change is
   discarded silently.

**A rebuild on a new day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. If the diff is dates and nothing
else, `git checkout -- docs/` rather than committing: bumping `lastmod` tells
crawlers the pages changed when they did not.

**Three habits this project keeps re-learning:**

- **Measure, don't look.** Drift, contrast, row heights, bracket alignment —
  all of it has a number, and eyes have been wrong here before.
- **Grep the built file, not the rendered DOM.** A browser read happens after
  the page's script has run. That is how `Theme: Auto` survived a check that
  reported no "Auto" anywhere.
- **Read the staged diff before committing.** `/publish` Gate 4 caught a comment
  reading *"Clan is not colour-coded"* directly above the rule that had just
  colour-coded it. The build was green; only the diff showed it.

## State

**Nothing is half-finished.** `main` is clean, no open PRs, `docs/` in sync with
the renderer, every live page verified SHA-256-identical to its committed
version. Published seven times on 2026-07-28, once on 2026-07-29.

- Live: <https://pueblogenealogy.github.io/>
- DOI (concept): `10.5281/zenodo.21637900` → <https://zenodo.org/records/21637901>
- Published: Genealogy I and IV.

Two things changed character this session and a cold start should know before
touching anything:

- **The edition now asserts one thing the plate does not** — the paternity of
  83–85. It is marked, footnoted, and kept out of the chart. See
  `METHOD.md` → *Editorial attribution* for the four rules before adding another.
- **The privacy gate now reads prose, not just markup**, and sweeps every page
  in `docs/`. It **fails closed**. If a build stops complaining about
  vocabulary, that is the gate working — read the message, do not loosen it.

## The open thread

**Design work on other sections of the site.** Started on 2026-07-29 and still
open. Done so far: the card's relative rows enlarged to `--t-base`, the row
highlight made clearable, the ruler's identity chip given its own band, and the
plate bar moved onto the plate's rail. Not yet looked at with the same eye: the
register below the plate, the footer apparatus, the landing page.

Two things that session proved worth doing on any element the reader touches —
both defects were found by checking, not by looking:

- **Ask what clears it, not just what sets it.** The row highlight and the
  ruler chip were both "correct" until something else was on screen at the same
  time.
- **Check the phone.** Two of the four fixes were mobile-only or mobile-first
  (the card's stacked divider, the bar's wrapped second row).

Before touching the card again, read `CLAUDE.md`'s card paragraph in **Design
invariants**. Short version: the card is a *regrouped detached copy* of the
register entry, so any rule not scoped to `.pcard` silently reformats the
104-entry register. Verify after any card change — the register's relation links
must still compute `display:inline`, its entry titles 16px.

**Tables 2 and 3 are the largest item by far and are held back on purpose**
until the design settles, so that changes are made against two tables rather
than four. Worth saying if it comes up: that premise is only half right. The
design lives in one renderer, so edits do not scale with table count; what
doubles is the built output to re-verify and the diff to read. The decision is
the user's and it is not unreasonable — just not for the stated reason.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Confirm the 83 / 84 attribution** | Needs the user + the records | 85 is firmly pinned — born after 69's death. 83 and 84 rest on ages that do not cleanly reconcile with the external evidence. It is **published and citable now**, so this is the one open item with a correctness edge |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` while the register's own entry titles read `56.`. The cards lost that inconsistency; the register kept it. One line in `rel_link` — but it changes the apparatus, not just the card, which is why it was left |
| Wikidata item | ~10 min, **needs the user** | Payload ready at `wikidata-quickstatements.txt`, 18 ids verified. **Not urgent** |
| AMNH Digital Library | Slow, **needs the user** | Pays three ways: likely source of the missing plates, a strong inbound link, and the handle for `.zenodo.json`, whose `related_identifiers` is **absent entirely** |
| Tables 2 and 3 | Blocked on scans **and** on the design decision above | Worth more than everything else here combined |

**Do not cut a GitHub release** to mark a checkpoint: Zenodo's webhook mints a
new version doi from it. Everything since v1.0.0 is presentational plus one
apparatus attribution; no transcription data changed. Save the version doi for
when Table 2 or 3 lands.

## Decisions already made — don't re-litigate

- **A chart row's highlight is class-driven wherever the card script runs.**
  `.line:target` is dropped under `html[data-card]` and kept as the no-JS path.
  Re-enabling `:target` alongside `.is-selected` re-opens the bug it fixed: a
  hash outlives every click, so the row it lit could never be turned off and a
  second row lit beside it. See `CLAUDE.md` invariant 2.
- **The plate bar has no max-width, on purpose** — it aligns to the plate, not
  to the title block, whose box aligns with nothing visible. The user chose this
  over matching the centred statistics line, which would have needed anchor
  positioning or moving the stats line out of the title block.

- **The person card carries the number, never the annotation.** Both the
  misprint note and the cross-reference were removed from it: the chart row the
  reader opened the card *from* already prints them. One consequence, in case
  it is revisited — `xref_printed` prints a cross-reference only at a person's
  **first** occurrence, so 67's card opened from the misnumbered 68 line does
  not surface it outside the register.
- **A person-level misprint variant was built and rejected.** `Chart.sic` →
  `data-sic` → the note on every card of that person. It worked and was
  measured; it multiplied the redundancy. Take it from git (`c38d313^`).
- **A build timestamp was built and reverted.** A clock time on the "Last
  updated" line would make `docs/` differ on every rebuild, down to the minute,
  killing the within-a-day sync check. See `CHANGELOG.md`.
- **No per-clan colours, and no colour-coding of sex.** Both built and reverted;
  the sex pair measured 1.05:1, and a 13-clan palette collapsed to about one
  just-noticeable difference under deuteranopia. **`--clan` is not that decision
  re-opened** — one colour for the *field*, so two colours must be told apart
  rather than thirteen. Three colours on a table page are now not `--ink`:
  `--sic`, `--muted-fixed`, `--clan`. A fourth needs the same evidence.
- **No on-page chart key.** Built twice, removed twice. The notation lives in
  the footer's *Navigating this chart* list, whose first three items are the
  only place `+`, `F.`/`M.` and the leader rule are decoded.
- **The plate's misprint is reproduced, not corrected.** Table 1 prints **68**,
  ringed in `--sic`, linked to 67. If someone "fixes" it to 67, that is the bug.
- **Research evidence never enters the repo** — not a code comment, not a
  changelog entry, not this file. The gate protects `docs/` only. The
  git-ignored workbook is the place.
- **No custom domain** for now. The doi is the durable citable identifier and
  resolves independently of the host.
- **Publishing goes through `/publish`.** Its last gate is *record it in
  `CHANGELOG.md`*, and skipping the skill is how the changelog once fell behind.

## Closed — do not re-raise

- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device**; both render
  correctly. The cmap reasoning is in `CLAUDE.md` as the durable evidence.
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by comparing the live page's SHA-256 against the committed `docs/` file, never
  by reading the build API. This session did exactly that, seven times.
