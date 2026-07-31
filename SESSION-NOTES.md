# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-31**, after the session that **published Genealogy III**.
The edition is now all four plates. The previous session's open thread is
closed.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md` — it is long this time, and it holds the
   two renderer changes and the wrong-link bug a future session would otherwise
   re-derive.
3. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**.
4. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.
   **Don't call `preview_stop` when you finish** — the user may still be
   looking at it. If the port is held by another chat's server, navigate to it
   rather than trying to stop it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-31**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing.

## State

`main` current and pushed at `b06eb10`, clean tree, no open PRs. **Genealogy III
is live.** `--public` exits 0, builds **6 pages**, reports 104 / 275 / 261 / 73
persons, and the deployed pages are byte-identical to `docs/` by SHA-256.
All four transcription modules pass `self_check()`. `PENDING` is empty.

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

**There isn't a big one.** The plates are done. What remains is a short list of
editorial and outreach items, none of them blocking each other. Most likely
first:

### 1 — A footnote for Genealogy III's cross-reference exceptions

Four exceptions, no two alike, all recorded in `transcription_iii.py`'s
docstring and **nothing said about them on the page**:

- **170–174**'s references into Genealogy II are **ten low**
- **218**'s `Gen. I, 101` is **one low**
- **173**'s `Gen. I, 149` **cannot resolve at all** (the person is Genealogy I's
  49; re-read twice at 5×, it is what the plate prints)
- **155**'s prose note `Gen. I, 8, 90` is **one high** — the only place III
  shows Genealogy II's +1 displacement

Genealogy II got `#note-crossref` for its own displacement, so the precedent
exists. **This is a design call, not a reading** — the readings are closed.

### 2 — The turned-comma mark

Five instances: **154, 156, 157, 228, 242**. Each reads as a turned comma
(opening quote) rather than the U+02BC used everywhere else on the plate. All
five are stored as U+02BC. Settling it needs 20× on the five against a known
U+02BC on the same line of type. **Don't mint a codepoint on less.**

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Footnote for III's cross-reference exceptions** | Needs a design call | Section 1 above. All four are in the module docstring |
| **The turned-comma mark** | ~15 min | Section 2 above |
| **Wikidata item** | ~10 min, **needs you** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. **Needs updating for all four tables** — it was written for three |
| **AMNH Digital Library** | Slow, **needs you** | Strong inbound link. Handle `2246/158` — `https://digitallibrary.amnh.org/handle/2246/158`. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do. **Note 155 is also why `linkify_xref` now takes a whole-reference verdict** — see the changelog |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate: another plate's numbering is not an anchor on this page. Genealogy II's note on 160 and 163 now says so. **Making them links would be a new feature across all four plates**, not a Table 2 edit — the old handoff item "link 160 and 163 into III" assumed otherwise and is retired |
| **Custom domain** | **Deferred, not closed** | Decided against for now. Decide before seeding inbound links. See `CLAUDE.md` |
| **Cut the release** | **Not yet — see the policy** | All four plates are published, which meets one of the policy's four clauses. The other three are not: two editorial items above, `.zenodo.json` still describes three plates, AMNH handle still absent from `related_identifiers`. **Publishing the site is not releasing it** |

## Decisions already made — don't re-litigate

**From this session:**

- **22's bracket runs 80, 82; 83 is 25's — and the plate's rule is over-drawn.**
  The user read it against the scan. The vertical is carried on past 82 to touch
  83, so the three appear to share one bracket. **The chart draws two**, which
  is the one place on this table where the drawn structure departs from the
  scan; footnoted at `#note-overdrawn`. Not a `PLATE_MISPRINTS` case — that
  table carries printed *text*, this is a rule.
- **43's bracket carries two leaders**, hers to 124 and 45's to 126. Settled by
  the user. Encoded `W25` 43+44 → 124, `W26` 43+45 → 126, and it is what
  `LEADER_ON_SPOUSE_ROW` exists for.
- **The four `drawn_under` values are confirmed against the scan** — W23 (40
  under 38), W34 (64 under 62), W36 (66 under 65), W45 (86 under 85). The two
  carrying children pass clan descent *discriminatingly*: W23's 116, 118 are
  Parrot (40's clan, not host 38's Sun); W34's 146–151 are Turkey (64's, not
  host 62's Badger). W36 and W45 have no issue at all.
- **III's three non-numeric misprints print as the plate sets them**, ringed in
  `--sic` with an annotation row, under `#note-misprint`. The user chose this
  over a quieter treatment. `PLATE_MISPRINTS` is now read by the renderer; it
  was declared and ignored before, which meant the build silently printed
  *corrected* readings.
- **`|` in a cross-reference is a typographic line break, never a change of
  subject.** Any judgement about a reference is made on the whole of it. This
  is why `linkify_xref` takes `cross_plate` from the caller now.
- **Genealogy III needs no editorial attribution, anywhere** — confirmed on the
  scan this session. 85/86/87 is Genealogy I's 83–85 *shape*, and 86's leader is
  on her own line while 87 has none. **Don't reach for METHOD.md's attribution
  machinery on this plate.**

**Still standing from earlier sessions:**

- **III does NOT share Genealogy II's +1 displacement into Genealogy I.** It was
  numbered against the final Genealogy I. Never carry `CROSS_REF_OFFSET` over.
- **Nothing in the cross-reference audit is corrected in the data.** `cross_ref`
  carries what the plate prints; every finding sits in the `plate_note` beside
  it.
- **192 is `Kiwaʼdyuwi`, with no raised dot, and the plates disagree** with
  Genealogy II's 188. Verified at 25×. Don't "fix" it.
- **191 `Ramona` vs Genealogy II's `Ramona of Sant Ana` is not a divergence** —
  this file stores "of Sant Ana" in `origin`.
- **152 and 153 are spelled differently at their two occurrences.** A finding
  about the plate; both spellings are in their `plate_note`.
- **`ORTHOGRAPHY_VERIFIED` is `True` and the pass is not to be redone.**
- **258 and 259 are each printed on two different people, and 256 and 257
  appear nowhere.** Encoded as `DUPLICATE_PLATE_NUMBERS` with synthetic ids.
  The edition states the fact and does not guess at the cause.
- **37 is female though the plate prints `M.`** Her children's clan is her own.

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **Publishing the site is not cutting a release.** Zenodo's webhook is on this
  repo; a GitHub release mints a permanent version doi that cannot be deleted.
  All four plates being live does not change the release policy.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only. A
  **published** source is quoted and cited; an **unpublished** one is gestured
  at and never named. See METHOD.md rule 4.

## Closed — do not re-raise

- **Genealogy III, entirely.** Read, drawn, audited, verified and **live**. Its
  orthography, cross-references, structure, six one-eye readings and three
  design decisions are all settled. Only the two editorial items above remain,
  and neither is a reading.
- **Whether the plate can be drawn.** It is: all 261 drawn, 0.000 px column
  drift at every generation in both blocks, every block row a whole `--lh`, no
  node's first line displaced from its top.
- **173's `See Gen. I, 149`.** It is what the plate prints and it does not
  resolve. The person is Genealogy I's 49.
- **Genealogy II's placement and glyph readings.** No remaining errors,
  2026-07-30.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file; `/publish` Gate 6 does this,
  and it passed on all six pages this session.
- **A privacy sweep must assert the content is present.** Use `curl -sL` *and*
  assert something like `id="p116"` exists. Done live this session: 261 chart
  anchors and 261 register entries on `/genealogy-iii/`, 0 research markers on
  all five pages.
- **`sips --cropOffset 0 0` centre-crops.** Use `1 1`. In `CLAUDE.md`.
