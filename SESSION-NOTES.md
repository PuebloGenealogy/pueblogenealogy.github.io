# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-29**, after a session that finished **Genealogy II** —
read, encoded, rendered and measured. It is on a branch, not published.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch table-ii-transcription`.** The work is on a branch, and there
   is an open **draft PR #14**.
2. Read the top section of `CHANGELOG.md` — one entry covers this whole
   session, and it opens with a list of claims in the entry *below* it that are
   now false. Read that list; the older entry is not safe on its own.
3. Read `CLAUDE.md` — **The one thing to get right** and **Design invariants**.
4. `scripts/transcription_ii.py` only if you are working on Table 2 itself. Its
   `STATE` block is accurate, and its per-record notes carry the pixel
   coordinates every reading was verified at.
5. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.
   **Don't call `preview_stop` when you finish** — the user may still be
   looking at it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-29**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing.

**Habits this project keeps re-learning:**

- **Measure, don't look.** Drift, contrast, row heights, bracket alignment.
- **Grep the built file, not the rendered DOM.**
- **Read the staged diff before committing.**
- **Ask what *clears* a state, not only what sets it.**
- **Judge structure at native resolution.** A downscale loses exactly the thin
  rules that carry the genealogy.

And the one this session added, at the cost of eleven wrong readings:

- **A column tile reads a NAME and never its final mark.** At 1450px a trailing
  diacritic is 4–6px wide with the sentence period beside it. Nine of eleven
  corrections were a *dropped* mark, almost all at the end of a name. Re-crop at
  6–25× before calling a reading done, and compare two marks at the **same**
  magnification rather than judging one alone.

## State

**Nothing is half-finished, and this is worth trusting.** Working tree clean.
`main` untouched. `--public` exits 0, builds **5 pages**, reports 104 / 275 / 73
persons, and `docs/` is byte-identical to what is committed. All three
transcription modules pass `self_check()`.

**Genealogy II is done and unpublished.** Branch `table-ii-transcription`,
commits `04d2deb`, `e7b2bdd`, `d8f9525`, `d657094` on top of the earlier
sessions' work. 275 records for the plate's 274 numbers, 61 marriages, 214
parent–child links, six generations, four descent blocks, **275 of 275 drawn**.
Measured at 1280×900: 0px column drift at every generation, 55 brackets on their
mother's line (≤0.016px), 0 rows off the `--lh` grid, 0px body sideways scroll.
Tables 1 and 4 re-measured as controls and unchanged at 0px.

**The live site does not yet have any of this.** It still serves two tables.

## The open thread

**Merge PR #14 and publish.** Everything upstream is finished; what remains is
the release decision, and it is not purely mechanical.

1. **The PR title and body are stale** — it says "upper block transcribed (plate
   numbers 1-153)" and is still a draft. Rewrite both before merging.
2. **Run `/publish`.** It gates the build, checks privacy, pushes, verifies live.
3. **Then decide about a release.** Cutting a GitHub release mints a new Zenodo
   version doi from `.zenodo.json` on the tagged commit. A whole new plate is
   worth one — but `.zenodo.json` and `CITATION.cff` describe a **two-table**
   edition, so read them before tagging or the deposit's metadata will describe
   the wrong thing.

Constraints that will surface late if you don't know them:

- **This session changed both published pages, and one change is visible.** The
  `.xref` fix makes every cross-reference row 3.7px taller, and Table 1's
  `#note-misprint` gained a paragraph. Table 1 is cited. Re-verify it after
  building — 0px drift, 24 brackets at 0px, misprint marker still pointing at
  its note.
- **Run `subset_font.py` BEFORE `make_chart.py`, or not at all.** It is not
  deterministic (fontTools rewrites `head.modified`) and the woff2 is
  base64-inlined into every page, so the wrong order leaves the pages carrying a
  font that is no longer on disk. Nothing fails. Don't re-run it just to see
  whether anything changed — read its coverage report.
- **The landing page's `PENDING` list now holds only Table 3.** Genealogy II
  moved out of it into `TABLES`.
- **Nothing may link to Genealogy III.** Persons 160 and 163 point into it;
  `linkify_xref` leaves any `Gen.` reference unlinked, which is what keeps that
  promise. Note it also leaves *Genealogy I* references unlinked — over-
  conservative on its face, but correct here for a second reason: Table 2's
  numbers into Genealogy I are displaced, so a link would resolve to the wrong
  person.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Table 3** | Large, and harder than Table 2 | Scan is in `sources/` at 3770 × 5503 — **a ninth of Table 1's pixel count**. Do not start it in the same session as anything else |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today, so all 93 brackets align, but a longer reference would sit two rows in a one-row budget. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable now, so this is the open item with a correctness edge |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| Wikidata item | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. Would need updating for three tables |
| AMNH Digital Library | Slow, **needs the user** | Still a strong inbound link, and the handle `.zenodo.json` omits |

## Decisions already made — don't re-litigate

**From this session:**

- **The three repeat people carry BOTH of the plate's settings** — 13, 54, 125.
  First occurrence in `name_as_printed`, second in `alt_name`, printed as
  `A (B)`. All six settings are unambiguous at magnification, so this is not a
  reading problem: the plate prints one name two ways, and suppressing either
  would hide what it says. Considered and rejected: print one and footnote the
  other; keep the variant only in `plate_note`.
- **`alt_name` now carries three meanings, knowingly.** English names the plate
  parenthesises (27, 42, 43, 140), the second half of a braced pair (14), and
  repeat-person settings. Only the first is parenthetical on the page.
  `#note-repeat-names` exists so a reader is told which is which. Don't "fix"
  this with a fourth field without reading that note first.
- **`31` is a root, and it is a man** — the other three roots are the mothers,
  because the plate makes the woman's line the primary. At 31+32 it does the
  opposite, so rooting at 32 would invert the two lines and show the reader
  something the plate does not.
- **The plate's numbers are shown; ids are plumbing.** `p["plate_number"]`
  prints, `p["id"]` addresses. They differ only at the duplicate 101. Distinct
  from the misprint path, which additionally rings the number in `--sic`.
- **Cross-plate person references are never `_p()`.** `_p(60)` on Table 1 links
  Table 1's person 60. Only explicit relative hrefs cross pages.

**Standing, from earlier sessions:**

- **Genealogy II's upper-block left column has ONE founding couple**, 1+2. The
  plate as a whole has four blocks. If a reading suggests three in that column,
  it is reading the overview.
- **Duplicate 101 prints 101 on both rows.** `101a`/`101b` was rejected.
- **Illegible passages: the user supplies the reading, used as given** — no
  footer note, no chart marker. The reason goes in `plate_note`. **If a reading
  comes from the census research, its source must not be named anywhere in the
  repo.**
- **A half-read plate is not registered.** `TABLES` stays untouched until
  `self_check()` passes.
- **A chart row's highlight is class-driven wherever the card script runs.**
  Re-enabling `:target` alongside `.is-selected` re-opens the bug it fixed.
- **The plate bar has no max-width, on purpose** — it aligns to the plate.
- **The ruler's height is load-bearing.** It holds the identity chip off the
  generation labels.
- **The person card carries the number, never the annotation.**
- **No per-clan colours, and no colour-coding of sex.** Both built and reverted.
  Three colours on a table page are not `--ink`: `--sic`, `--muted-fixed`,
  `--clan`. A fourth needs the same evidence.
- **No on-page chart key.** Built twice, removed twice.
- **The plate's misprint is reproduced, not corrected.** Table 1 prints **68**,
  and Table 2 now corroborates that 68 is Parsons's own number.
- **The edition asserts one thing the plate does not** — the paternity of 83–85.
  Read `METHOD.md` → *Editorial attribution* before adding another.
- **Research evidence never enters the repo.** The gate protects `docs/` only,
  reads prose as well as markup, and fails closed.
- **No custom domain** for now — but **decide it before seeding inbound links**,
  because every citation placed from now on points at whatever host is chosen.
- **Publishing goes through `/publish`.**

## Closed — do not re-raise

- **Genealogy II's glyph readings.** All verified at 6–25× on 2026-07-29, each
  with coordinates in its record. `ˑ` U+02D1 is **not used on this plate**;
  `˘` U+02D8 is, at 170 only. Font coverage is checked against the cmap of both
  master faces and now also against the built pages, by `check_against_build()`.
- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file.
- **Tables 2 and 3 are not blocked on scans.** Both are in `sources/`.
