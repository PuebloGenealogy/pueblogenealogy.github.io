# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-30**, after a session that fixed the first of the user's
reported placement errors on **Genealogy II** and found one it did not fix.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch table-ii-transcription`.** The work is on a branch, and there
   is an open **draft PR #14**.
2. Read the top entry of `CHANGELOG.md` — it opens with a list of claims in the
   entry below it that are now false, including two the previous session
   measured and got wrong.
3. Read `CLAUDE.md` — **The one thing to get right** and **Design invariants**.
4. `scripts/transcription_ii.py` only if you are working on Table 2 itself. Its
   `STATE` block is accurate and its per-record notes carry the pixel
   coordinates every reading was verified at.
5. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.
   **Don't call `preview_stop` when you finish** — the user may still be
   looking at it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-30**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing.

**Habits this project keeps re-learning:**

- **Measure, don't look.** Drift, contrast, row heights, bracket alignment.
- **Measure the right element.** See the open thread — a bracket check that
  compared `.node` tops read 0px on a bracket that is a full row out.
- **Grep the built file, not the rendered DOM.**
- **Read the staged diff before committing.**
- **Ask what *clears* a state, not only what sets it.**
- **Judge structure at native resolution.** A downscale loses exactly the thin
  rules that carry the genealogy.
- **A column tile reads a NAME and never its final mark.** Re-crop at 6–25×
  before calling a reading done.

And the one this session added:

- **"Wrong parents" and "wrong place on the page" are different findings.** The
  data can be right and the drawing wrong, and no structural check can tell you
  so. 31 was correctly read as having no leader stub *and* drawn four columns
  from where the plate sets him, for a whole session, because the only
  mechanism for drawing an unreachable person was to make him a root.

## State

Working tree clean. `main` untouched. `--public` exits 0, builds **5 pages**,
reports 104 / 275 / 73 persons, and `docs/` is byte-identical to what is
committed. All three transcription modules pass `self_check()`.

**Nothing is half-finished in code.** One defect is known, diagnosed and
deliberately not fixed — person 169's bracket, below.

**The build is sound; the READING is still not settled.** The user has more
placement errors to report and asked to be questioned about them. Everything
measured below describes a plate that builds and measures correctly, which is
a weaker claim than "is correct".

**Genealogy II is unpublished.** Branch `table-ii-transcription`, draft PR #14.
275 records for the plate's 274 numbers, 61 marriages, 214 parent–child links,
six generations, **three** descent blocks (not four — 31+32 was recounted this
session), 275 of 275 drawn. Measured at 1280×900: 0px column drift at all six
generations, step 425.59px, 0 rows off the `--lh` grid, 0px body sideways
scroll. Tables 1 and 4 re-measured as controls and unchanged at 0px.

**The live site does not have any of this.** It still serves two tables.

### Files this session changed

| File | What changed in it |
|---|---|
| `scripts/transcription_ii.py` | `UNATTACHED_BLOCKS` and its `self_check()` clause; `STATE` and the bracket-reading note corrected |
| `scripts/make_chart.py` | The splice in `Chart.render`; `.node.unattached` CSS; `roots` lost 31; undrawn persons now abort `--public`; `#note-unattached` |
| `CLAUDE.md` | Four claims corrected, two invariants added |
| `CHANGELOG.md` | The entry for this session |

Nothing under `data/`, no `.xlsx`, nothing under `build/`.

## The open thread

**ASK THE USER FOR THE REST OF THE PLACEMENT ERRORS. Do not merge PR #14 or run
`/publish` before that conversation.** They named 31, 32 and 97 as *examples*
and said the rest is "for later". That list is still outstanding.

Resolved this session, so don't re-open:

- **31, 32, 97** — the data was right, the drawing was wrong. Fixed via
  `UNATTACHED_BLOCKS`; 31 now sits at generation 4 between 29+30 and 33+34, at
  1336.98px, identical to 29 and 33, with no leader stub and the vertical
  passing his row as on the plate. The user confirmed 98–99 stay as children of
  33+34.
- **49 under 47** — confirmed correct by the user. No change.

**Then the two pieces of work that are already specified:**

1. **116–118's father is 49**, on the authority of Parsons's prose text — the
   user said so and it is not on the plate. This is METHOD.md's **second
   editorial attribution** and must meet all four of its rules: the chart never
   carries it, it is declared in `make_chart.py`'s `TABLES` entry and not in the
   transcription module, every row it produces is daggered to a footnote, and
   the evidence is not reproduced. Rule 4 differs here in one way worth getting
   right: Table 1's attribution rests on census research and its footnote had to
   stay vague, but **this one rests on a published 1923 sentence and can cite
   it**. *Blocked on the user for the page or the sentence* — ask for it.
2. **Person 169's leader rule and bracket stub point one row above her line.**
   Pre-existing, present identically in the committed build, 24.8px = exactly
   one `--lh`. 169 has two husbands, 168 and 183, and each marriage gets its own
   bracket, so both groups get `mother_row = 0` (`Chart.render` sets that
   whenever `u["wife"] == pid`). Two brackets cannot both start on one line, so
   the push logic adds `line_pad[0]` and moves 169's own line down to meet the
   **second** group — stranding the first. The Table 4 case the push logic was
   written for (11 and 12 under 10) has two *different* mothers, which is why it
   works there. Fixing it needs a plate reading first: how does Parsons actually
   set 169's two brackets? Also seen in the same pass: 158's group to 126 is
   0.023px off, probably the same cause and visually nothing.

**How this was found, because it is the method and not the incident:** measure a
bracket against the first **`.line`** in the group, never the first `.node`. The
`line_pad` displacement is a margin *inside* the block, so the node top reads
correct while the name sits a row lower. The previous session's "all 55 brackets
on their mother's line, max 0.016px" was measuring node tops.

Placements still flagged by the user for later, all deferred by them explicitly:
**232+233** (third block, printed at a child's indent — the same shape as 31 was,
so `UNATTACHED_BLOCKS` may apply), **U52 (234+54)**, **U60 (254+255)**.

**Only then** the release path: mark PR #14 ready, merge, run `/publish`, and
consider a release. Cutting one mints a new Zenodo version doi from
`.zenodo.json` on the tagged commit, and `.zenodo.json` and `CITATION.cff` both
still describe a **two-table** edition, so update them before tagging or the
deposit's metadata will describe the wrong thing.

Constraints that will surface late if you don't know them:

- **Merging changes both published pages, and one change is visible.** The
  `.xref` fix makes every cross-reference row 3.7px taller, Table 1's
  `#note-misprint` gained a paragraph, and every page now carries the
  `.node.unattached` CSS rule. Table 1 is cited. Re-verify it after building.
- **An undrawn person now aborts `--public`.** New this session. A half-read
  plate will therefore not build in public mode — that is deliberate, and the
  private build still only warns.
- **Run `subset_font.py` BEFORE `make_chart.py`, or not at all.** It is not
  deterministic and the woff2 is base64-inlined into every page. Don't re-run it
  to see whether anything changed — read its coverage report. To check coverage
  *without* dirtying anything, read the two `.woff2` cmaps with fontTools and
  diff against the text of `docs/` — that was done this session and found
  nothing missing.
- **The landing page's `PENDING` list holds only Table 3.**
- **Nothing may link to Genealogy III.** `linkify_xref` leaves any `Gen.`
  reference unlinked, which is what keeps that promise. It also leaves
  *Genealogy I* references unlinked — correct here, because Table 2's numbers
  into Genealogy I are displaced and a link would resolve to the wrong person.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Table 3** | Large, and harder than Table 2 | Scan is in `sources/` at 3770 × 5503 — **a ninth of Table 1's pixel count**. Do not start it in the same session as anything else |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable now, so this is the open item with a correctness edge |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| Wikidata item | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. Would need updating for three tables |
| AMNH Digital Library | Slow, **needs the user** | Still a strong inbound link, and the handle `.zenodo.json` omits |

## Decisions already made — don't re-litigate

**From this session:**

- **`UNATTACHED_BLOCKS` is the mechanism for "printed here, descent not
  drawn"** — not `roots`, and not a leader stub. `roots` is for a genuinely
  separate block at the left margin; a stub would assert a descent the plate
  withholds. It withholds `::before` only, so the vertical still passes the row.
  Considered and rejected: leaving 31 a root (draws him at generation 1, which
  is the bug); giving him a stub (asserts he is 9+10's son, which the plate
  does not).
- **31 is still the primary of his block, and he is a man.** The plate sets his
  line above and `+ 32` below; everywhere else on this plate the woman's line is
  the primary. Rooting at 32 would invert the two lines. `UNATTACHED_BLOCKS`
  therefore names the primary explicitly — it cannot be derived.
- **An undrawn person is fatal on `--public`, a warning on the private build.**
  A half-read plate legitimately has people no bracket reaches yet.
- **98 and 99 stay children of 33+34**, confirmed by the user against the
  plate's own rules: the rule from 33's line runs to their bracket, and both are
  Water as she is. 97 is Sun and hangs off 32's line, which is what makes 32 —
  not 33 — necessarily his mother.
- **9+10's vertical and 11+12's are two different rules.** The former takes 26,
  29, 33 and ends at 33; the latter begins at 35. The previous session's note
  read them as one.

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
`CLAUDE.md` owns all of them: the reverted per-clan palette and sex colouring,
the absent chart key, the class-driven row highlight, the plate bar's missing
max-width, the ruler's load-bearing height, the reproduced misprint, the 83–85
attribution, the illegible-passage rule, the deferred custom domain, the repeat
people carrying both settings, `alt_name`'s three meanings, the plate's numbers
vs ids, and `/publish`.

Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **A half-read plate is never registered in `TABLES`.** The renderer builds
  every registered table, so registering early is how a partial genealogy
  reaches `docs/`.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only.

## Closed — do not re-raise

- **Genealogy II's glyph readings.** All verified at 6–25× on 2026-07-29, each
  with coordinates in its record. `ˑ` U+02D1 is **not used on this plate**;
  `˘` U+02D8 is, at 170 only. Font coverage re-checked against the built pages
  on 2026-07-30 from the cmaps: nothing missing.
- **31 is not 9+10's son, and 33 is.** Verified three times now, most recently
  on the bracket-column strip x 3320, y 500, 480 × 1100.
- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file.
- **Tables 2 and 3 are not blocked on scans.** Both are in `sources/`.
