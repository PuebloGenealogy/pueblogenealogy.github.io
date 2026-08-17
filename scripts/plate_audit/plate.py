"""Read a native-resolution band out of a BMP and find bracket verticals + stubs.

Everything here is measurement on the scan at 1:1. Nothing is read from a
downscale, and nothing here decides a genealogy -- it reports what ink is
where, for a human to read against the crop.
"""
import struct, sys, json


class Band:
    def __init__(self, path, x0, x1, thresh=170):
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
        out, half = [], 4
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

    def rules_at(self, xl, xr, minrun=110, gapmax=30):
        """Runs of ink down one x cluster, tolerating the plate's broken ink.

        gapmax is deliberately small: a 400px bridge fuses two brackets that
        merely share a column, which is exactly the reading error this audit
        exists to catch.
        """
        a, b = xl - self.x0, xr - self.x0 + 1
        prof = [any(self.rows[y][a:b]) for y in range(self.h)]
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
                    out.append({"x": (xl + xr) / 2, "xl": xl, "xr": xr,
                                "y0": y0, "y1": last, "len": last - y0 + 1,
                                "dens": round(dens, 3)})
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
        # merge anything sharing an x within 5px and separated by < 400px
        out.sort(key=lambda r: (r["x"], r["y0"]))
        merged = []
        for r in out:
            for m in merged:
                if abs(m["x"] - r["x"]) <= 5:
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

    def stubs(self, rule, reach=110, gap=6, side="right", density=0.55, skip=3,
              overshoot=45):
        """Rows carrying a horizontal rule running away from the vertical.

        Not a contiguity test: the plate's rules are broken ink, and there is a
        clear white gap where a leader meets its vertical, so requiring an
        unbroken run finds almost nothing. Measure ink DENSITY across a window
        set `skip` px clear of the vertical instead.
        """
        hits = []
        # A vertical can stop short of its own last stub -- Table 1's 24-27
        # ends 33px above 27's rule -- so the window has to overshoot the
        # terminus. Keep it well under one row (146.6px on Table 1) or the
        # search reaches into the next group.
        for y in range(max(0, rule["y0"] - overshoot),
                       min(self.h, rule["y1"] + overshoot + 1)):
            row = self.rows[y]
            if side == "right":
                a = rule["xr"] - self.x0 + skip
                b = min(self.bw, a + reach)
            else:
                b = rule["xl"] - self.x0 - skip
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
    band = Band(path, x0, x1)
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
