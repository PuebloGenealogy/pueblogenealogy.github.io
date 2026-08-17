"""Hold a plate's transcription against the ink on its scan.

Usage: audit.py <transcription module> <brackets.json> <cols> [xtol] [variant.json]
   e.g. audit.py transcription.py t1_brackets.json 2:3499,3:6643,4:9801,5:12954 80

This is the check the DOM audit structurally cannot do. That one derives the
expected leader from `_GROUPS` and measures the rendered page, so it proves
data and rendering agree; it is silent when both agree with each other and
disagree with Parsons. Here the reference is the scan.

What it can decide
  * how many children the plate brackets in each group
  * how many bracket verticals a column carries at all -- the check that
    catches a group split in two that the plate draws as one
  * which row each bracket's leader hangs off

What it cannot decide
  * the NUMBER printed against each stub. Nothing here reads type, so a group
    of the right size whose members are misnumbered passes. Crops are for that.
"""
import json, os, sys, importlib.util, statistics

ROW_T1 = 146.6
# --row=N, as in brackets.py: the tolerance that decides whether a leader meets
# a stub is a fraction of a row, and Table 3's row is a sixth of Table 1's.
ROW_HINT = next((float(a.split("=")[1]) for a in sys.argv if a.startswith("--row=")),
                ROW_T1)
# A leader and the stub it meets are the same rule, so the gap between the two
# measured centres is ink thickness and centroid noise -- a few px whatever the
# plate's scale. Row-scaled alone this comes to 2px on Table 3, tighter than
# the 4px its leaders actually sit at, and then NOTHING matches: every bracket
# reports no leader and the check that finds a bracket on the wrong row goes
# quietly dead. Hence the floor.
YMATCH = max(5, int(round(12 * ROW_HINT / ROW_T1)))
sys.argv = [a for a in sys.argv if not a.startswith("--row=")]

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
mod_name = sys.argv[1]
spec = importlib.util.spec_from_file_location("t", f"{REPO}/scripts/{mod_name}")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)

GEN = {p[0]: p[1] for p in T.PERSONS}
UNION = {u[0]: u for u in T.UNIONS}
ON_SPOUSE = set(getattr(T, "LEADER_ON_SPOUSE_ROW", ()) or ())

groups = list(T._GROUPS)
VARIANT = sys.argv[5] if len(sys.argv) > 5 else None   # a deliberately-wrong
#                                    variant, to prove the audit actually fires

runs = json.load(open(sys.argv[2]))
if len(sys.argv) > 5:
    groups = [tuple(g) for g in json.load(open(sys.argv[5]))]

# ---- which column is which generation --------------------------------------
# Passed in, not inferred. Auto-clustering the detected x values looks tidy and
# is not safe: on Table 1 it returns the fold crease and a column of type among
# the real columns, and silently assigns generation 5 to the crease. The
# columns are a measurement -- take them from `brackets.py` output by eye once
# per plate. XTOL also does the filtering that drops crease and type.
COLS = {int(k): float(v) for k, v in
        (p.split(":") for p in sys.argv[3].split(","))}
XTOL = float(sys.argv[4]) if len(sys.argv) > 4 else 80.0

runs = [r for r in runs if any(abs(r["x"] - c) < XTOL for c in COLS.values())]
for r in runs:
    r["gen"] = min(COLS, key=lambda g: abs(COLS[g] - r["x"]))

bycol = {}
for g in groups:
    bycol.setdefault(GEN[g[3][0]], []).append(g)
gens = sorted(bycol)
colof = COLS

# ---- row pitch, measured off the plate itself ------------------------------
# Measured before the matching, because the matching needs it: a mother with no
# stub of her own is placed one row under her partner.
gaps = []
for r in runs:
    ys = [s["y"] for s in r["right"]]
    gaps += [b - a for a, b in zip(ys, ys[1:])]
# One row, not two: a '+' line between siblings makes some gaps a double.
# Take the smallest real gap and keep everything within a quarter of it.
real = [g for g in gaps if g > 0.5 * ROW_HINT]
base = min(real) if real else 0
ROW = statistics.median([g for g in real if g < base * 1.25]) if real else 0
YTOL = ROW * 0.3

rows = {}


def mother_row(uid, mother):
    if mother in rows:
        return rows[mother], "own stub"
    u = UNION.get(uid)
    if u:
        partner = u[2] if u[1] == mother else u[1]
        if partner in rows:
            return rows[partner] + ROW, f"one row under {partner}"
    return None, "founding couple - no reference on the plate"


def anchor_of(g):
    """The row the plate hangs this group's bracket off, if it is known yet."""
    uid, mother, father, kids = g
    a = mother
    if uid in ON_SPOUSE:
        u = UNION[uid]
        a = u[2] if u[1] == mother else u[1]
    return mother_row(uid, a)[0], a


# ---- match ink to expected groups ------------------------------------------
report, problems = [], []
for gen in gens:
    # A sibling bracket carries at least two stubs -- a single child is drawn
    # with no vertical at all. Anything shorter is a brace, a crease or an
    # artifact, and admitting one shifts every later group onto the wrong ink.
    ink = sorted((r for r in runs if r["gen"] == gen and len(r["right"]) >= 2),
                 key=lambda r: r["y0"])
    slots = []
    for r in ink:
        leaders = [l for l in r["left"]
                   if any(abs(l["y"] - s["y"]) < YMATCH for s in r["right"])]
        # Two groups abutting is a real thing and this splits the vertical
        # between them -- but only on evidence that survives a coarse plate.
        # Two groups cannot begin on the same row, so leaders closer together
        # than a row are one leader measured twice, or crease noise; and a
        # split that leaves a piece with fewer than two stubs has invented a
        # bracket, since a single child is drawn with no vertical at all.
        cuts = []
        for y in sorted(l["y"] for l in leaders):
            if not cuts or y - cuts[-1] >= ROW * 0.75:
                cuts.append(y)
        pieces = []
        for i, c in enumerate(cuts):
            hi = cuts[i + 1] if i + 1 < len(cuts) else 10 ** 9
            pieces.append((r, [s for s in r["right"]
                               if c - YMATCH <= s["y"] < hi - YMATCH],
                           [l for l in leaders if abs(l["y"] - c) < 1]))
        if len(cuts) <= 1 or any(len(p[1]) < 2 for p in pieces):
            slots.append((r, r["right"], leaders[:1]))
        else:
            slots += pieces
    multi = [g for g in bycol[gen] if len(g[3]) > 1]
    singles = [g for g in bycol[gen] if len(g[3]) == 1]

    # Put the expected groups in the order the PLATE sets them -- by the row
    # each one's mother stands on -- rather than the order `_GROUPS` happens to
    # list them in. Ink is already sorted by y, and pairing the two lists by
    # position silently mispairs every group after the first that disagrees:
    # Genealogy III's column 5 read "W23: plate 5, transcription 2" beside
    # "W24: plate 2, transcription 5", which is one swap wearing the costume of
    # two count errors.
    #
    # This orders by the mother's row; it does NOT match a bracket to whichever
    # leader is nearest, which would be circular -- the leader check exists to
    # find a bracket hanging off the wrong row, and a matcher free to choose
    # its partner would simply choose the row it landed on and report 0. The
    # mother's own row is measured from her stub in the PARENT bracket, which
    # is a different piece of ink from the leader being tested. A bracket out
    # by a row still sorts into the same place, because rows are 25px and
    # groups are hundreds apart.
    # Only the groups whose anchor is known are reordered, and they are sorted
    # among THEIR OWN positions -- the rest stay exactly where they were. An
    # all-or-nothing guard is no use here: a mother who is nobody's bracketed
    # child has no stub to stand on (III's 40 is one), and one unknown anchor
    # would leave the whole column in file order.
    known = [i for i, g in enumerate(multi) if anchor_of(g)[0] is not None]
    if known:
        placed = sorted((multi[i] for i in known),
                        key=lambda g: anchor_of(g)[0])
        for slot, g in zip(known, placed):
            multi[slot] = g

    if len(slots) != len(multi):
        problems.append(f"generation {gen}: the plate draws {len(slots)} bracket "
                        f"vertical(s) in this column, the transcription claims "
                        f"{len(multi)} group(s) of 2+ children "
                        f"({[g[0] or '(none)' for g in multi]})")
    for g, (r, stubs, leaders) in zip(multi, slots):
        uid, mother, father, kids = g
        for kid, s in zip(kids, stubs):
            rows[kid] = s["y"]
        report.append({"uid": uid or "(none)", "mother": mother, "kids": kids,
                       "nstub": len(stubs), "x": r["x"],
                       "leader": leaders[0]["y"] if leaders else None})
        if len(stubs) != len(kids):
            problems.append(f"{uid or '(none)'}: the plate brackets {len(stubs)} "
                            f"children, the transcription lists {len(kids)} {kids}")
    for g in singles:
        report.append({"uid": g[0] or "(none)", "mother": g[1], "kids": g[3],
                       "nstub": None, "x": colof.get(gen, 0), "leader": None})

print(f"row pitch measured at {ROW:.1f}px; a leader is flagged past {YTOL:.0f}px\n")
print(f"{'group':>7} {'mother':>6} {'children':<30} {'stubs':>5} "
      f"{'leader y':>9} {'expected':>9} {'diff':>7}")
for e in report:
    if e["nstub"] is None:
        print(f"{e['uid']:>7} {e['mother']:>6} {str(e['kids']):<30} "
              f"{'-':>5}   single child, no vertical")
        continue
    anchor = e["mother"]
    if e["uid"] in ON_SPOUSE:
        u = UNION[e["uid"]]
        anchor = u[2] if u[1] == e["mother"] else u[1]
    exp, how = mother_row(e["uid"], anchor)
    if e["uid"] in ON_SPOUSE:
        how += " (LEADER_ON_SPOUSE_ROW)"
    diff = None if exp is None or e["leader"] is None else e["leader"] - exp
    if diff is None:
        print(f"{e['uid']:>7} {e['mother']:>6} {str(e['kids']):<30} {e['nstub']:>5} "
              f"{e['leader'] or 0:>9.0f} {'-':>9} {'-':>7}   ({how})")
        continue
    flag = "" if abs(diff) <= YTOL else "  <-- CHECK"
    print(f"{e['uid']:>7} {e['mother']:>6} {str(e['kids']):<30} {e['nstub']:>5} "
          f"{e['leader']:>9.0f} {exp:>9.0f} {diff:>7.0f}{flag}   ({how})")
    if flag:
        problems.append(f"{e['uid']}: leader sits {diff:+.0f}px from {anchor}'s line "
                        f"({ROW:.0f}px to a row) -- bracket may hang off the wrong person")

print(f"\n{len(report)} groups, {sum(1 for e in report if e['nstub'])} with a bracket "
      f"vertical, {sum(e['nstub'] or 0 for e in report)} stubs measured")
if problems:
    print("\nPROBLEMS")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("No disagreement between the plate's ink and the transcription's structure.")
