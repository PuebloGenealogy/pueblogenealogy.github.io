# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `58965e5` |
| Vendored on | 2026-08-21 |

**`58965e5` is on `claude/resume-jntfyn` over there, not yet on `main`.** It is
pushed, so the SHA resolves; a reader checking out that project's `main` will
not find this `dist/` until the branch is merged. Merge it, then this line can
lose the caveat rather than the SHA.

## 2026-08-21 — the Death filter says what it accepts

**One upstream fix (`58965e5`), and it is a label rather than a behaviour.**
The two year fields were both labelled *Year* and are not symmetric: Birth
filters the birth **number**, so a letter can never match and is stripped on
input, while Death substring-matches the **rendered cell** — `d.` or
`d. 1918` — so `d` is the one way to reach every entry recorded as dead. That
matters more than it sounds: **24 carry a printed year and 103 more have no
year to type**, so stripping letters to make the shared label honest would have
deleted the only route to those 103. The user chose to relabel.

- **The placeholder reads `Year/d.`**, and the spoken label is *"Filter by
  death year, or d. for any recorded death"*.
- **`inputmode` follows the same split.** It was `numeric` on both, which on a
  phone offers a keypad with **no `d` on it** — the letter route was
  mislabelled *and* unreachable on the device most likely to need it. Birth
  keeps the keypad.

**The wording is a measurement, not a preference** — the same lesson the Sex
option's dash taught, one control along. The placeholder has to be COMPLETE at
the narrow layout, where the column is 62px with **47.2px inside the padding**:
*"Year or d."* measures **52px** and clips to `Year or d`, losing the period
that IS the value, and *"Year / d."* fits by **1.2px**, which is no margin at
all. `Year/d.` is **40px** with the face loaded and **37.6px** in the fallback
stack. Verified unclipped at 1280, 1000, 900, 700 and 375px, and `/` is in both
faces of the subset, so nothing substitutes. **The pan threshold did not move**:
617px of `scrollWidth` at 375px, as recorded.

Checked in the built page: `d` gives **115 of 620 people**, `1918` gives 5, and
Birth still strips letters (`18x7` → `187`).

**Shape: the FOURTH one, minus the data** — `search.js` moves, `index.html` is
byte-identical (a script change, stylesheet untouched), and
`search-index.json`'s only difference is `meta.generated`, 2026-08-18 →
2026-08-21, which is the clock. `identities`, `namesakes`, `people` and
`relationships` are byte-identical, field by field. **No `--refresh`
obligation**, and the register-bearing diff at this end is 0 lines on all four
table pages.

**The index was built from a cache seeded by hand, because this session cannot
reach the site.** Egress policy blocks `pueblogenealogy.github.io:443`, so
`--refresh` fails at the proxy; `cache/` was seeded from the local `docs/`
build instead, which is the same shortcut the 2026-08-17 entry describes and is
sound on the same grounds — `docs/` is reproducible and those bytes are the
published state. **A `--refresh` run is still owed** from a machine that can
reach the site; it should return these three files byte-identical apart from
`meta.generated`.

`leak_report()` run by hand over all three files, in `vendor/search/` and in
`docs/search/`: clean.

## 2026-08-18 — the sic tooltip names the reading, and `?open=` stops lying

Two small upstream fixes (`11a2960`), both of which the widget standing alone
wants, so neither is a host injection.

- **The `sic` tooltip names what the edition reads** — *"The plate prints this
  clan; the edition reads Badger"* against the old *"the edition's reading
  differs"*, which told a reader something was wrong without telling them what.
  The coyness had a cause and it is gone: the reading is published on the ringed
  span as `data-reading` (added here 2026-08-17), and the index already takes
  `sex` from it. Falls back to the old wording if a reading did not resolve —
  gate 1 refuses to build in that case, so the fallback should be unreachable.
  **The displayed value is unchanged**: `sexOf()`/`clanOf()` still show the
  plate's, because the edition annotates a misprint rather than correcting it.
- **`restoreOpen()` no longer leaves `open` naming a closed row.** It cleared
  the key when the row left the matches but not when the row merely fell past
  the rendered window — where it is deliberately *not* opened, since opening it
  would mean rendering as far as it and moving the page under the reader. The
  key went on to the URL regardless, so a link shared after a re-filter could
  reopen a row the sender was not looking at.

**Shape: the FOURTH one again** — `search.js` and `search-index.json` move
while **`index.html` is byte-identical** (a script change, stylesheet
untouched). **No `--refresh` obligation**: the index's only difference is
`meta.generated`, 2026-08-17 → 2026-08-18, which is the clock and not the index
drifting — `identities`, `namesakes`, `people` and `relationships` are all
byte-identical. Nothing at this end moved the register markup.

`leak_report()` run by hand over all three files: clean.

## 2026-08-17 (second) — five people moved parents, and only the index moved

**A re-vendor where the source project did not change at all.** `laguna-search`
is still at `65b8254`; what changed is its *input*, because this site published
a correction to Genealogy III's block 2 — 238 and 8 are 230+231's sons rather
than 236+237's, and 243, 245 and 246 are 236+237's rather than 232+233's.

So `index.html` and `search.js` came back **byte-identical** and only
`search-index.json` moved, which is the shape CLAUDE.md records for a data
change. The diff is exactly the correction and nothing else: **11
`relationships` records** (III-8, 230, 231, 232, 233, 236, 237, 238, 243, 245,
246) and **2 `people`** (238 and 239, generation 4 → 3). `meta` is unchanged,
including `generated`, because it is date-granular and this is the same day.

**Do not read the unchanged commit hash as meaning the re-vendor was
unnecessary.** The index is built by fetching these pages and parsing them, so
it goes stale on a data change here whether or not that project moves. The
`--refresh` run reported `re-fetched`, and its seven gates passed.

`leak_report()` run by hand over all three files: clean.

## 2026-08-17 — Juana is a woman, and the reading is read rather than guessed

**A data error on the public site, and the first re-vendor that had to be
built from a cache seeded by hand.** Genealogy III's 37 — Juana, whom the
edition reads **F** and the plate prints **`M.`** — was published in this index
as `sex: "M", sexPrinted: "M"`, so she could not be found as a woman. Two
independent halves, and fixing either alone left it visible:

- **The reading was not published.** This site rings a misprint and showed only
  the misprint, so the reading was unrecoverable from the page. That tool
  recovered a misprinted **clan** by *guessing* — nearest known clan within two
  edits, which gets `Bager` to Badger — and there is **no such vocabulary for
  sex**, since `M` and `F` are equally valid and neither is nearer the other.
  So it filed the printed letter under both fields, deliberately.
- **The sex filter tested only one reading** where the clan filter tested both,
  which is why the data error was invisible: the `sic` tooltip promises *"Both
  are searchable"*, true for clan and false for sex.

**The fix could not start upstream, and this is the part a fresh reader gets
backwards.** `build.py` builds the index by **parsing these published pages**
and reads no transcription module, so it has no `PERSONS` to take the reading
from. `make_chart.py` now emits **`data-reading`** on the ringed `.sex`/`.clan`
span — the fix `CLAUDE.md` had named years before it was needed — and only then
can the parser read it. A build gate asserting the index's `sex` matches the
transcription, landed first, would abort every build forever.

Upstream (`65b8254`): `sitesource.py` captures the attribute; `build_index()`
prefers it and keeps `nearest_clan()` as the fallback for a page built by an
older version of this site; **gate 1 now refuses a ringed field whose reading
did not resolve** (empty is legitimate for a sex nobody recorded, so it is
asked only where the field is ringed); and the sex filter matches both
readings. `sexOf()` is untouched — the plate's letter is still what the row
shows, because the edition reproduces the plate.

**Exactly one record moves in the whole index**: III·37, `sex` M → F,
`sexPrinted` still M. `identities`, `namesakes` and `relationships` are
byte-identical, and both clan misprints resolve to the same values the guess
produced, now stated rather than inferred.

**The re-vendor shape is a FOURTH one**, and the file list is the tell:
`search.js` and `search-index.json` both move while **`index.html` is
byte-identical** — a script-and-data change, the stylesheet untouched. The
three shapes recorded below are stylesheet-only, markup-and-stylesheet, and
data-only.

**And the build order inverts, which is the thing to plan for next time.** The
index is built by fetching *these* pages, but the change the index needs was
*in* those pages and not yet live — so a plain `--refresh` would have re-fetched
a site without `data-reading` and rebuilt the old index. The `cache/` directory
was seeded with the local `docs/` build, `build.py` run **without**
`--refresh` against it, and the result vendored. That is sound only because
`docs/` is reproducible and exactly those bytes were published in the same
commit; **the post-publish `--refresh` is what confirms it**, and if that run
ever disagrees, re-vendor from it. Do not use this shortcut for anything but a
change that ships in the same publish.

Seven changes to the search card and the person list, all **upstream in
`src/search.css` and `src/search.js`, none injected here**. The test is whether
the widget standing alone would want the change; table typography, a section's
own heading, its captions and the height of its own controls all belong to that
widget. What had to be host-side is the title block's type — see the note below
the list.

- **The name size** (`e31b271`) — `1.45rem` down to `1.2rem`, and `1.15rem`
  down to `1.05rem` in the 860px query.
- **The section head** (`de773d4`) — the kicker *Browse the complete edition*
  and the heading *All people* replaced by **`Index`**, the running count moved
  to sit beside it, and **`Clear all` removed**. The empty state's *Clear
  filters* is untouched.
- **The number field's note** (`81d28ed`) — the sentence naming the numbers as
  Parsons's own removed, and the instruction reworded to *"Choose a table and
  enter the number to find the person; press a numeral again to release it"*.
  The live `tableHint` after the em dash is untouched: it is a readout of which
  tables are selected, not part of that sentence.
- **The table buttons' caption** (`e937fdb`) — *Genealogy table* removed from
  above `I II III IV`. The group's `aria-label` stays, so the accessible name
  is unchanged; this removed a caption, not a name.
- **The number box's `#`** (`520d858`) — moved from above the box to beside
  it, so the name box, the numerals and the number box share a top and a
  bottom edge. It was the last caption left stacked in the card, and it held
  that half's control row 30.36px taller than the other's.
- **The standfirst, and the card's height** (`499a3b4`) — the standfirst
  rewritten to *"Search by name or find a person by table and number."*, and
  the card compacted vertically: the three controls from 52px to `--lg-tap`,
  and the four gaps around them tightened. 195.89px → 170.28px at 1100px.
  `--lg-tap` rather than a literal because 44px is the touch floor, so that is
  as compact as the card may get.
- **The unrecorded sex, and the Sex column** (`6eaedb0`) — the fourth option
  in the Sex filter reads `—` rather than *Not recorded*, with the wording
  kept on `title` for hover; `label` would replace the dash rather than
  describe it. **The wording of an option is a layout input**, because a
  `select` sizes to its widest OPTION and not to its column: *Not recorded*
  needed 124px, which is what the column was at the base and 1120px
  breakpoints and why the 860px block had to hold the control to a 104px
  column after it hung 20px over Birth. The widest option is now *Female* —
  71.78px at the mouse layout's 12.48px type, 72.78px at the narrow layout's
  13.12px — so the column is **80px at all three breakpoints**, with
  7.22–8.22px of headroom and 6.4–12px of clearance to Birth's left edge at
  375, 700, 1000 and 1300px. The narrow grid gives up 24px and the document's
  pan threshold moves with it, **675px → 651px** as a window width (636px of
  client width, clean at 636 and panning at 635).

Seven re-vendors, and between them they show every non-data shape there is:
stylesheet only, so **`index.html` alone** (the stylesheet is inlined there),
twice; markup *and* stylesheet, so **both `index.html` and `search.js`**, twice
— the card's boxes and, last, the Sex option and its column; and — the one this
file had not recorded before — **`search.js` alone**, twice, for a change to
what the script writes at runtime, which is what both the note and the caption
are. **`search-index.json` is byte-identical through all seven**, and it is the
only one that decides a `--refresh` obligation — so there is none. Nothing at
this end changed the register markup either.

**The bar and the title block's type on `/search/` moved the same day and are
NOT in this list**, because they are host-side: `write_search()` now builds the
bar from the site masthead's own tokens, sizes the widget's `.lede` from the
table pages' `.imprint`, and redraws its `.rule` from `.rule-double`. All three
fail the upstream test — the widget standing alone wants its own bar-less title
block, its own 20px lede and its own 452px gold rule.

The **data** shape is the one neither of these two is, and it is worth keeping.
Earlier that day **Genealogy IV's data changed** — 20's father corrected from 7
to 5 — and then `index.html` and `search.js` came back byte-identical while
only `search-index.json` moved, in `meta.generated` and four `relationships`
entries. That is the shape that owes a `--refresh`. Decide from the
**relationships** diff, never from `meta.generated`, which is date-granular and
differs on any later day.

## What is here, and what is not

`index.html`, `search.js`, `search-index.json` — the three files `index.html`
actually loads. Its stylesheet is already inlined, so `dist/search.css` is not
needed. `dist/embed.html` and `dist/standalone.html` are **deliberately not
vendored**: they are alternative packagings of the same content, and a second
copy of the edition at a second URL is a liability, not a feature.

## Re-vendoring

The index is built from the **published pages**, so it must be rebuilt after any
change here that moves the register markup — and the first run after a publish
takes `--refresh`, or its gates pass against a cache of the site as it was:

```bash
python3 build.py --refresh     # in the laguna-search checkout
```

Then copy `dist/index.html`, `dist/search.js` and `dist/search-index.json` here,
update the commit and date above, and rebuild:

```bash
python3 scripts/make_chart.py --public
```

`write_search()` in `scripts/make_chart.py` is what turns these into
`docs/search/`. It injects the edition's own subset font, which this output does
not carry — see the note there before assuming the page is self-contained.
