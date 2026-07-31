# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-30**, after the session that **read and encoded
Genealogy III** and verified the first half of its orthography.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md`.
3. **Read `scripts/transcription_iii.py`'s docstring.** It is the primary
   document for the open thread and holds everything the plate taught us —
   the tile grid, the paternity convention, the misprints, the two bracket
   calls, and exactly which ids are orthographically verified.
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
If that is all it is, `git checkout -- docs/` rather than committing.

## State

`main` current, **the live site is untouched by this session**. `--public`
exits 0, builds **5 pages**, reports 104 / 275 / 73 persons, and `docs/` is
byte-identical to what is committed. All four transcription modules pass
`self_check()`.

**One thing IS half-finished, deliberately: Genealogy III's orthography.**
`scripts/transcription_iii.py` exists, holds **261 persons, 72 unions, 192
parent–child links**, and passes `self_check()` — but it is **not registered in
`TABLES`** and `ORTHOGRAPHY_VERIFIED` is `False`. Nothing it contains can reach
`docs/`. Do not register it to "see how it looks".

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

**Finish Genealogy III's orthography pass, then its cross-reference audit.**

### 1 — Names, ids 85–229 and 248–261

Ids **1–84 and 230–247 are done**. The rest are provisional and **wrong by
default**: the 1.5× structural pass could not separate `˙` U+02D9 from `ʼ`
U+02BC and defaulted to `ʼ`. Sixteen of the eighty-odd names already checked
needed correcting, so expect a similar rate in what remains.

The recipe that works, reusable as-is:

```bash
sips -c <h> <w> --cropOffset <top> <left> sources/parsons-1923-table-3.jpg --out t.jpg
```

then `sips -Z $((w * 5)) t.jpg` to get 5×.

- Keep **`h` ≤ `w`**, or `-Z` scales the height instead and you lose the 5×.
- `w` of 400–440 covers number + sex + name in one column.
- **Never use `--cropOffset 0 0`** — it centre-crops silently. Use `1 1`.
- Generation columns, native x of the number: g1 145, g2 755, g3 1293,
  g4 1833, g5 2377, g6 2920, g7 3467. Crop from ~40px left of the number.
- Rows are ~25 native px apart.

Generation 5 (ids 85–183, plus 248–257) is the bulk of what is left.

**Set `ORTHOGRAPHY_VERIFIED = True` only when the whole plate is done**, and
update the docstring's verified-range line as you go so a cold start can resume
mid-column.

### 2 — The cross-reference audit, which has not been started

`transcription_ii.py` records that Parsons's "See Gen. I, n" references run
**exact through Genealogy I's person 53 and one high from its person 66 onward**.
Genealogy III's references have **not** been checked against that finding at
all. One is already known not to resolve: **173 cites `See Gen. I, 149`, and
Genealogy I has 104 people.** Check the whole set by name, sex and clan against
`transcription.py` and `transcription_ii.py`, exactly as Table 2's block does.

### 3 — Then, and only then, Gate 4

Register `"iii"` in `TABLES`, drop the matching `PENDING` entry, run
`subset_font.py` **before** the build (it reports the plate's new characters —
`ô`, `ó`, `ŭ` and the superscripts are the candidates), then `--public`.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Genealogy III orthography + cross-refs** | Large | The open thread above |
| **Genealogy III's two bracket calls** | ~15 min, **needs the user** | Both are one unbroken vertical with **two** leaders entering. 43+44→124 / 43+45→126, and 22→80,82 / 25→83. Coordinates are in the module docstring. The user reads the plate against the render; their reading wins |
| **How III's non-numeric misprints are shown** | Needs a design call | 37's sex letter `M.`, 50's clan `Chapparral Cock`, 255's clan `Bager`. `PLATE_NUMBER_MISPRINTS` covers numbers only; these sit in `PLATE_MISPRINTS` and `make_chart.py` does not read it. Do they get the `--sic` ring and annotation row, or something quieter? |
| **242's final glyph** | ~5 min | Reads as a *turned* comma, not the U+02BC used everywhere else. Left as U+02BC. Don't add a codepoint on that evidence |
| **Wikidata item** | ~10 min, **needs the user** | Payload at `wikidata-quickstatements.txt`, 18 ids verified. **Needs updating for three tables** |
| **AMNH Digital Library** | Slow, **needs the user** | Strong inbound link. Handle `2246/158` — `https://digitallibrary.amnh.org/handle/2246/158`. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs the user + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is probably to split at the plate's own line break with `\|`, as 160 and 169 now do. **III's person 155 has a four-line cross-reference already split this way** |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| **Link Table 2's 160 and 163 into III** | ~10 min, blocked | They carry cross-references into Genealogy III, printed unlinked because a link must not promise a page that does not exist. **Do this when III is published, not before** |
| **Custom domain** | Decided against, not closed | Decide before seeding inbound links. See `CLAUDE.md` |

## Decisions already made — don't re-litigate

**From this session:**

- **Genealogy III needs no editorial attribution, anywhere.** The plate marks
  paternity itself: the leader rule sits on the line of the parent whose
  marriage the group belongs to, so a spouse with no leader had no recorded
  issue. 85/86/87 is Table 1's 83–85 *shape* and still needs nothing, because
  86's leader is on her own line and 87 has none. **Don't reach for METHOD.md's
  attribution machinery on this plate.**
- **258 and 259 are each printed on two different people, and 256 and 257
  appear nowhere.** Both pairs were re-zoomed at 20× specifically to rule out a
  misreading. Encoded as `DUPLICATE_PLATE_NUMBERS` with synthetic ids 256/257.
  **The edition states the fact and does not guess at the cause** — do not
  "repair" the numbering.
- **37 is female though the plate prints `M.`** Her children's clan is her own,
  not her husband's. Reproduced as printed; the correction lives in
  `PLATE_MISPRINTS`, not in the data.
- **The module is not registered in `TABLES` and must not be** until the
  orthography pass finishes. This is the rule that exists so a partial plate
  never reaches `docs/`.

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

- **A half-read plate is never registered in `TABLES`.**
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. The build gate protects `docs/` only. A
  **published** source is quoted and cited; an **unpublished** one is gestured
  at and never named. See METHOD.md rule 4.

## Closed — do not re-raise

- **Genealogy III's structure.** 261 persons, 72 unions, 192 links, seven
  generations, two blocks, `self_check()` green with **all 192 links
  matrilineally consistent on the first run**. The bracket reading is settled
  except for the two calls listed above.
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
