# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-31**, after the session that **finished Genealogy III's
orthography pass and its cross-reference audit**. Both of the previous
session's open threads are now closed.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md`.
3. **Read `scripts/transcription_iii.py`'s docstring.** It is the primary
   document for the open thread and holds everything the plate taught us — the
   tile grid, the paternity convention, the misprints, the two bracket calls,
   the completed cross-reference audit, and what the trial registration proved.
4. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**.
5. Preview: `preview_start`, config name `site`, on `http://localhost:4173`.
   **Don't call `preview_stop` when you finish** — the user may still be
   looking at it. If the port is held by another chat's server, navigate to it
   rather than trying to stop it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built and committed
on **2026-07-30**; on any later date the first rebuild shows a date-only diff.
If that is all it is, `git checkout -- docs/` rather than committing. Confirmed
again on 2026-07-31 — the diff was five files, dates only.

## State

`main` current and pushed, clean tree, no open PRs. **The live site is
untouched by this session.** `--public` exits 0, builds **5 pages**, reports
104 / 275 / 73 persons, and `docs/` is byte-identical to what is committed. All
four transcription modules pass `self_check()`.

**Genealogy III is now READ IN FULL and still deliberately unpublished.**
`scripts/transcription_iii.py` holds 261 persons, 72 unions, 192 parent–child
links; `self_check()` passes; `ORTHOGRAPHY_VERIFIED` is now **`True`**; the
cross-reference audit is **done**. It is **not registered in `TABLES`**, so
nothing it contains can reach `docs/`.

What is unfinished is **not the reading** — it is **six plate readings that
have had only one pair of eyes**, plus three decisions that are the user's to
make. Those are the open thread. A cold start should not read "the plate is
done" as "the plate is ready".

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

**Get Genealogy III's six one-eye readings checked, settle three decisions,
then register it.** The reading work is finished; what remains is confirmation
and design.

### 1 — Six readings that want the user's eye

None of these can be caught by `self_check()`, by clan descent, or by any build
gate. They are assertions about **where the plate prints things**.

**Two bracket calls** (from 2026-07-30, unchanged). Both are one unbroken,
unoffset vertical with **two** leaders entering it:

- **43's two husbands** — vertical at native x 2267, y 2157–2222, stubs to 124
  and 126, leaders at 43's row and 45's row. Encoded 43+44 → 124, 43+45 → 126.
- **22 and 25** — vertical at native x 1749, y 4339–4425, stubs to 80, 82, 83,
  leaders at 22's row and 25's row. Encoded 22 → 80, 82 and 25 → 83. All three
  children are Corn, so clan descent cannot separate them.

For contrast, 86's and 89's brackets at native x 2853 *are* visibly offset
where they meet — this plate distinguishes adjacent brackets when it means to.

**Four `drawn_under` values** (new, 2026-07-31). Each is a second spouse whose
partner is not a block primary anywhere; without them, fifteen people are never
drawn at all. Read off the scan at the generation-4 and generation-5 columns:

| union | what the plate prints | `drawn_under` |
|---|---|---|
| `W23` 40+39 | `+ 40.` inside 38's block, below 38's own bracket | 38 |
| `W34` 64+63 | 62, `+ 63.`, `+ 64.` — three consecutive lines | 62 |
| `W36` 66+67 | 65, `+ 66.`, `+ 67.` — three consecutive lines | 65 |
| `W45` 86+87 | 85, `+ 86.`, `+ 87.` — three consecutive lines | 85 |

### 2 — Three decisions, all the user's

The footnote for the cross-reference exceptions, how the non-numeric misprints
are shown, and the turned-comma mark. All three are in the table below.

### 3 — Then, and only then, register it

Add `"iii"` to `TABLES` with `roots [1, 230]` and `root_columns {230: 2}`, drop
the matching `PENDING` entry, run `subset_font.py` **before** the build, then
`--public`.

**A trial registration on 2026-07-31 proved this works, and was reverted.**
With the four `drawn_under` values the plate draws **all 261 people**, column
drift is 0 px within each block at a 425.59 px step, and the leak gate passes.
The 425.59 px offset *between* blocks is `root_columns` indenting block 2, not
drift. `subset_font.py` reports the plate needs exactly **two** new characters,
**`ó` and `ô`** — no need to re-derive that list.

**When reverting a trial registration, revert `docs/` and the font together.**
Reverting one alone leaves the pages carrying the base64 of a font no longer on
disk. Nothing fails; the two simply disagree.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy III's six one-eye readings** | ~30 min, **needs the user** | The open thread above — two bracket calls and four `drawn_under` values. Their reading wins |
| **Footnote for III's cross-reference exceptions** | Needs a design call | Four exceptions, no two alike: 170–174's Gen. II refs are **ten low**; 218's `Gen. I, 101` is **one low**; 173's `Gen. I, 149` cannot resolve; 155's prose note `Gen. I, 8, 90` is **one high** and is the only place III shows Genealogy II's displacement. Genealogy II got a footnote for its displacement — does III? All four are in the module docstring |
| **How III's non-numeric misprints are shown** | Needs a design call | 37's sex letter `M.`, 50's clan `Chapparral Cock`, 255's clan `Bager`. `PLATE_NUMBER_MISPRINTS` covers numbers only; these sit in `PLATE_MISPRINTS` and `make_chart.py` does not read it. Do they get the `--sic` ring and annotation row, or something quieter? |
| **The turned-comma mark** | ~15 min | **Five instances now: 154, 156, 157, 228, 242** — was one. Reads as a turned comma (opening quote), not the U+02BC used everywhere else. All five left as U+02BC. Settling it needs 20× on the five against a known U+02BC on the same line of type. **Don't mint a codepoint on less** |
| **Wikidata item** | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. **Needs updating for three tables** |
| **AMNH Digital Library** | Slow, **needs the user** | Strong inbound link. Handle `2246/158` — `https://digitallibrary.amnh.org/handle/2246/158`. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do. **III's person 155 has a four-line cross-reference already split this way** |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| **Link Table 2's 160 and 163 into III** | ~10 min, blocked | They carry cross-references into Genealogy III, printed unlinked because a link must not promise a page that does not exist. **Do this when III is published, not before** |
| **Custom domain** | **Deferred, not closed** | Decided against for now. Decide before seeding inbound links. See `CLAUDE.md` |

## Decisions already made — don't re-litigate

**From this session:**

- **Genealogy III does NOT share Genealogy II's +1 displacement into Genealogy
  I.** Its references across the displaced range — 78, 79, 97, 98, 99, 100,
  101, 103, 104 — all name the person Genealogy I finally printed under that
  number. III was numbered against the **final** Genealogy I; II was not.
  **Do not carry `CROSS_REF_OFFSET` over to this plate.** The one place the
  displacement does appear is 155's prose note, `see Gen. I, 8, 90`, where the
  descendant is Genealogy I's 89.
- **Nothing in the audit is corrected in the data.** `cross_ref` carries what
  the plate prints; every finding sits in the `plate_note` beside it. That is
  the treatment Genealogy II gave its own displacement.
- **192 is `Kiwaʼdyuwi`, with no raised dot, and the plates disagree.**
  Genealogy II's 188 — the same person — has one. Verified at 25×. The
  2026-07-30 changelog entry claims the two match; it is wrong, and the
  2026-07-31 entry says so. **Don't "fix" 192 to agree with Genealogy II.**
- **191 `Ramona` vs Genealogy II's `Ramona of Sant Ana` is not a divergence.**
  Both plates print the same thing; this file stores "of Sant Ana" in `origin`,
  `transcription_ii.py` stores it in the name. **Do not reconcile them by
  editing either name.**
- **152 and 153 are spelled differently at their two occurrences on the plate.**
  A finding about the plate, not an unresolved reading. The first occurrence is
  what the file carries; both spellings are in their `plate_note`.
- **`ORTHOGRAPHY_VERIFIED` is `True` and the pass is not to be redone.** All 261
  names read at 5×, thirteen corrections. Generations 6–7 yielded exactly one
  (192) — the deeper generations are short names with few diacritics, so a
  fresh pass there would cost a session and find nothing.

**From the previous session, still standing:**

- **Genealogy III needs no editorial attribution, anywhere.** The plate marks
  paternity itself: the leader rule sits on the line of the parent whose
  marriage the group belongs to, so a spouse with no leader had no recorded
  issue. 85/86/87 is Table 1's 83–85 *shape* and still needs nothing, because
  86's leader is on her own line and 87 has none. **Don't reach for METHOD.md's
  attribution machinery on this plate.**
- **258 and 259 are each printed on two different people, and 256 and 257
  appear nowhere.** Both pairs re-zoomed at 20× to rule out a misreading.
  Encoded as `DUPLICATE_PLATE_NUMBERS` with synthetic ids 256/257. **The
  edition states the fact and does not guess at the cause.**
- **37 is female though the plate prints `M.`** Her children's clan is her own,
  not her husband's. Reproduced as printed; the correction lives in
  `PLATE_MISPRINTS`, not in the data.

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
`CLAUDE.md` owns all of them: the reverted per-clan palette and sex colouring,
the absent chart key, the class-driven row highlight, the plate bar's missing
max-width, the ruler's load-bearing height, the reproduced misprint, the
illegible-passage rule, the deferred custom domain, the repeat people carrying
both settings, the plate's numbers vs ids, `UNATTACHED_BLOCKS`, `root_columns`,
`SECOND_VISIT_OMITTED` vs `SECOND_VISIT_NOTE`, the release policy, and
Genealogy II's 116–118 attribution.

Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **A half-read plate is never registered in `TABLES`.** Genealogy III is now
  fully read, so this no longer *blocks* registration — but the six one-eye
  readings and the three decisions above do. A trial registration to look at
  the page is fine; leaving it in the tree is not.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only. A
  **published** source is quoted and cited; an **unpublished** one is gestured
  at and never named. See METHOD.md rule 4.

## Closed — do not re-raise

- **Genealogy III's orthography.** All 261 names verified at 5×; thirteen
  corrections. Only the turned-comma mark is open, and it is in the table above.
- **Genealogy III's cross-references.** All 51 person-level references plus the
  two prose references under 155, audited by name, sex and clan. The four
  exceptions are recorded; only the *footnote* decision is open.
- **Genealogy III's structure.** 261 persons, 72 unions, 192 links, seven
  generations, two blocks, `self_check()` green with **all 192 links
  matrilineally consistent on the first run**.
- **Whether the plate can be drawn at all.** It can — proved 2026-07-31 and
  reverted. All 261 drawn, 0 px drift within each block, leak gate clean.
- **173's `See Gen. I, 149`.** Re-read at 5× twice. It is what the plate prints
  and it does not resolve. The person is Genealogy I's 49.
- **Genealogy II's placement and glyph readings.** The user reported no
  remaining errors on 2026-07-30.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file; `/publish` Gate 6 does this.
- **A privacy sweep must assert the content is present.** Use `curl -sL` *and*
  assert something like `id="p116"` exists. A check that passes because it
  examined nothing is the most dangerous result it can produce.
- **`sips --cropOffset 0 0` centre-crops.** Cost a mis-read tile before it was
  spotted. Now in `CLAUDE.md`'s Environment section.
