# Per-plate reading chronology

Not auto-loaded. Current reading status for each plate belongs in
`SESSION-NOTES.md` (rolling) and `memory/standing-decisions.md` (settled
conclusions) — this file is the order-of-events record for how each plate
reached its current state, kept so nobody re-derives "was this actually
checked" from scratch.

**Two passes matter and they are not the same thing: placement (is this
person under the right parents) and orthography (is the name/sex/age/clan
transcribed correctly).** A plate can have one without the other, and
"placement read" was mistaken for "fully read" at least once — see below.

- **Genealogy IV** shipped 2026-07-31 with person 20 attached to the wrong
  marriage (6+7's child rather than 5+6's), and it survived four
  `self_check()` runs, every publish gate, and ten days live. Nothing
  structural could see it: 19 and 20 are both Bear, exactly like their
  mother, so clan descent couldn't discriminate, and the counts closed either
  way. **This is the finding that "no reading question open" is not the same
  claim as "the readings have all been checked."** Corrected 2026-08-10;
  placement read against all stubs the same day.
- **Genealogy I**: placement read 2026-08-17, the printed number checked
  against every one of its 76 stubs. No corrections.
- **Genealogy III**: block 2 read and corrected 2026-08-17 — two placement
  errors on one bracket column (238 and 8 belong to 230+231, not 236+237;
  243/245/246 belong to 236+237, not 232+233), both **Parrot throughout** on
  both sides of the error, the third time clan descent has been unable to see
  a placement error after Genealogy IV's Bear and Genealogy II's 31. Block 1
  was first run through the calibrated plate-audit rig and produced no new
  finding — explicitly not the same as "correct," since the rig can't read
  type and column 6 sits under a fold crease it's blind to. Block 1 was then
  actually read, 2026-08-17: right at every group, including the six
  column-6 groups the crease hides. Its orthography was read 2026-08-21, all
  229 entries, matching the transcription at every field. Nothing was
  corrected on this pass; two things worth not re-finding: 27's death note
  has a compositor-spaced (not data-wrong) period, and 153 carries a
  genuinely mixed record on purpose (first occurrence's spelling, second
  occurrence's age — the plate itself prints her twice, differently). Its two
editorial items are also both closed: the cross-reference footnote is
written and deployed (`#note-crossref`), and the second sort — the `ʽ`
U+02BD reading — is settled at all five instances, persons 154, 156, 157,
228 and 242, published `ebd8738` (PR #34) then `5441abc` (PR #35), both
2026-08-08.
- **Genealogy II**: placement-only through 2026-07-30, when the user's own
  flagged list (31/32/97, 49-under-47, 154+155/232+233, 169's two brackets,
  U52, U60, 254's descent from 235+236) was confirmed resolved. **All 52 bracketed groups
  were read against the scan on 2026-08-23** — a larger and stronger claim
  than the user's list alone — with no correction owed. 116–118's paternity
  was encoded the same day it was first considered (2026-07-30), once the
  user found the citable source (Parsons p. 195, on 47 dying childless).
  **Orthography has had only the first pass (placement); 248 and 249's medial
  marks remain the one open reading question on any plate** — see
  `SESSION-NOTES.md` for current status.

**Every one of these placement errors that clan descent missed shared a clan
between the true parent and the wrong alternative** — Genealogy IV's Bear,
Genealogy II's Water (person 31), Genealogy III's Parrot (block 2). This isn't
three separate coincidences; it's the shape of the check's blind spot, stated
as a durable rule in `memory/facts-worth-knowing.md`.

## The evidence behind two "no-attribution" readings, re-checked 2026-08-17

Both readings still stand, but on narrower grounds than the file that used to
carry this once claimed — worth keeping the actual measurements rather than
just the verdict, in case either is challenged again.

**Table 1's 85/86/87** (a woman with two husbands, one bracket, no stated
paternity): measured in the 160px gap between the text and the bracket, 86's
row carries a solid rule (50/142/138/24 ink px at y 227–230), and **both
husbands' rows are bare** — 85's and 87's alike, the constant 1–2px through
y 231–253 being the bracket vertical passing through, not a leader. So there
is one bracket and one leader, it sits on 86's line, and that line names no
father by itself. What settles the reading is the contrast with **43 on the
same plate**, where a woman's issue by a second husband gets its own leader
on that husband's line (45's, → 126) — 87's line carries nothing at all.
Clan can't help here: both of 86's marriages share her mother, so 184–189 are
Turquoise either way. The basis is Parsons's own practice with 43, not "a
spouse with no leader had no issue," which `W31` disproves as a general rule.

**Genealogy IV's 5/+6/+7** (evidence one step weaker again): measured in the
750px gap, 6's row is solid ink (750/750 at y 6099–6116) and both husbands'
rows carry nothing above 3px — the same configuration as 85/86/87, so the
single leader sits on the line 6 shares with both marriages and names no
father by itself. The difference: **Table 4 never demonstrates its own
convention** the way Table 1 does with 43 — its only other second marriage
with issue is V07, where the second spouse is the mother, whose line carries
the bracket anyway regardless. So this reading's basis has to reach across to
Genealogy III's 43, a cross-plate inference the project otherwise warns
against — kept because locally the bracket is drawn inside 5's block, with 5
as primary and 6, 7 both `+` lines under him. State the basis as cross-plate
if this is ever revisited, never as "a spouse with no leader had no issue."

## Identity across plates — the corpus's own unattested-join count

Since 2026-08-09, `/search/`'s index makes a second kind of editorial claim,
about identity across plates rather than paternity (METHOD.md's *Identity
across plates*; governed by the same rule 4, in its strongest form — no
identification here may rest on anything but the plates themselves). The
corpus carries **713 entries and 620 people, 79 drawn more than once**, of
which Parsons cross-references **65**. The other **14** are listed one by
one — **two of those are hers**, stated through a second husband rather than
by name — so the edition's own unattested count is **twelve**. Every join is
a family joined as a family, never a lone name; a shared name joins nothing,
which is what the three adjudicated namesake pairs exist to say (one still
open as of this writing). This changes nothing in the chart or the
register — the joins live only on `/search/` and its index, and every
unprinted one carries a ringed `NOT PRINTED` marker and quotes nothing.
