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
from plate import Band

bmp = sys.argv[1]
bands = json.loads(sys.argv[2])          # [[x0,x1], ...]
minrun = int(sys.argv[3]) if len(sys.argv) > 3 else 110

found = []
for x0, x1 in bands:
    b = Band(bmp, x0, x1)
    # Each candidate keeps its OWN x window. Pooling the windows of a whole
    # column merges brackets that merely sit at the same x at different y --
    # on Table 1's generation 3 that made one 52px window out of three rules
    # and reported the column empty.
    for cand in b.verticals(minrun):     # candidates: drift already followed
        xl, xr = cand["xl"], cand["xr"]
        if xr - xl > 45:                 # too wide to be one rule
            continue
        for r in b.rules_at(xl, xr, minrun=minrun):
            if r["dens"] < 0.8:          # a column of type, not a rule
                continue
            r["right"] = b.stubs(r, side="right")
            r["left"] = b.stubs(r, side="left")
            found.append(r)

# One rule drifts enough in x to be detected two or three times, each run a
# few px different -- and near-duplicates are worse than harmless: they push
# the expected groups out of step with the ink and flag brackets that are fine.
# Containment is not enough to catch them; cluster on overlap instead.
found.sort(key=lambda r: (-len(r["right"]), -r["len"]))
keep = []
for r in found:
    for k in keep:
        if abs(k["x"] - r["x"]) > 30:
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
