# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `321f814` |
| Vendored on | 2026-08-10 (third re-vendor that day) |

The **third** re-vendor of 2026-08-10, and the first where `search.js` moved
without the data moving: the Clan menu's checkbox fix, the menu panning itself
into view, the two search halves holding one line, the theme control moving to
the foot and the All People standfirst moving into the footer note. Markup and
stylesheet both, so **`index.html` and `search.js` both changed** —
`search-index.json` came back **byte-identical**, which is the only one of the
three that decides a `--refresh` obligation, and it says there is none: the
index is built by parsing the published pages, and nothing it parses moved.

Confirmed independently at this end, which is the test that actually settles
it: the register-bearing diff (`.reg`, `.reg-rel`, `.num`, `.xref`,
`sic-ring`, `data-rel`) on all four table pages was **0 lines**.

The two earlier re-vendors that day are worth keeping as the contrasting
shapes. The first: **Genealogy IV's data changed** — 20's father corrected
from 7 to 5 — so `index.html` and `search.js` came back byte-identical and
only `search-index.json` moved, in `meta.generated` and four `relationships`
entries. The second: a **stylesheet-only** change, so only `index.html` moved,
the stylesheet being inlined there. Decide from the **relationships** diff,
never from `meta.generated`, which is date-granular and differs on any later
day.

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
