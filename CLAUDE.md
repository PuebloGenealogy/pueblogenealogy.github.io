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
58 parent–child links, 4 generations. `--public` builds **6 pages** and the live
site serves all of them; `PENDING` is empty.

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
    holds **two kinds** of entry, and the distinction matters — three FAQ
    sentences that *state* the privacy boundary, and (added 2026-07-30) one
    quotation from **Parsons's own 1923 text**, in Genealogy II's
    `note-paternity`, where her word "widow" is the source speaking and not
    research escaping. **Allowlist the exact phrase; never loosen the
    pattern** — and keep the phrase off a source-line break, since the check is
    an exact substring replace against the rendered HTML
- `check_published_pages()` sweeps **every** `.html` in `docs/`. The per-table
  check only ever saw table pages, so the landing page — the one carrying the
  FAQ — went unchecked entirely until 2026-07-28

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
invalid structured data, a research-data leak, or **any person in `PERSONS` that
the page does not draw**. That last gate was added 2026-07-30: an undrawn person
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
| `.zenodo.json` | Metadata for the archived deposit. Read from the **tagged commit**, so it must land on `main` before a release is cut |
| `CITATION.cff` | How to cite. Carries the concept doi plus both dois under `identifiers` |

Identity is three constants at the top of `make_chart.py`: `SITE`, `REPO` and
`DOI`. Every canonical, sitemap entry and card derives from them. `DOI` is the
Zenodo **concept** doi, which always resolves to the newest release — never
hard-code a version doi here, or every citation printed on the site rots at the
next release.

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

One thing that will look like a bug and isn't: below 26rem the word "Genealogy"
in the table pills is visually hidden but kept in the accessible name, so the
sticky bar stays two rows on a phone.

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

**The theme control has no Auto state.** It toggles Light ↔ Dark and the button
always names a real palette. The system preference is still honoured: it is what
a first visit resolves to, and no choice is written to storage until the reader
presses the button, so an untouched control keeps following the OS.

The footer apparatus is a **two-column grid of `.app-sec` sections** at
`--measure-wide`, collapsing to one column below 56rem. Grid of whole sections,
not CSS multicolumn — multicolumn will break a heading away from the list it
introduces. This is also what puts the footer on the same left edge as the
register above it.

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
repo and not deployed — builds its whole index by fetching the four
`genealogy-*/` pages and parsing them. It reads no transcription module. So
some of what `make_chart.py` emits is now **consumed by something other than a
browser**, and changing it silently breaks a reader elsewhere:

| Hook | What is read from it |
|---|---|
| `<li class="reg" id="rN">` | one person; `N` is the **id** |
| `.num` `href="#pN"` + its text | the id and the **printed number**, the distinction that matters |
| `.sex` `.name` `.alt` `.blank` `.age` `.clan` `.vital` | the fields |
| `sic-ring` on `.sex` / `.clan` | that the value is the plate's misprint |
| `.reg-rel[data-rel]`, `data-with`, `data-editorial`, `a.edmark` | every relation, and which attribution is editorial |
| `.node` nesting depth, plus `.tree`'s `margin-inline-start` multiplier | **generation** — the register does not print it |
| `.xref` directly after a `.line#pN` | that person's cross-reference; `xref-cell` belongs to nobody |

Two consequences that are not obvious:

- **`dotted()` is not reversible, and one value is already lost.** It appends a
  period "unless the value already ends in one", so `d. in childhood.` and
  `d. in infancy` render identically. A parser cannot tell them apart; II·50
  reads back one period short. Nothing on this site is wrong — this is a cost
  paid by the consumer, recorded so nobody hunts it as a bug.
- **The reading behind a misprint is not published.** `sic-ring` marks that
  the printed sex or clan is wrong but never says what the transcription holds,
  so a consumer can show the misprint and cannot recover the reading. If that
  ever matters, the fix here is a `data-reading` attribute, not a change to
  what is displayed.

None of this constrains the edition's design — it constrains **silent** change.
Restructure the register freely; just expect `laguna-search` to need its parser
updated, and run its `tools/validate.py`, which compares all 713 entries and
every relation against `scripts/transcription*.py`.

## Two names cannot be found by their own plate's `fold()`

**Found 2026-08-03; not fixed, because it is a defect in this repo's data.**
The four transcription modules each carry their own `_FOLD` map and they are
**not identical**: only `transcription_ii.py` maps `ŏ` and `Ĭ`. Two names on
other plates carry those characters, so their own plate's `fold()` leaves the
diacritic in the key:

- `Dziŏ˙kwid˙yuʼă` — Genealogy III, 101
- `Ĭya˙ʼsi` — Genealogy III, 16

`fold()` is documented as a "diacritic-free lowercase key", and for these two it
is not one. Nothing on the site uses `fold()` today, so nothing is visibly
broken; the Find box keys on names and numbers directly. The fix is to give all
four modules the union of the maps. It is a one-line edit per module and it
changes no rendered output — but it touches four files that are otherwise
immutable, so it wants a deliberate decision rather than a drive-by.

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
  person 31, who is Water exactly as the couple whose bracket he sits inside.
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
  **No gate can see this defect.** The build reported all 261 drawn and 0 px
  column drift, and both were true — drift measures *columns*. The check that
  finds it is **"is any node's first `.line` displaced from that node's top?"**,
  in the browser, over every `.node`. Run it on any new plate.
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
  sits on the line of the parent whose marriage the group belongs to, so a
  spouse with no leader had no recorded issue. 85/86/87 is Table 1's 83–85 shape
  and still needs no attribution, because 86's leader is on her own line and 87
  has none. Don't reach for the attribution machinery on this plate.
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

`_backup-v1-laguna-genealogy-tables-2026-07-27/`, one level up, is the **sole
surviving copy** of the deleted v1 repo. Do not clean it up as stale.

## State

Site live and indexed-submitted; Search Console and Bing both verified;
structured data valid and guarded at build time. v1 is deleted.

**Archived at Zenodo**, concept doi `10.5281/zenodo.21637900`, first release
`v1.0.0` (2026-07-28). The doi appears in `CITATION.cff`, the README badge, the
**footer** citation block on every table page (`cite_html()` — the title-page
citation was removed on 2026-07-28 and never carried the doi), and as
`identifier` in the JSON-LD —
`Dataset` on the table pages, `CollectionPage` on the landing page, which is
the entity the deposit actually corresponds to. Archiving is automatic from now
on: Zenodo's webhook is on the repo, so **cutting a GitHub release mints a new
version doi**. `.zenodo.json` controls the record's metadata; without it Zenodo
would title the deposit after the repo.

### Release policy — set by the user 2026-07-30

**During active development: commit to `main`, cut no GitHub Releases, make no
Zenodo deposits.** The site keeps deploying from `main` as it always has;
publishing the site and cutting a release are different acts, and only the
second one touches Zenodo.

**The next release happens only when all four genealogy tables, the design, the
transcriptions, the text and the citations are finalized.** Then: one GitHub
Release, let the webhook archive it, and the **concept doi** stays the one on the
website.

The objective is to publish only stable, citation-ready editions and to avoid
minting permanent Zenodo versions that mark nothing. **Published Zenodo records
cannot be deleted** — every version is permanent and public — which is why
restraint here is the correct posture and not fussiness.

Consequences a session must not "fix":

- **The archive lags the site on purpose.** v1.0.0 archives Genealogies I and IV
  only, so the concept doi in every page footer currently resolves to a record
  without Genealogy II. That is the accepted cost of the policy, not a bug.
- **`CITATION.cff` describes the newest *minted* release**, `v1.0.0` /
  `2026-07-28` — never a planned one. It said `v1.1.0` / `2026-07-30` until this
  policy was set, which advertised a version nobody could resolve in the widget
  GitHub renders from that file. Do not bump it in anticipation of a tag.
- **The abstract may describe more plates than the release contains.** That is
  correct: the abstract describes the *work*, the version fields describe the
  *release*.
- **`.zenodo.json` is read from the tagged commit**, so bring it up to all four
  tables as part of cutting the final release — not before, and not as a
  standalone task.
- When the release is finally cut, add its version doi to `identifiers`
  *after* the webhook mints it. **Never guess a version doi**; the suffix is not
  reliably sequential from v1.0.0's.

**Outstanding:**
- **Inbound links** — a fresh `*.github.io` has no authority, and no on-page
  work substitutes. Zenodo is done and is itself the first such link. Next, by
  effort-to-return: a **Wikidata** item (heavily crawled, feeds Knowledge Graph,
  none of Wikipedia's conflict-of-interest friction), then the Wikipedia *Elsie
  Clews Parsons* external links — **propose on the Talk page**, since adding a
  link to one's own work is a COI and tends to be reverted — then the AMNH
  Digital Library, which hosts the original.
  **The Wikidata payload is `wikidata-quickstatements.txt`**, current for all
  four tables and ready to run as a `CREATE` batch; only the user can run it,
  because QuickStatements needs their OAuth login. Three things about it are
  decisions, not defaults, and re-deriving them wastes a session: `P2093` author
  name string rather than `P50`, which would require creating a biographical
  item about a living person; `P144` based on → `Q51498010`, the existing item
  for Parsons's 1923 article, so the new item joins the graph instead of
  dangling, and reaches her authorship through it; and **no counts of
  individuals**, which would be an uncheckable copy of numbers the site computes
  from the transcriptions. **Never put a backslash-escaped quote in that file** —
  QuickStatements V1 splits on tabs and strips the surrounding quote pair rather
  than honouring an escape, so use typographic quotes inside a value.
  **The AMNH handle is `2246/158`** — `https://digitallibrary.amnh.org/handle/2246/158`,
  found 2026-07-30. That is the identifier `.zenodo.json` omits from
  `related_identifiers`; add it when that file is brought to four tables for the
  release, not as a standalone edit. Note `digitallibrary.amnh.org` **403s
  automated fetches** — use a real browser, not `WebFetch`.
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
  added to this repo; the Search Console and Bing properties stay as verified;
  and **inbound links may now be seeded freely** — the "decide before seeding
  any inbound link" gate that used to sit on Wikidata and AMNH is **lifted**.
- **No release is outstanding, and that is still deliberate.** v1.1.0 was
  prepared and then **cancelled** by the release policy above: no GitHub
  Releases and no Zenodo deposits during active development. **All four plates
  are now published** (2026-07-31), and **Genealogy III's two editorial items
  are both closed** — same day, later session: the cross-reference footnote is
  written and **deployed** (`#note-crossref`, verified live by SHA-256), and
  the turned-comma mark is settled as unresolvable from this scan. So **two**
  of the policy's four clauses are met.
  The other two are not: `.zenodo.json` still describes three plates, and the
  AMNH handle is still absent from its `related_identifiers`. **Publishing the site
  is not releasing it.** Do not read "the last plate is up" as "cut the tag";
  when it is finally wanted, `.zenodo.json` must already be on `main` and
  current for all four tables, because Zenodo reads it from the tagged commit.
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
that had one a full 24.8px out (person 169, still open).

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
