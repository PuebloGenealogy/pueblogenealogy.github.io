# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-30**, after the session that **attributed Genealogy II's
116–118 to person 49** and **set the release policy**.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.** Nothing is in flight and no PR is open.
2. Read the top entry of `CHANGELOG.md`.
3. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**.
4. `scripts/transcription_ii.py` only if you are working on Table 2 itself.
5. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.
   **Don't call `preview_stop` when you finish** — the user may still be
   looking at it. If the port is held by another chat's server, navigate to it
   rather than trying to stop it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-30**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing.

## State

Working tree clean, `main` current, **deployed and verified live**. `--public`
exits 0, builds **5 pages**, reports 104 / 275 / 73 persons, and `docs/` is
byte-identical to what is committed. All three transcription modules pass
`self_check()`.

**Nothing is half-finished and nothing is unmerged.** PR #17 (the attribution)
and PR #18 (the publish gates) both merged and deployed today, verified by
SHA-256 against the committed files. A live privacy sweep of all five pages came
back clean.

One defect is known, diagnosed and deliberately left alone: the **0.023px**
sub-pixel offset on 158's group to 126. Invisible, and not worth touching shared
bracket code to chase.

**Genealogy III is the only plate left**, and the only thing between here and
the next release.

## The open thread

**Genealogy III — the last plate.** Nothing else is outstanding on the edition.

Read `/transcribe-plate` before starting, and note these before the first tile:

- **The scan is `sources/parsons-1923-table-3.jpg`, 3770 × 5503** — about **a
  ninth of Table 1's pixel count**. That makes it *harder*, not easier: there is
  less resolution with which to resolve a diacritic or a leader stub. Expect
  readings that Tables 1 and 2 settled at 6–25× to be genuinely ambiguous here.
- **Do not start it in the same session as anything else.**
- **A half-read plate is never registered in `TABLES`** — the renderer builds
  every registered table on every `--public` run, so registering early is how a
  partial genealogy reaches `docs/`. Register at Gate 5, after `self_check()`
  passes. *(Deliberate duplicate of `CLAUDE.md`; acting on it wrongly publishes
  a partial plate.)*
- Persons **160** and **163** on Table 2 carry cross-references into Genealogy
  III. They are printed unlinked today because a link must not promise a page
  that does not exist. **Link them when III lands.**
- The publish gates now derive their lists, so **III needs no edit to
  `/publish`** — but `.zenodo.json` and `CITATION.cff` will need bringing to
  four tables as part of cutting the release.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy III** | Large | The open thread above |
| **Wikidata item** | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. **Needs updating for three tables** |
| **AMNH Digital Library** | Slow, **needs the user** | Strong inbound link. **The handle is `2246/158`** — `https://digitallibrary.amnh.org/handle/2246/158`, found this session. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| **Custom domain** | Decided against, not closed | Decide before seeding inbound links. See `CLAUDE.md` |

## Decisions already made — don't re-litigate

**From this session:**

- **116–118's father is 49, and it is now encoded.** It was declined earlier the
  same day *only* because no source had been found; the user supplied
  **Parsons p. 195**, where she records of "Gen. II, 47" that his sheep and
  fields passed to his widow for want of offspring. The rule that blocked it was
  **satisfied, not waived**: *an attribution that cannot be footnoted is not
  made.* Do not re-open it in either direction.
- **The dagger marks the pairing, not the mother**, and it sits on the row
  rather than on the father's chip — partly because the mother is the plate's
  own bracket, partly because the card's rows are anchors and an `<a>` dagger
  cannot nest inside the chip's `<a>`. **Don't "fix" it to a per-chip mark
  without solving the card**, or the card loses the dagger silently.
- **Quoting a printed source may trip the leak gate.** Parsons's word "widow"
  matches `RESEARCH_PROSE`. The exact phrase is allowlisted in
  `RESEARCH_PROSE_ALLOWED`. **Allowlist the phrase; never loosen the pattern** —
  verified still failing closed on `census`, `enumerator`, `widowed` and every
  other use.
- **No releases and no Zenodo deposits during active development.** One release
  once all four tables, the design, the transcriptions, the text and the
  citations are final. **v1.1.0 was cancelled, not deferred.** The archive
  lagging the site is the accepted cost — **do not tag to close it.** The policy
  is in `CLAUDE.md`.
- **`CITATION.cff` names the newest release that EXISTS**, `v1.0.0` /
  `2026-07-28` — never a planned one. Its abstract describing three plates while
  the version says v1.0.0 is correct: the abstract describes the *work*, the
  version fields the *release*.

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
`CLAUDE.md` owns all of them: the reverted per-clan palette and sex colouring,
the absent chart key, the class-driven row highlight, the plate bar's missing
max-width, the ruler's load-bearing height, the reproduced misprint, the
illegible-passage rule, the deferred custom domain, the repeat people carrying
both settings, the plate's numbers vs ids, `UNATTACHED_BLOCKS`, `root_columns`,
and `SECOND_VISIT_OMITTED` vs `SECOND_VISIT_NOTE`.

Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **A half-read plate is never registered in `TABLES`.**
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only. Note the
  nuance added this session: a **published** source is quoted and cited; an
  **unpublished** one is gestured at and never named. See METHOD.md rule 4.

## Closed — do not re-raise

- **Genealogy II's placement and glyph readings.** The user reported no
  remaining errors on 2026-07-30; every glyph verified at 6–25× with coordinates
  in its record.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file; `/publish` Gate 6 does this.
- **A privacy sweep must assert the content is present.** One passed CLEAN on
  all five pages this session while inspecting redirect stubs, because the pages
  were fetched **without trailing slashes**. Use `curl -sL` *and* assert
  something like `id="p116"` exists. A check that passes because it examined
  nothing is the most dangerous result it can produce.
- **Tables 2 and 3 were never blocked on scans.** Both are in `sources/`.
