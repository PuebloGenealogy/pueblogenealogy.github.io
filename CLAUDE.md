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

## Where things are

| Path | What |
|---|---|
| `scripts/make_chart.py` | **The whole renderer** — CSS, JS, HTML, SEO, layout |
| `scripts/transcription*.py` | The 1923 baseline as data. Immutable — *except* to record what the plate actually prints, e.g. `PLATE_NUMBER_MISPRINTS` |
| `docs/` | Generated site. Never hand-edit |
| `assets/og-cover.jpg` | Social card, derived once from the plate scan (see `OG_IMAGE`) |
| `sources/` | Source scans, in repo but not served |
| `METHOD.md` | Editorial method — why readings are made as they are |
| `CITATION.cff` | How to cite. Carries **no doi**, deliberately — see *Release policy* |

There is **no `.zenodo.json`**; it was deleted 2026-08-08 with the rest of the
Zenodo surface. Identity is now two constants at the top of `make_chart.py`:
`SITE` and `REPO`. Every canonical, sitemap entry and card derives from them.
A `DOI` constant sat beside them until 2026-08-08 and must not come back.

## Layout

The chart reproduces the plate's column grid. Every `.node` is
`[.block][.kidcol]`; each nested node adds exactly one `--stub` plus one
`--col`-wide block, so generation *d* lands at `d × (--col + --stub)` on every
path. **Column drift must measure 0 px at every generation.** If it doesn't,
that invariant broke — don't patch it with per-element margins.

Sibling brackets hang off the **mother's** line, not the top of a block, and the
leader rules use the same `mother_row` index. Getting this wrong looks like a
styling detail while actually asserting a different genealogy.

Measure in the browser, don't judge by eye: walk `.node` depth and compare each
`.block`'s left offset.

## Design invariants

Four rules that look like styling preferences and are not:

1. **The root font size is pinned at 16px.** `GEOM` states the plate grid in rem
   against it, so changing the root rescales `--col` and `--stub` and breaks the
   drift invariant. The `--t-*` ramp exists to size **chrome and prose only** —
   nothing inside `.sheet` is sized from it.
2. **A selected or hovered `.line` may change `background`, `box-shadow` and
   `outline` — nothing else.** Padding, border or height there moves the row and
   throws the sibling bracket off its `mother_row`. That reads as a styling
   detail while actually asserting a different genealogy. All three selection
   highlights — chart row, register entry, targeted footer note — draw
   **outside** the border box for a second reason: an `inset` shadow paints its
   bar over the first glyphs, and a hugging outline sits on the text.
   **Which mechanism lights a chart row depends on `html[data-card]`** (set in
   the `popoverOK` block, so it means *the card script is running*, not *JS is
   on*): with it, `.is-selected` only, and `markSelected()` is the sole owner;
   without it, `:target`, which is all a no-JS reader has. Both can never be
   live at once, because **`:target` cannot be cleared** — the hash outlives
   every click — and two rows lit at once is the bug that came from trying
   (2026-07-29). Anything that selects a row goes through `syncSelection()`;
   note the popover's `toggle` and `hashchange` arrive as tasks in **no
   guaranteed order**, which is what `cardRow` is for.
3. **`--rule` is not text.** `body.chart` flattens all text to `--ink` by
   redefining `--muted`; the brackets and leader rules are deliberately excluded,
   because they carry the genealogy's structure.
4. **`--tap` floors every hit area** in the site chrome, and `--bar-h` derives
   from it so anchor `scroll-margin` tracks the bar. Don't restate either.

One thing that will look like a bug and isn't: **the table pills carry the roman
numeral alone at every width** (user, 2026-08-10), and the word "Genealogy " is
still in the markup and in each link's accessible name — `.masthead nav
.nav-word` hides it *visually*, because "I" is not a link name anyone can act on
by ear. **Do not delete the span.** The `≤26rem` rule that used to do this is
now scoped to **`.mast-right`**, where it still trades the Search label for the
glyph; two selectors on purpose, so widening one never silently unhides the
other. The site masthead and `/search/`'s host bar say the same thing in two
stylesheets (`.nav-word` / `.lg-hb-word`), including this pair of selectors —
keep them in step. **Since 2026-08-10 the bar's metrics cannot drift**: the host
bar is built from the masthead's own tokens, read out of `CSS`. What still can
drift is a *rule* one bar has and the other does not, which is why the two are
kept as a diff — see *A host bar* under *The search page is vendored*.

The wordmark reads **"Home"**, not the edition's name, on every page including
`/search/`. The bar is a way back, not a nameplate; the edition names itself in
the `<title>`, the title block and the citation.

**The person card is a regrouped copy of the register entry, and every
card-specific rule must stay scoped to it.** The card clones `#r{n}` — one
source of truth, and the register is also the no-JS person card — then rebuilds
it in `openCard`. So a CSS rule written without a `.pcard` prefix, or a DOM edit
made anywhere but the detached copy, silently reformats the 104-entry register
below the plate. After any card change, verify the register: its relation links
must still compute `display:inline` and its entry titles 16px. Two traps that
have already been hit: chips are `.reg-rel > a`, **direct children only** (a
cross-reference row is also a `.reg-rel`, and its links sit inside an `<em>` of
running prose); and the column divider is scoped to the exactly-two-column case,
because columns wrap and a wrapped column would hang a rule off nothing — the
phone reset of that divider must **out-specify** it, which it failed to do until
2026-07-29 (`.pc-col + .pc-col` is (0,2,0) against the pair rule's (0,3,0)). A
relative's row is `--t-base`, the size a person gets in the register and on the
plate — it is a person line, not a caption. The
card pairs children to a spouse from `data-rel` / `data-with`, **never** by
reading the label — `"Children (with 66)"` is prose, and digging a number out of
prose is the mistake `_p()` exists to prevent.

**There is no on-page chart key, by decision.** One was built as a `<details>`
above the plate and removed the same day; the notation it explained now lives in
the footer's *Navigating this chart* list, which is therefore the **only** place
`+` (spouse), `F.`/`M.` (sex) and the leader rule are decoded. Thinning those
three lines re-opens a defect that has already been introduced twice. Don't
rebuild the key without saying what changed — the reason it went is that it is
decode-once material and the plate is what the reader came for.

`.plate-caption` now carries the pan hint and nothing else, so the **caption**
is what hides above 1400px and in print; hiding only `.pan-hint` would leave an
empty figcaption holding its bottom padding open.

In the plate bar, Find sits left and Scale right, and the split is an **auto
start-margin on `#scale-mount`, never `justify-content:space-between`**. `#find`
carries `[hidden]` until the script unhides it, so space-between would strand
the scale buttons on the left for a reader without JavaScript. The bar has **no
max-width**: it rides the plate's rail, sharing `.scroll`'s `--s5` inline
padding, so Find lands on the sheet's left edge and Scale on its right (0px,
measured). It was centred at `--measure-wide` until 2026-07-29, which matched
the title block's *box* and therefore aligned with nothing a reader can see —
the statistics line inside that box is centred text, inset ~270px each side. Put
it back on a measure and it has to move with `.scroll`'s padding, or the rails
part again.

**The generation ruler is two bands, not one.** Its identity chip
(`.ruler-chipslot`) is a zero-width slot pinned to the inline start, so it
floats over whatever has been panned to that edge; sharing one band with the
labels meant the chip's opaque fill ate the first half of a label
(`GENERA|TION 2`). The chip sits at `flex-start`, the labels stay at
`flex-end`, and **`.ruler`'s height is the only thing separating them** — print
returns it to `2rem` because the chip is hidden there. Shrink that height and
the collision is back.

A table page's title block is the plate label, the numeral, the double rule and
the **statistics line** — no citation. The landing page keeps its citation.

`--muted-fixed` is the real `--muted`, captured at `:root`. Invariant 3 flattens
`--muted` to `--ink` on `body.chart`; a `var()` is substituted with the value the
element it is *declared on* computes, so anything that must keep the dimmer grey
through the flatten reads `--muted-fixed`. **Two things do**, each
deliberately: `.imprint`, so the statistics line matches the landing page's
`.c-stats` grey (6.15:1 light, 6.73:1 dark); and the person card's vital note
`.pcard .pc-title .vital`, so a death or birth note reads as metadata rather
than as part of the name (5.28:1 light, 5.69:1 dark, added 2026-07-28).
Everything else on a table page stays `--ink`. Adding a third is re-opening the
colour decision; measure the contrast if you do.

**The theme control has no Auto state, and since 2026-08-10 no system state
either — the default is LIGHT.** It toggles Light ↔ Dark and the button always
names a real palette. Set by the user; it replaces "a first visit resolves to
the system preference", which had been the rule since the control was built.

**The decision is made in CSS, not in the script**, and that is the half worth
protecting: `:root{color-scheme:light}` is what makes `light-dark()` resolve to
the light half of every pair, so the page is light with the script dead, blocked
or still parsing. The `prefers-color-scheme` palette block inside
`@supports not (light-dark())` is **deleted** — dark is reachable only through
`[data-theme="dark"]`, on either kind of engine. **Do not reintroduce one**: it
restores OS-follows-you behaviour in exactly the no-JS case nobody looks at.
`applyTheme()` defaults to `"light"` to agree with it; both halves have to
change together or a dark-OS reader gets a light page whose button says *Theme:
Dark*. A stored choice still wins in both directions, and nothing is written to
storage until the reader presses the button.

There is **one `<meta name="theme-color">` per page, not a media-keyed pair**,
for the same reason — the pair put dark browser chrome around a light page on a
dark OS until `applyTheme()` rewrote it, and permanently on the 404, which
ships no script.

**The control sits at the FOOT of every page** (user, 2026-08-10; it rode in the
masthead until then). `THEME_FOOT` is one string for all three page types, so it
cannot drift between them: chart pages take it after `</footer>`, the landing
page after `.prose` at `--measure` rather than `--measure-wide`, so its closing
rule lands on the same rail as the page above it. It keeps `.mast-btn`'s shape
and the `--tap` floor — it is site chrome wherever it stands — and it is named
in `@media print`, because hiding `.masthead` used to cover it and no longer
does. The 404 still has no theme control at all: no script, and the button is
authored `hidden`.

The footer apparatus is a **two-column grid of `.app-sec` sections** at
`--measure-wide`, collapsing to one column below 56rem. Grid of whole sections,
not CSS multicolumn — multicolumn will break a heading away from the list it
introduces. This is also what puts the footer on the same left edge as the
register above it.

**Three of its five sections fold, and two deliberately do not.** *Editorial
notes*, *Provenance* and *Citation* are `<details class="app-d">`, closed by
default (added 2026-08-09 at the user's request); *The record* and *Navigating
this chart* stay open, because they orient a reader who has just arrived at the
plate while the other three are consulted once. **Do not fold *Navigating this
chart* later** — see *There is no on-page chart key*: it is the only place `+`,
`F.`/`M.` and the leader rule are decoded, and hiding it behind a disclosure
re-opens by other means the defect that removing the key was meant to close.
The disclosure is the **same
idiom the landing page's FAQ and the register already use** — marker, sizes and
hover identical on purpose. The `<h2>` sits **inside the `<summary>`**, so the
apparatus still has five headings for a screen reader; `cite_html()` therefore
no longer emits its own.

Two things this must not break, both already solved and reused rather than
rebuilt:

- **A deep link into a folded section** — `#note-misprint`, `#note-paternity`,
  `#note-crossref` — is opened by `openDetailsFor()`, the fragment insurance the
  register's disclosure already relied on. Verified on load, on same-page click
  and across pages; `:target` still lights the note. **A new footer note that a
  reader can be sent to needs no new code, but it does need an `id`** — the
  insurance keys on `getElementById`.
- **The offprint carries every section, whatever the reader left folded.** A
  printed edition with its citation collapsed away is not an edition. Two
  mechanisms on purpose: `::details-content` in the print stylesheet (no script,
  current engines only) and a `beforeprint` handler that opens what is closed
  and **restores it on `afterprint`** — reopening all five would be a change the
  reader never made.

The misprint ring is an **`outline`**, never a border or padding: a border
widens the row and throws the sibling bracket off its `mother_row`. The
annotation is a separate row counted with `row += 1`, exactly as a
cross-reference row is, so everything below stays on the `--lh` grid — verified
by walking all 24 child groups and confirming each still sits on its mother's
line. `--sic` is text, so it clears 4.5:1 on both papers alone (6.43:1 light,
7.19:1 dark).

**Every in-block row must be an exact whole number of `--lh`, and that includes
`.xref`.** `Chart.render` budgets one `--lh` per `row += 1`, so a sibling group
whose mother's line sits *below* a cross-reference row is offset by the
difference. `.xref` shipped at `line-height:1.4` plus block padding — 21.09px
against a 24.8px budget — which put seven of Genealogy II's brackets 3.7px off
their mother's line (2026-07-29). It is now `line-height:var(--lh)` with zero
block padding, the same shape `.sic-row` already had. **Table 1 measured clean
throughout**, because no group there has a mother's line below an xref row: the
defect sat latent in shared CSS until a plate with six generations and 30
cross-references arrived, which is why this is stated as an invariant rather than
a fix. One thing it does *not* solve: a cross-reference that **wraps** occupies
two rows against a one-row budget. None does today, on any plate, and the build
has no font metrics with which to guard it — so split a long reference at the
plate's own line break with `|`, the row separator (see persons 160 and 169),
rather than letting CSS decide where the row count goes wrong.

**A row's height is STATED, not inferred from its line box — `height:var(--lh)`
on `.line` and `.sic-row`, `min-height` on `.xref`.** Added 2026-08-10, and it
is the other half of the invariant above: `line-height` alone does not carry it.
Every vertical offset in the chart is a multiple of `--lh` expressed as a
**margin** — `.kids{margin-top:calc(var(--lh) * N)}`, and the same calc from
`line_pad`. A margin is a length, so an engine keeps it to LayoutUnit precision:
**24.796875px**. A **line box is not a length**, and **WebKit quantises it to a
whole pixel**. Measured in Safari 26.3: every row box **24.000px** against a
declared line-height of 24.799999px, so each row of offset lost **0.796875px**
and it accumulated down the tree — **69 of 141 brackets off their mother's
line**, worst −20.016px (25 × 0.797) at III·21 → 74. The sign says where the
mismatch sat: **positive** on a `.kids` group, **negative** on a `line_pad` push
inside the block. Chromium reported 24.797px for both and was clean at 0.003px,
which is why this survived from launch to 2026-08-10 with nobody seeing it here.
A bracket off its mother's line asserts a different genealogy, so this is a
reading error wearing a styling error's clothes — **do not "simplify" these back
to `line-height` alone.** `.xref` keeps `min-height` and not `height` on purpose:
it is the one row type that is `white-space:normal`, so capping it at one row
would make a wrapped reference *overlap* the row below rather than merely
mis-budget it. Wrapping is still the unsolved case described just above.

This is also what a reader sees as a **break in the leader rule**: at III·113 →
204 the error is one row, 0.797px, and 204 is an **only child**, so
`:only-child::after` draws no bracket vertical to bridge the step. There are 29
only-child groups across the four plates (I 5, II 5, III 15, IV 4) and they are
the only places a sub-pixel row error is visible at all — everywhere else the
bracket's vertical covers it. Reported as "a break in the line", diagnosed twice
as a horizontal paint seam, and it was neither: **a 1px overlap on the abutting
rules fixed nothing and was reverted.** The gap was vertical.

**Three colours on a table page are not `--ink`**, and a fourth needs the same
evidence: `--sic` on the misprint annotation, `--muted-fixed` on the statistics
line, and **`--clan`** on the clan field (added 2026-07-28). `--clan` is *not*
the per-clan palette that was reverted — that gave 13 clans 13 hues and
collapsed under deuteranopia. This is one colour for the whole field, so two
colours must be told apart rather than thirteen, and they differ in lightness as
well as hue. Measured 5.86:1 on paper light / 9.53:1 dark, 6.22 / 10.40 on a
selected row. Its values are `--accent`'s — it is the gold the clan carried
before `body.chart`'s flatten — but the **token is separate on purpose**:
`--accent` means *interactive* everywhere else, and recolouring the chrome must
never recolour the genealogy. Declared in **all five** palette blocks; the three
static fallbacks exist for engines without `light-dark()`, and missing one
leaves that browser with an unstyled clan.

## The published markup is now an interface, not just a rendering

**Added 2026-08-03.** A separate finding aid — `laguna-search`, outside this
repo — builds its whole index by fetching the four
`genealogy-*/` pages and parsing them. It reads no transcription module. Since
2026-08-08 it has a remote of its own: **`PuebloGenealogy/laguna-search`,
private**, chosen by the user so the tool stops living in a single working copy
without adding public surface. **Private is a decision, not a default** —
private → public is a click, public → private un-forks and un-indexes nothing.
Its working copy is still the one under `claude-random/`; the remote is a
backstop, not a relocation.

**Since 2026-08-09 its OUTPUT is deployed here, at `/search/`, while the repo
itself stays private** — see *The search page is vendored, not generated here*.
That does not soften anything below. It sharpens it: this page is no longer
only a tool someone else runs, it is a page on this site, so a register change
that breaks the parser now breaks something the edition serves.

So
some of what `make_chart.py` emits is now **consumed by something other than a
browser**, and changing it silently breaks a reader elsewhere:

| Hook | What is read from it |
|---|---|
| `<li class="reg" id="rN">` | one person; `N` is the **id** |
| `.num` `href="#pN"` + its text | the id and the **printed number**, the distinction that matters |
| `.sex` `.name` `.alt` `.blank` `.age` `.clan` `.vital` | the fields |
| `sic-ring` on `.sex` / `.clan` | that the value is the plate's misprint |
| `data-reading` on a ringed `.sex` / `.clan` | the edition's own reading behind it. Six in the edition, all on Genealogy III. **Their gate 1 fails without it** — see below |
| `.reg-rel[data-rel]`, `data-with`, `data-editorial`, `a.edmark` | every relation, and which attribution is editorial |
| `.node` nesting depth, plus `.tree`'s `margin-inline-start` multiplier | **generation** — the register does not print it |
| `.xref` directly after a `.line#pN` | that person's cross-reference; `xref-cell` belongs to nobody |

Two consequences that are not obvious:

- **`dotted()` is not reversible, and one value is already lost.** It appends a
  period "unless the value already ends in one", so `d. in childhood.` and
  `d. in infancy` render identically. A parser cannot tell them apart; II·50
  reads back one period short. Nothing on this site is wrong — this is a cost
  paid by the consumer, recorded so nobody hunts it as a bug.
- **The reading behind a misprint IS published, as of 2026-08-17** — and the
  history is worth keeping, because the obvious fix is the wrong way round.
  `sic-ring` still marks that the printed sex or clan is what the plate shows,
  and the display is unchanged: **the edition annotates a misprint, it does not
  correct it**. What is new is `data-reading` on the ringed `.sex`/`.clan`
  span, carrying the transcription's own reading. **Six attributes in the whole
  edition**, all on Genealogy III — one sex (37) and two clans (50, 255) — each
  in the chart line and the register entry, emitted by `person_line()`.

  **Why it had to be added here, and why a gate landed first would have broken
  every build.** `laguna-search` recovered a misprinted **clan** by *guessing*:
  `nearest_clan()` folds the printed value and takes the single nearest clan
  within two edits from the vocabulary harvested off unringed entries, so
  `Bager` → Badger. There is **no such vocabulary for sex** — `M.` and `F.` are
  both valid and neither is nearer the other — so it filed the printed letter
  under both `sex` and `sexPrinted`, and **Genealogy III·37, Juana** was
  published as a man and could not be found as a woman. The report that found
  it prescribed fixing that builder to "take `sex` from `PERSONS`"; **it has no
  `PERSONS`**, because it builds the index by *parsing these published pages*
  and reads no transcription module. So the edition had to publish the reading
  before anything downstream could read it, and a build gate asserting the
  index's `sex` matches `PERSONS` would have aborted every build until it did.
  **Generalise it: when a consumer cannot see something, check whether it is
  published before designing a fix in the consumer.**

  **Three** things now depend on the attribute: the index takes `sex` from it
  (`nearest_clan()` demoted to a fallback for a page built by an older version
  of this site); that tool's **gate 1 refuses a ringed field whose reading did
  not resolve** — asked only where the field is ringed, since an empty sex is
  legitimate for someone with none recorded; and since 2026-08-18 (`80e0d2d`)
  the `sic` **tooltip names the reading** — *"the edition reads Badger"* rather
  than *"the edition's reading differs"*, which told a reader something was
  wrong without telling them what.
  **So dropping `data-reading` from a ringed span now fails their build**, which
  is the intended coupling and not a bug to route around.
  **What the tooltip did NOT change is the displayed value**, and that is the
  half to protect: `sexOf()` / `clanOf()` still show the plate's `M.` and
  `Bager`, ringed. The edition annotates a misprint; it does not correct one,
  there or here. Note also the copy trap it surfaced — **a sex reading is a
  label carrying its own period (`F.`) while a clan is a bare word**, so
  appending one unconditionally gives *"reads F.."*. That is `dotted()`'s rule
  turning up in a second codebase.

None of this constrains the edition's design — it constrains **silent** change.
Restructure the register freely; just expect `laguna-search` to need its parser
updated, and run its `tools/validate.py`, which compares all 713 entries and
every relation against `scripts/transcription*.py`. **It does not check that
tool's fold map** — its own docstrings claimed otherwise until 2026-08-08 and
were wrong; the map's only guard is its gate 3, below. Don't assume a check
exists because a comment says so.

**Both of that tool's checks read a CACHE of this site by default, so running
them to verify a publish proves nothing without `--refresh`.** `build.py` keeps
the four fetched pages under `cache/` and re-parses them unless the flag is
passed; every gate then passes against the site *as it was when the cache was
written*. The only signal is one word in its first line of output — `cached in
cache/` against `re-fetched` — and nothing fails, because a stale cache is still
perfectly valid HTML. Found 2026-08-08, re-checking the doi removal against a
cache five days older than the deploy. **After any publish here, the first run
over there takes `--refresh`.**

**One edit here can stop that tool's build, and it is a smaller edit than
restructuring anything.** Added 2026-08-07. `laguna-search` marks two people
who share a folded name, sex and clan — they sort adjacent in its alphabetical
list and otherwise read as a duplicate — and its `gate_namesakes_adjudicated`
**refuses to build** until every such pair has a hand-written verdict. There
are three today. **Correcting a single diacritic in a transcription module is
enough to create a fourth**, because folding is what decides the collision.
The `_FOLD` unification of 2026-08-08 was expected to be exactly such a change
and turned out not to be — it moved two fold keys and neither collided (see
*The four `_FOLD` maps are one map*) — but that was checked, not assumed, and
the next name edit deserves the same check. Nothing on this site breaks either
way: the gate is theirs, not ours, and it is deliberately noisy rather than
silent. Expect to adjudicate a pair after changing a name, and know the failure
is a feature.

**There is now a SECOND such gate, and it fails on a different input — a
character, not a collision.** Added 2026-08-08, when that tool's name-break
rule was ratified. It decides where a phonetic name may be divided by walking
back over the marks to a **vowel**, and its `NAME_VOWELS` is a literal set. So
a **vowel character new to this edition** is read as a consonant over there,
the walk-back never lands, and that name's break seams silently vanish. Its
**gate 5** then refuses to build — but only for a single-word name of **14+
characters**. A shorter name loses its seams and fails nothing.

**The literal set is not always `NAME_VOWELS`, and 2026-08-08 hit the other
one.** Beside it sits **`NAME_MARKS`** (`build.py`, currently `"ʼ˙˚˘" "ᶦᵘᵃᵉ"`) —
the marks the walk-back steps *over*. A new **modifier mark** belongs there, not
in `NAME_VOWELS`, and it will not be caught by being non-alphabetic: U+02BD and
U+02BC are both category **Lm**, so `.isalpha()` is `True` and an unlisted mark
is read as a **consonant**. That is exactly why `ʼ` is listed explicitly.

So a character new to a name needs classifying in **three** places in that
repo — the `FOLD` map in `src/search.js`, and then **either** `NAME_VOWELS`
**or** `NAME_MARKS` in `build.py` depending on what it is.

**Only the `FOLD` one has a gate that catches every case, and it is loud.**
That is `gate_keys_are_folded` — **gate 3** — which aborts the build with *"add
it to the FOLD map in src/search.js"* for any search key still holding a
non-`[a-z0-9]` character. The mark classification has only gate 5, which fires
for a single-word name of **14+ characters**; a shorter name loses its seams and
fails nothing. Verified against that repo's source on 2026-08-08, when U+02BD
entered five Genealogy III names, all of them 5–13 characters.

Nothing on this site breaks either way; this is written down because the failure
is in a different repo from its cause, and half of it is silent.

## The search page is vendored, not generated here

**Added 2026-08-09**, `6a882ee` (PR #39). `/search/` is the only page on this
site whose content `make_chart.py` did not write. `laguna-search`'s `dist/` is
copied into **`vendor/search/`** (three files — `index.html`, `search.js`,
`search-index.json`; its CSS is already inlined), and **`write_search()`** turns
that into `docs/search/`. `vendor/search/SOURCE.md` records the commit it came
from and how to refresh it.

**Both directories are generated. Do not hand-edit either.** `vendor/search/` is
overwritten by the next re-vendor exactly as `docs/` is by the next build.

`write_search()` deliberately does the least it can — it wraps, never rewrites.
Six things are injected, and each is there because the vendored file cannot
supply it:

- **The subset font.** `search.css` declares **no `@font-face` at all**, and
  every name it shows is phonetic. **Nothing downstream can catch a regression
  here**: `subset_font.py`'s coverage check reads the *text* of built pages, and
  the names arrive from `search-index.json` at runtime, so they appear in no
  HTML file and that check sees an effectively empty page. Drop the injection
  and the page keeps working, silently substituting. Verified at publish: all 89
  distinct characters in the index are in the subset, both faces `loaded`,
  `span.cell.name` computes `Laguna Serif`.
- **A host bar.** The widget draws a title block and no navigation, so a reader
  landing on `/search/` had no route into the edition. Scoped `.lg-host-bar`,
  taking its **colours** from the widget's own `--lg-*` tokens, so it follows
  the theme and cannot collide with the widget, which is scoped
  `.laguna-search`. It sets `--lg-sticky-top`, the widget's documented hook for
  "the host page has a bar this tall" — without it the widget's sticky filter
  header rests underneath it. `calc(var(--bar-h) + 1px)`, because `--bar-h`
  does not carry the bar's bottom border; measured flush, 0px overlap.

  **Its METRICS are the masthead's, lifted out of `CSS`** (user, 2026-08-10:
  make the bar uniform on every page). It used to restate them in round
  numbers, and the drift that produced is the reason this is now derived: **69px
  tall against the masthead's 49px**, a 44px hit floor where the site's is 32px
  on a mouse, a bare `system-ui` stack against `--font-ui`, a 16px inset against
  8px, and **no Search control at all**. `--font-ui`, `--tap`, `--bar-h`,
  `--s1`, `--s2`, `--s4` and `--t-xs` are emitted **under the site's own names**
  — a build guard aborts if the vendored file ever declares one of them — so
  every rule is the masthead's text with only the selectors and the colour
  tokens changed. **Diff the two when either moves; that diff should show
  selectors and colours and nothing else.** Measured identical after: bar 49px,
  pills 32×32, wordmark and Search inset 8px from each edge, at 375, 410, 430
  and 1000px, in both palettes.

  **One rule in it is not the masthead's, and it is what makes the rest of them
  work: `box-sizing`.** The site resets it globally; the widget scopes its reset
  to `.laguna-search *`, and this bar is deliberately outside that. Without
  `.lg-host-bar,.lg-host-bar *{box-sizing:border-box}` the identical
  declarations build a **different bar** — 65px tall, pills 50×34 — because
  padding and border are added on rather than absorbed. Nothing errors; the
  numbers just stop matching.

  **Search is in it, marked `aria-current="page"` rather than linked.** A bar
  that drops a control on one page is not uniform, and a link to the page you
  are on is a dead control — the wordmark's own idiom on the landing page. It
  takes the masthead's filled inversion, so the current page survives both
  themes and a monochrome screen. Its `font-weight:600` makes it 2px wider than
  the masthead's unmarked one; that 2px is the state, not drift.
- **The theme key, and the default palette.** `THEME_KEY_DECL` — two
  declarations, `window.LAGUNA_THEME_KEY = "lg-theme"` and
  `documentElement.dataset.theme = "light"` — and it is the **only** injection
  that does not go in at `</head>`. It is spliced in **after the charset meta**,
  because it has to precede the vendored blocking script that reads it, and
  nothing should come between the document and the declaration that decodes it.
  `write_search()` **aborts the build** if that meta is missing rather than emit
  a page whose palette silently detaches.

  The second declaration is there because **every other page defaults to light
  in CSS and this one cannot**: the widget's palette is keyed on
  `html[data-theme]` alone and its own default is the system preference, so
  without it a dark-OS reader gets a dark `/search/` beside a light everything
  else. It is set **host-side rather than as another widget option on purpose**
  — defaulting to light is *this site's* decision, and the widget standing alone
  should keep following its reader's OS. It runs ahead of the vendored boot
  script, which only assigns when it finds a stored value, so a stored choice
  still wins.

  This site stores the palette under **`lg-theme`** and the widget's own default
  is **`laguna-theme`**, and *both drive `html[data-theme]`* — so two keys means
  a reader who chose Dark on a chart page is handed the system preference at
  `/search/`, and the same in reverse. **Since 2026-08-09 the widget takes the
  key as configuration** (`laguna-search` `9974d55`), so there is one key and
  nothing to synchronise. The option is read in two places, which is why there
  is a global as well as a `mountSearch({ storageKey })` argument: `themeToggle()`
  runs at mount and can be passed one, but the pre-paint script runs before any
  module loads and can only read a global. Precedence is option → global →
  `"laguna-theme"`, verified all three ways in the browser.

  **Until that day this was a bridge** that mirrored the two keys and carried
  changes back with a `MutationObserver`. **Do not reintroduce one.** A second
  key is the defect, not the starting condition — if the widget ever needs
  another host-side value, ask for an option before writing a patch of that
  shape.

- **The h1 size** (added 2026-08-10). The widget sets its heading from its own
  ramp — `clamp(2.1rem,5vw,4rem)` at `.1em` — because it was built to stand
  alone: 64px against this edition's 40px at 1280px, and 40px against 25.6px on
  a phone. On this site it is one page of seven, so it takes the site's own
  size, letter-spacing and line-height. All three are **read out of `CSS`'s h1
  rule**, never restated; the ramp stays one literal and the build aborts if
  any of the three leaves that rule.
- **The rest of the title block** (added 2026-08-10, the same argument one line
  down — the widget sizes both for a page where its title block is the whole
  page).
  - **The standfirst.** `.lede` is `1.25rem`/1.45 — 20px — against the table
    pages' statistics line at `--t-base`/1.6, **16px**, under the same h1. Read
    out of **`CSS`'s `.imprint` rule**; verified 16px/25.6px on both pages.
  - **The double rule between them.** The widget's `.rule` is 452px wide and
    7px deep in **accent gold**; a table page's `.rule-double` is **8rem, 4px
    and ink**, and it is the same mark under the same heading. Read whole out
    of `.rule-double` — width, height, margin and both borders — with
    `var(--ink)` substituted for `var(--lg-ink)`, exactly as the bar's colours
    are. Verified identical on all six properties against a table page.
  Same abort as the h1 if either rule stops stating what is read from it.

**Which changes belong here, and which belong upstream — the test is whether
the widget standing ALONE would want them.** Added 2026-08-10, after two
requests took opposite answers on the same day. The h1 size is host-specific by
nature: `laguna-search`'s own site should keep its big heading, and only *this*
site needs it on *this* ramp. But the search card's one-line control row, and
the All People list keeping its columns at every width, are that widget's
layout however it is served — so both went **upstream, into
`src/search.css`**, and neither is injected here. An override of another
project's media queries is a thing to re-read on every re-vendor rather than a
thing to own; the first of those two was written as a host injection, anchored
to the rule it undid, and the anchor is what caught it the moment the upstream
fix landed. That is the shape to reach for if a host override is ever genuinely
unavoidable — **anchor it to the vendored rule and fail the build when it
moves** — but reach for upstream first.

**Four more changes ran that test later the same day, and they split three to
one.** Upstream: the Clan menu's checkbox fix and its pan-into-view, the two
search halves holding one line, the theme control moving to the foot, and
`color-scheme` following `[data-theme]` — every one of them something the widget
standing alone is wrong without. Host-side: **defaulting the palette to light**,
which is *this* site's decision and is a second declaration in
`THEME_KEY_DECL`. That one is the shape to notice — it was tempting to ask for
another widget option, and the right answer was that the widget standing alone
should keep following its reader's OS.

**`/search/`'s person list — headed *Index* since 2026-08-10, *All people*
before that, and called the All People list throughout this file — is a table
at EVERY width, and pans rather than stacks.** Set by the user 2026-08-10. It used to become a stacked card below
860px — name on its own line, then sex, birth, death and clan under it with
`Birth `/`Death ` glued on as `::before` labels standing in for the headings
overhead; a row went 56px → 153px and the header 82px → 270px. Now the columns
hold, `.card.people` takes `min-width:min-content`, and below **651px the
DOCUMENT pans sideways** (measured; see *The threshold is MEASURED* below).
Three things about that are load-bearing:

- **The pan is the document's, not an inner scroller's.** An inner scroller
  would become the sticky header's scroll container and the column names would
  stop following the reader down 634 rows — which is the only reason that
  header sticks. It also keeps the site to one horizontal scroller, which
  matters while the plate's `.scroll` has an open Safari freeze symptom.
  **Confirmed on device 2026-08-10**: the user checked `/search/` on their phone
  against the live build that carries the pan, and the header holds with no
  freeze. Admissible precisely because the build was known — see *And
  confirmation from the user is only evidence if you know which build they were
  on*, and note this says nothing about the plate's freeze, a different page and
  a different scroller.
- **`minmax(0,1fr)` and `min-width:0` are the enemy once the table sets the
  page's width.** A zero floor means the inner grid's 445px never reaches
  `min-content`, so the card stops short of its own minimum and the columns
  slide under `Table · #`. Both floors are released below 860px.
- **A column is as narrow as its CONTROL allows, never as its values look.**
  Sex's floor is its `select`, which sizes to its widest *option* — `Female`
  since 2026-08-10, `Not recorded` before it — and will hang over Birth rather
  than shrink; Clan's is its disclosure at 76px. Values like `M.` and `Corn`
  say nothing about it. **The wording of an option is therefore a layout
  input.** Shortening the unrecorded option to a dash took the widest option
  from 124px to 71.78px of need, and the column from 124/124/104px across the
  three breakpoints to a single **80px** at all three — which is what moved the
  pan threshold below. Change an option's text and re-measure the column.
  **A PLACEHOLDER is the same kind of input read the other way round**, added
  2026-08-21: it does not widen its column, it gets **clipped** by it. Death's
  input is 62px at the narrow layout with **47.2px inside the padding**, so
  when that field was relabelled to name what it accepts, *"Year or d."* (52px)
  clipped to `Year or d` — losing the period that IS the value — and
  *"Year / d."* fit by 1.2px, which is no margin. It ships as **`Year/d.`**,
  40px with the face loaded and 37.6px in the fallback stack, and the sentence
  it abbreviates lives in the `aria-label`, which has no width. **Measure a
  label against the narrow layout, in both the loaded face and the fallback,
  and check the subset carries every character in it** — `/` is in both faces;
  a character that is not would substitute silently in the one string on the
  page nothing else proofreads.

**A report that `/search/` is "broken on phones" is re-litigating this decision,
with ONE exception — and the exception is the host bar.** Added 2026-08-17,
after an outside investigation raised it. Everything such a report will measure
is right and already recorded: 375px of client width against **617px** of
`scrollWidth`, the heading past the right edge, the *Find by table and number*
half off-screen, the Clan and `Table · #` columns off-screen. All of that is
what panning **is**, it was asked for, and the user confirmed it on their own
phone. The prescribed cure — scope the overflow to an inner scroller, stack the
search card's halves — is precisely the shape the first bullet above rules out.
Check two claims before spending a round on one: the heading does **not**
truncate (the page's only `text-overflow:ellipsis` is on `.cbf-text`, the clan
filter's button), and the columns are not "hidden" but panned to.

**The real half of that report was that `.lg-host-bar` is `position:sticky`,
which does not stick HORIZONTALLY — FIXED 2026-08-17, and the fix is one
declaration on `body`.** The bar spanned the viewport, not the panned document,
so panning right to reach the `#` box slid it off to the left and left the top
of the page bare. The masthead on a table page has no such problem because
there the pan is scoped to `.scroll` and the document never moves. The cure is
`body{width:fit-content;min-width:100%}` in `write_search()` — **no rule in the
bar changes** — and `max-content` is the wrong tool that looks like the obvious
one, since it would size the table to its no-wrap width and blow the pan out
past the cards' own minimum. This was a **consequence** of the pan decision,
never an argument against it.

**Names still wrap there, deliberately.** Where a name may be divided is an
editorial question, answered in `build.py` and published as `<wbr>` seams
(ratified 2026-08-08). Forcing `nowrap` would truncate a transcribed name, so
4 of the first 60 rows take two lines below 860px and those rows run 59.3px
against 56px. It was 12 of 60 until the name size came down on 2026-08-10.

**The threshold is MEASURED, and it is 651px** — the document is clean at
**636px of client width** and pans at 635, so 651 as a window width with a 15px
scrollbar. It was **675px** until the Sex column came down from 124px to 80px
on 2026-08-10; the column gave up 24px in the narrow grid and the threshold
moved by exactly that. **State which of the two you measured** — this file
carried a disagreement for a session because they were confused, and there is a
third number that looks like both: the document's `scrollWidth` at phone
widths, **617px** at 375–480px (641 before the Sex column narrowed) and 636
once the viewport is near the threshold. Two quantities that both read as "the
width it pans at" and are not the same measurement. The claim that **widening
the Name column** moves the threshold to ~756px is **still unverified**; only
the base is known.

**The SIZE of the name is NOT a second lever on it, and that was measured on
2026-08-10 rather than reasoned.** The expectation — smaller name, narrower
content, earlier pan — is wrong, because the Name column is a **fixed 116px
track** in the narrow grid and the name's own width never reached that track's
minimum. Dropping `1.15rem` to `1.05rem` left the threshold where it was, at
675px. Widening the Name column remains the only lever **on that column** —
but the threshold is the whole grid's, so **any** column's floor moves it, and
the Sex column proved it the same day: shortening one option's text took 24px
out and the threshold with it. What the size *does* move is the
wrapping, and it moves it a lot: 12 of the first 60 rows to 4 at 375px, and at
1120px 2 rows to 0, every row back to a flat 56px.

**`.laguna-search .cell.name` is declared TWICE** in the vendored stylesheet —
the base rule (`1.2rem`/`700`/`1.12`, and `1.45rem` before 2026-08-10) and
again inside the 860px media query (`1.05rem`, and `1.15rem` before). Change
one and the other silently disagrees at the width nobody checked. Both live
**upstream in `src/search.css`**, not in a host injection: table typography is
the widget's own layout, and the upstream-vs-host test says so.

**Measure it with the font loaded — `await document.fonts.ready`.** The same
wrapped-row audit run against a cold iframe reported **11** wrapped rows at
1120px where the true figure is **2**: it was measuring fallback metrics
mid-load. Nothing errors, the number is plausible, and it is wrong by 5×. This
is the font-substitution trap in a new place — the measurement available is not
the measurement needed.

**The section is headed *Index*, and its head is a heading and its count —
nothing else** (user, 2026-08-10). It carried a kicker (*Browse the complete
edition*), the heading *All people* and a *Clear all* button, with the count
pushed to the opposite edge of the card by `justify-content: space-between`.
Now `Index` and `620 people` sit adjacent on one baseline, 0.8rem apart,
wrapping under each other if the card is ever too narrow to hold both — 320px
still holds them. The count keeps `role="status"` and `aria-live="polite"`; it
is the running total (`258 of 620 people` when filtered) and moving it left put
it where the reader is already looking. `aria-labelledby` still names the `h2`.

**Removing *Clear all* left the empty state's *Clear filters* alone, and that
is the load-bearing half.** Every filter clears from its own control — the
selects to `All`, the year fields empty, the Clan menu unchecks, the search box
keeps its clear button — but a reader who has filtered down to **no rows** can
see no such control, so that one button stays. Both are `.link-button`, so the
class did not become dead.

**All of that markup is written by `search.js` at RUNTIME and appears in no
HTML file** — grepping `docs/` for *Index*, the count, or the old *Browse the
complete edition* finds nothing either way.

**The search card's two halves also hold one line at every width** (user,
2026-08-10), and they hold it the same way: `.card.search` takes
`min-width:min-content` below 860px and **pans with the list** rather than
crushing. Two things that cost a round each. **A grid or flex item with
`min-width:0` contributes NOTHING to its track's minimum**, so the card first
resolved to 345.6px with a 190px name box inside a 161.8px column — the same
trap the list's block already warns about, one level up. And **`.laguna-search`
itself needs `min-width:min-content`**, or each card takes its own minimum and
the narrower one stops ~95px short of the list's right edge. Measured 320–1100px
after: one line throughout, both cards identical in width and left edge, and the
pan threshold still the list's.

**Two specificity traps in that stylesheet, and both were live for months.**
`.laguna-search .row-summary .grid` is (0,3,0) and carries the row's inline
padding, so a rule written at `.grid` — (0,2,0) — reaches the **header and not
the rows**. That is how the column names sat 4px left of their values from
861–1120px. Any breakpoint touching that padding must name both selectors.

The second is the **Clan menu, which lives inside `.head`** — so a rule written
at `.head input` reaches its option checkboxes. Below 860px that rule set
`width:100%; height:var(--lg-tap)` and **beat `.cbf-option input` on source
order**, turning every checkbox into a 44px block filling the option's width and
pushing the clan names out of the menu entirely: 340px of content in a 244px
box, a column of black squares, no labels, and a horizontal scrollbar inside the
dropdown. Above 860px `.cbf-option input` won, which is why it only ever showed
on a narrow window. Now `:not([type="checkbox"])` in **both** the base rule and
the media query — the base one still wins on source order, and that accident is
precisely what stopped holding once a later rule restated it.

**And a menu on a panning page must bring itself into view.** The Clan menu
hangs off the right edge of the last column, so with the page panned right to
reach the control it opened at x **−71.8** at 375px. No stylesheet can know
that: the menu is placed in document coordinates and the clipping is the
viewport's. `panIntoView()` on `toggle` moves it **horizontally and only
horizontally** — `scrollIntoView` would drag a sticky-headed page vertically to
reach a menu already in view top to bottom.

**The masthead's Search link sits in `.mast-right`, and since 2026-08-10 it sits
there alone.** Theme moved to the page foot that day and the pills dropped to
bare numerals, so a table page at 371px is **one row, 49px**; 1280px has been
49px throughout. Keep the history, because it is the measurement that governs
this corner: Search was moved here by the user on 2026-08-09 and took the bar
from **109px to 157px at 375px** — three permanently sticky rows, a fifth of an
812px viewport — because the pills and Theme already filled their row to **360px
against 359px of usable width**. That cost is repaid, not disproved.
**Re-measure before spending the width.**

**Do not buy a row back by shaving gaps.** `--tap` is `2rem`, and **`2.75rem`
under `(pointer:coarse)`** — so the floor on the phone, which is the only place
the row is scarce, is 44px and there is nothing to reclaim. This bar already has
a 2.9px-overrun comment recording what living on a thin margin costs. Search
measures 32px beside the pills on a desktop pointer and 44px on a coarse one,
matching them exactly; that is the check to re-run if `.mast-btn` ever changes.
Below 26rem its label is hidden and an inline SVG magnifier takes its place —
drawn, not typed, because U+2315 is missing from the UI stack and U+1F50D is an
emoji, and this bar has no embedded face. That rule is `.mast-right .nav-word`;
it was the shared `.nav-word` until the pills went numeral-only, and the two are
now separate on purpose.

**The landing page reaches it a second way, and that row is deliberately NOT a
plate.** Published 2026-08-09 (`5495819`). The contents block carries a
`.c-across` row to `/search/`, ruled in with the four plates but **outside the
`<ol>`** — `.contents ol li` still counts 4, so a screen reader hears the
edition's plates in Parsons's order and then a link, not a five-item list. It is
measured flush with them (left offset 0.00px, identical width and padding, same
17px title) and carries **its own `--rule-faint` bottom rule**, because a
plate's rule comes from `.contents li` and this row is not one. `.c-across` in
`LANDING_CSS_EXTRA` is a single declaration; everything else it inherits from
`.contents a`. Its count is **computed** from the built tables and says
**entries**, not people — the search page's own line reads "620 people, drawn
713 times", and the two must not contradict each other. Since 2026-08-10 that
line is `/search/`'s **second `.foot-note`**, not the standfirst under *All
people*: the user asked for the standfirst to go and for its content to live in
the page's provenance note. **It did not simply go.** The sentence naming how
many cross-plate joins are the edition's own rather than Parsons's has to sit
where the count is and not only inside a row a reader may never open — see
*There is a SECOND kind of editorial claim*. Don't renumber the landing row into
the list, and don't type a count into either copy: that is the shape of claim
that outlived its truth in `SITE_DESCRIPTION`.

**That placement is CLOSED as of 2026-08-21 — the user chose to leave it exactly
where it is, and it had been offered four times before that.** The ambiguity
being closed is that three blocks on this site answer to the name *provenance*:
`/search/`'s own footer note, the landing page's *Provenance and use*, and each
chart page's folded *Provenance* section. `/search/`'s footer note **is** that
page's provenance block, so the line is already where it was asked to be, and
the landing page stays silent on identity joins by decision rather than by
oversight. **Do not offer to move it again**, and note what the move would have
cost had it been taken: `write_search()` wraps the vendored page and never
rewrites it, so removing the paragraph is an **upstream** change in
`laguna-search` — which the upstream-vs-host test refuses, because a finding aid
standing alone wants to state what its index holds and which of its joins are
its own. The counts would then have to be recomputed here, beside the
`.c-across` row that says *entries* where this line says *people*.

**`/search/` is deliberately absent from `sitemap.xml`.** The page ships
`<meta name="robots" content="noindex">`, and advertising it in a sitemap while
asking robots to skip it is a contradictory signal, not a stronger one. This is
consistent with *Exposure posture* and is **not** a de-indexing measure — that
question is closed and stays closed. If the meta is ever dropped, add the path
to `write_site()` in the same commit.

**The re-vendor loop is `/publish` Gate 8, and `--refresh` is not optional.**
The index is built by fetching *these* pages, so it goes stale the moment the
register's markup moves — and nothing here can detect that, because a stale
index is still valid JSON that renders a working page. Run it when a `.reg`,
`.reg-rel`, `.num`, `.xref` or `sic-ring` changes shape, and always when a
plate's data changes. **The test for whether it is due is a diff, not a
memory**: filter the publish's diff of a table page for register-bearing markup
and count. It was 0 on 2026-08-09 — only the masthead moved — which is how that
gate was correctly skipped on the day it was written. It was **4, on Genealogy
IV alone**, on 2026-08-10, and the re-vendor was due; the other three plates
were 0 that day even though every one of them changed, because the change was
CSS. **The diff is per page, and one plate is enough.**

**When it IS due, decide from the `relationships` diff, and expect two of the
three files to be identical.** On 2026-08-10 `index.html` and `search.js` came
back **byte-identical** and only `search-index.json` moved — in
`meta.generated` (ignore it, it is date-granular) and four `relationships`
entries. Worth knowing what that tool had been publishing: 6's issue as **two
groups labelled by husband**, `Children (with 5)` and `Children (with 7)`, which
stated the split claim more explicitly than the chart ever did. A data error
here is louder over there.

**There is a SECOND shape of re-vendor, and it runs the other way: the change
starts UPSTREAM and no data moves at all.** Added 2026-08-10, the same day and
the mirror image of the entry above. A layout fix to `src/search.css` — the All
People list keeping its columns, the search card's one-line control row —
rebuilds `dist/`, and **`search.js` and `search-index.json` come back
byte-identical while only `index.html` moves**, because that is where the
stylesheet is inlined. Two consequences worth having in advance:

- **A byte-identical index means no `--refresh` obligation.** That obligation
  exists because the index is built by parsing *these* pages; a change that
  parses to the same thing has not staled it. Gate 8's diff test answers "is
  the index due", and the answer here is no — do not run the fetch to prove it.
- **`leak_report()` is still due on all three**, because the sweep is about
  what `docs/` will carry, not about what changed. Run it every time.

**A THIRD shape — and the set does NOT close here; see the fourth below.
`index.html` and `search.js` both move while `search-index.json` stays
byte-identical.** This is the one that looks alarming and is not. Added 2026-08-10, the third re-vendor of that day — a change
to both the widget's markup and its stylesheet (the Clan menu, the search card,
the theme control's move to the foot). Only **`search-index.json`** decides a
`--refresh` obligation, because only it is built by parsing these pages; two
files moving says nothing about whether the index is stale. **Confirm it at this
end rather than inferring it** — the register-bearing diff on all four table
pages was 0 lines that day, which is the test that actually settles it.

**A FOURTH shape, added 2026-08-17: `search.js` and `search-index.json` both
move while `index.html` is byte-identical** — a script-and-data change with the
stylesheet untouched (the sex filter and Juana's record). Nothing about the file
list decides a `--refresh` obligation; only the register-bearing diff does, and
it was 0 that day too.

**That re-vendor also inverted the BUILD ORDER, which is the part to plan for.**
The index is built by fetching *these* pages — but the change the index needed
(`data-reading`) was *in* those pages and not yet live, so a plain `--refresh`
would have re-fetched a site without it and rebuilt the old index. What was done
instead: seed `cache/` with the local `docs/` build, run `build.py` **without**
`--refresh` against it, vendor the result, and ship both in one publish. **That
is sound only because `docs/` is reproducible and exactly those bytes are
published in the same commit** — the post-publish `--refresh` is what confirms
it, and if that run ever disagrees, re-vendor from it. Do not reach for this
shortcut for anything that is not shipping in the same publish; the ordinary
rule is still publish first, then `--refresh`, then re-vendor.

**And run `leak_report()` by hand over the three vendored files every time.**
`check_published_pages()` only opens `.html`, so `search.js` (61 KB) and
`search-index.json` (307 KB) are never swept by the build. Done 2026-08-10 on
all three of that day's re-vendors, all three files clean each time.

**Running `--refresh` after a publish is a separate obligation from
re-vendoring, and it is the one that is never optional.** Gate 8 asks whether
the *index* is stale; the `--refresh` run is what stops that tool's gates
passing against a cache of the site as it was. Run it after every publish, then
decide the re-vendor from the diff above — not from the run's output, which will
look busy either way. On 2026-08-09 it was run post-publish, all seven of its
gates passed, and **all three vendored files came back byte-identical**, so
nothing was re-vendored.

**Do not take a re-vendor decision on `meta.generated`.** It is **date-granular**
(`"2026-08-09"`, not a timestamp), so a same-day rebuild is byte-identical and a
next-day one differs by that one field and nothing else. A handoff reading
"identical apart from `meta.generated`" is recording the clock moving, not the
index drifting.

**And do not take one on that project's COMMIT HASH either.** Added 2026-08-17.
The index is built by fetching *these* pages, so a data change here stales it
while `laguna-search` stands still: that day's re-vendor came from the same
commit as the one before it, `65b8254`, and `search-index.json` still moved by
11 `relationships` records and 2 `people`. An unchanged source commit is
evidence about that project, not about the index. The gate is *"always when a
plate's data changes"*, and it means always.

## The four `_FOLD` maps are one map — keep them identical

**Found 2026-08-03, fixed 2026-08-08.** The four transcription modules each
carry their own `_FOLD` map, and they used to differ: only `transcription_ii.py`
mapped `ŏ` and `Ĭ`, so two Genealogy III names kept their diacritic in a key
documented as "diacritic-free" — `Dziŏ˙kwid˙yuʼă` (III·101) and `Ĭya˙ʼsi`
(III·16). All four now hold the **union** of the four maps, byte-identical.

Measured before changing anything: across all 2,558 string fields in the four
modules, **exactly those two folds change**, and the per-plate count of colliding
folded names is unchanged (2 / 4 / 2 / 1). All four `self_check()`s pass and a
`--public` build leaves `docs/` byte-identical, as expected — `make_chart.py`
never calls `fold()`; the Find box keys on names and numbers directly.

**A new character in a name now needs adding to four maps, not one.** That is
the cost of the fix, and it is the cheaper failure: a map that has drifted is
silent, while four identical maps can be diffed. **This has already been paid
once**: `ʽ` U+02BD went into all four on 2026-08-08 when the second sort was
read on Genealogy III. It folds to `""`, exactly as `ʼ` does, so **no folded
name moved** — 0 of 713, with colliding-fold counts held at 2 / 4 / 2 / 1. Two characters are deliberately
**not** in it — `ï` and `ˑ` (U+02D1) appear only inside `plate_note` prose on
Genealogy II, quoting readings that were *withdrawn*, and are in no name on any
plate.

Note the knock-on in `laguna-search`, which folds independently: changing a
diacritic in a name here can create a fourth namesake collision there and stop
its build until the pair is adjudicated. This edit did not — no fold key moved
except those two, and neither collides.

Person references in the apparatus are linked by `_p()` at each call site,
**never by regex over the prose**. The apparatus is full of numbers that are not
people — 1923, vol. 19, pp. 133–292, U23, `d. 1908` — and a pattern loose enough
to catch "58+59" links those too.

## Facts worth knowing

- **Clan descent is matrilineal**, so a child's clan must equal its mother's.
  A clan mismatch means the reading is wrong, not the rule, and this is what
  caught errors in Table 1 and three brackets on Genealogy II.
  **But it only discriminates where the candidate mothers have DIFFERENT
  clans**, which is most of the time and not all of it. It said nothing about
  person 31, who is Water exactly as the couple whose bracket he sits inside;
  nor about Genealogy IV's 19 and 20, both Bear like their mother; nor about
  Genealogy III's block 2, where 230, 232, 236, 238, 8 and all five children
  moved between them are **Parrot throughout**. Three placement errors, three
  times blind — and two of them shipped. **Where a mother and the alternative
  share a clan, assume no structural check is watching at all.**
  The earlier phrasing here — "independently checks every bracket reading" —
  overstated it, and `self_check()` reporting *all structural checks pass* is
  narrower than it sounds: it verifies clan descent, that nobody is a child
  twice, that union ids resolve and that the counts close. **None of that can
  see whether a person is attached to the right parents.** For placement the
  evidence is the plate — the narrow bracket-column strip, stubs counted.
- **Person 8 (Yu˙si) appears twice** on Table 1; drawn once, with a
  cross-reference standing in for the repeat.
- **A person who appears twice can carry a different marriage each time, and
  the renderer must not merge them.** There are now two shapes and they need
  different mechanisms. Table 1's person 8 has **two different wives**, 7 and
  73, both printed under him: two groups, two `mother_row`s, nothing collides,
  and the already-drawn one is replaced by a child-column note —
  `SECOND_VISIT_NOTE`. Genealogy II's **169 has two husbands and is the mother
  of both groups**, so `u["wife"] == pid` gives both `mother_row = 0`, and two
  brackets cannot begin on one line: the push logic moved her own line down to
  meet the second group and stranded the first, one `--lh` out. Parsons has no
  such problem because she prints 169 **twice, one marriage each** — under
  156+157 as 168's wife bracketing 196–200, and under 164+165 as her parents'
  daughter bracketing 225, 226 — and the second occurrence prints **no `+ 168`
  line at all**. So the collision was self-inflicted: the renderer printed a
  marriage in a block where the plate prints none. `SECOND_VISIT_OMITTED` is
  the mechanism — it suppresses the `+` line, the bracket and the note, and
  prints the plate's own cross-reference row in their place, held back until
  the block's other union lines are down because that is where the plate sets
  it. **Don't reach for it when the two groups have different mothers**; that
  is `SECOND_VISIT_NOTE`'s case and it already works.
- **There is now a THIRD shape, and it is the one where the push logic actually
  has to be told the answer.** Genealogy III's **43** has two husbands and issue
  by both, printed **once**, so neither `SECOND_VISIT_*` applies. Both unions
  have `wife == pid`, so `Chart.render` gave both `mother_row = 0`; the second
  group could not begin there, and the push moved 43's own line down five rows
  to meet it — **stranding the first group**, exactly as 169's did. The page
  said 124 was 14+15's child. `LEADER_ON_SPOUSE_ROW` in a transcription module
  is the mechanism: it names the unions whose bracket the plate hangs off the
  **'+' spouse's** line, which is what Genealogy III does for a second husband
  (its leader sits on the line of the parent whose marriage the group is).
  Validated by `self_check()`; Tables 1, 2 and 4 declare none.
  **It is not only for second husbands, and since 2026-08-17 it holds a second
  entry that is purely a fidelity reading.** `W31` — 58 + 59 → 143, 144 — is a
  **single** marriage whose leader the plate simply draws from the husband's
  line: 58's "Badger" line carries no rule and 59's "Chaparral Cock" line
  carries the one that meets the bracket (native x 2020–2820, y 2795–2900, at
  3x). Nothing structural turned on it; the flag skips the `mother_row` reset
  and leaves `CHILDREN` untouched, so it moved only because the chart
  reproduces the plate. **Do not generalise it**: ten rows below, 60 + 61 → 145
  is the identical shape with the leader on 60's **own** line. The plate is
  inconsistent here, so every entry is read off the ink, one union at a time.
  **No gate can see this defect.** The build reported all 261 drawn and 0 px
  column drift, and both were true — drift measures *columns*. The check that
  finds it is **"is any node's first `.line` displaced from that node's top?"**,
  in the browser, over every `.node`. Run it on any new plate.
  **Genealogy IV's 5 / +6 / +7 looks exactly like this shape and is NOT it** —
  do not reach for `LEADER_ON_SPOUSE_ROW` there. 6 has two husbands and the
  block prints three lines, so the third shape is the natural guess; but the
  plate draws **one** vertical spanning 19 and 20 with a **single** leader
  entering at 19's row from 6's line, and **7's line carries no rule at all**.
  Both children are 5+6's and 6's second marriage has no recorded issue — the
  85/86/87 shape, where a spouse with no leader had none. The transcription had
  split it into two unions and the chart drew two brackets, asserting a
  paternity Parsons does not state; corrected 2026-08-10. **The reusable
  lesson is the diagnostic order**: count the leaders entering the vertical
  before counting the lines in the block.
- **An id addresses a person; `plate_number` is what prints.** There are now two
  reasons they differ, and they are not the same reason. A **misprint** (Table 1)
  shows the plate's wrong number, ringed in `--sic` with an annotation row,
  carried on the union via `PLATE_NUMBER_MISPRINTS`. A **duplicate** (Table 2,
  where Parsons numbers two people 101) shows the plate's *correct* number
  unringed and unannotated, carried on the person via
  `DUPLICATE_PLATE_NUMBERS` → `p["plate_number"]`. Both rows print 101 with
  distinct `#p` anchors. Every place a number is **shown** reads
  `plate_number` — chart line, register entry, relation chip, Find suggestion
  label — and every place one is **keyed** reads `id`: hrefs, `id="p…"`,
  `id="r…"`, and the datalist `value`, which the Find script turns into
  `#p` + value. Get that backwards and either a synthetic id prints on the page
  (it did, in four places, until 2026-07-29) or a name search jumps to the wrong
  person. Declaring the mapping is not enough — the renderer has to read it.
- **Misprint at 76 (Table 1):** the `+` line is numbered 68 but names person 67.
  The chart **prints 68** — the plate's number — ringed in `--sic` red, links it
  to person 67, and carries *(misprint, click here to see notes)* on its **own
  row below**, pointing at `#note-misprint`. Opening the person card from that
  line shows 68; from person 67's other lines it shows 67, and the register
  always keeps 67. **The card carries the number, never the annotation** — it
  repeated the note until 2026-07-28, and that was redundant with the chart row
  the reader opened it from. Declared in `transcription.py`'s
  `PLATE_NUMBER_MISPRINTS`, read through `union["printed_number"]`, carried to
  the card on `data-printed`; a table without one needs no entry. Do not "fix"
  this to 67: printing 67 makes the chart disagree with the scan, which is the
  one thing the edition exists not to do.
- **A cross-reference displacement belongs to a plate, not to the edition.**
  Genealogy II's references into Genealogy I run one high from person 66 onward
  (`CROSS_REF_OFFSET`). **Genealogy III's do not** — audited 2026-07-31, exact
  right across that range. So II was numbered against a Genealogy I that ran one
  ahead and III was numbered against the final one. **Never apply one plate's
  offset to another**; audit each by name, sex and clan. Genealogy III's four
  exceptions are its own, and no two are alike — one run of five that is *ten*
  low, one that is one low, one that cannot resolve at all, and exactly one
  instance of II's +1.
- **Editorial attribution exists, and there are now two cases** — 83–85 on
  Table 1 (added 2026-07-28) and **116–118 on Table 2** (added 2026-07-30).
  Both have the same shape: a woman with two husbands, one bracket, and no
  statement of which marriage the children belong to, so the transcription
  records no father and **the chart draws the plate's single bracket**. The
  *apparatus* splits them, from `TABLES[…]["paternity"]`, marked with a dagger
  linking to `#note-paternity`: 83, 84 to 69 and 85 to 70; all of 116–118 to 49.
  **The mark is at both ends** — the parents' `Children` rows and each child's
  own `Parents` row — and it marks **the pairing, not the mother**, who is the
  plate's own bracket. It sits on the row and not on the father's chip partly
  for that reason and partly because the card's rows are anchors: an `<a>`
  dagger cannot nest inside the chip's `<a>`. Don't "fix" that to a per-chip
  mark without solving the card, or the card loses the dagger silently.
  Read METHOD.md's *Editorial attribution* before adding a third — four rules
  govern it, and the first is that the chart never carries it.
  **The two differ in the one way a reader checking them cares about, and
  rule 4 now turns on it.** Table 1's evidence is external documentary research,
  which **must not enter the repo** — that footnote says a reading rests on
  evidence outside the plate, names no source, and stops. Table 2's is
  **Parsons's own text, p. 195**, which is published, so that footnote **quotes
  it and cites the page**. Do not flatten these into one rule in either
  direction: citing a printed source is required, and naming an unpublished one
  is a leak. Note the edition asserts nothing the plate does not *in the chart*,
  in either case; neither is a precedent for "improving" it.
  **Genealogy III needs none of this, and that is a finding about the plate, not
  an oversight.** It marks paternity itself: the leader rule reaching a bracket
  sits on the line of the parent whose marriage the group belongs to. 85/86/87
  is Table 1's 83–85 shape and still needs no attribution, because 86's leader
  is on her own line and 87 has none. Don't reach for the attribution machinery
  on this plate.
  **But the converse does NOT hold, and that was over-stated here until
  2026-08-17.** This paragraph read "so a spouse with no leader had no recorded
  issue", and block 1 falsifies it: **58 has no leader on her own line and two
  children**, 143 and 144, because the plate draws that group's leader from her
  husband 59 (see `LEADER_ON_SPOUSE_ROW`'s `W31`). So a leader present names
  whose marriage a group is; a leader **absent** from one partner's line means
  nothing on its own — read the other partner's line before concluding anyone
  was childless.
  **85/86/87 was re-checked against the scan the same day and the reading
  STANDS — but on narrower evidence than this file used to claim.** Measured in
  the 160px gap between the text and the bracket: 86's row carries a solid rule
  (50/142/138/24 ink px at y 227–230), and **both husbands' rows are bare** —
  85's and 87's alike, the constant 1–2px through y 231–253 being the bracket
  vertical passing, not a leader. So there is one bracket and one leader, and it
  sits on **86's** line, which she shares with *both* marriages: that line alone
  names no father. What settles it is the contrast with **43 on this same
  plate** — where a woman has issue by a second husband, the plate gives that
  group its own leader on the second husband's line (45's, → 126), and 87's line
  carries nothing at all. Clan cannot help: both marriages have the same mother,
  so 184–189 are Turquoise either way. **State it that way** — the reading rests
  on Parsons's practice with 43, not on "a spouse with no leader had no issue",
  which `W31` disproves as a general rule.
  **Genealogy IV's 5/+6/+7 was re-checked the same day and also STANDS, on
  evidence one step weaker again.** Measured in the 750px gap: 6's row is solid
  ink (750/750 at y 6099–6116) and **both husbands' rows carry nothing** above
  3px — the same configuration as 85/86/87, so the single leader sits on the
  line 6 shares with both marriages and names no father by itself. The
  difference is that **Table 4 never demonstrates its own convention**: its only
  other second marriage with issue is V07, where the second spouse is the
  *mother*, whose line carries the bracket anyway. So the "Parsons marks a
  second husband's issue when she means to" argument has to reach **across to
  Genealogy III's 43**, and a cross-plate inference is exactly what this file
  warns against elsewhere. What holds it up locally is that the bracket is drawn
  inside **5's block**, he being its primary with 6 and 7 both '+' lines under
  him. Keep the reading; state the basis as cross-plate, and never as "a spouse
  with no leader had no issue".
- **There is a SECOND kind of editorial claim now, and it is about identity, not
  paternity.** Added 2026-08-09 with `/search/`, and set out in METHOD.md's
  *Identity across plates*. Searching by name across four independent numberings
  means deciding whether two entries are two records of one person: the plates
  carry 713 entries and **620 people**, 79 drawn more than once, of which
  Parsons cross-references **65**. The other **14** are listed one by one — and
  **two of those are hers**, stated through a second husband rather than by
  name, so the edition's own unattested count is **twelve**. Every one is a
  family joined as a family, never a lone name; a shared name joins nothing,
  which is what the three adjudicated namesake pairs exist to say, one of them
  still **open**.
  **This changes nothing in the chart or the register**, and that is the point:
  the joins live on the search page and in its index, and every unprinted one
  carries a ringed **NOT PRINTED** marker and quotes nothing. Rule 1 of
  *Editorial attribution* holds unchanged — the chart never carries it. **Rule 4
  holds in its stronger form**: the evidence is the plates themselves, so it is
  quoted in full, and **no identification here rests on external documentary
  research, nor may one ever**.
- **English names in parentheses are plate data**, not research additions —
  person 90 "Heʼsa (Hazel)" on Table 1, and the Johnsons and Mana on Table 4.
- **`d.`** means the person had already died when Parsons recorded the
  genealogy, during her fieldwork of 1918–19; the year is given where known. A
  number after a name is their age at recording.
- **Phonetic glyph rendering is settled — don't re-open it.** Coverage was
  proven from the cmap: all 85 characters in the transcription and all 94
  rendered on Genealogy I are in both faces, `ᶦ` U+1DA6, `ᵘ` U+1D58, `ᵃ` U+1D43,
  `ʼ` U+02BC and `˙` U+02D9 included. The faces are base64 data URIs, so nothing
  is fetched and nothing can 404, and no combining marks are used, so there is
  no mark positioning to vary by platform. The one thing the cmap could not
  answer — whether a real browser on **Windows or Android** honours the embedded
  face — was **checked on device by the user on 2026-07-28: everything rendered
  correctly on both.** Note macOS substitutes for any font, so no on-screen
  comparison here can demonstrate the absence of substitution — if this is ever
  questioned again, read the cmap, don't measure widths.
- **Magnification has a floor, and past it the upscaler invents letterform.**
  A diacritic on Genealogy III is about **ten pixels of ink**. Crops read
  cleanly to roughly 5–8×; beyond that the mark becomes an amorphous blob and
  any apparent shape is the resampler, not the plate. Demonstrated 2026-07-31
  on III's turned-comma question: at 20× the questioned mark at 157 and a
  **known U+02BC two lines below it in the same block of type** are
  indistinguishable. So a glyph distinction that survives only above ~8× is
  **not evidence** — and the honest finding is "this scan cannot resolve it",
  which is a closure, not an open thread. Table 3 is 3770 × 5503, a ninth of
  Table 1's pixel count, so the same test is decidable on Table 1 and not here.
  Settling such a question needs a **better scan**, not a bigger crop.
- **And a phone photograph of the page IS that better scan.** Added 2026-08-08.
  The turned-comma question was carried for a week as needing AMNH; what settled
  it was the user photographing lines 156–159. A mark that is ten pixels of ink
  on `sources/parsons-1923-table-3.jpg` is **fifty** in a close photograph, which
  is past the floor by a factor of five. So when a glyph question is stuck,
  **ask for a photograph before reaching for an institutional scan** — it is
  hours rather than weeks, and it worked.
  **Measure it, don't look at it.** Three numbers per mark, taken at native
  resolution so no upscaling enters the measurement: height in rows, the
  horizontal centroid of the bottom third minus the top third, and ink mass top
  versus bottom. That is what distinguished the two sorts, and it is also what
  distinguishes a **mirror** from a **rotation** — both sorts being top-heavy is
  what picked U+02BD over U+02BB. Eyeballing a 6× crop had produced the right
  hunch and no evidence. The method and the numbers are in
  `transcription_iii.py`'s docstring. **All five instances are settled** — 154,
  156, 157, 228 and 242, published `5441abc` — so do not re-open it.
  **Two refinements from the second round, and they generalise.** *Heights
  compare only WITHIN one photograph*; the drift and the ink mass do not, so
  lead with those two and treat height as corroboration. And *look at the crop
  before believing a number* — the first crop box for the 159 control caught the
  `s` of `wits` and reported a known U+02BC as the questioned sort. The flood
  fill measures whatever blob it is handed, and a wrong box fails silently by
  producing a perfectly plausible number.
- **Reading a plate for TYPE is a different job from reading it for STRUCTURE,
  and the constraint is the display rather than the scan.** Recorded 2026-08-21,
  from the pass that read Genealogy III block 1's 229 entries; it had lived only
  in the handoff, which is overwritten every session. **Chunk rather than
  magnify** — anything taller than ~1500px is downscaled on display, which is
  what makes a big crop illegible.
  - **Plan the tiles from an ink-row profile**, one generation band at a time:
    count dark pixels per row inside the band's x range, group runs of ≥6 into
    text lines, then pack lines into tiles ≤420 native px tall. It found 276
    text lines in block 1, which **reconciles** against 229 people plus their
    cross-reference rows, 155's four continuation lines, `(Sister of 10)`, the
    six second-occurrence lines and the plate title. A reconciling count is what
    licenses trusting the rest — the same argument as the `_diag.html` DOM tally.
  - **Two magnifications, not one.** 380 native px at **4x** (1520px, as much as
    a vision read carries) over the number-sex-name field, and **2.8x** over the
    tail for age, clan and cross-reference. Re-crop at **6–7x** the moment a mark
    is ambiguous: that is what settled 60's `Kʼapokaʼă`, where 4x read the second
    apostrophe as a raised dot. Past ~8x see the magnification floor above.
  - **Table 3's generation columns**, native x of the right-aligned number:
    g1 145 · g2 755 · g3 1293 · g4 1833 · g5 2377 · g6 2920 · g7 3467. Band x
    from `col − 60`; a full line runs about 370px. Block 1 crops as three chunks
    × two strips with 830px of overlap —
    `crop.py /tmp/t3.bmp {0,1470} {150,1590,3030} 2300 {1480,1480,1450}` — plus
    block 2 at y 4440, h 1080. **A column-6 strip carrying the mother's column
    beside it** is what settled the six groups the fold crease hides:
    `crop.py /tmp/t3.bmp 2250 <y> 1150 1450` at y = 150, 1550, 2950 and
    (h=1100) 4400. Table 4 is 12255 × 8409 — crop at native and chunk hard.
  - **Remotely there is no `sips`, and the replacement is better for type.**
    `pip3 install pillow`, then crop straight from the JPEG with
    `Image.crop().resize(..., Image.NEAREST)`, which invents nothing exactly as
    `crop.py` does not.
- Google's structured-data validator is **stricter than schema.org** — valid
  schema.org has been rejected twice here. `check_structured_data()` guards the
  rules we have been told about, not all of them; a Search Console report
  outranks the build's opinion.

## Environment

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom`, owner of the
`PuebloGenealogy` org. **No Homebrew, no ImageMagick, no PIL** — use `sips`.

**`sips -c H W --cropOffset 0 0` centre-crops instead of cropping at the
origin.** It does not error; it returns a tile from the middle of the image, so
a plate-tiling grid silently reads the wrong region. Use `1 1`. Found
2026-07-30 while tiling Genealogy III, where it returned a region 2450 px down
the plate.

The repo lives under Google Drive, whose sync daemon can touch `.git` mid-write;
if git reports object corruption, that is the likely cause.

**A REMOTE session is a different machine, and two of its limits change what
the publish procedure can do.** Found 2026-08-21, working from Claude Code on
the web. Neither is a fault to debug — both are egress policy, and the proxy's
own README says to report a 403 rather than route around it.

- **There may be no route to the published site.** `pueblogenealogy.github.io:443`
  answered **403 to CONNECT**, so `curl` returns `000` and `build.py --refresh`
  dies in `urllib`. That takes out `/publish` **gate 6 entirely** — the 200
  sweep, the sitemap `<loc>` count and the page-by-page SHA-256 comparison —
  and the post-publish `--refresh` with it. **A green `pages build and
  deployment` run is not a substitute**: this repo verifies by hash precisely
  because the Pages API misreports the deployed commit. Push, then record both
  checks as owed and name the commands; do not write "verified".
  **It is a standing property of the environment, not a transient state — do
  not burn a turn re-testing it hopefully.** Re-measured 2026-08-21 from a
  second remote session: two `curl`s ten seconds apart, both `000`, and
  `$HTTPS_PROXY/__agentproxy/status` recorded a fresh `connect_rejected` for
  each with the same *gateway answered 403 to CONNECT* against that host. The
  status endpoint is the thing to read, because **`curl` hides the body of a
  failed CONNECT** and `000` alone cannot tell a policy denial from an outage;
  check the timestamps against `date -u` or you are reading the *previous*
  session's failure. The remedy is not in the session: either run the two
  checks from the Mac, or widen the environment's egress policy — which is set
  when the environment is created, covers `laguna-search`'s fetch target as the
  same host, and is documented at
  `https://code.claude.com/docs/en/claude-code-on-the-web`.
- **A delete-push is refused.** `git push origin --delete <branch>` returned
  **HTTP 403** in both repos while ordinary pushes went through, so a merged
  branch cannot be cleaned up from there. Delete the local one, say so, and
  leave the remote for a machine that can.

What a remote session gains, which the Mac does not have: **Pillow and a real
headless Chromium** (Playwright at `/opt/pw-browsers`), so a plate can be
cropped without `sips` and `/search/` can be measured at an actual 375px
viewport — where the desktop preview pane widens to the content instead. See
*The preview pane cannot simulate a NARROW viewport*.

**PRs here are squash-merged, so `git branch --no-merged` is not a test of
whether a branch holds unmerged work.** A squash puts the branch's *content*
on `main` as a new single-parent commit; the branch's own commit is never an
ancestor, so ancestry-based checks report merged work as unmerged and invite a
session to "rescue" something that is already published. **Read the PR state
instead** — `gh pr list --state all --head <branch>`, and compare
`git rev-parse <head>^{tree}` against the merge commit's tree if you want
proof. Found 2026-08-07 sweeping stale branches:
`handoff-2026-07-29-plate-chrome` looked unmerged and is PR #13, squashed onto
`main` as `5a37bdf`, tree `39b8487` — **identical** to the branch head
`df2b1e0`, empty diff. Nothing was ever at risk.

**The same mechanic has a second face, and that one IS dangerous: a stale open
PR can become a REVERT.** Branch new work off a branch that has not merged yet,
squash-merge the new work, and the old PR's content lands on `main` inside your
squash — leaving the old PR open, contributing nothing, and now proposing to
*undo* everything committed after it. Found 2026-08-08: PR #33 held the
previous session's handoff branch, PR #34 was branched from it, and after #34
and #35 merged, #33 would have deleted all five U+02BD readings and reverted the
font subset. It was **closed, not merged**.
`gh pr list --state open` is what surfaces it — run it when wrapping a session,
not only when tidying branches. The check that settles it is
`git diff origin/main origin/<branch>`, and the thing to read is the
**direction**: deletions there mean the branch is *behind* `main`, not ahead.

**A branch does not have to be built on to acquire this, and a PARKED one
acquires it fastest.** Found 2026-08-09. PR #43 was deliberately left open as
the build to test a Safari fix on; it was purely additive against `main` when it
was parked, and stopped being so within the hour — not because anything was
branched off it, but because `main` moved on `CHANGELOG.md` and
`SESSION-NOTES.md` while the branch stood still. Every session that records
anything widens it. So **a branch's direction is a fact with a timestamp, not a
property**: re-measure it at the moment of merging, never trust the reading that
was taken when it was parked, and bring `main` into the branch before merging
rather than after discovering the deletions. The records are the files that
drift first, which is also why the drift is easy to wave through — it looks like
handoff churn rather than a revert.

**That branch was CLOSED unmerged on 2026-08-10, and the end of the story is the
useful part.** In one further day it went from records-only drift to a genuine
revert: **152 insertions against 262 deletions** in `scripts/` and `docs/`
alone, because `main` had gained Genealogy IV's corrected parentage and the
row-box fix while the branch stood still. Nobody built on it; parking was the
whole cause. **A parked branch has a shelf life measured in days, and the cost
of keeping one is that its diff must be re-read every time it is considered.**
The right shape, when a fix needs testing later, is to leave the **commit**
reachable by SHA and cherry-pick it onto a fresh branch off current `main` at
the moment it is wanted — which also means it gets tested against a build that
has everything since. Nothing was lost closing it: the reasoning behind both
scroll attempts had been carried onto `main` during the previous wrap precisely
so the branch was never the only copy. **Carry the measurements to `main` when
you park a branch, and the branch becomes disposable.**

Two mechanics from the same sweep. GitHub **auto-deletes a branch on merge**,
so remote-tracking refs here go stale in bulk — ten did — and
`git fetch --prune` belongs *before* any cleanup. And a batch
`git push origin --delete a b c` **fails whole** if any one ref is already
gone: nothing is deleted, and the refs that do exist are left untouched, which
reads as a permissions problem and is not one.

`_backup-v1-laguna-genealogy-tables-2026-07-27/`, one level up, is the **sole
surviving copy** of the deleted v1 repo. Do not clean it up as stale.

## State

Site live; Search Console and Bing both verified; structured data valid and
guarded at build time. v1 is deleted.

### Release policy — REPLACED 2026-08-08. No release is ever cut

The old policy (set 2026-07-30) said: cut no releases *during active
development*, and cut one when all four tables, the design, the transcriptions,
the text and the citations were final. **All four are now final, so that policy
would read as "the release is due." It is not.** It has been replaced, not
satisfied.

**The current policy is simply: no GitHub Release, no Zenodo deposit, ever,
unless the user says otherwise.** The site keeps deploying from `main` as it
always has. Publishing the site and cutting a release remain different acts, and
only the second one touches Zenodo — which is now a thing the edition does not
do at all.

**Zenodo was withdrawn from the edition's public face on 2026-08-08**, as part
of *Exposure posture* above. What that involved, so nobody has to re-derive it:

- `.zenodo.json` — **deleted**.
- `DOI` / `DOI_URL` in `make_chart.py` — **deleted**, along with the footer
  citation's "Archived at" line in `cite_html()` and the `identifier` field in
  **both** JSON-LD blocks (`Dataset` on table pages, `CollectionPage` on the
  landing page).
- `CITATION.cff` — the `doi:` field and the whole `identifiers:` block gone.
  This is the repo's "Cite this repository" widget, so it is the most visible
  place a doi could reappear.
- `README.md` — the DOI badge and the archiving paragraph gone.
- The Zenodo **deposit webhook** on the repo — **removed**, so no future release
  could mint a doi even if one were tagged. Two things learned deleting it:
  **the hook id is not stable** (Zenodo replaced it mid-session, so a stale id
  returns `Not Found` exactly as an unscoped token does — re-read the id before
  concluding anything), and **GitHub's side is not the durable switch**. Zenodo
  can recreate the hook while the repo is still enabled at
  `zenodo.org/account/settings/github`. If a hook ever reappears, that flag is
  why. **The user has since severed the GitHub↔Zenodo link**, which settles it.
- **Do not go hunting for the webhook's access token.** The hook URL carried
  `?access_token=…` pointing at `zenodo.org`, so it was a **Zenodo** credential
  and never appeared in GitHub's settings; it does not appear under Zenodo →
  Applications either, because that page lists only hand-created tokens and
  webhook receiver tokens are minted internally. All three sections of that page
  were empty when checked on 2026-08-08. **That is expected, not a symptom.**
  Severing the linked account is what invalidates them.

**The record itself was deleted by the user the same day**, and the way that was
possible is worth recording, because the widely-repeated version of the rule is
wrong:

- **Zenodo lets a record's OWNER delete it within 30 days of publishing.**
  v1.0.0 was published 2026-07-28 and deleted 2026-08-08, 11 days in. The
  "published Zenodo records are permanent, only support can withdraw them" claim
  that this file carried earlier the same day is **false for the first 30 days**.
  It is true afterwards, which is why it is the version everyone repeats.
- **What survives is a tombstone, not the deposit.** Both dois — `…21637900`
  (concept) and `…21637901` (v1.0.0) — now return **HTTP 410 Gone** at
  `zenodo.org/records/21637901`; the concept doi redirects to the same page.
  The files are gone. **The metadata is kept and displayed**: title, author,
  year, doi, and the removal reason, which reads *"Personal data issue"* and is
  **publicly visible to anyone following the doi**.
- **So the residue is a citation stub, not an archived copy of the edition.**
  Nothing points from here to it, and it no longer holds a copy of the plates.
  A tombstone cannot be removed; that part really is permanent.

**A doi reappearing anywhere in this repo is a regression, not a restoration.**

### Exposure posture — set by the user 2026-08-08

**The user does not want the edition promoted, and does not care whether the
site is indexed.** This reverses the outreach programme that ran from launch
through 2026-08-07, and it is a decision, not a mood.

What is settled:

- **Wikidata is removed** — no item, payload deleted. See *Outstanding*.
- **No inbound link is seeded without asking.** The gate that the custom-domain
  closure lifted is back. Wikipedia's *Elsie Clews Parsons* external links and
  the AMNH Digital Library are **not** to be pursued as outreach; the AMNH
  handle is kept only as a fact about the source.
- **`GOOGLE_SITE_VERIFICATION` still must not be blanked**, and low exposure is
  now a *second* reason rather than a counter-argument. Search Console ownership
  is what a removal request runs through, so blanking the tag would remove the
  only mechanism for taking a page out of results. The hard rule stands
  unchanged; it now has two justifications instead of one.

**De-indexing — CLOSED 2026-08-08 by the user: it is not important, and nothing
is to be done about it.** It was carried as the open thread for two sessions,
awaiting a choice of level; the user struck it instead. So `robots.txt`,
`sitemap.xml`, the JSON-LD and the absence of `noindex` all stay exactly as
the build emits them today. **Do not re-raise it** as an obvious follow-on to
"the user wants low exposure" — not promoting the edition and taking it out of
Google are different requests, and only the first one was made.

The mechanism is kept because it is what makes the closure cheap to hold, and
because the intuitive move is the wrong one: **`Disallow:` in `robots.txt` does
not de-index.** It forbids crawling, so an already-indexed URL can persist in
results as a bare link that can no longer be re-read. **`<meta name="robots"
content="noindex">` is the tool that removes a page** — and it requires crawling
to stay *allowed*, so the two must not be combined. Neither is deployed here.

**Outstanding:**
- **Wikidata — REMOVED 2026-08-08 by the user. No item is to be created, and
  the payload is deleted.** This is a decision, not a deferral, and it is not
  to be re-derived: the user does not want the edition promoted, and does not
  care whether the site is indexed. `wikidata-quickstatements.txt` is gone from
  the working tree — it survives in git history, which is expected and fine, as
  it held nothing but bibliographic metadata about the edition. **Do not
  reconstruct it**, and do not offer a Wikidata item as an "easy win"; it was
  the highest-return inbound link on the old plan, which is exactly why a future
  session will be tempted to propose it again.
  The **whole inbound-links programme is under the same reconsideration** — see
  *Exposure posture*. Do not seed any inbound link without asking.
  **The AMNH handle is `2246/158`** — `https://digitallibrary.amnh.org/handle/2246/158`,
  found 2026-07-30. Kept because it is a **fact about the source**, not an
  outreach step: it is the institutional route to a better scan. It is **no
  longer the only route, and no longer the first one to try** — a photograph of
  the page settled 156 and 157 on 2026-08-08 after the scan could not, so ask
  for a photograph first. (It used to be recorded as the identifier
  `.zenodo.json` omitted from `related_identifiers`; that file no longer
  exists.) Note `digitallibrary.amnh.org`
  **403s automated fetches** — use a real browser, not `WebFetch`.
- **Custom domain — CLOSED 2026-07-31 by the user. The edition stays on
  `pueblogenealogy.github.io` permanently.** This is a decision, not another
  deferral, and it is **not to be re-opened** — it had been carried as "deferred,
  not closed" through several sessions and went missing from a `resume` list
  once. The reasoning is kept here in full, because the argument that settles it
  is not the obvious one and a future session that re-derives it from scratch
  will probably reach the wrong answer.
  **It is not an SEO question.** Google treats `github.io` as a public suffix,
  so no authority is inherited from it and none is lost by leaving. The old
  framing of a custom domain as "the strongest SEO upgrade" was simply wrong.
  **The real trade is durability against portability, and durability won.** A
  domain you own is portable — it can change hosts without breaking a
  doi-adjacent link — but it survives only as long as someone keeps paying for
  it. A lapsed domain does not degrade gracefully: it gets re-registered, and
  every citation seeded from Zenodo, Wikidata and AMNH then points at whoever
  bought it. `pueblogenealogy.github.io` needs no renewal, cannot lapse, and
  cannot be taken by a squatter. For a scholarly edition meant to outlive the
  attention of its editor, **GitHub's institutional durability beats the
  editor's own**, and that is the whole of the argument.
  Consequences: `SITE` in `make_chart.py` never changes; no `CNAME` file is ever
  added to this repo; and the Search Console and Bing properties stay as
  verified — see *Exposure posture* for a second, stronger reason they must.
  This closure once also lifted the gate on seeding inbound links. **That
  sentence is withdrawn as of 2026-08-08**: the gate is back and harder, because
  the user has since asked for low exposure. Nothing else about the domain
  decision changes — durability against portability is untouched by it.
- **No release is outstanding, and after 2026-08-08 none ever will be.** v1.1.0
  was prepared and cancelled in 2026-07; the whole release track is now closed
  by the *Release policy* above. **All four plates are published** (2026-07-31)
  and **Genealogy III's two editorial items are both closed** — the
  cross-reference footnote is written and **deployed** (`#note-crossref`,
  verified live by SHA-256), and the second sort is **settled at all five
  instances** — 154, 156, 157, 228 and 242 read U+02BD and are published
  (`ebd8738` PR #34, then `5441abc` PR #35, both 2026-08-08). **There is no
  reading question open on any plate.** Under the old policy that would have made the
  release due; it does not, because the policy changed. **Publishing the site is
  not releasing it, and releasing it is no longer on the table.**
  **"No reading question open" is not "the readings have all been checked", and
  2026-08-10 proved the difference.** Genealogy IV shipped on 2026-07-31 with
  20 attached to the wrong marriage, and it survived four self-checks, every
  publish gate and ten days of the plate being live. Nothing structural could
  see it: 19 and 20 are both Bear, exactly like their mother, so clan descent
  cannot discriminate; the counts close either way. **Placement is unverified
  wherever the user has not personally read it against the scan** — which is
  true of II (checked 2026-07-30), IV's 5/6/7 (2026-08-10) and **the whole of
  Genealogy I (2026-08-17: the user read the printed number against every one
  of its 76 stubs and every number matched)**. Treat a report of a "misaligned"
  or "broken" bracket as possibly a data error, not automatically a rendering
  one.
  **Genealogy III's BLOCK 2 is read and corrected as of 2026-08-17; its
  BLOCK 1 is not, and the distinction is the whole of what is known.** Block 2
  gave up **two placement errors on one bracket column**, both settled by the
  user reading the scan and both published (PR #60): 238 and 8 are 230+231's
  sons rather than 236+237's, and 243, 245 and 246 are 236+237's rather than
  232+233's. Block 1 was run through the calibrated plate audit and produced
  **no new finding, which is not the same as being correct** — the audit
  cannot read type, so a group of the right size whose members are misnumbered
  passes silently, and **column 6's six groups sit under the fold crease where
  the tool is blind altogether**. Block 1 is 4300 of the plate's 5503px.
  **BLOCK 1 WAS THEN READ, 2026-08-17, and the transcription is right at every
  group** — membership, the number printed against each stub, and clan descent,
  including the six column-6 groups the crease hides, which are real brackets
  with the right counts and clans. All 15 of the calibrated audit's problems
  are explained and none is a defect; they are a known-clean baseline now, so a
  16th problem is the signal. **Its ORTHOGRAPHY was then read too, 2026-08-21,
  and every one of block 1's 229 entries matches the transcription** — name,
  sex letter, age, clan, vital note and cross-reference, ids 1–229, read off
  the scan column by column at 4x with 6–7x confirmation on nine mark-dense
  names. **Nothing was corrected, and no reading is now owed on this plate.**
  Two things that pass are worth not re-finding: 27's death note is set
  `d .1917.` with the point after the *d* displaced, which is compositor
  spacing and not a character the data gets wrong; and **153 carries a mixed
  record on purpose** — the spelling of her first occurrence with the age from
  her second, exactly as her `plate_note` says, because the plate prints her
  twice and differently. The one thing this pass could NOT settle is a glyph
  the scan cannot resolve at all: see the magnification floor, and the five
  U+02BD instances that a photograph, not a bigger crop, closed.
  **Both of block 2's errors were Parrot throughout** — 230, 232, 236, 238, 8
  and all five children — so this is the third time clan descent has been
  unable to see a placement error, after Genealogy IV's Bear and Genealogy
  II's 31. When a mother and her candidate alternative share a clan, assume
  **no** structural check is watching.
- **Genealogy II is published and its reading is closed.** The user re-checked
  their full list on 2026-07-30 and reported **no remaining placement errors**.
  Everything they had flagged is resolved: **31, 32 and 97** via
  `UNATTACHED_BLOCKS`; **49 under 47** confirmed; **154+155 and 232+233** moved
  to their printed columns via `root_columns`; **169's two brackets** via
  `SECOND_VISIT_OMITTED`; **U52**, **U60** and **254's descent from 235+236**
  verified against the plate. Do not re-open any of these.
  **116–118's paternity IS encoded, as of 2026-07-30 (later the same day), and
  49 is the father.** It was declined earlier that day for one reason only —
  METHOD.md requires every attributed row to be daggered to a footnote, and no
  source for it had been found in Parsons's text. **The user found the source:
  p. 195**, where she records of "Gen. II, 47" that his sheep and fields passed
  to his widow for want of offspring. That names 47 as having died childless, so
  116–118 are not his, and 49 is the only other husband the plate gives 48. Her
  sentence also corroborates the plate independently — it has 47 dead and 48
  surviving him, which is what the plate's `d.` on 47 says.
  Encoded as `TABLES["ii"]["paternity"]`, apparatus only; **the chart still draws
  the plate's own fatherless bracket under 48** and its markup is byte-identical
  to before. The general rule that produced the earlier decision is unchanged and
  was *satisfied*, not waived — **an attribution that cannot be footnoted is not
  made.** Note the consequence for the leak gate: quoting Parsons trips
  `RESEARCH_PROSE` on her word "widow", so the exact phrase is allowlisted in
  `RESEARCH_PROSE_ALLOWED`. **Allowlist the phrase; never loosen the pattern.**
  This is the edition's **second** editorial attribution and the first with a
  citable source — see METHOD.md's rule 4, which now distinguishes the two cases.
  Two things about this plate the other two do not prepare you for:
  it runs to **six generations** and **274 numbers for 275 people**, and **its
  numbering is not a unique key** — Parsons numbers two different people 101.

## Working style

Report what was measured, not what was attempted. Flag uncertain readings
explicitly rather than burying them.

**Measure a bracket against the first `.line` in the group, never the first
`.node`.** They are not the same element and the difference is exactly the bug
worth finding. When two sibling groups claim one `mother_row`, `Chart.render`
pushes the mother's line down with `line_pad` — a margin *inside* the block. The
node's top stays where it belongs, so a node-to-node measurement reads 0px while
the name itself sits a row lower and the stub points at empty space. That is how
"all 55 brackets on their mother's line, max 0.016px" was reported for a page
that had one a full 24.8px out — person 169, **since fixed** by
`SECOND_VISIT_OMITTED`, and named here for the measuring mistake, not as an open
defect.

**And derive the expected leader from the TRANSCRIPTION, never from the DOM.**
The same defect has a second disguise, found 2026-08-10. An audit that matches
each bracket to the **nearest** `.lead-line` and measures the gap reports 0.00px
for a bracket hanging off the *wrong row* — the nearest line is whichever one it
landed on, so the check is circular and passes on exactly the case it exists to
catch. It reported all four plates clean while Genealogy IV drew 20 as 6+7's
child. The audit that works reads `_GROUPS`, takes the union's mother (or the
`LEADER_ON_SPOUSE_ROW` spouse), finds `#p{first_child}`, walks up to its
`.kids`, and asserts the bracket starts on **that named person's** line. 426
checks across four plates, and it is cheap.

**There is now a rig that measures the PLATE instead of the page —
`scripts/plate_audit/`, added 2026-08-17.** It reads a plate's bracket
verticals, the stubs entering each from the right and the leaders entering from
the left, at 1:1 off a raw BMP, and holds them against `_GROUPS`. That is the
one reference the DOM audit cannot have. It decides child counts per group, how
many verticals a column carries at all, and which row each leader hangs off;
it **cannot read type**, so a group of the right size whose members are
misnumbered passes and a human still reads the crops. Validated on Genealogy IV
with 20 restored to the 6+7 union — it names that defect and is silent on the
corrected data, and on **Genealogy III, where it found two real placement
errors in block 2** on 2026-08-17. **Its parameters are per plate and do not
transfer**: the test is that the stub-to-stub gaps hold **nothing below one
row** (Table 1: 144–148 × 65, 290–292 × 5; Table 3: 24–26 × 43, 49–51 × 19)
rather than spraying sub-row, and an uncalibrated run produces confident flags
that are the rig's own noise. Read its README before trusting a number from it.
**All three transcribed plates it has been pointed at are now calibrated there**
— Table 1, Table 3 and, since 2026-08-18, **Table 4** (144–148 × 27,
290–292 × 2, then a sparse tail).

**Table 4's calibration overturned what this file predicted would be wrong, and
the lesson generalises: the row pitch is rarely the problem.** It measured
145.8 against Table 1's default of 146.6, half a percent apart. What was wrong
was **the band**. A full-width band — which Table 3 tolerates — reads that
plate's own printed verticals at x 2850–2975 and 7704–7789 as brackets, one of
them a 3306px run carrying **74 "stubs" 12px apart**, and that is the entire
sub-row spray previously blamed on ink fragmentation. Two further band rules
came out of it, both cheap to re-lose:

- **A band must hold the rule PLUS the 110px stub reach on BOTH sides.**
  `stubs()` gives up when the remaining width is under 0.6 of the reach, so a
  230px band cost `V05` **all five** of its stubs and reported zero on a bracket
  that plainly has five — which looks exactly like an ink problem and is not.
- **`--overshoot` widens the LEFT side only**, so it cannot rescue a *stub*
  that sits above a rule's detected top. On Table 4 that is `V01`, whose
  vertical runs y 716–5995 with its two children **36 rows apart**; the rig
  starts it at 845 and reads the top stub as a *leader*. `V01` then pairs by
  position, takes `V11`'s bracket, and the displacement cascades into `V11` and
  `V03` — four of Table 4's ten problems from one missing stub.

**Table 4 SKEWS where Table 3 bows** — x 3195 at y 722 to 3132 at y 5800,
near-constant at −0.012 px per px of y. So `--skew` finally has a plate its
linear model describes, even though `--track=1` absorbs it and the flag is
still not passed.

**And its four constant ~+175px leader flags are the four Johnsons**, not the
plate: 8, 10, 15 and 17 carry an English name printed on its **own row**, so
each wife sits two rows under her husband where the audit's model assumes one.
Its two count disagreements are the plate collapsing `36-43. 8 children
deceased` and `50-53. 4 children deceased` onto one line each, both already in
`PLATE_NOTES`. **All ten are explained and none is a defect**, so Table 4 is a
known-clean baseline exactly as Table 3's fifteen are: diff the list, don't
read it fresh.

**Three things about that calibration are worth knowing before touching another
plate**, because each is a property of a scan rather than a threshold. A plate
can **bow** rather than skew — Table 3's left-hand rule runs x 683, 686, 666,
671 down its length, which no straight line and no fixed window follows, and
`--track` re-centres a rule's own window a pixel a row. A **fold crease can
cross a bracket column** — Table 3's third runs 10px from column 6's brackets,
so no x window separates them and `--maxthick` / `--ongrid` do it instead, on
the grounds that a crease blots 15–94 rows deep where a stub is 2–4 and lands
off the row grid. And **columns are not necessarily a grid**: Table 3's column
6 carries brackets at x 2786 *and* 2854, both real, each 61–63px left of its
own children.

**The audit pairs a bracket to the group whose MOTHER stands on its leader, and
that is deliberate even though it makes the leader test tautological.** Pairing
by `_GROUPS` order is what hid block 2's two errors — one displacement mispairs
everything after it, so the run reported them as "W23: plate 5, transcription
2" beside "W24: plate 2, transcription 5" and both were dismissed as noise.
What the identity pairing buys is three tests with teeth: **mismatched child
counts** (which is what found both errors, and the leader test found neither),
a bracket **no group claims**, and a group with **no bracket**. A pairing it
cannot make by identity falls back to position and **says so in the output** —
treat those lines as guesses, because that is exactly the basis that produced
the false alarms.

**A mother with no stub of her own cannot be anchored, and a LATER WIFE is the
case that bites.** The plate sets a second wife below the whole of her
husband's earlier issue — Genealogy III's 19 at y 3186, his second wife 21 at
y 3955, 31 rows, not one. Placing her one row under him puts her on the first
wife's row, where she loses the bracket to the group genuinely there and then
passes no rows to her own children, so every group they mother falls to a
guess: one wrong offset cost eight of nine flags. `UNIONS`'s fifth field is the
husband's marriage number and is what settles it.

**An audit that compares two things which MOVE TOGETHER passes on the defect it
exists to catch.** Found 2026-08-10 on `/search/`, and it is the same failure as
the nearest-`.lead-line` audit above wearing different clothes. The check was
"does each data cell sit at its column heading's left edge?" — it reported
**0.00px drift at every width** while the header's five columns were sliding
straight under `Table · #`, because heading and cell overflowed *by the same
amount* and the difference stayed zero. A screenshot found it in one look. So
when an audit compares A to B, ask what happens if A and B are wrong in the
same direction; if the answer is "it passes", the audit needs a **third,
independent** reference — here, the neighbour the pair was colliding with. And
**look at the thing at least once**: two measurements agreeing is not evidence
they are right.

**Under CSS `zoom`, never mix `getComputedStyle` with `getBoundingClientRect`.**
The plate scale control is `zoom`, and computed styles come back **unzoomed**
while rects come back **zoomed**. Adding a pseudo-element's computed `top` to an
element's rect therefore fabricates a constant error of exactly
`v − v × zoom` — with `top:12.4px` that is 1.86px at 85% and 3.72px at 70%, and
it looks precisely like a real misalignment that gets worse as you zoom out. It
cost an hour on 2026-08-10 and nearly convicted the Scale control. Measure
alignment from **element rects only**. The honest test that Scale is innocent is
that the error **normalised to rows** is identical at 100%, 85% and 70%.

**Check the built file, not only the rendered page.** A DOM read in the browser
happens after the page's own script has run, so it cannot see what the HTML
ships. That is how `Theme: Auto` survived a check that reported no "Auto"
anywhere: `applyTheme()` had already rewritten the label. For anything that
exists in the markup — labels, attributes, structured data, the leak markers —
grep `docs/`. The source scans in `sources/` are usually
the fastest authority — faster than catalog records, which describe publications
rather than plates.

**Never read structure off a downscaled plate.** A whole-plate overview is for
orientation and tile planning only. Genealogy II's overview appeared to show
three founding couples in its **left column**; at native resolution that column
has one, and 5 and 7 sit in the same column as 3, all carried by a single rule
off person 1's row. (The plate *as a whole* has three descent blocks — 1+2,
154+155, 232+233 — which is a different claim about a different part of the
plate. 31+32 was counted as a fourth until 2026-07-30; it is a couple the plate
prints *inside* the first block, not a block of its own — see below.) A
downscale loses exactly the thin rules that carry the genealogy, so it will
misplace people while looking perfectly legible.

**Indentation does not establish descent — a leader stub does.** On Genealogy II
this cost three near-misses, so treat it as the rule and not the exception:
232+233 and 31+32 both sit at exactly a child's indent, and 31 sits at that
indent *inside another bracket's vertical extent*. What says they are not
children is the **absence of a horizontal stub** joining the vertical rule to
their row. Read the bracket column as its own narrow strip — 260–320px, so the
vertical and every stub entering it are the only things in frame — and count the
stubs. The clan check will not save you here: 31 is Water exactly as the couple
whose bracket he sits inside are.

**"Not a child" and "not drawn here" are two different findings, and the second
one has its own mechanism.** Reading the missing stub correctly still left 31 in
the wrong place on the page for a whole session, because the only way an
unreachable person got drawn at all was to make him a **root** — and a root is
drawn at generation 1, at the far left, four columns from where the plate sets
him. The block was right and its position was not, which no structural check can
see and no clan can contradict. `UNATTACHED_BLOCKS` in a transcription module is
now the mechanism: it names the union, the partner the plate sets on the upper
line, the child column it is printed in and the child it is printed after, and
the renderer splices the block into that column and **withholds only the leader
stub** (`.kids > .node.unattached::before`). The vertical still passes the row,
as it does on the plate. Reach for it whenever the plate *prints* a couple
somewhere it does not *descend* them. An entry is validated by
`self_check()`, which also forbids splicing after a column's **last** child —
the bracket's bottom terminus is drawn from DOM position, so the rule would then
run past its own last child.

**A root is not automatically at the left margin, and that is a third case
again.** `roots` draws a block at generation 1. That is right for a block the
plate starts at the sheet's left edge and wrong for one it merely *indents*,
which is what Genealogy II does twice: measured on the scan 2026-07-30, person 1
sits at x 225 and person 3 — generation 2 — at x 1425, while the lower block's
154 sits at x 1340 and 232 at x 2690, the same column as 164, who is 154+155's
own child. `spec["root_columns"]` in `TABLES` sets the starting column
(`{154: 2, 232: 3}`), applied as a `margin-inline-start` on the `.tree` stated
in `--col`/`--stub`, so generation *d* still lands at *d* × (`--col` + `--stub`)
and drift stays 0 — verified at 425.59px step, spread ≤ 0.008px across all six.
**Do not reach for `UNATTACHED_BLOCKS` here**: the lower block is not descended
from the upper one, so splicing would assert a containment the plate does not,
and it would hit the last-child rule anyway, because the plate's vertical ends
*on* 164 with nothing beside 232 at all (bracket-column strip x 2480, y 9900).
The independent check that these two columns are right is that the `generation`
field — derived by walking the tree, never read off the plate — already stored
2 and 3 for them.

**A half-read plate is never registered in `TABLES`.** The renderer builds every
registered table on every `--public` run, so registering early is how a partial
genealogy reaches `docs/`. Register at Gate 5, after `self_check()` passes —
never before, as a way of previewing progress.
