# Session notes — where we stopped

**Rolling handoff. Overwrite this each session; it is not a history.**
History lives in `CHANGELOG.md`. How the project works lives in `CLAUDE.md`.
This file answers one question only: *what would I pick up next?*

Last updated **2026-07-31**, after the session that brought the **Wikidata
payload to four tables** and fixed the **last stale scope claim on the site** —
the landing page's own meta description. The edition is all four plates,
Genealogy III has nothing open on it, and the site is current.

---

## Start here in a new chat

A `SessionStart` hook (`.claude/hooks/session-start.sh`) loads this file and
prefixes `STALE:` or `UNCOMMITTED WORK:` when either applies. Believe those
warnings over anything written here.

1. **`git switch main && git pull`.**
2. Read the top entry of `CHANGELOG.md`.
3. Read `CLAUDE.md` — **The one thing to get right**, **Release policy**, and
   **Design invariants**.
4. Preview: `preview_start`, config name `site`. **It will not necessarily be on
   4173** — if that port is held, the tool assigns another and tells you which;
   use the port it reports. **Don't call `preview_stop` when you finish** — the
   user may still be looking at it.

**A rebuild on a later day dirties `docs/` with dates alone** — `dateModified`,
the "Last updated" line, the sitemap's `lastmod`. So "rebuild produces no diff"
is a valid sync check only *within* a day. `docs/` was last built on
**2026-07-31**; on any later date the first rebuild shows a date-only diff. If
that is all it is, `git checkout -- docs/` rather than committing.

## State

**Nothing is half-finished, and this is true rather than reassuring.** `main`
is current and pushed at `8cc4bee`, clean tree, no open PRs. Genealogy III's
`#note-crossref` is **live**. `--public` exits 0, builds 6 pages,
104 / 275 / 261 / 73 persons; all four `self_check()`s pass; the privacy gate
reports no research chips or vocabulary in 6 pages; 10 JSON-LD blocks valid.
A rebuild after the push left the tree clean, so `docs/` and the source agree
byte-for-byte.

**Verified live:** all six `.html` byte-identical to `docs/` by SHA-256, five
pages plus `sitemap.xml`, `robots.txt` and `404.html` all 200, sitemap 5 `<loc>`
entries (landing page plus one per plate — one fewer than the build's page
count, because `404.html` is deliberately absent), 0 stale-identity markers.
`#note-crossref` present once on `/genealogy-iii/` with 261 person anchors
beside it, 0 research markers on all five served pages.

The 0.023px sub-pixel offset on Genealogy II's 158 group is still known,
diagnosed and deliberately left alone. Invisible; not worth touching shared
bracket code.

## The open thread

**There isn't one, on the plates or on the site.** Genealogy III's two
editorial items are both closed (see *Decisions*), no plate has an open
reading, and the footnote is published. What remains is **outreach**, **one
correctness item on Genealogy I**, and **the release** — none of them blocking
each other, and every one of them needing the user rather than a build.

The one thing waiting on the user is **running the Wikidata batch**. The payload
at `wikidata-quickstatements.txt` is **current for all four tables** and every
Q/P id in it was re-verified live on 2026-07-31; a search confirms **no item for
this edition exists yet**, so it is still a `CREATE`. Paste it into
QuickStatements V1 at `quickstatements.toolforge.org` — it needs the user's
Wikidata OAuth login, which is the whole of why this cannot be finished without
them — then **record the resulting Q-number in `CLAUDE.md` and here**. Nothing
gates it: the custom-domain question that used to sit in front of every inbound
link was closed on 2026-07-31 in favour of staying on `github.io`, so the host
every seeded link points at is settled and permanent.

**The user asked on 2026-07-31 for this to be waiting for them at the next
`resume`.** They had the payload in hand and ran out of time; nothing about it
is unfinished. When they pick it up, **send them the file itself** rather than
pasting its contents into the reply — **the separators are tabs**, QuickStatements
V1 splits each line on them, and a re-render can turn them into spaces and fail
every line. If the tabs are mangled in transit anyway, the fallback is a
`#/v1=` URL using `|` between columns and `||` between rows. The three
non-obvious choices inside the payload — `P2093` over `P50`, `P144` to
`Q51498010`, and no counts of individuals — are explained in `CLAUDE.md` under
*Inbound links*; don't re-derive them, and don't re-verify the ids, which were
checked live on 2026-07-31.

## Other things that could be picked up

| | Effort | Notes |
|---|---|---|
| **Wikidata item** | ~5 min, **needs you** | Payload at `wikidata-quickstatements.txt` is **current for four tables and ready to run**, 19 ids verified live, still a `CREATE`. Only the OAuth-logged-in batch run is left. Record the Q-number afterwards |
| **AMNH Digital Library** | Slow, **needs you** | Strong inbound link. Handle `2246/158` — `https://digitallibrary.amnh.org/handle/2246/158`. That is the identifier `.zenodo.json` omits from `related_identifiers`. The site 403s automated fetches; use a real browser. **Now also the only route to settling the turned-comma mark** — see below |
| **Confirm the 83 / 84 attribution** (Genealogy I) | Needs you + the records | 85 is firmly pinned. 83 and 84 rest on ages that do not cleanly reconcile. Published and citable, so this is the open item with a correctness edge |
| **A wrapped cross-reference still miscounts its row** | Unknown; needs a design call | `row += 1` assumes one visual line. Nothing wraps today. Unguardable at build time — no font metrics. The fix is to split at the plate's own line break with `\|`, as 160, 169 and III's 155 do |
| **Register's relation lists lack the point** | ~1 line | They read `56 Weʼdyumă` where entry titles read `56.`. One line in `rel_link`, but it changes the apparatus |
| **Cross-plate references are never links** | Deliberate, not a gap | No reference from one plate into another is a link, on any plate. **Genealogy III's new `#note-crossref` now states this in so many words**, as Genealogy II's note on 160 and 163 already did. Making them links would be a new feature across all four plates |
| **Cut the release** | **Not yet — see the policy** | Two of the four clauses now met: all four plates published, **and the editorial items on III are closed**. Still outstanding: `.zenodo.json` describes three plates, and the AMNH handle is absent from `related_identifiers`. **Publishing the site is not releasing it** |

## Decisions already made — don't re-litigate

**From this session:**

- **Genealogy III's four cross-reference exceptions DO get a footnote**, and the
  user chose the fullest of four options: one `#note-crossref` in the apparatus,
  naming each exception **and the person each reference actually reaches**. It
  is in `TABLES["iii"]["notes"]`. The chart did not change and no reference is
  corrected in the data. Two options were declined — marking the four affected
  rows on the chart (it would put a numbering displacement in the same visual
  register as a printed misprint), and a short note that named no targets.
- **The turned-comma mark is closed as UNANSWERABLE FROM THIS SCAN.** The 20×
  test was run on 157 against 159, a known U+02BC two lines below it in the same
  block of type. **At 20× the two are the same amorphous blob** — a mark on this
  plate is about ten pixels of ink, and the difference visible at 6×–8× is the
  upscaler inventing an edge. All five (154, 156, 157, 228, 242) stay U+02BC.
  **Do not re-crop this.** 154, 228 and 242 were deliberately not magnified
  individually: the limit is a property of the scan and applies to every mark
  equally. Only a higher-resolution scan would settle it.
- **The note's counts were measured from the data, not copied.** 56 numeric
  references: 51 on the numbered lines, 5 in the two prose notes under 155. The
  docstring's "51 plus two" meant two prose *notes*.
- **`transcription_iii.py`'s docstring said the Gen. I half of 170–174 was
  exact throughout**, which contradicted exception (c) — 173's `Gen. I, 149`.
  Corrected in the module; the published note never carried the wrong claim.
- **An ink-geometry measurement was attempted and thrown away.** Bounding box
  and centroid, decoding PNG with `zlib` since there is no PIL. The crop windows
  caught neighbouring glyphs, so the numbers are contaminated. **They are not
  evidence and appear nowhere.** The visual test carries the conclusion.

**Still standing from earlier sessions:**

- **22's bracket runs 80, 82; 83 is 25's, and the plate's rule is over-drawn.**
  The chart draws two brackets where the plate draws one — the one place on this
  table where the drawn structure departs from the scan. Footnoted at
  `#note-overdrawn`.
- **43's bracket carries two leaders**, hers to 124 and 45's to 126. `W25`
  43+44 → 124, `W26` 43+45 → 126; this is what `LEADER_ON_SPOUSE_ROW` is for.
- **The four `drawn_under` values are confirmed against the scan** — W23, W34,
  W36, W45.
- **III's three non-numeric misprints print as the plate sets them**, ringed in
  `--sic`, under `#note-misprint`.
- **Genealogy III needs no editorial attribution, anywhere.** The plate marks
  paternity itself. Don't reach for METHOD.md's attribution machinery here.
- **III does NOT share Genealogy II's +1 displacement into Genealogy I.** Never
  carry `CROSS_REF_OFFSET` over. This is now stated on the published page.
- **`|` in a cross-reference is a typographic line break, never a change of
  subject.**
- **192 is `Kiwaʼdyuwi`, with no raised dot, and the plates disagree** with
  Genealogy II's 188. Verified at 25×. Don't "fix" it.
- **191 `Ramona` vs Genealogy II's `Ramona of Sant Ana` is not a divergence** —
  this file stores "of Sant Ana" in `origin`.
- **152 and 153 are spelled differently at their two occurrences.**
- **`ORTHOGRAPHY_VERIFIED` is `True` and the pass is not to be redone.**
- **258 and 259 are each printed on two different people, and 256 and 257
  appear nowhere.** `DUPLICATE_PLATE_NUMBERS`, synthetic ids.
- **37 is female though the plate prints `M.`**

**Standing decisions from earlier sessions are in `CLAUDE.md`, not here.**
Two are repeated here **on purpose**, because acting on either wrongly is
expensive and this is the file a session reads first:

- **Publishing the site is not cutting a release.** Zenodo's webhook is on this
  repo; a GitHub release mints a permanent version doi that cannot be deleted.
- **Research evidence never enters the repo** — not `plate_note`, not a commit
  message, not a changelog entry. A **published** source is quoted and cited; an
  **unpublished** one is gestured at and never named. METHOD.md rule 4.

## Closed — do not re-raise

- **The custom domain. Closed by the user 2026-07-31: the edition stays on
  `pueblogenealogy.github.io` permanently.** Not deferred this time — decided.
  A domain is portable but survives only while someone renews it, and a lapsed
  one is re-registered rather than merely lost, which would point every seeded
  citation at a squatter. `github.io` cannot lapse. Full reasoning in
  `CLAUDE.md`; **don't re-derive it**, the obvious argument reaches the wrong
  answer. **The gate on seeding inbound links is lifted** — Wikidata and AMNH
  no longer wait on anything.
- **Genealogy III, entirely — now including both editorial items.** Read, drawn,
  audited, verified, live, footnoted, **and the footnote is deployed**. Nothing
  on this plate is open.
- **Pages lags a push by seconds, and that is not a failed deploy.** Genealogy
  III's page served the previous build on the first SHA-256 pass and matched
  ten seconds later. **Poll; never rebuild to "fix" a `DIFF`** — rebuilding
  changes the local hash you are comparing against and hides the recovery.
- **Whether the plate can be drawn.** All 261 drawn, 0.000 px column drift at
  every generation in both blocks, every block row a whole `--lh`, no node's
  first line displaced from its top.
- **173's `See Gen. I, 149`.** It is what the plate prints and it does not
  resolve. The person is Genealogy I's 49. **Now stated on the page.**
- **Genealogy II's placement and glyph readings.** No remaining errors.
- **31 is not 9+10's son, and 33 is.** Verified three times.
- **Glyph rendering on Windows and Android was checked on device.**
- **The GitHub Pages build API misreports the deployed commit.** Verify deploys
  by SHA-256 against the committed `docs/` file; `/publish` Gate 6 does this.
- **A privacy sweep must assert the content is present.** Use `curl -sL` *and*
  assert something like `id="p116"` exists.
- **`sips --cropOffset 0 0` centre-crops.** Use `1 1`. In `CLAUDE.md`.
