# Laguna Genealogies — project context

A digital edition of the genealogical plates published with Elsie Clews Parsons,
**"Laguna Genealogies"**, *Anthropological Papers of the American Museum of
Natural History*, vol. 19, pt. 5 (1923), pp. 133–292.

**Live:** https://pueblogenealogy.github.io/ · **Repo:**
`PuebloGenealogy/pueblogenealogy.github.io` (public) · Pages from `main` /
`/docs`, HTTPS enforced.

Published, **all four plates, 713 individuals** (Genealogy III published
2026-07-31, `b06eb10`):
**Genealogy I** (Table 1) — 104 individuals, 27 marriages, 80 parent–child
links, 5 generations. **Genealogy II** (Table 2) — 275 individuals for the
plate's 274 numbers, 61 marriages, 214 parent–child links, **6 generations**,
three descent blocks. **Genealogy III** (Table 3) — 261 individuals, 72
marriages, 192 parent–child links, **7 generations**, two descent blocks, the
second indented. **Genealogy IV** (Table 4) — 73 individuals, 14 marriages,
58 parent–child links, 4 generations. `--public` builds **7 pages** and the live
site serves all of them; `PENDING` is empty. The seventh is **`/search/`**, added
2026-08-09 — not a plate, and the reason several counts here are 7 against a
sitemap of 5. See *The search page is vendored, not generated here*.

**The edition is now the whole of the genealogical material Parsons published**,
which changes what a stale scope claim costs: any sentence saying a plate is "in
preparation" or "not yet transcribed" is now simply false, and three such
sentences were live until 2026-07-31 — the landing-page FAQ, Genealogy II's note
on 160 and 163, and the README's plate table. There is no build gate for this.
Grep for it after any change to the edition's scope.

**Grep the plate numerals too, not only the hedging vocabulary.** A **fourth**
sentence survived that sweep the same day and was found only on 2026-07-31, in
`SITE_DESCRIPTION`: "Genealogies I and IV transcribed character by character".
It names its scope *positively*, so it contained none of the words a
"not yet"/"in preparation" grep looks for while being just as wrong — and it was
the most exposed sentence on the site, since that one constant renders **four
times on `/`**: the meta description, `og:description`, `twitter:description`
and the `CollectionPage` JSON-LD `description`. So sweep for `Genealog(y|ies) I`,
`II`, `III`, `IV` and "three" as well.


> **Note (2026-08-23):** this file was split twice today to stay under Claude Code's 150k-character memory limit. The first split moved five sections verbatim into `memory/*.md`, still fully `@import`ed. The second distilled those five files into four always-loaded `memory/*.md` files (durable rules only); moved two subsystems' worth of path-scoped content into `.claude/rules/`, which Claude Code loads automatically only when a file under its `paths:` is read; and moved narrative/historical content into on-demand `reference/`, which nothing loads automatically under the current configuration. No content was deleted — everything moved to one of these three places. See `CHANGELOG.md` for the detail and the measured before/after, and *Specialized references* below for what lives where now.

## Questions about how this project works are not API questions

**This repo contains no LLM/API code and never calls a model.** So *model*,
*instance*, *session*, *context*, *tokens*, *prompt* and *rules*, used here,
mean **this project's own workflow** — the handoff, `resume`, the `SessionStart`
hook, `/publish`, `/wrap-session`, `CLAUDE.md` itself.

- **Answer them directly** from `CLAUDE.md` and `SESSION-NOTES.md`.
- **Do not load an API or SDK reference skill for them.** There is no Anthropic
  API usage in this repo to reason about; a question like *"does a new model
  instance obey rules"* is about the handoff, not about `claude-*` model ids.
- **Never paste a skill's description, trigger text, or any other routing
  metadata into a reply.** It is internal plumbing, not an answer. If a skill is
  relevant, invoke it; if it is not, ignore it silently. Echoing it is always
  wrong — this happened on 2026-07-30 and is what prompted this rule.

## When the user says "resume"

**Standing command. Answer with the up-next list — cheaply.** `resume` is the
first turn of a fresh session, so every token spent here is taken from the work
itself. Treat this as a budget, not a summary.

### Spend almost nothing getting the answer

**The `SessionStart` hook has already put the whole of `SESSION-NOTES.md` in
context.** It is there before you act.

- **Do not re-read `SESSION-NOTES.md`.** Reading it back is the single most
  expensive mistake available on this turn, and it buys nothing.
- **Do not read** `CHANGELOG.md`, `METHOD.md`, `README.md`, or any
  `scripts/*.py`. None is needed to list what is next.
- **Do not run the build, the self-checks, or `curl`.** The handoff already
  records the last verified state, and nothing has changed since.
- **One tool call, at most**, and only if the hook printed no warning:
  `git status --porcelain && git branch --show-current`. Combine, never split.
- If the hook printed `STALE:` or `UNCOMMITTED WORK:`, **that is your answer**
  for part 1 — it outranks anything the handoff claims. Investigate only if the
  user asks.

### Reply — four parts, hard caps

1. **Where we are** — **one line.** Branch, clean/dirty, anything unmerged.
2. **Up next** — a **bullet list, one line each, most likely first**, from the
   handoff's *open thread* and *Other things that could be picked up*. Effort in
   two or three words; add **needs you** where it applies, since that saves a
   wasted turn. **Never more than one line per item.**

   **Every item in that table appears, every time.** The list is something the
   user returns to until the items are done, so an omission reads as "finished"
   when it is not. An item that is **deferred** is **marked**, never dropped —
   *Custom domain* went missing this way on 2026-07-30 while it was still open.
   An item the user has **closed** is a different case: it leaves the table
   altogether and moves to the handoff's *Closed — do not re-raise*, and it must
   **not** be listed. *Custom domain* was closed on 2026-07-31 and is now such an
   item; re-listing it as pending would invite a settled decision to be re-taken.
3. **Before you start** — **at most three bullets**, and only for the **first**
   item. Choose them by **consequence, not by order in the file**: the ones
   whose failure is expensive and irreversible outrank procedural ones. For
   Genealogy III, *don't register it in `TABLES` until `self_check()` passes*
   publishes a partial plate if ignored, and outranks *read `/transcribe-plate`*.
4. **Don't re-open** — **one line** naming what is settled, so its absence from
   the list reads as a choice.

**Summarise; never embellish.** Every number, count and attribution must come
from the handoff. Do not reach into `CLAUDE.md` or memory for a supporting
detail the handoff did not give, and do not attribute a measurement to the user
unless the handoff says they made it. On 2026-07-30 a `resume` reported that the
user had "verified all 24 brackets" of Genealogy II — the handoff said only that
they reported no remaining errors, and the 24 was **Table 1's** child-group
count, borrowed from an unrelated paragraph. **If the handoff is vague, be
vague.**

### Then stop

**Do not begin work on the first item.** `resume` asks for the list, not the
work. Do not restate decisions, do not explain the project, do not offer to do
several things at once, and **do not ask a clarifying question** — the list is
the question.

No preamble, no closing summary, no table where bullets will do. The detail
already lives in `SESSION-NOTES.md`; the user can ask for any of it, and asking
is cheaper than pre-loading it.

## Start here

1. **`docs/` is generated.** All design, copy and markup live in
   `scripts/make_chart.py` (~2,600 lines). Editing `docs/` is discarded silently
   on the next build.
2. **The edition publishes the 1923 transcription only** — never research
   columns. See below; this is the thing that must not go wrong.
3. **`SESSION-NOTES.md` is where the last session stopped** — read it first.
   It names the open thread, what is unresolved, and which files were last
   touched. Rolling, not a history; `/wrap-session` overwrites it.
4. `CHANGELOG.md` has the history. Read it instead of asking what changed.

### Which file owns what

Keep to this, or the two files drift into two changelogs:

| | Holds | Lifetime |
|---|---|---|
| **`CLAUDE.md`** (this file) | Permanent rules, conventions, invariants, and the privacy boundary | Durable. Loaded automatically on every session |
| **`SESSION-NOTES.md`** | Current progress, unresolved questions, recently edited files, next steps | Overwritten every session by `/wrap-session` |
| **`CHANGELOG.md`** | What changed and why, including work reverted | Append-only history |

**Anything permanent goes here, not in `SESSION-NOTES.md`** — that file is
designed to be thrown away, so a rule kept only there will eventually be lost.
It has happened: the illegible-passage rule below lived only in the handoff until
2026-07-29. `SESSION-NOTES.md` should **point** at this file rather than restate
it; a small number of deliberate duplicates is fine where losing the instruction
would be costly, and each one says it is a duplicate.

**Claude's external memory** (`~/.claude/projects/…/memory/`) is a convenience,
not a location. It is outside the repo, invisible to collaborators, and not
guaranteed to be surfaced. **No instruction may live there alone.** Anything
written there that matters is also written into one of the three files above.

---

## The one thing to get right

**No English names, no census matches, ever.** Some people identifiable through
that research have living descendants, the repo is public, and git history is
permanent — a leak cannot be undone by a later commit.

Enforced structurally, and must stay that way:

- Research columns live in `data/parsons_genealogy_I.xlsx`, which is git-ignored
- The public build reads `scripts/transcription*.py`, which have no research
  columns to read — there is no code path from workbook to `docs/`
- `make_chart.py --public` inspects its own output and **deletes the file**
  rather than write one. It checks two things — see `leak_report()`:
  - **markup**: `class="eng"` / `class="census"`
  - **prose**: the vocabulary research is written in (`census`, `familysearch`,
    `national archives`, `widow…`, `enumerat…`, …). Added 2026-07-28, because
    the markup grep was blind to the way research would actually escape — a
    footnote explaining *why* a reading was made carries no class at all.
    `<style>` blocks are excluded (the stylesheet ships `.census{}` rules);
    scripts are not. It **fails closed**: reword an allowlisted phrase and the
    build stops until the new wording is allowlisted. `RESEARCH_PROSE_ALLOWED`
    holds **three kinds** of entry, and the distinctions matter — three FAQ
    sentences that *state* the privacy boundary; (added 2026-07-30) one
    quotation from **Parsons's own 1923 text**, in Genealogy II's
    `note-paternity`, where her word "widow" is the source speaking and not
    research escaping; and (added 2026-08-09) one sentence from the **vendored
    search page**, stating the same boundary in that project's words. The third
    is copied **verbatim from `laguna-search`'s own allowlist**, and the two
    lists must stay in step: it runs this same gate over everything it writes,
    so a phrase either project rewords stops one build or the other.
    **Allowlist the exact phrase; never loosen the
    pattern** — and keep the phrase off a source-line break, since the check is
    an exact substring replace against the rendered HTML
- `check_published_pages()` sweeps **every** `.html` in `docs/`. The per-table
  check only ever saw table pages, so the landing page — the one carrying the
  FAQ — went unchecked entirely until 2026-07-28.
  **`.html` is the whole of it, and since 2026-08-09 that is a real gap rather
  than a tidy scope.** `docs/search/` ships a 61 KB `search.js` and a 307 KB
  `search-index.json` that this sweep never opens. Both are clean — checked by
  hand at publish — but nothing re-checks them on a later build. Run
  `leak_report()` over them by hand whenever `vendor/search/` is re-vendored.
  Note the third allowlist entry above exists **because of this gap, not
  despite it**: the sentence it covers lives in `search.js` today, so deleting
  the entry changes nothing until the day that script is inlined. Do not delete
  it on the evidence that it does nothing

The gate protects `docs/` only. It cannot see a code comment, a changelog entry
or a handoff note, and all of those are committed and public. Research evidence
goes in the git-ignored workbook and nowhere else in the repo.

Before committing new material, confirm `git status` lists no `.xlsx` and
nothing under `build/` or `data/`. `/publish` runs this gate.

**Illegible passages: the user supplies the reading, and it is used as given** —
no footer note, no chart marker, no hedge in the apparatus. The reason for the
reading goes in `plate_note`, which is inert in the renderer (read once, only to
test for `"braced"`). **If a reading came from the census research, its source
must not be named anywhere in the repo** — not in `plate_note`, not in a commit
message, not in a changelog entry. Say that a reading rests on evidence outside
the plate and stop there. This rule lived only in `SESSION-NOTES.md` until
2026-07-29, which is a file designed to be overwritten; it is permanent, so it
belongs here.

## Hard rules

| Never | Why |
|---|---|
| **Hand-edit anything in `docs/`** | Generated; overwritten every build. Edit `make_chart.py` |
| Blank `GOOGLE_SITE_VERIFICATION` | The tag is emitted by the build; blanking it lapses Search Console ownership |
| Re-run `scripts/build_workbook.py` | Overwrites the workbook, discarding research columns |
| Run OCR on a plate | Drops the diacritics and discards the bracket geometry |
| "Correct" a misprint in the data | The edition reproduces the plate; misprints are annotated, not fixed |
| Alter names, diacritics, numbering, clans or cross-references | Accuracy is the whole point |

## Commands

```bash
python3 scripts/transcription.py          # structural self-check, Table 1
python3 scripts/transcription_ii.py       # structural self-check, Table 2
python3 scripts/transcription_iii.py      # structural self-check, Table 3
python3 scripts/transcription_iv.py       # structural self-check, Table 4
python3 scripts/subset_font.py            # only when the data gains new characters
python3 scripts/make_chart.py --public    # the published build -> docs/
```

`--public` must end `N JSON-LD blocks valid` and **exit 0**. It exits 1 on
invalid structured data, a research-data leak, **any person in `PERSONS` that
the page does not draw**, or an incomplete `vendor/search/` (added 2026-08-09 —
METHOD.md describes `/search/` in the present tense, so a build that silently
omitted it would ship a document describing a 404). That last gate was added 2026-07-30: an undrawn person
used to be a console warning and a status line, which is how seven of Genealogy
II's went unnoticed for a whole session — nothing fails, the page just quietly
holds fewer people than the plate. The private build still only warns, because a
half-read plate legitimately has people no bracket reaches yet. `make_chart.py` with no flag is
the private build; it needs `data/*.xlsx`, which is not in this clone.

**That order is not cosmetic. `subset_font.py` runs BEFORE the build, or not at
all** — it is **not deterministic** (fontTools writes a fresh `head.modified` on
every run) and `make_chart.py` base64-inlines the woff2 into every page. Run it
after, and the pages carry the base64 of a font that is no longer on disk.
Nothing fails; the two simply disagree, and the next "does a rebuild produce a
diff?" check answers misleadingly. For the same reason **never re-run it to see
whether anything changed** — it dirties every page — read its coverage report,
which names each plate's new characters, or `none`.

The coupling runs backwards too, and that is the half that gets missed:
**throwing away a trial build means reverting `docs/` and the font together.**
Revert only `docs/` and the pages carry the base64 of the old font while a new
one sits on disk; revert only the font and it is the reverse. Same silent
disagreement, same misleading sync check. Found 2026-07-31, previewing
Genealogy III.

It ends by holding the subset against the **built pages**, and that check is the
one that matters: it reads `docs/` and demands every character in it be in the
font. Reasoning from the data about what *ought* to render is how `†` and `›`
stayed missing from every published page since launch — both are set from the
page's own script, so they appear in no template string anyone would scan, and
macOS substituted silently.

**Preview:** `preview_start`, config name `site` — serves `docs/` on
`http://localhost:4173`. Loop: edit `make_chart.py` → rerun `--public` → reload.

**The pane serves `/search/` from cache, and a plain reload does not clear it.**
Found 2026-08-10, twice in one session, and both times it presented as *the
change did not apply* — a rebuilt page reporting the **old** computed values,
which is the most misleading failure available in this loop because it looks
like a CSS specificity problem. Bust it: `location.replace('/search/?v=' +
Date.now())`, or a `?v=` on the `src` of every measuring iframe. Read a value
you changed before trusting any measurement.

**The preview is Chromium, so it cannot settle a WebKit question — and the user
reads this edition in Safari.** When a report names Safari, the preview can show
that a change is *inert* (geometry unchanged, nothing else broken) and can never
show that it *works*, because the engine that has the behaviour is not the
engine under test. Say which of the two you measured. This cost two fixes on
2026-08-09, both reasoned out against inferences the preview was structurally
unable to test, and **the first was simply wrong** — see the changelog's scroll
entry. The same asymmetry as font substitution: the measurement available is not
the measurement needed, so reason from the mechanism and then **ask the user to
confirm on the browser that has it**. Three WebKit facts learned there, all
cheap to re-lose: `.scroll` computes `overflow-y:auto` though only `overflow-x`
is authored (the propagation rule promotes a `visible` axis whenever the other
scrolls, and a written `clip` computes to `hidden` for the same reason); WebKit
focuses a `tabindex` region **on click**, then routes the wheel to whatever
holds focus; and — the expensive one — **WebKit quantises a line box to a whole
pixel while keeping a margin at LayoutUnit precision**. See *A row's height is
stated* below.

**Better than reasoning at a browser you cannot run: make the page measure
itself in the one the reader has.** On 2026-08-10 two rounds of mechanism-first
reasoning produced two wrong answers, and a throwaway `docs/_diag.html` — one
page that loaded each plate in an iframe and printed a DOM tally, the row-box
heights and every bracket sorted by offset — named the cause from a single
screenshot. Three things made it work, and all three are worth copying:
**report a DOM tally** so a disagreeing count proves the harness wrong before
you trust its numbers (they matched exactly, which is what licensed believing
the rest); **sort the offenders by magnitude**, not by map order, or the four
the user actually named stay buried under "and 19 more"; and **delete it after**
— it lives in `docs/`, so the build sweeps it and counts it as an extra
published page. Note it tripped the leak gate on its first build, because a
function in it was named `census`: the gate deleted the file and exited 1, which
is the gate working, not a false positive.

**The preview pane cannot simulate a NARROW viewport that the page overflows —
it widens to the content instead.** Found 2026-08-10. `resize_window` to 375px
on a page whose content was **641px** wide at that width — `/search/`, before
the Sex column narrowed it to 617px later the same day — reports `innerWidth`
**648**, not 375: there
is no pan to photograph, because the pane grew to fit. So a phone check of
anything wider than the phone must go in a **fixed-width iframe** — the same
self-measuring harness as above, but rendered *visibly* and screenshotted,
rather than measured offscreen. `f.contentWindow.innerWidth` reports the real
355 and the pan is real inside it.

**And confirmation from the user is only evidence if you know which build they
were on.** The scroll freeze was reported clear on 2026-08-09 — **on the live
site, which carries no fix**. So the symptom is **intermittent**, and an absence
observed on an unfixed build says nothing about a fix at all. Before writing
down "verified", ask which build was under the user's hands; a fix that cannot
be distinguished from the bug's own remission has not been tested.

**A blank screenshot means a zero-sized viewport, not a scroll bug.** The
browser pane can come up reporting `innerWidth`/`innerHeight` of **0**, which
captures nothing; because scrolling a zero-height viewport changes nothing
either, it presents as "screenshots work at scroll 0 and nowhere else". Read
`innerWidth` before believing anything you see, and fix it with `resize_window`
at an **explicit** `1280x900` — the `desktop` preset alone did not restore it
(2026-08-09, which is why the folded footer shipped measured but unseen).
Screenshots capture at scroll 0 regardless, so to see something further down,
translate it into view — `document.body.style.transform = 'translateY(-Npx)'` —
rather than scrolling. That is an inspection-only DOM edit; it changes nothing
in `docs/`, and a reload discards it.

**Publish:** `/publish` — gated build, privacy check, push, live verification.

**Finish a session:** `/wrap-session` — backfills `CHANGELOG.md`, rewrites
`SESSION-NOTES.md` as a handoff, and checks this file for claims the session
falsified. Run it before stopping, not after.

A `SessionStart` hook (`.claude/hooks/session-start.sh`) reads
`SESSION-NOTES.md` into context at the start of every session, and flags it as
stale when `scripts/` or `docs/` has moved since the notes were last committed.
It fails open — if it errors, the session starts normally with no handoff. Note
what it cannot do: hooks on session events are **shell commands only**, so it
can guarantee the handoff is read but never write one. That is still
`/wrap-session`'s job.

**Its staleness test has a blind spot, and publishing walks straight into it.**
The test asks whether `scripts/` or `docs/` moved *since the notes were last
committed* — so committing `SESSION-NOTES.md` **in the same commit** as a build
makes the notes look current no matter what they say. A handoff can be freshly
committed and wrong, and that is the one case the warning cannot fire on. It
happened on 2026-08-08: the Zenodo removal committed notes and `docs/` together,
leaving a header describing the *previous* session with no `STALE:` to catch it.
So when a session both publishes and hands off, **read the handoff's own summary
before trusting it** — the hook's silence is not evidence there.

**A handoff's claims about what is PUSHED are the least reliable thing in it,
and the error runs in the direction nobody expects.** `/wrap-session` writes the
notes before the branch is pushed and the PR opened, so the notes describe the
repo one step behind itself — and the failure is not a stale *warning*, it is a
handoff that **understates what is already done**. On 2026-08-09 the notes said
the branch was unpushed with no open PRs and that `laguna-search`'s paired
commit was unpushed; all three were wrong, PR #41 was open, and both remotes
already had the work. A session acting on that would have re-pushed or, worse,
tried to "rescue" published work. **Never take a publication state from the
handoff.** Two commands settle it and they are cheap:

```bash
gh pr list --state open
git rev-list --left-right --count origin/main...HEAD
```

Do the same in the other repo before concluding a paired commit is unpushed.

**New plate:** `/transcribe-plate`. `make_chart.py` is table-agnostic: add a
`TABLES` entry, drop the matching `PENDING` one, write
`scripts/transcription_<n>.py` on the same schema. Counts in the page copy are
computed from data, never typed.

## Project context — always loaded

The four files below are `@import`ed and load automatically, every session,
before you act. Each is the durable, distilled rule set for its area — where
the reasoning behind a rule got long enough to be worth keeping, it moved to
`reference/`, not here.

- `memory/architecture-and-design.md` — where things are, layout, design
  invariants, and the register-markup interface tripwire
- `memory/facts-worth-knowing.md` — facts worth knowing, including the four
  `_FOLD` maps rule
- `memory/standing-decisions.md` — current standing decisions; do not change
  without asking first
- `memory/measurement-gotchas.md` — DOM/measurement traps that recur across
  sessions

@memory/architecture-and-design.md

@memory/facts-worth-knowing.md

@memory/standing-decisions.md

@memory/measurement-gotchas.md

## Specialized references — not always loaded

Everything above was distilled from five larger files. What didn't survive
distillation went to one of two places, depending on whether it's a rule that
applies only within a subsystem, or a piece of history nobody needs on every
turn.

**`.claude/rules/`** — automatically triggered conditional context. Claude
Code loads a rule file into context the first time you *read* a file matching
its `paths:` glob, in that session — not before, and **not** ahead of a
brand-new file created with `Write` before anything under that path has been
read yet. This is triggering, not enforcement: the rule becomes context Claude
reasons from, the same as this file, not a hook that blocks an action.

| Rule file | Triggers on reading a file under | Covers |
|---|---|---|
| `.claude/rules/search-integration.md` | `vendor/search/**`, `docs/search/**` | The published markup as an interface, `write_search()`'s injections, the vendored search page, current `/search/` pan-threshold figures |
| `.claude/rules/plate-audit.md` | `scripts/plate_audit/**` | Calibration and known-clean baselines for the audit rig |

Editing `make_chart.py` or `scripts/transcription*.py` directly triggers
neither rule — both are large, multi-purpose files a path-scoped rule can't
isolate down to the relevant functions. That's why the register-markup
tripwire is in always-loaded `memory/architecture-and-design.md` instead of
relying on either rule to fire.

**`reference/`** — manual, on-demand only. Nothing in `reference/` is
automatically loaded under the current project configuration; open a file
there when the table below says to.

| File | Read it when |
|---|---|
| `reference/environment-notes.md` | Working in a Claude Code session that isn't the Mac (remote/web), or you need the private-vs-public build environment detail |
| `reference/history/INDEX.md` | You want the story behind a rule stated tersely elsewhere, and aren't sure which history file has it |
| `reference/history/search-pan-threshold.md` | Re-deriving or second-guessing the `/search/` pan-threshold numbers |
| `reference/history/zenodo-and-exposure-posture.md` | Reconsidering Zenodo, releases, Wikidata, the custom domain, or exposure posture — read `memory/standing-decisions.md` first; those conclusions stand until the user says otherwise |
| `reference/history/plate-reading-chronology.md` | Checking whether a plate's placement or orthography pass actually happened, and when |
| `reference/history/webkit-and-measurement-postmortems.md` | Diagnosing a rendering discrepancy that smells like the WebKit line-box defect or one of the other measurement-tooling traps found before |
