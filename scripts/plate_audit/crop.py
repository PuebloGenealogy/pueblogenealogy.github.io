"""Exact native-resolution crop out of the plate BMP, written as PNG.

Usage: crop.py <bmp> <x0> <y0> <w> <h> <out.png> [scale]

scale is an integer nearest-neighbour magnification: it duplicates pixels and
invents nothing. Past ~5-8x on a coarse plate the mark is a blob either way --
see CLAUDE.md on the magnification floor -- so this is for reading rules and
stubs, which are many pixels wide, not for adjudicating a diacritic.
"""
import struct, sys, zlib


def read_band(path, x0, y0, w, h):
    f = open(path, "rb")
    head = f.read(64)
    off = struct.unpack_from("<I", head, 10)[0]
    W = struct.unpack_from("<i", head, 18)[0]
    H = struct.unpack_from("<i", head, 22)[0]
    flip = H > 0
    H = abs(H)
    stride = ((W * 3 + 3) // 4) * 4
    x1 = min(x0 + w, W); y1 = min(y0 + h, H)
    rows = []
    for y in range(y0, y1):
        ry = (H - 1 - y) if flip else y
        f.seek(off + ry * stride + x0 * 3)
        raw = f.read((x1 - x0) * 3)
        rows.append(raw)
    f.close()
    return rows, x1 - x0, y1 - y0


def write_png(path, rows, w, h, scale=1):
    out = bytearray()
    for row in rows:
        # BMP is BGR; PNG wants RGB
        rgb = bytearray(w * 3)
        for x in range(w):
            rgb[3 * x] = row[3 * x + 2]
            rgb[3 * x + 1] = row[3 * x + 1]
            rgb[3 * x + 2] = row[3 * x]
        if scale > 1:
            big = bytearray(w * 3 * scale)
            for x in range(w):
                px = rgb[3 * x:3 * x + 3]
                for k in range(scale):
                    big[3 * (x * scale + k):3 * (x * scale + k) + 3] = px
            rgb = big
        for _ in range(scale):
            out += b"\x00" + rgb

    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", w * scale, h * scale, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(out), 6))
    png += chunk(b"IEND", b"")
    open(path, "wb").write(png)


if __name__ == "__main__":
    bmp, x0, y0, w, h, out = (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]),
                              int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
    scale = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    rows, rw, rh = read_band(bmp, x0, y0, w, h)
    write_png(out, rows, rw, rh, scale)
    print(f"{out}  {rw}x{rh} native at ({x0},{y0}) scale {scale}")
