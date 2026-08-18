"""Read a native-resolution band out of a BMP and find bracket verticals + stubs.

Everything here is measurement on the scan at 1:1. Nothing is read from a
downscale, and nothing here decides a genealogy -- it reports what ink is
where, for a human to read against the crop.

Every window in here is a length in pixels, and the plates are not on one
scale: Table 1 sets 146.6px to a row, Table 3 sets 24.7px in a scan a ninth
the pixel count. So the windows are stated as fractions of the ROW PITCH and
multiplied up, rather than retuned by hand per plate. `row` defaults to
Table 1's, where every derived constant is exactly the integer it was written
as, so a Table 1 run is unchanged.
"""
import struct, sys, json

ROW_T1 = 146.6                  # the plate the constants below were tuned on


class Band:
    def __init__(self, path, x0, x1, thresh=170, row=ROW_T1, xmerge=5, skew=0.0):
        self.f = open(path, "rb")
        head = self.f.read(64)
        self.off = struct.unpack_from("<I", head, 10)[0]
        self.w = struct.unpack_from("<i", head, 18)[0]
        h = struct.unpack_from("<i", head, 22)[0]
        self.bpp = struct.unpack_from("<H", head, 28)[0]
        assert self.bpp == 24
        self.flip = h > 0
        self.h = abs(h)
        self.stride = ((self.w * 3 + 3) // 4) * 4
        self.row = float(row)
        self.s = self.row / ROW_T1
        # NOT scaled by the row pitch. A rule's drift in x is the scan's skew,
        # which is an angle: it costs the same pixels on a coarse plate as on a
        # fine one, and on Table 3 it is 16px over the 4183px left-hand rule.
        # Scaling this down to 1px is what splits that rule into four.
        #
        # Widening the tolerance instead is the wrong cure, and Table 3 says why
        # in one measurement: its fold crease runs 15px from the col-6 bracket,
        # closer than that rule's own drift. A flat 20px window swallows the
        # crease into the bracket. So the drift is spent as an ANGLE -- x may
        # move by `skew` per px of y -- and a fragment at nearly the same y gets
        # nearly no allowance at all.
        self.xmerge = xmerge
        self.skew = skew
        self.x0, self.x1 = x0, min(x1, self.w)
        self.bw = self.x1 - self.x0
        self.rows = []                      # bytearray per y, 1 = dark
        for y in range(self.h):
            ry = (self.h - 1 - y) if self.flip else y
            self.f.seek(self.off + ry * self.stride + self.x0 * 3)
            raw = self.f.read(self.bw * 3)
            d = bytearray(self.bw)
            for x in range(self.bw):
                b = raw[3 * x]; g = raw[3 * x + 1]; r = raw[3 * x + 2]
                if (r * 2 + g * 5 + b) >> 3 < thresh:
                    d[x] = 1
            self.rows.append(d)
        self.f.close()

    def n(self, base, floor=1):
        """A Table 1 window, in this plate's pixels. Identity on Table 1."""
        return max(floor, int(round(base * self.s)))

    def columns(self, minink=400):
        """x positions that carry enough ink over the page to be a rule."""
        tot = [0] * self.bw
        for row in self.rows:
            for x in range(self.bw):
                if row[x]:
                    tot[x] += 1
        cols, cur = [], []
        for x in range(self.bw):
            if tot[x] >= minink:
                cur.append(x)
            elif cur:
                cols.append(cur); cur = []
        if cur:
            cols.append(cur)
        # A cluster can span a rule AND the type beside it. Measuring stubs
        # from the edge of such a cluster reads them from inside the numbers,
        # which reports zero stubs on a bracket that plainly has five. Split
        # each cluster at its ink peaks and keep a narrow window on each.
        out, half = [], self.n(4)
        for c in cols:
            peaks, i = [], 0
            while i < len(c):
                j = i
                while j + 1 < len(c) and tot[c[j + 1]] > tot[c[j]] * 0.45:
                    j += 1
                seg = c[i:j + 1]
                best = max(seg, key=lambda x: tot[x])
                if not peaks or best - peaks[-1] > 2 * half:
                    peaks.append(best)
                elif tot[best] > tot[peaks[-1]]:
                    peaks[-1] = best
                i = j + 1
            for p in peaks:
                out.append((self.x0 + max(0, p - half),
                            self.x0 + min(self.bw - 1, p + half), tot[p]))
        return out

    def _trace(self, xl, xr, track, gapmax=1):
        """Follow one rule down the page, letting its window re-centre.

        Table 3's rules do not skew, they BOW: the left-hand rule runs x 683 at
        the top, 686 at y 1000, 666 at y 3600 and 671 at the foot. No fixed
        window holds 20px of that, and no linear skew describes it either --
        widen the window and it takes in the fold crease 15px away. So the
        window moves at most `track` px a row, which a rule can afford and a
        crease 15px off cannot reach.

        Returns (profile, edges), edges giving this rule's own left and right
        in plate coordinates at every y -- which is what the stubs are then
        measured from, rather than from an average the rule has left behind.
        """
        # A 2px window cannot be tracked: the first stub it meets drags it off
        # the rule and it never comes back. Table 3's col-7 bracket is exactly
        # that -- found with the window held still, lost the moment it moves --
        # so give the window room to see the rule shift under it.
        w = max(xr - xl + 1, 2 * int(track) + 3)
        # One column can carry several brackets, and between two of them the
        # window has nothing to follow -- so it holds the x the LAST rule
        # ended at, while the bow has moved the next one. Table 3's col-3
        # bracket for 5+6 sits at x 1215 under a rule that finished at 1208,
        # and is invisible to a 5px window. After a rule ends, the window may
        # therefore jump once to re-acquire. `pad` stays far short of the 535px
        # between columns, so it can only ever find the same column's next rule.
        pad = max(6, w)
        cx = (xl + xr) / 2.0 - self.x0
        prof, edges, miss = [], [], 0
        for y in range(self.h):
            a = max(0, min(self.bw - w, int(round(cx - w / 2.0))))
            seg = self.rows[y][a:a + w]
            ink = [i for i, v in enumerate(seg) if v]
            if not ink and track and miss > gapmax:
                a2 = max(0, min(self.bw - (w + 2 * pad),
                                int(round(cx - w / 2.0 - pad))))
                seg2 = self.rows[y][a2:a2 + w + 2 * pad]
                ink2 = [i for i, v in enumerate(seg2) if v]
                if ink2:
                    cx = a2 + (ink2[0] + ink2[-1]) / 2.0
                    a = max(0, min(self.bw - w, int(round(cx - w / 2.0))))
                    seg = self.rows[y][a:a + w]
                    ink = [i for i, v in enumerate(seg) if v]
            prof.append(bool(ink))
            miss = 0 if ink else miss + 1
            if ink and track:
                want = a + (ink[0] + ink[-1]) / 2.0
                cx += max(-track, min(track, want - cx))
            edges.append((a + self.x0, a + w - 1 + self.x0))
        return prof, edges

    def rules_at(self, xl, xr, minrun=110, gapmax=None, track=0):
        """Runs of ink down one x cluster, tolerating the plate's broken ink.

        gapmax is deliberately small: a 400px bridge fuses two brackets that
        merely share a column, which is exactly the reading error this audit
        exists to catch.

        track=0 holds the window still, which is what Table 1 was read with.
        """
        if gapmax is None:
            gapmax = self.n(30)
        a, b = xl - self.x0, xr - self.x0 + 1
        if track:
            prof, edges = self._trace(xl, xr, track, gapmax)
        else:
            prof = [any(self.rows[y][a:b]) for y in range(self.h)]
            edges = None
        out, y = [], 0
        while y < self.h:
            if prof[y]:
                y0 = y; last = y
                while y < self.h and y - last <= gapmax:
                    if prof[y]:
                        last = y
                    y += 1
                if last - y0 + 1 >= minrun:
                    # a rule is solid; a column of text rows is not, and it
                    # otherwise survives the gap tolerance and reports one
                    # "stub" per line of type
                    dens = sum(prof[y0:last + 1]) / (last - y0 + 1)
                    r = {"x": (xl + xr) / 2, "xl": xl, "xr": xr,
                         "y0": y0, "y1": last, "len": last - y0 + 1,
                         "dens": round(dens, 3)}
                    if edges:
                        mid = (y0 + last) // 2
                        r["x"] = (edges[mid][0] + edges[mid][1]) / 2
                        r["xl"], r["xr"] = edges[y0][0], edges[y0][1]
                        r["edges"] = edges       # dropped before serialising
                    out.append(r)
            else:
                y += 1
        return out

    def verticals(self, minrun):
        runs = []
        for x in range(self.bw):
            y = 0
            while y < self.h:
                if self.rows[y][x]:
                    y0 = y
                    while y < self.h and self.rows[y][x]:
                        y += 1
                    if y - y0 >= minrun:
                        runs.append((x, y0, y - 1))
                else:
                    y += 1
        runs.sort()
        out, used = [], [False] * len(runs)
        for i, (x, a, b) in enumerate(runs):
            if used[i]:
                continue
            used[i] = True
            xs, y0, y1 = [x], a, b
            for j in range(i + 1, len(runs)):
                if used[j]:
                    continue
                x2, c, d2 = runs[j]
                if x2 - max(xs) > 1:
                    continue
                if min(y1, d2) - max(y0, c) > 0.3 * min(y1 - y0, d2 - c):
                    used[j] = True
                    xs.append(x2); y0 = min(y0, c); y1 = max(y1, d2)
            out.append({"x": self.x0 + sum(xs) / len(xs),
                        "xl": self.x0 + min(xs), "xr": self.x0 + max(xs),
                        "y0": y0, "y1": y1, "len": y1 - y0 + 1})
        # a fold crease and JPEG noise break one rule into collinear fragments;
        # merge anything sharing an x within 5px, plus whatever the plate's own
        # skew explains over the y between them
        out.sort(key=lambda r: (r["x"], r["y0"]))
        merged, xmerge = [], self.xmerge
        for r in out:
            rmid = (r["y0"] + r["y1"]) / 2
            for m in merged:
                mmid = (m["y0"] + m["y1"]) / 2
                pred = m["x"] + self.skew * (rmid - mmid)
                if abs(pred - r["x"]) <= xmerge:
                    m["xl"] = min(m["xl"], r["xl"]); m["xr"] = max(m["xr"], r["xr"])
                    m["y0"] = min(m["y0"], r["y0"]); m["y1"] = max(m["y1"], r["y1"])
                    m["len"] = m["y1"] - m["y0"] + 1
                    m["parts"] += 1
                    break
            else:
                r["parts"] = 1
                merged.append(dict(r))
        merged.sort(key=lambda r: (r["y0"], r["x"]))
        return merged

    def stubs(self, rule, reach=None, gap=None, side="right", density=0.55,
              skip=None, overshoot=None):
        """Rows carrying a horizontal rule running away from the vertical.

        Not a contiguity test: the plate's rules are broken ink, and there is a
        clear white gap where a leader meets its vertical, so requiring an
        unbroken run finds almost nothing. Measure ink DENSITY across a window
        set `skip` px clear of the vertical instead.
        """
        reach = self.n(110) if reach is None else reach
        gap = self.n(6) if gap is None else gap
        skip = self.n(3) if skip is None else skip
        overshoot = self.n(45) if overshoot is None else overshoot
        hits = []
        # A vertical can stop short of its own last stub -- Table 1's 24-27
        # ends 33px above 27's rule -- so the window has to overshoot the
        # terminus. Keep it well under one row (146.6px on Table 1) or the
        # search reaches into the next group.
        for y in range(max(0, rule["y0"] - overshoot),
                       min(self.h, rule["y1"] + overshoot + 1)):
            row = self.rows[y]
            edges = rule.get("edges")
            xl = edges[y][0] if edges else rule["xl"]
            xr = edges[y][1] if edges else rule["xr"]
            if side == "right":
                a = xr - self.x0 + skip
                b = min(self.bw, a + reach)
            else:
                b = xl - self.x0 - skip
                a = max(0, b - reach)
            if b - a < reach * 0.6:
                continue
            ink = sum(row[a:b])
            if ink >= density * (b - a):
                hits.append(y)
        # collapse consecutive rows into one stub
        groups = []
        for y in hits:
            if groups and y - groups[-1][-1] <= gap:
                groups[-1].append(y)
            else:
                groups.append([y])
        return [{"y": sum(g) / len(g), "thick": len(g)} for g in groups]


if __name__ == "__main__":
    path, x0, x1, minrun = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    row = float(sys.argv[5]) if len(sys.argv) > 5 else ROW_T1
    band = Band(path, x0, x1, row=row)
    rules = [r for r in band.verticals(minrun)]
    out = []
    for r in rules:
        r["right"] = band.stubs(r, side="right")
        r["left"] = band.stubs(r, side="left")
        out.append(r)
    print(json.dumps(out, indent=None))
    for r in out:
        print(f"x={r['x']:8.1f} y {r['y0']:6d}-{r['y1']:6d} len {r['len']:5d} "
              f"| right stubs {len(r['right']):2d} at "
              + ",".join(f"{s['y']:.0f}" for s in r["right"])
              + f" | left {len(r['left'])} at "
              + ",".join(f"{s['y']:.0f}" for s in r["left"]), file=sys.stderr)
