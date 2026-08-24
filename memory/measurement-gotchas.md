## Measurement gotchas

**The recurring failure mode: a measurement that returns a plausible wrong
number instead of an error, usually because what's easy to measure isn't what
actually needs measuring.** Every gotcha below is an instance of that; look
for the pattern before trusting a clean-looking result.

- **Measure a bracket against the first `.line` in a group, never the first
  `.node`.** They're not the same element. When two sibling groups share one
  `mother_row`, `Chart.render` pushes the mother's line down with `line_pad` —
  a margin *inside* the block — so a node-to-node measurement reads 0px while
  the name itself sits a row lower. This is how "all 55 brackets on their
  mother's line, max 0.016px" was reported for a page with one a full 24.8px
  out (person 169, since fixed by `SECOND_VISIT_OMITTED`).
- **Derive the expected leader from the TRANSCRIPTION, never from the DOM.**
  An audit that matches each bracket to the *nearest* `.lead-line` reports
  0.00px for a bracket hanging off the *wrong* row too, because the nearest
  line is whichever one it happens to have landed on — it's circular, and it
  passed on the exact case it existed to catch (all four plates "clean" while
  Genealogy IV drew 20 as 6+7's child). The audit that works reads `_GROUPS`,
  finds the union's mother (or its `LEADER_ON_SPOUSE_ROW` spouse), and asserts
  the bracket starts on *that named person's* line — cheap, and it doesn't
  have this hole.
- **An audit comparing two quantities that move TOGETHER passes on the exact
  defect it exists to catch.** "Does each data cell sit at its column
  heading's left edge?" reported 0.00px drift at every width while the whole
  header was sliding under `Table · #`, because heading and cell overflowed by
  the same amount. When an audit compares A to B, ask what happens if both are
  wrong in the same direction — if the answer is "it passes," it needs a
  third, independent reference. **And look at the thing at least once**: two
  measurements agreeing is not evidence they're right.
- **Three DOM measurements that return a plausible wrong number, not an
  error:** `innerText` sweeps in child elements (a namesake marker on its own
  line got counted as wrapped text); `scrollWidth` clamps at the box under
  visible overflow, so it can't tell you how much wider than its column
  something wants to be; `white-space:nowrap` doesn't stop a break at
  `<wbr>` in Chromium, so it isn't a way to measure natural width here. The
  measurement that works is an off-screen clone with the computed font copied
  onto it. **That `<wbr>` finding was measured in Chromium only — Safari/WebKit
  was not tested, and the edition is read in Safari.** Confirm it there before
  relying on it for anything; this project has already found one WebKit-only
  rendering divergence (the line-box quantisation defect, see
  `memory/architecture-and-design.md`), so cross-engine agreement here is not
  assumed.
- **Under CSS `zoom`, never mix `getComputedStyle` with
  `getBoundingClientRect`.** Computed styles come back unzoomed; rects come
  back zoomed. Adding a pseudo-element's computed `top` to an element's rect
  fabricates a constant error (`v − v × zoom`) that looks exactly like a real
  misalignment growing as you zoom out. Measure alignment from element rects
  only — the tell that a "misalignment" is really this trap is that the error
  *normalised to rows* is identical at every zoom level.
- **Check the built file, not only the rendered page.** A DOM read happens
  after the page's own script has run, so it can't see what the HTML actually
  ships — `applyTheme()` rewriting a label is invisible to a check that reads
  the live DOM. For anything that exists in the markup itself — labels,
  attributes, structured data, leak markers — grep `docs/`.
- **Never read structure off a downscaled plate overview.** A downscale loses
  exactly the thin rules that carry the genealogy, so it will misplace people
  while looking perfectly legible. Use an overview for orientation and tile
  planning only.
- **Indentation does not establish descent — a leader stub does.** Read the
  bracket column as its own narrow strip (the vertical and every stub entering
  it, nothing else in frame) and count stubs; the clan check won't save you
  here, since a person can share a clan with the bracket he merely sits beside.
- **"Not a child" and "not drawn here" are different findings with different
  mechanisms.** A plate can *print* a couple somewhere it doesn't *descend*
  them from — `UNATTACHED_BLOCKS` splices the block into the right column
  while withholding only the leader stub, so the vertical still passes the row
  as it does on the plate. Separately, a block the plate merely *indents*
  (rather than starting at the sheet's left edge) is not automatically a
  generation-1 root — `root_columns` sets its starting column explicitly, so
  drift stays 0 without asserting a containment the plate doesn't draw.
- **A half-read plate is never registered in `TABLES`.** The renderer builds
  every registered table on every `--public` run, so registering early is how
  a partial genealogy reaches `docs/`. Register only after `self_check()`
  passes, never as a way to preview progress.

**Plate-audit-tool specifics — calibration numbers, the bracket bench,
`stubs.py`, per-table thresholds — are not here.** They load automatically
when you open a file under `scripts/plate_audit/`; see
`.claude/rules/plate-audit.md`.
