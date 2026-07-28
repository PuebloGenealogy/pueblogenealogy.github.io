# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-28**.

---

## Start here in a new chat

1. Read `CLAUDE.md` — especially **Design invariants** and **The one thing to
   get right**. Both encode failures that already happened.
2. Read the top entry of `CHANGELOG.md` for what shipped last.
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

## State

Site live, archived, citable. Nothing is broken and nothing is half-finished:
`main` is clean, no open PRs, `docs/` is in sync with the renderer.

- Live: <https://pueblogenealogy.github.io/>
- DOI (concept): `10.5281/zenodo.21637900` → <https://zenodo.org/records/21637901>
- Published: Genealogy I and IV. Tables 2 and 3 await scans.

## The open design thread

**Redesign the chart key.** The old always-visible band was removed because it
cost ~100px above the plate and was reference material a reader needs once.
`key_html()` and the `.key` CSS are still in `make_chart.py`, unreferenced, as
the starting point.

What has to be true of the replacement:

- It must restore three notations currently explained nowhere on the page:
  `+` (spouse, on the line below), `F.`/`M.` (sex as printed), and the leader
  rule. The others survive in the footer apparatus.
- It should work **without JavaScript** — `<details>` does, a popover does not.
- The print rule hides `.plate-tools`. A key parked in the toolbar disappears
  from printed sheets unless it is forced open in `@media print`. The old key
  printed; losing that would be a silent regression.

Open question worth deciding first: should the key be permanently visible, or
opened on demand? It is decode-once material, which argues for on-demand.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Glyph check on Windows/Android | 5 min, needs a device | Font coverage already proven; only live rendering is unknown |
| Wikidata item | ~10 min | Payload already drafted and every ID verified; **not urgent** |
| Wikipedia external link | Slow | Propose on the *Elsie Clews Parsons* Talk page — a direct edit is a COI and gets reverted |
| Tables 2 and 3 | Blocked | Needs scans. Worth more than everything else here combined |
| Delete `prettyph3nom/laguna-genealogy` | 1 min | Empty, unrelated to v1. Needs `gh auth refresh -h github.com -s delete_repo` |

## Decisions already made — don't re-litigate

- **No custom domain** for now. The DOI is the durable citable identifier and
  resolves independently of the host. If this is revisited, decide it *before*
  seeding inbound links.
- **No colour-coding of sex, and no per-clan colours.** Both were built and
  reverted; the measurements are in `CHANGELOG.md`. Short version: colours that
  must each clear 4.5:1 on the same paper cannot differ enough from each other
  to be told apart, and both schemes collapsed under deuteranopia. All text on a
  table page is `--ink`.
- Publishing goes through `/publish`, whose last gate is *record it in
  `CHANGELOG.md`*. The 2026-07-28 session merged PRs directly and skipped that
  gate, which is why the changelog had to be backfilled. Use the skill.
