---
paths:
  - "scripts/plate_audit/**"
---

# Plate-audit rig — calibration and known-clean baselines

This loads automatically because you're touching `scripts/plate_audit/`. It
covers the tool itself: what it measures, how it's calibrated per plate, and
which flagged "problems" are already explained. General DOM/measurement
gotchas that aren't specific to this rig live in `memory/measurement-gotchas.md`
(always loaded).

## What the rig is, and its limits

**`scripts/plate_audit/` measures the PLATE, not the rendered page** — bracket
verticals, stubs entering from the right, leaders entering from the left, read
at 1:1 off a raw BMP and held against `_GROUPS`. That's the one reference the
DOM audit (`memory/measurement-gotchas.md`) can't have: it decides child counts
per group, how many verticals a column carries, and which row each leader
hangs off. **It cannot read type** — a group of the right size whose members
are misnumbered passes silently, so a human still reads the crops. Read
`README.md` in this directory before trusting a number from it: **parameters
are per-plate and do not transfer**. Calibration target: stub-to-stub gaps
should hold nothing below one row (Table 1: 144–148 × 65, 290–292 × 5; Table 3:
24–26 × 43, 49–51 × 19) rather than spraying sub-row; an uncalibrated run
produces confident flags that are the rig's own noise.

**The audit pairs a bracket to the group whose MOTHER stands on its leader —
deliberate, even though it makes the leader test tautological.** Pairing by
`_GROUPS` order instead is what hid Genealogy III block 2's two real errors:
one displacement mispairs everything after it, so mismatches read as noise
("W23: plate 5, transcription 2" beside "W24: plate 2, transcription 5") and
get dismissed. Identity pairing buys three tests with teeth: mismatched child
counts (what actually found block 2's errors), a bracket no group claims, and
a group with no bracket. A pairing that falls back to position **says so in
the output** — treat those as guesses.

**A bracketless group is bounded by its LEADER-matched neighbours, never the
positional ones.** Within a column and descent block, bracket y rises with the
lowest child id — check that holds on the leader-matched brackets before
relying on it (it holds on every column/block of Table 2 but one). Feeding
positional pairings into this instead collapses it (that's what put U46's
bracket 2000px into the wrong descent block).

**A mother with no stub of her own can't be anchored, and a LATER WIFE is the
case that bites.** The plate sets a second wife below the whole of her
husband's earlier issue (not one row under him) — placing her one row under
puts her on the first wife's row, stealing that bracket and passing no rows to
her own children (one wrong offset once cost eight of nine flags on Genealogy
III). `UNIONS`'s fifth field, the husband's marriage number, settles it.

## Per-plate calibration — known-clean baselines, diff the list, don't re-read it fresh

**Table 1 and Table 3**: calibrated, their problem counts (Table 3: 15) fully
explained and stable. Table 3's calibration rests on two things the rig can't
be told generically: it **bows** rather than skews (its left rule runs
x 683, 686, 666, 671 down its length — no straight line or fixed window
follows it), and a **fold crease crosses a bracket column** — the third rule
runs 10px from column 6's brackets, so no x window separates them and
`--maxthick`/`--ongrid` do that job instead, on the grounds that a crease
blots 15–94 rows deep where a real stub is 2–4. Table 3's columns are also
not necessarily a grid: column 6 carries brackets at both x 2786 and x 2854,
both real, each 61–63px left of its own children. Block 1 of Table 3 is 4300
of the plate's 5503px, and column 6's six groups sit entirely under the fold
crease the rig is blind to — the rig produced no new finding there, which is
not the same as "correct"; those six groups were only confirmed by an actual
human read, 2026-08-17.

**Table 4**: calibrated 2026-08-18 (`--row=145.8`, close to Table 1's 146.6 —
row pitch is rarely the actual problem). Two *separate*, opposite band-width
failures were involved, not one: (1) too **wide** a band reads the plate's
own printed verticals as brackets unless narrowed; (2) too **narrow** a band
cost `V05` all five of its stubs — one 230px-band miss looked exactly like
ink fragmentation. A band must hold the rule plus the full 110px stub reach
on *both* sides; `--overshoot` only widens the left side, so it can't rescue
a stub sitting above a rule's detected top — `V01`, whose vertical runs
y 716–5995 with its two children 36 rows apart; the rig starts it at 845 and
misreads the top stub as a leader, and the miscount cascades into `V11` and
`V03` (four of ten problems from one missing stub). Table 4 **skews** (x 3195
at y 722 to x 3132 at y 5800, near-constant at −0.012 px per px of y — a
plate `--skew`'s linear model actually describes, though `--track=1`
absorbs it and the flag still isn't passed) where Table 3 **bows**. The four
"leader +175px" flags are the four Johnson entries — persons **8, 10, 15 and
17** — each an English name printed on its own row, so the wife sits two
rows under her husband, not one. The remaining two of ten: the plate itself
collapsing "36-43. 8 children deceased" and "50-53. 4 children deceased"
onto one line each, both already in `PLATE_NOTES`. All ten of Table 4's
flags are explained (4 Johnson + 4 V01-cascade + 2 count-collapse); **do not
re-derive `--row`**.

**Table 2**: calibrated 2026-08-23 (`--thresh=140`, per-block `--yband`,
`--row=52`, `--track=1`, `--xmerge=15`, `--maxthick=8`, `minrun=40`,
`--gapmax=30` for block 2 only; `--xrefrow` added for this plate). Three flags
were added for this plate, all defaulting to the previous behaviour
(`--thresh`, `--yband`, `--xnear`), plus `audit.py`'s `--xrefrow`. Its 23
flagged problems are now a **baseline, not a fresh list** — every one is
explained in `TABLE2-BENCH.md`; diff against it, don't re-read the plate.
`--ongrid` is **the wrong tool for this plate and that's settled** — tested at
0.25, 0.35 and 0.45 against that baseline on 2026-08-23. It assumes one row
pitch and this plate has two: its runs of undifferentiated siblings sit
**42–50px** apart against a **51.5px** row, so many real stubs are
**1.58–1.60 rows** from their neighbour, **0.42** off-grid at best. The
falling problem count is the trap — **23 → 21 → 18**, every one of them
silence bought by **deleting ink**: at 0.25 it drops **four runs and 22
stubs** including a confirmed nine-stub bracket, and at 0.45 **nine more
stubs** with three groups' brackets. It rejects per **run**, never per stub.
And it never does the job anyway: the crease stub it was meant to catch sits
at the same 1.58-row offset as the real second-pitch stubs, so below 0.42 it
rejects both and above 0.42 it accepts both. **Table 3's output is
byte-identical across the change, which is the regression test to re-run if
any is touched.**

**The bracket bench** (`TABLE2-BENCH.md`) is a published deliverable, not a
source — its generator lived in a session scratchpad and no longer exists, so
if it's ever rebuilt, put the generator in the repo this time. Its 52 cards
were never individually ticked; the verdicts come from reading directly off
the scan.

**`stubs.py`** (twenty lines, rebuild rather than hunt for it) stacks the
~46px band around each of a bracket's stub rows into one image — a nine-child
group becomes one picture instead of nine. Identify each group from the
numbers printed against its stubs, never from the rig's own pairing.

**Genealogy II — all 52 groups, 2026-08-23: no correction owed.** See
`TABLE2-BENCH.md` for the full verdict record before treating any of its
flagged 23 as a live issue.
