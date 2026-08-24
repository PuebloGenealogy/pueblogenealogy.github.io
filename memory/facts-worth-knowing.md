## Facts worth knowing

- **Clan descent is matrilineal**, so a child's clan must equal its mother's —
  this caught real errors in Table 1 and three brackets on Genealogy II. **It
  only discriminates where the candidate mothers have DIFFERENT clans**, which
  is most of the time and not all of it: three known placement errors (person
  31 on Genealogy II; 19/20 on Genealogy IV; block 2's 230/232/236/238/8 and
  five children on Genealogy III) were invisible to this check because the
  mother and the wrong alternative shared a clan, and two of the three
  shipped. **Where a mother and the alternative share a clan, assume no
  structural check is watching at all.** `self_check()` reporting *all
  structural checks pass* only means clan descent, no-double-child, resolvable
  union ids and closing counts — **it cannot see whether a person is attached
  to the right parents.** For placement, the evidence is the plate itself, the
  bracket-column strip, stubs counted. Treat a report of a "misaligned" or
  "broken" bracket as possibly a **data** error, not automatically a
  **rendering** one — this is exactly the shape Genealogy IV's person-20
  misplacement took, and it survived four `self_check()` runs and every
  publish gate.
- **Person 8 (Yu˙si) appears twice** on Table 1; drawn once, with a
  cross-reference standing in for the repeat.
- **A person who appears twice can carry a different marriage each time, and
  there are now three distinct shapes for it.** (1) **Two groups, two
  `mother_row`s, nothing collides** — Table 1's person 8 has two wives (7 and
  73) both printed under him; the already-drawn occurrence is replaced by a
  child-column note, `SECOND_VISIT_NOTE`. (2) **One person, two husbands,
  printed twice, one marriage each, the second occurrence printing no `+`
  line** — Genealogy II's 169; the renderer's own `SECOND_VISIT_OMITTED`
  suppresses the `+` line/bracket/note and prints the plate's own
  cross-reference row in their place. Don't reach for it when the two groups
  have different mothers — that's shape (1). (3) **Two husbands, issue by
  both, printed ONCE** — Genealogy III's 43; `LEADER_ON_SPOUSE_ROW` in a
  transcription module names which union's bracket the plate hangs off the
  **'+' spouse's** line rather than the primary's. **It also covers a second,
  purely fidelity-driven case** — a single marriage whose leader the plate
  simply draws from the husband's line (`W31`, 58+59→143,144) — and it does
  **not** generalize: ten rows below, the identical-looking 60+61→145 has its
  leader on the wife's own line, because the plate is genuinely inconsistent
  and every entry is read off the ink one union at a time. No gate can see
  this defect (column drift and drawn-count checks both pass regardless); the
  check that finds it is "is any node's first `.line` displaced from its
  node's top," run over every `.node` on any new plate. **A block that looks
  like this shape may not be it** — Genealogy IV's 5/+6/+7 looks like shape
  (3) but is one vertical with a single leader and 7's line carrying no rule
  at all; it was mis-transcribed as two unions until corrected 2026-08-10.
  Count the leaders entering the vertical before counting the lines in the
  block.
- **An id addresses a person; `plate_number` is what prints — and there are
  two distinct reasons they diverge.** A **misprint** (e.g. Table 1's 76,
  which prints 68 but names person 67) shows the plate's wrong number, ringed
  in `--sic`, via `PLATE_NUMBER_MISPRINTS` on the union. A **duplicate**
  (Table 2, where Parsons numbers two different people 101) shows the plate's
  *correct*, unringed number via `DUPLICATE_PLATE_NUMBERS` on the person. Every
  place a number is **shown** reads `plate_number`; every place one is
  **keyed** reads `id`. Get it backwards and either a synthetic id prints on
  the page or a name search jumps to the wrong person. **Do not "fix" a
  misprint to the correct number** — printing the correct number makes the
  chart disagree with the scan, the one thing this edition exists not to do.
  The card shows the number, never the misprint annotation (redundant with the
  chart row the reader opened it from — fixed 2026-07-28).
- **A cross-reference displacement belongs to a plate, not to the edition —
  never apply one plate's offset to another.** Genealogy II's references into
  Genealogy I run one high from person 66 onward (`CROSS_REF_OFFSET`);
  Genealogy III's do not (audited clean 2026-07-31). Genealogy III has four
  exceptions of its own, no two alike. Audit each plate by name, sex and clan.
- **Editorial attribution — four rules govern it (METHOD.md), and the chart
  never carries it.** Two cases exist: Table 1's 83–85/85 (added 2026-07-28)
  and Table 2's 116–118 (added 2026-07-30), both a woman with two husbands, one
  bracket, no stated paternity — the apparatus daggers the split, the chart
  draws the plate's single bracket. **The two differ in evidentiary weight,
  and that difference is rule 4**: Table 1's rests on external documentary
  research and must never name its source; Table 2's rests on **Parsons's own
  text, p. 195** (she records 47 dying childless, corroborating the plate's
  `d.` on him), so its footnote quotes and cites her. Do not flatten the two
  into one rule in either direction. **116–118's paternity is encoded, and 49
  is the father** — declined earlier the same day for want of a footnotable
  source, then satisfied once the user found p. 195 (encoded as
  `TABLES["ii"]["paternity"]`, apparatus only; **the chart still draws the
  plate's own fatherless bracket under 48**, markup byte-identical to
  before). Quoting Parsons trips the `RESEARCH_PROSE` leak gate on her word
  "widow," so that exact phrase is allowlisted — see *The one thing to get
  right* in `CLAUDE.md`.
  Genealogy III needs none of this — its leader-rule placement already marks
  paternity structurally (see `LEADER_ON_SPOUSE_ROW` above). **But "a leader
  absent from one partner's line" does NOT mean "no issue by that
  marriage"** — this file overstated that converse until 2026-08-17; `W31`
  disproves it as a general rule (58 has no leader on her own line and two
  children). 85/86/87 and Genealogy IV's 5/+6/+7 were both re-checked directly
  against the scan on 2026-08-17 and both still stand, but on narrower
  evidence than previously claimed — read the actual ink gap, don't reason
  from "no leader, no issue."
  A **second, distinct kind of editorial claim** exists since 2026-08-09,
  about identity across plates rather than paternity — see METHOD.md's
  *Identity across plates*. It changes nothing in the chart or register; it
  lives only on `/search/` and its index, governed by the same rule 4 in its
  strongest form (no identification here may ever rest on anything but the
  plates themselves).
- **English names in parentheses are plate data**, not research additions —
  person 90 "Heʼsa (Hazel)" on Table 1, the Johnsons and Mana on Table 4.
- **`d.`** means the person had already died when Parsons recorded the
  genealogy (fieldwork 1918–19); a number after a name is age at recording.
- **Phonetic glyph rendering is settled — don't re-open it.** All characters
  in use are in both embedded faces (base64 data URIs, nothing fetched, no
  combining-mark positioning to vary by platform), checked on device on
  Windows and Android. macOS substitutes for any font, so no on-screen
  comparison on a Mac can prove the absence of substitution — read the cmap.
- **Magnification has a floor (~8×), and past it the upscaler invents
  letterform** — a glyph distinction that only survives above that is not
  evidence; the honest finding is "this scan cannot resolve it." A **phone
  photograph of the page is a materially better scan than a bigger crop of the
  original** — this closed a week-old open question in hours once tried.
  Measure marks, don't eyeball them: height (comparable only *within* one
  photograph), horizontal centroid drift, and ink-mass top-vs-bottom together
  distinguish a mirror from a rotation; look at the crop before trusting a
  number, since a mis-boxed crop fails silently with a plausible-looking
  result. Method and worked numbers: `transcription_iii.py`'s docstring.
- **When a glyph question is a choice between known mark/sort populations
  already present on the page, measure those populations first** — don't
  reach for a bigger crop or a new photograph until that has been tried.
  Only request a better photograph when the scan itself lacks the evidence
  to settle the question. (Worked example — Genealogy II's 248/249, resolved
  2026-08-23: `reference/history/plate-reading-chronology.md`.)
- **Reading a plate for TYPE is a different job from reading it for
  STRUCTURE**, constrained by the display rather than the scan — chunk into
  tiles ≤420 native px tall rather than magnifying a whole generation band
  (anything taller than ~1500px downscales on display and becomes illegible).
  Plan tiles from an ink-row profile; a reconciling tile-line count against
  the known entry count is what licenses trusting the rest. Two magnifications
  (4× for number/sex/name, 2.8× for the tail), re-crop at 6–7× only when a
  mark is ambiguous. Table-specific crop geometry and remote-session tooling
  (no `sips`; use Pillow): `reference/environment-notes.md`.
- Google's structured-data validator is **stricter than schema.org** — valid
  schema.org has been rejected twice here. Trust a Search Console report over
  the build's own opinion.

## The four `_FOLD` maps are one map — keep them identical

**All four transcription modules' `_FOLD` maps must stay byte-identical.**
They used to differ (found 2026-08-03, fixed 2026-08-08): only
`transcription_ii.py` folded `ŏ` and `Ĭ`, so two Genealogy III names —
`Dziŏ˙kwid˙yuʼă` (III·101) and `Ĭya˙ʼsi` (III·16) — kept a diacritic in a key
documented as diacritic-free. Measured across all 2,558 string fields in the
four modules before the fix, exactly those two folds changed, and the
per-plate count of colliding folded names was unchanged (2/4/2/1) — the union
of the four maps is a pure bugfix, not a behavior change. **A new character in
a name now needs adding to all four maps, not one** — the cost of the fix, and
the cheaper failure, since four identical maps can be diffed while one drifted
map is silent. This has already been paid once (`ʽ` U+02BD, 2026-08-08 — folds
to `""` exactly as `ʼ` does, so it moved 0 of 713 names, colliding-fold counts
held at 2/4/2/1). `ï` and `ˑ` (U+02D1) are deliberately **not** in the map —
they appear only inside `plate_note` prose on Genealogy II, quoting withdrawn
readings, and are in no name on any plate.

**This is also a `laguna-search` coupling**, not only a data-integrity rule: that
tool folds independently, so a diacritic change here can create a fourth
namesake collision there and stop its build until the pair is adjudicated —
that is expected, not a bug to route around. Full detail on what a new
character needs (which of that tool's two literal sets it belongs in, and
which gate does or doesn't catch a miss): `.claude/rules/search-integration.md`,
which loads automatically once you're working under `vendor/search/` or
`docs/search/`, or read it directly before touching a name's diacritics.

Person references in the apparatus are linked by `_p()` at each call site,
**never by regex over the prose** — the apparatus is full of numbers that
aren't people (1923, vol. 19, pp. 133–292, `d. 1908`), and a loose pattern
catches those too.
