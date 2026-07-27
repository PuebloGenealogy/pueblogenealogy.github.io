"""
Regenerate the genealogy chart.

    python3 scripts/make_chart.py            private build -> build/
    python3 scripts/make_chart.py --public   published build -> docs/

TWO SOURCES, TWO DESTINATIONS. The private build reads the workbook, including
anything typed into the green english_name / census_name columns, and lands in
build/, which is git-ignored. The public build reads scripts/transcription.py --
the 1923 baseline, which has no research columns to begin with -- and lands in
docs/, which is what GitHub Pages serves.

That is the privacy boundary, and it is structural rather than a matter of
remembering to strip columns: there is no code path from the workbook to docs/.
The two builds share the same Chart class and the same person_line(), because
in baseline mode the research keys are simply empty strings, so the chips that
render them never appear. See the README.
"""

import argparse
import base64
import datetime as dt
import html
import importlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
XLSX = ROOT / "data" / "parsons_genealogy_I.xlsx"

# The workbook holds research columns (english_name, census_name) that are NOT
# for publication, so this build lands in build/ -- which is git-ignored -- and
# never in docs/. Nothing under build/ reaches the internet.
OUT = ROOT / "build" / "genealogy-i-private.html"

DOCS = ROOT / "docs"
FONT_DIR = ROOT / "vendor" / "gentium"

# One entry per transcribed plate. Adding a table is an entry here plus its
# transcription module -- nothing else in this file should need editing, which
# is the point: Table 1's numbering must not leak into the renderer.
TABLES = {
    "i": {
        "numeral": "I",
        "plate": "Table 1",
        "module": "transcription",
        "roots": [1, 54],          # the founding women, in plate order
        "slug": "genealogy-i",
        "couples": "1+2 and 54+55",
        "notes": """
    <li>Person 8 (Yu&#729;si) appears twice on the plate &mdash; as husband in the upper half
        and as a son of 58+59 in the lower half. Here he is drawn once, in the lower half,
        with a cross-reference standing in for the repeated sibling group.</li>
    <li>The &lsquo;+&rsquo; line under 76 is numbered 68 on the plate but names
        Shuwai&#700;&#7590;ri, Turkey &mdash; person 67. Drawn as 67; the misprint is
        recorded on union U23.</li>
""",
    },
    "iv": {
        "numeral": "IV",
        "plate": "Table 4",
        "module": "transcription_iv",
        "roots": [1, 59],          # the founding women, in plate order
        "slug": "genealogy-iv",
        "couples": "1+2 and 59+60",
        "notes": """
    <li>Persons 3 and 4 appear twice on the plate. Person 4 links the two families:
        husband of 3 in the upper half, son of 59+60 in the lower. They are drawn once,
        with &ldquo;For descendants, see above&rdquo; standing in for the repeat, as the
        plate has it.</li>
    <li>Two sibling groups are printed collectively &mdash; &ldquo;36-43. 8 children
        deceased&rdquo; and &ldquo;50-53. 4 children deceased&rdquo;. The plate assigns
        each of them a number, so each is drawn, with the collective setting recorded
        in the data.</li>
    <li>The English names in parentheses &mdash; Hugh, Frank, Paul and Joe Johnson,
        and Mana &mdash; are printed on the plate. They are part of the transcription,
        not additions to it.</li>
    <li>Persons 19 and 20 are printed with no sex, and person 73 with no father: the
        plate records neither, so neither is supplied.</li>
""",
    },
}

# Plates referenced by a transcribed table but not yet transcribed themselves.
# They appear on the landing page as inert cards so the edition states its own
# scope rather than implying Genealogy I is the whole work.
PENDING = [
    ("Table 2", "Genealogy II",
     "Genealogy I carries live cross-references into this table at persons 12 and 73."),
    ("Table 3", "Genealogy III",
     "Referenced from Genealogy I at person 73."),
]

NUMBER_WORDS = {3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}

# The chart's geometry, in rem at the fixed 16px root. Single source of truth:
# the CSS custom properties are emitted from here, and the print reduction is
# computed from here, so the two can never disagree. The values themselves are
# the long-verified ones -- --col must exceed the widest line at generations
# 1 to n-1 or a line will spill into the next column (see the CSS comment).
GEOM = {"lh_rem": 1.55, "stub_rem": 2.6, "col_rem": 24, "sheet_pad_rem": 2.2}


def geom_css():
    """The geometry tokens, emitted from GEOM rather than typed into the CSS."""
    return (":root{--lh:%srem;--stub:%srem;--col:%srem;--sheet-pad:%srem}\n"
            % (GEOM["lh_rem"], GEOM["stub_rem"], GEOM["col_rem"],
               GEOM["sheet_pad_rem"]))


def print_zoom(n_gens):
    """
    The zoom that fits one sheet on a landscape page, from the same GEOM the
    layout uses. 1030px is the printable width of landscape A4/letter at 96dpi
    inside the 12mm @page margins; the browser's shrink-to-fit is the backstop.
    """
    rem = (2 * GEOM["sheet_pad_rem"]
           + (n_gens - 1) * (GEOM["col_rem"] + GEOM["stub_rem"])
           + GEOM["col_rem"])
    sheet_px = rem * 16 + 2   # + the sheet's own border
    return min(1.0, round(1030 / sheet_px, 3))

SITE = "https://pueblogenealogy.github.io"
REPO = "https://github.com/PuebloGenealogy/pueblogenealogy.github.io"
AUTHOR = "Elizabeth Heger-Vlahovic"

# Google Search Console ownership token, from Settings -> Ownership verification
# -> HTML tag (the content="..." value only, not the whole tag). Left empty until
# a property is created; while empty no tag is emitted and the output is
# unchanged. It lives here rather than as a hand-placed file in docs/ because
# docs/ is generated and a stray file there would be easy to lose.
GOOGLE_SITE_VERIFICATION = ""


def describe(spec, n_persons, n_gens):
    """The meta/OG description for one table. Generated so counts cannot go stale."""
    gens = NUMBER_WORDS.get(n_gens, str(n_gens))
    return (
        f"A verified digital transcription of {spec['plate']}, "
        f"“Genealogy {spec['numeral']}”, from Elsie Clews Parsons’s Laguna "
        f"Genealogies (1923): {n_persons} individuals across {gens} generations, "
        "with names, ages, clans and marriages as printed."
    )

# Where the plate replaces a sibling bracket with a cross-reference because the
# same children are already drawn elsewhere on the sheet. Union U04 (7 x 8) is
# drawn under 7 in the upper half; under 8 in the lower half the plate prints
# this note instead. See PLATE_NOTES in the workbook.
SECOND_VISIT_NOTE = {
    "U04": "For descendants, see above, 13-15, 28-30",   # Table 1, under 8
    "V02": "For descendants, see above",                 # Table 4, under 4
}

RESEARCH_KEYS = ("english_name", "census_name", "census_year", "match_confidence", "notes")
BASE_KEYS = ("sex", "name_as_printed", "alt_name", "age", "clan", "vital_note",
             "origin", "cross_ref", "plate_note")


def load_baseline(spec):
    """
    The same four structures load() returns, built from a table's 1923 baseline.

    Every research key is set to "" -- not omitted -- so Chart and person_line
    work unchanged and the English-name and census chips cannot render. The
    absence of research data here is a property of the module, not of this
    function: a transcription module has no such columns to read.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    T = importlib.import_module(spec["module"])

    problems = T.self_check()
    if problems:
        raise SystemExit(f"{spec['module']}.py failed its structural checks:\n  "
                         + "\n  ".join(problems))

    persons = {}
    for pid, _gen, sex, name, alt, age, clan, vital, origin, xref, note in T.PERSONS:
        p = dict(zip(BASE_KEYS, (sex, name, alt, age, clan, vital, origin, xref, note)))
        p = {k: ("" if v is None else str(v).strip()) for k, v in p.items()}
        p.update({k: "" for k in RESEARCH_KEYS})
        p["id"] = pid
        p["generation"] = _gen
        persons[pid] = p

    # UNIONS rows are 6-tuples, or 7 with a trailing drawn_under -- the id of
    # the block the plate prints this marriage inside, when that is not either
    # partner's own block. Table 1 uses none, so it is read as absent there.
    unions = []
    for row in T.UNIONS:
        uid, wife, husband, _wo, _ho, note = row[:6]
        unions.append({
            "union_id": uid,
            "wife": wife or 0,
            "husband": husband or 0,
            "note": note or "",
            "drawn_under": (row[6] if len(row) > 6 else 0) or 0,
        })

    kids_by_union, kids_by_mother = {}, {}
    for uid, mother, _father, child, _note in T.CHILDREN:
        if uid:
            kids_by_union.setdefault(uid, []).append(child)
        else:
            # Paternity not assignable on the plate (83-85), so the group hangs
            # off the mother's line alone.
            kids_by_mother.setdefault(mother, []).append(child)

    return persons, unions, kids_by_union, kids_by_mother


def load():
    from openpyxl import load_workbook

    wb = load_workbook(XLSX, data_only=False)

    def rows(sheet):
        ws = wb[sheet]
        hdr = [c.value for c in ws[1]]
        for row in ws.iter_rows(min_row=2, values_only=True):
            # Skip only fully blank rows. A blank first cell is meaningful:
            # CHILDREN rows whose paternity cannot be assigned carry no union_id.
            if all(v is None or str(v).strip() == "" for v in row):
                continue
            yield dict(zip(hdr, row))

    persons = {}
    for r in rows("PERSONS"):
        persons[int(r["id"])] = {
            k: ("" if r.get(k) is None else str(r[k]).strip())
            for k in ("sex", "name_as_printed", "alt_name", "age", "clan", "vital_note",
                      "origin", "cross_ref", "plate_note", "english_name", "census_name",
                      "census_year", "match_confidence", "notes")
        }
        persons[int(r["id"])]["id"] = int(r["id"])
        persons[int(r["id"])]["generation"] = r.get("generation") or 0

    unions = [
        {
            "union_id": r["union_id"],
            "wife": int(r["wife_id"] or 0),
            "husband": int(r["husband_id"] or 0),
            "note": r.get("note") or "",
            "drawn_under": 0,
        }
        for r in rows("UNIONS")
    ]

    kids_by_union, kids_by_mother = {}, {}
    for r in rows("CHILDREN"):
        uid = r.get("union_id") or ""
        child, mother = int(r["child_id"]), int(r["mother_id"])
        if uid:
            kids_by_union.setdefault(uid, []).append(child)
        else:
            kids_by_mother.setdefault(mother, []).append(child)

    return persons, unions, kids_by_union, kids_by_mother


def esc(s):
    return html.escape(str(s))


def dotted(s):
    """Add the plate's trailing period, unless the value already ends in one ('d.')."""
    s = esc(s)
    return s if s.endswith(".") else s + "."


def linkify_xref(text, persons):
    """
    Wrap person-number tokens in same-table anchors: '76' -> <a href="#p76">76</a>,
    '90-3' -> <a href="#p90">90-3</a>. `text` is already HTML-escaped.

    A cross-reference into another genealogy ('see Gen. II, 21, 74') is left
    entirely untouched: those numbers belong to a table that is not transcribed,
    and a link must not promise content that does not exist. The visible text is
    identical either way -- only the markup around it changes.
    """
    if "Gen." in text:
        return text

    def repl(m):
        if int(m.group(1)) in persons:
            return f'<a href="#p{m.group(1)}">{m.group(0)}</a>'
        return m.group(0)

    return re.sub(r"(\d+)(?:-\d+)?", repl, text)


def wrap_line(inner, lead=False, anchor=None):
    """
    Wrap a line's spans in its row div.

    `lead` draws the plate's leader rule running from the end of the text to the
    child column -- 'F. Lupi. Sun (Navaho)————————'. Only the mother's line gets
    one, since that is the line the sibling bracket hangs off. The text is kept
    in its own .txt span so the surrounding flex context cannot collapse the
    spaces between fields.

    `anchor` is the citable id ("p13") a person's first printed occurrence
    carries, so #p13 is a stable URL for that line.
    """
    aid = f' id="{anchor}"' if anchor else ""
    if lead:
        return (f'<div class="line lead-line"{aid}><span class="txt">{inner}</span>'
                '<span class="lead"></span></div>')
    return f'<div class="line"{aid}>{inner}</div>'


def person_line(p, is_spouse, english_seen):
    """The spans of one printed line: '7. F. Dziwaiʼᶦdyitsʼa. d. 1908. Sun'"""
    bits = []
    if is_spouse:
        bits.append('<span class="plus">+</span>')
    # The number is the plate's own citation apparatus, so it is a link: #p13
    # is the stable address of person 13's first printed line.
    bits.append(f'<a class="num" href="#p{p["id"]}">{p["id"]}.</a>')
    bits.append(f'<span class="sex">{esc(p["sex"])}.</span>')

    name, alt = p["name_as_printed"], p["alt_name"]
    if name and alt:
        if "braced" in p["plate_note"]:
            nm = f'<span class="brace">{{</span>{esc(name)} / {esc(alt)}<span class="brace">}}</span>'
        else:
            nm = f'{esc(name)} <span class="alt">({esc(alt)})</span>'
    elif name:
        nm = esc(name)
    else:
        nm = '<span class="blank">———</span>'
    # kjq = Western Keres. Without this the names sit inside lang="en" and a
    # screen reader applies English phonics to Americanist transcription.
    lang = ' lang="kjq"' if name else ""
    bits.append(f'<span class="name"{lang}>{nm}.</span>')

    eng = p["english_name"]
    if eng and eng != alt:
        english_seen.add(p["id"])
        bits.append(f'<span class="eng">{esc(eng)}</span>')

    if p["age"]:
        bits.append(f'<span class="age">{dotted(p["age"])}</span>')
    if p["vital_note"]:
        bits.append(f'<span class="vital">{dotted(p["vital_note"])}</span>')

    if p["clan"]:
        clan = esc(p["clan"]) + (f' ({esc(p["origin"])})' if p["origin"] else "")
    elif p["origin"]:
        clan = f'of {esc(p["origin"])}'
    else:
        clan = ""
    if clan:
        bits.append(f'<span class="clan">{clan}</span>')

    census = " ".join(x for x in (p["census_name"], p["census_year"]) if x)
    if census:
        bits.append(f'<span class="census" title="census match">{esc(census)}</span>')

    return " ".join(bits)


class Chart:
    def __init__(self, persons, unions, kids_by_union, kids_by_mother):
        self.P = persons
        self.U = unions
        self.KU = kids_by_union
        self.KM = kids_by_mother
        self.rendered_unions = set()
        self.xref_printed = set()
        self.english_seen = set()
        self.placed = set()  # drawn as a descendant line; drives sibling-group dedupe
        self.seen = set()    # drawn anywhere, including as a '+' spouse line

    def unions_of(self, pid):
        # Every marriage this person is in, including ones already drawn from the
        # other spouse's side: the plate prints the '+' line in both places and
        # replaces the repeated sibling bracket with a cross-reference.
        return [u for u in self.U
                if pid in (u["wife"], u["husband"]) or u["drawn_under"] == pid]

    def render(self, pid, depth=0):
        """
        Draw one block (a person plus their '+' spouse lines) and its descendants.

        Vertical alignment follows the plate: a sibling bracket hangs off the
        MOTHER's line, not off the top of the block. Where the mother is the
        block's primary -- 66 with children 80-82 -- that is row 0. Where the
        primary is male and the mothers are his wives -- 8 with wives 7 and 73 --
        each group sits on its own wife's row. Verified against the plate at
        sources/parsons-1923-table-1.jpg.
        """
        p = self.P[pid]
        self.placed.add(pid)
        # The FIRST printed occurrence of a person -- primary line or '+' spouse
        # line, whichever the document reaches first -- carries the citable
        # id="p{n}". seen-order equals document order here: a block's own lines
        # are all marked before its child column is rendered.
        first = pid not in self.seen
        self.seen.add(pid)

        # Entries are (kind, content, anchor); the list index is the row, which
        # is what the leader rules and the child-column offsets are keyed on.
        block = [("line", person_line(p, False, self.english_seen),
                  f"p{pid}" if first else None)]
        shown = {pid}           # ids already printed in this block
        row = 0                # index of the last line written into the block
        groups = []            # (mother_row, kind, payload) -> the child column

        if p["cross_ref"] and pid not in self.xref_printed:
            self.xref_printed.add(pid)
            for part in p["cross_ref"].split("|"):
                block.append(("xref", linkify_xref(esc(part.strip()), self.P), None))
                row += 1

        # Pass 1: lay out this block's own lines and decide where each sibling
        # group belongs. No recursion here, so union bookkeeping resolves in the
        # same order it did before descendants are drawn.
        for u in self.unions_of(pid):
            drawn_before = u["union_id"] in self.rendered_unions
            self.rendered_unions.add(u["union_id"])
            if pid in (u["wife"], u["husband"]):
                other = u["husband"] if u["wife"] == pid else u["wife"]
            else:
                # A drawn_under union: the primary is not a partner, so the '+'
                # line to print is whichever partner this block has not shown.
                # Table 4 sets 6's second husband 7 under 5, because 6 is
                # already on the line above.
                other = u["husband"] if u["wife"] in shown else u["wife"]
            mother_row = row
            if other:
                sp = self.P[other]
                first_sp = other not in self.seen
                self.seen.add(other)
                shown.add(other)
                block.append(("line", person_line(sp, True, self.english_seen),
                              f"p{other}" if first_sp else None))
                row += 1
                mother_row = row
                if sp["cross_ref"] and other not in self.xref_printed:
                    self.xref_printed.add(other)
                    for part in sp["cross_ref"].split("|"):
                        block.append(("xref", linkify_xref(esc(part.strip()), self.P), None))
                        row += 1
            if u["wife"] == pid:
                mother_row = 0          # the primary is the mother

            kids = self.KU.get(u["union_id"], [])
            if kids and (drawn_before or all(k in self.placed for k in kids)):
                note = SECOND_VISIT_NOTE.get(u["union_id"], "see elsewhere on this table")
                groups.append((mother_row, "note", note))
            else:
                new = [k for k in kids if k not in self.placed]
                if new:
                    groups.append((mother_row, "kids", new))

        orphans = [k for k in self.KM.get(pid, []) if k not in self.placed]
        if orphans:
            groups.append((0, "kids", orphans))

        # Pass 2: draw the child column, each group on its own mother's row.
        #
        # A group is as tall as the subtree it contains, so two multi-child
        # groups in one block cannot both start on their mother's line unless
        # the block's own lines are spread apart -- which is exactly what the
        # plate does. Table 4 sets 11 and 12 under 10 with three children each,
        # and prints 12 three lines below 11, not one. So when a group cannot
        # begin at its mother's row, the mother's line is pushed down to meet
        # it, and every line after it follows in normal flow.
        groups.sort(key=lambda g: g[0])
        col = []
        child_cursor = 0     # next free row in the child column
        pushed = 0           # rows inserted into the block so far
        line_pad = {}        # block line index -> extra rows before that line
        for mother_row, kind, payload in groups:
            target = mother_row + pushed
            if child_cursor > target:
                delta = child_cursor - target
                line_pad[mother_row] = line_pad.get(mother_row, 0) + delta
                pushed += delta
                target = child_cursor
            gap = target - child_cursor
            if kind == "note":
                inner = ('<div class="node"><div class="block">'
                         f'<div class="xref xref-cell">{linkify_xref(esc(payload), self.P)}</div>'
                         '</div></div>')
                rows = 1
            else:
                parts = [self.render(k, depth + 1) for k in payload]
                inner = "".join(h for h, _ in parts)
                rows = sum(r for _, r in parts)
            style = f' style="margin-top:calc(var(--lh) * {gap})"' if gap else ""
            col.append(f'<div class="kids"{style}>{inner}</div>')
            child_cursor = target + rows

        # A leader rule goes on every row that a sibling group hangs off, i.e.
        # each mother's line -- whether she is the primary (66) or a '+' spouse
        # (12, 17, 57). Same row index the child column is offset by.
        lead_rows = {g[0] for g in groups}
        lines = []
        for i, (kind, content, anchor) in enumerate(block):
            html_line = (wrap_line(content, lead=(i in lead_rows), anchor=anchor)
                         if kind == "line"
                         else f'<div class="xref">{content}</div>')
            if line_pad.get(i):
                html_line = html_line.replace(
                    "<div ", f'<div style="margin-top:calc(var(--lh) * {line_pad[i]})" ', 1)
            lines.append(html_line)

        # Leaf blocks need no fixed width: nothing hangs off them, so a long
        # generation-5 entry can run past the column instead of widening the sheet.
        node_class = "node" if col else "node leaf"
        out = [f'<div class="{node_class}">', '<div class="block">', *lines, "</div>"]
        if col:
            out.append('<div class="kidcol">' + "".join(col) + "</div>")
        out.append("</div>")  # .node
        # Height in rows, so the caller can stack sibling groups without
        # assuming every group is one line tall.
        return "".join(out), max(len(block) + pushed, child_cursor)


def font_css():
    """
    @font-face rules with the subset woff2 base64-inlined, or "" if absent.

    Inlining keeps the page a single self-contained file -- no external request,
    nothing to break if the fonts folder is ever moved, and archivable as one
    document. ~35 kB for both faces.

    The face is named "Laguna Serif" rather than Gentium: the OFL reserves the
    latter for unmodified releases, and a subset is a modification. See
    scripts/subset_font.py.
    """
    faces = []
    for style, weight in (("regular", "normal"), ("italic", "italic")):
        path = FONT_DIR / f"laguna-serif-{style}.woff2"
        if not path.exists():
            print(f"  note: {path.name} missing -- falling back to system fonts. "
                  "Run scripts/subset_font.py to embed it.")
            return ""
        b64 = base64.b64encode(path.read_bytes()).decode("ascii")
        faces.append(
            "@font-face{font-family:'Laguna Serif';font-style:%s;font-weight:400;"
            "font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
            % (weight, b64)
        )
    return "\n".join(faces) + "\n"


CSS = """
/* ---- tokens ------------------------------------------------------------ */
/* One palette, both themes. Custom-property declarations are never dropped at
   parse time (any token stream is valid), so a static-then-light-dark() pair
   would NOT fall back -- the second declaration always wins and turns
   invalid-at-computed-value-time where light-dark() is unsupported. Hence the
   structure below: static light tokens unconditionally; the light-dark()
   pairs only inside @supports; a static dark set (via the media query and
   [data-theme], exactly like the old site) for engines without light-dark().
   The [data-theme] color-scheme flips are all the JS theme control needs. */
:root{color-scheme:light dark}
:root[data-theme="light"]{color-scheme:light}
:root[data-theme="dark"]{color-scheme:dark}
:root{
  --paper:#FAF8F4; --panel:#FFFDF9; --ink:#1C1A17; --muted:#635D53;
  /* plate rules: >=3:1 against --panel in BOTH themes (non-text minimum) */
  --rule:#7D766B;
  /* chrome hairlines only -- never the plate's own rules */
  --rule-faint:#C4BFB4;
  --accent:#7A5C1E; --accent-strong:#5C450F; --ink-lineage:#3A342A;
  --wash:#F4E6CA; --shadow:rgba(0,0,0,.07);
  /* research chips -- private build only; class names are the leak check's markers */
  --eng-bg:#E8DFC8; --eng-fg:#4A3A12; --cen-bg:#DCE6EF; --cen-fg:#22384C;
  /* two type voices: the plate speaks 1923, the chrome speaks 2026 */
  --font-plate:"Laguna Serif","Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --font-ui:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --bar-h:2.75rem; --measure:42rem; --measure-wide:72rem;
  --s1:.25rem; --s2:.5rem; --s3:.75rem; --s4:1rem; --s5:1.5rem; --s6:2.5rem; --s7:4rem;
}
@supports (color: light-dark(#000,#fff)){
  :root{
    --paper:light-dark(#FAF8F4,#191713);
    --panel:light-dark(#FFFDF9,#221F1B);
    --ink:light-dark(#1C1A17,#E9E6DF);
    --muted:light-dark(#635D53,#A49E93);
    --rule:light-dark(#7D766B,#756F66);
    --rule-faint:color-mix(in oklab,var(--rule) 45%,var(--paper));
    --accent:light-dark(#7A5C1E,#DBB970);
    --accent-strong:light-dark(#5C450F,#DBB970);
    --ink-lineage:light-dark(#3A342A,#C9C0AF);
    --wash:light-dark(#F4E6CA,#2E250D);
    --shadow:light-dark(rgba(0,0,0,.07),rgba(0,0,0,.45));
    --eng-bg:light-dark(#E8DFC8,#3A3016);
    --eng-fg:light-dark(#4A3A12,#F0DFAE);
    --cen-bg:light-dark(#DCE6EF,#1D2E3D);
    --cen-fg:light-dark(#22384C,#BCD7EE);
  }
}
/* Engines without light-dark() (Firefox ESR 115, Safari <=17.4): the same
   dark set, statically, keyed the way the old site keyed it. Kept in step
   with the pairs above -- change one, change both. */
@supports not (color: light-dark(#000,#fff)){
  @media (prefers-color-scheme:dark){
    :root{
      --paper:#191713; --panel:#221F1B; --ink:#E9E6DF; --muted:#A49E93;
      --rule:#756F66; --rule-faint:#423F38; --accent:#DBB970;
      --accent-strong:#DBB970; --ink-lineage:#C9C0AF; --wash:#2E250D;
      --shadow:rgba(0,0,0,.45); --eng-bg:#3A3016; --eng-fg:#F0DFAE;
      --cen-bg:#1D2E3D; --cen-fg:#BCD7EE;
    }
    :root[data-theme="light"]{
      --paper:#FAF8F4; --panel:#FFFDF9; --ink:#1C1A17; --muted:#635D53;
      --rule:#7D766B; --rule-faint:#C4BFB4; --accent:#7A5C1E;
      --accent-strong:#5C450F; --ink-lineage:#3A342A; --wash:#F4E6CA;
      --shadow:rgba(0,0,0,.07); --eng-bg:#E8DFC8; --eng-fg:#4A3A12;
      --cen-bg:#DCE6EF; --cen-fg:#22384C;
    }
  }
  :root[data-theme="dark"]{
    --paper:#191713; --panel:#221F1B; --ink:#E9E6DF; --muted:#A49E93;
    --rule:#756F66; --rule-faint:#423F38; --accent:#DBB970;
    --accent-strong:#DBB970; --ink-lineage:#C9C0AF; --wash:#2E250D;
    --shadow:rgba(0,0,0,.45); --eng-bg:#3A3016; --eng-fg:#F0DFAE;
    --cen-bg:#1D2E3D; --cen-fg:#BCD7EE;
  }
}
@media (prefers-contrast:more){:root{--muted:var(--ink);--rule:var(--muted)}}

/* ---- base -------------------------------------------------------------- */
*{box-sizing:border-box}
/* 'Laguna Serif' is the embedded Gentium subset (see font_css). It leads the
   stack because it is the only face guaranteed to carry the phonetic modifier
   letters ᶦ ᵘ ᵃ; the rest are fallbacks for a build made without it.
   Root size is fixed at 16px: the chart's metrics were measured against it. */
body{margin:0;background:var(--paper);color:var(--ink);
  font:16px/1.55 var(--font-plate)}
:focus-visible{outline:2px solid var(--accent-strong);outline-offset:2px}
.visually-hidden{position:absolute;width:1px;height:1px;margin:-1px;padding:0;
  overflow:hidden;clip-path:inset(50%);white-space:nowrap;border:0}
.skip{position:fixed;inset-inline-start:-100vw;inset-block-start:var(--s3);
  z-index:100;background:var(--paper);color:var(--ink);
  border:1px solid var(--rule);padding:.5rem 1rem;
  font:600 .8125rem/1 var(--font-ui);text-decoration:none}
.skip:focus{inset-inline-start:var(--s3)}

/* ---- masthead (sticky site chrome) ------------------------------------- */
.masthead{position:sticky;inset-block-start:0;z-index:30;min-height:var(--bar-h);
  display:flex;align-items:center;flex-wrap:wrap;gap:var(--s2) var(--s5);
  padding:var(--s2) var(--s4);background:var(--paper);
  border-block-end:1px solid var(--rule-faint);
  font:400 .72rem/1.2 var(--font-ui);letter-spacing:.08em}
.wordmark{text-transform:uppercase;letter-spacing:.14em;font-weight:600;
  color:var(--ink);text-decoration:none}
a.wordmark:hover{color:var(--accent)}
a.wordmark:focus-visible{color:var(--accent)}
.masthead nav{color:var(--muted);text-transform:uppercase}
.masthead nav a{color:var(--muted);text-decoration:underline;text-underline-offset:.25em}
.masthead nav a:hover{color:var(--accent)}
.masthead nav a:focus-visible{color:var(--accent)}
.masthead nav a[aria-current="page"]{color:var(--ink);text-decoration:none}
.mast-right{margin-inline-start:auto;display:flex;align-items:center;gap:var(--s4)}
.mast-link{color:var(--muted);text-transform:uppercase;text-underline-offset:.25em}
.mast-link:hover{color:var(--accent)}
.mast-link:focus-visible{color:var(--accent)}
.mast-btn{font:inherit;letter-spacing:inherit;text-transform:uppercase;
  color:var(--muted);background:none;border:1px solid var(--rule-faint);
  border-radius:2px;padding:.3rem .6rem;cursor:pointer;min-height:24px}
.mast-btn:hover{color:var(--ink);border-color:var(--rule)}
.mast-btn:focus-visible{color:var(--ink);border-color:var(--rule)}

/* ---- title page -------------------------------------------------------- */
.titlepage{max-width:var(--measure);margin:0 auto;
  padding:var(--s7) var(--s5) var(--s5);text-align:center}
.plate-label{font-variant:small-caps;letter-spacing:.22em;font-size:.8125rem;
  color:var(--muted)}
h1{font-size:clamp(1.6rem,1.15rem + 1.9vw,2.5rem);font-weight:400;
  letter-spacing:.09em;line-height:1.15;margin:.35rem 0 0;text-wrap:balance}
.rule-double{width:8rem;height:4px;margin:var(--s4) auto;
  border-block-start:2px solid var(--ink);border-block-end:1px solid var(--ink)}
.cite{font-size:.9375rem;color:var(--muted);line-height:1.65}
.imprint{margin-block-start:var(--s3);font-variant:small-caps;
  letter-spacing:.22em;font-size:.8125rem;color:var(--muted)}

/* ---- editor's key ------------------------------------------------------ */
.key{max-width:var(--measure-wide);margin:0 auto;
  padding:0 var(--s5) var(--s5);display:flex;flex-wrap:wrap;
  gap:var(--s2) var(--s5);justify-content:center;
  font-size:.8125rem;line-height:1.55;color:var(--muted)}
.key .k{white-space:nowrap}
.key .k-label{font-family:var(--font-ui);font-size:.75rem}
.key-bracket,.key-lead{display:inline-block;vertical-align:middle;
  width:1.1rem;height:.95rem;position:relative}
.key-bracket{border-inline-start:1px solid var(--rule)}
.key-bracket::before,.key-bracket::after{content:"";position:absolute;
  inset-inline:0;border-block-start:1px solid var(--rule)}
.key-bracket::before{inset-block-start:0}
.key-bracket::after{inset-block-end:0}
.key-lead{height:.5rem;border-block-end:1px solid var(--rule)}

/* ---- plate bar --------------------------------------------------------- */
.plate-bar{max-width:var(--measure-wide);margin:0 auto;
  padding:0 var(--s5) var(--s3);display:flex;justify-content:space-between;
  align-items:baseline;gap:var(--s3) var(--s4);flex-wrap:wrap}
.plate-cap{font-variant:small-caps;letter-spacing:.14em;font-size:.8125rem;
  color:var(--muted)}
.plate-tools{display:flex;align-items:center;gap:var(--s3);
  font-family:var(--font-ui);flex-wrap:wrap}
/* :not([hidden]) -- an unconditional display would defeat the hidden
   attribute (author display beats the UA's [hidden]{display:none}) and ship
   a dead search form to no-JS readers. */
#find:not([hidden]){display:flex;align-items:center;gap:var(--s2)}
#find input{font:.8125rem var(--font-ui);color:var(--ink);
  background:var(--panel);border:1px solid var(--rule);border-radius:2px;
  padding:.35rem .6rem;width:17rem;max-width:60vw}
#find input:focus-visible{outline:2px solid var(--accent-strong);
  outline-offset:1px}
.find-note{font:.75rem var(--font-ui);color:var(--muted)}
#scale-mount{display:flex;align-items:center;gap:var(--s1)}
.scale-l{font:.72rem var(--font-ui);text-transform:uppercase;
  letter-spacing:.08em;color:var(--muted);margin-inline-end:var(--s1)}
.scale-btn{font:.8125rem var(--font-ui);color:var(--muted);background:none;
  border:1px solid var(--rule-faint);border-radius:2px;padding:.3rem .55rem;
  cursor:pointer;min-height:24px}
.scale-btn[aria-pressed="true"]{color:var(--ink);border-color:var(--rule)}
.scale-btn:hover{color:var(--ink)}
.scale-btn:focus-visible{color:var(--ink)}

/* ---- the plate: shell, scroller, ruler, sheet -------------------------- */
.plate{margin:0}
/* The shell owns the edge fades as overlays, so nothing about the scroller's
   own layout -- the container the chart invariants live in -- changes. */
.scroll-shell{position:relative;timeline-scope:--plate-x}
.scroll-shell::before,.scroll-shell::after{content:"";position:absolute;
  inset-block:0 var(--s6);width:2rem;pointer-events:none;z-index:5}
.scroll-shell::before{inset-inline-start:0;visibility:hidden;
  background:linear-gradient(to right,var(--paper),transparent)}
.scroll-shell::after{inset-inline-end:0;opacity:.5;
  background:linear-gradient(to left,var(--paper),transparent)}
/* The region is focusable so a keyboard user can scroll the wide chart with the
   arrow keys; without that the later generations are unreachable. Give the
   focus ring room so it is not clipped by the scroll container. */
.scroll{overflow-x:auto;padding:var(--s3) var(--s5) var(--s6);
  -webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;
  scrollbar-color:var(--rule) transparent;scrollbar-gutter:stable;
  scroll-timeline:--plate-x inline}
.scroll:focus-visible{outline:2px solid var(--accent);outline-offset:-4px}
/* Reduction wrapper: the scale control and the print fit both zoom HERE, so
   the ruler and the sheet always scale together and the column grid survives
   scaling by construction. */
.plate-zoom{display:inline-block;min-width:100%;zoom:var(--plate-zoom,1)}
/* Generation ruler: editorial apparatus OUTSIDE the sheet's frame. Its labels
   are sized from the same --col/--stub/--sheet-pad tokens as the grid, so
   alignment is exact by construction and the 0px-drift check covers it.
   It pans with the plate; viewport-pinned identity is the masthead's job
   (position:sticky cannot pin vertically inside a horizontal scroller). */
.ruler{display:flex;align-items:flex-end;width:max-content;min-width:100%;
  height:2rem;margin-block-end:var(--s2);
  padding-inline-start:calc(var(--sheet-pad) + 1px);
  font:600 .72rem/1.9 var(--font-ui);text-transform:uppercase;
  letter-spacing:.08em;color:var(--muted);
  border-block-end:1px solid var(--rule-faint);position:relative}
.ruler .gen{flex:none;width:var(--col);margin-inline-end:var(--stub);
  border-inline-start:1px solid var(--rule-faint);padding-inline-start:.5rem}
.ruler .gen:last-child{width:auto;margin-inline-end:0}
/* Identity chip: a zero-width sticky slot on the INLINE axis (which genuinely
   scrolls), so it can never displace a label. Invisible at rest; fades in over
   the first 8% of pan where scroll-driven animations exist. */
/* min-width:0 defeats the flex item's min-width:auto -- without it the slot
   takes the chip's content width and displaces every label by that much. */
.ruler-chipslot{flex:0 0 0px;min-width:0;overflow:visible;position:sticky;
  inset-inline-start:var(--s3);z-index:1;align-self:center}
.ruler-chip{display:inline-block;white-space:nowrap;padding:.05rem .55rem;
  border:1px solid var(--rule-faint);border-radius:999px;background:var(--paper);
  color:var(--ink);font:400 .72rem/1.9 var(--font-plate);text-transform:none;
  letter-spacing:.02em;opacity:0}
/* Progress hairline under the ruler: inks left-to-right as the plate pans. */
.ruler::after{content:"";position:absolute;inset-inline:0;inset-block-end:-1px;
  height:2px;background:var(--accent);transform-origin:0 50%;transform:scaleX(0)}
@media (prefers-reduced-motion:no-preference){
  @supports (animation-timeline:scroll()){
    .ruler-chip{animation:chip-in linear both;animation-timeline:--plate-x;
      animation-range:0% 8%}
    .ruler::after{animation:plate-progress linear both;animation-timeline:--plate-x}
    .scroll-shell::before{visibility:visible;opacity:0;
      animation:fade-in linear both;animation-timeline:--plate-x;animation-range:0% 6%}
    /* Base 0, first keyframe 1: when the plate does not overflow the timeline
       is INACTIVE, the animation applies nothing, and the base 0 hides the
       fade -- a raised base would leave it stuck over a non-scrolling plate. */
    .scroll-shell::after{opacity:0;
      animation:fade-right linear both;animation-timeline:--plate-x;animation-range:94% 100%}
  }
}
@keyframes chip-in{to{opacity:1}}
@keyframes plate-progress{to{transform:scaleX(1)}}
@keyframes fade-in{to{opacity:1}}
@keyframes fade-right{from{opacity:1}to{opacity:0}}
/* The sheet: a flat matted plate. Layout rules below are byte-identical to the
   verified originals -- skin only may change. */
.sheet{display:inline-block;min-width:100%;background:var(--panel);
  border:1px solid var(--rule);padding:2rem var(--sheet-pad)}
.tree + .tree{margin-top:3.2rem;padding-top:2.4rem;border-top:1px dashed var(--rule)}
.node{display:flex;align-items:flex-start}
/* THE COLUMN GRID. Every .node is [.block][.kidcol] and every nested node adds
   exactly one --stub of padding plus one block, so a fixed block width puts
   generation d at d x (--col + --stub) on every path -- which is what makes the
   two families share one set of columns, as they do on the plate. --col is the
   single tunable: it must exceed the widest line at generations 1-4 (measured
   339px) or that line will spill into the next column.
   Vertical padding must stay 0: every line is exactly one --lh tall, which is
   what lets a sibling group be offset onto its mother's row by whole rows. */
.block{white-space:nowrap;padding:0;width:var(--col)}
.node.leaf > .block{width:auto}
.line{line-height:var(--lh);
  scroll-margin-block:calc(var(--bar-h) + 1.5rem) 1rem;
  scroll-margin-inline:var(--stub)}
.line:target{background:var(--wash);box-shadow:inset 2px 0 0 var(--accent)}
/* The plate's leader rule, filling the gap from the end of the mother's text to
   the child column: '1. F. Lupi. Sun (Navaho)————————3. F. Nayowʼ˙ăitsa. Sun'.
   It ends exactly at --col, where the child's bracket bar begins, so the two
   read as one continuous rule. */
.lead-line{display:flex;align-items:baseline}
.lead-line > .txt{white-space:nowrap}
.lead{flex:1 1 auto;min-width:1.2rem;align-self:stretch;position:relative}
.lead::before{content:"";position:absolute;left:.5rem;right:0;top:50%;
  border-top:1px solid var(--rule)}
/* One .kids group per sibling bracket, stacked so each can be offset onto the
   row of its own mother -- see the docstring on Chart.render. */
.kidcol{display:flex;flex-direction:column}
.kids{display:flex;flex-direction:column}
.kids > .node{position:relative;padding-left:var(--stub)}
.kids > .node::before{content:"";position:absolute;left:0;width:var(--stub);
  top:calc(var(--lh)/2);border-top:1px solid var(--rule)}
.kids > .node::after{content:"";position:absolute;left:0;border-left:1px solid var(--rule)}
.kids > .node:first-child::after{top:calc(var(--lh)/2);bottom:0}
.kids > .node:last-child::after{top:0;height:calc(var(--lh)/2)}
.kids > .node:not(:first-child):not(:last-child)::after{top:0;bottom:0}
.kids > .node:only-child::after{display:none}
/* Lineage inking: hovering or focusing within a block darkens the rules a
   reader would trace with a finger -- its own bracket and the brackets it
   hangs. Color-only, on the existing 1px borders; the plate is never dimmed.
   Engines without :has() simply read the chart as before. */
.kids > .node:has(.block:hover,.block:focus-within)::before,
.kids > .node:has(.block:hover,.block:focus-within)::after{
  border-color:var(--ink-lineage)}
.node:has(> .block:hover,> .block:focus-within) > .block .lead::before,
.node:has(> .block:hover,> .block:focus-within) > .kidcol > .kids > .node::before,
.node:has(> .block:hover,> .block:focus-within) > .kidcol > .kids > .node::after{
  border-color:var(--ink-lineage)}
@media (prefers-reduced-motion:no-preference){
  .kids > .node::before,.kids > .node::after,.lead::before{
    transition:border-color .12s ease}
}
.num{color:var(--muted);font-variant-numeric:tabular-nums}
a.num{text-decoration:none}
a.num:hover{color:var(--accent);text-decoration:underline}
a.num:focus-visible{color:var(--accent);text-decoration:underline}
.sex{color:var(--muted)}
/* + and ——— are text content (spouse marker, unrecorded name), so they hold
   the 4.5:1 text minimum via --muted; --rule is reserved for drawn rules. */
.plus{color:var(--muted);font-weight:600}
.name{font-weight:500}
.alt,.brace{color:var(--muted)}
.age{font-style:italic;font-variant-numeric:tabular-nums}
.vital{font-style:italic;color:var(--muted)}
.clan{color:var(--accent)}
.blank{color:var(--muted);letter-spacing:-.05em}
.eng{background:var(--eng-bg);color:var(--eng-fg);border-radius:2px;
  padding:.02em .38em;font-size:.86em;font-weight:600}
.census{background:var(--cen-bg);color:var(--cen-fg);border-radius:2px;
  padding:.02em .38em;font-size:.8em}
/* Wraps at the column edge, as the plate sets it:
   'For second husband and offspring see Gen.' / 'II, 21, 74' */
.xref{font-size:.8rem;color:var(--muted);font-style:italic;
  white-space:normal;max-width:var(--col);line-height:1.4;padding:.1rem 0 .1rem 1.4rem}
.xref a{color:inherit;text-decoration:underline dotted;text-underline-offset:.15em}
.xref a:hover{color:var(--accent)}
.xref a:focus-visible{color:var(--accent)}
/* A cross-reference standing in the child column, where the plate prints it in
   place of a sibling bracket: sits on its mother's baseline, no indent. */
/* padding must be 0 so the cell is exactly one line tall; otherwise it pushes
   the next sibling group off its mother's row. */
.xref-cell{padding:0;line-height:var(--lh);white-space:nowrap;max-width:none}
.plate-caption{max-width:var(--measure-wide);margin:0 auto;
  padding:0 var(--s5) var(--s5);font-size:.8125rem;line-height:1.55;
  color:var(--muted)}
.pan-hint{display:none}
@media (max-width:1400px){.pan-hint{display:inline}}

/* ---- register of persons ----------------------------------------------- */
.apparatus-register{max-width:var(--measure-wide);margin:0 auto;
  padding:var(--s6) var(--s5) 0}
.apparatus-register h2,footer h2,.prose h2{font-family:var(--font-plate);
  font-size:.8125rem;font-variant:small-caps;letter-spacing:.14em;
  font-weight:600;color:var(--ink);margin:0 0 var(--s3)}
.reg-note{font:.75rem/1.5 var(--font-ui);color:var(--muted);margin:0 0 var(--s3)}
.register-d{background:var(--panel);border:1px solid var(--rule-faint);
  border-radius:2px}
.register-d summary{cursor:pointer;padding:var(--s3) var(--s4);
  font:.8125rem var(--font-ui);color:var(--muted)}
.register-d summary:hover{color:var(--ink)}
.register-d[open] summary{border-block-end:1px solid var(--rule-faint)}
.reg-list{list-style:none;margin:0;padding:var(--s4);columns:1;
  column-gap:var(--s6)}
@media (min-width:900px){.reg-list{columns:2}}
.reg{break-inside:avoid;padding:var(--s2);
  scroll-margin-block:calc(var(--bar-h) + 1.5rem) 1rem}
.reg:target{background:var(--wash)}
.reg + .reg{border-block-start:1px solid var(--rule-faint)}
.reg-line{font-size:.9375rem}
.reg-rel{font-size:.8125rem;line-height:1.6;color:var(--muted);
  padding-inline-start:1.4rem}
.rel-l{font-family:var(--font-ui);font-size:.7rem;text-transform:uppercase;
  letter-spacing:.08em;color:var(--muted)}
.reg-rel a{color:inherit;text-decoration:underline dotted;
  text-underline-offset:.15em}
.reg-rel a:hover{color:var(--accent)}
.reg-rel a:focus-visible{color:var(--accent)}

/* ---- footer apparatus --------------------------------------------------- */
footer{max-width:var(--measure);margin:0 auto;
  padding:var(--s6) var(--s5) var(--s7);font-size:.875rem;color:var(--muted);
  line-height:1.7;text-wrap:pretty}
footer h2{margin:var(--s6) 0 var(--s3)}
footer h2:first-child{margin-block-start:0}
footer ul{margin:.3rem 0;padding-left:1.2rem}
footer li{margin:.25rem 0}
footer a{color:var(--accent)}
footer code{font-family:var(--font-ui);font-size:.9em}
.cite-block{margin:var(--s3) 0;padding:var(--s3) var(--s4);
  background:var(--panel);border-inline-start:2px solid var(--rule)}
.cite-block p{margin:.4rem 0}
.copy-btn{font:.8125rem var(--font-ui);color:var(--muted);background:none;
  border:1px solid var(--rule-faint);border-radius:2px;padding:.3rem .6rem;
  cursor:pointer;margin-inline-start:var(--s2);min-height:24px}
.copy-btn:hover{color:var(--ink);border-color:var(--rule)}
.copy-btn:focus-visible{color:var(--ink);border-color:var(--rule)}
.updated{margin-top:var(--s6);padding-top:var(--s4);
  border-top:1px solid var(--rule-faint);font-size:.75rem}
.print-url{display:none;font-size:.75rem}

/* ---- person card (popover; JS-filled from the register) ----------------- */
.pcard{position:fixed;margin:var(--s2);padding:var(--s4);
  width:min(26rem,90vw);background:var(--panel);color:var(--ink);
  border:1px solid var(--rule);border-radius:3px;
  box-shadow:0 6px 24px var(--shadow);font-size:.9375rem}
.pcard .reg-rel{padding-inline-start:0;margin-block-start:var(--s1)}
.pcard-actions{display:flex;gap:var(--s3);align-items:center;
  margin:var(--s3) 0 0;font-family:var(--font-ui);font-size:.8125rem}
.pcard-actions button{font:.8125rem var(--font-ui);color:var(--muted);
  background:none;border:1px solid var(--rule-faint);border-radius:2px;
  padding:.3rem .6rem;cursor:pointer;min-height:24px}
.pcard-actions button:hover{color:var(--ink);border-color:var(--rule)}
.pcard-actions button:focus-visible{color:var(--ink);border-color:var(--rule)}
.pcard-actions a{color:var(--accent)}
@supports (anchor-name:--pc){
  .pcard{inset:auto;position-anchor:--pc;
    position-area:block-end span-inline-end;
    position-try-fallbacks:flip-block,flip-inline}
}
@media (prefers-reduced-motion:no-preference){
  .pcard{opacity:1;transition:opacity .12s ease;
    transition-behavior:allow-discrete}
  @starting-style{.pcard:popover-open{opacity:0}}
}
@media (max-width:640px){
  .pcard{inset:auto 0 0 0;width:100%;max-width:none;margin:0;
    max-height:60vh;max-height:60dvh;overflow-y:auto;
    border-radius:8px 8px 0 0;position-area:none}
}

/* ---- print: the offprint ------------------------------------------------ */
@media print{
  :root,:root[data-theme]{color-scheme:light}
  body{background:#fff;color:#000}
  .masthead,.skip,.plate-tools,.pan-hint,.apparatus-register,[popover],
  .ruler-chipslot{display:none}
  .scroll{overflow:visible;padding:0}
  .scroll-shell::before,.scroll-shell::after,.ruler::after{display:none}
  .sheet{border:0;box-shadow:none}
  .plate-zoom{zoom:var(--print-zoom,.7)}
  .ruler{border-block-end-color:#000}
  .tree{break-inside:avoid-page}
  footer{break-before:page}
  footer a[href^="http"]::after,.prose a[href^="http"]::after{
    content:" (" attr(href) ")";font-size:.9em}
  .line:target,.reg:target{background:none;box-shadow:none}
  a.num,.xref a{color:inherit;text-decoration:none}
  .print-url{display:block}
  @page{size:landscape;margin:12mm}
}
"""

# A bracket mark: two generations joined, which is what the plate is made of.
FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='5' fill='%231c1a17'/%3E"
    "%3Cg stroke='%23d9b872' stroke-width='2' fill='none'%3E"
    "%3Cpath d='M7 16h6M13 8v16M13 8h6M13 16h6M13 24h6'/%3E%3C/g%3E%3C/svg%3E"
)


CITE = """Elsie Clews Parsons, &ldquo;Laguna Genealogies,&rdquo;<br>
    <em>Anthropological Papers of the American Museum of Natural History</em>,
    vol.&nbsp;19, pt.&nbsp;5 (1923), pp.&nbsp;133&ndash;292."""

# Notes true of every plate in the edition. Plate-specific notes live on the
# TABLES entry, because a note about Table 1's misprint printed under Table 4
# would be a false statement about that plate.
READING_COMMON = """
    <li>Clan membership is matrilineal: every sibling group carries its mother's clan.
        That rule was used to verify the bracket readings against the plate.</li>
    <li>A dash in place of a name means the plate printed no name.</li>
    <li>The dashed rule separating the two halves is an editorial addition,
        not on the plate. It marks the two founding couples, {couples}.</li>
"""

# The redesign's one disclosure: the reading aids are 2026 apparatus, the sheet
# is 1923. Printed with the editorial notes on every chart page.
APPARATUS_NOTE = """
    <li>The generation ruler above the chart, the linked person numbers, and the
        register below the chart are editorial apparatus of this edition, not
        part of the plate.</li>
"""

def navigating_html(spec):
    """The footer's how-to list. The example anchor uses this table's first
    founding person, so it is correct on every table regardless of size."""
    r = spec["roots"][0]
    return f"""
    <li>Every person number is a stable link &mdash; <code>#p{r}</code> addresses
        person {r}&rsquo;s first printed line, and the address bar keeps it while
        you read.</li>
    <li>The chart region can be focused and panned with the arrow keys; on a
        narrow screen, scroll sideways to follow the later generations.</li>
    <li>With JavaScript: with the chart focused, press <code>/</code> to find a
        person by number or name; selecting a person number opens its register
        card, and Esc closes it. The Theme and Scale controls remember your
        choice.</li>
"""

# Applies a stored manual theme before first paint so the page cannot flash the
# wrong palette. Inline in <head> on every page; theme state is otherwise CSS.
THEME_SNIPPET = ('<script>try{var t=localStorage.getItem("lg-theme");'
                 'if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}'
                 'catch(e){}</script>')

# The shared theme module: cycle Auto -> Light -> Dark on #theme, persist, and
# keep the theme-color metas in step. String-formatted into both scripts below.
_THEME_JS = r"""
var THEMES=["auto","light","dark"];
function applyTheme(t){
  if(t==="light"||t==="dark"){root.dataset.theme=t}
  else{t="auto";delete root.dataset.theme}
  doc.querySelectorAll('meta[name="theme-color"]').forEach(function(m){
    m.content=t==="light"?"#FAF8F4":t==="dark"?"#191713"
      :(m.media&&m.media.indexOf("dark")>=0?"#191713":"#FAF8F4")});
  var b=$("#theme");if(b)b.textContent="Theme: "+t.charAt(0).toUpperCase()+t.slice(1);
}
function cycleTheme(){
  var cur=root.dataset.theme||"auto";
  var next=THEMES[(THEMES.indexOf(cur)+1)%THEMES.length];
  store("lg-theme",next==="auto"?null:next);applyTheme(next);
}
var themeBtn=$("#theme");
if(themeBtn){themeBtn.hidden=false;applyTheme(read("lg-theme")||"auto")}
"""

_JS_PRELUDE = r"""
"use strict";
var doc=document,root=doc.documentElement;
function $(s,c){return (c||doc).querySelector(s)}
function store(k,v){try{v===null?localStorage.removeItem(k):localStorage.setItem(k,v)}catch(e){}}
function read(k){try{return localStorage.getItem(k)}catch(e){return null}}
"""

# Landing page: the theme module only.
LANDING_JS = ("(function(){" + _JS_PRELUDE + _THEME_JS + r"""
doc.addEventListener("click",function(e){
  var t=e.target&&e.target.closest?e.target.closest("[data-action=theme]"):null;
  if(t)cycleTheme();
});
})();""")

# Chart pages: theme, scale, finder, register insurance, copy actions and the
# person card. Every module is feature-checked so one failure never cascades;
# everything JS reveals is authored hidden, so a no-JS page has no dead
# controls. Five delegated listeners, no scroll or resize handlers.
UI_JS = ("(function(){" + _JS_PRELUDE + _THEME_JS + r"""
function flip(b,txt){var o=b.textContent;b.textContent=txt;b.disabled=true;
  setTimeout(function(){b.textContent=o;b.disabled=false},1500)}

/* plate scale -- the reduction. Zooms ruler and sheet together. */
var pz=$(".plate-zoom"),mount=$("#scale-mount");
function applyScale(v){
  pz.style.setProperty("--plate-zoom",v);
  mount.querySelectorAll("button").forEach(function(b){
    b.setAttribute("aria-pressed",b.dataset.v===v?"true":"false")});
}
/* Gated on CSS zoom support (Firefox gained it in 126): an engine that would
   drop the zoom declaration must get the documented no-control fallback,
   not three buttons that do nothing. */
if(pz&&mount&&typeof CSS!=="undefined"&&CSS.supports&&CSS.supports("zoom","0.7")){
  mount.setAttribute("role","group");
  mount.setAttribute("aria-label","Plate scale");
  mount.insertAdjacentHTML("beforeend",
    '<span class="scale-l">Scale</span>'+
    ["1","0.85","0.7"].map(function(v){
      return '<button class="scale-btn" data-action="scale" data-v="'+v+'">'+
        Math.round(parseFloat(v)*100)+'%</button>'}).join(""));
  var sv=read("lg-scale");
  applyScale(sv==="0.85"||sv==="0.7"?sv:"1");
}

/* finder: leading integer wins; otherwise diacritic-folded substring match. */
var form=$("#find"),input=$("#find-q"),note=$("#find-note"),
    datalist=$("#persons-list");
function fold(s){return s.normalize("NFD").replace(/\p{M}+/gu,"")
  .replace(/[\p{Lm}˙'’]/gu,"").toLowerCase()}
if(form&&input&&datalist){
  form.hidden=false;
  var opts=[].map.call(datalist.options,function(o){
    return {id:o.value,folded:fold(o.textContent||"")}});
  form.addEventListener("submit",function(e){
    e.preventDefault();
    var q=input.value.trim();if(!q)return;
    var id=null,m=q.match(/^\d+/);
    if(m)id=m[0];
    if(!id){var f=fold(q);
      for(var i=0;i<opts.length;i++){
        if(opts[i].folded.indexOf(f)>=0){id=opts[i].id;break}}}
    var el=id&&doc.getElementById("p"+id);
    if(!el){note.textContent="No person “"+q+"” in this table.";return}
    note.textContent="";
    if(location.hash!=="#p"+id)location.hash="#p"+id;
    el.scrollIntoView({inline:"start",block:"center",
      behavior:matchMedia("(prefers-reduced-motion:no-preference)").matches
        ?"smooth":"auto"});
  });
  /* WCAG 2.1.4: the bare "/" shortcut is active only while focus is inside
     the plate figure -- the component it serves -- never page-wide. */
  var plateEl=$(".plate");
  if(plateEl)plateEl.addEventListener("keydown",function(e){
    if(e.key==="/"&&!e.altKey&&!e.ctrlKey&&!e.metaKey){
      e.preventDefault();input.focus();input.select();
    }
  });
  input.addEventListener("keydown",function(e){
    if(e.key==="Escape")input.blur();
  });
}

/* fragment insurance: a #r{n} link must open the register's disclosure, and
   hash navigation dismisses the person card. */
function openDetailsFor(hash){
  if(!hash||hash.length<2)return;
  var el=doc.getElementById(hash.slice(1));
  if(el&&el.closest){var d=el.closest("details");
    /* If we had to open the disclosure ourselves, the browser's own fragment
       scroll already missed (the target was display:none) -- finish the jump. */
    if(d&&!d.open){d.open=true;el.scrollIntoView({block:"center"})}}
}
addEventListener("hashchange",function(){
  openDetailsFor(location.hash);
  if(popoverOK){try{card.hidePopover()}catch(e){}}
  if(navFromCard){
    navFromCard=false;
    var el=doc.getElementById(location.hash.slice(1));
    var na=el&&el.querySelector?el.querySelector("a.num"):null;
    if(na)na.focus({preventScroll:true});
  }
});
openDetailsFor(location.hash);

/* copy citation */
var citeText=$("#cite-text"),copyMount=$("#copy-mount");
if(citeText&&copyMount&&navigator.clipboard){
  copyMount.insertAdjacentHTML("beforeend",
    '<button class="copy-btn" data-action="copycite" aria-live="polite">Copy citation</button>');
}

/* person card: filled by cloning the register entry -- single source of
   truth. Without popover support the number stays a plain working anchor. */
var card=$("#pcard"),CANON=root.getAttribute("data-canonical")||"",
    lastInvoker=null,anchoredEl=null,navFromCard=false,
    popoverOK=!!card&&("showPopover" in HTMLElement.prototype),
    anchorsOK=typeof CSS!=="undefined"&&CSS.supports&&
      CSS.supports("anchor-name","--pc");
if(popoverOK){
  card.hidden=false;
  card.addEventListener("toggle",function(e){
    /* preventScroll: closing via a relation link must not yank the plate
       back to the invoker -- the reader is on their way somewhere else. */
    if(e.newState==="closed"&&lastInvoker){
      lastInvoker.focus({preventScroll:true});lastInvoker=null}});
}
function openCard(a){
  var id=(a.getAttribute("href")||"").slice(2);
  var reg=doc.getElementById("r"+id);
  if(!reg)return false;
  card.innerHTML="";
  var body=doc.createElement("div");
  body.className="pcard-body";
  body.innerHTML=reg.innerHTML;
  var line=body.querySelector(".reg-line");if(line)line.id="pcard-t";
  card.appendChild(body);
  var act=doc.createElement("p");act.className="pcard-actions";
  var inner='<a href="#r'+id+'">Open register entry</a>';
  if(navigator.clipboard&&CANON)
    inner='<button data-action="copylink" data-id="'+id+'" aria-live="polite">Copy link</button> '+inner;
  act.innerHTML=inner;card.appendChild(act);
  if(anchoredEl)anchoredEl.style.removeProperty("anchor-name");
  anchoredEl=a;lastInvoker=a;
  if(anchorsOK)a.style.setProperty("anchor-name","--pc");
  card.style.cssText="";
  card.showPopover();
  if(!anchorsOK&&!matchMedia("(max-width:640px)").matches){
    var r=a.getBoundingClientRect(),t=r.bottom+4,l=r.left;
    if(t+card.offsetHeight+8>innerHeight)t=Math.max(8,r.top-card.offsetHeight-4);
    if(l+card.offsetWidth+8>innerWidth)l=Math.max(8,innerWidth-card.offsetWidth-8);
    card.style.inset="auto";card.style.top=t+"px";card.style.left=l+"px";
  }
  card.focus();
  return true;
}

/* one delegated click listener for every control */
doc.addEventListener("click",function(e){
  var t=e.target&&e.target.closest?e.target.closest("[data-action],a.num,#pcard a"):null;
  if(!t)return;
  var act=t.dataset?t.dataset.action:"";
  if(act==="theme"){cycleTheme();return}
  if(act==="scale"){store("lg-scale",t.dataset.v);applyScale(t.dataset.v);return}
  if(act==="copycite"&&citeText){
    navigator.clipboard.writeText(citeText.textContent.replace(/\s+/g," ").trim())
      .then(function(){flip(t,"Copied")})
      .catch(function(){flip(t,"Copy failed")});return}
  if(act==="copylink"){
    navigator.clipboard.writeText(CANON+"#p"+t.dataset.id)
      .then(function(){flip(t,"Copied")})
      .catch(function(){flip(t,"Copy failed")});return}
  /* a hash link inside the card: close toward the target, never back to the
     invoker; when the hash will not change, no hashchange fires, so finish
     the jump here. */
  if(popoverOK&&t.tagName==="A"&&t.closest("#pcard")){
    var h=t.getAttribute("href")||"";
    if(h.charAt(0)==="#"){
      lastInvoker=null;navFromCard=true;
      try{card.hidePopover()}catch(err){}
      if(h===location.hash){
        navFromCard=false;
        var same=doc.getElementById(h.slice(1));
        if(same){same.scrollIntoView({inline:"start",block:"center"});
          var na=same.querySelector("a.num");if(na)na.focus({preventScroll:true})}
        e.preventDefault();
      }
    }
    return;
  }
  if(popoverOK&&t.matches&&t.matches("a.num")&&t.closest(".sheet")){
    /* a modified click asks for the browser's own behavior (new tab etc.) */
    if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    if(openCard(t))e.preventDefault();
  }
});
})();""")


def masthead_html(tables, current_slug, prefix, home):
    """
    The sticky site bar -- the guaranteed carrier of identity and the way home
    2800px deep in the page. `tables` is [(numeral, slug), ...]; `prefix`
    starts every table link ("../" on a published chart page, "" on the
    landing page, the absolute site URL in the private build); `home` is the
    wordmark's href, or None on the landing page, which names itself.
    """
    if home:
        mark = f'<a class="wordmark" href="{home}">Laguna Genealogies</a>'
    else:
        mark = ('<span class="wordmark" aria-current="page">'
                'Laguna Genealogies</span>')
    links = " &middot; ".join(
        f'<a href="{prefix}{slug}/"'
        + (' aria-current="page"' if slug == current_slug else "")
        + f">{numeral}</a>"
        for numeral, slug in tables)
    return f"""<header class="masthead">
  {mark}
  <nav aria-label="Tables">Tables: {links}</nav>
  <span class="mast-right">
    <a class="mast-link" href="{REPO}">Source</a>
    <button id="theme" class="mast-btn" data-action="theme" hidden>Theme: Auto</button>
  </span>
</header>"""


def ruler_html(spec, n_gens):
    """
    The generation ruler: a column-header row that pans with the plate. Sized
    from the same --col/--stub/--sheet-pad tokens as the grid, so alignment is
    exact by construction. Decorative to AT (the chart states its generation
    count in the region label), hence aria-hidden.
    """
    chip = f"{spec['plate']} &middot; Genealogy {spec['numeral']}"
    gens = "".join(f'<span class="gen">Gen. {i}</span>'
                   for i in range(1, n_gens + 1))
    return ('<div class="ruler" aria-hidden="true">'
            f'<span class="ruler-chipslot"><span class="ruler-chip">{chip}</span></span>'
            f"{gens}</div>")


def key_html():
    """
    The editor's key, always visible between title page and plate. Specimens
    reuse the real chart classes so the key can never drift from the chart's
    styling; explanatory words are new UI text and speak in the UI stack.
    No specimen may use a glyph outside the font subset, and no key item may
    carry class="eng" or class="census" -- the leak grep matches those.
    """
    items = [
        ('<span class="num">7.</span>', "person number — a link; select for details"),
        ('<span class="plus">+</span>', "spouse, on the line below"),
        ('<span class="sex">F. M.</span>', "sex as printed"),
        ('<span class="blank">———</span>', "no name recorded"),
        ('<span class="clan">Sun</span>', "clan — matrilineal"),
        ('<span class="vital">d. 1908.</span>', "age or vital note, as printed"),
        ('<span class="key-bracket"></span>', "sibling group, hung on the mother's line"),
        ('<span class="key-lead"></span>', "descent — the leader rule"),
    ]
    spans = "".join(
        f'<span class="k">{specimen} <span class="k-label">{esc(label)}</span></span>'
        for specimen, label in items)
    return f'<section class="key" aria-label="Key to the chart">{spans}</section>'


def datalist_html(persons, drawn):
    """Finder suggestions: number, printed name, clan. Baseline fields only.
    Persons not drawn on the chart (unreachable from the founding couples --
    a reported data condition) are omitted: the finder cannot jump to them."""
    opts = []
    for pid in sorted(persons):
        if pid not in drawn:
            continue
        p = persons[pid]
        nm = p["name_as_printed"] or "———"
        if p["alt_name"]:
            nm += f" ({p['alt_name']})"
        label = f"{pid} · {nm}" + (f" · {p['clan']}" if p["clan"] else "")
        opts.append(f'<option value="{pid}">{esc(label)}</option>')
    return '<datalist id="persons-list">' + "".join(opts) + "</datalist>"


def register_html(persons, unions, ku, km, drawn):
    """
    The Register of persons: a generated index, one entry per person in plate
    order, with parents, spouses and children as #p{n} links. It is the no-JS
    search, the no-JS person card, and the single source the person-card
    popover clones -- never a second truth.

    Research keys are blanked on a copy before person_line runs, so the
    English-name and census chips can never render here, in either build.
    A person the chart did not draw (`drawn` is Chart.seen) still gets an
    entry -- the register records everyone -- but no #p link, because its
    target would not exist.
    """
    parents = {}
    for u in unions:
        for k in ku.get(u["union_id"], []):
            parents[k] = (u["wife"], u["husband"])
    for m, kids in km.items():
        for k in kids:
            parents[k] = (m, 0)

    spouses, children = {}, {}
    for u in unions:
        w, h = u["wife"], u["husband"]
        if w and h:
            spouses.setdefault(w, []).append(h)
            spouses.setdefault(h, []).append(w)
        kids = ku.get(u["union_id"], [])
        if kids:
            if w:
                children.setdefault(w, []).append((h, kids))
            if h:
                children.setdefault(h, []).append((w, kids))
    for m, kids in km.items():
        children.setdefault(m, []).append((0, kids))

    def rel_link(pid):
        p = persons[pid]
        if p["name_as_printed"]:
            nm = f'<span class="name" lang="kjq">{esc(p["name_as_printed"])}</span>'
        else:
            nm = '<span class="blank">———</span>'
        if pid not in drawn:
            return f'<span class="num">{pid}</span> {nm}'
        return f'<a href="#p{pid}"><span class="num">{pid}</span> {nm}</a>'

    def rel_row(label, links):
        return (f'<div class="reg-rel"><span class="rel-l">{label}</span> '
                + " &middot; ".join(links) + "</div>")

    items = []
    for pid in sorted(persons):
        p = dict(persons[pid])
        p.update({k: "" for k in RESEARCH_KEYS})
        rows = []
        pm, pf = parents.get(pid, (0, 0))
        par = [rel_link(x) for x in (pm, pf) if x]
        if par:
            rows.append(rel_row("Parents", par))
        sp = [rel_link(x) for x in spouses.get(pid, [])]
        if sp:
            rows.append(rel_row("Spouse" if len(sp) == 1 else "Spouses", sp))
        groups = children.get(pid, [])
        for other, kids in groups:
            if not other:
                label = "Children (father not recorded)"
            elif len(groups) > 1:
                label = f"Children (with {other})"
            else:
                label = "Children"
            rows.append(rel_row(label, [rel_link(k) for k in kids]))
        xr = persons[pid]["cross_ref"]
        if xr:
            for part in xr.split("|"):
                rows.append('<div class="reg-rel"><em>'
                            + linkify_xref(esc(part.strip()), persons)
                            + "</em></div>")
        line = person_line(p, False, set())
        if pid not in drawn:
            # No chart line to link to: demote the number anchor to a span.
            line = line.replace(f'<a class="num" href="#p{pid}">',
                                '<span class="num">', 1).replace("</a>", "</span>", 1)
        items.append(f'<li class="reg" id="r{pid}">'
                     f'<div class="reg-line">{line}</div>'
                     + "".join(rows) + "</li>")

    return f"""<section class="apparatus-register" id="register-sec" aria-labelledby="reg-h">
  <h2 id="reg-h">Register of persons</h2>
  <p class="reg-note">Editorial apparatus, generated from the transcription.
     Numbers link back to the chart; the plate itself is unchanged.</p>
  <details id="register" class="register-d">
    <summary>All {len(persons)} entries</summary>
    <ol class="reg-list">{"".join(items)}</ol>
  </details>
</section>"""


def cite_html(spec, today):
    """The recommended two-part citation, generated so it can never go stale."""
    canonical = f"{SITE}/{spec['slug']}/"
    root_id = spec["roots"][0]
    return f"""<h2>Citation</h2>
  <blockquote class="cite-block" id="cite-text">
    <p>Elsie Clews Parsons, &ldquo;Laguna Genealogies,&rdquo;
       <em>Anthropological Papers of the American Museum of Natural History</em>,
       vol.&nbsp;19, pt.&nbsp;5 (1923), pp.&nbsp;133&ndash;292, {spec['plate']}.</p>
    <p>Digital transcription: {esc(AUTHOR)},
       <em>Laguna Genealogies: A Digital Edition</em>, {today.year},
       {canonical}. CC&nbsp;BY&nbsp;4.0.</p>
  </blockquote>
  <p>To cite one person&rsquo;s line, use its number&rsquo;s link:
     <a href="#p{root_id}">{canonical}#p{root_id}</a> is person {root_id}.<span id="copy-mount"></span></p>"""


def jsonld_chart(spec, description, today):
    """Bibliographic structured data -- public builds only, counts computed."""
    canonical = f"{SITE}/{spec['slug']}/"
    data = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": (f"Genealogy {spec['numeral']} — Parsons 1923, Laguna Pueblo: "
                 "a digital transcription"),
        "description": description,
        "url": canonical,
        "creator": {"@type": "Person", "name": AUTHOR},
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isBasedOn": {"@type": "CreativeWork", "name": "Laguna Genealogies",
                      "author": {"@type": "Person", "name": "Elsie Clews Parsons"},
                      "datePublished": "1923"},
        "isPartOf": {"@type": "WebSite",
                     "name": "Laguna Genealogies: A Digital Edition",
                     "url": SITE + "/"},
        "dateModified": today.isoformat(),
    }
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False) + "</script>")


def jsonld_site(built, today):
    data = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Laguna Genealogies: A Digital Edition",
        "url": SITE + "/",
        "description": ("Digital editions of the genealogical plates from "
                        "Elsie Clews Parsons, Laguna Genealogies (1923)."),
        "creator": {"@type": "Person", "name": AUTHOR},
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "dateModified": today.isoformat(),
        "hasPart": [
            {"@type": "Dataset",
             "name": f"Genealogy {spec['numeral']} — Parsons 1923",
             "url": f"{SITE}/{spec['slug']}/"}
            for spec, _ in built
        ],
    }
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False) + "</script>")


def build_doc(spec, description, gens, n_gens, trees, status, public, today,
              stats, persons, unions, ku, km, drawn):
    """The full HTML document. Identical in both modes apart from the footer,
    the meta, and the masthead's link base (the private build lives outside
    the site tree, so its links are absolute)."""
    canonical = f"{SITE}/{spec['slug']}/"
    tables = [(TABLES[k]["numeral"], TABLES[k]["slug"]) for k in sorted(TABLES)]
    if public:
        head_extra = f"""<link rel="canonical" href="{canonical}">
<meta name="description" content="{esc(description)}">
<meta name="author" content="{esc(AUTHOR)}">
<meta property="og:type" content="article">
<meta property="og:title" content="Genealogy {spec['numeral']} &mdash; Parsons 1923, Laguna Pueblo">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Laguna Genealogies: A Digital Edition">
<meta name="twitter:card" content="summary">
{jsonld_chart(spec, description, today)}"""
        provenance = f"""
  <h2>Provenance</h2>
  <ul>
    <li>This is a transcription of a plate in an existing published source. The
        1923 publication is in the public domain in the United States.</li>
    <li>The transcription, encoding and layout are by {esc(AUTHOR)}, released under
        <a href="https://creativecommons.org/licenses/by/4.0/">CC&nbsp;BY&nbsp;4.0</a>.
        Please cite both this edition and Parsons.</li>
    <li>Readings can be checked against the source scan, which is kept in the
        <a href="{REPO}">project repository</a>
        together with the data and the code that drew this page.</li>
    <li>Names are set in a subset of SIL Gentium, embedded in this page under the
        <a href="../fonts/OFL.txt">SIL Open Font License</a>, so the phonetic
        diacritics render the same everywhere.</li>
  </ul>"""
        mast = masthead_html(tables, spec["slug"], "../", "../")
        canon_attr = f' data-canonical="{canonical}"'
    else:
        head_extra = '<meta name="robots" content="noindex,nofollow">'
        provenance = """
  <h2>This is the private build</h2>
  <ul>
    <li>Generated from <code>data/parsons_genealogy_I.xlsx</code>, so it may show
        English names and census matches. It is git-ignored and must not be published.</li>
    <li>Edit the workbook, then re-run <code>python3 scripts/make_chart.py</code>.</li>
    <li>The public page is built separately with <code>--public</code>, from
        <code>scripts/transcription.py</code>, which has no research columns.</li>
  </ul>"""
        mast = masthead_html(tables, spec["slug"], f"{SITE}/", f"{SITE}/")
        canon_attr = ""

    imprint = (f"{stats['persons']} individuals &middot; {stats['gens']} generations "
               f"&middot; {stats['unions']} marriages &middot; {stats['links']} "
               "parent&ndash;child links")

    return f"""<!doctype html>
<html lang="en"{canon_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Genealogy {spec['numeral']} &mdash; Parsons 1923, Laguna Pueblo{"" if public else " (private build)"}</title>
<meta name="theme-color" content="#FAF8F4" media="(prefers-color-scheme:light)">
<meta name="theme-color" content="#191713" media="(prefers-color-scheme:dark)">
<link rel="icon" href="{FAVICON}">
{head_extra}
<style>{font_css()}{geom_css()}{CSS}</style>
{THEME_SNIPPET}
</head>
<body>
<a class="skip" href="#plate">Skip to chart</a>
<a class="skip" href="#register-sec">Skip past chart to the register</a>
{mast}
<div class="titlepage">
  <div class="plate-label">{spec['plate']}</div>
  <h1>GENEALOGY {spec['numeral']}</h1>
  <div class="rule-double"></div>
  <div class="cite">
    {CITE}
  </div>
  <p class="imprint">{imprint}</p>
</div>
{key_html()}
<main>
<div class="plate-bar">
  <span class="plate-cap">Plate &mdash; after the 1923 foldout; layout preserved</span>
  <span class="plate-tools">
    <search><form id="find" hidden>
      <label class="visually-hidden" for="find-q">Find a person by number or name</label>
      <input id="find-q" list="persons-list" autocomplete="off"
             placeholder="Find: number or name ( / )" enterkeyhint="go">
      <span id="find-note" role="status" class="find-note"></span>
    </form></search>
    <span id="scale-mount"></span>
  </span>
</div>
{datalist_html(persons, drawn)}
<figure class="plate">
  <div class="scroll-shell">
    <div class="scroll" id="plate" tabindex="0" role="region"
         aria-label="Genealogy {spec['numeral']} chart, {gens} generations, scrollable horizontally; use the arrow keys to scroll &mdash; person numbers are links">
      <div class="plate-zoom" style="--print-zoom:{print_zoom(n_gens)}">
        {ruler_html(spec, n_gens)}
        <div class="sheet">{trees}</div>
      </div>
    </div>
  </div>
  <figcaption class="plate-caption">Redrawn from the plate as printed; brackets,
    columns and leader rules reproduce the 1923 layout.<span class="pan-hint">
    Scroll sideways to follow the later generations &mdash; person numbers are
    links.</span></figcaption>
</figure>
</main>
{register_html(persons, unions, ku, km, drawn)}
<footer id="apparatus">
  <h2>The record</h2>
  <ul>{"".join(status)}</ul>
  <h2>Editorial notes</h2>
  <ul>{READING_COMMON.format(couples=spec["couples"])}{spec["notes"]}{APPARATUS_NOTE}</ul>{provenance}
  {cite_html(spec, today)}
  <h2>Navigating this chart</h2>
  <ul>{navigating_html(spec)}</ul>
  <p class="updated">Last updated
     <time datetime="{today.isoformat()}">{today.strftime("%-d %B %Y")}</time>.
     {f'<span class="print-url">Published at {canonical}</span>' if public else ''}</p>
</footer>
<div id="pcard" class="pcard" popover role="dialog" aria-labelledby="pcard-t" tabindex="-1" hidden></div>
<script>{UI_JS}</script>
</body>
</html>
"""


LANDING_CSS_EXTRA = """
.contents{max-width:var(--measure);margin:0 auto;padding:var(--s4) var(--s5)}
.contents ol{list-style:none;margin:0;padding:0}
.contents li{border-block-end:1px solid var(--rule-faint)}
.contents li:first-child{border-block-start:1px solid var(--rule-faint)}
.contents a{display:block;padding:var(--s4) var(--s2);text-decoration:none;
  color:inherit}
.c-title{display:block;font-size:1.0625rem;color:var(--ink)}
.contents a:hover .c-title{color:var(--accent)}
.contents a:focus-visible .c-title{color:var(--accent)}
.c-stats{display:block;font-size:.8125rem;color:var(--muted);
  margin-block-start:var(--s1)}
.contents .pending{padding:var(--s4) var(--s2)}
.contents .pending .c-title{color:var(--muted)}
.pending-tag{font-style:italic;font-size:.9375rem}
.prose{max-width:var(--measure);margin:0 auto;
  padding:var(--s6) var(--s5) var(--s7);font-size:.875rem;line-height:1.7;
  color:var(--muted);text-wrap:pretty}
.prose h2{margin:var(--s6) 0 var(--s3)}
.prose a{color:var(--accent)}
"""


def write_site(today, built):
    """
    The files around the chart: landing page, robots.txt, sitemap.xml, .nojekyll,
    and the font licence. All generated, so none of docs/ is ever hand-edited.
    """
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "fonts").mkdir(exist_ok=True)

    # .nojekyll stops Pages running Jekyll, which would otherwise ignore any
    # file or folder whose name begins with an underscore.
    (DOCS / ".nojekyll").write_text("")

    licence = FONT_DIR / "OFL.txt"
    if licence.exists():
        shutil.copyfile(licence, DOCS / "fonts" / "OFL.txt")

    (DOCS / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8"
    )

    stamp = today.isoformat()
    paths = ["/"] + [f"/{spec['slug']}/" for spec, _ in built]
    urls = "".join(
        f"\n  <url><loc>{SITE}{path}</loc><lastmod>{stamp}</lastmod></url>"
        for path in paths
    )
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )

    verify = (f'<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">\n'
              if GOOGLE_SITE_VERIFICATION else "")

    rows = []
    for spec, st in built:
        stats_line = (f'{st["persons"]} individuals &middot; {st["gens"]} '
                      f'generations &middot; {st["unions"]} marriages &middot; '
                      f'{st["links"]} parent&ndash;child links')
        rows.append(
            f'    <li><a href="{spec["slug"]}/">\n'
            f'      <span class="c-title">{spec["plate"]} &mdash; Genealogy {spec["numeral"]}</span>\n'
            f'      <span class="c-stats">{stats_line}</span>\n'
            '    </a></li>\n')
    for i, (plate, name, note) in enumerate(PENDING):
        # The id exists so a cross-reference can point here the day the table
        # ships; nothing links to it yet -- a link must not promise content.
        m = re.search(r"\d+", plate)
        n = m.group() if m else f"x{i + 1}"
        rows.append(
            f'    <li class="pending" id="pending-{n}">\n'
            f'      <span class="c-title">{plate} &mdash; {name} '
            '<span class="pending-tag">&middot; in preparation</span></span>\n'
            f'      <span class="c-stats">{note}</span>\n'
            '    </li>\n')
    rows = "".join(rows)

    tables = [(TABLES[k]["numeral"], TABLES[k]["slug"]) for k in sorted(TABLES)]
    landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Laguna Genealogies &mdash; A Digital Edition of Parsons 1923</title>
<link rel="canonical" href="{SITE}/">
<meta name="description" content="Digital editions of the genealogical plates from Elsie Clews Parsons, Laguna Genealogies (1923), transcribed and encoded from the original.">
<meta name="author" content="{esc(AUTHOR)}">
<meta property="og:type" content="website">
<meta property="og:title" content="Laguna Genealogies: A Digital Edition">
<meta property="og:description" content="Digital editions of the genealogical plates from Elsie Clews Parsons, Laguna Genealogies (1923).">
<meta property="og:url" content="{SITE}/">
<meta name="theme-color" content="#FAF8F4" media="(prefers-color-scheme:light)">
<meta name="theme-color" content="#191713" media="(prefers-color-scheme:dark)">
<link rel="icon" href="{FAVICON}">
{verify}{jsonld_site(built, today)}
<style>{font_css()}{geom_css()}{CSS}{LANDING_CSS_EXTRA}</style>
{THEME_SNIPPET}
</head>
<body>
{masthead_html(tables, None, "", None)}
<div class="titlepage">
  <div class="plate-label">A Digital Edition</div>
  <h1>LAGUNA GENEALOGIES</h1>
  <div class="rule-double"></div>
  <div class="cite">
    {CITE}
  </div>
</div>
<main>
<nav class="contents" aria-label="Contents">
  <ol>
{rows}  </ol>
</nav>
</main>
<div class="prose">
  <h2>What this is</h2>
  <p>Elsie Clews Parsons published a set of foldout genealogical plates with
     <em>Laguna Genealogies</em> in 1923. They are dense, hand-set, and hard to read
     from a scan. This edition transcribes them character by character &mdash; including
     the Americanist phonetic diacritics &mdash; and redraws them as text you can search,
     copy, and check against the original.</p>
  <p>Nothing has been corrected, normalised or filled in. Where the plate contains a
     misprint it is reproduced and annotated rather than silently fixed; where Parsons
     recorded no name, the entry stays blank.</p>

  <h2>Provenance and use</h2>
  <p>This is Laguna Pueblo material. Parsons's Laguna fieldwork is itself contested:
     she published information that members of the community regarded as restricted.
     This edition is a transcription of an already published source and adds no new
     information about the community. It is offered as a finding aid for the printed
     record.</p>
  <p>The 1923 publication is in the public domain in the United States. The
     transcription, encoding and layout are by {esc(AUTHOR)} and are released under
     <a href="https://creativecommons.org/licenses/by/4.0/">CC&nbsp;BY&nbsp;4.0</a>.</p>
  <p>Data, source scan and the code that generated these pages are in the
     <a href="{REPO}">project repository</a>.
     Corrections are welcome and are recorded as dated commits, so the edition carries
     its own revision history.</p>
  <p class="updated">Last updated
     <time datetime="{stamp}">{today.strftime("%-d %B %Y")}</time>.</p>
</div>
<script>{LANDING_JS}</script>
</body>
</html>
"""
    (DOCS / "index.html").write_text(landing, encoding="utf-8")
    print(f"  wrote docs/index.html, robots.txt, sitemap.xml, .nojekyll, fonts/OFL.txt")


def build_table(spec, public, today):
    """Build one table. Returns (doc, stats) so the caller can assemble the site."""
    if public:
        persons, unions, ku, km = load_baseline(spec)
        out = DOCS / spec["slug"] / "index.html"
    else:
        if not XLSX.exists():
            print(f"missing {XLSX}; run build_workbook.py first")
            return None, None
        persons, unions, ku, km = load()
        out = OUT

    chart = Chart(persons, unions, ku, km)
    trees = "".join(f'<div class="tree">{chart.render(r)[0]}</div>' for r in spec["roots"])

    missing = sorted(set(persons) - chart.seen)
    links = sum(len(v) for v in ku.values()) + sum(len(v) for v in km.values())
    n_gens = max((int(p["generation"]) for p in persons.values() if p["generation"]),
                 default=0)
    gens = NUMBER_WORDS.get(n_gens, str(n_gens))

    status = [f"<li>{len(persons)} individuals across {n_gens} generation columns; "
              f"{len(unions)} marriages; {links} "
              "parent&ndash;child links.</li>"]
    if public:
        status.append("<li>Transcribed from the plate and verified against it. Clan "
                      "descent is matrilineal, which gives every bracket an independent "
                      f"check; all {len(unions)} marriages pass it.</li>")
    else:
        filled = sorted(p["id"] for p in persons.values() if p["english_name"])
        census_filled = sorted(p["id"] for p in persons.values() if p["census_name"])
        if filled:
            status.append("<li>English names filled in for: "
                          + ", ".join(str(i) for i in filled) + ".</li>")
        else:
            status.append("<li>No English names filled in yet. Add them in the "
                          "<code>english_name</code> column of PERSONS and re-run this script.</li>")
        if census_filled:
            status.append("<li>Census matches recorded for: "
                          + ", ".join(str(i) for i in census_filled) + ".</li>")
    if missing:
        status.append(f"<li><strong>Not drawn:</strong> {missing} &mdash; these ids are in "
                      "PERSONS but reachable from neither founding couple.</li>")

    stats = {"persons": len(persons), "unions": len(unions),
             "links": links, "gens": gens}
    doc = build_doc(spec, describe(spec, len(persons), n_gens), gens, n_gens,
                    trees, status, public, today, stats, persons, unions, ku, km,
                    chart.seen)

    # Every drawn person must carry exactly one citable id="p{n}" -- its first
    # printed occurrence. A duplicate would silently break every deep link to
    # the later occurrence, so it aborts the build like the privacy grep does.
    ids = re.findall(r'id="(p\d+)"', doc)
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        raise SystemExit(f"ABORTED: duplicate person anchors {dupes} in {out.name}")
    if set(ids) != {f"p{i}" for i in chart.seen}:
        raise SystemExit(f"ABORTED: person anchors do not match drawn persons in {out.name}")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    print(f"  {len(chart.seen)} of {len(persons)} persons drawn")
    if missing:
        print(f"  NOT DRAWN: {missing}")

    if public:
        # A published build that leaked a research chip would be the one failure
        # that cannot be walked back, so check the bytes rather than trusting the
        # data path that produced them.
        for marker in ('class="eng"', 'class="census"'):
            if marker in doc:
                out.unlink()
                raise SystemExit(f"ABORTED: {marker} found in {out.name}; output deleted")
        print("  no english/census chips in output")

    return doc, stats


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    ap.add_argument("--public", action="store_true",
                    help="build the published page(s) from the 1923 baseline into docs/")
    ap.add_argument("--table", default="i", choices=sorted(TABLES),
                    help="which plate to build (default: i)")
    args = ap.parse_args()
    today = dt.date.today()

    if not args.public:
        # The workbook holds one table, so the private build is always that one.
        doc, _ = build_table(TABLES[args.table], public=False, today=today)
        return 0 if doc else 1

    # Publishing rebuilds every table, so the landing page, sitemap and the
    # per-table counts can never describe a stale set.
    built = []
    for key in sorted(TABLES):
        spec = TABLES[key]
        _, stats = build_table(spec, public=True, today=today)
        built.append((spec, stats))
    write_site(today=today, built=built)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
