# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `9974d55` |
| Vendored on | 2026-08-09 |

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
