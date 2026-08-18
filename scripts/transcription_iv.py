"""
Verbatim transcription of Table 4, "Genealogy IV", from
Elsie Clews Parsons, "Laguna Genealogies",
Anthropological Papers of the American Museum of Natural History, vol. 19, pt. 5
(1923), pp. 133-292.

Source image: sources/parsons-1923-table-4.jpg (12255 x 8409 px)
sha256 e3ac35e27f8621e21b7c84df503ddf224a4368ec4514b408e48daa5c77788bf3

Read tile by tile at native resolution. This file is the immutable 1923
baseline. Do NOT add research data here -- see the README's privacy boundary.

HOW THIS PLATE DIFFERS FROM TABLE 1
-----------------------------------
1. RANGE ENTRIES. The plate collapses deceased sibling groups onto one line:
   "36-43.  8 children deceased.  Sun" and "50-53.  4 children deceased.
   Chaparral Cock". They are stored expanded, one person per id, because the
   plate does assign eight and four distinct numbers; the collapsed
   presentation is recorded in plate_note so nothing is invented and nothing
   is lost.
2. FIELD ORDER. This plate prints clan before the vital note -- "Sun. d." --
   where Table 1 prints "d. 1908. Sun". Same fields, different setting.
3. ENGLISH NAMES ON THE PLATE. Five people carry a parenthesised English name
   (Hugh, Frank, Paul and Joe Johnson; Mana). Like "Hazel" at Table 1's 90,
   these are PLATE DATA and belong in alt_name -- they are not research
   additions and must not be confused with one.
4. PERSONS 3 AND 4 APPEAR TWICE, as Table 1's person 8 does. Person 4 is the
   link between the two families: husband of 3 in the upper half, son of
   59+60 in the lower. Their repeated sibling group is replaced on the plate
   by "For descendants, see above".
5. NO SEX RECORDED for 19 and 20: the plate prints the number, a dash and the
   clan, with no F./M. Stored as empty, not guessed.
6. PATERNITY NOT ASSIGNED for 73: person 67 has no '+' spouse line.
"""

# (id, generation, sex, name_as_printed, alt_name, age, clan,
#  vital_note, origin, cross_ref, plate_note)
PERSONS = [
    # ---- family 1 -------------------------------------------------------
    (1,  1, "F", "",                "",              "",   "Sun",            "d.", "Navaho", "", "name printed as a dash"),
    (2,  1, "M", "Kiwi",            "",              "",   "Turkey",         "d.", "",       "", ""),
    (3,  2, "F", "Hieguma",         "",              "",   "Sun",            "d.", "",       "", "appears twice on the plate; drawn once"),
    (4,  2, "M", "Hio˙ʼdʼyăi",      "",              "",   "Corn",           "d.", "",       "", "appears twice on the plate; links the two families"),
    (5,  2, "M", "Naʼyabuni",       "",              "",   "Sun",            "d.", "",       "", ""),
    (6,  2, "F", "Tsiwaitina",      "",              "",   "Bear",           "",   "",       "", ""),
    (7,  2, "M", "Tsʼa˙ʼsh˙umăiʼ",  "",              "",   "Parrot",         "",   "",       "", "second husband of 6"),
    (8,  3, "M", "Dyaʼgăĭyăĭ",      "Hugh Johnson",  "",   "Sun",            "",   "",       "", "English name printed in parentheses on the plate"),
    (9,  3, "F", "Dziʼwaiʼsh˙u",    "",              "",   "Locust",         "",   "",       "", ""),
    (10, 3, "M", "Tsiʼraăi",        "Frank Johnson", "",   "Sun",            "",   "",       "", "English name printed in parentheses on the plate"),
    (11, 3, "F", "Na˙ʼs˙iăi",       "",              "",   "Chaparral Cock", "",   "",       "", ""),
    (12, 3, "F", "Dzio˙ʼkoish",     "",              "",   "Sun",            "",   "",       "", "second wife of 10"),
    (13, 3, "F", "Dzamaiʼ",         "",              "45", "Sun",            "",   "",       "", ""),
    (14, 3, "M", "Kʼaityima",       "",              "55", "Oak",            "",   "",       "", ""),
    (15, 3, "M", "Yaaiʼs˙dyiwăʼ",   "Paul Johnson",  "43", "Sun",            "",   "",       "", "English name printed in parentheses on the plate"),
    (16, 3, "F", "Dyăʼwaitʼsi",     "",              "",   "Chaparral Cock", "",   "",       "", ""),
    (17, 3, "M", "I˙ʼg˙ugăi",       "Joe Johnson",   "33", "Sun",            "",   "",       "", "English name printed in parentheses on the plate"),
    (18, 3, "F", "Dzaidʼyuwiʼ",     "",              "30", "Water",          "",   "",       "", ""),
    (19, 3, "",  "",                "",              "",   "Bear",           "",   "",       "", "no sex printed on the plate; name printed as a dash"),
    (20, 3, "",  "",                "",              "",   "Bear",           "",   "",       "", "no sex printed on the plate; name printed as a dash"),
    (21, 4, "M", "Ho˙akʼăʼ",        "",              "",   "Locust",         "",   "",       "", ""),
    (22, 4, "M", "Shka˙ʼkuli",      "",              "",   "Locust",         "",   "",       "", ""),
    (23, 4, "F", "Kaauʼs˙iyĕ",      "",              "",   "Locust",         "",   "",       "", ""),
    (24, 4, "F", "Osha˙ʼradʼyĕʼ",   "",              "",   "Locust",         "",   "",       "", ""),
    (25, 4, "F", "",                "",              "",   "Locust",         "d.", "",       "", "name printed as a dash"),
    (26, 4, "M", "Yaiʼtʼyimai",     "",              "",   "Chaparral Cock", "d.", "",       "", ""),
    (27, 4, "M", "Mo˙kʼaich˙",      "",              "",   "Chaparral Cock", "",   "",       "", ""),
    (28, 4, "M", "Shuwityʼi",       "",              "",   "Chaparral Cock", "d.", "",       "", ""),
    (29, 4, "M", "Kawe˙ʼsh˙dyĭmă",  "",              "",   "Sun",            "",   "",       "", ""),
    (30, 4, "M", "Pero",            "",              "",   "Sun",            "",   "",       "", ""),
    (31, 4, "F", "",                "",              "",   "Sun",            "",   "",       "", "name printed as a dash"),
    (32, 4, "M", "Ko˙ʼrai˙tyʼiʼ",   "",              "",   "Sun",            "",   "",       "", ""),
    (33, 4, "M", "No˙ʼraai",        "",              "",   "Sun",            "",   "",       "", ""),
    (34, 4, "M", "Gat˙ăyă",         "",              "",   "Sun",            "",   "",       "", ""),
    (35, 4, "F", "Dzai˙ʼtyʼiyăiʼ",  "",              "3",  "Sun",            "",   "",       "", ""),
]

# The plate prints 36-43 as a single line: "8 children deceased. Sun".
PERSONS += [
    (i, 4, "", "", "", "", "Sun", "d.", "", "",
     "one of the eight printed collectively as '36-43. 8 children deceased. Sun'")
    for i in range(36, 44)
]

PERSONS += [
    (44, 4, "M", "Shauʼwag˙oʼyĕ",      "", "",  "Chaparral Cock", "",       "", "", ""),
    (45, 4, "F", "Kʼauwimaitsʼă",      "", "",  "Chaparral Cock", "",       "", "", ""),
    (46, 4, "F", "Dzamaiʼd˙yuwitsʼa",  "", "",  "Chaparral Cock", "",       "", "", ""),
    (47, 4, "M", "Rauʼs˙iyăi",         "", "",  "Chaparral Cock", "",       "", "", ""),
    (48, 4, "M", "Dyuityiĕ",           "", "",  "Chaparral Cock", "",       "", "", ""),
    (49, 4, "F", "Dyiᶦd˙zaid˙yui",     "", "",  "Chaparral Cock", "",       "", "", ""),
]

# The plate prints 50-53 as a single line: "4 children deceased. Chaparral Cock".
PERSONS += [
    (i, 4, "", "", "", "", "Chaparral Cock", "d.", "", "",
     "one of the four printed collectively as '50-53. 4 children deceased. Chaparral Cock'")
    for i in range(50, 54)
]

PERSONS += [
    (54, 4, "M", "Mid˙yăiʼsĭw˙ă",   "",         "10", "Water", "",         "", "", ""),
    (55, 4, "F", "Kwid˙yaid˙yui",   "",         "7",  "Water", "",         "", "", ""),
    (56, 4, "M", "Shaatse",         "",         "",   "Water", "d. 1913",  "", "", ""),
    (57, 4, "M", "Koʼya˙ʼshdyiĕ",   "",         "",   "Water", "d. 1917",  "", "", ""),
    (58, 4, "M", "Yaiʼyaăi",        "",         "2",  "Water", "",         "", "", ""),
    # ---- family 2 -------------------------------------------------------
    (59, 1, "F", "",                "",         "",   "Corn",      "",   "", "", "name printed as a dash"),
    (60, 1, "M", "",                "",         "",   "",          "",   "", "", "name and clan both printed as dashes"),
    (61, 2, "F", "Tsaiyaʼ",         "Eldest",   "",   "Corn",      "d.", "", "",
     "'(Eldest)' is printed in parentheses after the name; a descriptor, not a personal name"),
    (62, 2, "M", "Wa˙k˙ain˙eʼeshuʼ", "",        "",   "Water",     "d.", "", "", ""),
    (63, 2, "F", "Tsiwaisie",       "Mana",     "",   "Corn",      "",   "", "",
     "English name printed in parentheses on the plate"),
    (64, 2, "M", "Kăiyăiʼd˙yăiʼ",   "",         "",   "Turquoise", "",   "", "",
     "plate prints beneath the name: '(Presumedly brother of Gen. II, 59)' -- spelling as printed"),
    (65, 3, "M", "Kaiedyurĕ",       "",         "",   "Corn",      "",   "", "", ""),
    (66, 3, "F", "Tsa˙ʼs˙ĭro",      "",         "",   "Sun",       "",   "", "", ""),
    (67, 3, "F", "Niwi",            "",         "",   "Corn",      "d.", "", "", ""),
    (68, 4, "F", "Gauʼs˙irĕ",       "",         "",   "Sun",       "",   "", "", ""),
    (69, 4, "F", "Gwiʼt˙yʼi",       "",         "",   "Sun",       "",   "", "", ""),
    (70, 4, "F", "",                "",         "",   "Sun",       "",   "", "", "name printed as a dash"),
    (71, 4, "F", "",                "",         "",   "Sun",       "",   "", "", "name printed as a dash"),
    (72, 4, "F", "",                "",         "",   "Sun",       "",   "", "", "name printed as a dash"),
    (73, 4, "M", "",                "",         "",   "Corn",      "",   "", "", "name printed as a dash"),
]

# (union_id, wife_id, husband_id, wife_order, husband_order, note)
UNIONS = [
    ("V01",  1,  2, 1, 1, ""),
    ("V02",  3,  4, 1, 1, "3 and 4 are both printed twice on the plate"),
    ("V03",  6,  5, 1, 1, ""),
    # drawn_under=5: the plate prints this marriage inside 5's block, on the
    # line below 6, because 6 is already shown there as 5's wife.
    ("V04",  6,  7, 2, 1, "second husband of 6; no issue recorded. Corrected "
     "2026-08-10: 20 was attached to THIS union and belongs to V03. Read at "
     "native resolution, x 4400-6800 / y 6040-6380: the plate draws ONE "
     "vertical spanning 19 and 20 with a SINGLE leader entering it at 19's "
     "row, from 6's line; 7's line ends after 'Parrot' and carries no rule at "
     "all. Splitting the bracket asserted a paternity the plate does not "
     "state, and drew a leader on 7's line the plate does not print. Nothing "
     "structural could see it: 19 and 20 are both Bear, exactly like their "
     "mother, so clan descent cannot separate them. "
     "RE-MEASURED 2026-08-17, and the BASIS restated: in the 750px gap "
     "between the text and the bracket, 6's row is solid ink (750/750 at "
     "y 6099-6116) and BOTH husbands' rows carry nothing above 3px. So the "
     "one leader sits on the line 6 shares with BOTH marriages, and names no "
     "father on its own. The reading that 19 and 20 are 5's rests on two "
     "things, neither of them the old justification: Parsons marks a second "
     "husband's issue when she means to -- Gen. III's 43 gives her second "
     "husband 45 his own leader -- and this bracket is drawn inside 5's "
     "block, he being its primary with 6 and 7 both '+' lines under him. "
     "NOTE the first argument is CROSS-PLATE: Table 4 never demonstrates its "
     "own convention, since its only other second marriage with issue (V07) "
     "has the second spouse as the MOTHER, whose line carries the bracket "
     "anyway. Do NOT restate this as 'a spouse with no leader had no recorded "
     "issue' -- Gen. III's 58, who has no leader on her own line and two "
     "children, disproves that as a general rule (see LEADER_ON_SPOUSE_ROW's "
     "W31 there)", 5),
    ("V05",  9,  8, 1, 1, ""),
    ("V06", 11, 10, 1, 1, ""),
    ("V07", 12, 10, 1, 2, "second wife of 10"),
    ("V08", 13, 14, 1, 1, ""),
    ("V09", 16, 15, 1, 1, ""),
    ("V10", 18, 17, 1, 1, ""),
    ("V11", 59, 60, 1, 1, ""),
    ("V12", 61, 62, 1, 1, ""),
    ("V13", 63, 64, 1, 1, ""),
    ("V14", 66, 65, 1, 1, ""),
]

# (union_id, mother_id, father_id, child_id, note)
_GROUPS = [
    ("V01",  1,  2, [3, 5]),
    ("V02",  3,  4, [8, 10, 13, 15, 17]),
    # Both children hang off 6's line under the plate's single bracket -- see
    # V04's note in UNIONS. V04 has no group at all, exactly as V12 has none.
    ("V03",  6,  5, [19, 20]),
    ("V05",  9,  8, [21, 22, 23, 24, 25]),
    ("V06", 11, 10, [26, 27, 28]),
    ("V07", 12, 10, [29, 30, 31]),
    ("V08", 13, 14, list(range(32, 44))),
    ("V09", 16, 15, list(range(44, 54))),
    ("V10", 18, 17, [54, 55, 56, 57, 58]),
    ("V11", 59, 60, [61, 4, 63]),
    ("V13", 63, 64, [65, 67]),
    ("V14", 66, 65, [68, 69, 70, 71, 72]),
]

CHILDREN = [(uid, m, f, c, "") for uid, m, f, cs in _GROUPS for c in cs]

# Person 67 has no '+' spouse line, so the plate assigns 73 no father.
CHILDREN.append(("", 67, 0, 73,
                 "67 has no husband printed; the plate does not assign paternity"))

PLATE_NOTES = [
    ("lower half, col. 3", "For descendants, see above",
     "printed opposite the second appearance of 3+4, in place of a sibling bracket"),
    ("lower half, col. 2", "(Presumedly brother of Gen. II, 59)",
     "printed under 64; spelling as printed"),
    ("upper half, col. 4", "36-43.  8 children deceased.  Sun",
     "eight ids collapsed onto one line; stored expanded"),
    ("upper half, col. 4", "50-53.  4 children deceased.  Chaparral Cock",
     "four ids collapsed onto one line; stored expanded"),
]

CLANS = ["Sun", "Turkey", "Corn", "Locust", "Chaparral Cock", "Bear", "Parrot",
         "Oak", "Water", "Turquoise"]

ORTHOGRAPHY = [
    ("ʼ", "U+02BC", "modifier letter apostrophe", "glottal stop / raised apostrophe as printed"),
    ("˙", "U+02D9", "dot above", "raised dot: aspiration or length"),
    ("ă", "U+0103", "a with breve", ""),
    ("ĕ", "U+0115", "e with breve", ""),
    ("ĭ", "U+012D", "i with breve", ""),
    ("ᶦ", "U+1DA6", "superscript i", "in 49 Dyiᶦd˙zaid˙yui"),
]

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
    """Diacritic-free lowercase key, for matching against other spellings."""
    out = name
    for k, v in _FOLD.items():
        out = out.replace(k, v)
    return "".join(c for c in out if c.isalnum()).lower()


def self_check() -> list[str]:
    """Structural checks that must hold for the transcription to be sound."""
    problems = []
    ids = [p[0] for p in PERSONS]
    if ids != list(range(1, 74)):
        problems.append("PERSONS ids are not exactly 1..73")

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
