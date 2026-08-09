# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-08**, and this header covers **two** sessions — read both
paragraphs. The site **has** moved: `ebd8738` (PR #34) is now the last commit to
touch a built page, superseding `778bfb9`.

**Photographs settled the second sort at ALL FIVE instances, and every one is
PUBLISHED.** `ebd8738` (PR #34) took 156 and 157; `5441abc` (PR #35) took 154,
228 and 242. They now read `Yaʼdôkyʽ`, `Pʽĕʼnitsʼaʼyo`, `Dziotyʽ`, `Awieʽ` and
`Shipʼaʼpʽ` — all U+02BD, MODIFIER LETTER REVERSED COMMA.

Measured at native resolution: every known U+02BC sweeps its tail down-left and
every questioned mark sweeps down-right; both sorts are top-heavy, so it is a
**mirror, not a rotation**, which is what picks U+02BD over U+02BB. 156 and 242
each carry both sorts **inside one word**. Full measurements are in
`CHANGELOG.md` and `transcription_iii.py`'s docstring — **don't re-derive them,
and don't re-crop the scan.** The ten-pixel limit that closed this on 2026-07-31
is unchanged; a photograph is what moved it, not more magnification.

**So there is no open thread, and no reading question is open on any plate.**
Everything left needs the user.

Two things carried over from the session before it, both still true:
**the four `_FOLD` maps were unified** (they had drifted; all four now hold the
union, byte-identical — `ʽ` has since been added to all four), and
**de-indexing was struck by the user, not decided** — nothing was edited, and
`robots.txt`, `sitemap.xml`, the JSON-LD and the absence of `noindex` all stay
as the build emits them. See *Decisions already made*.

Everything else left needs the user. That is stated plainly below rather than
dressed up as work.

**One mechanical note.** PR #34's squash also carried `b256e8a`, the previous
session's handoff-close commit, which had never reached `main` — its branch
looked merged because PR #32 had been squashed. Nothing was at risk; it is
recorded because a `resume` in this session reported that branch as holding
nothing unpublished, and that was wrong.

---

## Start here in a new chat

**Start the session in THIS directory, then type `resume`.**

```bash
cd "/Users/eli/My Drive/CLAUDE - GENEALOGY TABLES - CREATED BY FABLE/pueblogenealogy.github.io" && claude
```

**Even when the work is in `laguna-search`.** That repo has **no `CLAUDE.md`
and no `SessionStart` hook**; only a `launch.json` entry lives here. Start a
session there and you get no rules, no handoff auto-load, and no `site`
preview config. Editing the sibling directory from here works fine.

| | here | `laguna-search` |
|---|---|---|
| `CLAUDE.md` | yes | **none** |
| `SessionStart` hook | yes | **none** |
| `launch.json` | `site` **and** `laguna-search` | tool only |

1. **`git switch main && git pull`.**
2. Read the top **three** entries of `CHANGELOG.md` — all **2026-08-08**. The
   lowest of the three is the exposure change and is the substantial one.
3. Read `CLAUDE.md` — **Exposure posture** and **Release policy** first. Both
   were rewritten on 2026-08-08 and both now forbid things a cold start would
   otherwise propose as easy wins. Then **The one thing to get right** and
   **Design invariants**.
4. Preview: `preview_start`, config name `site`. **It will not necessarily be on
   4173** — if that port is held, the tool assigns another and tells you which.
   **Don't call `preview_stop` when you finish** — the user may still be looking.
5. **For the search tool**, `preview_start` config name **`laguna-search`**,
   port 4180, serving its `dist/`. Run `python3 build.py --inline` in that repo
   first and preview **`standalone.html`**, not `index.html`, or the browser
   serves a cached ES module and you measure the previous build. **`--inline` is
   not optional** — `standalone.html` is only written when it is passed.
6. **`build.py` reads `cache/`, not the live site, unless you pass `--refresh`.**
   It says which — `cached in cache/` against `re-fetched` — and that line is the
   only warning you get. Every gate then passes against **whatever the site
   looked like when the cache was written**, so a build run to check a deploy
   proves nothing without the flag. Nothing fails, because a stale cache is
   still valid HTML, and the cache is git-ignored in the *other* repo, so
   nothing here ever mentions it. Found 2026-08-08 against a five-day-stale
   cache. **After any publish here, the first run over there is `--refresh`.**
   Also in `CLAUDE.md`, since it recurs after every publish and this file does
   not survive.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and published
**2026-08-08**; on any later date the first rebuild shows a date-only diff. If
that is all it is, `git checkout -- docs/` rather than committing.

**The `SessionStart` hook cannot vouch for this file.** Its staleness test asks
whether `scripts/` or `docs/` moved *since the notes were committed* — so a
session that commits notes and a build together looks current regardless of what
the notes say. That happened on 2026-08-08 and had to be corrected in a
follow-up commit. Read the summary above on its own merits; the hook's silence
is not evidence. Recorded in `CLAUDE.md`.

## Waiting on the user — raise these, don't decide them

De-indexing used to be item 1 here. **It is closed**; do not re-add it.

1. **Whether `laguna-search` ever lands on the site.** Unblocked and still
   undecided. Work would be in **this** repo: a `make_chart.py` page plus
   serving the index. **Note this cuts against the exposure posture** — it adds
   a page and a reason to be found — so it is a bigger question than it was when
   it was first raised.
2. **II·182 / IV·69 — one woman or two?** The one namesake the plates do not
   settle. Marked `?` and joined nowhere. Only the scans can decide it, and if
   they do it is a line in that tool's `NAMESAKES`, **not** a change here.
3. **Confirm the 83 / 84 attribution on Genealogy I.** The oldest of these and
   the only one with a correctness edge, since it is published and citable.

## State

**Nothing is half-finished.** `main` is clean, no open PRs, no branches but
`main`. `laguna-search` is clean on its own `main`.

**`778bfb9` is the last commit that moved a built page, and it is deployed and
verified** — all six pages SHA-256-identical to the committed `docs/`, all 200,
sitemap 5 `<loc>`, stale-identity 0, and `zenodo|10.5281|doi.org` **0 on every
live page** while `id="p116"` is still present. Everything after it —
`01d176d`, `e2e5142`, `9666966`, `ffc519b` — touches documentation and the
transcription modules' fold maps only. `--public` was run **twice** this
session, before and after the `_FOLD` edit: 6 pages, 104 / 275 / 261 / 73 drawn,
privacy gate clean, 10 JSON-LD blocks valid, exit 0, **`docs/` byte-identical
both times**, dates included, because it was the same day as the publish.

**The `_FOLD` unification is complete and needs no follow-up anywhere.** All
four maps hash identical; all four `self_check()`s pass. The renderer never
calls `fold()`, so nothing published moved. **`laguna-search` needs no re-run
on account of it** — its namesake gate keys on folded names, and no fold key it
consumes changed. `ï` and `ˑ` (U+02D1) were deliberately left out of the union:
both occur only in Genealogy II `plate_note` prose quoting *withdrawn* readings,
and in no name on any plate.

**`laguna-search` is verified against the deployed pages and needs nothing until
they move again.** All seven gates, 713 entries → 620 people, 505 names with
break seams, 3 namesake pairs with II·182 / IV·69 still the one open
adjudication; the validator agrees on every field and relation but for II·50's
known unreversible period. The check is only worth anything with `--refresh` —
step 6 above. **Re-run it after the next publish, not before.**

**Two user-side actions were completed outside the repo** and are not loose
ends: the Zenodo deposit was deleted, and the GitHub↔Zenodo link severed. Both
dois now return **410 Gone** at a tombstone. **Do not go looking for webhook
access tokens to revoke** — they are Zenodo-internal and invisible by design;
`CLAUDE.md` says why, and an empty Applications page is the expected result.

**One durable risk, and it is not code.** `laguna-search` **has no remote**. Its
history exists in exactly one working copy, under Google Drive, whose sync
daemon is known to touch `.git` mid-write. Nothing has gone wrong. Raise it;
don't do it unasked, since publishing that repo is a visibility decision — and
under the current posture, more clearly so than before.

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

> **There isn't one.** This is not a hedge — it is the state. De-indexing was
> the last thing the user had left hanging, and they struck it. Everything
> remaining either **needs the user** (the three items above) or is recorded as
> deliberately-not-doing (below).
>
> **Do not manufacture one.** The temptation on a cold start is to pick the
> largest remaining table row and begin; two of the three open items are
> decisions the user has to make, and the third needs records nobody here has.
> **Ask which, or ask what they want to do.**
>
> If pressed for the item with the most at stake, it is **confirming the
> 83 / 84 attribution on Genealogy I** — it is published, citable, and the only
> open item with a correctness edge. It needs the user and the records; it is
> not startable alone.
>
> One constraint that outlives all of this: **`GOOGLE_SITE_VERIFICATION` must
> not be blanked.** Search Console ownership is how a removal request is filed,
> so blanking the tag destroys the only mechanism for taking a page out of
> results. Low exposure is a *second* reason to keep it, not a reason to drop
> it. The hard rule in `CLAUDE.md` is unchanged.

**`laguna-search` — phases 1, 2, 2b, 2c and the design pass are all done.** It
lives at
`../claude-random/Search by ChatGPT Sites - Claude Recreate/laguna-search/`,
one level up, and is **its own git repo** with its own README, ANALYSIS.md and
gates. **It is not deployed and is not wired into this site.**

What it is: a framework-free search over all four plates — 713 plate entries
resolved to **620 people** — built by fetching the four published
`genealogy-*/` pages and parsing them. `python3 build.py` runs **seven** gates;
`python3 tools/validate.py` compares every field and relation against
`scripts/transcription*.py`. Read its build output for current counts rather
than trusting a number here — **the counts in this file were two sessions stale
until 2026-08-07**, because sessions work on that tool without touching this
repo.

**Read its `ANALYSIS.md` before changing it.** It records what was wrong with
the ChatGPT prototype, and three of those get reintroduced by someone being
helpful: a **synthetic id** displayed as a plate number; **203 unnamed entries**
filtered out of the directory; and cross-plate identity decided by **name + sex
+ clan**, which merges strangers in a pueblo where names repeat.

**Its gates key on THIS repo's spelling** — both recorded in `CLAUDE.md` →
*The published markup is now an interface*:

- `gate_namesakes_adjudicated` fails until every unjoined pair sharing a folded
  name, sex and clan has a hand-written verdict. **Correcting one diacritic here
  can create a new pair.** Three today; one, II·182 / IV·69, is `?`. The
  `_FOLD` unification was expected to create a fourth and **did not** — but that
  was measured, not assumed, and the next name edit deserves the same check.
- **`gate_names_break_lawfully` (gate 5)** fails when a single-word name of 14+
  characters has no legal break seam. **A vowel character new to this edition**
  would do it. It only catches the long names; a shorter one loses its seams
  **silently**.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Land `laguna-search` on the site** | Session-sized, **needs you first** | In tension with the exposure posture — it adds a page and a reason to be found. Raise that when asking |
| **Give `laguna-search` a remote** | ~5 min, **needs you** | It has none, so the whole tool exists in one working copy under Google Drive. Publishing that repo is a visibility decision — more pointed now |
| **II·182 / IV·69 — one woman or two?** | **needs you + the plates** | Both F., Sun, generation 4; nothing contradicts them and no relative of either is drawn on the other plate. Marked `?`, joined nowhere. The honest outcome may be *unresolvable*, as the turned-comma mark was |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **Two split pairs have no gate** | Recorded, no action needed | `Kowaiʼd˙yuitsʼa` I·27 / III·66 and `Shauʼd˙yiyĕ` I·39 / II·225 fold one character apart, so the namesake gate never sees them. **The `_FOLD` unification did not change this** — neither pair's difference is one of the characters that moved. In that tool's **ANALYSIS.md §1.3b**. **Don't loosen the namesake rule to edit distance to "fix" it** |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus. **Also parsed by `laguna-search`** — harmless there, but rerun its validator |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate. Genealogy III's `#note-crossref` states this. **`laguna-search` resolves them internally**, which is evidence it is doable but not a reason to change the plates |
| **AMNH Digital Library** | Slow, **needs you** | **No longer an outreach item** — inbound links are off. Kept only because handle `2246/158` is **the only route to settling the turned-comma mark**, which needs a better scan. `digitallibrary.amnh.org` 403s automated fetches; use a real browser |

## Decisions already made — don't re-litigate

**Set by the user on 2026-08-08 — none of them provisional:**

- **De-indexing is CLOSED, and nothing was edited.** The user struck it as
  unimportant rather than choosing a level. `robots.txt`, `sitemap.xml`, the
  JSON-LD and the absence of `noindex` stay as the build emits them. **This is
  the one a cold start will re-derive**, because "the user wants low exposure"
  reads as an argument for `robots.txt`. It is not: not promoting the edition
  and taking it out of Google are different requests, and only the first was
  made. The mechanism is kept in `CLAUDE.md` — **`Disallow:` does not
  de-index**, and `noindex` needs crawling left *allowed* — so the closure is
  cheap to hold, not so it can be reopened.
- **No Wikidata item, ever.** The payload is deleted. It survives in git
  history, which is fine — bibliographic metadata only. **Do not reconstruct
  it**, and do not offer it as an easy win; it was the highest-return item on
  the old plan, which is exactly why it will be tempting to re-propose.
- **No inbound link is seeded without asking.** The gate the custom-domain
  closure once lifted is back and harder. Wikipedia's *Elsie Clews Parsons*
  external links and AMNH are **not** outreach targets.
- **No GitHub Release and no Zenodo deposit, ever, unless the user says
  otherwise.** The old policy's trigger was "all four tables final" — they *are*
  final, so a session reading only that sentence concludes the release is due.
  **The policy was replaced, not satisfied.**
- **A doi reappearing anywhere in this repo is a regression, not a
  restoration.** Both dois now 410.
- **Zenodo lets a record's OWNER delete it within 30 days of publishing.** The
  widely-repeated "published records are permanent" is true only *after* that
  window. That session asserted the wrong version first; the correction is in
  `CLAUDE.md` and `CHANGELOG.md`.

**Still standing from earlier sessions:**

- **The custom domain is closed.** The edition stays on
  `pueblogenealogy.github.io` permanently. Not deferred — decided. Full
  reasoning in `CLAUDE.md`; **don't re-derive it**, the obvious argument reaches
  the wrong answer.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. A **published** source is quoted and cited; an
  **unpublished** one is gestured at and never named. METHOD.md rule 4.
- **The tool reads the published site, not the transcription modules.** Chosen
  2026-08-03 after being shown the trade. Cost: one unrecoverable trailing
  period (`dotted()` is not injective), a dependency on the register's markup,
  and — as 2026-08-08 showed — a cache that must be refreshed deliberately.
- **A person is not a plate entry.** 713 entries are 620 people. Joined only
  where Parsons cross-references them, and only after the reference is confirmed
  by name, sex and clan. **Never on a name coincidence.**
- **Refusing to merge is a claim, and is shown like one.** `distinct` and `open`
  never share a mark.
- **`build.py` decides, `search.js` renders.** Don't reintroduce a client-side
  identity, namesake or break rule.
- **A phonetic name may break only immediately before a consonant, and only
  where walking back over the marks lands on a vowel.** **`y` is a consonant.**
  Two stronger glottal rules were put to the user and rejected on measured cost.
- **`.cell.name` carries no `overflow-wrap`, and that is a rule.**
- **Merged entries are not flattened into one record.** The plates disagree, and
  that is data.
- **A calculated birth year is never shown as a recorded one.**
- **`fold()` is the edition's, not NFKD's** — and as of 2026-08-08 the **same**
  map in all four modules. Keep them identical; a character new to a name goes
  in all four.
- **22's bracket runs 80, 82; 83 is 25's**, and the plate's rule is over-drawn.
- **43's bracket carries two leaders.** `LEADER_ON_SPOUSE_ROW`.
- **Genealogy III needs no editorial attribution, anywhere.** The plate marks
  paternity itself.
- **III does NOT share Genealogy II's +1 displacement into Genealogy I.**
- **192 is `Kiwaʼdyuwi`, with no raised dot, and the plates disagree.** Verified
  at 25×. Don't "fix" it.
- **`ORTHOGRAPHY_VERIFIED` is `True` and the pass is not to be redone.**
- **37 is female though the plate prints `M.`**

## Closed — do not re-raise

- **De-indexing.** Struck by the user 2026-08-08. Nothing to do, nothing
  pending, no level to choose.
- **Unifying the four `_FOLD` maps.** Done 2026-08-08, `ffc519b`. Two folds
  changed, no new collisions, `docs/` unmoved. The rule that replaces it —
  *keep the four maps identical* — is in `CLAUDE.md`, not a task.
- **Wikidata, Zenodo and the release track**, all three. See above. These are
  the ones a helpful cold start will try to reopen.
- **Re-running `laguna-search` against the doi removal.** Done 2026-08-08, both
  checks pass. It becomes live again only when the published pages next move —
  and then with `--refresh`.
- **The `laguna-search` design pass, entirely.** Opened 2026-08-07, closed
  2026-08-08. Deployment was never part of it and remains a separate decision.
- **The custom domain.** Closed 2026-07-31 by the user.
- **Genealogy III, entirely** — including both editorial items.
- **Whether the plate can be drawn.** All 261 drawn, 0.000 px column drift.
- **173's `See Gen. I, 149`.** It is what the plate prints and it does not
  resolve.
- **Genealogy II's placement and glyph readings.** No remaining errors.
- **Glyph rendering on Windows and Android was checked on device.**
- **Pages lags a push by seconds, and that is not a failed deploy.** Poll;
  **never rebuild to "fix" a `DIFF`.**
- **The GitHub Pages build API misreports the deployed commit.** Verify by
  SHA-256; `/publish` Gate 6 does this.
- **`sips --cropOffset 0 0` centre-crops.** Use `1 1`.
- **PRs here are squash-merged, so `git branch --no-merged` reports merged work
  as unmerged.** Read the PR state, not the ancestry.
