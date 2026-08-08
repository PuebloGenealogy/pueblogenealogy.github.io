# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-07**. Two things happened that day. First a short
housekeeping session: the `2026-08-03` notes branch was merged, a preview entry
was added for the search tool, and **every stale branch was deleted on both
sides**. Then the user reported apparent duplicates in `laguna-search`, and the
fix went in there. **Nothing on the site changed on either count** — the
edition is all four plates and is current, and `8cc4bee` is still the last
commit that moved a built page.

The **search tool is still the open thread**. It was built on **2026-08-03**,
outside this repo and not deployed, and in building it turned the published
markup into something another program reads.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md` — now **2026-08-07**.
3. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**. Also **The published markup is now an interface**,
   which gained a paragraph on 2026-08-07: correcting one diacritic here can
   stop `laguna-search`'s build, by design.
4. Preview: `preview_start`, config name `site`. **It will not necessarily be on
   4173** — if that port is held, the tool assigns another and tells you which;
   use the port it reports. **Don't call `preview_stop` when you finish** — the
   user may still be looking at it.
5. **For the search tool**, `preview_start` config name **`laguna-search`**,
   port 4180, serving its `dist/`. That entry is committed here but nothing
   here builds it — run `python3 build.py` in that repo first, and preview
   **`standalone.html`**, not `index.html`, or the browser will serve you a
   cached ES module and you will measure the previous build.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built on
**2026-07-31**; on any later date the first rebuild shows a date-only diff. If
that is all it is, `git checkout -- docs/` rather than committing. This was
done on 2026-08-03 and the diff was dates only.

## State

**Nothing is half-finished in this repo.** `main` is clean, no open PRs.
**`8cc4bee` is still the last commit that changed the site**; everything after
it is notes and changelog and touches no built page. `--public` was re-run on
2026-08-03: 6 pages, 104 / 275 / 261 / 73 drawn, all four `self_check()`s pass,
privacy gate clean on 6 pages, 10 JSON-LD blocks valid, and the only diff was
dates, which was reverted.

**Don't trust a tip hash in this file — run `git log --oneline -3` and
`git branch -a`.** A handoff cannot state the commit that contains it, and the
tool's own handoff twice sent a session to fast-forward from a branch that had
already been deleted. If `git branch` shows a `handoff-2026-08-07-*` branch, it
is redundant with `main` and safe to delete.

**`main` is the branch; the remote had no others as of the 2026-08-07 sweep.**
Everything else was merged and deleted;
`docs/` did not move, so the Pages redeploy served identical bytes. The one
functional change was a `.claude/launch.json` entry named **`laguna-search`**,
serving that tool's `dist/` on 4180 beside `site` on 4173 — inert if the
directory is absent, since nothing here builds it.

That sweep produced one durable finding, now in **`CLAUDE.md` → Environment**:
**PRs here are squash-merged, so `git branch --no-merged` reports merged work
as unmerged** — read the PR state, not the ancestry. Nothing was at risk; the
worked example and the two `push --delete` / prune mechanics are there.

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

**The new work is not in this repo.** See the open thread.

## The open thread

> **The next session is a layout and design pass on `laguna-search`, named by
> the user on 2026-08-07.** The work is **not in this repo** — it is
> `src/search.css` and `src/search.js` one level up. **Start by reading that
> tool's own `SESSION-NOTES.md` → *Next step — LAYOUT AND DESIGN***, which
> lists seven stylesheet rules that look like preferences and are not, the
> ES-module cache trap that has broken three verification passes, and the
> design questions genuinely open. Nothing here needs to change for it.

**`laguna-search` — phases 1, 2, 2b, 2c done; the next pass is design.** It
lives at
`../claude-random/Search by ChatGPT Sites - Claude Recreate/laguna-search/`,
one level up from this repo, and is **its own git repo** with its own README,
ANALYSIS.md and gates. **It is not deployed and is not wired into this site.**

What it is: a framework-free search over all four plates — 713 plate entries
resolved to **620 people** — built by fetching the four published
`genealogy-*/` pages and parsing them. No transcription module, no local data,
nothing written back. `python3 build.py` runs **six** gates; `python3
tools/validate.py` compares every field and every relation against
`scripts/transcription*.py` and they agree.

**Its `main` is at `fd51810`, clean, and is now its only branch.** It has no
remote, so nothing there has been or can be pushed.

**The counts in this file were two sessions stale until 2026-08-07** — they
said 634 people, five gates, 65 joins. Sessions have worked on that tool
without touching this repo, so its numbers drift here silently and are worth
re-reading from its own build output rather than trusted from this paragraph.

**Read its `ANALYSIS.md` before changing it.** It records what was wrong with
the ChatGPT prototype the user supplied, and three of those are the kind of
thing that gets reintroduced by someone being helpful:

- a **synthetic id** was being displayed as a plate number (`II · 1010`);
- **203 unnamed entries** were filtered out of the directory entirely;
- cross-plate identity was decided by **name + sex + clan**, which merges
  strangers in a pueblo where names repeat. It is now decided by **Parsons's
  own cross-references**, each one verified against the entry it lands on by
  name, sex and clan, because the printed numbers are displaced on three of the
  four plates. **79 people, 172 entries** — 65 of them Parsons's own joins and
  **14 the tool's**, added 2026-08-04, each labelled *NOT PRINTED* in the UI.

Three things it reports on every build and does **not** resolve, all of which
match what this edition already documents: II·199's `Gen. I, 43 (?)` (Parsons's
own question mark), II·208's `Gaaish` against `Gaaiʼd˙yuitsʼa`, III·173's
`Gen. I, 149`, plus a conflict where II·138 and II·139 both land on I·82 and
neither is merged.

**The joins it refuses are now marked too — 2026-08-07, `fd51810`.** The user
read the alphabetical list and reported *"I, 52 is the same as III, 250"*. The
data was right: I·52 is a boy of 4 and III·250 has a wife and three children in
the same fieldwork. But the refusal was **nowhere on the page**, so two
adjacent rows read as the tool repeating itself. A row now carries `≠ III · 250`
while closed, and the panel gives the verdict and its evidence.

**The gate is the part worth knowing about, not the three findings.**
`gate_namesakes_adjudicated` finds every unjoined pair sharing a folded name,
sex and clan and **fails closed both ways** — a pair with no verdict aborts the
build, a verdict naming no pair aborts it too. That matters *here*: a new pair
can appear without anyone touching that repo, because **this edition need only
correct a diacritic** for one to show up. It caught two things on its first
run — a pair the hand sweep missed on a **single plate** (II·83 / II·144), and
a verdict that had been written against III·222, which already carries
Parsons's own *Gen. II, 83*. Namesakes are now computed between **people**, not
entries.

One verdict is **open** and says so: II·182 / IV·69 agree on name, sex, clan and
generation with nothing to corroborate or contradict. It is marked `?`, not
`≠`. Do not "resolve" it from this file — settling it needs the plates.

**Two decisions are the user's, and neither is urgent:** whether the two-panel
layout is right, and whether this ever lands on the site. Landing it means a
`make_chart.py` page plus serving the index — a separate decision, not a
consequence of the tool existing.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Wikidata item** | ~5 min, **needs you** | Payload at `wikidata-quickstatements.txt` is **current for four tables and ready to run**, 19 ids verified live, still a `CREATE`. Only the OAuth-logged-in batch run is left. **Send the file, don't paste it** — the separators are tabs. Record the Q-number afterwards |
| **`laguna-search` design pass** | Session-sized | **The named next session.** Layout and design only, in that repo's `src/`. The two-panel question is **settled** — one panel won in phase 2, don't reopen it. Deployment is a separate decision and is **not** part of this |
| **II·182 / IV·69 — one woman or two?** | **needs you + the plates** | The one **open** namesake. Both F., Sun, generation 4; nothing contradicts them and no relative of either is drawn on the other plate, so name, sex and clan are the whole of the evidence. Marked `?` in the tool and joined nowhere. Only the plates can settle it — and if they do, it is a line in that tool's `NAMESAKES`, **not** a change to this edition |
| **Unify the four `_FOLD` maps** | ~4 lines, needs a decision | Only `transcription_ii.py` maps `ŏ` and `Ĭ`, so `fold()` leaves diacritics in the keys for III·101 and III·16 despite its docstring. **Affects nothing published** — `fold()` is unused in the build. Touches four otherwise-immutable files, so decide rather than drive by. In `CLAUDE.md`. **New 2026-08-07:** this is now the likeliest way to trip `laguna-search`'s namesake gate — folding is what decides a name collision, so budget for adjudicating a new pair there |
| **AMNH Digital Library** | Slow, **needs you** | Strong inbound link. Handle `2246/158` — `https://digitallibrary.amnh.org/handle/2246/158`. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser. **Also the only route to settling the turned-comma mark** |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus. **Now also parsed by `laguna-search`** — harmless there, but rerun its validator |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate. Genealogy III's `#note-crossref` states this. Making them links would be a new feature across all four plates. **`laguna-search` now resolves them internally**, which is evidence it is doable but not a reason to change the plates |
| **Cut the release** | **Not yet — see the policy** | Two of the four clauses met: all four plates published, editorial items on III closed. Still outstanding: `.zenodo.json` describes three plates, and the AMNH handle is absent from `related_identifiers`. **Publishing the site is not releasing it** |

## Decisions already made — don't re-litigate

**From this session (all about `laguna-search`, none about the site):**

- **The tool reads the published site, not the transcription modules.** The
  user chose this on 2026-08-03 after being shown the trade. The cost is one
  unrecoverable trailing period (`dotted()` is not injective) and a dependency
  on the register's markup; the gain is that provenance is exactly what the
  edition publishes. `tools/validate.py` proves the parse against the modules.
- **A person is not a plate entry.** 713 entries are 620 people. Entries are
  joined only where Parsons cross-references them, and only after the reference
  is confirmed by name, sex and clan. **Never on a name coincidence** — that is
  what the prototype did — and never by trusting a printed number. The
  fourteen joins the tool makes itself (2026-08-04) are the stated exception:
  each rests on **relatives matching by name on both plates**, not on the name
  alone, and each is labelled in the UI.
- **Refusing to merge is a claim, and is shown like one** (2026-08-07). Two
  people sharing a name, a sex and a clan get a mark on the closed row and a
  verdict in the panel. `distinct` and `open` never share a mark — letting an
  unsettled pair look settled is the prototype's error told backwards.
- **`build.py` decides, `search.js` renders.** The namesake note used to be
  computed in the browser from its own `twinKey`, a second implementation of
  the build's rule, and it was wrong in two ways the build is not. Don't
  reintroduce a client-side identity or namesake rule; the fold map is
  single-sourced for exactly this reason.
- **Merged entries are not flattened into one record.** Each plate's reading
  stands; the panel shows them side by side. The plates disagree, and that is
  data.
- **A calculated birth year is never shown as a recorded one.** 162 are
  arithmetic on a recorded age; 1 is printed on a plate. Separate fields,
  `c.` prefix, `est.` chip.
- **`fold()` is the edition's, not NFKD's.** NFKD keeps `ʼ` U+02BC (a modifier
  *letter*) and turns `ᶦ` into `ɪ`, not `i`. The prototype's version mis-folds
  27 of 510 named entries. The map now has exactly one copy, in `search.js`.
- **The nearest-clan match for a misprint is filtering only.** The site
  publishes `sic-ring` but not the reading behind it, so `Bager` is filed under
  Badger for the filter and still **displayed as Bager**. Reported every build.

**Still standing from earlier sessions:**

- **22's bracket runs 80, 82; 83 is 25's, and the plate's rule is over-drawn.**
  Footnoted at `#note-overdrawn`.
- **43's bracket carries two leaders**, hers to 124 and 45's to 126.
  `LEADER_ON_SPOUSE_ROW`.
- **The four `drawn_under` values are confirmed against the scan** — W23, W34,
  W36, W45.
- **III's three non-numeric misprints print as the plate sets them**, ringed in
  `--sic`, under `#note-misprint`.
- **Genealogy III needs no editorial attribution, anywhere.** The plate marks
  paternity itself.
- **III does NOT share Genealogy II's +1 displacement into Genealogy I.** Never
  carry `CROSS_REF_OFFSET` over. Stated on the published page.
- **`|` in a cross-reference is a typographic line break, never a change of
  subject.**
- **192 is `Kiwaʼdyuwi`, with no raised dot, and the plates disagree** with
  Genealogy II's 188. Verified at 25×. Don't "fix" it.
- **191 `Ramona` vs Genealogy II's `Ramona of Sant Ana` is not a divergence.**
- **152 and 153 are spelled differently at their two occurrences.**
- **`ORTHOGRAPHY_VERIFIED` is `True` and the pass is not to be redone.**
- **258 and 259 are each printed on two different people, and 256 and 257
  appear nowhere.** `DUPLICATE_PLATE_NUMBERS`, synthetic ids.
- **37 is female though the plate prints `M.`**

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **Publishing the site is not cutting a release.** Zenodo's webhook is on this
  repo; a GitHub release mints a permanent version doi that cannot be deleted.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. A **published** source is quoted and cited; an
  **unpublished** one is gestured at and never named. METHOD.md rule 4.

## Closed — do not re-raise

- **The custom domain. Closed by the user 2026-07-31: the edition stays on
  `pueblogenealogy.github.io` permanently.** Not deferred this time — decided.
  A domain is portable but survives only while someone renews it, and a lapsed
  one is re-registered rather than merely lost, which would point every seeded
  citation at a squatter. `github.io` cannot lapse. Full reasoning in
  `CLAUDE.md`; **don't re-derive it**, the obvious argument reaches the wrong
  answer. **The gate on seeding inbound links is lifted.**
- **Whether the search tool should use the ChatGPT prototype's data.** It never
  did. `person-data.ts` and `relationship-data.ts` were read as a shape
  reference and nothing more. The prototype folder is untouched and unused.
- **Genealogy III, entirely — including both editorial items.** Read, drawn,
  audited, verified, live, footnoted, and the footnote is deployed.
- **Pages lags a push by seconds, and that is not a failed deploy.** Poll;
  **never rebuild to "fix" a `DIFF`** — rebuilding changes the local hash you
  are comparing against and hides the recovery.
- **Whether the plate can be drawn.** All 261 drawn, 0.000 px column drift at
  every generation in both blocks.
- **173's `See Gen. I, 149`.** It is what the plate prints and it does not
  resolve. The person is Genealogy I's 49. Stated on the page.
- **Genealogy II's placement and glyph readings.** No remaining errors.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file; `/publish` Gate 6 does this.
- **A privacy sweep must assert the content is present.** Use `curl -sL` *and*
  assert something like `id="p116"` exists.
- **`sips --cropOffset 0 0` centre-crops.** Use `1 1`. In `CLAUDE.md`.
