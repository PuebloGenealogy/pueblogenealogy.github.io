## Where things are

| Path | What |
|---|---|
| `scripts/make_chart.py` | **The whole renderer** — CSS, JS, HTML, SEO, layout |
| `scripts/transcription*.py` | The 1923 baseline as data. Immutable — *except* to record what the plate actually prints, e.g. `PLATE_NUMBER_MISPRINTS` |
| `docs/` | Generated site. Never hand-edit |
| `assets/og-cover.jpg` | Social card, derived once from the plate scan (see `OG_IMAGE`) |
| `sources/` | Source scans, in repo but not served |
| `METHOD.md` | Editorial method — why readings are made as they are |
| `CITATION.cff` | How to cite. Carries **no doi**, deliberately — see *Release policy* |

There is **no `.zenodo.json`**; it was deleted 2026-08-08 with the rest of the
Zenodo surface. Identity is now two constants at the top of `make_chart.py`:
`SITE` and `REPO`. Every canonical, sitemap entry and card derives from them.
A `DOI` constant sat beside them until 2026-08-08 and must not come back.

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

**A block that starts partway down the tree needs its own starting column, not
generation 0** — which is what Genealogy II does twice: measured on the scan
2026-07-30, person 1 sits at x 225 and person 3 — generation 2 — at x 1425,
while the lower block's 154 sits at x 1340 and 232 at x 2690, the same column
as 164, who is 154+155's own child. `spec["root_columns"]` in `TABLES` sets
the starting column (`{154: 2, 232: 3}`), applied as a `margin-inline-start`
on the `.tree` stated in `--col`/`--stub`, so generation *d* still lands at
*d* × (`--col` + `--stub`) and drift stays 0 — verified at 425.59px step,
spread ≤ 0.008px across all six. **Do not reach for `UNATTACHED_BLOCKS`
here**: the lower block is not descended from the upper one, so splicing
would assert a containment the plate does not, and it would hit the
last-child rule anyway, because the plate's vertical ends *on* 164 with
nothing beside 232 at all (bracket-column strip x 2480, y 9900). The
independent check that these two columns are right is that the `generation`
field — derived by walking the tree, never read off the plate — already
stored 2 and 3 for them.

## Design invariants

Four rules that look like styling preferences and are not:

1. **The root font size is pinned at 16px.** `GEOM` states the plate grid in rem
   against it, so changing the root rescales `--col` and `--stub` and breaks the
   drift invariant. The `--t-*` ramp exists to size **chrome and prose only** —
   nothing inside `.sheet` is sized from it.
2. **A selected or hovered `.line` may change `background`, `box-shadow` and
   `outline` — nothing else.** Padding, border or height there moves the row and
   throws the sibling bracket off its `mother_row`. All three selection
   highlights draw **outside** the border box for the same reason an inset
   shadow or hugging outline would otherwise disturb the text.
   **Which mechanism lights a chart row depends on `html[data-card]`** (set in
   the `popoverOK` block, meaning *the card script is running*, not *JS is
   on*): with it, `.is-selected` only, owned solely by `markSelected()`;
   without it, `:target`, which is all a no-JS reader has. Both must never be
   live at once — `:target` cannot be cleared by a click, so two rows lighting
   at once was a real bug (2026-07-29). Anything that selects a row goes
   through `syncSelection()`; `cardRow` exists because the popover's `toggle`
   and `hashchange` arrive as tasks in no guaranteed order.
3. **`--rule` is not text.** `body.chart` flattens all text to `--ink` by
   redefining `--muted`; the brackets and leader rules are deliberately excluded,
   because they carry the genealogy's structure.
4. **`--tap` floors every hit area** in the site chrome, and `--bar-h` derives
   from it so anchor `scroll-margin` tracks the bar. Don't restate either.

**The table pills carry the roman numeral alone at every width** (user,
2026-08-10) — this looks like a bug and isn't. The word "Genealogy " stays in
the markup and each link's accessible name; `.masthead nav .nav-word` only
hides it visually, since "I" alone is not an actionable link name by ear. **Do
not delete the span.** The same hiding rule exists twice on purpose — once in
the site masthead (`.nav-word`), once in `/search/`'s host bar (`.lg-hb-word`)
— keep them in step rather than merging them, so widening one never silently
unhides the other. The wordmark reads **"Home"**, not the edition's name, on
every page including `/search/` — it's a way back, not a nameplate. The
`≤26rem` rule that trades the Search label for a glyph is scoped to
`.mast-right` specifically, not shared with the pills' own hiding rule — two
selectors on purpose, so widening one never silently unhides the other.

**A table page's title block is the plate label, the numeral, the double rule
and the statistics line — no citation.** The landing page keeps its citation.

**The person card is a regrouped copy of the register entry, and every
card-specific rule must stay scoped to it.** The card clones `#r{n}` — one
source of truth, and the register is also the no-JS person card — then rebuilds
it in `openCard`. A CSS rule written without a `.pcard` prefix, or a DOM edit
made anywhere but the detached copy, silently reformats the register below the
plate. After any card change, verify the register still computes relation links
`display:inline` and entry titles 16px. Two traps already hit: chips are
`.reg-rel > a`, **direct children only** (a cross-reference row is also a
`.reg-rel`, with links inside an `<em>` of running prose); and the phone reset
of the column divider must **out-specify** the pair rule
(`.pc-col + .pc-col` is (0,2,0) against (0,3,0)), which it failed to do until
2026-07-29. The card pairs children to a spouse from `data-rel`/`data-with`,
**never** by reading the label — digging a number out of prose is exactly the
mistake `_p()` exists to prevent. A relative's row is sized from `--t-base` —
the size a person gets in the register and on the plate — never from the
chrome `--t-*` ramp; it's a person line, not a caption.

**There is no on-page chart key, by decision.** The footer's *Navigating this
chart* list is the **only** place `+` (spouse), `F.`/`M.` (sex) and the leader
rule are decoded — don't rebuild a key without saying what changed, and don't
fold that footer section (see below): thinning it re-opens a defect already
introduced twice.

In the plate bar, Find sits left and Scale right on an **auto start-margin on
`#scale-mount`, never `justify-content:space-between`** — `#find` carries
`[hidden]` until scripted, so space-between would strand Scale for a no-JS
reader. The bar has no max-width; it rides the plate's rail on `.scroll`'s own
padding. It was centred at `--measure-wide` until 2026-07-29, which matched
the title block's box and so aligned with nothing a reader can see — the
statistics line inside that box is centred text, inset roughly 270px each
side. Putting it back on a measure means it has to move with `.scroll`'s
padding, or the rails part again.

`.plate-caption` carries the pan hint and nothing else, so the **caption** is
what hides above 1400px and in print — hiding only `.pan-hint` would leave an
empty `<figcaption>` holding its bottom padding open.

**The generation ruler is two bands, not one** — its identity chip
(`.ruler-chipslot`) floats at `flex-start` over whatever's panned to that edge,
labels stay at `flex-end`, and `.ruler`'s height is the only thing keeping the
chip from eating the first half of a label. Print returns that height to `2rem`
since the chip is hidden there; shrinking it elsewhere reopens the collision.

`--muted-fixed` is the real `--muted`, captured at `:root`, for anything that
must keep the dimmer grey through invariant 3's flatten — currently `.imprint`
(statistics line, matching the landing page's `.c-stats` grey: 6.15:1 light,
6.73:1 dark) and the person card's `.pc-title .vital` (so a death/birth note
reads as metadata rather than part of the name: 5.28:1 light, 5.69:1 dark).
Everything else on a table page stays `--ink`; adding a third use is
re-opening the colour decision — measure the contrast if you do.

**Theme has no Auto/system state — the default is LIGHT, decided in CSS, not
script.** `:root{color-scheme:light}` makes `light-dark()` resolve light with
the script dead, blocked or still parsing; the old `prefers-color-scheme`
fallback block is deleted on purpose and must not come back, since it restores
OS-follows-you exactly in the no-JS case nobody looks at. `applyTheme()`
defaults to `"light"` to agree; both halves change together or a dark-OS reader
gets a light page whose button lies. A stored choice still wins in both
directions, and nothing is written to storage until the reader presses the
button. One `<meta name="theme-color">` per page, not a media-keyed pair —
a media-keyed pair put dark browser chrome around a light page on a dark OS
until `applyTheme()` rewrote it, and permanently on the 404, which ships no
script. The control sits at the **foot** of every page (user, 2026-08-10) via
one shared `THEME_FOOT` string: chart pages take it after `</footer>`, the
landing page after `.prose` at `--measure`. It keeps `.mast-btn`'s shape and
the `--tap` floor, and it's named in `@media print` because hiding
`.masthead` used to cover it and no longer does. The 404 still has no theme
control at all — no script, and the button is authored `hidden`.

The footer is a two-column grid of `.app-sec` sections (grid of whole
sections, not multicolumn, so a heading never breaks from its list), one
column below 56rem. **Three of its five sections fold — *Editorial notes*,
*Provenance*, *Citation*** — and two deliberately do not — *The record* and
*Navigating this chart* — because those two orient a reader who just arrived.
The disclosure is the same idiom the landing page's FAQ and the register
already use — marker, sizes and hover identical on purpose — and the `<h2>`
sits inside the `<summary>`, so the apparatus still has five headings for a
screen reader; `cite_html()` no longer emits its own for this reason. Two
things a folded section must not break, both already solved: a deep link
into it (`openDetailsFor()`, keyed on `getElementById`, so a new linkable
footer note just needs an `id`), and print (every section opens via
`::details-content` plus a `beforeprint`/`afterprint` handler that restores
whatever the reader had folded).

The misprint ring is an **`outline`**, never border or padding — a border
widens the row and throws the sibling bracket off its `mother_row`. It's
counted as its own row (`row += 1`), same as a cross-reference row, so
everything below stays on the `--lh` grid.

**Every in-block row must be an exact whole number of `--lh`, including
`.xref`.** `Chart.render` budgets one `--lh` per `row += 1`; `.xref` used to
ship with block padding that put seven of Genealogy II's brackets 3.7px off
their mother's line (2026-07-29) — it's now `line-height:var(--lh)` with zero
block padding. Table 1 measured clean throughout only because no group there
happens to have a mother's line below an xref row — the defect was latent
until a six-generation, 30-cross-reference plate arrived, which is why this is
an invariant rather than a one-off fix. Unsolved case: a cross-reference that
**wraps** costs two rows against a one-row budget; none does today, and there's
no font-metric guard for it, so split a long reference at the plate's own line
break with `|` rather than let CSS silently mis-budget the row count.

**A row's height is STATED (`height:var(--lh)` on `.line`/`.sic-row`,
`min-height` on `.xref`), never inferred from the line box — `line-height`
alone does not carry it.** WebKit quantises a line box to a whole pixel while a
margin stays at LayoutUnit precision (24.000px rendered against a declared
24.799999px); Chromium does not do this, which is why the defect survived from
launch to 2026-08-10 unnoticed — 69 of 141 brackets were off their mother's
line in Safari alone. **Do not "simplify" these back to `line-height` alone.**
`.xref` keeps `min-height`, not `height`, on purpose — it's the one row type
that wraps, and capping it at one row would make an overlong reference overlap
the row below rather than merely mis-budget it. (Full discovery narrative:
`reference/history/webkit-and-measurement-postmortems.md`.)

**Three colours on a table page are not `--ink`, and a fourth needs the same
evidence**: `--sic` on the misprint annotation (clears 4.5:1 on both papers
alone: 6.16:1 light, 7.84:1 dark — stated in `make_chart.py`'s own token
comment and independently recomputed 2026-08-23), `--muted-fixed` on the
statistics line, and
**`--clan`** on the clan field. `--clan` is *not* the reverted 13-hue per-clan
palette (which collapsed under deuteranopia) — it's one colour for the whole
field, distinguished from `--ink` in both lightness and hue, measured 5.86:1
paper-light / 9.53:1 dark, 6.22:1 / 10.40:1 on a selected row. It shares
`--accent`'s value but is a **separate token on purpose**, since `--accent`
means *interactive* everywhere else and recolouring chrome must never
recolour the genealogy. Declared in all five palette blocks; missing a static
fallback leaves that
browser's clan unstyled.

### The register markup is a published interface — read before changing its shape

**`.reg`, `.reg-rel`, `.num`, `.xref`, `sic-ring`, `data-reading`, and the
`.node` nesting depth are not just this site's rendering — a separate tool,
`laguna-search`, parses these exact hooks out of the built `docs/*.html` pages
to build `/search/`'s index.** Changing what `person_line()` or the register
emits, or changing the four transcription modules' `_FOLD` maps (see
`memory/facts-worth-knowing.md`), can silently break that parser or its
namesake-collision gate on the *other* side of a re-vendor, with no warning
from this repo's own build. **Before changing register markup, `write_search()`,
or a name/diacritic that could shift `_FOLD`, read `.claude/rules/search-integration.md`
in full** — it triggers automatically when you open a file under
`vendor/search/` or `docs/search/`, but editing `make_chart.py` or
`scripts/transcription*.py` directly does not, since both are large
multi-purpose files a path-scoped rule can't isolate down to the relevant
functions.
