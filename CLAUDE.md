# Laguna Genealogies — project context

A digital edition of the genealogical plates published with Elsie Clews Parsons,
**"Laguna Genealogies"**, *Anthropological Papers of the American Museum of
Natural History*, vol. 19, pt. 5 (1923), pp. 133–292.

**Live:** https://pueblogenealogy.github.io/ · **Repo:**
`PuebloGenealogy/pueblogenealogy.github.io` (public) · Pages from `main` /
`/docs`, HTTPS enforced.

Published, **three plates, 452 individuals** (PR #14 merged 2026-07-30):
**Genealogy I** (Table 1) — 104 individuals, 27 marriages, 80 parent–child
links, 5 generations. **Genealogy II** (Table 2) — 275 individuals for the
plate's 274 numbers, 61 marriages, 214 parent–child links, **6 generations**,
three descent blocks. **Genealogy IV** (Table 4) — 73 individuals, 14 marriages,
58 parent–child links, 4 generations. `--public` builds **5 pages** and the live
site serves all of them. Genealogy III is scanned and untouched.

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
    scripts are not. Three FAQ sentences that state the privacy boundary are
    allowlisted by exact phrase, so it **fails closed**: reword the FAQ and the
    build stops until the new wording is allowlisted
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
- **Editorial attribution exists, and 83–85 is the only case** (added
  2026-07-28). Person 68 has two husbands, 69 and 70; the plate's bracket does
  not say which marriage her children belong to, so `transcription.py` records
  no father and **the chart draws the plate's single bracket**. The *apparatus*
  splits them — 83, 84 to 69; 85 to 70 — from `TABLES["i"]["paternity"]`,
  marked with a dagger linking to `#note-paternity`. Read METHOD.md's
  *Editorial attribution* before adding another: four rules govern it, and the
  first is that the chart never carries it. The supporting evidence is external
  documentary research and **must not enter the repo** — the footnote says a
  reading rests on evidence outside the plate and stops there. Note this is the
  first time the edition asserts anything the plate does not; it is not a
  precedent for "improving" the chart.
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
- Google's structured-data validator is **stricter than schema.org** — valid
  schema.org has been rejected twice here. `check_structured_data()` guards the
  rules we have been told about, not all of them; a Search Console report
  outranks the build's opinion.

## Environment

macOS, Python 3.11. openpyxl 3.1.5, fontTools 4.63.0 + brotli. `gh` 2.96.0 at
`~/.local/bin/gh`, authenticated as `prettyph3nom`, owner of the
`PuebloGenealogy` org. **No Homebrew, no ImageMagick, no PIL** — use `sips`.

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
would title the deposit after the repo. **`.zenodo.json` and `CITATION.cff` were
brought up to three tables on 2026-07-30**, ahead of the release, because Zenodo
reads them from the *tagged commit* and not from `main`'s tip. `CITATION.cff`
now says `v1.1.0` / `2026-07-30` — **correct that date before tagging if the
release slips to another day**, and add v1.1.0's version doi to `identifiers`
*after* the webhook mints it. **Never guess a version doi**; the suffix is not
reliably sequential from v1.0.0's.

**Outstanding:**
- **Inbound links** — a fresh `*.github.io` has no authority, and no on-page
  work substitutes. Zenodo is done and is itself the first such link. Next, by
  effort-to-return: a **Wikidata** item (heavily crawled, feeds Knowledge Graph,
  none of Wikipedia's conflict-of-interest friction), then the Wikipedia *Elsie
  Clews Parsons* external links — **propose on the Talk page**, since adding a
  link to one's own work is a COI and tends to be reverted — then the AMNH
  Digital Library, which hosts the original and could also supply the handle
  `.zenodo.json` currently omits from `related_identifiers`.
- **Custom domain** — **currently decided against**; listed here because it is
  not closed, only deferred. The reasoning is the paragraph below, which used to
  point at `SESSION-NOTES.md` and no longer does: that file is overwritten every
  session and had already lost it.
  **Decide it before seeding any inbound links.** Every
  link and citation placed from now on points permanently at whatever host is
  chosen, and most will never be updated. Note the old framing of this as "the
  strongest SEO upgrade" overstated it: Google treats `github.io` as a public
  suffix, so no authority is inherited from it and none is lost by leaving. The
  real argument is citation permanence and portability — a domain you own can
  change hosts without breaking a doi-adjacent link — which is an argument for
  doing it first or not at all. Drops onto this repo via a `CNAME` file.
- **PR #15 is open and the live FAQ is wrong until it lands.** Branch
  `fix-faq-three-tables`. Two landing-page answers, in the visible copy *and*
  the `FAQPage` JSON-LD: one still says Tables 2 and 3 are "not yet
  transcribed", the other still claims the clan check "independently verifies
  each bracket reading". Not merged because that is a second live deployment
  and only PR #14 was authorised — **ask, then merge and re-verify by
  SHA-256.**
- **The v1.1.0 release has not been cut.** Metadata is ready; see the Zenodo
  paragraph above for the date and version-doi traps.
- **Genealogy II is published and its reading is closed.** The user re-checked
  their full list on 2026-07-30 and reported **no remaining placement errors**.
  Everything they had flagged is resolved: **31, 32 and 97** via
  `UNATTACHED_BLOCKS`; **49 under 47** confirmed; **154+155 and 232+233** moved
  to their printed columns via `root_columns`; **169's two brackets** via
  `SECOND_VISIT_OMITTED`; **U52**, **U60** and **254's descent from 235+236**
  verified against the plate. Do not re-open any of these.
  **116–118's paternity is NOT encoded, by decision (2026-07-30).** It was
  going to be a second editorial attribution naming 49 as the father, but
  METHOD.md requires every such row to be daggered to a footnote, no source for
  it was identified in Parsons's text, and the user asked for no footnote and no
  editorial note. So the chart draws the plate's own fatherless bracket under 48
  and asserts nothing. Do not re-open this as an oversight; and note the general
  rule it illustrates — **an attribution that cannot be footnoted is not made.**
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
