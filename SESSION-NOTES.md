# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-08-08**. The site moved twice, and **`5441abc` is now the
last commit to touch a built page**, superseding `778bfb9`.

**The second sort on Genealogy III is settled at all five instances, and every
one is published.** `ebd8738` (PR #34) took 156 and 157; `5441abc` (PR #35)
took 154, 228 and 242. They read `Yaʼdôkyʽ`, `Pʽĕʼnitsʼaʼyo`, `Dziotyʽ`,
`Awieʽ` and `Shipʼaʼpʽ` — all **U+02BD, MODIFIER LETTER REVERSED COMMA**.

What decided it, in one line each, so nobody re-derives it: the user
**photographed** the lines; measured at native resolution, every known U+02BC
sweeps its tail down-left and every questioned mark sweeps down-right; both
sorts are **top-heavy**, so it is a **mirror, not a rotation**, which is what
picks U+02BD over U+02BB; and 156 and 242 each carry **both sorts inside one
word**, so neither needs a control from another line. Full numbers are in
`CHANGELOG.md` and in `transcription_iii.py`'s docstring.

**Do not re-crop the scan.** The ten-pixel limit that closed this on 2026-07-31
is unchanged. A photograph is what moved it, not more magnification — and that
is now a durable rule in `CLAUDE.md`: *when a glyph question is stuck, ask for a
photograph before reaching for an institutional scan.*

**No reading question is open on any plate.**

---

## The open thread

> **`laguna-search` will not build until it is told about U+02BD.** This is the
> one concrete, unblocked piece of work, and it was created by this session's
> publish.
>
> Its **gate 3** (`gate_keys_are_folded` in `build.py`) **aborts the build**
> with *"add it to the FOLD map in src/search.js"* the moment it re-fetches a
> page containing `ʽ`. Verified by reading that code, not assumed. So the
> failure is **loud**, which is the good case.
>
> **Two edits, both in that repo, and the second is the one that would be
> missed:**
>
> 1. **`FOLD` in `src/search.js`** — add `"ʽ": ""`, exactly as this repo's four
>    `_FOLD` maps have it. `build.py` parses that literal out of `search.js`, so
>    the browser and the build cannot disagree; there is only one place to edit.
> 2. **`NAME_MARKS` in `build.py`** (line ~381, currently `"ʼ˙˚˘" "ᶦᵘᵃᵉ"`) —
>    add `ʽ` there too. `'ʽ'.isalpha()` is `True`, so without it the name-break
>    walk-back reads the mark as a **consonant**. In these five names `ʽ` is
>    always word-final or followed by a vowel, so **no seam actually looks
>    affected** — but that is luck, not design, and gate 5 only fires on
>    single-word names of 14+ characters, so the general failure is silent.
>    All five names here are 5–13 characters.
>
> **Then re-run it with `--refresh`.** The published pages moved, so the cached
> copy is stale — and its checks read `cache/` by default, so a run without the
> flag proves nothing. `python3 build.py --refresh`, then
> `python3 tools/validate.py`.
>
> **Expect the namesake gate to stay at three pairs.** Folding here did not
> change: 0 of 713 folded names moved and the colliding-fold counts held at
> 2 / 4 / 2 / 1. That was measured both times. But that tool folds
> *independently*, so confirm rather than assume.
>
> One constraint that outlives all of this: **`GOOGLE_SITE_VERIFICATION` must
> not be blanked.** Search Console ownership is how a removal request is filed,
> so blanking the tag destroys the only mechanism for taking a page out of
> results. Low exposure is a *second* reason to keep it, not a reason to drop
> it.

## Start here in a new chat

**Start the session in THIS directory, then type `resume`.**

```bash
cd "/Users/eli/My Drive/CLAUDE - GENEALOGY TABLES - CREATED BY FABLE/pueblogenealogy.github.io" && claude
```

**Even when the work is in `laguna-search`** — which, this time, it is. That
repo has **no `CLAUDE.md` and no `SessionStart` hook**; only a `launch.json`
entry lives here. Start a session there and you get no rules, no handoff
auto-load, and no `site` preview config. Editing the sibling directory from
here works fine.

| | here | `laguna-search` |
|---|---|---|
| `CLAUDE.md` | yes | **none** |
| `SessionStart` hook | yes | **none** |
| `launch.json` | `site` **and** `laguna-search` | tool only |

1. **`git switch main && git pull`.**
2. Read the top **two** entries of `CHANGELOG.md`, both **2026-08-08** — they
   are the U+02BD reading, first the three marks and then the two. Everything
   below them is settled history. The **fifth** entry down, *the edition stops
   advertising itself*, is the one that constrains what you may propose.
3. Read `CLAUDE.md` — **Exposure posture** and **Release policy** first. Both
   forbid things a cold start would otherwise propose as easy wins. Then
   **The one thing to get right** and **Design invariants**.
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
   still valid HTML. **The cache is stale right now**, since the pages moved
   twice today. Also in `CLAUDE.md`, since it recurs after every publish and
   this file does not survive.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and published
**2026-08-08**; on any later date the first rebuild shows a date-only diff. If
that is all it is, `git checkout -- docs/` rather than committing.

**The `SessionStart` hook cannot vouch for this file.** Its staleness test asks
whether `scripts/` or `docs/` moved *since the notes were committed* — so a
session that commits notes and a build together looks current regardless of what
the notes say. Both of today's publishes deliberately kept the record commit
**separate** from the build commit for exactly this reason. Read the summary
above on its own merits; the hook's silence is not evidence.

## State

**Nothing is half-finished here.** `main` is clean, no open PRs, no branches but
`main`. `laguna-search` is clean on its own `main` at `3e673bc` — but see *The
open thread*: it will not build against the current site until it is told about
U+02BD.

**`5441abc` is the last commit that moved a built page, and it is deployed and
verified** — all six pages SHA-256-identical to the committed `docs/`, all 200,
sitemap 5 `<loc>`, stale-identity 0. All five U+02BD readings are live (7 / 5 /
5 / 5 / 5 occurrences) with **zero** of any old reading, and both inlined faces
carry the glyph. `--public` was re-run while wrapping: exit 0, and `docs/`
**unchanged**, which is the font/pages sync check passing.

**A stale PR had turned into a revert, and it is now closed.** PR #33 held the
previous session's handoff branch. Its own commit had already reached `main`
inside PR #34's squash — PR #34 was branched from it — so #33 contributed
nothing and would have **deleted all five U+02BD readings** and reverted the
font subset if merged. Closed, not merged; branch deleted. The general shape is
worth recognising: **branching new work off an unmerged branch and squash-merging
the new work turns the old PR into a revert.** `gh pr list --state open` catches
it; `git diff origin/main origin/<branch>` settles it — read the *direction*,
since deletions mean the branch is behind `main`, not ahead.

**One correction to something said in-session.** It was reported mid-session
that `laguna-search` would merely "sort with the raw character in the key" until
`ʽ` was added. That was wrong in the reader's favour: its **gate 3 aborts the
build outright**. The open thread above has the verified behaviour.

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

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Teach `laguna-search` U+02BD, then `--refresh`** | ~15 min | **The open thread.** Two edits — `FOLD` in `src/search.js`, `NAME_MARKS` in `build.py` — then `build.py --refresh` and `tools/validate.py`. Gate 3 aborts until the first one is done |
| **Land `laguna-search` on the site** | Session-sized, **needs you first** | In tension with the exposure posture — it adds a page and a reason to be found. Raise that when asking |
| **Give `laguna-search` a remote** | ~5 min, **needs you** | It has none, so the whole tool exists in one working copy under Google Drive. Publishing that repo is a visibility decision — more pointed now |
| **II·182 / IV·69 — one woman or two?** | **needs you + the plates** | Both F., Sun, generation 4; nothing contradicts them and no relative of either is drawn on the other plate. Marked `?`, joined nowhere. The honest outcome may be *unresolvable* |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **Two split pairs have no gate** | Recorded, no action needed | `Kowaiʼd˙yuitsʼa` I·27 / III·66 and `Shauʼd˙yiyĕ` I·39 / II·225 fold one character apart, so the namesake gate never sees them. **Neither the `_FOLD` unification nor the U+02BD edit changed this.** In that tool's **ANALYSIS.md §1.3b**. **Don't loosen the namesake rule to edit distance to "fix" it** |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus. **Also parsed by `laguna-search`** — harmless there, but rerun its validator |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate. Genealogy III's `#note-crossref` states this. **`laguna-search` resolves them internally**, which is evidence it is doable but not a reason to change the plates |
| **AMNH Digital Library** | Slow, **needs you** | **No longer an outreach item, and no longer needed for the glyph question** — a photograph settled that. Handle `2246/158` is kept only as a fact about the source. `digitallibrary.amnh.org` 403s automated fetches; use a real browser |

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
  window.

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
  and a cache that must be refreshed deliberately.
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
  in all four. `ʽ` was added to all four this way.
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

- **The second sort on Genealogy III, at all five instances.** 154, 156, 157,
  228 and 242 read U+02BD, published `ebd8738` and `5441abc`. Photographed and
  measured; **do not re-open it on the strength of a crop of the scan.** 228 is
  the one with a stated caveat — no control in its own frame — and the caveat is
  recorded in the docstring rather than left as doubt.
- **De-indexing.** Struck by the user 2026-08-08.
- **Unifying the four `_FOLD` maps.** Done 2026-08-08, `ffc519b`. The rule that
  replaces it — *keep the four maps identical* — is in `CLAUDE.md`, not a task.
- **Wikidata, Zenodo and the release track**, all three. These are the ones a
  helpful cold start will try to reopen.
- **The `laguna-search` design pass, entirely.** Deployment was never part of it
  and remains a separate decision.
- **The custom domain.** Closed 2026-07-31 by the user.
- **Genealogy III, entirely** — including both editorial items.
- **Whether the plate can be drawn.** All 261 drawn, 0.000 px column drift.
- **173's `See Gen. I, 149`.** It is what the plate prints and it does not
  resolve.
- **Genealogy II's placement and glyph readings.** No remaining errors.
- **Glyph rendering on Windows and Android was checked on device.**
- **`subset_font.py` is run only when the data gains a NEW character.** The
  U+02BD edit needed it once, for 156 and 157; the second publish did **not**,
  and re-running would only have dirtied every page. The coverage check it ends
  with can be run directly against `docs/` without regenerating the font.
- **Pages lags a push by seconds, and that is not a failed deploy.** Poll;
  **never rebuild to "fix" a `DIFF`.**
- **The GitHub Pages build API misreports the deployed commit.** Verify by
  SHA-256; `/publish` Gate 6 does this.
- **`sips --cropOffset 0 0` centre-crops.** Use `1 1`.
- **PRs here are squash-merged, so `git branch --no-merged` reports merged work
  as unmerged.** Read the PR state, not the ancestry — and see *State* for the
  second face of this, where a stale open PR becomes a revert.
