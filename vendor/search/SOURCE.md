# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `44e3d7b` **plus an uncommitted `src/search.css`** |
| Vendored on | 2026-08-10 (second re-vendor that day) |

> **The provenance above is incomplete on purpose, and must be closed.** This
> `index.html` was built from a working tree that is `44e3d7b` with 96/65 lines
> changed in `src/search.css` and nothing committed. **Commit that upstream and
> replace the SHA here**, or the only copy of the reasoning behind this layout
> is one uncommitted file outside this repo.

Re-vendored a **second** time on 2026-08-10, for a **stylesheet** change rather
than a data one: the All People list now keeps its columns at every width
instead of stacking into cards below 860px, and the search card's numerals and
number box hold one line. `search.js` and `search-index.json` came back
**byte-identical** — which is the tell that this was a pure layout change and
carries **no `--refresh` obligation**: the index is built by parsing the
published pages, and nothing it parses moved.

The earlier re-vendor that day was the opposite shape, and is worth keeping as
the contrast: **Genealogy IV's data changed** — 20's father was corrected from 7
to 5 — `index.html` and `search.js` came back byte-identical, and only
`search-index.json` moved, in `meta.generated` and four `relationships` entries.
Decide a re-vendor from the **relationships** diff, never from `meta.generated`,
which is date-granular and differs on any later day.

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
