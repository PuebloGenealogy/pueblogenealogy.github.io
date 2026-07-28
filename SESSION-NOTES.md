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

**Closing out:** run `/wrap-session` before stopping. It backfills
`CHANGELOG.md`, rewrites this file, and re-checks `CLAUDE.md` for claims the
session falsified. It is not optional politeness — the 2026-07-28 session
merged five PRs without it and the changelog silently fell a day behind.

## State

Site live, archived, citable. Nothing is broken and nothing is half-finished:
`main` is clean, no open PRs, `docs/` in sync with the renderer.

- Live: <https://pueblogenealogy.github.io/>
- DOI (concept): `10.5281/zenodo.21637900` → <https://zenodo.org/records/21637901>
- Published: Genealogy I and IV. Tables 2 and 3 await scans.
- The chart key shipped 2026-07-28 as a closed `<details>` above the plate. The
  page explains its own notation again; nothing on the edition is half-built.

## The open thread

**There isn't one.** The key redesign — the thread every previous handoff
named — is done and live, so the next session is choosing rather than
continuing. Read that as a good state, not a missing note.

The largest remaining item by a wide margin is **Tables 2 and 3**, and it is
blocked on scans, not on work. Everything else below is small, optional, or
needs the user at a browser.

If the key is revisited, the two things that will look wrong and aren't are now
recorded in `CLAUDE.md` under Design invariants: it sits **outside**
`.plate-tools` because the print rule hides that span, and `@media print`
carries **two** overrides for forcing a closed `<details>` open because engines
disagree — in Chrome 148 only `::details-content` fires and the legacy selector
is inert. Deleting either as redundant silently drops the key from printed
sheets on some browser.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| Glyph check on Windows/Android | 5 min, needs a device | Font coverage already proven; only live rendering is unknown |
| Wikidata item | ~10 min | Payload ready at `wikidata-quickstatements.txt`, all 18 ids verified live; **not urgent** |
| Wikipedia external link | Slow | Propose on the *Elsie Clews Parsons* Talk page — a direct edit is a COI and gets reverted |
| Tables 2 and 3 | Blocked | Needs scans. Worth more than everything else here combined |
| Delete `prettyph3nom/laguna-genealogy` | 1 min, **needs the user** | Blocked on a token scope — see below |

## Carried over — blocked on the user, not on work

**Delete the empty repo `prettyph3nom/laguna-genealogy`.** Attempted
2026-07-28 and refused with `HTTP 403 … needs the "delete_repo" scope`. The
`gh` token holds `gist, read:org, repo, workflow` — GitHub gates repo deletion
behind a scope that has to be granted explicitly, and granting it is a browser
OAuth flow no agent can drive.

```bash
gh auth refresh -h github.com -s delete_repo   # opens a browser; user only
gh repo delete prettyph3nom/laguna-genealogy --yes
```

Or repo **Settings → Danger Zone → Delete this repository**.

Safe to delete, verified twice: 0 KB, 0 forks, 0 stars, 0 issues, no branches.
It is **not** the v1 repo — v1 was `laguna-genealogy-tables`, which 404s under
both owners and is genuinely gone. This is an unrelated empty repo whose only
cost is showing up beside the real one in lists like Zenodo's.

**Don't retry the delete before the scope is granted** — it will 403 again.
Ask, or skip it.

## Decisions already made — don't re-litigate

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
  difference under deuteranopia. All text on a table page is `--ink`.
- **Publishing goes through `/publish`.** Its last gate is *record it in
  `CHANGELOG.md`*, and skipping the skill is how the changelog fell behind.
- **The Wikidata item is optional.** The doi already put the edition into
  DataCite, and from there OpenAIRE and Google Dataset Search, which is the
  discovery infrastructure that matters. Wikidata adds a slow, modest signal.
  If it is done: paste `wikidata-quickstatements.txt` into
  <https://quickstatements.toolforge.org/> while logged in — creating the item
  needs a Wikidata account, so no agent can do it. The payload uses
  `P2093 author name string` rather than `P50 author` deliberately: P50 would
  require creating a biographical item about a living person, which carries its
  own notability bar and privacy questions. It links `P144 based on` to
  `Q51498010`, the 1923 article's existing item.
