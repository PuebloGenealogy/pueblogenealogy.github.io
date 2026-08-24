# WebKit and measurement postmortems

Not auto-loaded. The durable rules these produced are stated tersely in
`memory/architecture-and-design.md` and `memory/measurement-gotchas.md`; this
file is the discovery story behind the ones dense enough to be worth keeping.

## The WebKit line-box quantisation defect (found 2026-08-10)

A row's height in the chart is now stated explicitly (`height:var(--lh)` on
`.line`/`.sic-row`, `min-height` on `.xref`) rather than inferred from
`line-height` alone — every vertical offset is a multiple of `--lh` expressed
as a margin (`.kids{margin-top:calc(var(--lh) * N)}`). The reason: a margin is
a length, and an engine keeps it to LayoutUnit precision — measured
**24.796875px**. A line box is *not* a length, and **WebKit quantises it to a
whole pixel**. Measured directly in Safari 26.3: every row box rendered
**24.000px** against a declared line-height of 24.799999px, so each row of
accumulated offset lost 0.796875px going down the tree — **69 of 141 brackets
ended up off their mother's line**, worst case −20.016px (25 rows × 0.797px)
at Genealogy III's 21→74. The sign tells you where the mismatch sits:
positive on a `.kids` group, negative on a `line_pad` push inside a block.
Chromium reported 24.797px for the same declared value and was clean to
0.003px — which is exactly why this shipped at launch and sat undetected for
weeks: every measurement taken in the (Chromium) preview pane was fine.

**What it looked like before it was diagnosed correctly: a break in the
leader rule.** At III's 113→204, the error was exactly one row (0.797px), and
204 is an only child — so `:only-child::after` draws no bracket vertical to
bridge the step, and the break was visible as a horizontal seam. It was
reported as "a break in the line" and diagnosed twice as a horizontal paint
seam before the real cause was found; a 1px overlap patch on the abutting
rules was tried, fixed nothing, and was reverted. There are 29 only-child
groups across the four plates (I: 5, II: 5, III: 15, IV: 4), and they are the
*only* places a sub-pixel row error is visible at all — everywhere else the
bracket's own vertical stroke covers the gap.

## The generation-ruler two-band layout (no single incident date, but the reasoning is worth keeping)

The generation ruler is two bands, not one, because its identity chip
(`.ruler-chipslot`) is a zero-width slot pinned to the inline start — it
floats over whatever content has been panned to that edge. Tried as a single
band with the labels, the chip's opaque fill ate the first half of a label
("GENERA|TION 2"). Splitting into two bands (chip at `flex-start`, labels at
`flex-end`) fixed it, and `.ruler`'s height became the only thing keeping them
apart — which is why print returns that height to `2rem` (the chip is hidden
in print) and why shrinking it elsewhere silently reopens the collision.

## Font-substitution and the "measurement available is not the measurement needed" family

Several distinct traps share one underlying lesson: what's *easy* to measure
in a given tool isn't necessarily what the question actually needs, and each
of these produced a plausible, wrong-looking-right number rather than an
error.

- **Font substitution**: macOS silently substitutes a missing glyph with
  something plausible rather than failing, so an on-screen check on a Mac can
  never prove the *absence* of substitution — only reading the embedded
  face's cmap can. This is the same asymmetry as the WebKit-vs-Chromium
  measurement gap above: the environment you can easily test in isn't always
  the one the question is actually about.
- **The preview pane is Chromium, and the edition is read in Safari.** A
  preview-pane measurement can show a change is *inert* (geometry unchanged)
  but can never show it *works* on the engine that has the behaviour in
  question. This cost two fixes on 2026-08-09, and the first one shipped
  simply wrong before a Safari check caught it.
- **A narrow-viewport check in the preview pane doesn't simulate what it
  claims to** — the pane widens to fit content rather than clipping at the
  requested width, so a 375px `resize_window` against 641px of real content
  reports `innerWidth: 648`, not 375. There's no pan to photograph because the
  pane grew instead. The fix is a fixed-width iframe, rendered visibly and
  screenshotted, with `f.contentWindow.innerWidth` read directly rather than
  inferred.
- **A blank screenshot means a zero-sized viewport, not a scroll bug** — the
  browser pane can come up reporting `innerWidth`/`innerHeight` of 0, which
  captures nothing and, because scrolling a zero-height viewport changes
  nothing either, presents as "screenshots work at scroll 0 and nowhere
  else." Read `innerWidth` before trusting anything you see; fix with an
  explicit `resize_window` at `1280x900` rather than a named preset, which
  didn't reliably restore it.
- **Confirmation from the user is only evidence if you know which build they
  were on.** A scroll-freeze symptom was once reported "clear" on 2026-08-09
  — on the live site, which carried no fix. An absence observed on an unfixed
  build says nothing about whether a fix works; a fix that can't be
  distinguished from the bug's own intermittency hasn't actually been tested.
