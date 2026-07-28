# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-28**.

---

## Start here in a new chat

You may already have this file in context — a `SessionStart` hook
(`.claude/hooks/session-start.sh`) loads it automatically and prefixes a
`STALE:` or `UNCOMMITTED WORK:` line when either applies. If those warnings are
present, believe them over anything written below. If the hook did not fire,
nothing is lost; reading this file is the whole of it.

1. Read `CLAUDE.md` — especially **Design invariants** and **The one thing to
   get right**. Both encode failures that already happened.
2. Read the top entries of `CHANGELOG.md`. 2026-07-28 has six, because the day
   shipped six times; read them newest-first and stop when they stop mattering.
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

**Two habits this project keeps re-learning:**

- **Measure, don't look.** Column drift, contrast, row heights, bracket
  alignment — all of it has a number, and eyes have been wrong here before.
- **Grep the built file, not the rendered DOM.** A browser read happens after
  the page's script has run. That is exactly how `Theme: Auto` survived a check
  that reported no "Auto" anywhere.

**One practical note on the preview:** don't leave the browser viewport pinned
to an emulated size. Responsive checks are worth doing, but reset to native
afterwards — a viewport left at 1280×800 inside a larger window shows the user
a cropped page and reads as a broken site.

## State

Site live, archived, citable, and **fully published** — `main` is clean, no open
PRs, `docs/` in sync with the renderer, and every live page verified
SHA-256-identical to its committed version.

- Live: <https://pueblogenealogy.github.io/>
- DOI (concept): `10.5281/zenodo.21637900` → <https://zenodo.org/records/21637901>
- Published: Genealogy I and IV. Tables 2 and 3 await scans.

Nothing is half-finished. What a table page is now, after a day of cutting the
chrome back and then adding a little of it in again:

- **No on-page chart key.** The notation lives in the footer's *Navigating this
  chart* list — see the decision below.
- Title block is the plate label, the numeral, the double rule and the
  **statistics line**; no citation (the landing page keeps its own).
- Plate bar: **Find left, Scale right**. Theme control toggles **Light ↔ Dark**,
  no Auto.
- Plate caption carries only the pan hint, and hides above 1400px and in print.
- Footer apparatus is **two columns**, with every person reference linked.
- **Table 1's misprint prints as 68**, as the plate has it — ringed in `--sic`
  red, linked to person 67, with *(misprint, click here to see notes)* on its
  own row beneath. It had been silently corrected to 67. If someone "fixes" it
  back, that is the bug.

## The open thread

**There isn't one.** Every thread previous handoffs carried is closed: the chart
key (built, removed, notation relocated), the empty repo, the glyph check, and
the misprint fidelity error. The next session is **choosing**, not continuing.
Read that as a good state, not a missing note.

The largest remaining item by a wide margin is **Tables 2 and 3**, and it is
blocked on scans, not on work. Everything else below is small or optional.

Three things to know before touching the table-page chrome again:

- **`navigating_html()` is load-bearing.** Its first three list items are the
  only place on the page that `+`, `F.`/`M.` and the leader rule are decoded.
  They have already been lost once by a change that looked purely cosmetic.
- **Anything drawn on a `.line` must not take space.** Selection highlights and
  the misprint ring are `outline` and `box-shadow` only, drawn *outside* the
  border box — a border or padding moves the row and throws the sibling bracket
  off its `mother_row`. Adding a row is fine if it is counted (`row += 1`) and
  is exactly one `--lh` tall, as the misprint row and cross-reference rows are.
- **A measured audit is in `CHANGELOG.md` and was deliberately not acted on.**
  The page has four left edges at full width: masthead 8px, plate 59px, chrome
  115px, prose 371px. The plate sits 56px left of the toolbar that controls it,
  because the scroller is full-bleed while its chrome is capped at
  `--measure-wide`. Below ~1400px they converge. Don't re-measure it; decide.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Wikidata item | ~10 min, **needs the user** | Payload ready at `wikidata-quickstatements.txt`, all 18 ids verified live; creating the item needs a logged-in Wikidata account. **Not urgent** |
| Wikipedia external link | Slow, **needs the user** | Propose on the *Elsie Clews Parsons* Talk page — a direct edit is a COI and gets reverted |
| Tables 2 and 3 | Blocked on scans | Worth more than everything else here combined |

## Decisions already made — don't re-litigate

- **No on-page chart key.** Built twice, removed twice. It is decode-once
  material and the plate is what the reader came for; the notation belongs in
  the footer, where it is. The code is deleted, not parked — if it is ever
  wanted back, take it from git rather than leaving a third unreferenced copy.
- **The plate's misprint is reproduced, not corrected.** This is the edition's
  whole premise, and the chart had been quietly violating it. Declared as data
  in `PLATE_NUMBER_MISPRINTS`, annotated in the apparatus.
- **No custom domain** for now. `pueblogenealogy.github.io` is a GitHub
  subdomain, not an owned domain, and the doi is the durable citable identifier
  — it resolves independently of the host, which removed the strongest argument
  for buying one. If this is revisited, decide it *before* seeding inbound
  links, since those point permanently at whatever host is chosen.
- **No colour-coding of sex, and no per-clan colours.** Both were built and
  reverted; the measurements are in `CHANGELOG.md`. Short version: two colours
  that must each clear 4.5:1 on the same paper cannot differ enough from each
  other to be told apart — the sex pair measured 1.05:1 — and a 13-clan palette
  chosen by optimisation still collapsed to about one just-noticeable
  difference under deuteranopia. All text on a table page is `--ink`, with
  exactly two deliberate exceptions: `--muted-fixed` on the statistics line and
  `--sic` on the misprint annotation.
- **Publishing goes through `/publish`.** Its last gate is *record it in
  `CHANGELOG.md`*, and skipping the skill is how the changelog once fell behind.
- **The Wikidata item is optional.** The doi already put the edition into
  DataCite, and from there OpenAIRE and Google Dataset Search, which is the
  discovery infrastructure that matters. Wikidata adds a slow, modest signal.
  If it is done: paste `wikidata-quickstatements.txt` into
  <https://quickstatements.toolforge.org/> while logged in. The payload uses
  `P2093 author name string` rather than `P50 author` deliberately: P50 would
  require creating a biographical item about a living person, which carries its
  own notability bar and privacy questions. It links `P144 based on` to
  `Q51498010`, the 1923 article's existing item.

## Closed — do not re-raise

- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways. It had
  been carried in three handoffs.
- **Glyph rendering on Windows and Android was checked on device** and both
  render correctly. The cmap reasoning is kept in `CLAUDE.md` as the durable
  evidence.
- **The GitHub Pages build API misreports the deployed commit.** It labelled the
  `536c43a` build `b1f7b1c`. The served bytes were correct; only the metadata
  was wrong, and the decision was to leave it. Verify deploys by comparing the
  live page's SHA-256 against the committed `docs/` file, not by reading the
  build API.
