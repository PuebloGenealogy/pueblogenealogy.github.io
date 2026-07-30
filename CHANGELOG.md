# Changelog

What changed, when, and anything a future session would otherwise re-derive.
Newest first.

## 2026-07-30 (later) — Genealogy II published: reading settled, PR #14 merged, live

**The edition now serves three plates.** The user re-checked their placement
list and reported **no remaining placement errors**, which closed the thread the
previous two sessions were blocked on. PR #14 merged as `04ded51` and deployed.

### Claims in the entry below that this session falsified

- **"Person 169's bracket is a full `--lh` out. Still open" → fixed**, and the
  cause was ours, not a layout bug. See below.
- **"`roots` is for a genuinely separate block at the left margin"** — too
  strong. A root can be a separate block that the plate merely *indents*, which
  is what Genealogy II does twice. `root_columns` is the new mechanism.
- **"Clan descent … independently checks every bracket reading"** was still live
  in **three** places outside `CLAUDE.md`, which had already corrected it:
  `.zenodo.json`, `CITATION.cff`, and the landing-page FAQ. All three now say
  what the check actually does — it discriminates only where the possible
  mothers belong to different clans. This is the third session to find a copy of
  this sentence; if another turns up, that is why.

### 169's two brackets — the renderer was drawing a marriage the plate does not

Her bracket was one `--lh` out because she has two husbands **and is the mother
of both groups**, so `u["wife"] == pid` gave both `mother_row = 0`. Two brackets
cannot begin on one line, so `line_pad` pushed her own line down to meet the
second group and stranded the first.

Parsons has no such problem, because she prints 169 **twice, one marriage
each** — under 156+157 as 168's wife bracketing 196–200, and under 164+165 as
her parents' daughter bracketing 225, 226 — and **the second occurrence prints
no `+ 168` line at all**. Read at x 3650 y 7500 and x 3650 y 9700, 1500px wide.
So the collision was self-inflicted: the renderer printed a marriage in a block
where the plate prints none.

`SECOND_VISIT_OMITTED` in `make_chart.py` suppresses the `+` line, the bracket
and the child-column note, and prints the plate's own cross-reference row
instead, held back until the block's other union lines are down because that is
where the plate sets it. **Both occurrences now measure 0px.**

**This is not Table 1's person 8** and must not be merged with him: he has two
*different* wives, 7 and 73, two distinct `mother_row`s, and nothing collides.
That is `SECOND_VISIT_NOTE`, and it is untouched.

### The roots were at the left margin; the plate only indents them

Measured on the scan: person 1 at x 225, person 3 — generation 2 — at x 1425,
while the lower block's **154 sits at x 1340** (person 3's column) and **232 at
x 2690**, the same column as 164, who is 154+155's own child. All three roots
were being drawn at generation 1.

`spec["root_columns"] = {154: 2, 232: 3}` indents the `.tree` in the grid's own
`--col`/`--stub` tokens. **Deliberately not `UNATTACHED_BLOCKS`**: the lower
block is not descended from the upper one, so splicing would assert a
containment the plate does not, and it would hit `self_check()`'s last-child
rule anyway — the bracket-column strip at x 2480, y 9900 shows 154+155's
vertical ending *on* 164 with nothing beside 232 at all. The independent check
is that the `generation` field, derived by walking the tree and never read off
the plate, had already stored 2 and 3.

### Verified at the user's request, no change needed

**254's descent from 235+236** — strip x 4720, y 11400: 236's leader rule meets
the vertical at its top corner, which is 254's own row, and a stub enters there.
The vertical runs to 260 and terminates. Stubs enter 254, 255, 256, 258, 259,
260; **257 takes none**. The 255 anomaly stands as recorded — he takes a stub
although he is a `+` line, and he is Eagle where every child on that bracket is
Water, so it is not descent. **U52 (234+54)** and **U60 (254+255)** also
confirmed.

### 116–118's paternity is deliberately NOT encoded

It was specified as METHOD.md's second editorial attribution, naming 49 as the
father. It is not being made. METHOD.md requires every such row to be daggered
to a footnote; **no source for it was identified in Parsons's text**, and the
user asked for no footnote and no editorial note. The chart therefore draws the
plate's own fatherless bracket under 48 and asserts nothing. The general rule,
now in `CLAUDE.md`: **an attribution that cannot be footnoted is not made.**
Do not re-open this as an oversight.

### Release metadata brought to three tables

`.zenodo.json` and `CITATION.cff` described a two-table edition, and Zenodo
reads both from the **tagged commit**. Both now describe three plates and 452
individuals. `CITATION.cff` goes to **`v1.1.0` / `2026-07-30`** — a plate is
additive, hence the minor bump. **v1.1.0's version DOI is deliberately absent**:
it does not exist until Zenodo's webhook fires on the release, and it cannot be
guessed from v1.0.0's. `README.md`'s plate table gained Table 2.

### Published and verified

Merged, deployed, and checked **by SHA-256 against the live URLs** — the Pages
build API misreports the deployed commit, so hashes are the only real check. All
four pages byte-identical to `main`, HTTP 200, sitemap carrying four URLs.
Privacy sweep of the **live** pages: no `class="eng"`/`class="census"`, no
research vocabulary; the only `census` occurrences are the three allowlisted
FAQ sentences that state the boundary itself.

### Found by checking the live site, not the build — PR #15, OPEN

The landing-page FAQ was stale in two answers, in the visible copy **and** the
`FAQPage` JSON-LD:

- it still said **"Tables 2 and 3 … are not yet transcribed"**, shipped by the
  very release that publishes Genealogy II;
- it still claimed the clan check **"independently verifies each bracket
  reading"**.

Both fixed on branch `fix-faq-three-tables` and merged as **`f9e50c2`** once the
user authorised the second deployment, then re-verified live by SHA-256. The
privacy allowlist is untouched, so the gate still fails closed on a reword.

**The lesson, since this is the second time it has paid off:** the build gate
inspects `docs/`, but only a fetch of the live page proves what a reader gets.
Grep the built file for markup; fetch the live URL for truth.

### Measured, 1280×900

Column drift spread **≤ 0.008px across all six generations**, step 425.59px. 57
bracket groups, **worst 0.023px** (the pre-existing sub-pixel 158→126). **0 rows
off the `--lh` grid.** 0px body sideways scroll at desktop *and* mobile. Ruler
labels 425.6px apart, still tracking the grid. All three `self_check()`s pass;
`--public` exits 0 at 275/275 persons and 8 valid JSON-LD blocks. Tables 1 and 4
and the landing page byte-identical through the Table 2 work.

## 2026-07-30 — 31+32+97 drawn where the plate prints them, not at the left margin

The first of the user's reported placement errors, resolved. **The data was
right and the drawing was wrong**, which is a distinction the previous session
did not have a mechanism for.

### Claims in the entry below that this session falsified

- **"Four descent blocks" → three.** 1+2, 154+155, 232+233. 31+32 is a couple
  the plate prints *inside* the first block. The page copy is computed from
  `len(roots)` and now reads "three descent blocks / three founding couples".
- **"All 55 sibling brackets on their mother's line, max 0.016px" → 54 of 55.**
  Person **169**'s bracket is a full `--lh` (24.8px) out, and was in the
  committed build too. The measurement compared each group's first `.node` top
  against the mother's line; the displacement is *inside* the block, in
  `line_pad`, so the node top reads correct while the name sits a row lower.
  Measure the first `.line`. Still open — see below.
- **"Stubs run from the vertical rule into rows 33, 35, 36, 38 and 40"** — those
  are **two** verticals, not one. 9+10's takes 26, 29, 33 and ends at 33;
  11+12's begins at 35. It does not change any reading, but it is the strip a
  future session will re-crop.

### What changed

- **`UNATTACHED_BLOCKS`** in `scripts/transcription_ii.py` — a new plate-layout
  declaration: the union, the partner on the upper line, the child column it is
  printed in, the child it is printed after. One entry, `U17` after 29 in `U05`.
  `self_check()` validates every field and forbids splicing after a column's
  last child, which would drag the bracket's bottom terminus past its own last
  child.
- **`Chart.render` splices** that block into the column and marks the node
  `unattached`; `.kids > .node.unattached::before{display:none}` withholds the
  leader stub and nothing else, so the vertical still passes the row exactly as
  it does on the plate. Group tuples now carry their union id, which is how the
  splice knows which column it is in.
- **31 came out of `roots`.** He was there because rooting was the only way an
  unreachable person got drawn at all — but a root is drawn at generation 1, and
  the plate sets him at generation 4, between 29+30 and 33+34.
- **An undrawn person is now fatal on `--public`**, like a duplicate anchor. It
  was a console warning, which is how seven of this plate's went unnoticed
  through a whole session. The private build still only warns.
- **`#note-unattached`** added to Table 2's apparatus: a couple sitting in a
  bracket with no rule joining it is otherwise indistinguishable from a
  rendering fault.

### Measured, 1280×900

31 at left 1336.98px, identical to 29 and 33 (0px), sibling order 26, 29, **31**,
33, no stub, vertical present. Column drift **0px at all six generations**, step
425.59px. 0 rows off the `--lh` grid, 0px body overflow, register unharmed.
Tables 1 and 4 as controls: 0px drift, 0 brackets off, 0 rows off grid. Their
only diff is `dateModified`, the "Last updated" line, and the one shared CSS
rule.

### Settled with the user, and still open

49 under 47 is **correct**. **116–118's father is 49** on the authority of
Parsons's prose — to be added as an editorial attribution under METHOD.md's four
rules, apparatus only, and unlike Table 1's it can cite its source, since a
published 1923 sentence is not census research. Deferred at the user's request:
the rest of the placement-error list, **232+233**, **U52**, **U60**, and
person **169**'s bracket.

## 2026-07-29 — Genealogy II published to the branch: read, encoded, rendered, measured

**Genealogy II is complete and rendered** — 275 records for the plate's 274
numbers, 61 marriages, 214 parent–child links, **six generations**, four descent
blocks. Registered in `TABLES` as `"ii"`, so `--public` now builds **5 pages**
and reports 104 / 275 / 73 persons. Still on branch `table-ii-transcription`;
nothing is on `main` and the live site is unchanged.

Commits: `04d2deb`, `e7b2bdd`, `d8f9525`, `d657094`.

### Claims in the entry below that this session falsified

Read these before trusting anything in the previous section:

- **"Exact through its 27" and "six independent matches" → 53 and 29.** The
  cross-reference exact range reaches Genealogy I's person **53**, on 22 name
  matches, plus 7 displaced ones. Both footnotes say 53.
- **"Runs past 269 persons" → 274.** Already corrected mid-session below; noted
  again because the figure appears twice.
- **"One founding couple, not three" → FOUR descent blocks.** That claim was
  about the upper block's left column and is still true *there*. The plate as a
  whole has four: 1+2, **31+32**, 154+155, 232+233.
- **`ˑ` U+02D1 is not used on this plate at all.** Its only two sites, 142 and
  163, were misreadings; see below. `˘` U+02D8 replaces it as the one new
  codepoint.
- **Person 13's discrepancy is not "the upper marked the less certain".** Both
  settings were re-read at high magnification and both are unambiguous.
- **Person 14 is `S˙ʼiʼrowaisiwa`, not `S˙ʼĭʼrowaisiwa`** — a plain dotted i.

### Gate 1b: eleven of thirteen glyph readings were wrong

Every reading marked `SEE TODO` was re-read at 6–25× native magnification, and
each record now carries the pixel coordinates it was verified at. **Two
confirmed the earlier reading (20, 59). Eleven corrected it**, including one
that carried no marker and was found only because another was wrong the same
way:

| | was | is |
|---|---|---|
| 14 | `S˙ʼĭʼrowaisiwa` | `S˙ʼiʼrowaisiwa` |
| 21 | `Dziwaikch` | `Dziwaikch˙ʼ` |
| 45 | `Ka˙chănĭsh` | `Ka˙chănĭshʼ` |
| 52 | `Gauʼs˙inăiʼ` | `Gauʼs˙in˙ăiʼ` |
| 64 | `Kʼaisĭyăiʼ` | `Kʼais˙ĭyăiʼ` |
| 80 | `Gauʼs˙iro` | `Gauʼs˙ĭro` |
| 135 | `Săp` | `Säpʼ` |
| 142 | `Kăaiˑʼyunăiʼ` | `Kăaiʼʼyunăiʼ` |
| 146 | `Aiʼs˙iyĕ` | `Aiʼs˙iyĕʼᵉ` |
| 162 | `Da˙ʼyu` | `Da˙ʼyuʼ` |
| 163 | `Ĭyaˑʼsi` | `Ĭya˙ʼsi` |
| 170 | `Kʼuʼn˙ash` | `Kʼuʼn˙ash˘` |

**The pattern is the part worth keeping.** Nine of the eleven *dropped a mark*
rather than misidentifying one, and nearly all sit at the **end** of a name,
where a 1450px column tile renders the mark 4–6px wide with the sentence period
beside it. **A column tile is enough to read a name and never enough to read its
final mark.** Two shape confusions account for the rest, and both need a
same-magnification comparison rather than a judgement in isolation: `˙` (round,
no tail) against `ʼ` (bulb at top, tail down-left) — person 22's `Shaiyo˙ʼsi˙ĕ`
prints the pair adjacent and is the reference specimen; and a mark against the
same mark repeated, which is how 142 and 163 both became an exotic `ˑ`.

### Five defects, four of them latent in code the published plates never exercise

Registering the plate was one `TABLES` entry. Making it *correct* surfaced five
bugs, and the reason they had never fired is worth more than the fixes.

**1. Seven people were not drawn — three separate causes.** A fatherless sibling
group (one the plate brackets under a mother without saying which marriage) was
only ever looked up on a block's **primary**, so 116–118 under 48 — who has two
husbands and is printed only as a `+` line under the first — were silently
absent. Person 49 needed `drawn_under`: the plate sets `47.` / `+ 48.` / `+ 49.`
as three consecutive lines, so neither partner of 48+49 is a primary anywhere.
And **31+32+97 is a fourth descent block**: re-verified on the scan at x 3450
y 700, leader stubs enter rows 33, 35, 36, 38 and 40 and 31's row has none,
though it sits at the same indent and inside another bracket's vertical extent.
*The indent is what makes it look like a child line; the missing stub is what
says it is not.* 31 is Water exactly as 9+10 are, so the clan check could never
have caught it. **An undrawn person is reported by the build but is not an
error**, so all seven would have shipped.

**2. `.xref` rendered 21.09px against a 24.8px budget.** `Chart.render` counts a
cross-reference as `row += 1`; the CSS set `line-height:1.4` plus block padding.
Seven of Genealogy II's brackets sat **3.7px off their mother's line**. Table 1
has cross-reference rows too and measured clean — because no group there has a
mother's line *below* one. Fixed the way `.sic-row` already does it:
`line-height` is the token, block padding zero. **This does change Table 1's
published appearance**, by 3.7px per cross-reference row.

**3. `DUPLICATE_PLATE_NUMBERS` was declared and never read.** The decision to
give the second person numbered 101 a synthetic id for addressing while printing
the plate's number was recorded in `transcription_ii.py` and never implemented
in the renderer, so **`1010` — a number that appears nowhere on the plate —
printed in four places**: chart line, register entry, relation chips and the
Find suggestions. Now `p["plate_number"]` carries what is shown and `p["id"]`
stays the key. **This is not the misprint path**: there the plate is wrong and
the number is ringed in `--sic` with an annotation row; here the plate is right
and merely reuses a number, so it is set like any other, unringed.

**4. Two cross-references used `/` where the row separator is `|`** (160, 169),
so the page printed a slash the plate does not set and two statements collapsed
into one budgeted row. Genealogy I's person 73 had it right.

**5. The font subset was partly driven by `plate_note` prose** — editorial
commentary, inert in the renderer — so quoting a glyph in order to say it is
*not* on the plate shipped it. Narrowing the scan made room for a real check,
`check_against_build()`, which reads the built pages and demands every character
in them be in the subset. It immediately found **two glyphs missing, and missing
since each page shipped: `†` U+2020 and `›` U+203A**, both set from the page's
own script and therefore in no HTML template string anyone would scan. The
dagger is not decorative — it marks the single editorial attribution this
edition makes (Genealogy I, 83–85). They rendered only because macOS substitutes
silently, *the exact trap `subset_font.py` exists to prevent*.

### Measured, not eyeballed

At 1280×900, with Tables 1 and 4 re-measured as controls:

| | Table 1 | **Table 2** | Table 4 |
|---|---|---|---|
| generations | 5 | **6** | 4 |
| column drift | 0 px | **0 px** | 0 px |
| step per generation | 425.6 px | **425.6 px** | 425.6 px |
| sibling brackets | 24 at 0 px | **55 at ≤0.016 px** | 14 at 0 px |
| rows off the `--lh` grid | 0 | **0** | 0 |
| body sideways scroll | 0 px | **0 px** | 0 px |

425.6px is `--col + --stub` (26.6rem at the pinned 16px root). Nothing in this
layout had been tested past five generations before this plate.

### Decisions taken

- **The three repeat people carry BOTH of the plate's settings** (user, this
  session) — 13 `Dzia˙ʼyotsʼa (Tsiaiutsa)`, 54 `Ma˙ʼrani (Ma˙ʼran˙i)`, 125
  `Gowaʼk˙ʼd˙yăiʼ (Gowaʼkʼad˙zăiʼ)`. First occurrence in `name_as_printed`,
  second in `alt_name`. All six settings are unambiguous at magnification, so
  suppressing either would hide something the plate says. `REPEAT_PERSON_NAMES`
  declares each pair and `self_check()` holds it against the records — the pair
  otherwise lives in two places and a later edit to one would be silent.
  **The cost, accepted knowingly:** `alt_name` now carries three meanings the
  renderer cannot tell apart, all printed as `(alt)` — an English name the plate
  itself parenthesises (27, 42, 43, 140), the second half of a braced pair (14),
  and this. Only the first is parenthetical on the page. `#note-repeat-names`
  is what stops a reader taking `Ma˙ʼrani (Ma˙ʼran˙i)` for an English name.
- **Table 1's `#note-misprint` now carries Table 2's corroboration.** It said
  *what* the plate does; it can now say why 68 is Parsons's own number rather
  than a typesetter's slip. **Cross-plate person references must not go through
  `_p()`** — `_p(60)` on Table 1's page links *its* person 60, a different human
  being — so "Table 2's own person 60" is deliberately plain text and the only
  link added is the explicit `../genealogy-ii/#note-crossref`.

### Two traps for the next session

- **`subset_font.py` is not deterministic.** fontTools writes a fresh
  `head.modified` on every run, and `make_chart.py` base64-inlines the woff2
  into every page. **Run the subsetter first, then the build** — backwards, the
  pages carry the base64 of a font no longer on disk. Nothing fails; the two
  just disagree, and the next "does a rebuild produce a diff?" check gives a
  misleading answer. For the same reason, do not re-run it to see whether
  anything changed — read the coverage report.
- **A wrapped cross-reference still miscounts.** `row += 1` assumes one visual
  line. Every in-block row is now an exact `--lh` multiple and no cross-
  reference currently wraps on any table, so all 93 brackets across the three
  plates align — but a longer one would occupy two rows against a one-row
  budget. Unguarded, because the build has no font metrics.

## 2026-07-29 — Genealogy II: scans in, upper block read, three findings

Nothing published and nothing registered. `docs/` is byte-identical to what it
was: a rebuild produced no diff, and `--public` still reports 104 and 73 persons
across 4 pages. A half-read plate must not render.

Work is on branch `table-ii-transcription`, commits `c1aa97f` and `de42460`.

### The scans

Both arrived. **Table 2 is 7770 × 12681, portrait** — the published plates are
landscape — sha256 `d7d050f5…39f7a6`. Legibility was tested before committing to
the read and is good: the raised dot (U+02D9) and the modifier apostrophe
(U+02BC) are cleanly separable at native resolution, which is the distinction
Table 1 got wrong once.

**Table 3 is 3770 × 5503 — about a ninth of Table 1's pixel count.** Untouched
so far. Expect it to be materially harder and budget accordingly.

### Scale, measured rather than assumed

Table 2 runs past **269 persons** against Table 1's 104, in two blocks joined at
the couple 154+155, and reaches **six generations** where Table 1 reaches five.
On that evidence the session was split at the plate's own block boundary: plate
numbers 1–153 read and encoded now, 154–269 next. The reason is not tidiness —
reading ~269 persons in one context would force a summarization mid-read, and a
reading that only ever lived in the conversation is one that can go missing.

### The clan rule decided three brackets

Matrilineal descent is not just a check here; it resolved geometry that row
alignment alone would have got wrong.

- **64** sits on 17's row but is Turkey, and 17's wife 18 is Corn. It belongs to
  15+16, whose other four children are all Turkey.
- **47's** line carries two `+` spouses, 48 (F, Parrot) and 49 (M, Turquoise).
  49 cannot be 47's spouse; he is 48's second husband, and children 116–118 are
  Parrot, so the group hangs off 48's line.
- **51+52** — children 119–121 are Lizard, which is 52's clan, not 51's Water.

Also corrected against the low-resolution overview: there is **one founding
couple, not three**. A single vertical rule off person 1's row carries 3, 5 and
7, all Water as their mother is. The overview appeared to show three separate
couples in the left column; at native resolution 5 and 7 sit in the same column
as 3. *Judge structure at native resolution, not from a downscale.*

### Three findings, recorded and not acted on

- **The plate numbers two different people 101** — `101. F. Naauʼg˙ŭyăiʼ. Water`
  and, on the next line, `101. M. ———. d. Water`, then 102 normally. Confirmed
  at magnification; not a broken 100 and not a scan artefact. `PLATE_NUMBER_MISPRINTS`
  does **not** model this — it maps one union to one wrongly-printed number,
  where here two people share one.
- **Parsons's cross-references into Genealogy I run one high from its person 66
  onward**, and are exact through its 27. Six independent matches on name, sex
  and clan, two of them on age as well. This bears on Table 1, which is
  published and cited: its own misprint prints **68** for person **67**
  (Shuwaiʼᶦri), and Table 2 independently calls that same man 68. **One
  phenomenon, not two unrelated slips** — Parsons worked from a numbering of
  Genealogy I that ran one ahead of the one finally printed. That strengthens
  the standing decision to reproduce 68 rather than "fix" it.
- **Person 43 prints `+ Locust`** where a clan alone belongs, the `+` identical
  in form to the spouse mark. Recorded, not interpreted.

### Font coverage — answered from the cmap, not by eye

Three codepoints appear that neither published table uses: `ŏ` U+014F, `ˑ`
U+02D1, `ᵉ` U+1D49 (the last confirmed, in 84 `Ha˙tsʼᵉ`). All three are already
in **both** master Gentium faces, checked directly against
`vendor/gentium/Gentium-{Regular,Italic}.ttf`. So Gate 4 is a `subset_font.py`
re-run and nothing needs sourcing. macOS substitutes silently, so this could not
have been settled by looking at rendered text.

### Decisions taken

- **Duplicate 101 → internal id for addressing, printed number for display.**
  Both rows print 101, as the plate does. This extends the id/`data-printed`
  separation Table 1 already makes rather than adding a second mechanism.
  *101a/101b was rejected*: it would print something the plate does not, which
  is the one thing the edition exists not to do.
- **The offset is noted on both published pages** — a footnote on Table 2, and a
  sentence added to Table 1's existing `#note-misprint` recording the
  corroboration. Editing a published, cited page means re-verifying it after
  the build.

### The lower block, opened: 154–171 and 232–233

174 records now. **101 plate numbers remain** — 172–231 and 234–274.

**The numbering runs to 274, not 269.** The first orientation pass missed
270–274 at the far right, so the earlier count was low. Treat any figure taken
from an orientation crop as provisional until the tiles confirm it.

- **Three founding couples, not two** — 1+2, 154+155 and **232+233**. The third
  is printed at exactly a child's indent; the only visible difference is that no
  leader rule enters it from the left. Its clan settles it independently: 232 is
  Sun, 154 is Parrot, so 232 cannot be 154's daughter. This is the **second**
  time on this plate that indentation alone would have asserted false descent.
- **The two blocks are one genealogy.** 13, 14, 53, 54, 125 and 126 are drawn in
  the upper block and reappear below carrying "For descendants, see above"; 169
  repeats inside the lower block. Each is stored **once**, as Table 1's person 8
  and Table 4's 3 and 4 are. This is the likeliest route to a duplicate person
  in this file — the ids already exist.
- **Genealogy III is referenced but not transcribed.** Persons 160 and 163 point
  into it. Nothing may link there until Table 3 ships; `#pending-3` is what
  those references resolve to.
- **Person 160 is Genealogy I's person 73** — name, clan and death year (1914)
  all agree.

Two upper-block readings corrected from the lower block's larger setting:
**person 14 carries a braced pair of names**, `{ S˙ʼĭʼrowaisiwa /
Kʼaiʼsh˙dŏwăʼ }`, which is the `{ }` convention the renderer already knows about
at `make_chart.py:544`; and that settled the `ŏ` U+014F reading flagged as
uncertain above.

**One discrepancy left open.** Person 13 reads `Dzia˙ʼyotsʼa` in the upper block
and `Tsiaiutsa` in the lower — one numbered person, two names, both tiles
legible. Both readings are recorded, the upper marked the less certain. Not
resolved by picking one.

Two markings recorded as printed rather than interpreted: **161's sex is
`M.-F.`**, used nowhere else on the plate, stored empty rather than guessed; and
a **heavy ink stroke across 169's row**, which is not type and is noted as an
observation of *this copy*, not as plate data.

## 2026-07-29 — four presentation fixes: card, selection, ruler chip, plate bar

Nothing in the transcription changed. Four things a reader touches did.

### The row highlight could not be cleared

- **The defect.** A chart row lights up two ways: `.line:target` from a `#p`
  anchor and `.line.is-selected` from `openCard`. A hash survives every
  subsequent click, and `markSelected` could only ever clear its own class — so
  following a relation link out of a card (which navigates to `#p{n}`) left the
  row lit with nothing able to turn it off, and opening another card lit a
  **second** row beside it. Only leaving the page and returning cleared it.
- **The fix.** Where the card script runs, the class is the *only* mechanism:
  `.line.is-selected,html:not([data-card]) .line:target`. `data-card` is set
  inside the `popoverOK` block, so it means "the card script is live", not
  "JavaScript is enabled" — where the popover is unsupported the numbers are
  plain anchors and `:target` is untouched.
- `syncSelection()` / `lineFor()` move the class on load, on `hashchange`, in
  the same-hash branch (no `hashchange` fires there), and after a Find submit
  (searching the person already named by the hash fires none either).
- `cardRow` exists because the popover's `toggle` and `hashchange` both arrive
  as tasks in an order that is **not guaranteed**: the close handler clears only
  the highlight it set (`selRow===cardRow`), so it cannot wipe one that hash
  navigation already moved. Correct in either order.
- `rowClick` deselects on a click on bare plate — after a relation link the card
  has already closed, so no close event is coming and the hash never changes
  again. That click is the only thing left that can clear it.
- Verified by counting rows whose computed `outline-style` is `solid`: exactly
  one at every step of card → relative → click-away → other card → register
  link, plus a cold load at `#p5`, and `:target` still lights the row with
  `data-card` removed.

### Everything else

- **Card relatives at `--t-base`, not `--t-sm`.** The row *is* a person line —
  number, name, clan — so it is set at the size the register entry and the plate
  line give a person. The clan is `.92em`, so one declaration moved both. The
  register was re-verified after: relation links `display:inline`, titles 16px.
- **The ruler's identity chip had its own collision.** It is pinned to the
  plate's inline start and shared one 2rem band with the generation labels, so
  whichever label had been panned to that edge sat under it and the chip's
  opaque fill ate the first half of the word (`GENERA|TION 2`). The ruler is now
  3.4rem with the chip at `flex-start` and the labels still at `flex-end`; the
  chip's line-height dropped 1.9 → 1.5 to keep the reserved band small. Print
  returns it to 2rem, where the chip is hidden anyway. Column drift re-measured
  at **0px across all five generations**, and the labels still sit on their
  columns.
- **The plate bar rides the plate's rail.** Find now lands on the sheet's left
  edge and Scale on its right — 0px at both ends, at 1724px and at 375px, both
  tables. It was centred at `--measure-wide`, which matched the title block's
  *box* exactly and therefore aligned with nothing visible: the statistics line
  inside that box is centred text, inset ~270px each side. If it ever moves back
  to a measure it has to move with `.scroll`'s padding or the rails part again.
- **A phone-only card bug, found while verifying the first item.** The mobile
  divider reset was `.pc-col + .pc-col` (0,2,0) against
  `.pc-cols--pair > .pc-col + .pc-col` (0,3,0) — one specificity point short, so
  a stacked second column kept a 16px indent and a rule hanging off nothing.

### Considered and not done

- **Aligning the plate bar to the statistics line itself** was the other reading
  of the request, and was offered with its cost. There is no robust CSS for it:
  the line is centred text whose width changes per table and wraps on a narrow
  screen, so the bar would have to match a sibling's *content* width. That needs
  either CSS anchor positioning (Chrome-only, and it would make the bar
  absolutely positioned) or moving the statistics line out of the title block —
  which `CLAUDE.md` pins as one of the four things that block *is*. The user
  chose the plate's rail. Don't re-open it without a mechanism that survives
  Safari.
- **`.imprint` was not touched.** Spreading its words to the container's edges
  would have "aligned" it by making a centred imprint line into a justified row,
  and the landing page's `.c-stats` would have had to follow.

### One thing left unverified

`Enter` in the Find field could not be exercised through the browser automation
— character keys reach the input but the synthetic `Enter` never submits the
form, and `Escape` likewise never reaches the popover. The submit handler itself
was verified directly (`requestSubmit()`), and implicit submission is unchanged
by anything here, but nobody has watched a real keypress do it in this session.

## 2026-07-28 — a build timestamp, built and reverted

- **Reverted at the user's request; recorded so it is not proposed again.** The
  footer's "Last updated" line was given a clock time and zone — `28 July 2026,
  12:04 MST` — from a single offset-aware `BUILD_TIME` captured per run, local
  rather than UTC so the date could not print as tomorrow's all evening.
  JSON-LD `dateModified` and the sitemap's `lastmod` were deliberately left
  date-only.
- **The cost is the reason it went.** `docs/` would then differ on every
  rebuild, down to the minute, which kills the sync check this project relies
  on: *"rebuild produces no diff"* is currently valid within a day, and would
  have become valid never. The only way to keep both is to print the time only
  when the date changed, which is self-defeating.

## 2026-07-28 — the card rebuilt, 83–85 attributed, the leak gate closed

Three things in one push. The third is the one to read first.

### The leak gate had two holes

- **It was blind to prose.** The gate grepped output for `class="eng"` /
  `class="census"` — a research *field* rendered into the page. Research would
  not escape that way. It would escape as a **sentence**: a footnote explaining
  *why* a reading was made. That carries no class, and nothing would have
  stopped it. This was found by nearly writing one.
- **It never saw the landing page.** The check lived inside `build_table`, which
  only handles table pages — so `docs/index.html`, which carries the FAQ and is
  the only public prose that discusses this vocabulary, was unchecked entirely.
- Now `leak_report()` checks markup **and** vocabulary (`census`,
  `familysearch`, `national archives`, `widow…`, `enumerat…`), and
  `check_published_pages()` sweeps every `.html` in `docs/`. **Fails closed**:
  three FAQ sentences that state the boundary are allowlisted by exact phrase,
  so rewording one stops the build until it is allowlisted again. `<style>`
  blocks are excluded — the stylesheet ships `.census{}` rules and a selector
  name says nothing about a person; scripts are **not** excluded.
- Verified against **15 cases**: caught all nine leaks (including the exact
  sentence this was written for, `Family Search` spaced, "widower", "census
  roll"), stayed silent on all six legitimate ones. Then end-to-end by injecting
  a real leak — build aborted, quoted the sentence, deleted the file, exit 1.
- **The gate protects `docs/` only.** It cannot see a code comment, a changelog
  entry or a handoff note, and those are all committed and public.

### Editorial attribution — the first of its kind

- The plate brackets {83, 84, 85} under **68** alone. She has two husbands, 69
  and 70, and the bracket does not say which marriage the children belong to,
  which is why `transcription.py` records their father as unassigned.
- On external evidence, 83 and 84 are attributed to 68+69 and 85 to 68+70.
  **The chart is untouched** — hash-compared across the full 31KB chart region,
  the only difference was an unrelated `clan-origin` token. It still draws the
  plate's single bracket. Only the register and the cards split the group.
- Declared in `TABLES["i"]["paternity"]`, **not** in `transcription.py`: that
  module is the plate, and the plate does not say this. Every row it produces
  carries a dagger linking to `#note-paternity`; 70's plate-attested group sits
  unmarked beside its marked one, so the difference is visible.
- **The supporting evidence is not published and must not enter the repo.** The
  note says a reading rests on evidence outside the plate and stops there.
- `METHOD.md` gains an *Editorial attribution* section with the four rules any
  future one must meet. Its governing principle was reworded: nothing is
  supplied **in the chart**, and the word that always mattered is *silent*.
- **Unresolved:** the evidence pins 85 firmly (born after 69's death). 83 and 84
  rest on ages that do not cleanly line up — worth confirming before it is cited.

### The card is a card now

- It regroups a *detached copy* of the register entry: header band, then one
  column per spouse with that spouse's children under them, so the reader no
  longer pairs `SPOUSES: 66, 76` against `CHILDREN (WITH 66)` themselves.
- `rel_row` gained `data-rel` / `data-with` so the card can pair a children
  group with its other parent **without parsing the label**, which is prose.
  `rel_link` gained `.rel-x` so an undrawn person is still one enumerable
  element. The register renders identically and is still the no-JS card.
- Badge carries the plate number (`68.`), so the number and sex mark leave the
  header *text* — but stay in the dialog's accessible name via
  `.visually-hidden`, or every card would have been silently renamed.
- Clan became a `Clan: X` badge, suppressed for the one value that is an origin
  rather than a clan (101, "of Zuñi", marked `.clan-origin` in `person_line`).
  The vital note steps back to `--muted-fixed` — metadata, not name — making it
  the second deliberate user of that token after `.imprint` (5.28:1 light,
  5.69:1 dark). Every relation button carries its clan; **89** is the only
  person in either table with none, and it is omitted with no placeholder.
- Traps worth knowing: chips are `.reg-rel > a`, **direct children only** — a
  cross-reference row is also a `.reg-rel` and its links sit in running prose.
  The column divider is scoped to the exactly-two-column case, because columns
  wrap (68 has three) and a wrapped column would hang a rule off nothing.
- New tokens: `--t-lg`, `--t-xl`, `.edmark`. Parent buttons → spouse heading
  measured 0px before, 24px after; column drift 0.00px at all five generations.

## 2026-07-28 — the clan gets its own colour, the number gets air

- **`--clan` is a third exception to "all text on a table page is `--ink`",**
  after `--muted-fixed` on the statistics line and `--sic` on the misprint. Add
  a fourth only with the same evidence.
- **This is not the reverted per-clan palette, and the distinction is the whole
  argument.** That one gave 13 clans 13 hues and collapsed to about one
  just-noticeable difference under deuteranopia. This gives the *field* one
  colour: two colours to tell apart, not thirteen, differing in lightness as
  well as hue, so it survives any colour vision. Measured against every
  background it can sit on — paper 5.86:1 light / 9.53:1 dark, panel 6.12 /
  8.74, selected row 6.22 / 10.40 — all clear of the 4.5:1 text minimum.
- **The values are `#7A5C1E` / `#DBB970`, which are `--accent`'s.** Not a
  coincidence: this is the gold the clan carried before `body.chart`'s flatten,
  and the `--sel-bg` comment has quoted those exact ratios as "the clan gold"
  the whole time. **The token is deliberately separate from `--accent`** —
  accent means *interactive* everywhere else, and recolouring the chrome must
  never recolour the genealogy. Declared in **all five** palette blocks (the
  `light-dark()` set plus three static fallbacks for Firefox ESR 115 and Safari
  ≤17.4); miss one and a browser gets an unstyled clan.
- **It flattens to black in print.** The offprint is black on white and gold
  degrades to a weak grey; the colour never carried information the word itself
  doesn't.
- **`.2em` after the number's point**, so "65." reads as the entry's label
  rather than the first word of the name. A margin, not a wider space
  character — independent of the font, and whitespace collapsing can't eat it.
- **Measured, because this is the invariant that breaks quietly:** column drift
  **0.00px at all five generations**, unchanged from baseline. The widest line
  on Table 1 grew 275.7px → 284.4px inside its 384px `--col` block, leaving
  99.6px of slack, so nothing was pushed toward the stub and no sibling bracket
  moved off its `mother_row`.
- **Caught at Gate 4, worth repeating:** the comment above `.clan` still read
  *"Clan is not colour-coded: it renders as text like every other field."* The
  diff review is what found it. Read the diff, not just the build output.

## 2026-07-28 — the card drops the cross-reference row

- **Second half of the entry below, same reasoning.** The card repeated the
  plate's cross-reference — *"For second wife and offspring see below, 76,
  90-3"* — which the chart already prints directly under the person's line. The
  card is opened *from* that line, so the reader was told it twice in one
  glance, exactly as with the misprint note. Removed on the clone; the register
  keeps every row.
- **The rule is structural, not per-person:** a relation row with no `.rel-l` is
  a cross-reference. So `openCard` drops it without a list of ids, and a future
  table is covered without an entry. **Persons 12, 67 and 73 carry one on
  Table 1** (73 has two); Table 4 has none. Read that from the transcriptions'
  `cross_ref` column, not by opening cards.
- **The consequence to know before reverting this.** The chart prints a
  cross-reference only at a person's **first** occurrence — `xref_printed`
  dedupes it. Person 67's is therefore on line 67 and *not* on the misnumbered
  68 line below, so opening 67's card from that line no longer surfaces the
  cross-reference at all. It is still in the register entry, one click away on
  the card itself, and on the chart at 67. A narrower rule — keep the row only
  where the clicked line lacks it — was offered and not taken.
- **Measured:** all 214 chart lines on Table 1 opened programmatically, zero
  cards contain a cross-reference row; cards 12, 67 and 73 each now end at
  their CHILDREN row; the register still carries all four rows.

## 2026-07-28 — the person card gets its own format

- **The card was rendering the register's format.** It clones the register
  entry — one source of truth, which is right — but it was also inheriting a
  layout built for scanning 104 stacked entries. As a single card it now sets
  its own: the printed line is the title at `--t-lg` (a new 1.125rem step,
  added because the ramp stopped at `--t-md`) and underlined; the relation rows
  keep the register's 1.4rem indent instead of having it zeroed; each label
  gains a colon; each related person is a rounded chip.
- **Scoping is the whole trick, and the next change here must keep it.** Every
  CSS rule is under `.pcard` and every DOM edit is made on the *clone* in
  `openCard`, never in `rel_row` or `rel_link`. The register renders the same
  markup and must keep its dense list — verified after the change: its links
  still compute `display:inline`, its entry titles still 16px.
- **Chips are `.reg-rel > a`, direct children only.** A cross-reference row is
  *also* a `.reg-rel`, but its links sit inside an `<em>` of running prose —
  "For second wife and offspring see below, 76, 90-3". A descendant selector
  turns those into buttons mid-sentence. This is the trap in this markup.
- **Three edits to the clone, each with a reason not to do it the obvious way.**
  The colon and the number's point are written as real text, not CSS `::after`,
  so they survive a copy out of the card. The middot between relations is
  *collapsed to a space*, not deleted — deleting the text node also closes the
  gap after the label, and the space is what keeps copied text readable. Both
  text edits are idempotent, so reopening a card cannot accumulate `56..`.
- **Measured:** 4px radius chips, 26.6px tall, matching the 24px floor the
  card's action buttons already use rather than `--tap`; checked in both
  palettes and at 375px, where the card is the bottom sheet — chips wrap, no
  overflow, no horizontal body scroll.
- **Not done, and worth deciding:** the register's own relation lists still read
  `56 Weʼdyumă` without the point, while its entry titles carry it. The card
  just lost that inconsistency; the register still has it. One line in
  `rel_link` if it should match.

## 2026-07-28 — the person card drops the misprint note

- **The card repeated an annotation the reader was already looking at.** Opening
  the person card from the misnumbered `+` line under 76 appended
  *(misprint, click here to see notes)* directly under the card's first line —
  the same sentence, in the same red, as the `SIC_ROW` sitting on the chart row
  the card was opened from and anchored to. Two statements of one fact in a
  single glance. The card now carries **the number and nothing else**.
- **The number swap stayed.** `data-printed` on the link still makes the card
  read 68 from that line and 67 from person 67's other lines. That is plate
  fidelity, not annotation, and it is the half of this that must not be
  "simplified" away later. `.pcard-sic` and its CSS are deleted.
- **Where the misprint is still explained:** the chart's own annotation row, and
  the footer note at `#note-misprint`. Those are the only two places, by
  decision — same shape as the rule that keeps `+`, `F.`/`M.` and the leader
  rule decoded once, in the footer.
- **A person-level variant was built first and rejected by the user**, so don't
  rebuild it: the misprint was made a fact about the person (`Chart.sic` →
  `data-sic` on the register entry → note on *every* one of that person's
  cards). It worked — measured across all 214 chart lines, exactly the two
  occurrences of 67 carried it and no one else — but it multiplied the
  redundancy rather than removing it. Take it from git if it is ever wanted.

## 2026-07-28 — the theme button's static label said Auto

- **Fixing a miss from the entry below.** The Auto state was removed from the
  theme control, but the button still shipped `Theme: Auto` as its literal
  markup; `applyTheme()` overwrote it on the first tick, so it was only visible
  in the moment before the script ran. The static label is now bare `Theme`,
  which is all the server can honestly say — it cannot know which palette a
  reader resolves to.
- **Worth recording is how it was missed.** The check that passed was
  `!document.body.textContent.includes('Auto')`, run in the browser *after* the
  script had already rewritten the label. Testing rendered state cannot see what
  the HTML ships; for anything that exists in the markup, grep the built file.

## 2026-07-28 — selection highlights move off the text

- **The highlight no longer sits on the words it highlights.** All three of them
  — the selected chart row, the register entry, and a targeted footer note —
  used `box-shadow: inset 4px 0 0`, which paints a bar over the first glyphs,
  plus an outline hugging the text at `outline-offset:-1px`. Every part of the
  treatment is now drawn **outside** the border box: the leading rule is a
  shadow offset `-.3rem` with no spread, the halo a `.3rem` spread behind it,
  the ring an outline at a matching `+.3rem`.
- **Still layout-neutral, which is the constraint that matters.** Shadows and
  outlines take no space, so nothing moves: the selected row measures 25px,
  exactly as an unselected one does, all 24 child groups still sit on their
  mothers' lines, and column drift is 0px at every generation. Invariant 2
  permits `background`, `box-shadow` and `outline` on a selected `.line` and
  this uses only those three.

## 2026-07-28 — the misprint annotation gets its own row, and a colour

Refines the entry below, same day.

- **The annotation moved off the printed line.** It was sitting inline between
  the number and the name — inside the transcription, in other words. It is now
  *(misprint, click here to see notes)* on its **own row directly beneath** the
  Shuwaiʼᶦri line, so the printed line contains only what the plate prints.
- **`+ 68.` is ringed in red.** The ring is an `outline`, never a border or
  padding: a border widens the row and throws the sibling bracket off its
  `mother_row`, which is the failure this project has documented twice.
- **`--sic`, a new colour, and the only thing on a table page that is not
  `--ink`.** It is text, so it has to clear 4.5:1 on both papers by itself:
  `#B3261E` measures **6.43:1** on the light paper, `#FF8A80` **7.19:1** on the
  dark. Declared in all five theme blocks.
- **The person card follows the line it was opened from.** From the misprinted
  line it titles the card *68.* and repeats the red note under the first line;
  from person 67's three other lines it still says *67.*, and the register entry
  always says 67. Carried on `data-printed`, so the card is told rather than
  left to guess — verified in all three states.
- **The layout proof, because this added a row to the chart.** All **24** child
  groups were walked before and after: every sibling bracket still sits on its
  mother's line, 0 mismatches both times, and column drift is still 0px at every
  generation. The annotation row is exactly one `--lh` tall (25px, same as a
  `.line`) and is counted with `row += 1` like a cross-reference row, which is
  what keeps everything below it on the grid.
- Clicking the note from inside the card closes the card and lands on the
  highlighted note, clear of the sticky bar. Table 4 emits none of this markup.

## 2026-07-28 — the misprint is printed as printed; footer goes two-column

- **The plate's misprint is reproduced again, which is the point of the
  edition.** The `+` line under 76 on Table 1 is numbered **68** on the plate but
  names Shuwaiʼᶦri, Turkey = person 67. The chart had been drawing it as *67* —
  a silent correction, and a direct breach of the rule that misprints are
  annotated and not fixed. It now prints **68**, links to `#p67`, and carries a
  *misprint* marker that jumps to `#note-misprint` in the editorial notes, which
  is highlighted on arrival. Declared as data in `transcription.py`'s new
  `PLATE_NUMBER_MISPRINTS`, read through `union["printed_number"]` with
  `getattr`, so Table 4 needs no entry and the renderer stays table-agnostic —
  Table 1's numbering must not leak into it.
- **The footer apparatus is a two-column grid** of `.app-sec` sections at
  `--measure-wide`, one column below 56rem. Font size unchanged. Grid, not CSS
  multicolumn: multicolumn will happily break an `h2` away from the `ul` it
  introduces. Side effect worth having — the footer now shares a left edge with
  the register above it, closing one of the four-left-edges findings recorded
  two entries below.
- **Person references in the apparatus are links.** `1+2`, `54+55`, `Person 8`,
  `58+59`, `76`, `person 67`, and Table 4's `3`, `4`, `59+60`, `36-43`, `50-53`,
  `19`, `20`, `73` all resolve to `#pN`. Done with a `_p()` helper at each call
  site, **never a regex over the prose** — the apparatus is thick with numbers
  that are not people (1923, vol. 19, pp. 133–292, U23), and a pattern loose
  enough to catch `58+59` would link those too. Ranges point at their first
  member, the rule `linkify_xref` already uses.
- **The theme control lost its Auto state.** It toggles Light ↔ Dark, so the
  button always names a real palette. The system preference is still honoured —
  it is what a first visit resolves to, and nothing is written to storage until
  the reader presses the button, so an untouched control keeps following the OS.
- **The statistics line is back under the table title**, in the landing page's
  grey and a step larger (16px against `.c-stats`' 14px). That needed
  `--muted-fixed`: the real `--muted` captured at `:root`, because `body.chart`
  redefines `--muted` to `--ink` and a `var()` takes the value of the element it
  is declared on. `.imprint` is the only user, deliberately. Contrast measured
  **6.15:1 light, 6.73:1 dark**. The title block also drops to `--measure-wide`
  on table pages — it no longer holds a citation, and the line does not fit in a
  40rem measure at 16px.
- Measured after: column drift **0px at every generation** on both tables, no
  dangling `#` anchors in either footer, footer one column at 375px with no
  horizontal overflow, no console errors, build exit 0 with 6 JSON-LD blocks
  valid, structural self-checks pass on both tables.

## 2026-07-28 — toolbar splits left/right; the table title pages are cut back

- **Find goes hard left, Scale hard right**, spanning the plate bar. The push is
  an auto start-margin on `#scale-mount`, **not** `justify-content:space-between`
  — `#find` carries `[hidden]` until the script unhides it, so with
  space-between a reader without JavaScript would get the scale buttons stranded
  on the left of an otherwise empty bar. Verified in that state: with `#find`
  hidden the buttons still measure flush to the bar's right edge. On a phone the
  row wraps, find above and scale right-aligned below.
- **The table title pages lose the source citation and the statistics line.**
  `<div class="cite">` and `<p class="imprint">` are gone from Genealogy I and
  IV; a table page's title block is now the plate label, the numeral and the
  double rule. The landing page keeps its citation — the removal was scoped to
  the table pages.
- **The doi is untouched by that.** It was never in the title-page citation: it
  lives in `cite_html()`, the footer's *Citation* block, and in the JSON-LD
  `identifier`. Both table pages still carry it twice. Checked, because the
  title-page block and the footer block read alike and cutting the wrong one
  would have rotted every printed citation.
- The now-unused `.imprint` CSS and the `imprint` local were deleted rather than
  left dangling. `CITE` stays — the landing page still renders it.
- Measured after: column drift **0px at every generation** on both tables, find
  flush left and scale flush right to the bar's content box on both, build exit
  0 with 6 JSON-LD blocks valid, no console errors.

## 2026-07-28 — the key comes back off the page; the notation moves to the footer

Same day as the entry below, and it partly reverses it. Read the two together.

- **The on-page chart key was removed again, by decision, and its code deleted.**
  `key_html()`, the `.key`/`.key-d` CSS and the print overrides are gone rather
  than left unreferenced — keeping them uncalled last time is exactly what
  produced the "looks like a bug but isn't" note in `CLAUDE.md` that then had to
  be corrected twice. Recoverable from git if it is ever wanted back.
- **The three notations did not go with it.** `+` (spouse), `F.`/`M.` (sex) and
  the leader rule are now the first three items of the footer's **Navigating
  this chart** list, which is therefore the only place on the page they are
  decoded. `navigating_html()` says so in its docstring. This is the third time
  these three have moved; do not thin them out.
- **The plate caption lost its provenance sentence.** "Redrawn from the plate as
  printed; brackets, columns and leader rules reproduce the 1923 layout" is
  removed — the footer's editorial notes already make that claim. The caption now
  carries only the pan hint, so **`.plate-caption` is what hides above 1400px and
  in print**, not `.pan-hint`: hiding only the span left an empty figcaption
  holding its own bottom padding open. Measured 0px above the breakpoint and 0px
  under the print rules.
- **Footer order changed:** *Navigating this chart* moved up to sit directly
  under *The record*, ahead of *Editorial notes*, *Provenance* and *Citation*.
  How to read the thing now precedes the scholarly apparatus about it.
- **Glyph rendering on Windows and Android was verified on device** and is no
  longer an open question. Recorded under Facts worth knowing, with the cmap
  reasoning kept as the durable evidence.
- Measured after the change: column drift **0px at every generation** on both
  tables, no horizontal overflow at 375px, masthead still two rows, no console
  errors, build exit 0 with 6 JSON-LD blocks valid.
- **Audited but not changed** — recorded so the next session does not re-derive
  it. The page has four left edges at full width: masthead 8px, plate 59px,
  chrome (toolbar, caption, register) 115px, prose 371px. The plate and the
  chrome that controls it are 56px apart because the scroller is full-bleed
  while its chrome is capped at `--measure-wide`. Below ~1400px they converge,
  which is why it is easy to miss. Left alone deliberately this round.

## 2026-07-28 — the chart key returns, as a disclosure

- **The key is back and the open design thread is closed.** Since the
  always-visible band was removed earlier the same day, three notations had been
  explained nowhere on the page — `+` for a spouse, `F.`/`M.` for sex, and the
  leader rule. `key_html()` now renders a **closed `<details>`** between the
  title page and the plate bar: **34px collapsed** against the old band's
  ~100px, for material a reader decodes once. `key_html()` and the `.key` CSS
  are therefore **no longer unreferenced** — the note in `CLAUDE.md` saying so
  has been replaced.
- **Why `<details>` and not a popover:** the key has to work with JavaScript
  off. Nothing in the page script touches it — verified by grepping the shipped
  script, which references `details`/`summary` only in two pre-existing places,
  one of them the line-click guard that already excluded `summary` and so does
  not hijack the disclosure.
- **The key sits outside `.plate-tools`, deliberately.** The print rule hides
  that span; a key parked in the toolbar would have vanished from printed
  sheets, and the old band printed. `@media print` forces the disclosure open
  using **both** mechanisms — the legacy `summary~*{display:block}` and
  `::details-content` — because engines disagree. Measured in Chrome 148: with
  the disclosure closed, only `::details-content` fires (34px → 106px); the
  legacy selector alone was **inert**. Do not delete either one on the grounds
  that it looks redundant.
- **Chrome is `.register-d`'s**, so the site has one disclosure look, not two.
  The default triangle marker is kept rather than the landing page's `+`/`–`
  marker: `+` is chart notation for a spouse and the key explains it two lines
  below, which would have been a genuine collision.
- **The summary's padding is solved from `--tap`, not floored by it.** With the
  line-height pinned, `calc((var(--tap) - 1.4em) / 2)` makes the hit area
  measure exactly `--tap` at both pointer sizes with the label centred; a bare
  `min-block-size` cleared the floor but left the label sitting high on a coarse
  pointer. Measured 32px. The floor is kept as the guarantee.
- **Measured, not assumed:** column drift **0px at every generation** on both
  tables (I: 5 generations, IV: 4); no horizontal overflow at 375px with the key
  open, items wrapping to 7 rows; masthead still two rows; no console errors.
- The editorial-apparatus note now names the key alongside the generation ruler,
  the person numbers and the register — it is 2026 apparatus, not the plate.

## 2026-07-28 — DOI minted; table pages reworked for readability and reach

- **Archived at Zenodo; the edition has a DOI.** Concept doi
  `10.5281/zenodo.21637900`, first release `v1.0.0`. Zenodo's webhook is on the
  repo, so **cutting a GitHub release now mints a new version doi
  automatically** — that is a side effect worth knowing before tagging
  casually. `.zenodo.json` controls the record and is read from the **tagged
  commit**, so it must be on `main` before a release is cut; without it Zenodo
  titles the deposit after the repo. The doi is in `CITATION.cff`, the README
  badge, the citation block on every table page, and as JSON-LD `identifier`
  (`Dataset` on table pages, `CollectionPage` on the landing page, which is the
  entity the deposit actually corresponds to). Always the **concept** doi, never
  a version doi: a version doi on the page would rot every printed citation at
  the next release.
- **The chart key and the plate caption were removed** from the table pages.
  `key_html()` and the `.key` CSS are kept but **unreferenced**, deliberately,
  as the starting point for a redesign. Consequence to fix when that lands:
  three notations — `+` for spouse, `F.`/`M.` for sex, and the leader rule — are
  now explained nowhere on the page. The rest survive in the footer apparatus.
- **Toolbar, typography and navigation reworked.** `--tap` floors every hit area
  (32px mouse, 44px coarse pointer) and `--bar-h` derives from it. Table links
  became labelled buttons with the current page a filled inversion, not a colour
  shift, so it survives both themes and colour blindness. The apparatus moved
  from 14px to fluid 16–18px, cutting the measure from ~96 to ~64 characters.
  Generation columns are spelled out. The whole printed line now opens a
  person's card, guarded so a text selection stays a copy gesture. `see above` /
  `see below` are links, targeted from the union whose children the note stands
  in for — never by parsing the English.
- **Colour was tried three ways and ended flat.** Sex-coloured names (blue/pink)
  and 13 per-clan colours were both built and both **reverted**. The
  measurements are the reason, and are worth not re-deriving: two colours that
  must each clear 4.5:1 on the same paper cannot differ from each other by much,
  so the sex pair sat at **1.05:1** — hue-only, and unreadable under
  deuteranopia. The 13-clan palette was chosen by optimisation, not by eye, and
  its closest pairs still fell to about **one just-noticeable difference** under
  deuteranopia. All text on a table page is now `--ink` via `body.chart`
  redefining `--muted`; `--rule` is untouched, because the brackets and leader
  rules are drawn structure, not text.
- **Phonetic glyph coverage proven without a device.** Reading the shipped woff2
  binaries with fontTools, all 85 characters in the transcription and all 94
  rendered on Genealogy I are in the cmap of both faces. The faces are base64
  data URIs, so nothing is fetched and nothing can 404, and no combining marks
  are used. Tofu is ruled out by construction. Note macOS substitutes for any
  font, so **no on-screen comparison here can demonstrate absence of
  substitution — read the cmap, do not measure widths**. Live rendering on
  Windows and Android is still unchecked.
- **Custom domain considered and declined for now.** `pueblogenealogy.github.io`
  is a GitHub subdomain, not an owned domain. The doi is now the durable citable
  identifier and resolves independently of the host, which removes the strongest
  argument for buying one. If that changes, do it **before** seeding inbound
  links, since those point permanently at whatever host is chosen.
- **Session handoff made structural, not remembered.** Three pieces, because
  the record kept depending on someone thinking of it: `SESSION-NOTES.md` is a
  **rolling** handoff — overwrite it, never append, or it becomes a second
  changelog and stops answering "what do I pick up?"; `/wrap-session` writes it
  and backfills this file; and a `SessionStart` hook
  (`.claude/hooks/session-start.sh`) reads it into a new session automatically,
  so nothing has to be linked by hand. The hook also flags the two silent
  failures — notes older than the last `scripts/`/`docs/` commit, and an
  unclean tree — and fails open, exiting 0 with no output on any error.
  **What a hook cannot do:** `prompt` and `agent` hook types are restricted to
  tool events, so session-event hooks are shell commands only and can never
  author a changelog entry. Reading is automatic; writing still needs the
  skill. `Stop` was the wrong event — it fires after every assistant turn, not
  at session end.
- **`CLAUDE.md` gained a Design invariants section.** Four rules that read as
  styling preferences and are not: the root font size is pinned at 16px because
  `GEOM` states the plate grid in rem against it; a selected `.line` may change
  `background`, `box-shadow` and `outline` and nothing else, or the sibling
  bracket leaves its `mother_row`; `--rule` is excluded from the `body.chart`
  text flattening because brackets are drawn structure, not text; and `--tap` /
  `--bar-h` are stated once and derived. It also names the two things that look
  like bugs and are deliberate — the unreferenced `key_html()`, and the
  visually-hidden "Genealogy" in the table pills below 26rem.
- **This changelog was itself the thing that went missing.** Five PRs merged
  before anyone noticed the entry stopped at the previous day, because the
  session merged PRs directly instead of running `/publish`, whose last gate is
  *record it*. `/publish` now also says that publishing and releasing are
  different acts — pushing deploys the site, but cutting a GitHub release mints
  a new Zenodo version doi.
- **Deleting `prettyph3nom/laguna-genealogy` is blocked on a token scope**, not
  on work: `gh` holds `gist, read:org, repo, workflow` and repo deletion needs
  `delete_repo`, granted through a browser flow no agent can drive. It is empty
  and is **not** the v1 repo — v1 was `laguna-genealogy-tables`, which 404s
  under both owners. Carried in `SESSION-NOTES.md` with a note not to retry it
  blind.
- Zero column drift held at every step; re-measured after each change.

## 2026-07-27 — Search Console verified, fieldwork notes recovered from v1

- **Google Search Console ownership verified** on the URL-prefix property for
  `https://pueblogenealogy.github.io/`. The token is in
  `GOOGLE_SITE_VERIFICATION` in `make_chart.py`; blanking it drops the tag on
  the next build and ownership lapses. A Domain property cannot work here —
  `github.io` is on the Public Suffix List.
- **Recovered two editorial additions from v1.** Fable's clone sat 5 commits
  behind v1's `main`, so this edition never had them. Three of the five were a
  chart key that Fable had independently rebuilt; the other two were content:
  the dates of record (Genealogy I taken February 1918, Parsons returning June
  1919 for II–IV and revising I, chiefly name spellings) and what `d.` asserts
  (already dead *at time of recording*, year given when known). Both are now on
  the landing page, in each table's reading notes, and in METHOD.md/README.md.
- **Search Console and Bing both verified**; sitemap submitted (3 URLs). The
  dead v1 property was removed from Search Console. Bing was set up by importing
  from Search Console — the v2 property only.
- **v1 deleted.** `prettyph3nom/laguna-genealogy-tables` is gone and
  `prettyph3nom.github.io/laguna-genealogy-tables/` now 404s. This edition is
  the only one. Verified after the fact: repo 404, site 404, v2 unaffected.
- **Structured data corrected twice**, both found by Search Console rather than
  by the build. First: the landing page's `hasPart` entries were name-and-url
  stubs, and a nested Dataset is validated as a Dataset in its own right, so
  both failed the required `description`. Second: `isPartOf: {"@type":
  "WebSite"}` is valid schema.org but Google's Dataset validator rejects it —
  the collection relation it accepts is `includedInDataCatalog` +
  `DataCatalog`. `check_structured_data()` now guards both classes of failure
  and fails the build with exit 1. **Validating against schema.org is not the
  same as validating against Google**, and the check encodes only the rules we
  have actually been told about.
- **v1 mirrored before deletion** to
  `_backup-v1-laguna-genealogy-tables-2026-07-27/` — bare mirror plus working
  copy, `git fsck` clean, 19 commits over 4 refs, test-restored successfully.
  Deleting the repo itself is still outstanding; it needs `delete_repo` scope,
  which `gh auth refresh` cannot obtain non-interactively.

**Lesson worth keeping:** mirror before you delete. The two recovered notes
would have been lost silently, and nothing in the working tree hinted they
existed.

## 2026-07-27 — v2 published at pueblogenealogy.github.io

**The site moved to its own org, repo and root URL.**

- New home: `https://pueblogenealogy.github.io/`, from
  `PuebloGenealogy/pueblogenealogy.github.io`, Pages on `main` / `/docs`.
- Fresh git history. The previous folder was a one-commit shallow clone of the
  v1 repo (`prettyph3nom/laguna-genealogy-tables`) carrying the entire
  interactive redesign as *uncommitted* working-tree changes — roughly 2,850
  lines, never pushed. That work is now the initial commit here.
- Identity is two constants, `SITE` and `REPO` at the top of
  `scripts/make_chart.py`. Masthead and table links were already relative, so
  moving from a `/laguna-genealogy-tables/` subdirectory to a root URL needed no
  link rewrites at all.
- The v1 site is untouched and still live. Retiring it is an open task.

**SEO.**

- `og:image` / `twitter:image`: a 1200×630 band of the actual Table 1 plate,
  derived once with `sips` and committed at `assets/og-cover.jpg`. Not generated
  per build — the source scan is 33 MB and `sips` is macOS-only. `write_site()`
  copies it into `docs/`. Cards are `summary_large_image`.
- One `social_meta()` emits the Open Graph / Twitter block for every page.
- `FAQPage` structured data over five questions, with answers rendered as
  ordinary page text.
- `BreadcrumbList` on each table page.
- `Dataset` gained keywords, spatial and temporal coverage, `inLanguage`
  `["en","kjq"]`, and the Parsons citation. `KEYWORDS` and `SITE_DESCRIPTION`
  are single-sourced so meta, card and structured data cannot drift apart.
- `docs/404.html`, styled like the site.
- Landing copy now names the journal, volume and pages, and Kawaika.

**Workflow.**

- `.claude/launch.json` — `preview_start` config named `site`, serves `docs/` on
  port 4173.
- `.claude/skills/publish/` — `/publish`, the gated release procedure.
- `CLAUDE.md` rewritten for v2; this changelog started.

**Verified this session.** Both structural self-checks pass (104/27/80 and
73/14/58). The public build reproduces `docs/` byte-identically from
`scripts/`, confirming nothing in `docs/` was hand-edited. Column drift measured
**0 px at all five generations** of Genealogy I in the browser. All five live
routes return 200. All JSON-LD blocks parse.

**Gotcha worth remembering.** Creating the repo auto-enabled Pages from the repo
*root*, which served the rendered README at `/` and 404'd every subpath.
Repointing the source to `/docs` does **not** trigger a rebuild on its own — an
explicit `POST .../pages/builds` is required. Documented in the publish skill.
