# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-30**, after the session that **published Genealogy II**.
The site now serves three plates.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.** There is no work in flight and no open PR;
   `main` is current and deployed.
2. Read the top entry of `CHANGELOG.md`. It opens with the claims in the entry
   below it that are now false, including a sentence that has now been found and
   corrected in three separate files.
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
- **Measure the right element.** A bracket check that compares `.node` tops
  reads 0px on a bracket that is a full row out. Compare the first `.line`.
- **Grep the built file, not the rendered DOM.**
- **Judge structure at native resolution.** A downscale loses exactly the thin
  rules that carry the genealogy.
- **A column tile reads a NAME and never its final mark.** Re-crop at 6–25×.
- **"Wrong parents" and "wrong place on the page" are different findings.**

And the one this session added, which paid off immediately:

- **Fetch the live URL; don't trust the build output.** The privacy gate
  inspects `docs/`, and `--public` exited 0 on a landing page whose FAQ told
  readers Genealogy II was *not yet transcribed* — on the very release that
  published it. Grep the built file for markup, fetch the live page for truth.
  Verify deploys by **SHA-256 against the committed file**; the Pages build API
  misreports the deployed commit.

## State

Working tree clean, `main` current and deployed. `--public` exits 0, builds
**5 pages**, reports 104 / 275 / 73 persons, and `docs/` is byte-identical to
what is committed. All three transcription modules pass `self_check()`.

**Genealogy II is PUBLISHED and the site is correct.** PR #14 merged as
`04ded51`, PR #15 (the FAQ correction) as `f9e50c2`. After each merge all four
live pages were verified byte-identical to `main` by SHA-256, HTTP 200, sitemap
carrying four URLs, and a privacy sweep of the **live** pages came back clean —
no `class="eng"` or `class="census"`, no research vocabulary, and the only
`census` occurrences are the three allowlisted FAQ sentences that state the
boundary itself.

**Nothing is half-finished, and nothing is unmerged.** One defect is known,
diagnosed and left alone — the 0.023px sub-pixel offset on 158's group to 126,
which is invisible and not worth touching shared bracket code to chase.

Measured at 1280×900: column drift spread ≤ 0.008px at all six generations, step
425.59px; 57 bracket groups, worst 0.023px; 0 rows off the `--lh` grid; 0px body
sideways scroll at desktop and mobile.

### Files this session changed

| File | What changed in it |
|---|---|
| `scripts/make_chart.py` | `SECOND_VISIT_OMITTED`; `root_columns` + the `.tree` indent; two FAQ answers |
| `scripts/transcription_ii.py` | 169's, 254's and 255's plate notes; the generation-derivation note |
| `.zenodo.json`, `CITATION.cff` | Three tables; `v1.1.0`; the clan-check overstatement removed |
| `README.md` | Table 2 row; "when Table 3 is added" |
| `CLAUDE.md` | Outstanding rewritten; three invariants added |
| `CHANGELOG.md` | The entry for this session |

Nothing under `data/`, no `.xlsx`, nothing under `build/`.

## The open thread

**Genealogy III — the last plate.** It is now the only thing between here and
the next release.

**Cutting v1.1.0 is NO LONGER the open thread; it was cancelled.** The user set
a release policy on 2026-07-30: during active development, commit to `main` and
cut **no GitHub Releases and no Zenodo deposits**. One release only, once all
four tables, the design, the transcriptions, the text and the citations are
final. **The policy is in `CLAUDE.md` — read it there, not here.**

Two consequences that look like bugs and are not:

- `CITATION.cff` says `v1.0.0` / `2026-07-28`, the newest release that actually
  exists, while its abstract describes three plates. That is correct: the
  abstract describes the *work*, the version fields the *release*.
- The concept doi in every page footer resolves to v1.0.0, which holds
  Genealogies I and IV only. **The archive lags the site on purpose.** Do not
  tag to close the gap.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Cut the v1.1.0 release** | ~15 min, **needs the user** | Metadata is ready; read the date warning above |
| **Wikidata item** | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. **Needs updating for three tables** |
| **Table 3** | Large, and harder than Table 2 | Scan is in `sources/` at 3770 × 5503 — **a ninth of Table 1's pixel count**. Do not start it in the same session as anything else |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **Custom domain** | Decided against, not closed | Decide before seeding inbound links. See `CLAUDE.md` |
| **AMNH Digital Library** | Slow, **needs the user** | Still a strong inbound link, and the handle `.zenodo.json` omits |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |

## Decisions already made — don't re-litigate

**From this session:**

- **`SECOND_VISIT_OMITTED` is not `SECOND_VISIT_NOTE`.** Use the first when the
  plate prints no second occurrence of a marriage at all — no `+` line, no
  bracket, only a prose cross-reference. Use the second when the plate *does*
  print the `+` line and replaces only the sibling bracket. Table 1's person 8
  is the second kind (two *different* wives, two `mother_row`s, no collision);
  169 is the first (two husbands, she is the mother of both groups).
- **`root_columns` is an indent, not a splice.** 154+155 and 232+233 sit at
  generations 2 and 3 because that is where the plate prints them. Considered
  and rejected: `UNATTACHED_BLOCKS`, which would assert the lower block is
  descended from the upper one and would hit the last-child rule besides.
- **116–118's paternity is not encoded, and that is final.** No source in
  Parsons's text, and the user asked for no footnote or editorial note. **An
  attribution that cannot be footnoted is not made.** Not an oversight.
- **The clan check does not independently verify every bracket reading.** It
  discriminates only where the candidate mothers differ in clan. Corrected in
  `.zenodo.json`, `CITATION.cff` and the FAQ this session; `CLAUDE.md` already
  had it right.
- **v1.1.0's version doi is absent on purpose** until Zenodo mints it.
- **254 is a child of 235+236**, verified on the strip. **255's stub is not
  descent** — he is Eagle, every child on that bracket is Water.

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
`CLAUDE.md` owns all of them: the reverted per-clan palette and sex colouring,
the absent chart key, the class-driven row highlight, the plate bar's missing
max-width, the ruler's load-bearing height, the reproduced misprint, the 83–85
attribution, the illegible-passage rule, the deferred custom domain, the repeat
people carrying both settings, `alt_name`'s three meanings, the plate's numbers
vs ids, `UNATTACHED_BLOCKS`, and `/publish`.

Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **A half-read plate is never registered in `TABLES`.** The renderer builds
  every registered table, so registering early is how a partial genealogy
  reaches `docs/`.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only.

## Closed — do not re-raise

- **Genealogy II's placement.** The user re-checked their full list on
  2026-07-30 and reported **no remaining errors**. 31/32/97, 49 under 47,
  154+155, 232+233, 169, U52 and U60 are all settled and measured.
- **Genealogy II's glyph readings.** All verified at 6–25× on 2026-07-29, each
  with coordinates in its record. `ˑ` U+02D1 is **not used on this plate**;
  `˘` U+02D8 is, at 170 only. Font coverage re-checked against the built pages
  from the cmaps: nothing missing.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **`prettyph3nom/laguna-genealogy` is deleted.** Verified three ways.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file.
- **Tables 2 and 3 were never blocked on scans.** Both are in `sources/`.
