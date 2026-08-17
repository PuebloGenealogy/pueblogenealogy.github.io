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

`crop.py` cuts an exact native-resolution PNG for a human to read:

```bash
python3 scripts/plate_audit/crop.py /tmp/t1.bmp 9541 1090 2300 4710 out.png
```

## Calibration is per plate, and skipping it produces confident nonsense

**Parameters tuned on one plate do not transfer.** Table 1 and Table 4 have
different paper, ink weight and scan scale, and the same settings that read
Table 1 cleanly fragment Table 4's stubs.

The cheap test is the **stub-to-stub gap distribution**, which on a correctly
calibrated plate is sharply bimodal — one row and two rows, nothing else:

| plate | gaps |
|---|---|
| Table 1, calibrated | 146 × 62, 292 × 5 |
| Table 4, **not** calibrated | 22, 23, 24, 25, 26, 27, 28, 30, 33, 35, 37, 39 … |

Table 4's spray of small gaps corrupts the measured row pitch, which then
flags leaders that are fine — eight of them, four at a constant ~+176px against
a nominal 146px row. **Those were artifacts of the rig, not findings about the
plate.** Check the distribution before believing a single flag.

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
