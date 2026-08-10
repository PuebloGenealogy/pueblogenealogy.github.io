# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `44e3d7b` |
| Vendored on | 2026-08-10 |

Re-vendored 2026-08-10 because **Genealogy IV's data changed** — 20's father was
corrected from 7 to 5 — and the index is built by parsing the published pages.
`index.html` and `search.js` came back **byte-identical**; only
`search-index.json` moved, and only in `meta.generated` and four
`relationships` entries (IV-20's parents, IV-5's children, IV-6's two child
groups collapsing to one, IV-7 losing children). That is the shape of a genuine
re-vendor: decide from the **relationships** diff, never from `meta.generated`,
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
