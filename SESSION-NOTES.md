# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-08**. The session did two things: merged the 2026-08-07
handoff (PR #27) and deleted its branch, and then **closed the `laguna-search`
design pass** — the name-break rule was ratified by the user, implemented,
measured and committed in that repo.

**Nothing on the site changed.** The edition is all four plates and is current;
**`8cc4bee` is still the last commit that moved a built page**. `--public` was
re-run as a check: 6 pages, 104 / 275 / 261 / 73 drawn, all four `self_check()`s
pass, privacy gate clean, 10 JSON-LD blocks valid, and the only diff was dates,
which was reverted.

**No design or editorial question is open in either repo.** See *State*.

---

## Start here in a new chat

**Start the session in THIS directory, then type `resume`.**

```bash
cd "/Users/eli/My Drive/CLAUDE - GENEALOGY TABLES - CREATED BY FABLE/pueblogenealogy.github.io" && claude
```

**Even when the work is in `laguna-search`.** That repo has **no `CLAUDE.md`
and no `SessionStart` hook**; only a `launch.json` entry lives here. Start a
session there and you get no rules, no handoff auto-load, and no `site`
preview config. Editing the sibling directory from here works fine and is what
the last three sessions did throughout.

| | here | `laguna-search` |
|---|---|---|
| `CLAUDE.md` | yes | **none** |
| `SessionStart` hook | yes | **none** |
| `launch.json` | `site` **and** `laguna-search` | tool only |

`resume` is a standing command defined in `CLAUDE.md`. It costs almost nothing
— the hook has already put this file in context — and it answers with the
up-next list and then **stops**, rather than starting work.

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md` — now **2026-08-08**.
3. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**. Also **The published markup is now an interface**,
   which gained a paragraph on 2026-08-08: there are now **two** gates in
   `laguna-search` that one edit here can trip, and the second one is half
   silent.
4. Preview: `preview_start`, config name `site`. **It will not necessarily be on
   4173** — if that port is held, the tool assigns another and tells you which;
   use the port it reports. **Don't call `preview_stop` when you finish** — the
   user may still be looking at it.
5. **For the search tool**, `preview_start` config name **`laguna-search`**,
   port 4180, serving its `dist/`. That entry is committed here but nothing
   here builds it — run `python3 build.py --inline` in that repo first, and
   preview **`standalone.html`**, not `index.html`, or the browser will serve
   you a cached ES module and you will measure the previous build. **`--inline`
   is not optional for that**: `standalone.html` is only written when it is
   passed, so a plain `build.py` leaves a stale one on disk.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built on
**2026-07-31**; on any later date the first rebuild shows a date-only diff. If
that is all it is, `git checkout -- docs/` rather than committing. Done again
on 2026-08-08 and the diff was dates only. To check it is *only* dates rather
than eyeballing it: normalise the dates out of the added and removed lines and
diff the two sets.

## Waiting on the user — raise these, don't decide them

Three things are blocked on a decision, not on effort. **One fewer than last
session**: the name-break rule was ratified 2026-08-08 and is closed.

1. **Whether `laguna-search` ever lands on the site.** This is now the live
   one. It was previously deferred behind "finish the design pass" — that pass
   is done, so nothing is in front of it any more. Landing it is work in
   **this** repo: a `make_chart.py` page plus serving the index. It is still a
   separate decision and **not** a consequence of the tool being finished.
2. **II·182 / IV·69 — one woman or two?** The one namesake the plates do not
   settle. Marked `?` and joined nowhere. Only the scans can decide it, and if
   they do it is a line in that tool's `NAMESAKES`, **not** a change here.
3. **Confirm the 83 / 84 attribution on Genealogy I.** The oldest of these and
   the only one with a correctness edge, since it is published and citable.

**Nothing here blocks anything else.** Every other item in the table can be
picked up without asking.

## State

**Nothing is half-finished, in either repo.** This one is clean on `main` with
no open PRs; `laguna-search` is clean on its `main` with the design pass
committed. No design question, editorial question or unreviewed change is
outstanding anywhere.

**`8cc4bee` is still the last commit that changed the site**; everything after
it is notes and changelog and touches no built page.

**Run `git log --oneline -3` and `git branch -a`. Don't trust a tip hash or a
branch name in this file.** A handoff cannot describe the commit that contains
it, and naming a working branch guarantees the sentence rots — that happened
three times across the two repos on 2026-08-07, once to the very paragraph
written to warn about it. This file names neither for this repo.

**One durable risk, and it is not code.** `laguna-search` **has no remote**.
Its history — now including the whole design pass — exists in exactly one
working copy, under Google Drive, whose sync daemon is already known to touch
`.git` mid-write. Nothing has gone wrong. But "it is committed" means less
there than it does here, and giving it a remote is a five-minute job nobody has
asked for. Raise it; don't do it unasked, since publishing that repo is a
visibility decision, not a backup decision.

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

> **There isn't one, and that is a real answer rather than a gap.** The thread
> that had been open since 2026-08-07 — long names wrapping in
> `laguna-search`'s name column — is closed: ratified, implemented, measured,
> committed.
>
> **The most likely next piece of work is the decision at the top of *Waiting
> on the user*: whether the search tool lands on the site.** If the answer is
> yes, the work is in **this** repo and not that one — a `make_chart.py` page
> plus serving the index — and it is the first thing in a long time that would
> move a built page. Read the **Release policy** in `CLAUDE.md` before
> starting: publishing the site is not cutting a release, and a new page does
> not change that.
>
> If the answer is no or not yet, pick from the table below. **Not the
> Wikidata batch — that was removed on 2026-08-08 and is not an option any
> more.** See *Exposure posture* in `CLAUDE.md`.

**`laguna-search` — phases 1, 2, 2b, 2c and the design pass are all done.** It
lives at
`../claude-random/Search by ChatGPT Sites - Claude Recreate/laguna-search/`,
one level up from this repo, and is **its own git repo** with its own README,
ANALYSIS.md and gates. **It is not deployed and is not wired into this site.**

What it is: a framework-free search over all four plates — 713 plate entries
resolved to **620 people** — built by fetching the four published
`genealogy-*/` pages and parsing them. No transcription module, no local data,
nothing written back. `python3 build.py` now runs **seven** gates; `python3
tools/validate.py` compares every field and every relation against
`scripts/transcription*.py` and they agree, but for the one irreducible
ambiguity (II·50's trailing period — `dotted()` is not injective).

**Its `main` carries the design pass as of 2026-08-08 and is its only branch.**
It has no remote, so nothing there has been or can be pushed. Read its build
output for current counts rather than trusting a number in this paragraph —
**the counts here were two sessions stale until 2026-08-07**, because sessions
work on that tool without touching this repo and its numbers drift here
silently.

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

**Its gates are the part worth knowing about, because two of them key on THIS
repo's spelling.** Both are recorded in `CLAUDE.md` → *The published markup is
now an interface*:

- `gate_namesakes_adjudicated` fails until every unjoined pair sharing a folded
  name, sex and clan has a hand-written verdict. **Correcting one diacritic
  here can create a new pair.** Three today; one, II·182 / IV·69, is `?` and
  says so.
- **`gate_names_break_lawfully` (gate 5, new 2026-08-08)** fails when a
  single-word name of 14+ characters has no legal break seam. **A vowel
  character new to this edition** would do it — that set is a literal, so an
  unknown character reads as a consonant and the seams vanish. It only catches
  the long names; a shorter one loses its seams **silently**.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| ~~Wikidata item~~ | **Removed 2026-08-08** | Deleted by the user's decision, payload and all. Not deferred — **don't re-propose it**, and don't reconstruct the file from git history. `CLAUDE.md` → *Exposure posture* |
| **Land `laguna-search` on the site** | Session-sized, **needs you first** | See *Waiting on the user* 1. Now unblocked by the design pass finishing, but still a decision. A `make_chart.py` page plus serving the index. Would be the first change to a built page since `8cc4bee` |
| **Give `laguna-search` a remote** | ~5 min, **needs you** | It has none, so the whole tool exists in one working copy under Google Drive. See *State*. Publishing that repo is a visibility decision, so ask rather than doing it |
| **Two split pairs have no gate** | Recorded, no action needed | `Kowaiʼd˙yuitsʼa` I·27 / III·66 and `Shauʼd˙yiyĕ` I·39 / II·225 fold one character apart, so the namesake gate never sees them. Correct for the reader — they sort apart and never look like duplicates — but they are unjoined judgements nothing checks. In that tool's **ANALYSIS.md §1.3b**. **Don't loosen the namesake rule to edit distance to "fix" it** |
| **II·182 / IV·69 — one woman or two?** | **needs you + the plates** | The one **open** namesake. Both F., Sun, generation 4; nothing contradicts them and no relative of either is drawn on the other plate, so name, sex and clan are the whole of the evidence. Marked `?` in the tool and joined nowhere. Only the plates can settle it — and if they do, it is a line in that tool's `NAMESAKES`, **not** a change to this edition. Note the honest outcome may be *unresolvable*, as the turned-comma mark was |
| **Unify the four `_FOLD` maps** | ~4 lines, needs a decision | Only `transcription_ii.py` maps `ŏ` and `Ĭ`, so `fold()` leaves diacritics in the keys for III·101 and III·16 despite its docstring. **Affects nothing published** — `fold()` is unused in the build. Touches four otherwise-immutable files, so decide rather than drive by. In `CLAUDE.md`. **This is the likeliest way to trip `laguna-search`'s namesake gate** — budget for adjudicating a new pair there |
| **AMNH Digital Library** | Slow, **needs you** | **No longer an outreach item** — inbound links are off, see `CLAUDE.md` → *Exposure posture*. Kept only because handle `2246/158` (`https://digitallibrary.amnh.org/handle/2246/158`) is **the only route to settling the turned-comma mark**, which needs a better scan than this one. The site 403s automated fetches; use a real browser |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus. **Also parsed by `laguna-search`** — harmless there, but rerun its validator |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate. Genealogy III's `#note-crossref` states this. Making them links would be a new feature across all four plates. **`laguna-search` now resolves them internally**, which is evidence it is doable but not a reason to change the plates |
| ~~Cut the release~~ | **Closed 2026-08-08** | No release is ever cut and no Zenodo deposit is ever made. The whole release track was withdrawn with the archive. `CLAUDE.md` → *Release policy*. **Don't re-propose it because all four plates are final** — that was the old policy's trigger and the old policy is gone |

## Decisions already made — don't re-litigate

**From this session (all about `laguna-search`, none about the site):**

- **A phonetic name may break only immediately before a consonant, and only
  where walking back over the marks `ʼ ˙ ˚ ˘ ᶦ ᵘ ᵃ ᵉ` lands on a vowel**
  (ratified 2026-08-08, `ANALYSIS.md` §4a). **`y` is a consonant** for this
  rule — it follows from the clusters `dy`, `d˙y`, `ty`, and reading it as a
  vowel deletes seams. Measured over all 448 names at the real cell width: at
  210px, 15 wrap, **0** begin a line with a mark, **0** overflow; clean from
  150px up; no name reaches three lines; longest run between seams is 9
  characters.
- **Two stronger glottal rules were put to the user and rejected on measured
  cost.** Forbidding a break in any name containing `ʼ` leaves **1 of 73** long
  names breakable. Forbidding a break immediately *after* one strips 45 of 215
  seams and leaves three names with none. **Neither is a fix for anything** —
  the drafted rule already forbids a line beginning with any mark, which was
  the actual objection. Don't re-derive these.
- **`.cell.name` carries no `overflow-wrap`, and that is a rule.** Any value
  hands the decision back to the browser and the `<wbr>` seams stop mattering.
  The two are a pair and were changed together.
- **Widening the name column, dropping Birth/Death into the panel at ≤1120px,
  and shrinking the name's type are all closed** as answers to wrapping
  (2026-08-07). The break rule replaced them.
- **Breaking at the glottal `ʼ` alone does not work**, though it looks right:
  four long names carry no usable one, and in the `…itsʼă`-final names it is
  second from last, leaving 15–17 characters on the first line.

**Still standing from earlier sessions:**

- **The tool reads the published site, not the transcription modules.** The
  user chose this on 2026-08-03 after being shown the trade. The cost is one
  unrecoverable trailing period (`dotted()` is not injective) and a dependency
  on the register's markup; the gain is that provenance is exactly what the
  edition publishes. `tools/validate.py` proves the parse against the modules.
- **A person is not a plate entry.** 713 entries are 620 people. Entries are
  joined only where Parsons cross-references them, and only after the reference
  is confirmed by name, sex and clan. **Never on a name coincidence** — that is
  what the prototype did — and never by trusting a printed number. The
  fourteen joins the tool makes itself are the stated exception: each rests on
  **relatives matching by name on both plates**, and each is labelled in the UI.
- **Refusing to merge is a claim, and is shown like one.** Two people sharing a
  name, a sex and a clan get a mark on the closed row and a verdict in the
  panel. `distinct` and `open` never share a mark — letting an unsettled pair
  look settled is the prototype's error told backwards.
- **`build.py` decides, `search.js` renders.** True of namesakes and now of
  break seams. Don't reintroduce a client-side identity, namesake or break
  rule; the fold map is single-sourced for exactly this reason.
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

- **No release is ever cut, and the edition carries no doi.** Zenodo was
  withdrawn on 2026-08-08: the deposit **deleted** by the user (inside Zenodo's
  30-day owner window), the webhook removed, the GitHub link severed. Both dois
  return **410 Gone**. **A doi reappearing in this repo is a regression** — and
  now also an unresolvable link. `CLAUDE.md` → *Release policy* and *Exposure
  posture*.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. A **published** source is quoted and cited; an
  **unpublished** one is gestured at and never named. METHOD.md rule 4.

## Closed — do not re-raise

- **The `laguna-search` design pass, entirely.** Opened 2026-08-07, closed
  2026-08-08. The name column's long-name wrapping is fixed by the break rule
  above — ratified by the user, implemented, measured at seven widths, and
  committed. **The two-panel question was settled in phase 2** (one panel won).
  Deployment was never part of this pass and is a separate decision, listed
  above as open.
- **The custom domain. Closed by the user 2026-07-31: the edition stays on
  `pueblogenealogy.github.io` permanently.** Not deferred — decided. A domain
  is portable but survives only while someone renews it, and a lapsed one is
  re-registered rather than merely lost, which would point every seeded
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
- **PRs here are squash-merged, so `git branch --no-merged` reports merged work
  as unmerged.** Read the PR state, not the ancestry. In `CLAUDE.md`.
