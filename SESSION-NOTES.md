# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-28**, after a session spent entirely on the **person
card** and the **printed line**.

---

## Start here in a new chat

You may already have this file in context — a `SessionStart` hook
(`.claude/hooks/session-start.sh`) loads it automatically and prefixes a
`STALE:` or `UNCOMMITTED WORK:` line when either applies. If those warnings are
present, believe them over anything written below.

1. Read `CLAUDE.md` — especially **Design invariants** and **The one thing to
   get right**. Both encode failures that already happened.
2. Read the top entries of `CHANGELOG.md`, newest first. 2026-07-28 is long;
   stop when the entries stop mattering.
3. Bring the preview up: `preview_start`, config name `site`, serves `docs/` on
   `http://localhost:4173`.
4. Loop: edit `scripts/make_chart.py` → `python3 scripts/make_chart.py --public`
   → reload. **Never hand-edit `docs/`** — it is regenerated and your change is
   discarded silently.

**A rebuild on a new day dirties `docs/` even with no code change**, because
`dateModified`, the visible "Last updated" line and the sitemap's `lastmod` all
carry today's date. So "rebuild produces no diff" is only a valid sync check
*within* a day. If the diff is dates and nothing else, discard it rather than
committing — bumping `lastmod` tells crawlers the pages changed when they did
not.

**Three habits this project keeps re-learning:**

- **Measure, don't look.** Column drift, contrast, row heights, bracket
  alignment — all of it has a number, and eyes have been wrong here before.
- **Grep the built file, not the rendered DOM.** A browser read happens after
  the page's script has run. That is how `Theme: Auto` survived a check that
  reported no "Auto" anywhere.
- **Read the staged diff before committing.** `/publish` Gate 4 caught a comment
  reading *"Clan is not colour-coded"* directly above the rule that had just
  colour-coded it. The build was green; only the diff showed it.

## State

Site live, archived, citable, and **fully published**. `main` is clean, no open
PRs, `docs/` in sync with the renderer, every live page verified SHA-256-
identical to its committed version.

- Live: <https://pueblogenealogy.github.io/>
- DOI (concept): `10.5281/zenodo.21637900` → <https://zenodo.org/records/21637901>
- Published: Genealogy I and IV. Tables 2 and 3 await scans.

**Five changes shipped on 2026-07-28**, all to how a person reads:

1. The person card no longer repeats the **misprint note** — the chart row it
   was opened from already carries it.
2. The card **sets its own format** instead of inheriting the register's:
   title at `--t-lg` underlined, indented `PARENTS:` / `SPOUSES:` /
   `CHILDREN:` rows, each person a rounded chip.
3. Chips carry the plate's **point after the number** — `56. Weʼdyumă`.
4. The card no longer repeats the **cross-reference** row either.
5. The **clan has its own colour** (`--clan`), and the number's point gained
   `.2em` of air on every printed line.

## The open thread

**There isn't one.** Nothing is half-finished. The next session is *choosing*.

The largest remaining item by a wide margin is **Tables 2 and 3**, blocked on
scans, not on work.

Two things to know before touching the card or the printed line again:

- **Everything card-specific is scoped to `.pcard` or done on the clone in
  `openCard`.** The card clones the register entry — one source of truth — so a
  rule written without that scope silently reformats the 104-entry register
  below the plate. Verify after any change: the register's relation links must
  still compute `display:inline` and its entry titles `16px`.
- **Chips are `.reg-rel > a`, direct children only.** A cross-reference row is
  *also* a `.reg-rel`, and its links sit inside an `<em>` of running prose. A
  descendant selector turns those into buttons mid-sentence. `openCard` now
  drops those rows from the card outright, so nothing should reach the rule —
  the `>` is what keeps it true if they ever come back.

## Pick up next — small, and genuinely open

| | Effort | Notes |
|---|---|---|
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` while the register's own *entry titles* read `56.`. The cards lost that inconsistency on 2026-07-28; the register still has it. One line in `rel_link` — but it changes the apparatus, not just the card, which is why it was left for a decision |
| Wikidata item | ~10 min, **needs the user** | Payload ready at `wikidata-quickstatements.txt`, all 18 ids verified live; creating the item needs a logged-in account. **Not urgent** |
| Wikipedia external link | Slow, **needs the user** | Propose on the *Elsie Clews Parsons* Talk page — a direct edit is a COI and gets reverted |
| Tables 2 and 3 | Blocked on scans | Worth more than everything else here combined |

## Decisions already made — don't re-litigate

- **No per-clan colours, and no colour-coding of sex.** Both built and reverted;
  measurements in `CHANGELOG.md`. The sex pair measured 1.05:1, and a 13-clan
  palette collapsed to about one just-noticeable difference under deuteranopia.
  **`--clan` is not this decision re-opened** — it gives the *field* one colour,
  so two colours must be told apart rather than thirteen, and they differ in
  lightness as well as hue. **Three** colours on a table page are now not
  `--ink`: `--sic`, `--muted-fixed`, `--clan`. A fourth needs the same evidence.
- **The person card carries the number, never the annotation.** Both the
  misprint note and the cross-reference were removed for one reason: the chart
  row the reader opened the card *from* already prints them. Note the one
  consequence, in case it is ever revisited — `xref_printed` prints a
  cross-reference only at a person's **first** occurrence, so opening 67's card
  from the misnumbered 68 line no longer surfaces it outside the register.
- **A person-level misprint variant was built and rejected.** `Chart.sic` →
  `data-sic` on the register entry → the note on *every* card of that person. It
  worked and was measured; the user judged it multiplied the redundancy. Take it
  from git (`c38d313^`) rather than rebuilding it.
- **No on-page chart key.** Built twice, removed twice. The notation lives in
  the footer's *Navigating this chart* list, whose first three items are the
  only place `+`, `F.`/`M.` and the leader rule are decoded.
- **The plate's misprint is reproduced, not corrected.** Table 1 prints **68**,
  as the plate has it, ringed in `--sic`, linked to 67. If someone "fixes" it
  back to 67, that is the bug.
- **No custom domain** for now. The doi is the durable citable identifier and
  resolves independently of the host. If revisited, decide it *before* seeding
  inbound links.
- **Publishing goes through `/publish`.** Its last gate is *record it in
  `CHANGELOG.md`*, and skipping the skill is how the changelog once fell behind.

## Closed — do not re-raise

- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device**; both render
  correctly. The cmap reasoning is in `CLAUDE.md` as the durable evidence.
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by comparing the live page's SHA-256 against the committed `docs/` file, not
  by reading the build API. This session did exactly that, five times.
