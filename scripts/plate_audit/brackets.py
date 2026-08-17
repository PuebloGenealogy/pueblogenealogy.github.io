"""Inventory every bracket on a plate: its vertical, its child stubs, and the
leader(s) entering it.

The count of leaders entering a vertical is the diagnostic the handoff names --
one leader means one group however many '+' lines sit above it. This reports
the ink; it does not decide the genealogy.

Two things this went wrong on first, both worth keeping in the code:

  * A rule DRIFTS in x down its length -- 16px of travel on Table 1 -- so a
    fixed narrow window loses half of it and reports one bracket as four. The
    candidate pass merges adjacent columns to follow the drift.
  * An ink cluster can hold the rule AND the type beside it. Measuring stubs
    from the cluster's edge then reads them from inside the numbers and reports
    ZERO stubs on a bracket that plainly has five. Stubs are measured from the
    candidate's own edges, never a cluster's.

An x-ink profile cannot tell the two apart: the same threshold that isolates
Table 1's sharp spike swallows type on Table 4's flat one. The long unbroken
run is the thing that distinguishes a rule, so that is what is detected.
"""
import sys, json
from plate import Band, ROW_T1

# --row=N states this plate's row pitch, which is what every window in plate.py
# is a fraction of. Table 3 sets 24.7px to a row against Table 1's 146.6, so
# leaving it at the default reads Table 3 with windows six times too wide.
FLAGS = ("--row=", "--xmerge=", "--maxwidth=", "--skew=", "--track=",
         "--maxthick=", "--ongrid=", "--gapmax=")
argv = [a for a in sys.argv if not a.startswith(FLAGS)]


def flag(name, default):
    return next((float(a.split("=")[1]) for a in sys.argv
                 if a.startswith(name)), default)


ROW = flag("--row=", ROW_T1)
# --xmerge / --maxwidth are the drift budget, in PIXELS and deliberately not
# scaled: see Band.xmerge. Table 3 wants 20 and 24 against Table 1's 5 and 45.
XMERGE = int(flag("--xmerge=", 5))
MAXWIDTH = int(flag("--maxwidth=", 45))
SKEW = flag("--skew=", 0.0)              # px of x per px of y; Table 3 is 0.004
# --track lets a rule's window re-centre as it descends, at most N px a row.
# 0 is Table 1's fixed window. Table 3 bows 20px and needs 1.
TRACK = flag("--track=", 0.0)
# --maxthick drops a "stub" too deep to be a rule. Table 3's fold crease runs
# 10px from the col-6 brackets, so no x window separates them -- but the crease
# answers the density test in blots 15 to 94 rows deep, where a stub is 2 to 4.
# Every one of that plate's 39 sub-row stub gaps is a crease blot. 0 is off.
MAXTHICK = int(flag("--maxthick=", 0))
# --ongrid=TOL keeps only runs whose stubs all sit a whole number of rows
# apart, to within TOL of a row. The plate sets every child on the same grid,
# so a real bracket cannot fail this; a crease answers the density test at
# whatever y its blots happen to fall. It is the ONLY thing that separates
# Table 3's column 6 from the crease 10px away, since no x window does.
# Rejection is per RUN, not per stub -- dropping the odd stub would let a
# blot be dressed up as a bracket, whereas dropping the run shows up in the
# audit as a count the transcription disagrees with, which is loud. 0 is off.
ONGRID = flag("--ongrid=", 0.0)
# --gapmax is the ink break a rule may carry without being read as two rules.
# Row-scaled it comes to 5px on Table 3, and that plate's breaks are 7 -- so
# W46's nine children came back as three brackets of 5, 2 and 4. It stays far
# under one row (10px against 24.75), so it still cannot fuse two brackets
# that are rows apart, which is the reading error the small value protects.
GAPMAX = int(flag("--gapmax=", 0)) or None

bmp = argv[1]
bands = json.loads(argv[2])              # [[x0,x1], ...]
minrun = int(argv[3]) if len(argv) > 3 else 110

found = []
for x0, x1 in bands:
    b = Band(bmp, x0, x1, row=ROW, xmerge=XMERGE, skew=SKEW)
    # Each candidate keeps its OWN x window. Pooling the windows of a whole
    # column merges brackets that merely sit at the same x at different y --
    # on Table 1's generation 3 that made one 52px window out of three rules
    # and reported the column empty.
    for cand in b.verticals(minrun):     # candidates: drift already followed
        xl, xr = cand["xl"], cand["xr"]
        if xr - xl > MAXWIDTH:           # too wide to be one rule
            continue
        for r in b.rules_at(xl, xr, minrun=minrun, track=TRACK, gapmax=GAPMAX):
            if r["dens"] < 0.8:          # a column of type, not a rule
                continue
            r["right"] = b.stubs(r, side="right")
            r["left"] = b.stubs(r, side="left")
            if MAXTHICK:
                r["right"] = [s for s in r["right"] if s["thick"] <= MAXTHICK]
                r["left"] = [s for s in r["left"] if s["thick"] <= MAXTHICK]
            r.pop("edges", None)         # per-row, and far too big to serialise
            if ONGRID:
                ys = [s["y"] for s in r["right"]]
                gaps = [b - a for a, b in zip(ys, ys[1:])]
                # The grid test is applied only to SHORT gaps. A row pitch is
                # never exact, so the error accumulates: at 24.70px against a
                # true 24.75, a legitimate 33-row gap lands 0.6 of a row off
                # grid and the run is thrown away -- which is what happened to
                # W04's bracket, one of the two this filter first "lost".
                # Nothing is given up by the narrowing, because the junk this
                # exists to reject is sub-row in the first place.
                if any(g < ROW * 0.75 or (g < ROW * 6.5 and
                       abs(g / ROW - round(g / ROW)) > ONGRID) for g in gaps):
                    continue
            found.append(r)

# One rule drifts enough in x to be detected two or three times, each run a
# few px different -- and near-duplicates are worse than harmless: they push
# the expected groups out of step with the ink and flag brackets that are fine.
# Containment is not enough to catch them; cluster on overlap instead.
found.sort(key=lambda r: (-len(r["right"]), -r["len"]))
keep, xnear = [], max(1, int(round(30 * ROW / ROW_T1)))
for r in found:
    for k in keep:
        if abs(k["x"] - r["x"]) > xnear:
            continue
        lo, hi = max(k["y0"], r["y0"]), min(k["y1"], r["y1"])
        if hi - lo > 0.5 * min(k["len"], r["len"]):
            break
    else:
        keep.append(r)

keep.sort(key=lambda r: (r["y0"], r["x"]))
for r in keep:
    print(f"x {r['x']:8.1f}  y {r['y0']:6d}-{r['y1']:6d}  len {r['len']:5d}  "
          f"stubs {len(r['right']):2d} [" + ",".join(f"{s['y']:.0f}" for s in r["right"])
          + f"]  leaders {len(r['left'])} [" + ",".join(f"{s['y']:.0f}" for s in r["left"]) + "]",
          file=sys.stderr)
print(json.dumps(keep))
