# vendor/search — the finding aid's build output

Generated files, copied in. **Do not edit them here**; the edit is discarded the
next time they are re-vendored, exactly as `docs/` is.

| | |
|---|---|
| Source | `PuebloGenealogy/laguna-search` (private) |
| Vendored from | `dist/`, at `e31b271` |
| Vendored on | 2026-08-10 (fourth re-vendor that day) |

The **fourth** re-vendor of 2026-08-10, and the cleanest of the three shapes:
a **stylesheet-only** change, so **only `index.html` moved** — the stylesheet
is inlined there — while `search.js` and `search-index.json` came back
**byte-identical**. The change is the All People list's name size, `1.45rem`
down to `1.2rem` and `1.15rem` down to `1.05rem` in the 860px query.

**Only `search-index.json` decides a `--refresh` obligation**, because only it
is built by parsing the published pages. It did not move, so there is none.
Nothing here changed the register markup either — this edit is entirely in the
other repo's stylesheet.

It went **upstream, into `src/search.css`, not into an injection here**: the
test is whether the widget standing alone would want the change, and table
typography is that widget's own layout. The h1 size remains the one thing that
had to be host-side, because it sits on *this* site's ramp.

The three earlier re-vendors that day are worth keeping as the contrasting
shapes. The first: **Genealogy IV's data changed** — 20's father corrected
from 7 to 5 — so `index.html` and `search.js` came back byte-identical and
only `search-index.json` moved, in `meta.generated` and four `relationships`
entries. The second: a **stylesheet-only** change, the same shape as this one.
The third: markup *and* stylesheet, so `index.html` and `search.js` both moved
while the data stood still. Decide from the **relationships** diff, never from
`meta.generated`, which is date-granular and differs on any later day.

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
