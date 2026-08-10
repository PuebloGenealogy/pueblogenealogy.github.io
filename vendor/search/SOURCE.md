# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `499a3b4` |
| Vendored on | 2026-08-10 (ninth re-vendor that day) |

Six changes to the search card and the person list, all **upstream in
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

Six re-vendors, and between them they show every non-data shape there is:
stylesheet only, so **`index.html` alone** (the stylesheet is inlined there),
twice; markup *and* stylesheet, so **both `index.html` and `search.js`**; and —
the one this file had not recorded before — **`search.js` alone**, twice, for a
change to what the script writes at runtime, which is what both the note and
the caption are. **`search-index.json` is byte-identical through all six**,
and it is the only one that decides a `--refresh` obligation — so there is
none. Nothing at this end changed the register markup either.

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
