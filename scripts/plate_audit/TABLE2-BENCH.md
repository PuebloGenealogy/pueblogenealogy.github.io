# Genealogy II read group by group against the scan

The half `audit.py` cannot do — **the number printed against each stub** — for
Table 2's 52 bracketed groups.

**COMPLETE, 2026-08-23. All 52 groups read. No correction is owed to
`transcription_ii.py`.** Every group's stubs carry exactly the numbers the
transcription lists, in order; clan descent holds at all 52; and every leader
sits on the line of the parent the transcription names.

**All 23 of the rig's problems are explained and none is a defect.** They are
now a known-clean baseline in the sense Table 3's 15 and Table 4's 10 are:
**diff the list, do not read it fresh.** A 24th problem, or a change in which
ids appear, is the signal.

Read `README.md`'s Table 2 section before quoting any number from a run.

## Method

`brackets.py` at the calibrated settings gives every vertical's y extent and
stub rows. Each verdict reads a **native-resolution crop** of those rows at
2–2.6x and identifies the group from the **numbers printed against the stubs**,
never from the rig's pairing — which is the whole point, since the pairing is
what is untrustworthy on this plate. Where a rule's position was itself the
question, the ink was measured rather than eyeballed.

Two tools, twenty lines each, in the session scratchpad:

- `cut.py X Y W H OUT [SCALE]` — one native crop, NEAREST-scaled.
- `stubs.py OUT X W SCALE y1 y2 …` — **stacks the plate rows a bracket's stubs
  enter into one image**, hairline-separated. This is what made the read
  affordable, and it is the piece worth rebuilding rather than hunting for: a
  nine-child group is one picture, not nine, and a group whose stubs are
  1500px apart (U41) reads exactly as cheaply as one whose stubs adjoin. The
  whole plate went in about twenty images.

Coordinates are plate px on `sources/parsons-1923-table-2.jpg` (7770 × 12681).
Column x: g2 1292 · g3 2488 · g4 3662 · g5 4813 · g6 5933.

**A caution paid for on the way**: the `PERSONS` schema is
`(id, generation, sex, name, alt_name, age, clan, vital_note, origin,
cross_ref, plate_note)` — **age is index 5**, between `alt_name` and `clan`. A
helper that read it at index 8 reported every age as absent, which for one turn
looked like a run of missing ages on the plate. They are all present.

## What was and was not verified

**Verified for all 52 groups**: the number against every stub; the child list
and its order; clan descent; and the parent whose line the leader hangs off —
for the 42 groups the rig paired *by identity* that pairing is itself the
check, and the 10 it paired by position were each traced by hand (below).

**Not a systematic orthography pass.** Names, sexes, ages and dashes were read
off the crops and matched everywhere they were legible, including the awkward
ones — 14's braced two-line name, 161's `M.-F.` sex, 264's dash *followed by a
period*, 268 and 269's dashes for name *and* clan with no sex, 259's number set
without its period, 42's `(Annie)`, 140's `(Hazel)`, 238's `(Fred Kai)`, and
the two people Parsons both numbers **101**. But this pass was aimed at
placement. Genealogy III took placement (2026-08-17) and orthography
(2026-08-21) as two separate passes and this plate should too; **two marks are
flagged below and neither is settled**.

## Verdicts

### Block 1 — 27 of 27

| group | claim | plate |
|---|---|---|
| U01 | 1 + 2 → 3, 5, 7 | 3 stubs ✓ |
| U02 | 3 + 4 → 9, 11 | 2 ✓ |
| U04 | 7 + 8 → 15, 17, 19, 22, 24 | 5 ✓ |
| U05 | 9 + 10 → 26, 29, 33 | 3 ✓ |
| U06 | 11 + 12 → 35, 36, 38, 40, 41, 42, 44 | 7 ✓ |
| U07 | 13 + 14 → 45, 47, 50, 51, 53 | 5 ✓ |
| U08 | 16 + 15 → 56, 58, 60, 63, 64 | 5 ✓ |
| U09 | 18 + 17 → 65, 66 | 2 ✓ |
| (19) | 19 → 67–74 | 8 ✓ |
| U12 | 23 + 22 → 75–79 | 5 ✓ |
| U13 | 25 + 24 → 80, 81, 82 | 3 ✓ |
| U14 | 27 + 26 → 83, 84 | 2 ✓ |
| U15 | 28 + 26 → 85–90 | 6 ✓ |
| U16 | 29 + 30 → 91–96 | 6 ✓ |
| U18 | 33 + 34 → 98, 99 | 2 ✓ |
| U21 | 42 + 43 → 101, 101, 102, 103, 104, 105 | 6 ✓ |
| U22 | 46 + 45 → 106–115 | 10 ✓ |
| (48) | 48 → 116, 117, 118 | 3 ✓ |
| U25 | 52 + 51 → 119, 121 | 2 ✓ |
| (53) | 53 → 122, 124, 125, 127 | 4 ✓ |
| U28 | 57 + 56 → 128, 129 | 2 ✓ |
| U29 | 58 + 59 → 130–136 | 7 ✓ |
| U30 | 61 + 60 → 137, 138, 139 | 3 ✓ |
| U31 | 62 + 60 → 140–143 | 4 ✓ |
| U32 | 119 + 120 → 144, 145, 146 | 3 ✓ |
| U33 | 122 + 123 → 147–151 | 5 ✓ |
| U34 | 125 + 126 → 152, 153 | 2 ✓ |

**U21 is the duplicate, and the plate prints it exactly as recorded.** Two
consecutive stubs both read **101** — `101. F. Naauʼg˙ŭyăiʼ. Water` and
`101. M. — d. Water` — then 102–105. `DUPLICATE_PLATE_NUMBERS = {1010: 101}`
is right, and the synthetic id never appears on the page.

### Block 2 — 17 of 17

| group | claim | plate |
|---|---|---|
| U35 | 154 + 155 → 14, 156, 158, 161, 162, 164 | 6 ✓ |
| U36 | 157 + 156 → 166, 168, 170, 172 | 4 ✓ |
| U37 | 159 + 158 → 174, 176 | 2 ✓ |
| U38 | 160 + 158 → 126, 178 | 2 ✓ |
| U39 | 163 + 162 → 180, 181 | 2 ✓ |
| U40 | 164 + 165 → 169, 184 | 2 ✓ |
| U42 | 167 + 166 → 186, 188–195 | 9 ✓ |
| U43 | 169 + 168 → 196–200 | 5 ✓ |
| U44 | 169 + 183 → 225, 226 | 2 ✓ |
| U45 | 171 + 170 → 201–206 | 6 ✓ |
| U46 | 173 + 172 → 207, 208 | 2 ✓ |
| U47 | 175 + 174 → 209, 210, 211 | 3 ✓ |
| U48 | 176 + 177 → 212–217 | 6 ✓ |
| U49 | 178 + 179 → 218, 219 | 2 ✓ |
| U50 | 182 + 181 → 220–224 | 5 ✓ |
| U51 | 185 + 184 → 227, 228 | 2 ✓ |
| U57 | 186 + 187 → 229, 230, 231 | 3 ✓ |

### Block 3 — 8 of 8

| group | claim | plate |
|---|---|---|
| U41 | 232 + 233 → 54, 235, 237, 238, 240, 242 | 6 ✓ |
| U52 | 234 + 54 → 244, 246, 248–253 | 8 ✓ |
| U53 | 236 + 235 → 254, 256, 258, 259, 260 | 6 stubs; the sixth is 255 ✓ |
| U54 | 239 + 238 → 261–264 | 4 ✓ |
| U55 | 240 + 241 → 265, 266, 267 | 3 ✓ |
| U56 | 243 + 242 → 268, 269 | 2 ✓ |
| U60 | 254 + 255 → 270, 271, 272 | 3 ✓ |
| U61 | 256 + 257 → 273, 274 | 2 ✓ |

**U53's sixth stub is 255's, and it is already documented.** Stubs enter 254,
255, 256, 258, 259 and 260; **257 takes none**. 255's own `plate_note` records
it as the only `+` line on the plate to take a leader, and it is not descent —
255 is Eagle and every child is Water. **This is the one group on the plate
where counting stubs alone would convict a sound reading.**

## Why the rig reported 23 problems — seven mechanisms, no defects

Positional pairing is the biggest, exactly as the README warns, but it is not
the only one, and **two of these are not in the README's list of three**.

1. **Positional pairing after an unmatched group** — U38, U43, U46, U49, U52,
   U53, U60, U61, and the leader flags on U07, U44, U46 and U49. On this plate
   the fallback reaches **across descent blocks**: U60 was handed a block-1
   bracket 8000px away, U49 a block-3 one. One unmatched group high in a column
   costs everything below it.
2. **Two abutting brackets merged into one run** — U50's vertical terminates on
   224 and U44's begins on 225, **29px below**. The run came back as a single
   6-stub vertical (y 10004–10252) carrying **two** leaders, 10011 on 182's line
   and 10251 on 169's. One merge, two problems: *U44 brackets 6 against 2* and
   *U50 has no bracket at all*.
3. **One bracket split into two fragments** — U33's single 5-stub vertical over
   147–151 came back as y 2848–2938 and y 2976–3070, three stubs each, and the
   second fragment then displaced U34. Hence *U33 brackets 3 against 5* and
   *U34 brackets 3 against 2*. A paper repair taped across 148–149 is visible
   in the crop and is the likely cause of the break.
4. **A vertical detected below its own top stub, which is then read as a
   LEADER.** This is Table 4's `V01` failure reproduced on Table 2, and it is
   the commonest shortfall here — **U30** (137's stub at y 3923 reported as a
   leader at 3927, leaving 138 and 139 as the only "children"), **U43** (196
   and 197 lost, bottom 3 of 5 detected), **U38** (126 lost, 1 of 2 detected).
   `--overshoot` cannot rescue any of them: it widens the **left** side only.
5. **A fold crease read as a stub** — the (53) group. The rig found 5 stubs
   where the plate prints 4. The extra, at y 2968, has a 153px dark run at
   x 4795–4948, which is *stub-shaped on width alone* — a real stub two rows
   below measures 139px at x 4777–4916. At 5x it is unmistakably the torn
   overlapping paper edge of the crease, with no stub anywhere on that row.
   **This is the one mechanism that inflates a count rather than shortening
   it**, and the only one where the ink test alone points the wrong way.
6. **Near-duplicate detections of one rule** — the unclaimed *generation 3
   bracket at x 2542, y 8520–10241* is a second reading of U35's vertical at
   x 2519, and the g4 run at x 3688, y 7568–8608 is a second reading of U36's
   at x 3672. The README already warns these are worse than harmless.
7. **Brackets not detected at all** — U49 (218, 219) and U51 (227, 228), both
   two-stub groups in the faint lower-middle of the plate. Both are plainly
   there in the crops.

## Two things worth not re-deriving

**U46's leader ends in mid-air, and that is the plate, not a fault.** Measured:
the vertical is x 4823–4824, **y 8747–8817**, stubs at 8755 and 8808. 173's
leader runs **x 4676 → 4818 at y 8703** — one row above the vertical's top and
5px short of it in x, over blank paper the whole way (luma 215–230 down the
gap; these rules run under 60). It is unmistakably the `+ 173 … Bear———` row
and no other rule enters from the left, so the group hangs off 173 as
transcribed.

**U30's leader is on 61's own line** — `+ 61. F. Tsikʼaʼyăaitsʼa. d. Eagle———`
runs right into the bracket. 60's line sits two rows above it because
`See Gen. I, 68` is printed between them, which is what the audit's
"two rows under 60" model is for.

## Suggested next step for the rig, not taken here

Mechanism 5 is the one a flag might fix: **`--ongrid` is off for Table 2** and
it is precisely the tool Table 3 uses to reject crease blots, on the grounds
that a crease lands off the row grid while every real stub sits a whole number
of rows from its neighbour. Turning it on should drop the (53) group's phantom
fifth stub. It was **not** changed here, because a flag change has to be
re-baselined — and until today Table 2 had no baseline to diff against. It has
one now, which is what makes the experiment safe to run.

## Open, flagged not settled

- **248 and 249's medial marks** (U52). At 6.5x, 248 reads `Oyo` + a raised dot
  + what may be **two** apostrophes before the `y`, against the transcription's
  `Oyo˙ʼyʼăi` — one before the `y` and one after. 249 is the same shape. Both
  are plausible as transcribed and neither is confirmed; a raised dot and an
  apostrophe are hard to separate at this size. **Belongs to an orthography
  pass. Do not correct either on the strength of this note** — and note the
  magnification floor: past ~8x the resampler invents letterform, so if the
  scan cannot settle it, the answer is a photograph of the page, not a bigger
  crop.
