# `/search/` pan-threshold — measurement history

Not auto-loaded. The current, final figures live in
`.claude/rules/search-integration.md`; this file is the story of how they were
reached, kept because the vendored stylesheet's own comment still cites an
older number and someone re-vendoring needs to know it's superseded, not wrong.

**2026-08-09 — the list layout decision itself.** The user set the person list
("All people," later renamed "Index") to stay a table at every width and pan
rather than stack below some threshold, replacing a stacked-card layout below
860px that turned a 56px row into 153px and the header into 270px. The pan
works because `.card.people` takes `min-width:min-content` — `minmax(0,1fr)`
and `min-width:0` are the enemy once the table sets the page's width, since a
zero floor lets the inner grid stop short of its own minimum and the columns
slide under the surrounding chrome. The search card that sits above the list
hit the identical trap independently: `.card.search` needed the same
`min-width:min-content` treatment below 860px (a `min-width:0` item
contributes nothing to its track's minimum, so it first resolved to 345.6px
with a 190px name box crammed into a 161.8px column), and `.laguna-search`
itself needed `min-width:min-content` too, or the narrower card stopped
~95px short of the list's right edge. Both floors release below 860px.

**2026-08-10 — first measured threshold: 675px window.** With the Sex column
at its original 124px width (its floor being the widest `<select>` option,
then "Not recorded"), the document panned at a window width of 675px (636px
document clean, 635px pans — see below for the distinction).

**Same day — the Sex column narrowed, and the threshold moved with it.**
Shortening the unrecorded-sex option's label from "Not recorded" to a dash
took the widest option from 124px to 71.78px of needed width, and the column
from 124/124/104px across three breakpoints down to a flat 80px. The pan
threshold dropped by exactly the pixels the column gave up: **651px window**.
**Lesson that generalises**: a column's floor is set by its *control*, not by
how wide its printed values look — `M.` and `Corn` say nothing about it. A
placeholder is the same kind of input read the other way: it doesn't widen its
column, it gets clipped by it. Relabelling Death's filter to "Year or d."
(52px) clipped to "Year or d" at the narrow layout, losing the trailing period
that IS the value; "Year / d." fit by 1.2px, no real margin; it shipped as
"Year/d." (40px loaded, 37.6px fallback), with the full phrase moved into the
`aria-label`, which has no width constraint.

**Two different quantities both looked like "the width it pans at," and this
file conflated them for a session before they were told apart:** the
*document's* client width at which panning is clean (636px) vs. the width at
which it starts (635px) vs. `scrollWidth` at phone widths (617px at 375–480px,
641px before the Sex-column narrowing). All three were re-confirmed
2026-08-22: 636 clean, 635 pans, 617px `scrollWidth`.

**A separate, larger claim — "~756px as a window width" — was tested and
settled as the right SHAPE, just not the right number to act on.** The
threshold moves 1:1 with the Name column's floor, verified at five floors
(140→660, 150→670, 170→690, 190→710, 210→730px client width, each exactly
`636 + (floor − 116)`). A 221px-floor Name track (⇒ 756px window) would work,
but it's wider than the job needs: **0 of 620 names break at a 200px floor**
(720px client / 735px window). Widening the Name column costs the pan
threshold pixel-for-pixel and buys nothing on row height, which is entirely
the Clan column's cost (`Chaparral Cock` at 89.49px against a 76px track,
natural width **43 of 620 rows exceed 56px below the (860px) pan threshold —
42 of them, plus one `Chapparral Cock`, the double-p misspelling that is
III·50's own known plate misprint, not a transcription slip. At 860px and
above, exactly one row is still tall: that same misspelling, at 97.11px
against the widened track's 92px maximum — the 42 correctly-spelled rows go
flat once the layout widens**).

**The SIZE of the name font is NOT a second lever on the threshold — measured,
not reasoned, 2026-08-10.** The intuitive expectation (smaller name → narrower
content → earlier pan) is wrong: the Name column is a fixed 116px track in the
narrow grid, and the name's own rendered width never reached that track's
floor. Dropping the font from 1.15rem to 1.05rem left the threshold exactly at
675px (the pre-Sex-column number, at the time this was tested). What font size
*does* move is wrapping, and it moves it a lot: 12 of the first 60 rows wrap
down to 4 at 375px.

**Names still wrap on `/search/`, deliberately — where a name breaks is an
editorial `<wbr>` decision, ratified 2026-08-08.** Re-measured across all 620
rows on 2026-08-22, in Chromium at real viewports, the true figures are: **32
names take two lines at or below the pan threshold, and 21 still do at 860px
and 1120px.** The figures this file carried before that walk — 4 of the first
60, 12 before the name size came down — were only a 60-row sample; the whole
index had never been walked. **In that same 60-row sample the true split is 3
names wrapping and 4 tall rows, and they are not the same rows** — the
near-match of those two counts (3 and 4) is what made an old, wrong claim
("shrinking the font returns every row to a flat 56px") look self-consistent
for nearly a year. **A wrapping name does NOT make its row taller.** The
row-height cost belongs to the Clan column: two lines of name are 37.63px
against a 38.4px content box, so a wrapped name fits inside a flat row, while
tall rows are a Clan-column phenomenon in every case but one (below).

**The vendored stylesheet (`src/search.css`, in the separate `laguna-search`
repo) still carries a comment citing the pre-Sex-column numbers** — "measured
675px before and after, panning at 674 either way." The claim it makes is
still true; only its figures are superseded, by the Sex-column change later
the same day. Correct it there on the next re-vendor of that project, not
here.
