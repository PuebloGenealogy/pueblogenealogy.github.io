"""
Verbatim transcription of Table 2, "Genealogy II", from
Elsie Clews Parsons, "Laguna Genealogies",
Anthropological Papers of the American Museum of Natural History, vol. 19, pt. 5
(1923), pp. 133-292.

Source image: sources/parsons-1923-table-2.jpg (7770 x 12681 px)
sha256 d7d050f52c7e6d03bb60a1a4b338972e9dbb3b7e8cdc8299b97317d45339f7a6

Read tile by tile at native resolution. This file is the immutable 1923
baseline. Do NOT add research data here -- see the README's privacy boundary.

*** WORK IN PROGRESS -- Gate 1 (reading) is not complete. ***
Do not register this module in make_chart.py's TABLES until self_check() passes
and the persons/unions/children counts reconcile.

HOW THIS PLATE DIFFERS FROM TABLES 1 AND 4
------------------------------------------
1. ORIENTATION AND SIZE. This plate is portrait (7770 x 12681) where Tables 1
   and 4 are landscape, and it is much the largest of the three: the numbering
   runs past 269, against Table 1's 104 and Table 4's 73.
2. TWO BLOCKS. An upper block of six generations and a lower block joined at
   the couple 154+155. Table 1 has five generations; this is the first plate
   here to reach six.
3. HEAVY CROSS-REFERENCING INTO THE OTHER PLATES. Many entries carry
   "See Gen. I, <n>", and two carry references into Genealogy IV
   ("Brother of Gen. IV, 9"; "Presumedly brother of Gen. IV, 64"). Both target
   plates are already published in this edition.
4. ENGLISH NAMES ON THE PLATE. As at Table 1's 90 and Table 4's Johnsons, some
   entries carry a parenthesised English name -- 27 (Minnie), 42 (Annie),
   43 (David Leonia). These are PLATE DATA and belong in alt_name; they are
   not research additions and must not be confused with one.
5. FOLD CREASES. The scanned plate carries horizontal and vertical fold
   creases. Where one crosses text the reading is checked at a tighter crop.
"""

# (id, generation, sex, name_as_printed, alt_name, age, clan,
#  vital_note, origin, cross_ref, plate_note)
PERSONS = [
    # ---- generation 1 ---------------------------------------------------
    (1,  1, "F", "",                 "",       "",   "Water",  "",   "", "", "name printed as a dash"),
    (2,  1, "M", "",                 "",       "",   "",       "",   "", "", "no name and no clan printed"),

    # ---- generation 2 -- the three daughters of 1+2, all Water ----------
    (3,  2, "F", "Dziu˙ʼnitsʼa",     "",       "",   "Water",  "",   "", "", ""),
    (4,  2, "M", "",                 "",       "",   "Turquoise", "", "", "", "name printed as a dash"),
    (5,  2, "F", "",                 "",       "",   "Water",  "",   "", "", "name printed as a dash"),
    (6,  2, "M", "",                 "",       "",   "",       "",   "", "", "name and clan both printed as dashes"),
    (7,  2, "F", "Tsaiʼityʼd˙yai",   "",       "",   "Water",  "",   "", "", ""),
    (8,  2, "M", "",                 "",       "",   "",       "",   "", "", "name and clan both printed as dashes"),

    # ---- generation 3 ---------------------------------------------------
    (9,  3, "F", "Kăaiʼd˙yuwĕ",      "",       "",   "Water",  "",   "", "", ""),
    (10, 3, "M", "Kʼaikyie",         "",       "",   "Lizard", "",   "", "", ""),
    (11, 3, "F", "Goyaiʼd˙yuwĕʼ",    "",       "70", "Water",  "",   "", "", ""),
    (12, 3, "M", "Gʼausire",         "",       "",   "Oak",    "d. 1915", "", "", ""),
    (13, 3, "F", "Dzia˙ʼyotsʼa",     "",       "",   "Water",  "d.", "",
     "For descendants, see above",
     "DISCREPANCY -- SEE TODO. The plate prints this person twice, and the two "
     "readings do not agree: 'Dzia˙ʼyotsʼa' in the upper block, 'Tsiaiutsa' in "
     "the lower. Both tiles were legible. Re-read both before Gate 3; the "
     "upper reading is the less certain of the two"),
    (14, 3, "M", "S˙ʼĭʼrowaisiwa",   "Kʼaiʼsh˙dŏwăʼ", "", "Parrot", "d. 1918", "",
     "For descendants, see above",
     "braced: the plate joins two names with a '{' for this one person -- "
     "'S˙ʼĭʼrowaisiwa' over 'Kʼaiʼsh˙dŏwăʼ'. Second name carried in alt_name. "
     "The breve over 'o' (U+014F) in the second name is confirmed at the lower "
     "block's larger setting. Drawn once; the repeat carries 'For descendants, "
     "see above'"),
    (15, 3, "M", "Dzăʼyu",           "",       "",   "Water",  "",   "", "", ""),
    (16, 3, "F", "Sho˙tyʼi",         "",       "",   "Turkey", "d.", "", "", ""),
    (17, 3, "M", "Tyi˙kʼamăi",       "",       "",   "Water",  "",   "", "", ""),
    (18, 3, "F", "Dziʼw˙ămaiʼ",      "",       "",   "Corn",   "d.", "", "", ""),
    (19, 3, "F", "Dzaiʼᶦtyʼi",       "",       "50", "Water",  "",   "", "",
     "name printed without a following period"),
    (20, 3, "M", "Kyʼĭauʼd˙yăĭăi",   "",       "",   "Sun",    "d.", "", "See Gen. I, 11",
     "medial vowels unverified -- SEE TODO"),
    (21, 3, "M", "Dziwaikch",        "",       "35", "Water",  "",   "", "",
     "trailing marks after 'ch' unverified -- SEE TODO; third husband of 19"),
    (22, 3, "M", "Shaiyo˙ʼsi˙ĕ",     "",       "48", "Water",  "",   "", "", ""),
    (23, 3, "F", "Go˙wʼăiʼ",         "",       "",   "Lizard", "",   "", "", ""),
    (24, 3, "M", "Hĕʼnadyi",         "",       "",   "Water",  "",   "", "", ""),
    (25, 3, "F", "Dzaiʼr˙inăiʼ",     "",       "",   "Bear",   "",   "", "", ""),

    # ---- generation 4 ---------------------------------------------------
    (26, 4, "M", "Dzaiʼsiyăiʼ",      "",       "",   "Water",  "",   "", "", ""),
    (27, 4, "F", "Mini",             "Minnie", "",   "Lizard", "d.", "", "", "English name printed in parentheses on the plate"),
    (28, 4, "F", "",                 "",       "",   "Bear",   "",   "", "", "name printed as a dash; second wife of 26"),
    (29, 4, "F", "Dya˙ʼg˙ŭr",        "",       "",   "Water",  "",   "", "", ""),
    (30, 4, "M", "Kʼautyurĕ",        "",       "",   "",       "",   "", "", "no clan printed"),
    (31, 4, "M", "Re˙ʼni",           "",       "",   "Water",  "",   "", "", ""),
    (32, 4, "F", "",                 "",       "",   "Sun",    "d.", "", "", "name printed as a dash"),
    (33, 4, "F", "Dziwaid˙yui",      "",       "",   "Water",  "",   "", "", ""),
    (34, 4, "M", "Ha˙ʼg˙yuĕ",        "",       "",   "Bear",   "",   "", "", ""),
    (35, 4, "M", "Dzira˙ʼai",        "",       "",   "Water",  "",   "", "", ""),
    (36, 4, "M", "Shaaiʼyunăi",      "",       "",   "Water",  "",   "", "", ""),
    (37, 4, "F", "Hĭwaiʼ",           "",       "",   "Corn",   "",   "", "", ""),
    (38, 4, "M", "Kawi˙ʼd˙yăiʼ",     "",       "",   "Water",  "",   "", "", ""),
    (39, 4, "F", "Paura",            "",       "",   "Parrot", "",   "", "", ""),
    (40, 4, "M", "",                 "",       "",   "Water",  "d.", "", "", "name printed as a dash"),
    (41, 4, "M", "",                 "",       "",   "Water",  "d.", "", "", "name printed as a dash"),
    (42, 4, "F", "Dzanăiʼ",          "Annie",  "30", "Water",  "",   "", "", "English name printed in parentheses on the plate"),
    (43, 4, "M", "Dyaiʼyuwe",        "David Leonia", "", "Locust", "", "",
     "Brother of Gen. IV, 9",
     "English name printed in parentheses on the plate; the plate prints '+ Locust', "
     "a '+' identical in form to the spouse mark standing between the name and the "
     "clan. Verified at native resolution. Recorded, not interpreted"),
    (44, 4, "F", "Dzĭwiʼ",           "",       "20", "Water",  "",   "", "", ""),
    (45, 4, "M", "Ka˙chănĭsh",       "",       "60", "Water",  "",   "", "", "trailing mark after 'sh' unverified -- SEE TODO"),
    (46, 4, "F", "Dzaaiʼy˙ăi",       "",       "",   "Bear",   "",   "", "", ""),
    (47, 4, "M", "Kaauʼs˙iyăiʼ",     "",       "",   "Water",  "d.", "", "", ""),
    (48, 4, "F", "Nati",             "",       "",   "Parrot", "",   "", "", ""),
    (49, 4, "M", "Gawaiʼᶦsᶦ",        "",       "",   "Turquoise", "", "", "",
     "two superscript i (U+1DA6), verified at native resolution; second husband of 48"),
    (50, 4, "M", "",                 "",       "",   "Water",  "d. in childhood.", "", "", "name printed as a dash"),
    (51, 4, "M", "Haiʼyuwăi˙siwăʼ",  "",       "",   "Water",  "",   "", "", ""),
    (52, 4, "F", "Gauʼs˙inăiʼ",      "",       "",   "Lizard", "d.", "", "", "mark before 'ăi' unverified -- SEE TODO"),
    (53, 4, "F", "Kawiʼtsʼirăiʼ",    "",       "50", "Water",  "",   "", "", ""),
    (54, 4, "M", "Ma˙ʼrani",         "",       "",   "Sun",    "",   "", "",
     "DISCREPANCY -- SEE TODO. Printed twice. The lower-block occurrence "
     "(native crop at x 3760, y 10780) reads 'Ma˙ʼran˙i', with a raised dot "
     "before the final 'i' that the upper-block reading above does not carry. "
     "The lower reading is the clearer. Re-read the upper occurrence before "
     "Gate 3"),
    (55, 4, "M", "Go˙tyʼiăiʼ",       "",       "65", "Corn",   "",   "", "", "second husband of 53"),
    (56, 4, "M", "Dzawi˙răi",        "",       "",   "Turkey", "",   "", "", ""),
    (57, 4, "F", "",                 "",       "",   "",       "",   "", "", "name printed as a dash; no clan printed"),
    (58, 4, "F", "Kʼoyo˙ʼs˙ăi",      "",       "45", "Turkey", "",   "", "", ""),
    (59, 4, "M", "Yăʼwĭĭʼyăiʼ",      "",       "",   "Turquoise", "", "",
     "Presumedly brother of Gen. IV, 64",
     "medial vowels unverified -- SEE TODO"),
    (60, 4, "M", "Shuwaiʼᶦri",       "",       "",   "Turkey", "",   "",
     "See Gen. I, 68",
     "cross-reference printed as 'See Gen. I, 68' -- SEE TODO, appears to name Gen. I 67"),
    (61, 4, "F", "Tsikʼaʼyăaitsʼa",  "",       "",   "Eagle",  "d.", "",
     "See Gen. I, 67",
     "cross-reference printed as 'See Gen. I, 67' -- SEE TODO, appears to name Gen. I 68"),
    (62, 4, "F", "Dziwiʼd˙yăi",      "",       "33", "Badger", "",   "", "See Gen. I, 77", "second wife of 60"),
    (63, 4, "M", "Dyaiʼtsʼdyĭwă",    "",       "",   "Turkey", "d.", "", "", ""),
    (64, 4, "M", "Kʼaisĭyăiʼ",       "",       "",   "Turkey", "",   "", "", "mark before 'ĭ' unverified -- SEE TODO"),
    (65, 4, "M", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),
    (66, 4, "M", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),
    (67, 4, "M", "Dzauwaiʼd˙yăi",    "",       "24", "Water",  "",   "", "See Gen. I, 24", ""),
    (68, 4, "M", "Kaaiʼdziăis˙iwă",  "",       "",   "Water",  "d.", "", "See Gen. I, 25", ""),
    (69, 4, "F", "Dziwaiid˙yi",      "",       "",   "Water",  "d.", "", "", ""),
    (70, 4, "F", "",                 "",       "",   "Water",  "d.", "", "", "name printed as a dash"),
    (71, 4, "M", "",                 "",       "",   "Water",  "d.", "", "", "name printed as a dash"),
    (72, 4, "F", "Gawaiʼy˙unăi",     "",       "18", "Water",  "",   "", "See Gen. I, 26", ""),
    (73, 4, "F", "Kowaiʼd˙yui",      "",       "16", "Water",  "",   "", "See Gen. I, 27", ""),
    (74, 4, "F", "Dziwŭrshdyăwiʼ",   "",       "4",  "Water",  "",   "", "", ""),
    (75, 4, "F", "",                 "",       "",   "Lizard", "",   "", "", "name printed as a dash"),
    (76, 4, "M", "Dzaiʼd˙yiăiʼ",     "",       "",   "Lizard", "",   "", "", ""),
    (77, 4, "M", "Koiʼchinăʼ",       "",       "",   "Lizard", "",   "", "", ""),
    (78, 4, "F", "",                 "",       "",   "Lizard", "",   "", "", "name printed as a dash"),
    (79, 4, "M", "",                 "",       "",   "Lizard", "",   "", "", "name printed as a dash"),
    (80, 4, "F", "Gauʼs˙iro",        "",       "",   "Bear",   "",   "", "", "mark over 'i' unverified -- SEE TODO"),
    (81, 4, "F", "",                 "",       "",   "Bear",   "",   "", "", "name printed as a dash"),
    (82, 4, "F", "",                 "",       "",   "Bear",   "",   "", "", "name printed as a dash"),

    # ---- generation 5 ---------------------------------------------------
    # 85-100 and 106-115 print no sex letter: number, dash, clan only. Stored
    # as empty, not guessed -- the same treatment Table 4 gives its 19 and 20.
    (83, 5, "F", "Dzaaiʼd˙yid˙yuwe", "",       "",   "Lizard", "",   "", "", ""),
    (84, 5, "F", "Ha˙tsʼᵉ",          "",       "",   "Lizard", "",   "", "",
     "superscript e (U+1D49) -- a codepoint neither Table 1 nor Table 4 uses. "
     "CHECK THE FONT SUBSET AT GATE 4"),
    (85, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (86, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (87, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (88, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (89, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (90, 5, "",  "",                 "",       "",   "Bear",   "",   "", "", "no sex printed; name printed as a dash"),
    (91, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (92, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (93, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (94, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (95, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (96, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (97, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (98, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (99, 5, "",  "",                 "",       "",   "Water",  "",   "", "", "no sex printed; name printed as a dash"),
    (100, 5, "", "",                 "",       "",   "Corn",   "",   "", "", "no sex printed; name printed as a dash"),

    # *** THE PLATE PRINTS 101 TWICE. See DUPLICATE_PLATE_NUMBERS below. ***
    # Ids here are provisional pending that decision: the first 101 keeps 101,
    # the second is parked at 1010 so nothing collides while Gate 1 continues.
    (101, 5, "F", "Naauʼg˙ŭyăiʼ",    "",       "",   "Water",  "",   "", "", ""),
    (1010, 5, "M", "",               "",       "",   "Water",  "d.", "", "",
     "PROVISIONAL ID. The plate numbers this line 101, the same number as the "
     "line above it. Verified at high magnification. Name printed as a dash"),
    (102, 5, "M", "",                "",       "",   "Water",  "d.", "", "", "name printed as a dash"),
    (103, 5, "F", "Paura",           "",       "",   "Water",  "",   "", "", ""),
    (104, 5, "F", "Chais˙iăiʼ",      "",       "",   "Water",  "",   "", "", ""),
    (105, 5, "F", "Dzidzaid˙yuweʼ",  "",       "",   "Water",  "",   "", "", ""),
    (106, 5, "F", "Dzitʼaid˙yuwi",   "",       "",   "Bear",   "d. at 14", "", "", ""),
    (107, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (108, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (109, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (110, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (111, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (112, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (113, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (114, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    (115, 5, "",  "",                "",       "",   "Bear",   "d.", "", "", "no sex printed; name printed as a dash"),
    # 116-118, 128, 134 carry English names as the name itself, not
    # parenthesised as at Table 1's 90. Plate data either way.
    (116, 5, "F", "Julia",           "",       "18", "Parrot", "",   "", "", ""),
    (117, 5, "F", "Susie",           "",       "16", "Parrot", "",   "", "", ""),
    (118, 5, "M", "Isaac",           "",       "13", "Parrot", "",   "", "", ""),
    (119, 5, "F", "Kʼăwaity˙id˙yuweʼ", "",     "23", "Lizard", "",   "", "", ""),
    (120, 5, "M", "Gwiʼd˙zirăiʼ",    "",       "",   "Bear",   "",   "", "", ""),
    (121, 5, "F", "Guʼmiyăiʼ",       "",       "18", "Lizard", "",   "", "", ""),
    (122, 5, "F", "Dzaid˙yuwiʼ",     "",       "30", "Water",  "",   "", "", ""),
    (123, 5, "M", "I˙ʼg˙ugăi",       "",       "33", "Sun",    "",   "", "", ""),
    (124, 5, "M", "Dzĭo˙kwid˙yuʼă",  "",       "19", "Water",  "",   "", "", ""),
    (125, 5, "F", "Gowaʼk˙ʼd˙yăiʼ",  "",       "18", "Water",  "",   "", "",
     "DISCREPANCY -- NOT A READING PROBLEM. Printed twice, and THE PLATE SETS "
     "THE TWO DIFFERENTLY: 'Gowaʼk˙ʼd˙yăiʼ' in the upper block (crop x 5080, "
     "y 3150) and 'Gowaʼkʼad˙zăiʼ' in the lower (crop x 4160, y 9555). Both "
     "were re-read at 380 px on 2026-07-29 and both are unambiguous at that "
     "size, so no tighter crop will settle it. Age 18 and clan Water agree in "
     "both. One person, one name to print -- an EDITORIAL choice, and one for "
     "the user, not for the transcriber"),
    (126, 5, "M", "Yo˙ʼkwi",         "",       "23", "Chaparral Cock", "", "", "", ""),
    (127, 5, "F", "Howa˙kʼă",        "",       "",   "Water",  "d. 1919 at 13", "", "", ""),
    (128, 5, "F", "Mary Saiu",       "",       "",   "",       "",   "", "", "no clan printed"),
    (129, 5, "M", "",                "",       "",   "",       "",   "", "", "name and clan both printed as dashes"),
    (130, 5, "M", "Dzĭnătsʼĭd˙yiwă", "",       "",   "Turkey", "",   "", "", ""),
    (131, 5, "F", "Dziwaiʼy˙unăiʼ",  "",       "",   "Turkey", "",   "", "", ""),
    (132, 5, "M", "Djo˙s˙iyăi",      "",       "",   "Turkey", "",   "", "", ""),
    (133, 5, "M", "Yaʼod˙yidyăis˙iwăʼ", "",    "",   "Turkey", "",   "", "", ""),
    (134, 5, "F", "Juanina",         "",       "",   "Turkey", "",   "", "", ""),
    (135, 5, "F", "Săp",             "",       "",   "Turkey", "",   "", "",
     "trailing mark after 'p' unverified -- SEE TODO"),
    (136, 5, "F", "Dzid˙zaiʼd˙yuwi", "",       "",   "Turkey", "",   "", "", ""),
    # 137-143 each carry a "See Gen. I, n" that is one HIGHER than the
    # Genealogy I person whose name, sex and clan match. See CROSS_REF_OFFSET.
    (137, 5, "M", "Shauʼm˙ăiʼ",      "",       "",   "Eagle",  "",   "", "See Gen. I, 81", ""),
    (138, 5, "M", "",                "",       "",   "Eagle",  "",   "", "See Gen. I, 82", "name printed as a dash"),
    (139, 5, "M", "",                "",       "",   "Eagle",  "d.", "", "See Gen. I, 83", "name printed as a dash"),
    (140, 5, "F", "Heʼsa",           "Hazel",  "",   "Badger", "",   "", "See Gen. I, 91",
     "English name printed in parentheses on the plate"),
    (141, 5, "F", "Dzaĭyăiʼ",        "",       "",   "Badger", "",   "", "See Gen. I, 92", ""),
    (142, 5, "F", "Kăaiˑʼyunăiʼ",    "",       "",   "Badger", "",   "", "See Gen. I, 93",
     "medial marks unverified -- SEE TODO"),
    (143, 5, "M", "Dziw˙aiʼs˙iwă",   "",       "",   "Badger", "",   "", "See Gen. I, 94", ""),

    # ---- generation 6 ---------------------------------------------------
    (144, 6, "F", "Dzaaiʼd˙yid˙yuweʼ", "",     "6",  "Lizard", "",   "", "", ""),
    (145, 6, "F", "Kʼo˙ty˙imaiʼ",    "",       "4",  "Lizard", "",   "", "", ""),
    (146, 6, "M", "Aiʼs˙iyĕ",        "",       "9 mos.", "Lizard", "", "", "",
     "trailing mark after 'ĕ' unverified -- SEE TODO"),
    (147, 6, "M", "Mid˙yăiʼsĭw˙ă",   "",       "10", "Water",  "",   "", "", ""),
    (148, 6, "F", "Kwid˙yaid˙yui",   "",       "7",  "Water",  "",   "", "", ""),
    (149, 6, "M", "Shaatse",         "",       "",   "Water",  "d. 1913, at 3 days", "", "", ""),
    (150, 6, "M", "Koʼya˙ʼshdyiĕ",   "",       "",   "Water",  "d. 1917, at 2", "", "", ""),
    (151, 6, "M", "Yaiʼyaăi",        "",       "2",  "Water",  "",   "", "", ""),
    (152, 6, "M", "Tsiᶦshdyĭʼwă",    "",       "3",  "Water",  "",   "", "", ""),
    (153, 6, "F", "Gaiʼtsdyui",      "",       "5 mos.", "Water", "", "", "", ""),

    # =====================================================================
    # LOWER BLOCK -- founding couple 154+155
    # Generations below are numbered WITHIN this block: 154+155 are its
    # generation 1. Whether the two blocks share a generation frame is a
    # question for Gate 2, not a reading -- see the structure notes.
    # =====================================================================
    (154, 1, "F", "",                "",       "",   "Parrot", "",   "", "", "name printed as a dash"),
    (155, 1, "M", "",                "",       "",   "Turkey", "",   "", "", "name printed as a dash"),

    (156, 2, "M", "Shʼauʼs˙imăiʼ",   "",       "",   "Parrot", "d.", "", "See Gen. I, 10", ""),
    (157, 2, "F", "Dyaiʼᶦs˙itsʼă",   "",       "",   "Sun",    "d. 1918, at 60", "", "See Gen. I, 9", ""),
    (158, 2, "M", "Niʼʼy˙ŭyăiʼ",     "",       "",   "Parrot", "",   "", "", ""),
    (159, 2, "F", "",                "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (160, 2, "F", "Yo˙ʼs˙iro",       "",       "",   "Chaparral Cock", "d. 1914", "",
     "For second husband and descendant, see Gen. III, 154, 220 / "
     "For third husband and descendant, see Gen. I, 8, 90",
     "second wife of 158; the year 1914 is set in bold on the plate. This is "
     "Genealogy I's person 73 -- name, clan and death year all agree"),
    (161, 2, "",  "Gawai˙d˙yirăiʼ",  "",       "",   "Parrot", "d.", "", "",
     "sex printed as 'M.-F.' -- a marking used nowhere else on this plate. "
     "Stored empty rather than guessed; recorded here as printed"),
    (162, 2, "M", "Da˙ʼyu",          "",       "",   "Parrot", "d.", "", "",
     "trailing mark after 'yu' unverified -- SEE TODO"),
    (163, 2, "F", "Ĭyaˑʼsi",         "",       "",   "Bear",   "",   "",
     "For second husband and descendants, see Gen. III, 14, 49-55, 135-141", ""),
    (164, 2, "F", "Heaʼʼs˙i",        "",       "",   "Parrot", "d.", "", "", ""),
    (165, 2, "M", "Ha˙ʼpai",         "",       "",   "Oak",    "d.", "", "", ""),

    # =====================================================================
    # THIRD FOUNDING COUPLE -- 232+233
    # No leader rule enters 232 from the left, where 158 and 164 both have
    # one. Verified at native resolution. Their son is 54, who also appears
    # in the upper block as 53's husband.
    # =====================================================================
    (232, 1, "F", "Yuwaiʼd˙yaitsʼă", "",       "",   "Sun",    "",   "", "", ""),
    (233, 1, "M", "Gaʼʼaiʼ",         "",       "",   "Turkey", "",   "", "", ""),

    # ---- lower block, generation 3 --------------------------------------
    (166, 3, "M", "G˙yiʼmi",         "",       "45", "Sun",    "",   "", "See Gen. I, 16", ""),
    (167, 3, "F", "Nămăiʼ",          "",       "40", "Oak",    "",   "", "See Gen. I, 17", ""),
    (168, 3, "M", "Kowăuʼsh˙dyiwă",  "",       "42", "Sun",    "",   "", "See Gen. I, 18", ""),
    (169, 3, "F", "Haiʼtyʼʼimăiʼ",   "",       "43", "Parrot", "",   "",
     "See Gen. I, 19 / For first husband and descendants, see below",
     "appears twice within the lower block; drawn once. A heavy ink stroke runs "
     "from this line's clan to its sibling bracket on the scanned copy -- it is "
     "not type, and is recorded as an observation of this copy, not as data"),
    (170, 3, "M", "Kʼuʼn˙ash",       "",       "",   "Sun",    "",   "", "See Gen. I, 20",
     "trailing mark after 'ash' unverified -- SEE TODO"),
    (171, 3, "F", "Shayaʼai",        "",       "",   "Sun",    "",   "", "See Gen. I, 21",
     "number printed without a following period"),
    (172, 3, "M", "Dziraiʼᶦtyʼi",     "",       "",   "Sun",    "",   "", "See Gen. I, 22", ""),
    (173, 3, "F", "Dziʼs˙dyuwi",      "",       "",   "Bear",   "d.", "", "See Gen. I, 23", ""),
    (174, 3, "M", "Shta˙ʼyăi",        "",       "",   "",       "",   "", "",
     "no clan printed; name printed without a following period"),
    (175, 3, "F", "Kio˙ʼd˙yiăi",      "",       "",   "Bear",   "",   "", "", ""),
    (176, 3, "F", "Dzaʼwaiʼᶦy˙unăiʼ", "",       "",   "Sun",    "",   "", "", ""),
    (177, 3, "M", "Maiʼs˙iwă",        "",       "",   "Turkey", "",   "", "",
     "set in noticeably larger type than the lines around it -- an observation "
     "of this copy's setting, not data"),
    (178, 3, "F", "Shuwăiʼ",          "",       "",   "Chaparral Cock", "", "", "", ""),
    (179, 3, "M", "",                 "",       "",   "White",  "",   "", "",
     "name printed as a dash. 'White' stands where every other line prints a "
     "clan. Recorded as printed, not interpreted"),
    (180, 3, "F", "Säpʼᵃ",            "",       "",   "Bear",   "d.", "", "",
     "diaeresis on 'a' (U+00E4) -- a codepoint neither Table 1 nor Table 4 "
     "uses. Confirmed at a 330 px crop"),
    (181, 3, "M", "Ma˙tsʼăĭ yăiʼ",    "",       "",   "Bear",   "",   "", "",
     "the plate sets this name as two words, with a space; confirmed at a "
     "460 px crop"),
    (182, 3, "F", "Gwiʼtyʼi",         "",       "",   "Sun",    "",   "", "", ""),
    (183, 3, "M", "",                 "",       "",   "Mexican", "",  "", "",
     "name printed as a dash. 'Mexican' stands where every other line prints a "
     "clan, as 'White' does at 179. Recorded as printed, not interpreted. "
     "This is the first husband of 169, whose line here carries 'For second "
     "husband and descendants, see above'"),
    (184, 3, "M", "Djaiʼd˙ziĕ",       "",       "30", "Parrot", "",   "", "", ""),
    (185, 3, "F", "Kăauʼd˙yuwi",      "",       "35", "Corn",   "",   "", "", ""),
    (234, 4, "F", "Go˙ʼyăiʼ",         "",       "",   "Eagle",  "",   "", "",
     "second wife of 54, printed as a second '+' line under him below 53. "
     "Generation follows her husband's upper-block value, not her column in "
     "the lower block -- see the block-frame question at Gate 2"),
    (235, 3, "M", "Charley Kai",      "",       "",   "Sun",    "",   "", "",
     "English name printed as the name itself, as at 116-118, 128 and 134"),
    (236, 3, "F", "Kaweishdyiŭr",     "",       "",   "Water",  "",   "", "", ""),
    (237, 3, "F", "Tsʼid˙yuwiʼ",      "",       "",   "Sun",    "d.", "", "", ""),
    (238, 3, "M", "Yo˙rimăiʼ",        "Fred Kai", "", "Sun",    "",   "", "",
     "English name printed in parentheses on the plate"),
    (239, 3, "F", "Dziwiʼs˙dy˙uwi",   "",       "",   "Chaparral Cock", "", "", "", ""),
    (240, 3, "F", "Dzi˙d˙jaʼai",      "",       "",   "Sun",    "d.", "", "", ""),
    (241, 3, "M", "Tsiyusiĕ",         "",       "",   "Parrot", "",   "", "", ""),
    (242, 3, "M", "Shaaiʼshdyiăi",    "",       "",   "Sun",    "",   "", "", ""),
    (243, 3, "F", "",                 "",       "",   "Mohave", "",   "", "",
     "name printed as a dash. 'Mohave' stands where every other line prints a "
     "clan, as 'White' does at 179 and 'Mexican' at 183. Recorded as printed, "
     "not interpreted"),
    # Column C of the lower block ends here, at 243.

    # ---- lower block, generation 4 (column D) ---------------------------
    # 186 and 188-195 sit at one indent: they are siblings, not mother and
    # children -- 186 is 23 and 188 is 22. Their Oak clan and their "See Gen.
    # I" numbers both point at 167 (Nămăiʼ, Oak, 40) as the mother.
    (186, 4, "F", "Shăaityʼid˙yuweʼ", "",       "23", "Oak",    "",   "", "", ""),
    (187, 4, "M", "Ramona of Sant Ana", "",     "50", "Turkey", "",   "", "",
     "the plate prints the name with a place, spelled 'Sant Ana'. Recorded as "
     "printed, not normalised"),
    (188, 4, "F", "Kiwaʼd˙yuwi",      "",       "22", "Oak",    "",   "", "See Gen. I, 33",
     "Gen. I 33 is this same woman by name and clan but prints her age as 18. "
     "Both are recorded as each plate prints them"),
    (189, 4, "F", "Ko˙ri",            "",       "21", "Oak",    "",   "", "See Gen. I, 31", ""),
    (190, 4, "M", "Tsᶦgaiʼs˙iwăʼ",    "",       "20", "Oak",    "",   "", "See Gen. I, 32",
     "this line crosses a fold crease and the medial 's˙i' reads ambiguously "
     "as 's˙i' or 'sʼï' at any crop. Gen. I 32 is the same man and prints "
     "'Tsᶦgaiʼs˙iwăʼ' on a far better-resolved plate; that settles it"),
    (191, 4, "M", "Tsiʼd˙yimĕ",       "",       "17", "Oak",    "",   "", "See Gen. I, 34",
     "no trailing apostrophe here, where Gen. I 34 prints 'Tsiʼd˙yimĕʼ'. "
     "Confirmed at a 620 px crop; each plate is recorded as it prints"),
    (192, 4, "F", "Sha˙tyʼi",         "",       "14", "Oak",    "",   "", "See Gen. I, 35", ""),
    (193, 4, "M", "Aiʼwanăi",         "",       "8",  "Oak",    "",   "", "See Gen. I, 36", ""),
    (194, 4, "M", "Dyăiʼtsdyămŭr",    "",       "6",  "Oak",    "",   "", "See Gen. I, 37", ""),
    (195, 4, "M", "Iyăiʼs˙dyiwă",     "",       "5",  "Oak",    "",   "", "See Gen. I, 38", ""),
    (196, 4, "F", "Kăauʼshurtsʼa",    "",       "9",  "Parrot", "",   "", "See Gen. I, 40", ""),
    (197, 4, "M", "Onăiʼ",            "",       "8",  "Parrot", "",   "", "See Gen. I, 41", ""),
    (198, 4, "F", "Wamais",           "",       "7",  "Parrot", "",   "", "See Gen. I, 42",
     "no trailing marks here, where Gen. I 42 prints 'Wamais˙ʼ'"),
    (199, 4, "M", "Gaishpidjaʼtyᵃ˙",  "",       "6",  "Parrot", "",   "", "See Gen. I, 43 (?)",
     "THE QUESTION MARK IS PARSONS'S OWN, printed on the plate after the "
     "reference. It is the only cross-reference on this plate that carries one, "
     "and it is warranted: Gen. I 43 is 'Yoʼd˙yidyăiʼ', a different name. Copy "
     "the '(?)' through to the page -- it is her doubt, not ours. Trailing "
     "superscript a then raised dot, confirmed at a 260 px crop"),
    (200, 4, "M", "Hea˙ʼshdyĭwă",     "",       "",   "Parrot", "d. 1917, at 2", "", "See Gen. I, 44",
     "Gen. I 44 prints 'Hea˙ʼsh˙dyĭwă' and 'd. 1917, aged 2'. Each plate is "
     "recorded as it prints"),
    (201, 4, "M", "Dziwaiʼi˙siro",    "",       "",   "Sun",    "",   "", "See Gen. I, 45",
     "raised dot after the medial 'i', which Gen. I 45 does not print"),
    (202, 4, "F", "Kuyăiʼd˙yid˙uweʼ", "",       "",   "Sun",    "",   "", "See Gen. I, 48",
     "no 'y' before 'uweʼ', where Gen. I 48 prints 'Kuyăiʼd˙yid˙yuweʼ'. "
     "Confirmed at a 480 px crop"),
    (203, 4, "F", "Edna",             "",       "",   "Sun",    "",   "", "",
     "English name printed as the name itself; no cross-reference on this line"),
    (204, 4, "F", "Yăaiʼdyid˙yuwi",   "",       "",   "Sun",    "",   "", "See Gen. I, 49", ""),
    (205, 4, "M", "Owi˙ʼd˙zĭraiʼ",    "",       "",   "Sun",    "",   "", "See Gen. I, 47", ""),
    (206, 4, "F", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (207, 4, "M", "",                 "",       "",   "Bear",   "",   "", "", "name printed as a dash"),
    (208, 4, "F", "Gaaish",           "",       "",   "Bear",   "",   "", "See Gen. I, 53",
     "Gen. I 53 is 'Gaaiʼd˙yuitsʼa', F, Bear, aged 3 -- the same girl under a "
     "shorter form of the name. Each plate is recorded as it prints"),
    (209, 4, "F", "Onăiʼ",            "",       "10", "Bear",   "",   "", "", ""),
    (210, 4, "M", "Niăiʼ",            "",       "4",  "Bear",   "",   "", "", ""),
    (211, 4, "M", "Shʼauwiăiʼ",       "",       "3",  "Bear",   "",   "", "", ""),
    # 212-219 print no sex letter: number, dash, clan only -- the same setting
    # as 85-100 and 106-115 in the upper block. Stored empty, not guessed.
    (212, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (213, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (214, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (215, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (216, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (217, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (218, 4, "",  "",                 "",       "",   "Chaparral Cock", "", "", "", "no sex printed; name printed as a dash"),
    (219, 4, "",  "",                 "",       "",   "Chaparral Cock", "", "", "", "no sex printed; name printed as a dash"),
    (220, 4, "F", "Shauʼkʼămă",       "",       "15", "Sun",    "",   "", "", ""),
    (221, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (222, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (223, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (224, 4, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (225, 4, "",  "Shauʼd˙yidĕ",      "",       "15", "Parrot", "",   "", "",
     "no sex printed, although this line does carry a name and an age. Every "
     "other sexless line on the plate prints a dash for the name as well; this "
     "is the only one that does not. Confirmed at an 800 px crop"),
    (226, 4, "",  "",                 "",       "",   "Parrot", "d.", "", "", "no sex printed; name printed as a dash"),
    (227, 4, "M", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),
    (228, 4, "F", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),

    # ---- lower block, generation 5 (column E) ---------------------------
    # 229-231 are the children of 186+187. All Oak, as 186 is.
    (229, 5, "F", "Shawityi",         "",       "6",  "Oak",    "",   "", "", ""),
    (230, 5, "M", "Awie˙",            "",       "4",  "Oak",    "",   "", "", ""),
    (231, 5, "M", "Yoreni",           "",       "1",  "Oak",    "",   "", "", ""),

    # ---- the 232+233 branch's grandchildren -----------------------------
    # 244-253 hang off 234's line, and every one of them is Eagle, which is
    # 234's clan and not 54's Sun. So they are the children of 54+234.
    # Their generation therefore follows 54's upper-block value + 1 = 5, even
    # though they are printed in the same column D as the lower block's
    # generation 4. See the GENERATION FRAME note below: this is the same
    # unresolved question, showing up in the data.
    (244, 5, "F", "Dyaiyo˚wăiʼ",      "",       "",   "Eagle",  "",   "", "",
     "ring above (U+02DA) between 'yo' and 'wăiʼ' -- a codepoint neither "
     "Table 1 nor Table 4 uses. Confirmed at a 240 px crop; present in both "
     "master Gentium faces"),
    (245, 5, "M", "Kaiyaiʼ",          "",       "",   "Corn",   "",   "", "", ""),
    (246, 5, "F", "Shatsʼăiʼ",        "",       "",   "Eagle",  "",   "", "", ""),
    (247, 5, "M", "Joe Mantoya of Jemez", "",   "",   "",       "",   "", "",
     "no clan printed. The plate prints the name with a place, spelled "
     "'Mantoya' and 'Jemez'. Recorded as printed, not normalised"),
    (248, 5, "M", "Oyo˙ʼyʼăi",        "",       "",   "Eagle",  "",   "", "", ""),
    (249, 5, "M", "Dzi˙ʼyaid˙yiʼwă",  "",       "",   "Eagle",  "",   "", "", ""),
    (250, 5, "F", "Ga˙ʼwiaitsʼă",     "",       "",   "Eagle",  "",   "", "", ""),
    (251, 5, "M", "Rioʼ",             "",       "",   "Eagle",  "",   "", "", ""),
    (252, 5, "F", "Ganaiʼ",           "",       "",   "Eagle",  "",   "", "", ""),
    (253, 5, "F", "Tsʼa˙ʼshdjdyuweʼ", "",       "",   "Eagle",  "",   "", "", ""),

    # ---- lower block, generation 4 resumes (column D) -------------------
    # 254-260 are Water, which is 236's clan, so they hang off 235+236.
    (254, 4, "F", "Lina",             "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself"),
    (255, 4, "M", "Kaauʼstyiăiʼ",     "",       "",   "Eagle",  "",   "", "",
     "this '+' line also carries a leader rule entering from the left, which "
     "no other '+' line on the plate does. Noted for Gate 2, not interpreted"),
    (256, 4, "F", "Gʼawaidyuwi",      "",       "",   "Water",  "",   "", "", ""),
    (257, 4, "M", "John Perry",       "",       "",   "Eagle",  "",   "", "",
     "English name printed as the name itself"),
    (258, 4, "M", "Oʼkʼaiyă",         "",       "",   "Water",  "",   "", "", ""),
    (259, 4, "F", "Kʼataiʼd˙yuwĕʼ",   "",       "",   "Water",  "",   "", "",
     "number printed without a following period, as at 19 and 171"),
    (260, 4, "M", "Willi",            "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself"),
    # 261-264 are Chaparral Cock, which is 239's clan, so they hang off
    # 238+239. 265-269 are Sun, and 268-269 print no clan at all.
    (261, 4, "F", "",                 "",       "",   "Chaparral Cock", "", "", "", "name printed as a dash"),
    (262, 4, "M", "John",             "",       "",   "Chaparral Cock", "", "", "",
     "English name printed as the name itself"),
    (263, 4, "M", "Dyumaiʼ",          "",       "",   "Chaparral Cock", "", "", "", ""),
    (264, 4, "F", "",                 "",       "",   "Chaparral Cock", "", "", "",
     "name printed as a dash, followed by a period -- the only dashed name on "
     "the plate that carries one"),
    (265, 4, "M", "Naisiyĕ",          "",       "",   "Sun",    "",   "", "", ""),
    (266, 4, "M", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (267, 4, "F", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (268, 4, "",  "",                 "",       "",   "",       "",   "", "",
     "no sex printed; name and clan both printed as dashes"),
    (269, 4, "",  "",                 "",       "",   "",       "",   "", "",
     "no sex printed; name and clan both printed as dashes"),
    # Column D of the lower block ends here, at 269.

    # ---- lower block, generation 5 (column E) ---------------------------
    # 270-274 are all Water. 254's rule carries 270-272 and 256's carries
    # 273-274; both women are Water.
    (270, 5, "M", "Kʼauʼwină",        "",       "",   "Water",  "",   "", "", ""),
    (271, 5, "F", "Dziaid˙yuwe",      "",       "",   "Water",  "",   "", "", ""),
    (272, 5, "F", "Josephine",        "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself"),
    (273, 5, "F", "Dziᶦʼyăiʼ",        "",       "",   "Water",  "",   "", "", ""),
    (274, 5, "F", "Naiyaisiroʼ",      "",       "",   "Water",  "",   "", "", ""),
    # THE PLATE'S NUMBERING ENDS AT 274.
]

# ---------------------------------------------------------------------------
# CROSS_REF_OFFSET -- Parsons's references into Genealogy I run one high
#
# Every "See Gen. I, n" on this plate was checked against scripts/transcription.py
# by name, sex and clan. The references fall into two groups:
#
#   EXACT      -- 20 -> Gen. I 11; 67 -> 24; 68 -> 25; 72 -> 26; 73 -> 27
#                 and, added 2026-07-29 from the lower block's column D, eight
#                 more, every one an exact name-and-clan match:
#                   188 -> Gen. I 33 (Kiwaʼd˙yuwi, F, Oak)
#                   189 -> Gen. I 31 (Ko˙ri, F, Oak)
#                   190 -> Gen. I 32 (Tsᶦgaiʼs˙iwăʼ, M, Oak)
#                   191 -> Gen. I 34 (Tsiʼd˙yimĕʼ, M, Oak)
#                   192 -> Gen. I 35 (Sha˙tyʼi, F, Oak)
#                   193 -> Gen. I 36 (Aiʼwanăi, M, Oak)
#                   194 -> Gen. I 37 (Dyăiʼtsdyămŭr, M, Oak)
#                   195 -> Gen. I 38 (Iyăiʼs˙dyiwă, M, Oak)
#                 and nine more from the same column:
#                   196 -> Gen. I 40 (Kăauʼshurtsʼa, F, Parrot)
#                   197 -> Gen. I 41 (Onăiʼ, M, Parrot)
#                   198 -> Gen. I 42 (Wamais˙ʼ, F, Parrot)
#                   200 -> Gen. I 44 (Hea˙ʼsh˙dyĭwă, M, Parrot, d. 1917)
#                   201 -> Gen. I 45 (Dziwaiʼisiro, M, Sun)
#                   202 -> Gen. I 48 (Kuyăiʼd˙yid˙yuweʼ, F, Sun)
#                   204 -> Gen. I 49 (Yăaiʼdyid˙yuwi, F, Sun)
#                   205 -> Gen. I 47 (Owi˙ʼd˙zĭraiʼ, M, Sun)
#                   208 -> Gen. I 53 (Gaaiʼd˙yuitsʼa, F, Bear)
#                 So the exact range runs to at least Genealogy I's person 53,
#                 not merely its 27. THE FOOTNOTE COPY MUST SAY 53.
#
#   PARSONS'S OWN DOUBT -- 199 prints "See Gen. I, 43 (?)". It is the only
#                 reference on the plate with a question mark, and the only one
#                 in the exact range that does not match: Gen. I 43 is
#                 Yoʼd˙yidyăiʼ, not Gaishpidjaʼtyᵃ˙. Carry the "(?)" through.
#   ONE HIGH   -- 61 prints 67, names Gen. I 66 (Tsikʼayăaiʼtsʼa, F, Eagle, d.)
#                 60 prints 68, names Gen. I 67 (Shuwaiʼᶦri, M, Turkey)
#                 62 prints 77, names Gen. I 76 (Dziwiʼd˙yăi, F, 33, Badger --
#                                                name AND age match)
#                 137 prints 81, names Gen. I 80 (Shauʼm˙ăiʼ, M, Eagle)
#                 138 prints 82, names Gen. I 81 (---, M, Eagle)
#                 140 prints 91, names Gen. I 90 (Heʼsa (Hazel), F, Badger)
#                 141 prints 92, names Gen. I 91 (Dzăiyăiʼ, F, Badger)
#
# So the references are exact through Genealogy I's person 53 and one too high
# from at least its person 66 onward. Twenty-two independent name matches in
# the exact range, seven in the displaced one, all +1. Nothing between 54 and
# 65 is referenced from this plate, so where the displacement begins is not
# determinable from these two plates alone -- say "from person 66 onward",
# not "from person 54".
#
# THIS BEARS ON TABLE 1, WHICH IS ALREADY PUBLISHED. Table 1's own misprint
# (PLATE_NUMBER_MISPRINTS = {"U23": 68}) prints 68 for person 67 -- Shuwaiʼᶦri
# -- and Table 2 independently calls that same man 68. The two are one
# phenomenon, not two unrelated slips: Parsons was working from a numbering of
# Genealogy I that ran one ahead of the one finally printed.
#
# NOTHING IS CORRECTED HERE. cross_ref carries what the plate prints.
#
# DECIDED 2026-07-29 (user): note it on BOTH published pages.
#   - Table 2 gets a footnote saying its references into Genealogy I are exact
#     through person 27 and one high from person 66 onward, with the matched
#     names as the evidence.
#   - Table 1's existing #note-misprint gains a sentence: the same displacement
#     appears independently on Table 2, which also calls Shuwaiʼᶦri 68. That
#     STRENGTHENS the standing decision to print 68 rather than "fix" it to 67
#     -- the number is Parsons's, not a typesetter's slip.
# Both are apparatus edits, so both go through _p() at each call site, never a
# regex over the prose. Editing Table 1's apparatus touches a published, cited
# page: re-verify that page after building.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# DUPLICATE_PLATE_NUMBERS
#
# Parsons numbers two different people 101 in generation 5 -- "101. F.
# Naauʼg˙ŭyăiʼ. Water" and, on the next line, "101. M. ---. d. Water",
# followed normally by 102. Confirmed at high magnification; it is not a
# scanning artefact and not a broken 100.
#
# This is a DIFFERENT class of error from Table 1's, and the existing
# machinery does not cover it. Table 1's PLATE_NUMBER_MISPRINTS maps a UNION
# to the number printed on its '+' line -- one person, wrongly numbered. Here
# two distinct people carry one number, so the ids cannot be both unique and
# equal to what the plate prints.
#
# DECIDED 2026-07-29 (user): internal id + printed number. The synthetic id
# below exists only so anchors, links and the register have something unique to
# address; the CHART, THE REGISTER AND THE CARD ALL PRINT 101, for both people.
# This is the separation Table 1 already makes between a person's id and the
# number the plate puts on their row -- carried to the card as data-printed --
# so extend that path rather than adding a second one. A footer note explains
# that two people are numbered alike. Do not renumber to 101a/101b: that would
# print something the plate does not.
#
# Read as: {internal id: the number the plate prints}
# ---------------------------------------------------------------------------
DUPLICATE_PLATE_NUMBERS = {1010: 101}

# ---------------------------------------------------------------------------
# STATE -- every plate number is read; the structure is not encoded
#
# DONE:  plate numbers 1-274, every one of them, plus the second 101. 275
#        records, no gaps, no id collisions. The numbering ends at 274 --
#        verified by sweeping the plate's right margin, which is blank past
#        column E in both halves of the lower block.
# TO DO: UNIONS and CHILDREN, for the whole plate, including the part read in
#        the earlier session. Then the SEE TODO readings, then Gate 3.
#
# WHERE EACH COLUMN WAS READ, in native pixel coordinates of
# sources/parsons-1923-table-2.jpg. Columns are ~1300-1500 px wide and text
# lines are ~65 px; tiles of about 1450-1600 x 1250 read cleanly with no
# downscaling by the image reader. Keep these -- re-reading a line during
# Gate 2 is a one-command job with them:
#   lower col C  x 3760, y 8550-12680   -> 172-185, 125/126, 53/54/234, 235-243
#   lower col D  x 4870, y 6150-12680   -> 186-228, 244-269
#   lower col E  x 6000, y 6330         -> 229-231
#   lower col E  x 6050, y 11500        -> 270-274
# A tile helper that takes (left, top, width, height) is three lines of sips:
#   sips -c <height> <width> --cropOffset <top> <left> <scan> --out tile.jpg
#
# GLYPH READINGS STILL UNVERIFIED (grep "SEE TODO"). Each is a tighter crop's
# work. Two are worth doing first because they would add a codepoint:
#   - 14  Kʼaiʼsh˙dŏwăʼ   breve over 'o' (U+014F)
#   - 84  Ha˙tsʼᵉ         superscript e (U+1D49) -- this one IS confirmed
#   - 45, 52, 59, 64, 80, 135, 142, 146, 20, 21: trailing or medial marks
#
# AND THREE PEOPLE DRAWN TWICE WHOSE TWO OCCURRENCES DISAGREE. These are a
# different kind of open item from the marks above, and the difference is the
# point: THEY ARE NOT READING PROBLEMS. 125's pair was re-read at 380 px on
# 2026-07-29 and both settings are unambiguous at that size. The plate simply
# prints one person's name two ways, and the edition must print one. That is
# an EDITORIAL choice and it belongs to the user:
#   - 13   Dzia˙ʼyotsʼa / Tsiaiutsa          (upper reading the less certain)
#   - 54   Ma˙ʼrani / Ma˙ʼran˙i              (one raised dot apart)
#   - 125  Gowaʼk˙ʼd˙yăiʼ / Gowaʼkʼad˙zăiʼ   (both crops verified legible)
# Each record carries the coordinates of both occurrences. 169's two
# occurrences agree; it is named here only so nobody hunts for a fourth.
#
# Note this is the same phenomenon that shows up BETWEEN plates, where it is
# not a problem at all: 191 vs Gen. I 34, 198 vs Gen. I 42, 200 vs Gen. I 44,
# 202 vs Gen. I 48 all differ in a mark, and there each plate is simply
# recorded as it prints. Only the within-plate repeats force a choice.
#
# ONE MORE WORTH A LOOK: 135 reads "Săp" with a breve in the upper block,
# while 180 in the lower block clearly reads "Säpʼᵃ" with a diaeresis and a
# superscript a. They are different people -- 135 is Turkey, 180 is Bear -- so
# this is not a repeat-person discrepancy, but 180's crop is the better one
# and it is worth re-reading 135 against it.
#
# FONT COVERAGE IS NOT A PROBLEM. The cmap of both master faces
# (vendor/gentium/Gentium-{Regular,Italic}.ttf) was checked directly and
# carries U+014F, U+02D1, U+1D49 and -- checked 2026-07-29 for the two
# codepoints the lower block added -- U+00E4 and U+02DA, as well as the marks
# already in use. So Gate 4 is a re-run of scripts/subset_font.py once the
# readings are final; there is nothing to source. Do not judge this by looking
# at rendered text: macOS substitutes silently for any missing face.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# STRUCTURE CONFIRMED SO FAR (Gate 1 tracing, generations 1-4)
#
# Read off the plate's brackets and then checked against matrilineal descent --
# a child's clan must equal its mother's. Every group below passes that check,
# and in three places the check is what decided an ambiguous bracket.
#
#   1+2  ->  3, 5, 7                 (one founding couple, not three: a single
#                                     vertical rule off person 1's row carries
#                                     all three daughters. All Water, as 1 is.)
#   3+4  ->  9, 11                   Water
#   5+6  ->  13                      Water
#   7+8  ->  15, 17, 19, 22, 24      Water
#
#   15+16 -> 56, 58, 60, 63, 64      Turkey  (16 is Turkey)
#   17+18 -> 65, 66                  Corn    (18 is Corn)
#   19+20/21 -> 67..74               Water   (19 is Water)
#   22+23 -> 75..79                  Lizard  (23 is Lizard)
#   24+25 -> 80, 81, 82              Bear    (25 is Bear)
#
# THE THREE THE CLAN RULE DECIDED:
#   - 64 sits on 17's row on the plate but is Turkey, and 17's wife 18 is Corn.
#     It belongs to 15+16, whose other children are all Turkey. Reading the
#     row alignment alone would have put it in the wrong sibling group.
#   - 47's line carries two '+' spouses, 48 (F, Parrot) and 49 (M, Turquoise).
#     49 cannot be 47's spouse; he is 48's second husband. Children 116-118 are
#     Parrot -- 48's clan -- so the group hangs off 48's line.
#   - 51+52: children 119-121 are Lizard, which is 52's clan, not 51's Water.
#
# STILL TO TRACE: the generation 4 -> 5 brackets (26-82 -> 83-143) and
# 5 -> 6 (119-123 -> 144-153), then the rest of the lower block.
#
# LOWER BLOCK, traced so far:
#   154+155 -> 14, 156, 158, 161, 162, 164   Parrot (154 is Parrot)
#   156+157 -> 166, ...                      Sun    (157 is Sun)
#   158+159 -> 174, 176                      Sun    (159 is Sun)
#   158+160 -> 126, 178                      Chaparral Cock (160 is C. Cock)
#   232+233 -> 54                            Sun    (232 is Sun)
#
# ADDED 2026-07-29, from the columns read this session. Each was read off the
# brackets AND passes the clan check; where the bracket alone was ambiguous,
# the clan is what decided it, and that is said explicitly:
#   166+167 -> 186, 188-195                  Oak    (167 is Oak; the eight
#              "See Gen. I" numbers land on Genealogy I's own sibling group
#              31-38, whose mother there is its person 17 -- and 167 carries
#              "See Gen. I, 17". Two independent confirmations.)
#   186+187 -> 229, 230, 231                 Oak    (186 is Oak, 187 Turkey)
#   53+54   -> 122, 147-151                  Water  (53 is Water. The plate
#              does not draw them here: the slot in column D carries the line
#              "For descendants see 122, 147-151" instead. That text is an
#              INTERNAL cross-reference, the only one on the plate that points
#              at this plate's own numbers, and it is not a person record.)
#   54+234  -> 244-253                       Eagle  (234 is Eagle, 54 is Sun.
#              The clan is the whole argument: ten children in a row, every
#              one Eagle, hanging off 234's rule and not 53's.)
#   235+236 -> 254, 256, 258, 259, 260       Water  (236 is Water, 235 Sun)
#   238+239 -> 261-264                       Chaparral Cock (239 is C. Cock)
#   254+255 -> 270, 271, 272                 Water  (254 is Water, 255 Eagle)
#   256+257 -> 273, 274                      Water  (256 is Water, 257 Eagle)
#
# STILL UNASSIGNED in the lower block: 172/173, 180-185, 196-228, 237, 240-243,
# 265-269. Their columns and clans are recorded; their brackets are not traced.
#
# *** THE TWO BLOCKS' GENERATION FRAMES -- RESOLVED 2026-07-29 ***
#
# The `generation` field in PERSONS above is currently written in TWO frames:
# the upper block's own, and a lower-block-local one where 154+155 are
# "generation 1". They differ by exactly one, and the conversion is
#
#     upper generation == lower generation + 1
#
# so 154+155 sit at upper generation 2 and the plate is six generations deep
# counted either way. Under that conversion every column of the lower block
# maps to one upper generation, with no column holding two:
#
#     lower col A (154, 155)                  -> upper 2
#     lower col B (156-165, 232, 233)         -> upper 3
#     lower col C (166-185, 234-243)          -> upper 4
#     lower col D (186-228, 244-269)          -> upper 5
#     lower col E (229-231, 270-274)          -> upper 6
#
# HOW THE THIRD ANCHOR DISSOLVED. It looked for a while as though 126 broke
# this: he is stored at upper generation 5 and he is a child of 158+160, who
# are lower generation 2, which would force lower 2 == upper 4. The upper
# block settles it -- crop x 4700, y 3010, 1300 x 340. There, 125 is the CHILD
# line and "+ 126" is her SPOUSE line; in the lower block the roles swap, 126
# being the child and "+ 125" the spouse. So 126's stored 5 is his WIFE's
# generation, taken from the line he is printed beside, and says nothing about
# his own descent. His own descent puts him at upper 4. Not an anchor at all.
#
# The other two agree and are what the table above is built on:
#   - 13 and 14 are upper generation 3 and are children of 154+155
#     => 154+155 are upper generation 2.
#   - 54 is upper generation 4 and is the son of 232+233
#     => 232+233 are upper generation 3, i.e. lower column B, which is exactly
#        the indent they are printed at. Their stored "generation 1" is wrong;
#        "founding couple" means no parents are drawn, not column A.
#
# WHAT TO DO ABOUT IT -- and the reason it is NOT done here. `generation` is
# not a layout input. make_chart.py reads it in exactly one place that matters,
# `n_gens = max(...)`, to print "N generations" in the page copy; the chart's
# columns come from walking UNIONS and CHILDREN, not from this field. So the
# frames being mixed cannot bend the plate. Rather than hand-renumber 120-odd
# records off their column positions now, DERIVE the field from the traced tree
# during Gate 2, when every bracket is encoded and the depth falls out for
# free. Hand-renumbering from columns would put a guess where a derivation
# belongs.
#
# Two records need a decision even so, and neither is arithmetic:
#   - 126, whose descent is drawn in the lower block (upper 4) but who is
#     printed beside a wife at upper 5. Take the generation from the descent
#     the plate actually draws.
#   - 169, drawn twice inside the lower block, currently 3, column C, so 4.
#
# THREE FOUNDING COUPLES ON THIS PLATE, not two: 1+2, 154+155, and 232+233.
# 232 was the trap -- it is printed at the same indent as 158 and 164, which
# are children, but no leader rule enters it from the left. Checked at native
# resolution. Its clan settles it independently: 232 is Sun and 154 is Parrot,
# so 232 cannot be 154's daughter.
#
# *** THE TWO BLOCKS ARE ONE GENEALOGY, NOT TWO. ***
# People drawn in the upper block reappear in the lower one, exactly as
# Table 1's person 8 and Table 4's 3 and 4 do:
#   13, 14   drawn in the upper block; the lower repeat carries
#            "For descendants, see above"
#   125, 126 drawn in the upper block as a couple; 126 reappears as a child
#            of 158+160, whose Chaparral Cock clan he carries
#   53, 54   drawn in the upper block as a couple; 54 reappears as the son of
#            232+233, whose Sun clan he carries
#   169      appears twice inside the lower block itself, once with
#            "For first husband and descendants, see below" and once with
#            "For second husband and descendants, see above"
# Each such person is stored ONCE. The repeat becomes a cross-reference. Do
# not create a second record for any of them -- the ids above already exist.
#
# CROSS-REFERENCES OUT OF THIS PLATE go to Genealogy I (published) and
# Genealogy III (NOT transcribed -- 160 and 163 both point into it). A link
# must not promise content: the landing page's `#pending-3` anchor exists for
# exactly this, and nothing may link to Genealogy III until it ships.
#
# FOUR LINES PRINT SOMETHING OTHER THAN A CLAN where every other line prints
# one: 179 "White", 183 "Mexican", 243 "Mohave", and -- as part of the name
# rather than the clan field -- 187 "Ramona of Sant Ana" and 247 "Joe Mantoya
# of Jemez", both of whom have no clan printed at all. They are recorded as
# printed and NOT interpreted, and the clan field carries the word verbatim.
# Note what this does to the clan check at Gate 3: none of the five is a
# mother, so no child's clan is tested against one of these words. If a later
# reading ever makes one of them a mother, that is the moment to decide
# whether these belong in `clan` at all -- not before.
# ---------------------------------------------------------------------------

UNIONS = [
    # (union_id, wife_id, husband_id, wife_order, husband_order, note)
]

CHILDREN = [
    # (union_id, mother_id, father_id, child_id, note)
]
