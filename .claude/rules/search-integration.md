---
paths:
  - "vendor/search/**"
  - "docs/search/**"
---

# `/search/` and the `laguna-search` integration

This loads automatically because you're touching `vendor/search/` or
`docs/search/`. It also covers `scripts/make_chart.py`'s `write_search()` and
the register-emitting markup (`.reg`, `.reg-rel`, `.num`, `.xref`, `sic-ring`,
`data-reading`) — **that content does NOT auto-trigger**, since `make_chart.py`
is a large multi-purpose file a path-scoped rule can't isolate down to the
relevant functions. If you were routed here from the tripwire in
`memory/architecture-and-design.md`, this is the file you need.

## The published markup is an interface, not just a rendering

A separate tool, **`laguna-search`** (outside this repo, private,
`PuebloGenealogy/laguna-search`), builds its whole search index by **fetching
and parsing the four built `genealogy-*/` pages** — it reads no transcription
module. Since 2026-08-09 its *output* is deployed here at `/search/` while its
own repo stays private (see *Vendoring*, below); that doesn't soften the
coupling, it sharpens it — this page is no longer only a tool someone else
runs, it's part of what this edition serves.

**Markup hooks it depends on:**

| Hook | What is read from it |
|---|---|
| `<li class="reg" id="rN">` | one person; `N` is the **id** |
| `.num` `href="#pN"` + its text | the id and the **printed number** — distinct, get this backwards and either a synthetic id prints or a search jumps to the wrong person |
| `.sex` `.name` `.alt` `.blank` `.age` `.clan` `.vital` | the fields |
| `sic-ring` on `.sex`/`.clan` | the plate's value is a misprint |
| `data-reading` on a ringed `.sex`/`.clan` | the edition's own reading behind it (six in the edition, all on Genealogy III) — **their gate 1 fails without it** |
| `.reg-rel[data-rel]`, `data-with`, `data-editorial`, `a.edmark` | every relation, and which attribution is editorial |
| `.node` nesting depth + `.tree`'s `margin-inline-start` multiplier | **generation** — never printed directly |
| `.xref` directly after a `.line#pN` | that person's cross-reference |

Two non-obvious consequences: **`dotted()` is not reversible** — it appends a
period unless the value already ends in one, so "d. in childhood." and "d. in
infancy" render identically and a parser can't tell them apart (nothing here
is wrong; it's a cost the consumer pays). And **a misprint's underlying reading
is published on purpose, since 2026-08-17** — `sic-ring` still marks that the
*printed* value is what the plate shows (the edition annotates a misprint, it
never corrects one), but `data-reading` on that span carries the transcription's
actual reading, because `laguna-search` has no `PERSONS` to read from (it only
parses these pages) and previously guessed at a misprinted sex by filing the
printed letter under both `sex` and `sexPrinted` — which published Genealogy
III·37 as a man, unfindable as a woman. **Generalise it: when a downstream
consumer can't see something, check whether it can be published before
designing a fix on their side.** Dropping `data-reading` from a ringed span now
fails their build; that's the intended coupling. Since 2026-08-18 (`80e0d2d`)
the `sic` tooltip **names the reading** — "the edition reads Badger" rather
than "the edition's reading differs," which used to tell a reader something
was wrong without saying what. What the tooltip did **not** change is the
displayed value: `sexOf()`/`clanOf()` still show the plate's `M.`/`Bager`,
ringed — the edition annotates a misprint, it does not correct one, there or
here. It also surfaced a copy trap worth knowing before touching either
function: **a sex reading is a label carrying its own period (`F.`) while a
clan is a bare word**, so appending a period unconditionally gives "reads
F.." — `dotted()`'s rule turning up in a second codebase.

Restructure the register freely; just expect `laguna-search` to need its
parser updated, and run its `tools/validate.py`, which compares all 713
entries and every relation against `scripts/transcription*.py`. **It does not
check that tool's fold map** — its own docstrings claimed otherwise until
2026-08-08 and were wrong; the map's only guard is `gate_keys_are_folded`,
below. Don't assume a check exists because a comment says so.

**A name's diacritics are a second coupling surface**, independent of the
markup hooks above — see `memory/facts-worth-knowing.md`'s `_FOLD`-map rule for
the always-loaded half of this. Two of that tool's own literal sets matter when
a character is genuinely new to a name: **`NAME_VOWELS`** (where the
name-break walk-back must land) and **`NAME_MARKS`** (marks the walk-back steps
*over* — note a modifier mark like U+02BD/U+02BC is Unicode category Lm, so
`.isalpha()` is true and an unlisted one gets read as a consonant; that's why
`ʼ` is listed explicitly). **Only the `FOLD` map in `src/search.js` has a gate
that catches every case** (`gate_keys_are_folded`, loud). The vowel/mark
classification only has **gate 5**, which fires solely for a single-word name
of 14+ characters — a shorter name silently loses its break seams and fails
nothing. So a genuinely new character needs classifying in **three** places
over there: `FOLD` in `src/search.js`, and either `NAME_VOWELS` or
`NAME_MARKS` in `build.py`. Nothing breaks on this side either way — flagged
because the failure lands in a different repo from its cause, and half of it
is silent there.

**Two more gates on the other side, both noisy by design, not bugs to route
around:** a namesake-collision gate refuses to build until every pair sharing
a folded name/sex/clan has a hand-written verdict (three exist today;
correcting one diacritic here is enough to create a fourth); expect to
adjudicate after a name edit. And their two validation checks
(`tools/validate.py`, comparing all entries/relations against this repo's
transcription modules) **read a CACHE of this site by default** — running
either to verify a publish proves nothing without `--refresh`; the only tell
is one word in the first line of output, `cached in cache/` vs `re-fetched`.
**After any publish here, the first run over there takes `--refresh`.**

## Vendoring: `/search/` is the only page `make_chart.py` doesn't write

`laguna-search`'s `dist/` is copied into `vendor/search/` (`index.html`,
`search.js`, `search-index.json` — CSS is already inlined);
`vendor/search/SOURCE.md` records the source commit. **`write_search()`** wraps
that into `docs/search/`. **Both directories are generated — never hand-edit
either**, exactly like `docs/` generally.

`write_search()` deliberately does the least it can — it wraps, never
rewrites, injecting exactly six things the vendored file can't supply on its
own:

1. **The subset font** — `search.css` declares no `@font-face`; names arrive
   from JSON at runtime and appear in no HTML file, so `subset_font.py`'s own
   coverage check can't see this page at all. Verified by hand at publish.
2. **A host bar** (`.lg-host-bar`) — the widget draws no navigation, so a
   reader landing here needs a route back. Its metrics are derived from the
   masthead's own tokens (`--font-ui`, `--tap`, `--bar-h`, etc., emitted under
   the site's own names — a build guard aborts if the vendored file ever
   declares one of them), so diffing the two should show only selectors and
   colours changing. One rule is genuinely its own, not the masthead's:
   `box-sizing:border-box`, scoped outside the widget's own reset — omit it and
   the *same* declarations build a visibly different bar (65px vs 49px tall).
   Search sits in it, marked `aria-current="page"` rather than linked (a link
   to the page you're on is a dead control).
3. **The theme key + default palette** (`THEME_KEY_DECL`) — spliced right
   after the charset meta, before the vendored boot script reads it; the build
   **aborts** if that meta is missing. This site defaults `/search/` to light
   (matching every other page) rather than the widget's own system-preference
   default — set host-side, not as a widget option, because "default to light"
   is this site's decision, not the widget's. **Since 2026-08-09 there is one
   storage key** (`lg-theme`, taken by the widget as configuration) — do not
   reintroduce a second key or a bridge between two keys; that was the defect,
   not the starting condition.
4. **The h1 size**, 5. **the standfirst**, 6. **the double rule** — the widget
   sizes all three for standing alone as a full page; here they're read
   directly out of this site's own CSS rules (never restated as literals) so
   they inherit the site's ramp instead. Build aborts if any of those source
   rules stop stating what's read from them.

**Test for what belongs here vs. upstream in `laguna-search`'s own
`src/search.css`: would the widget standing ALONE want this change?** If yes,
it's upstream (e.g. the Clan-menu checkbox fix, the search card's one-line
control row, the theme control's move to the foot, `color-scheme` following
`[data-theme]`). If it's specific to *this* host — defaulting the palette to
light — it's a host injection. Anchor a host override to the specific vendored
rule it depends on and fail the build when that rule moves, rather than
silently drifting; but reach for upstream first.

**The person-list ("Index") layout is a table at every width, and pans rather
than stacks below 651px window width — decided, not a defect.** A report that
`/search/` is "broken on phones" is re-litigating this; the one legitimate
exception ever found was `.lg-host-bar` using `position:sticky` (which doesn't
stick horizontally) — fixed 2026-08-17 with one `body{width:fit-content;
min-width:100%}` declaration, no change to the bar itself. Current measured
figures, re-confirmed 2026-08-22: **pan threshold 651px window / 636px client
clean / 635px pans**, moving 1:1 with the Name column's floor (a wider Name
column trades pan threshold for nothing on row height, which is the **Clan**
column's cost, not Name's — `Chaparral Cock` at 89.49px is what makes a row
tall, and a wrapped name does *not*, since two name lines fit inside a flat
row's content box). Full history of the four superseded measurements that
preceded these final numbers, and why the vendored `src/search.css` still
carries an older figure in its own comment (correct on next re-vendor, not
here): `reference/history/search-pan-threshold.md`.

Two structural things worth knowing before touching layout here: `.laguna-search
.cell.name` is declared **twice** in the vendored stylesheet (base rule + the
860px media query) — change one and the other silently disagrees; both live
upstream. And a Clan-menu dropdown on a panning page must bring itself into
view **horizontally only** (`panIntoView()`, not `scrollIntoView`, which would
drag a sticky-headed page vertically instead) — the menu is placed in document
coordinates while clipping is the viewport's.

**Two specificity traps in that stylesheet were live for months before either
was caught — expect a third.** `.laguna-search .row-summary .grid` is
(0,3,0) and carries the row's inline padding, so a rule written at just
`.grid` — (0,2,0) — reaches the **header and not the rows**; that's how the
column names sat 4px left of their values from 861–1120px. Any breakpoint
touching that padding must name both selectors. Separately, the **Clan menu
lives inside `.head`**, so a rule at `.head input` reaches its option
checkboxes too — below 860px that rule won on source order over
`.cbf-option input` and turned every option into a 44px block, no labels
visible. Both are now guarded with `:not([type="checkbox"])` in the base rule
and the media query, but the fix is source-order-dependent, not
specificity-proof — restating either rule later can silently reopen it.

## Re-vendoring — decide from the register-markup diff, not from which files moved

**The re-vendor loop is `/publish` Gate 8, and `--refresh` is not optional
after any publish.** The index goes stale the moment the register's markup
moves, and nothing here can detect that automatically — a stale index is still
valid JSON that renders a working page. **The test for whether a re-vendor is
due is a diff of register-bearing markup (`.reg`, `.reg-rel`, `.num`, `.xref`,
`sic-ring`) per table page, not a memory of what changed** — a CSS-only change
across all four plates can leave that diff at 0.

Four shapes have been observed for what moves together on a re-vendor, and
**only the register-markup diff above decides whether `--refresh` is owed** —
never infer it from which of the three vendored files changed:

1. Only `search-index.json` moves (data-only change here) → `--refresh` owed.
2. Only `index.html` moves, `search.js`/`search-index.json` byte-identical
   (upstream CSS-only fix) → **no** `--refresh` obligation — a change that
   parses to the same thing hasn't staled the index.
3. `index.html` and `search.js` both move, `search-index.json`
   byte-identical (upstream markup + CSS change) → confirm at this end via the
   register-markup diff; don't infer from the file list.
4. `search.js` and `search-index.json` both move, `index.html`
   byte-identical (upstream script+data change) → same: confirm via the
   register-markup diff, not the file list.

Regardless of shape, **run `leak_report()` by hand over all three vendored
files every time** — `check_published_pages()` only opens `.html`, so
`search.js` and `search-index.json` are never swept by the normal build. And
never decide a re-vendor is due from `meta.generated` (date-granular, moves
every day regardless) or from the upstream repo's commit hash (a data change
here stales the index even when that repo hasn't moved).

**One inversion of the normal build order is sound, but only when shipping in
the same publish**: if the index needs a change that's *in* these pages but
not yet live (e.g. `data-reading`'s rollout), seed `cache/` with the local
`docs/` build, run `build.py` without `--refresh` against it, vendor that
result, and ship both together — verified after the fact by the normal
post-publish `--refresh`. Don't reach for this shortcut for anything not
shipping in the same publish.

`/search/` carries `<meta name="robots" content="noindex">` and is
deliberately absent from `sitemap.xml` (consistent with the exposure posture
in `memory/standing-decisions.md`, not a de-indexing measure — that question is
separately closed). If that meta is ever dropped, add the path to
`write_site()` in the same commit.
