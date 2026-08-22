# Genealogy II read group by group against the scan

The half `audit.py` cannot do — **the number printed against each stub** — for
Table 2's 52 bracketed groups. The rig's 23 problems are its own pairing, not
findings; this file is where each one is either explained or turned into a
correction. Read `README.md`'s Table 2 section before quoting a number here.

**Status: 16 of 52 groups read. No correction owed so far.**
Block 3 complete (8/8). Block 2 at 8 of 17. Block 1 not started (0 of 27).

## Method

`brackets.py` at the calibrated settings gives every vertical's y extent and
stub rows. Each verdict below reads a **native-resolution crop** of those rows
at 2–2.6x, and identifies the group from the **numbers printed against the
stubs** rather than from the rig's pairing. Where a rule's position is itself
the question, the ink is measured, not eyeballed.

Two tools, both in the session scratchpad and both worth rebuilding rather than
hunting for — they are twenty lines each:

- `cut.py X Y W H OUT [SCALE]` — one native crop, NEAREST-scaled.
- `stubs.py OUT X W SCALE y1 y2 …` — **stacks the plate rows a bracket's stubs
  enter into one image**, hairline-separated. This is what makes the read
  affordable: a nine-child group is one picture, not nine. A group whose stubs
  are 1500px apart (U41) reads exactly as cheaply as one whose stubs are
  adjacent.

Coordinates are plate px on `sources/parsons-1923-table-2.jpg` (7770 × 12681).
Column x: g2 1292 · g3 2488 · g4 3662 · g5 4813 · g6 5933.

**A caution paid for on the way**: the `PERSONS` schema is
`(id, generation, sex, name, alt_name, age, clan, vital_note, origin,
cross_ref, plate_note)` — **age is index 5**, between `alt_name` and `clan`.
A helper that read it at index 8 reported every age as absent, which for one
turn looked like a run of missing ages on the plate. They are all present.

## Verdicts

### Block 3 — COMPLETE, 8 of 8, nothing to correct

| group | claim | plate | |
|---|---|---|---|
| U41 | 232 + 233 → 54, 235, 237, 238, 240, 242 | 6 stubs, same numbers | ✓ |
| U52 | 234 + 54 → 244, 246, 248–253 | 8 stubs, same numbers | ✓ |
| U53 | 236 + 235 → 254, 256, 258, 259, 260 | 6 stubs; the sixth is 255 | ✓ |
| U54 | 239 + 238 → 261–264 | 4 stubs, same numbers | ✓ |
| U55 | 240 + 241 → 265, 266, 267 | 3 stubs, same numbers | ✓ |
| U56 | 243 + 242 → 268, 269 | 2 stubs, same numbers | ✓ |
| U60 | 254 + 255 → 270, 271, 272 | 3 stubs, same numbers | ✓ |
| U61 | 256 + 257 → 273, 274 | 2 stubs, same numbers | ✓ |

Every name, sex, age, clan, dash and parenthesised English name on these 34
lines matches the transcription, including the fiddly ones: 238's
`(Fred Kai)`, 264's dash **followed by a period**, 268 and 269 printing a dash
for name *and* clan with no sex, 259's number set without its period, and 54
printing as `Ma˙ʼran˙i` where the id's name field reads `Ma˙ʼrani` — which is
the discrepancy already verified in its `plate_note`.

**U53's sixth stub is 255's, and it is already documented.** The bracket carries
stubs into 254, 255, 256, 258, 259 and 260; **257 takes none**. 255 is the `+`
line, and 255's own `plate_note` records this as the only `+` line on the plate
to take a leader. It is not descent — 255 is Eagle and every child is Water.
So the plate's 6 stubs against the transcription's 5 children is **correct as
transcribed**, and this is the one place on the plate where stub-counting alone
would convict a sound reading.

**Closes three of the 23.** *U60 brackets 2 against 3* and *U61 brackets 3
against 2* are the two groups' brackets **swapped by positional pairing** — U60
had been handed a block-1 bracket 8000px away. The unclaimed *generation 6
bracket at x 5954, y 11730–11780* is U61's real one.

### Block 2 — 8 of 17

| group | claim | plate | |
|---|---|---|---|
| U42 | 167 + 166 → 186, 188–195 | 9 stubs, same numbers | ✓ |
| U43 | 169 + 168 → 196–200 | 5 stubs, same numbers | ✓ |
| U44 | 169 + 183 → 225, 226 | 2 stubs, same numbers | ✓ |
| U45 | 171 + 170 → 201–206 | 6 stubs, same numbers | ✓ |
| U46 | 173 + 172 → 207, 208 | 2 stubs, same numbers | ✓ |
| U47 | 175 + 174 → 209, 210, 211 | 3 stubs, same numbers | ✓ |
| U48 | 176 + 177 → 212–217 | 6 stubs, same numbers | ✓ |
| U50 | 182 + 181 → 220–224 | 5 stubs, same numbers | ✓ |

Still to read: **U35, U36, U37, U38, U39, U40, U49, U51, U57**.

**U46's leader ends in mid-air, and that is the plate.** Measured: the vertical
is x 4823–4824, **y 8747–8817**, stubs at 8755 and 8808. 173's leader runs
**x 4676 → 4818 at y 8703** — one row above the vertical's top and 5px short of
it, across blank paper the whole way (luma 215–230; these rules run under 60).
It is unambiguously the `+ 173 … Bear———` row and no other rule enters from the
left here, so the group hangs off 173 exactly as transcribed.

**U50 and U44 are one detection, and that is the rig.** Their brackets abut:
U50's vertical terminates on 224 and U44's begins on 225, 29px below. The run
came back as a single 6-stub vertical, y 10004–10252, carrying **two** leaders
(10011 on 182's line, 10251 on 169's). Hence *U44 brackets 6 against 2* and
*U50 has no bracket at all* — one merge, two problems.

**U43's bracket is 5 stubs; the rig found the bottom 3.** Detected y 7694–7978
over 198, 199, 200, so 196 and 197 at ~7556 and ~7662 fell outside. The top
corner and 196's leader are plainly there in the crop. Hence *U43 brackets 2
against 5*, and the vertical it was given instead is U46's.

## Running total against the rig's 23 problems

**Nine explained, none a defect**: the U60/U61 swap (2) and U61's unclaimed
bracket (1); U46's count and its +2217px leader (2); U44's count and U50's
missing bracket (2); U43's count (1); and U52's count, which was U46's
mispairing reported from the other end (1).

Every one is the same mechanism the README already names — **a group that
cannot be matched by leader takes a leftover bracket in plate order** — plus
two detections that split or merged a run. Nothing so far is a finding about
the transcription.

## Open questions, flagged not settled

- **248 and 249's medial marks** (U52). At 6.5x, 248 reads `Oyo` + a raised dot
  + what may be **two** apostrophes before the `y`, against the transcription's
  `Oyo˙ʼyʼăi` — one apostrophe before the `y` and one after. 249 is the same
  shape. Both are plausible as transcribed and neither is confirmed; a raised
  dot and an apostrophe are hard to separate at this size. **This belongs to an
  orthography pass, not to the bracket read** — Genealogy III took those as two
  separate passes (placement 2026-08-17, orthography 2026-08-21) and this plate
  should too. Do not correct either on the strength of this note.
