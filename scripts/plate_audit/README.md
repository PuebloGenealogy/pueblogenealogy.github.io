# Reading a plate's brackets off the scan

Four throwaway-looking scripts that are not throwaway: they hold a
transcription against **the ink on the plate**, which is the one check nothing
else here can do.

The DOM audit described in `CLAUDE.md` derives the expected leader from
`_GROUPS` and measures the rendered page. It proves data and rendering agree.
It is **silent when both agree with each other and disagree with Parsons** —
which is exactly how Genealogy IV shipped with 20 on the wrong marriage and
survived four `self_check()`s, every publish gate and ten days live. Here the
reference is the scan.

## What it can and cannot decide

**Can:** how many children the plate brackets in each group; how many bracket
verticals a column carries at all (the check that catches one group split into
two, or two merged into one); which row each bracket's leader hangs off.

**Cannot:** the **number printed against each stub**. Nothing here reads type.
A group of the right size whose members are misnumbered passes silently — that
half is a human reading crops, and on Genealogy I it was done on 2026-08-17.

## Running it

`sips` cannot be trusted to crop at an origin (`--cropOffset 0 0` centre-crops;
see `CLAUDE.md`), so everything reads a raw BMP directly. Put the BMP somewhere
scratch — it is ~570 MB for Table 1 and must never be committed.

```bash
sips -s format bmp sources/parsons-1923-table-1.jpg --out /tmp/t1.bmp
python3 scripts/plate_audit/brackets.py /tmp/t1.bmp \
    '[[3200,3700],[6400,6950],[9500,10100],[12700,13500]]' 110 > /tmp/t1.json
python3 scripts/plate_audit/audit.py transcription.py /tmp/t1.json \
    2:3499,3:6643,4:9801,5:12954 80
```

The bands and the column list are **measurements, taken once per plate** by
reading `brackets.py`'s stderr and cropping anything unexplained. Do not let the
script guess them: auto-clustering the detected x values returns the fold crease
and a column of type among the real columns, and silently calls the crease a
generation.

Table 3, whose calibration is set out below, is read with:

```bash
python3 scripts/plate_audit/brackets.py /tmp/t3.bmp '[[0,3770]]' 12 \
    --row=24.7 --track=1 --maxthick=6 --ongrid=0.25 > /tmp/t3.json
```

## The flags, and why each one exists

Every window in `plate.py` was tuned on Table 1 and is stated as a fraction of
its **row pitch**, 146.6px. `--row` multiplies them all. Table 3 sets **24.7px**
to a row in a scan a ninth the pixel count, so leaving it at the default reads
that plate with windows six times too wide. Measure it by autocorrelating the
row-ink profile of a dense list; do not estimate it from the page height.

The rest are **not** row-scaled, because they answer to the scan rather than to
the type, and each was forced by a specific measurement:

| flag | Table 1 | Table 3 | what it answers |
|---|---|---|---|
| `--row` | 146.6 | **24.7** | the plate's row pitch; scales every window |
| `--track` | 0 | **1** | px a rule's window may re-centre per row |
| `--xmerge` | 5 | 5 | px apart two fragments are still one rule |
| `--maxwidth` | 45 | 45 | px beyond which a candidate is type, not a rule |
| `--maxthick` | off | **6** | px deep beyond which a "stub" is a blot |
| `--ongrid` | off | **0.25** | rows of slack before a run is off the grid |
| `minrun` (positional) | 110 | **12** | px of contiguous ink that makes a rule |

`--skew` is **not used by Tables 1 or 3** — see the bow, below. Table 4 is the
plate it was built for and it is still not needed there, because `--track`
absorbs the same drift; see *Table 4* below.

Table 4, whose calibration is set out below, is read with:

```bash
python3 scripts/plate_audit/brackets.py /tmp/t4.bmp \
    '[[2990,3400],[6060,6450],[9100,9500]]' 140 \
    --row=145.8 --track=1 --xmerge=20 --maxwidth=70 --overshoot=140 > /tmp/t4.json
python3 scripts/plate_audit/audit.py transcription_iv.py /tmp/t4.json \
    2:3160,3:6193,4:9260 80 --row=145.8
```

`crop.py` cuts an exact native-resolution PNG for a human to read:

```bash
python3 scripts/plate_audit/crop.py /tmp/t1.bmp 9541 1090 2300 4710 out.png
```

## Calibration is per plate, and skipping it produces confident nonsense

**Parameters tuned on one plate do not transfer.** Table 1 and Table 4 have
different paper, ink weight and scan scale, and the same settings that read
Table 1 cleanly fragment Table 4's stubs.

The cheap test is the **stub-to-stub gap distribution**. What a correctly
calibrated plate gives is a hard spike at one row, a smaller one at two, and
then **nothing at all below one row**:

| plate | gaps |
|---|---|
| Table 1, calibrated | 144–148 × 65, 290–292 × 5, then a sparse tail |
| Table 3, calibrated | 24–26 × 43, 49–51 × 19, then a sparse tail |
| Table 4, calibrated | 144–148 × 27, 290–292 × 2, then a sparse tail |
| Table 4, **before** calibration | 9.5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 … |

Table 4's spray of small gaps corrupts the measured row pitch, which then
flags leaders that are fine — eight of them, four at a constant ~+176px against
a nominal 146px row. **Those were artifacts of the rig, not findings about the
plate.** Check the distribution before believing a single flag.

**Read the test as "nothing under one row", not as "one row and two rows and
nothing else".** That is how this file first stated it and it is wrong about
its own plate: Table 1's calibrated tail runs 437, 582, 728, 872, 1020, 1022,
1312, 1456, 1594, 1746 and 3499px. A group's children are only consecutive
rows when nothing is printed between them, and on a deep plate a great deal
is — Table 3's first bracket carries exactly two children, **169 rows apart**,
because the whole of the elder's descent is set between them. A large gap is
the plate's shape. A **sub-row** gap is the rig fragmenting.

## Table 3, calibrated 2026-08-17 — what its scan does that Table 1's does not

Three things, and none is a matter of turning a threshold down.

**The plate BOWS, it does not skew.** Its left-hand rule runs x 683 at the top,
686 at y 1000, 666 at y 3600 and 671 at the foot — 20px of travel that no
straight line describes, so `--skew` was built, measured at −0.0051, and thrown
away as the wrong model. No fixed window holds 20px either, and widening one to
suit takes in the fold crease. `--track=1` lets a rule's own window re-centre a
pixel a row, and it is what recovers the two longest rules whole: 4184px and
3013px, against four fragments each before.

Two things the tracker had to learn, both found by a bracket going missing:

- **A 2px window cannot be tracked.** The col-7 bracket is exactly that — found
  with the window held still, lost the moment it moves, because the first stub
  it meets drags it off the rule. The traced window is padded to `2·track + 3`.
- **A column carries several brackets, and between them there is nothing to
  follow.** The window holds the x the last rule ended at while the bow has
  moved the next one: the col-3 bracket for 5+6 sits at x 1215 under a rule
  that finished at 1208. After a rule ends the window may jump once to
  re-acquire, by at most its own width — far short of the 535px between
  columns, so it can only ever find the same column's next rule.

**The fold crease crosses a bracket column.** Table 3 is folded in four; two of
its creases (x≈942, x≈1920) fall between columns and are dropped by `XTOL`, but
the third runs at x≈2878–2960, **10px from the col-6 brackets at 2853–2863**.
No x window separates them. What does is that the crease answers the density
test in blots 15 to 94 rows deep where a stub is 2 to 4 (`--maxthick=6`), and
that its blots fall wherever they fall while every real stub sits a whole
number of rows from its neighbour (`--ongrid=0.25`). Together they take the
plate from 8 junk runs and 39 sub-row gaps to **none**, and `--ongrid` rejects
per **run**, not per stub — dropping the odd stub would let a blot be dressed
up as a bracket, whereas dropping the run shows up in the audit as a count the
transcription disagrees with, which is loud.

**Its columns are not a grid.** Table 1's four column x values are worth ±80px
of tolerance. Table 3's column 6 carries brackets at x 2786 *and* x 2854 — 68px
apart, both real, each sitting the same 61–63px left of the children it
brackets. So `XTOL` here is ~75, and a column's x is a range to be measured,
not a number to be assumed.

### Where that leaves it — two real findings, and column 6 still unreadable

Calibrated, the rig found **two placement errors in Genealogy III's block 2**
on 2026-08-17, both confirmed by the user against the scan and published: 238
and 8 are 230+231's sons rather than 236+237's, and 243, 245 and 246 are
236+237's rather than 232+233's. Both surfaced as **child-count
disagreements** and neither was visible to the leader test — which is why
`audit.py` now pairs by identity and reports counts.

Against the corrected transcription the run reports **15 problems, none of
them a new finding**:

| | what it is |
|---|---|
| W13 | the only count disagreement paired by IDENTITY, and already explained — 22's vertical is over-drawn past 82 to reach 83, who is 25's child (confirmed 2026-07-31) |
| W12, W37, W40, W52 | count disagreements **paired by position**, which the output labels. Guesses |
| W53–W55, W58, W60, W71 | bracketless, every one in column 6 under the crease |
| W19, W31, W69, W47 | leader flags, all on positional pairs — evidence about the guess, not the plate |

**Count them with `grep -cE "^  - "`.** This section said 14 for an hour
because the number was read off a `tail -14` that had truncated the list.

**Column 6 cannot be read by this tool at all** — six of its groups never match
— and that is the crease, not a setting. It needs crops and a human.

**It got one on 2026-08-17, and all 15 are now explained.** Block 1 was read
group by group against the scan and the transcription is right at every group.
The six bracketless groups are real brackets the crease hides — counts and clans
all match. The four count disagreements are the rig losing a stub across a tall
row: W12 is 4 not 3, W37 is 6 not 5, W40 is 8 not 6, W52 is 7 not 2, and the
culprit each time is a *See Gen.* continuation row, or 155's "For first
husband…" prose block, widening a gap. W19 and W69's leaders are on the
mother's **own** line, verified at 3x — the offset is the continuation row under
32 and under 243 — and W47 is 92 printed twice, the leader on her first
occurrence.

**One flag was real, and it was not a reading error:** W31, where the plate
hangs 58 + 59's bracket off the **husband's** line. Encoded as
`LEADER_ON_SPOUSE_ROW = {"W26", "W31"}` and published the same day. The plate is
not consistent about it — 60 + 61 → 145 is the same shape with the leader on
60's own line — so this is a per-union reading, never a rule to generalise.

**So the 15 are now a known-clean baseline.** A 16th problem, or a change in
which W-ids appear, is the signal. Re-run with the calibration above and **diff
the list**, rather than reading it fresh. The half this tool cannot do — the
number printed against each stub — **was** done for block 1 in that pass, which
is what makes the baseline trustworthy. What was not done is the orthography:
names, ages and diacritics were not re-read.

**Do not report any of the 15 as a defect in the transcription.** A positional
pairing is exactly the basis on which one of the two real errors above was
nearly dismissed.

## Table 4, calibrated 2026-08-17 — what its scan does that the others do not

**Its row pitch was never the problem.** Measured at **145.8** from the stub
grid (431 long baselines of page type gave 146.7, and the stub gaps are the
better measure: 1312/9, 1166/8, 1019/7 all land on 145.6–145.8). Table 1's
default of 146.6 was already within half a percent. What made the plate look
uncalibrated was two other things.

**A full-width band reads the plate's own borders as brackets.** Table 3 can be
read with `'[[0,3770]]'` because its junk is the fold crease. Table 4 has long
printed verticals at x 2850–2975 and 7704–7789 that answer every density test:
one is a 3306px run carrying **74 "stubs" 12px apart**, which is the entire
sub-row spray this file used to attribute to fragmentation. Narrow bands drop
it, exactly as Table 1's do, and the spray goes to **none**.

**A band must hold the rule PLUS the stub reach on BOTH sides.** The first
narrow bands tried here were 230px wide and cost `V05` all five of its stubs —
`stubs()` gives up when `b - a < reach * 0.6`, and 62px of band to the right of
the rule is under the 110px reach. It reports **zero stubs on a bracket that
plainly has five**, which looks exactly like an ink problem and is not. Allow
the rule's whole x drift plus ~150px each side.

**The plate SKEWS where Table 3 bows, and it is the one plate `--skew` was built
for.** Its generation-2 rule runs x ≈ 3195 at y 722 and 3132 at y 5800 — 63px,
and the per-200px differences are near-constant at −0.012 px per px of y, which
is a straight line and not Table 3's bow. `--track=1` absorbs it in practice, so
`--skew` is still not passed; the point is that the drift here has a model, and
Table 3's does not.

### The 10 problems it reports, none of them a defect

| | what it is |
|---|---|
| V01 count, V11 bracketless, V02 and V03 leaders | **one root cause** — see below |
| V08 (plate 5, transcription 12), V09 (plate 7, transcription 10) | the plate collapses **`36-43. 8 children deceased`** and **`50-53. 4 children deceased`** onto ONE line each. Both are in `PLATE_NOTES`; the stub count is right and the child count is right |
| V05, V06, V09, V10 leaders, all ~**+175px** against a 147px row | the **four Johnsons**. 8, 10, 15 and 17 carry an English name — `(Hugh Johnson)` — printed on its **own row**, so each wife sits TWO rows under her husband, not one. The audit's expected-leader model assumes one |

**The single root cause behind the first four is V01's top stub.** Its vertical
runs y 716–5995 with children 36 rows apart — 3 at the top, 5 at the bottom —
and the rig starts it at y 845, so the stub at 721 falls outside the right-hand
window. `--overshoot` cannot rescue it: **that flag widens the LEFT side only**,
by design, so the stub is seen as a *leader* at 728 instead. V01 then pairs by
position, takes V11's bracket, and the displacement cascades — V11 is left
bracketless and V03's expected leader is computed off the wrong stub, 1088px
out. This is the README's own warning about positional pairing, reproduced from
a single missing stub.

**V02's remaining leader flag is person 3 being printed twice**, so the expected
row is taken from the lower occurrence and the measurement comes back −6042px.

**So Table 4's 10 are a known-clean baseline, like Table 3's 15.** An 11th
problem, or a change in which V-ids appear, is the signal. Diff the list.

## Traps already paid for

- A rule **drifts in x** down its length — 16px on Table 1 — so a fixed narrow
  window loses it and reports one bracket as four.
- An ink cluster can hold the rule **and the type beside it**; measuring stubs
  from the cluster's edge reads them from inside the numbers and reports **zero
  stubs on a bracket that plainly has five**.
- An x-ink profile cannot separate rule from type: the threshold that isolates
  Table 1's sharp spike swallows type on Table 4's flat hump. The **long
  unbroken run** is what distinguishes a rule.
- The plate's rules are **broken ink**, with a white gap where a leader meets
  its vertical. Requiring an unbroken run finds almost nothing; measure ink
  density across a window instead.
- A vertical can **stop short of its own last stub** (Table 1's 24–27 ends 33px
  above 27's rule), so the stub window has to overshoot the terminus — but by
  well under one row.
- **Near-duplicate detections of one rule are worse than harmless.** They push
  the expected groups out of step with the ink and flag brackets that are fine.
- A run with fewer than two stubs is a brace, a crease or an artifact — never a
  sibling bracket, since a single child is drawn with no vertical at all.

## Validated

Against Genealogy IV with 20 restored to the 6+7 union — the exact state that
shipped until 2026-08-10 — the audit reports:

> generation 3: the plate draws 3 bracket vertical(s) in this column, the
> transcription claims 2 group(s) of 2+ children

and does not report it on the corrected data. That is the defect, named from
the ink.
