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
    (54, 4, "M", "Ma˙ʼrani",         "",       "",   "Sun",    "",   "", "", ""),
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
    (125, 5, "F", "Gowaʼk˙ʼd˙yăiʼ",  "",       "18", "Water",  "",   "", "", ""),
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
]

# ---------------------------------------------------------------------------
# CROSS_REF_OFFSET -- Parsons's references into Genealogy I run one high
#
# Every "See Gen. I, n" on this plate was checked against scripts/transcription.py
# by name, sex and clan. The references fall into two groups:
#
#   EXACT      -- 20 -> Gen. I 11; 67 -> 24; 68 -> 25; 72 -> 26; 73 -> 27
#   ONE HIGH   -- 61 prints 67, names Gen. I 66 (Tsikʼayăaiʼtsʼa, F, Eagle, d.)
#                 60 prints 68, names Gen. I 67 (Shuwaiʼᶦri, M, Turkey)
#                 62 prints 77, names Gen. I 76 (Dziwiʼd˙yăi, F, 33, Badger --
#                                                name AND age match)
#                 137 prints 81, names Gen. I 80 (Shauʼm˙ăiʼ, M, Eagle)
#                 138 prints 82, names Gen. I 81 (---, M, Eagle)
#                 140 prints 91, names Gen. I 90 (Heʼsa (Hazel), F, Badger)
#                 141 prints 92, names Gen. I 91 (Dzăiyăiʼ, F, Badger)
#
# So the references are exact through Genealogy I's person 27 and one too high
# from at least its person 66 onward. Six independent name matches, all +1.
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
# STATE -- upper block read, lower block not started
#
# DONE:  plate numbers 1-153, six generations, 154 records (the extra is the
#        second person numbered 101). No gaps, no id collisions.
# TO DO: persons 154 to roughly 269 -- the entire lower block, joined to this
#        one at the couple 154+155 -- then UNIONS and CHILDREN for both.
#
# GLYPH READINGS STILL UNVERIFIED (grep "SEE TODO"). Each is a tighter crop's
# work; none blocks reading the lower block. Two are worth doing first because
# they would add a codepoint to the edition:
#   - 14  Kʼaiʼsh˙dŏwăʼ   breve over 'o' (U+014F)
#   - 84  Ha˙tsʼᵉ         superscript e (U+1D49) -- this one IS confirmed
#   - 45, 52, 59, 64, 80, 135, 142, 146, 20, 21: trailing or medial marks
#
# FONT COVERAGE IS NOT A PROBLEM. The cmap of both master faces
# (vendor/gentium/Gentium-{Regular,Italic}.ttf) was checked directly and
# carries U+014F, U+02D1 and U+1D49 as well as the marks already in use. So
# Gate 4 is a re-run of scripts/subset_font.py once the readings are final --
# there is nothing to source. Do not judge this by looking at rendered text:
# macOS substitutes silently for any missing face.
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
# ---------------------------------------------------------------------------

UNIONS = [
    # (union_id, wife_id, husband_id, wife_order, husband_order, note)
]

CHILDREN = [
    # (union_id, mother_id, father_id, child_id, note)
]
