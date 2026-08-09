"""
Verbatim transcription of Table 1, "Genealogy I", from
Elsie Clews Parsons, "Laguna Genealogies",
Anthropological Papers of the American Museum of Natural History, vol. 19 (1923).

Source image: sources/parsons-1923-table-1.jpg (16172 x 11798 px)

This file is the immutable 1923 baseline. Do NOT add research data here --
add it in the workbook (parsons_genealogy_I.xlsx), which is the editable layer.
Rebuilding the workbook from this file would discard your edits.

Orthography (Americanist transcription as used by Parsons):
    'ʼ'  U+02BC  glottal stop / raised apostrophe, as printed
    '˙'  U+02D9  raised dot (aspiration / length)
    ă ĕ ĭ ŭ Ă     breve
    ᶦ ᵘ ᵃ         superscript letters
    ñ             as printed in "Zuñi"
"""

# ---------------------------------------------------------------------------
# PERSONS
# id, generation, sex, name_as_printed, alt_name, age, clan, vital_note,
# origin, cross_ref, plate_note
# ---------------------------------------------------------------------------
PERSONS = [
    (1,  1, "F", "Lupi",              "",        "",   "Sun",   "",     "Navaho", "", ""),
    (2,  1, "M", "",                  "",        "",   "Lizard", "",    "",       "", "name left blank in the plate"),
    (3,  2, "F", "Nayowʼ˙ăitsa",      "",        "",   "Sun",   "",     "",       "", ""),
    (4,  2, "M", "Mariano",           "",        "",   "Lizard", "",    "",       "", ""),
    (5,  3, "F", "Heʼyăis˙itsʼă",     "",        "",   "Sun",   "",     "",       "", ""),
    (6,  3, "M", "Kʼotsima",          "",        "",   "Oak",   "",     "",       "", ""),
    (7,  3, "F", "Dziwaiʼᶦdyitsʼa",   "",        "",   "Sun",   "d. 1908", "",    "", ""),
    (8,  3, "M", "Yu˙si",             "",        "55", "Water", "",     "",       "", ""),
    (9,  3, "F", "Dyai˙ʼᶦs˙itsʼă",    "",        "60", "Sun",   "",     "",       "", ""),
    (10, 3, "M", "Shʼauʼs˙imăiʼ",     "",        "",   "Parrot", "d.",  "",       "", ""),
    (11, 3, "M", "Kyʼĕauʼd˙yăŭăi",    "",        "",   "Sun",   "d.",   "",       "", ""),
    (12, 3, "F", "Dzaiʼᶦtyʼi",        "",        "50", "Water", "",     "",
     "For second husband and offspring see Gen. II, 21, 74", ""),
    (13, 4, "F", "Juana",             "",        "25", "Sun",   "",     "",       "", ""),
    (14, 4, "F", "Ais",               "",        "19", "Sun",   "",     "",       "", ""),
    (15, 4, "F", "Kʼă˙ʼwină",         "",        "18", "Sun",   "",     "",       "", ""),
    (16, 4, "M", "G˙yiʼmi",           "",        "45", "Sun",   "",     "",       "", ""),
    (17, 4, "F", "Nămăiʼ",            "",        "40", "Oak",   "",     "",       "", ""),
    (18, 4, "M", "Kowăuʼsh˙dyiwă",    "",        "42", "Sun",   "",     "",       "", ""),
    (19, 4, "F", "Haiʼtyʼʼi˙măiʼ",    "Juana",   "",   "Parrot", "",    "",       "", "alternate name printed in parentheses below"),
    (20, 4, "M", "Kʼuʼna˙shᵘ",        "",        "",   "Sun",   "",     "",       "", ""),
    (21, 4, "F", "Shayaʼai",          "",        "",   "Sun",   "",     "",       "", ""),
    (22, 4, "M", "Dziraiʼᶦtyʼi",      "",        "",   "Sun",   "",     "",       "", ""),
    (23, 4, "F", "Dziʼs˙dyuwi",       "",        "",   "Bear",  "",     "",       "", ""),
    (24, 4, "M", "Dzauwaiʼd˙yăi",     "",        "23", "Water", "",     "",       "", ""),
    (25, 4, "M", "Kaaiʼdziăi˙s˙iwă",  "",        "",   "Water", "d. 1913", "",    "", ""),
    (26, 4, "F", "Gawaiʼy˙unăiʼ",     "",        "17", "Water", "",     "",       "", ""),
    (27, 4, "F", "Kowaiʼd˙yuitsʼa",   "",        "15", "Water", "",     "",       "", ""),
    (28, 5, "F", "Goʼisdyuitsʼă",     "",        "4",  "Sun",   "",     "",       "", ""),
    (29, 5, "M", "",                  "",        "",   "Sun",   "d. 1917, aged 2", "", "", "name left blank in the plate"),
    (30, 5, "F", "",                  "",        "",   "Sun",   "b. Nov. 20, 1917", "", "", "name left blank in the plate"),
    (31, 5, "F", "Ko˙ri",             "",        "20", "Oak",   "",     "",       "", ""),
    (32, 5, "M", "Tsᶦgaiʼs˙iwăʼ",     "",        "19", "Oak",   "",     "",       "", ""),
    (33, 5, "F", "Kiwaʼd˙yuwi",       "",        "18", "Oak",   "",     "",       "", ""),
    (34, 5, "M", "Tsiʼd˙yimĕʼ",       "",        "16", "Oak",   "",     "",       "", ""),
    (35, 5, "F", "Sha˙tyʼi",          "",        "13", "Oak",   "",     "",       "", ""),
    (36, 5, "M", "Aiʼwanăi",          "",        "7",  "Oak",   "",     "",       "", ""),
    (37, 5, "M", "Dyăiʼtsdyămŭr",     "",        "5",  "Oak",   "",     "",       "", ""),
    (38, 5, "M", "Iyăiʼs˙dyiwă",      "",        "4",  "Oak",   "",     "",       "", ""),
    (39, 5, "M", "Shauʼd˙yiyĕ",       "",        "14", "Parrot", "",    "",       "", ""),
    (40, 5, "F", "Kăauʼshurtsʼa",     "",        "8",  "Parrot", "",    "",       "", ""),
    (41, 5, "M", "Onăiʼ",             "",        "7",  "Parrot", "",    "",       "", ""),
    (42, 5, "F", "Wamais˙ʼ",          "",        "6",  "Parrot", "",    "",       "", ""),
    (43, 5, "M", "Yoʼd˙yidyăiʼ",      "",        "5",  "Parrot", "",    "",       "", "age printed without a following period"),
    (44, 5, "M", "Hea˙ʼsh˙dyĭwă",     "",        "",   "Parrot", "d. 1917, aged 2", "", "", ""),
    (45, 5, "M", "Dziwaiʼisiro",      "",        "19", "Sun",   "",     "",       "", ""),
    (46, 5, "F", "Gauʼs˙dyuwe",       "",        "18", "Sun",   "",     "",       "", ""),
    (47, 5, "M", "Owi˙ʼd˙zĭraiʼ",     "",        "16", "Sun",   "",     "",       "", ""),
    (48, 5, "F", "Kuyăiʼd˙yid˙yuweʼ", "",        "14", "Sun",   "",     "",       "", ""),
    (49, 5, "F", "Yăaiʼdyid˙yuwi",    "",        "7",  "Sun",   "",     "",       "", ""),
    (50, 5, "F", "Ăʼwaid˙id˙yuwe",    "",        "6",  "Sun",   "",     "",       "", ""),
    (51, 5, "M", "Auʼy˙unăi",         "",        "2",  "Sun",   "",     "",       "", ""),
    (52, 5, "M", "Aʼud˙yăi",          "",        "4",  "Bear",  "",     "",       "", ""),
    (53, 5, "F", "Gaaiʼd˙yuitsʼa",    "",        "3",  "Bear",  "",     "",       "", ""),
    (54, 1, "F", "Chuetsa",           "",        "",   "Badger", "",    "Zuñi",   "", ""),
    (55, 1, "M", "Kʼausiro",          "Gauʼsh˙uro", "", "Eagle", "",    "Zuñi",   "",
     "two names braced together in the plate"),
    (56, 2, "M", "We˙ʼdyumă",         "",        "80", "Badger", "",    "",       "", ""),
    (57, 2, "F", "Tsʼa˙ʼsh˙umăi",     "",        "",   "Eagle", "d.",   "",       "", ""),
    (58, 2, "M", "Ka˙ʼyo˙",           "",        "",   "Badger", "",    "",       "", ""),
    (59, 2, "F", "",                  "",        "",   "Water", "",     "Navaho", "", "name left blank in the plate"),
    (60, 2, "F", "Gawaiʼidyid˙yu",    "",        "",   "Badger", "",    "",       "", ""),
    (61, 2, "M", "Ishŭrneai",         "Garsia",  "",   "Chaparral Cock", "", "",  "",
     "alternate name printed in parentheses below"),
    (62, 2, "F", "Siu˙ʼrositsʼă",     "Yu˙yaitsʼᵃ", "", "Badger", "",   "",       "",
     "two names braced together in the plate"),
    (63, 2, "M", "Wakaienishe",       "",        "",   "Water", "",     "",       "", ""),
    (64, 2, "F", "Waiaye",            "",        "",   "Badger", "",    "",       "", "number printed without a following period"),
    (65, 3, "M", "Tsiwaiʼᶦd˙yirăi",   "",        "",   "Eagle", "d.",   "",       "", ""),
    (66, 3, "F", "Tsikʼayăaiʼtsʼa",   "",        "",   "Eagle", "d.",   "",       "", ""),
    (67, 3, "M", "Shuwaiʼᶦri",        "",        "",   "Turkey", "",    "",
     "For second wife and offspring see below, 76, 90-3", ""),
    (68, 3, "F", "Kuyuʼd˙yuwe",       "",        "34", "Eagle", "",     "",       "", ""),
    (69, 3, "M", "Kʼawaiʼᶦshu",       "",        "",   "Sun",   "d. (?)", "",     "", ""),
    (70, 3, "M", "Wiyăiʼd˙yuă",       "",        "45", "Turkey", "",    "",       "", ""),
    (71, 3, "F", "Gaiyaiʼs˙dyaitsʼʼaʼ", "",      "",   "Water", "d.",   "",       "", ""),
    (72, 3, "M", "Stauutiye",         "",        "",   "Lizard", "d.",  "",       "", ""),
    (73, 3, "F", "Yo˙ʼs˙iro",         "",        "",   "Chaparral Cock", "d. 1914", "",
     "For first husband and descendants, see Gen. II, 158, 159, 160 | "
     "For second husband and descendant, see Gen. III, 154, 220",
     "name printed without a following period"),
    (74, 3, "M", "",                  "",        "",   "Badger", "",    "",       "", "name left blank in the plate"),
    (75, 3, "M", "",                  "",        "",   "Badger", "d.",  "",       "", "name left blank in the plate"),
    (76, 3, "F", "Dziwiʼd˙yăi",       "Lupi",    "33", "Badger", "",    "",       "", "alternate name printed in parentheses below"),
    (77, 3, "F", "Gaiʼsiro",          "",        "",   "Badger", "d.",  "",       "", ""),
    (78, 3, "F", "Tsa˙ʼtsʼiʼ",        "",        "",   "Badger", "d. in 1905", "", "", ""),
    (79, 3, "M", "Dziwishpirăiʼ",     "",        "70", "Parrot", "",    "",       "", ""),
    (80, 4, "M", "Shauʼm˙ăiʼ",        "",        "",   "Eagle", "",     "",       "", ""),
    (81, 4, "M", "",                  "",        "",   "Eagle", "",     "",       "", "name left blank in the plate"),
    (82, 4, "M", "",                  "",        "",   "Eagle", "d.",   "",       "", "name left blank in the plate"),
    (83, 4, "F", "Dzaaiʼtyiĕ",        "",        "5",  "Eagle", "",     "",       "", ""),
    (84, 4, "F", "Gaityʼiʼaitsʼă",    "",        "4",  "Eagle", "",     "",       "", ""),
    (85, 4, "F", "Dzawai˙g˙uitsʼă",   "",        "2",  "Eagle", "",     "",       "", ""),
    (86, 4, "F", "Go˙w˙aitsʼă",       "",        "",   "Water", "d. 1913, aged 18", "", "", ""),
    (87, 4, "F", "Go˙wai",            "",        "",   "Water", "d.",   "",       "", ""),
    (88, 4, "F", "Go˙w˙aid˙yuitsʼa",  "",        "17", "Water", "",     "",       "", ""),
    (89, 4, "F", "",                  "",        "",   "",      "d. in infancy", "", "",
     "name left blank and no clan given in the plate"),
    (90, 4, "F", "Heʼsa",             "Hazel",   "",   "Badger", "",    "",       "",
     "English name 'Hazel' printed in parentheses in the plate"),
    (91, 4, "F", "Dzăiyăiʼ",          "",        "",   "Badger", "",    "",       "", ""),
    (92, 4, "F", "Kăaiʼʼyunăiʼ",      "",        "",   "Badger", "",    "",       "", ""),
    (93, 4, "M", "Dziw˙aiʼs˙iwă",     "",        "",   "Badger", "",    "",       "", ""),
    (94, 4, "M", "Goa˙ʼs˙iro",        "",        "18", "Badger", "",    "",       "", ""),
    (95, 4, "F", "Gŭyaiʼtsʼă",        "",        "17", "Badger", "",    "",       "", ""),
    (96, 4, "F", "Juana",             "",        "7",  "Badger", "",    "",       "", ""),
    (97, 4, "F", "Shuʼmăĭ",           "",        "30", "Badger", "",    "",       "", ""),
    (98, 4, "M", "Dzaiʼʼg˙ai",        "",        "",   "Lizard", "",    "",       "", ""),
    (99, 4, "M", "Ho˙ʼpy˙di˙waʼ",     "",        "25", "Badger", "",    "",       "", ""),
    (100, 4, "F", "Dzaiʼsdyui",       "",        "21", "Badger", "",    "",       "", ""),
    (101, 4, "M", "",                 "",        "",   "",      "",     "Zuñi",   "",
     "printed as '— of Zuñi'; no clan given"),
    (102, 5, "F", "",                 "",        "5",  "Badger", "",    "",       "", "name left blank in the plate"),
    (103, 5, "F", "",                 "",        "1",  "Badger", "",    "",       "", "name left blank in the plate"),
    (104, 5, "M", "",                 "",        "4",  "Badger", "",    "",       "", "name left blank in the plate"),
]

# ---------------------------------------------------------------------------
# UNIONS  (each '+' line in the plate is a marriage)
# union_id, wife_id, husband_id, wife_marriage_order, husband_marriage_order, note
#   order = 1 unless the plate shows that person with more than one spouse
#   0 in an id field = spouse not shown on the plate
# ---------------------------------------------------------------------------
UNIONS = [
    ("U01",   1,   2, 1, 1, ""),
    ("U02",   3,   4, 1, 1, ""),
    ("U03",   5,   6, 1, 1, ""),
    ("U04",   7,   8, 1, 1, "8 has two wives on the plate: 7 and 73"),
    ("U05",   9,  10, 1, 1, ""),
    ("U06",  12,  11, 1, 1, "12's second husband is in Genealogy II (see 12 cross_ref)"),
    ("U07",  13,   0, 1, 0, "husband not shown on the plate; 13's line runs straight to 28-30"),
    ("U08",  17,  16, 1, 1, ""),
    ("U09",  19,  18, 1, 1, ""),
    ("U10",  21,  20, 1, 1, ""),
    ("U11",  23,  22, 1, 1, ""),
    ("U12",  54,  55, 1, 1, ""),
    ("U13",  57,  56, 1, 1, ""),
    ("U14",  59,  58, 1, 1, ""),
    ("U15",  60,  61, 1, 1, ""),
    ("U16",  62,  63, 1, 1, "63 marries both 62 and 64"),
    ("U17",  64,  63, 1, 2, "63 marries both 62 and 64; no children shown for this union"),
    ("U18",  66,  67, 1, 1, "67's second wife is 76 (see U23)"),
    ("U19",  68,  69, 1, 1, "68 has two husbands on the plate: 69 and 70"),
    ("U20",  68,  70, 2, 1, "70 also marries 77 (see U24)"),
    ("U21",  71,  72, 1, 1, ""),
    ("U22",  73,   8, 1, 2, "8's second wife"),
    ("U23",  76,  67, 1, 2,
     "PLATE MISPRINT: the '+' line under 76 is numbered 68, but names Shuwaiʼᶦri, Turkey = person 67. "
     "67's own cross-reference ('For second wife and offspring see below, 76, 90-3') confirms 67."),
    ("U24",  77,  70, 1, 2, "70 also marries 68 (see U20)"),
    ("U25",  78,  79, 1, 1, ""),
    ("U26",  97,  98, 1, 1, ""),
    ("U27", 100, 101, 1, 1, ""),
]

# ---------------------------------------------------------------------------
# PLATE_NUMBER_MISPRINTS  (union_id -> the number the plate prints on that '+'
# line, where it is not the number of the person the line names)
#
# The edition reproduces the plate: the printed number is what is drawn, and
# the reading that resolves it lives in the apparatus. Correcting it silently
# in the chart would make the page disagree with the scan it transcribes.
# ---------------------------------------------------------------------------
PLATE_NUMBER_MISPRINTS = {"U23": 68}

# ---------------------------------------------------------------------------
# CHILDREN  (each bracketed sibling group in the plate)
# union_id, mother_id, father_id, child_id, note
#   father_id = 0 when the plate does not let paternity be assigned
# ---------------------------------------------------------------------------
_GROUPS = [
    ("U01",  1,  2, [3]),
    ("U02",  3,  4, [5, 7, 9, 11]),
    ("U04",  7,  8, [13, 14, 15]),
    ("U05",  9, 10, [16, 18, 20, 22]),
    ("U06", 12, 11, [24, 25, 26, 27]),
    ("U07", 13,  0, [28, 29, 30]),
    ("U08", 17, 16, [31, 32, 33, 34, 35, 36, 37, 38]),
    ("U09", 19, 18, [39, 40, 41, 42, 43, 44]),
    ("U10", 21, 20, [45, 46, 47, 48, 49, 50, 51]),
    ("U11", 23, 22, [52, 53]),
    ("U12", 54, 55, [56, 58, 60, 62, 64]),
    ("U13", 57, 56, [65, 66, 68]),
    ("U14", 59, 58, [71, 8]),
    ("U15", 60, 61, [74, 75, 76, 77]),
    ("U16", 62, 63, [78]),
    ("U18", 66, 67, [80, 81, 82]),
    ("",    68,  0, [83, 84, 85]),
    ("U21", 71, 72, [86, 87, 88]),
    ("U22", 73,  8, [89]),
    ("U23", 76, 67, [90, 91, 92, 93]),
    ("U24", 77, 70, [94, 95, 96]),
    ("U25", 78, 79, [97, 99, 100]),
    ("U26", 97, 98, [102, 103]),
    ("U27", 100, 101, [104]),
]

_CHILD_NOTES = {
    8:  "cross-link: 8 also appears in the upper half of the plate as husband of 7 and 73",
    83: "sibling group drawn off 68's line only; 68 has two husbands (69, 70) and the plate does not assign paternity",
    84: "sibling group drawn off 68's line only; 68 has two husbands (69, 70) and the plate does not assign paternity",
    85: "sibling group drawn off 68's line only; 68 has two husbands (69, 70) and the plate does not assign paternity",
}

CHILDREN = [
    (union_id, mother, father, child, _CHILD_NOTES.get(child, ""))
    for union_id, mother, father, kids in _GROUPS
    for child in kids
]

# ---------------------------------------------------------------------------
# Notes printed on the plate that are not tied to a single person
# ---------------------------------------------------------------------------
PLATE_NOTES = [
    ("upper half, col. 3", "For second husband and offspring see Gen. II, 21, 74", "printed under 12"),
    ("lower half, col. 3", "For second wife and offspring see below, 76, 90-3", "printed under 67"),
    ("lower half, col. 3", "For first husband and descendants, see Gen. II, 158, 159, 160",
     "printed under 73"),
    ("lower half, col. 3", "For second husband and descendant, see Gen. III, 154, 220",
     "printed under 73"),
    ("lower half, col. 4", "For descendants, see above, 13-15, 28-30",
     "printed opposite the second appearance of 7, in place of a sibling bracket"),
]

CLANS = ["Sun", "Lizard", "Oak", "Water", "Parrot", "Bear", "Badger", "Eagle",
         "Turkey", "Chaparral Cock"]

ORTHOGRAPHY = [
    ("ʼ", "U+02BC", "modifier letter apostrophe", "glottal stop / raised apostrophe as printed"),
    ("˙", "U+02D9", "dot above", "raised dot: aspiration or length"),
    ("ă", "U+0103", "a with breve", ""),
    ("ĕ", "U+0115", "e with breve", ""),
    ("ĭ", "U+012D", "i with breve", ""),
    ("ŭ", "U+016D", "u with breve", ""),
    ("Ă", "U+0102", "A with breve", ""),
    ("ᶦ", "U+1DA6", "superscript i", ""),
    ("ᵘ", "U+1D58", "superscript u", ""),
    ("ᵃ", "U+1D43", "superscript a", ""),
    ("ñ", "U+00F1", "n with tilde", "as printed in 'Zuñi'"),
]

# ---------------------------------------------------------------------------
# ASCII folding, for matching against census spellings
# ---------------------------------------------------------------------------
# The union of all four plates' characters, and identical in all four modules:
# a fold key must not depend on which plate the name was read from. Keep them
# in step — a character mapped here and not there is a name that cannot be
# found by its own plate's fold().
_FOLD = {
    "ʼʼ": "", "ʼ": "", "ʽ": "", "˙": "", "˚": "", "˘": "",
    "ă": "a", "Ă": "A", "ĕ": "e", "ĭ": "i", "Ĭ": "I",
    "ŏ": "o", "ŭ": "u", "ä": "a", "ñ": "n",
    "ô": "o", "ó": "o", "ɪ": "i",
    "ᶦ": "i", "ᵘ": "u", "ᵃ": "a", "ᵉ": "e",
}


def fold(name: str) -> str:
    """Diacritic-free lowercase key for fuzzy matching against census spellings."""
    out = name
    for src, dst in _FOLD.items():
        out = out.replace(src, dst)
    return "".join(c for c in out if c.isalnum()).lower()


def self_check() -> list[str]:
    """Structural checks that must hold for the transcription to be sound."""
    problems = []
    ids = [p[0] for p in PERSONS]
    if ids != list(range(1, 105)):
        problems.append("PERSONS ids are not exactly 1..104")

    clan = {p[0]: p[6] for p in PERSONS}
    # Laguna clan membership is matrilineal: a child's clan is its mother's clan.
    for union_id, mother, father, child, _ in CHILDREN:
        if clan[child] and clan[mother] and clan[child] != clan[mother]:
            problems.append(
                f"clan mismatch: child {child} ({clan[child]}) "
                f"vs mother {mother} ({clan[mother]})"
            )

    kids = [c[3] for c in CHILDREN]
    if len(kids) != len(set(kids)):
        problems.append("a person appears as a child more than once")

    spouses = {i for u in UNIONS for i in (u[1], u[2]) if i}
    unplaced = set(ids) - set(kids) - spouses
    if unplaced:
        problems.append(f"persons neither child nor spouse: {sorted(unplaced)}")

    return problems


if __name__ == "__main__":
    issues = self_check()
    print(f"{len(PERSONS)} persons, {len(UNIONS)} unions, {len(CHILDREN)} child links")
    if issues:
        print("PROBLEMS:")
        for i in issues:
            print("  -", i)
    else:
        print("all structural checks pass")
