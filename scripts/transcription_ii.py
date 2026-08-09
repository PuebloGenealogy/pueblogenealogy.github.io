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
    (13, 3, "F", "Dzia˙ʼyotsʼa",     "Tsiaiutsa", "", "Water", "d.", "",
     "For descendants, see above",
     "DISCREPANCY, and now a VERIFIED one. The plate prints this person twice "
     "and the two readings do not agree: 'Dzia˙ʼyotsʼa' in the upper block, "
     "'Tsiaiutsa' in the lower. BOTH were re-read at high magnification on "
     "2026-07-29 -- upper at x 2650 y 1740, lower at x 2820 y 6180 -- and "
     "both are unambiguous. The lower carries no diacritics at all. So the "
     "earlier note's 'the upper reading is the less certain' is withdrawn: "
     "neither is uncertain, and these are not variant readings of one setting "
     "but two different settings of one name. DECIDED 2026-07-29 (user): "
     "carry BOTH, upper first, lower in alt_name -- see REPEAT_PERSON_NAMES. "
     "These two are the furthest apart of the three: not a spelling variant "
     "but a different name"),
    (14, 3, "M", "S˙ʼiʼrowaisiwa",   "Kʼaiʼsh˙dŏwăʼ", "", "Parrot", "d. 1918", "",
     "For descendants, see above",
     "braced: the plate joins two names with a '{' for this one person -- "
     "'S˙ʼiʼrowaisiwa' over 'Kʼaiʼsh˙dŏwăʼ'. Second name carried in alt_name. "
     "BOTH re-read 2026-07-29 at x 2780 y 6070, and the first name is "
     "CORRECTED: the letter between the two apostrophes is a plain dotted i, "
     "not 'ĭ'. The two breves in the second name sit in the same crop and are "
     "unmistakable cups, which is what makes the plain i certain rather than "
     "merely likely. The breve over 'o' (U+014F) is confirmed with them. "
     "Drawn once; the repeat carries 'For descendants, see above'"),
    (15, 3, "M", "Dzăʼyu",           "",       "",   "Water",  "",   "", "", ""),
    (16, 3, "F", "Sho˙tyʼi",         "",       "",   "Turkey", "d.", "", "", ""),
    (17, 3, "M", "Tyi˙kʼamăi",       "",       "",   "Water",  "",   "", "", ""),
    (18, 3, "F", "Dziʼw˙ămaiʼ",      "",       "",   "Corn",   "d.", "", "", ""),
    (19, 3, "F", "Dzaiʼᶦtyʼi",       "",       "50", "Water",  "",   "", "",
     "name printed without a following period"),
    (20, 3, "M", "Kyʼĭauʼd˙yăĭăi",   "",       "",   "Sun",    "d.", "", "See Gen. I, 11",
     "medial vowels VERIFIED 2026-07-29 at a 640 px crop, x 2760 y 4700: the "
     "sequence after 'd˙y' is a-breve, i-breve, a-breve, i, exactly as read"),
    (21, 3, "M", "Dziwaikch˙ʼ",      "",       "35", "Water",  "",   "",  "",
     "trailing marks VERIFIED 2026-07-29 at x 2960 y 4805: a raised dot then "
     "an apostrophe, the same '˙ʼ' pair 22 carries mid-name -- compared "
     "side by side at that magnification, where a round dot and a raised "
     "comma are plainly different shapes. The period after them is "
     "punctuation, not orthography. An earlier note here "
     "called him '19's third husband'; the plate prints no such words, only a "
     "second '+' line under her (verified at x 2450, y 4620). He is recorded "
     "as her second drawn husband and nothing more"),
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
    (45, 4, "M", "Ka˙chănĭshʼ",      "",       "60", "Water",  "",   "", "",
     "trailing mark VERIFIED 2026-07-29 at x 3820 y 1795: an apostrophe, not "
     "a dot. The lower dot on that line is the sentence period"),
    (46, 4, "F", "Dzaaiʼy˙ăi",       "",       "",   "Bear",   "",   "", "", ""),
    (47, 4, "M", "Kaauʼs˙iyăiʼ",     "",       "",   "Water",  "d.", "", "", ""),
    (48, 4, "F", "Nati",             "",       "",   "Parrot", "",   "", "", ""),
    (49, 4, "M", "Gawaiʼᶦsᶦ",        "",       "",   "Turquoise", "", "", "",
     "two superscript i (U+1DA6), verified at native resolution; second husband of 48"),
    (50, 4, "M", "",                 "",       "",   "Water",  "d. in childhood.", "", "", "name printed as a dash"),
    (51, 4, "M", "Haiʼyuwăi˙siwăʼ",  "",       "",   "Water",  "",   "", "", ""),
    (52, 4, "F", "Gauʼs˙in˙ăiʼ",     "",       "",   "Lizard", "d.", "", "",
     "VERIFIED 2026-07-29 at x 3880 y 2690: there IS a raised dot between "
     "'n' and 'ă'. The earlier reading dropped it"),
    (53, 4, "F", "Kawiʼtsʼirăiʼ",    "",       "50", "Water",  "",   "", "", ""),
    (54, 4, "M", "Ma˙ʼrani",         "Ma˙ʼran˙i", "", "Sun",   "",   "", "",
     "DISCREPANCY, and now a VERIFIED one -- both occurrences were re-read at "
     "high magnification on 2026-07-29 and both are unambiguous. Upper block "
     "(x 3880, y 2910) reads 'Ma˙ʼrani'; lower block (x 3760, y 10780) reads "
     "'Ma˙ʼran˙i', with a raised dot before the final 'i'. So this is not a "
     "reading problem: the plate sets one man's name two ways. DECIDED "
     "2026-07-29 (user): carry BOTH, upper first, lower in alt_name -- see "
     "REPEAT_PERSON_NAMES. These two differ by a single raised dot, which is "
     "the narrowest of the three and the one where a reader most needs to be "
     "told the difference is the plate's and not a typo of ours"),
    (55, 4, "M", "Go˙tyʼiăiʼ",       "",       "65", "Corn",   "",   "", "", "second husband of 53"),
    (56, 4, "M", "Dzawi˙răi",        "",       "",   "Turkey", "",   "", "", ""),
    (57, 4, "F", "",                 "",       "",   "",       "",   "", "", "name printed as a dash; no clan printed"),
    (58, 4, "F", "Kʼoyo˙ʼs˙ăi",      "",       "45", "Turkey", "",   "", "", ""),
    (59, 4, "M", "Yăʼwĭĭʼyăiʼ",      "",       "",   "Turquoise", "", "",
     "Presumedly brother of Gen. IV, 64",
     "medial vowels VERIFIED 2026-07-29 at x 3920 y 3470: both medial i's "
     "carry breves, as read. The parenthetical is printed on its own line"),
    (60, 4, "M", "Shuwaiʼᶦri",       "",       "",   "Turkey", "",   "",
     "See Gen. I, 68",
     "cross-reference VERIFIED 2026-07-29 at x 3700 y 3350: the plate prints "
     "'See Gen. I, 68' on its own line under this name. It is not a doubtful "
     "reading -- it is the displacement CROSS_REF_OFFSET records, and it is "
     "the independent corroboration that Table 1's own '68' is Parsons's "
     "number. Recorded as printed"),
    (61, 4, "F", "Tsikʼaʼyăaitsʼa",  "",       "",   "Eagle",  "d.", "",
     "See Gen. I, 67",
     "cross-reference VERIFIED 2026-07-29 at x 3700 y 3350: printed as "
     "'See Gen. I, 67'. Same displacement as 60 above; recorded as printed"),
    (62, 4, "F", "Dziwiʼd˙yăi",      "",       "33", "Badger", "",   "", "See Gen. I, 77", "second wife of 60"),
    (63, 4, "M", "Dyaiʼtsʼdyĭwă",    "",       "",   "Turkey", "d.", "", "", ""),
    (64, 4, "M", "Kʼais˙ĭyăiʼ",      "",       "",   "Turkey", "",   "", "",
     "VERIFIED 2026-07-29 at x 3760 y 4480: a raised dot stands between 's' "
     "and 'ĭ'. The earlier reading dropped it"),
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
    (80, 4, "F", "Gauʼs˙ĭro",        "",       "",   "Bear",   "",   "", "",
     "VERIFIED 2026-07-29 at x 3950 y 5600: the letter after the raised dot "
     "is a dotless i under a breve, not a plain i. Compare 52, which has the "
     "same 'Gauʼs˙' opening and a plain 'i' after it"),
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
    (125, 5, "F", "Gowaʼk˙ʼd˙yăiʼ",  "Gowaʼkʼad˙zăiʼ", "18", "Water", "", "", "",
     "DISCREPANCY -- NOT A READING PROBLEM. Printed twice, and THE PLATE SETS "
     "THE TWO DIFFERENTLY: 'Gowaʼk˙ʼd˙yăiʼ' in the upper block (crop x 5080, "
     "y 3150) and 'Gowaʼkʼad˙zăiʼ' in the lower (crop x 4160, y 9555). Both "
     "were re-read at 380 px on 2026-07-29 and both are unambiguous at that "
     "size, so no tighter crop will settle it. Age 18 and clan Water agree in "
     "both. DECIDED 2026-07-29 (user): carry BOTH, upper first, lower in "
     "alt_name -- see REPEAT_PERSON_NAMES"),
    (126, 5, "M", "Yo˙ʼkwi",         "",       "23", "Chaparral Cock", "", "", "", ""),
    (127, 5, "F", "Howa˙kʼă",        "",       "",   "Water",  "d. 1919 at 13", "", "", ""),
    (128, 5, "F", "Mary Saiu",       "",       "",   "",       "",   "", "", "no clan printed"),
    (129, 5, "M", "",                "",       "",   "",       "",   "", "", "name and clan both printed as dashes"),
    (130, 5, "M", "Dzĭnătsʼĭd˙yiwă", "",       "",   "Turkey", "",   "", "", ""),
    (131, 5, "F", "Dziwaiʼy˙unăiʼ",  "",       "",   "Turkey", "",   "", "", ""),
    (132, 5, "M", "Djo˙s˙iyăi",      "",       "",   "Turkey", "",   "", "", ""),
    (133, 5, "M", "Yaʼod˙yidyăis˙iwăʼ", "",    "",   "Turkey", "",   "", "", ""),
    (134, 5, "F", "Juanina",         "",       "",   "Turkey", "",   "", "", ""),
    (135, 5, "F", "Säpʼ",            "",       "",   "Turkey", "",   "", "",
     "RE-READ 2026-07-29 at x 5050 y 3655, and the earlier reading was wrong "
     "twice over: the 'a' carries a DIAERESIS (U+00E4), not a breve -- two "
     "clear separate dots -- and there is a trailing apostrophe. So this is "
     "'Säpʼ', one superscript 'a' short of 180's 'Säpʼᵃ'. They remain "
     "different people: 135 is Turkey, 180 is Bear"),
    (136, 5, "F", "Dzid˙zaiʼd˙yuwi", "",       "",   "Turkey", "",   "", "", ""),
    # 137-143 each carry a "See Gen. I, n" that is one HIGHER than the
    # Genealogy I person whose name, sex and clan match. See CROSS_REF_OFFSET.
    (137, 5, "M", "Shauʼm˙ăiʼ",      "",       "",   "Eagle",  "",   "", "See Gen. I, 81", ""),
    (138, 5, "M", "",                "",       "",   "Eagle",  "",   "", "See Gen. I, 82", "name printed as a dash"),
    (139, 5, "M", "",                "",       "",   "Eagle",  "d.", "", "See Gen. I, 83", "name printed as a dash"),
    (140, 5, "F", "Heʼsa",           "Hazel",  "",   "Badger", "",   "", "See Gen. I, 91",
     "English name printed in parentheses on the plate"),
    (141, 5, "F", "Dzaĭyăiʼ",        "",       "",   "Badger", "",   "", "See Gen. I, 92", ""),
    (142, 5, "F", "Kăaiʼʼyunăiʼ",    "",       "",   "Badger", "",   "", "See Gen. I, 93",
     "VERIFIED 2026-07-29 at x 5090 y 4395: the two medial marks are TWO "
     "IDENTICAL APOSTROPHES, both slanting the same way with the bulb at the "
     "top. The earlier 'ˑ' (U+02D1) reading is withdrawn -- see 163, which "
     "was read the same wrong way and is a '˙ʼ' pair"),
    (143, 5, "M", "Dziw˙aiʼs˙iwă",   "",       "",   "Badger", "",   "", "See Gen. I, 94", ""),

    # ---- generation 6 ---------------------------------------------------
    (144, 6, "F", "Dzaaiʼd˙yid˙yuweʼ", "",     "6",  "Lizard", "",   "", "", ""),
    (145, 6, "F", "Kʼo˙ty˙imaiʼ",    "",       "4",  "Lizard", "",   "", "", ""),
    (146, 6, "M", "Aiʼs˙iyĕʼᵉ",      "",       "9 mos.", "Lizard", "", "", "",
     "VERIFIED 2026-07-29 at x 6360 y 2755: TWO marks follow the 'ĕ' -- an "
     "apostrophe, then a superscript e (U+1D49). Same 'ʼ + superscript "
     "vowel' pattern as 84's 'Ha˙tsʼᵉ' and 180's 'Säpʼᵃ'"),
    (147, 6, "M", "Mid˙yăiʼsĭw˙ă",   "",       "10", "Water",  "",   "", "", ""),
    (148, 6, "F", "Kwid˙yaid˙yui",   "",       "7",  "Water",  "",   "", "", ""),
    (149, 6, "M", "Shaatse",         "",       "",   "Water",  "d. 1913, at 3 days", "", "", ""),
    (150, 6, "M", "Koʼya˙ʼshdyiĕ",   "",       "",   "Water",  "d. 1917, at 2", "", "", ""),
    (151, 6, "M", "Yaiʼyaăi",        "",       "2",  "Water",  "",   "", "", ""),
    (152, 6, "M", "Tsiᶦshdyĭʼwă",    "",       "3",  "Water",  "",   "", "", ""),
    (153, 6, "F", "Gaiʼtsdyui",      "",       "5 mos.", "Water", "", "", "", ""),

    # =====================================================================
    # LOWER BLOCK -- founding couple 154+155
    # Generations here are in the SAME frame as the upper block's, derived
    # from the traced tree at Gate 2 (see the generation-frame note below).
    # 154+155 are generation 2, not 1: their children 13 and 14 are drawn in
    # the upper block at generation 3. "Founding couple" means the plate
    # draws no parents for them, not that they sit in the first column.
    # =====================================================================
    (154, 2, "F", "",                "",       "",   "Parrot", "",   "", "", "name printed as a dash"),
    (155, 2, "M", "",                "",       "",   "Turkey", "",   "", "", "name printed as a dash"),

    (156, 3, "M", "Shʼauʼs˙imăiʼ",   "",       "",   "Parrot", "d.", "", "See Gen. I, 10", ""),
    (157, 3, "F", "Dyaiʼᶦs˙itsʼă",   "",       "",   "Sun",    "d. 1918, at 60", "", "See Gen. I, 9", ""),
    (158, 3, "M", "Niʼʼy˙ŭyăiʼ",     "",       "",   "Parrot", "",   "", "", ""),
    (159, 3, "F", "",                "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (160, 3, "F", "Yo˙ʼs˙iro",       "",       "",   "Chaparral Cock", "d. 1914", "",
     "For second husband and descendant, see Gen. III, 154, 220 | "
     "For third husband and descendant, see Gen. I, 8, 90",
     "second wife of 158; the year 1914 is set in bold on the plate. This is "
     "Genealogy I's person 73 -- name, clan and death year all agree. The two "
     "statements are separated by '|', the renderer's row separator, NOT by "
     "'/': a slash would be printed on the page, and the plate prints no "
     "slash -- it sets the two on separate lines. Same correction at 169; "
     "Genealogy I's own person 73 had it right"),
    (161, 3, "",  "Gawai˙d˙yirăiʼ",  "",       "",   "Parrot", "d.", "", "",
     "sex printed as 'M.-F.' -- a marking used nowhere else on this plate. "
     "Stored empty rather than guessed; recorded here as printed"),
    (162, 3, "M", "Da˙ʼyuʼ",         "",       "",   "Parrot", "d.", "", "",
     "trailing mark VERIFIED 2026-07-29 at x 2860 y 9810: an apostrophe"),
    (163, 3, "F", "Ĭya˙ʼsi",         "",       "",   "Bear",   "",   "",
     "For second husband and descendants, see Gen. III, 14, 49-55, 135-141",
     "RE-READ 2026-07-29 at x 2860 y 9865: the pair after 'Ĭya' is a raised "
     "dot then an apostrophe, '˙ʼ'. The earlier 'ˑ' (U+02D1) reading is "
     "withdrawn here as at 142, and with both gone U+02D1 is no longer used "
     "anywhere on this plate"),
    (164, 3, "F", "Heaʼʼs˙i",        "",       "",   "Parrot", "d.", "", "", ""),
    (165, 3, "M", "Ha˙ʼpai",         "",       "",   "Oak",    "d.", "", "", ""),

    # =====================================================================
    # THIRD FOUNDING COUPLE -- 232+233
    # No leader rule enters 232 from the left, where 158 and 164 both have
    # one. Verified at native resolution.
    # Gate 2 found they have SIX children, not the one the first pass saw:
    # 54, 235, 237, 238, 240 and 242, on a single bracket running the height
    # of column C (x 3620, y 10440 and 11890). Every one is Sun, which is
    # 232's clan and not 233's Turkey.
    # 54 also appears in the upper block as 53's husband.
    # =====================================================================
    (232, 3, "F", "Yuwaiʼd˙yaitsʼă", "",       "",   "Sun",    "",   "", "", ""),
    (233, 3, "M", "Gaʼʼaiʼ",         "",       "",   "Turkey", "",   "", "", ""),

    # ---- lower block, generation 3 --------------------------------------
    (166, 4, "M", "G˙yiʼmi",         "",       "45", "Sun",    "",   "", "See Gen. I, 16", ""),
    (167, 4, "F", "Nămăiʼ",          "",       "40", "Oak",    "",   "", "See Gen. I, 17", ""),
    (168, 4, "M", "Kowăuʼsh˙dyiwă",  "",       "42", "Sun",    "",   "", "See Gen. I, 18", ""),
    (169, 4, "F", "Haiʼtyʼʼimăiʼ",   "",       "43", "Parrot", "",   "",
     "See Gen. I, 19 | For first husband and descendants, see below",
     "appears twice within the lower block, and the plate gives each occurrence "
     "exactly ONE marriage and one bracket -- under 156+157 as 168's wife, "
     "bracketing 196-200, with 'For first husband and descendants, see below'; "
     "and under 164+165 as their daughter, bracketing 225, 226, with 'For "
     "second husband and descendants, see above'. The second occurrence prints "
     "no '+ 168' line at all. Read 2026-07-30 at x 3650 y 7500 and x 3650 "
     "y 9700, 1500 px wide. This is why she needs make_chart.py's "
     "SECOND_VISIT_OMITTED: she is the mother of both groups, so the renderer "
     "gave both mother_row = 0 and could not put two brackets on one line. "
     "A heavy ink stroke runs "
     "from this line's clan to its sibling bracket on the scanned copy -- it is "
     "not type, and is recorded as an observation of this copy, not as data"),
    (170, 4, "M", "Kʼuʼn˙ash˘",      "",       "",   "Sun",    "",   "", "See Gen. I, 20",
     "trailing mark VERIFIED 2026-07-29 at x 4150 y 7995, and it is a "
     "SPACING BREVE (U+02D8) -- a cup opening upward with thickened "
     "terminals, standing after 'sh' and over no letter. This is the only "
     "spacing breve on the plate and the only place the codepoint is needed. "
     "Recorded where the plate sets it; whether the compositor meant it over "
     "the 'a' is an interpretation this edition does not make"),
    (171, 4, "F", "Shayaʼai",        "",       "",   "Sun",    "",   "", "See Gen. I, 21",
     "number printed without a following period"),
    (172, 4, "M", "Dziraiʼᶦtyʼi",     "",       "",   "Sun",    "",   "", "See Gen. I, 22", ""),
    (173, 4, "F", "Dziʼs˙dyuwi",      "",       "",   "Bear",   "d.", "", "See Gen. I, 23", ""),
    (174, 4, "M", "Shta˙ʼyăi",        "",       "",   "",       "",   "", "",
     "no clan printed; name printed without a following period"),
    (175, 4, "F", "Kio˙ʼd˙yiăi",      "",       "",   "Bear",   "",   "", "", ""),
    (176, 4, "F", "Dzaʼwaiʼᶦy˙unăiʼ", "",       "",   "Sun",    "",   "", "", ""),
    (177, 4, "M", "Maiʼs˙iwă",        "",       "",   "Turkey", "",   "", "",
     "set in noticeably larger type than the lines around it -- an observation "
     "of this copy's setting, not data"),
    (178, 4, "F", "Shuwăiʼ",          "",       "",   "Chaparral Cock", "", "", "", ""),
    (179, 4, "M", "",                 "",       "",   "White",  "",   "", "",
     "name printed as a dash. 'White' stands where every other line prints a "
     "clan. Recorded as printed, not interpreted"),
    (180, 4, "F", "Säpʼᵃ",            "",       "",   "Bear",   "d.", "", "",
     "diaeresis on 'a' (U+00E4) -- a codepoint neither Table 1 nor Table 4 "
     "uses. Confirmed at a 330 px crop"),
    (181, 4, "M", "Ma˙tsʼăĭ yăiʼ",    "",       "",   "Bear",   "",   "", "",
     "the plate sets this name as two words, with a space; confirmed at a "
     "460 px crop"),
    (182, 4, "F", "Gwiʼtyʼi",         "",       "",   "Sun",    "",   "", "", ""),
    (183, 4, "M", "",                 "",       "",   "Mexican", "",  "", "",
     "name printed as a dash. 'Mexican' stands where every other line prints a "
     "clan, as 'White' does at 179. Recorded as printed, not interpreted. "
     "This is the first husband of 169, whose line here carries 'For second "
     "husband and descendants, see above'"),
    (184, 4, "M", "Djaiʼd˙ziĕ",       "",       "30", "Parrot", "",   "", "", ""),
    (185, 4, "F", "Kăauʼd˙yuwi",      "",       "35", "Corn",   "",   "", "", ""),
    (234, 4, "F", "Go˙ʼyăiʼ",         "",       "",   "Eagle",  "",   "", "",
     "second wife of 54, printed as a second '+' line under him below 53"),
    (235, 4, "M", "Charley Kai",      "",       "",   "Sun",    "",   "", "",
     "English name printed as the name itself, as at 116-118, 128 and 134"),
    (236, 4, "F", "Kaweishdyiŭr",     "",       "",   "Water",  "",   "", "", ""),
    (237, 4, "F", "Tsʼid˙yuwiʼ",      "",       "",   "Sun",    "d.", "", "", ""),
    (238, 4, "M", "Yo˙rimăiʼ",        "Fred Kai", "", "Sun",    "",   "", "",
     "English name printed in parentheses on the plate"),
    (239, 4, "F", "Dziwiʼs˙dy˙uwi",   "",       "",   "Chaparral Cock", "", "", "", ""),
    (240, 4, "F", "Dzi˙d˙jaʼai",      "",       "",   "Sun",    "d.", "", "", ""),
    (241, 4, "M", "Tsiyusiĕ",         "",       "",   "Parrot", "",   "", "", ""),
    (242, 4, "M", "Shaaiʼshdyiăi",    "",       "",   "Sun",    "",   "", "", ""),
    (243, 4, "F", "",                 "",       "",   "Mohave", "",   "", "",
     "name printed as a dash. 'Mohave' stands where every other line prints a "
     "clan, as 'White' does at 179 and 'Mexican' at 183. Recorded as printed, "
     "not interpreted"),
    # Column C of the lower block ends here, at 243.

    # ---- lower block, generation 4 (column D) ---------------------------
    # 186 and 188-195 sit at one indent: they are siblings, not mother and
    # children -- 186 is 23 and 188 is 22. Their Oak clan and their "See Gen.
    # I" numbers both point at 167 (Nămăiʼ, Oak, 40) as the mother.
    (186, 5, "F", "Shăaityʼid˙yuweʼ", "",       "23", "Oak",    "",   "", "", ""),
    (187, 5, "M", "Ramona of Sant Ana", "",     "50", "Turkey", "",   "", "",
     "the plate prints the name with a place, spelled 'Sant Ana'. Recorded as "
     "printed, not normalised"),
    (188, 5, "F", "Kiwaʼd˙yuwi",      "",       "22", "Oak",    "",   "", "See Gen. I, 33",
     "Gen. I 33 is this same woman by name and clan but prints her age as 18. "
     "Both are recorded as each plate prints them"),
    (189, 5, "F", "Ko˙ri",            "",       "21", "Oak",    "",   "", "See Gen. I, 31", ""),
    (190, 5, "M", "Tsᶦgaiʼs˙iwăʼ",    "",       "20", "Oak",    "",   "", "See Gen. I, 32",
     "this line crosses a fold crease and the medial 's˙i' reads ambiguously "
     "as 's˙i' or 'sʼï' at any crop. Gen. I 32 is the same man and prints "
     "'Tsᶦgaiʼs˙iwăʼ' on a far better-resolved plate; that settles it"),
    (191, 5, "M", "Tsiʼd˙yimĕ",       "",       "17", "Oak",    "",   "", "See Gen. I, 34",
     "no trailing apostrophe here, where Gen. I 34 prints 'Tsiʼd˙yimĕʼ'. "
     "Confirmed at a 620 px crop; each plate is recorded as it prints"),
    (192, 5, "F", "Sha˙tyʼi",         "",       "14", "Oak",    "",   "", "See Gen. I, 35", ""),
    (193, 5, "M", "Aiʼwanăi",         "",       "8",  "Oak",    "",   "", "See Gen. I, 36", ""),
    (194, 5, "M", "Dyăiʼtsdyămŭr",    "",       "6",  "Oak",    "",   "", "See Gen. I, 37", ""),
    (195, 5, "M", "Iyăiʼs˙dyiwă",     "",       "5",  "Oak",    "",   "", "See Gen. I, 38", ""),
    (196, 5, "F", "Kăauʼshurtsʼa",    "",       "9",  "Parrot", "",   "", "See Gen. I, 40", ""),
    (197, 5, "M", "Onăiʼ",            "",       "8",  "Parrot", "",   "", "See Gen. I, 41", ""),
    (198, 5, "F", "Wamais",           "",       "7",  "Parrot", "",   "", "See Gen. I, 42",
     "no trailing marks here, where Gen. I 42 prints 'Wamais˙ʼ'"),
    (199, 5, "M", "Gaishpidjaʼtyᵃ˙",  "",       "6",  "Parrot", "",   "", "See Gen. I, 43 (?)",
     "THE QUESTION MARK IS PARSONS'S OWN, printed on the plate after the "
     "reference. It is the only cross-reference on this plate that carries one, "
     "and it is warranted: Gen. I 43 is 'Yoʼd˙yidyăiʼ', a different name. Copy "
     "the '(?)' through to the page -- it is her doubt, not ours. Trailing "
     "superscript a then raised dot, confirmed at a 260 px crop"),
    (200, 5, "M", "Hea˙ʼshdyĭwă",     "",       "",   "Parrot", "d. 1917, at 2", "", "See Gen. I, 44",
     "Gen. I 44 prints 'Hea˙ʼsh˙dyĭwă' and 'd. 1917, aged 2'. Each plate is "
     "recorded as it prints"),
    (201, 5, "M", "Dziwaiʼi˙siro",    "",       "",   "Sun",    "",   "", "See Gen. I, 45",
     "raised dot after the medial 'i', which Gen. I 45 does not print"),
    (202, 5, "F", "Kuyăiʼd˙yid˙uweʼ", "",       "",   "Sun",    "",   "", "See Gen. I, 48",
     "no 'y' before 'uweʼ', where Gen. I 48 prints 'Kuyăiʼd˙yid˙yuweʼ'. "
     "Confirmed at a 480 px crop"),
    (203, 5, "F", "Edna",             "",       "",   "Sun",    "",   "", "",
     "English name printed as the name itself; no cross-reference on this line"),
    (204, 5, "F", "Yăaiʼdyid˙yuwi",   "",       "",   "Sun",    "",   "", "See Gen. I, 49", ""),
    (205, 5, "M", "Owi˙ʼd˙zĭraiʼ",    "",       "",   "Sun",    "",   "", "See Gen. I, 47", ""),
    (206, 5, "F", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (207, 5, "M", "",                 "",       "",   "Bear",   "",   "", "", "name printed as a dash"),
    (208, 5, "F", "Gaaish",           "",       "",   "Bear",   "",   "", "See Gen. I, 53",
     "Gen. I 53 is 'Gaaiʼd˙yuitsʼa', F, Bear, aged 3 -- the same girl under a "
     "shorter form of the name. Each plate is recorded as it prints"),
    (209, 5, "F", "Onăiʼ",            "",       "10", "Bear",   "",   "", "", ""),
    (210, 5, "M", "Niăiʼ",            "",       "4",  "Bear",   "",   "", "", ""),
    (211, 5, "M", "Shʼauwiăiʼ",       "",       "3",  "Bear",   "",   "", "", ""),
    # 212-219 print no sex letter: number, dash, clan only -- the same setting
    # as 85-100 and 106-115 in the upper block. Stored empty, not guessed.
    (212, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (213, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (214, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (215, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (216, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (217, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (218, 5, "",  "",                 "",       "",   "Chaparral Cock", "", "", "", "no sex printed; name printed as a dash"),
    (219, 5, "",  "",                 "",       "",   "Chaparral Cock", "", "", "", "no sex printed; name printed as a dash"),
    (220, 5, "F", "Shauʼkʼămă",       "",       "15", "Sun",    "",   "", "", ""),
    (221, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (222, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (223, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (224, 5, "",  "",                 "",       "",   "Sun",    "",   "", "", "no sex printed; name printed as a dash"),
    (225, 5, "",  "Shauʼd˙yidĕ",      "",       "15", "Parrot", "",   "", "",
     "no sex printed, although this line does carry a name and an age. Every "
     "other sexless line on the plate prints a dash for the name as well; this "
     "is the only one that does not. Confirmed at an 800 px crop"),
    (226, 5, "",  "",                 "",       "",   "Parrot", "d.", "", "", "no sex printed; name printed as a dash"),
    (227, 5, "M", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),
    (228, 5, "F", "",                 "",       "",   "Corn",   "d.", "", "", "name printed as a dash"),

    # ---- lower block, generation 5 (column E) ---------------------------
    # 229-231 are the children of 186+187. All Oak, as 186 is.
    (229, 6, "F", "Shawityi",         "",       "6",  "Oak",    "",   "", "", ""),
    (230, 6, "M", "Awie˙",            "",       "4",  "Oak",    "",   "", "", ""),
    (231, 6, "M", "Yoreni",           "",       "1",  "Oak",    "",   "", "", ""),

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
    (254, 5, "F", "Lina",             "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself. HER DESCENT FROM 235+236 WAS "
     "RE-VERIFIED 2026-07-30 at the user's request, on the bracket-column strip "
     "x 4720, y 11400, 300 x 900: 236's leader rule meets the vertical at the "
     "TOP corner, which is 254's own row, and a stub enters 254 there. The "
     "vertical then runs to 260 and terminates. Stubs enter 254, 255, 256, 258, "
     "259 and 260; 257 takes none. Her Water clan is 236's, which agrees"),
    (255, 5, "M", "Kaauʼstyiăiʼ",     "",       "",   "Eagle",  "",   "", "",
     "this '+' line also carries a leader rule entering from the left, which "
     "no other '+' line on the plate does -- 257, the other '+' line in the "
     "same group, takes no stub. Confirmed on the strip above. It is NOT "
     "descent: 255 is Eagle and every child of this bracket is Water. See "
     "U60 in UNIONS, which is where the reading is stated"),
    (256, 5, "F", "Gʼawaidyuwi",      "",       "",   "Water",  "",   "", "", ""),
    (257, 5, "M", "John Perry",       "",       "",   "Eagle",  "",   "", "",
     "English name printed as the name itself"),
    (258, 5, "M", "Oʼkʼaiyă",         "",       "",   "Water",  "",   "", "", ""),
    (259, 5, "F", "Kʼataiʼd˙yuwĕʼ",   "",       "",   "Water",  "",   "", "",
     "number printed without a following period, as at 19 and 171"),
    (260, 5, "M", "Willi",            "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself"),
    # 261-264 are Chaparral Cock, which is 239's clan, so they hang off
    # 238+239. 265-269 are Sun, and 268-269 print no clan at all.
    (261, 5, "F", "",                 "",       "",   "Chaparral Cock", "", "", "", "name printed as a dash"),
    (262, 5, "M", "John",             "",       "",   "Chaparral Cock", "", "", "",
     "English name printed as the name itself"),
    (263, 5, "M", "Dyumaiʼ",          "",       "",   "Chaparral Cock", "", "", "", ""),
    (264, 5, "F", "",                 "",       "",   "Chaparral Cock", "", "", "",
     "name printed as a dash, followed by a period -- the only dashed name on "
     "the plate that carries one"),
    (265, 5, "M", "Naisiyĕ",          "",       "",   "Sun",    "",   "", "", ""),
    (266, 5, "M", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (267, 5, "F", "",                 "",       "",   "Sun",    "",   "", "", "name printed as a dash"),
    (268, 5, "",  "",                 "",       "",   "",       "",   "", "",
     "no sex printed; name and clan both printed as dashes"),
    (269, 5, "",  "",                 "",       "",   "",       "",   "", "",
     "no sex printed; name and clan both printed as dashes"),
    # Column D of the lower block ends here, at 269.

    # ---- lower block, generation 5 (column E) ---------------------------
    # 270-274 are all Water. 254's rule carries 270-272 and 256's carries
    # 273-274; both women are Water.
    (270, 6, "M", "Kʼauʼwină",        "",       "",   "Water",  "",   "", "", ""),
    (271, 6, "F", "Dziaid˙yuwe",      "",       "",   "Water",  "",   "", "", ""),
    (272, 6, "F", "Josephine",        "",       "",   "Water",  "",   "", "",
     "English name printed as the name itself"),
    (273, 6, "F", "Dziᶦʼyăiʼ",        "",       "",   "Water",  "",   "", "", ""),
    (274, 6, "F", "Naiyaisiroʼ",      "",       "",   "Water",  "",   "", "", ""),
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
#     through person 53 and one high from person 66 onward, with the matched
#     names as the evidence. (This line said 27 until 2026-07-29, contradicting
#     the evidence listed above it in this same block -- the exact range was
#     extended to 53 by the lower block's column D and the summary was not
#     updated with it. Both footnotes are written and both say 53.)
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
# REPEAT_PERSON_NAMES
#
# Three people are drawn twice on this plate and THE PLATE SETS THE NAME
# DIFFERENTLY IN THE TWO PLACES. All six settings were re-read at high
# magnification (13 and 54 on 2026-07-29, 125 on the same day at 380 px) and
# every one is unambiguous, so this is not a reading problem to be cropped
# away: the plate genuinely prints one person's name two ways.
#
# DECIDED 2026-07-29 (user): CARRY BOTH. The first occurrence in reading
# order -- the upper block, in all three cases -- goes in name_as_printed;
# the second goes in alt_name, which the renderer prints as " (second)".
# Suppressing either would hide something the plate says.
#
# Read as: {id: (as printed at the first occurrence, at the second)}
REPEAT_PERSON_NAMES = {
    13:  ("Dzia˙ʼyotsʼa",   "Tsiaiutsa"),       # a different name, not a variant
    54:  ("Ma˙ʼrani",       "Ma˙ʼran˙i"),       # one raised dot apart
    125: ("Gowaʼk˙ʼd˙yăiʼ", "Gowaʼkʼad˙zăiʼ"),  # age 18 and Water in both
}

# ONE THING THIS DECISION OWES GATE 4, and it is not optional. alt_name now
# carries THREE different meanings on this plate, and the renderer cannot
# tell them apart -- it prints " (alt)" for all of them:
#
#   1. an ENGLISH NAME the plate itself prints in parentheses (27, 42, 43,
#      140). Genuinely parenthetical on the page.
#   2. the second half of a BRACED PAIR, where the plate joins two names with
#      a '{' for one person (14). Not parenthetical on the page.
#   3. the second SETTING of a repeat person's name (13, 54, 125, here).
#      Not parenthetical on the page either.
#
# Only the first is what the plate looks like. So the three at (3) will
# render in a form the plate never sets, exactly as (2) already does -- the
# cost the user accepted in choosing to carry both. What must NOT happen is
# a reader taking "Ma˙ʼrani (Ma˙ʼran˙i)" for an English name or an editorial
# gloss. The apparatus therefore has to say, once, that a parenthesis after
# a name on THIS table means one of those three things, and name which
# people are which. Route every person reference through _p().
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# STATE -- read and encoded; self_check() passes; NOT yet registered
#
# DONE:  Gate 1, plate numbers 1-274 plus the second 101 -- 275 records, no
#        gaps, no id collisions, and the numbering verified to end at 274 by
#        sweeping the plate's right margin.
#        Gate 2, 61 unions and 214 child links, every bracket traced from the
#        rules. self_check() passes: 0 clan mismatches on 214 links, nobody a
#        child twice, nobody neither child nor spouse, and the arithmetic
#        closes at 214 children + 61 spouse-only = 275.
#        Gate 1b, every unverified glyph reading re-read at high
#        magnification on 2026-07-29. Nothing is marked SEE TODO any more.
#        The three repeat-person name choices, decided by the user the same
#        day: carry both settings. See REPEAT_PERSON_NAMES, which self_check()
#        now holds against the records.
#        Gate 4 DONE and MEASURED at 1280x900 on 2026-07-29. Registered in
#        TABLES as "ii"; font subset re-run; apparatus written. Measured:
#          - column drift 0 px at ALL SIX generations, step 425.6 px each
#            (= --col + --stub), which nothing in this layout had been tested
#            at before this plate
#          - all 55 sibling brackets on their mother's line, max 0.016 px
#          - 0 in-block rows off the --lh grid
#          - 0 px body sideways scroll; the plate pans inside .scroll
#          - Table 1 (5 gens, 24 brackets) and Table 4 (4 gens, 14) re-measured
#            as controls: 0 px drift, 0 px bracket offset
#        FIVE DEFECTS SURFACED IN THE PROCESS, all fixed -- see CHANGELOG. Four
#        were in shared code that the two published plates never exercised:
#          - 7 people undrawn: a fatherless sibling group whose mother is only
#            a '+' line was never looked up (116-118 under 48); 49 needed
#            drawn_under; 31+32+97 were reachable from nothing and were rooted,
#            which drew them but at generation 1 -- see UNATTACHED_BLOCKS, which
#            replaced that on 2026-07-30 and puts them where the plate does
#          - .xref rendered 21.09 px against a 24.8 px budget, putting 7
#            brackets 3.7 px off their mother's line
#          - DUPLICATE_PLATE_NUMBERS was declared here but never READ by the
#            renderer, so the synthetic id 1010 printed on the page in four
#            places instead of the plate's 101
#          - two cross-references used '/' where the renderer's row separator
#            is '|', printing a slash the plate does not set
#          - the font subset was driven partly by plate_note prose, and was
#            missing two glyphs the published pages have always used
# TO DO: the sentence Table 2's cross-reference finding adds to TABLE 1's
#        #note-misprint. Table 1 is published and cited, so re-verify that page
#        after building. Table 2's own side of it is written (#note-crossref).
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
# GLYPH READINGS: ALL VERIFIED 2026-07-29. There is no "SEE TODO" left in
# this file. Twelve marks were re-read at 6-25x native magnification; each
# record carries the pixel coordinates it was verified at, so any of these is
# one command to re-check. TWO CONFIRMED the earlier reading (20, 59) and TEN
# CORRECTED IT:
#   21   Dziwaikch      -> Dziwaikch˙ʼ     trailing '˙ʼ' pair was dropped
#   45   Ka˙chănĭsh     -> Ka˙chănĭshʼ     trailing ʼ was dropped
#   52   Gauʼs˙inăiʼ    -> Gauʼs˙in˙ăiʼ    medial ˙ was dropped
#   64   Kʼaisĭyăiʼ     -> Kʼais˙ĭyăiʼ     medial ˙ was dropped
#   80   Gauʼs˙iro      -> Gauʼs˙ĭro       plain i was really ĭ
#   135  Săp            -> Säpʼ            breve was really a DIAERESIS, and
#                                          a trailing ʼ was dropped
#   142  Kăaiˑʼyunăiʼ   -> Kăaiʼʼyunăiʼ    'ˑ' was really a second ʼ
#   146  Aiʼs˙iyĕ       -> Aiʼs˙iyĕʼᵉ      two trailing marks were dropped
#   162  Da˙ʼyu         -> Da˙ʼyuʼ         trailing ʼ was dropped
#   170  Kʼuʼn˙ash      -> Kʼuʼn˙ash˘      trailing SPACING BREVE was dropped
# And one that carried no TODO at all, found because 142 was wrong the same
# way:
#   163  Ĭyaˑʼsi        -> Ĭya˙ʼsi         'ˑ' was really a '˙ʼ' pair
#   14   S˙ʼĭʼrowaisiwa -> S˙ʼiʼrowaisiwa  'ĭ' was really a plain dotted i
#
# THE PATTERN IN THOSE TEN IS WORTH KEEPING. Nine of the ten dropped a mark
# rather than misidentifying one, and every one of them sits at the END of a
# name, where a 1450 px column tile renders the mark 4-6 px wide and the
# sentence period sits right beside it. A column tile is enough to read a
# NAME and never enough to read its final mark. Two shape confusions are the
# ones to watch for, and both need a same-magnification comparison rather
# than a judgement in isolation:
#   - '˙' (round, no tail) vs 'ʼ' (bulb at top, tail down-left). Person 22's
#     'Shaiyo˙ʼsi˙ĕ' prints the pair adjacent and is the reference specimen.
#   - a raised mark vs the same mark repeated. 142 and 163 both read as the
#     exotic 'ˑ' when they were an ordinary pair.
#
# CODEPOINT CONSEQUENCES, both checked against the cmap of BOTH master faces:
#   - U+02D1 'ˑ' IS NO LONGER USED. Its only two sites were 142 and 163.
#   - U+02D8 '˘' IS NEW, at 170 only, and is present in both faces.
#   - 14's 'ŏ' (U+014F) and 84's 'ᵉ' (U+1D49) were already confirmed.
#
# AND THREE PEOPLE DRAWN TWICE WHOSE TWO OCCURRENCES DISAGREE -- SETTLED
# 2026-07-29, and no longer an open item. The point about them was that THEY
# ARE NOT READING PROBLEMS: all six settings were re-read at high
# magnification and every one is unambiguous, so the plate genuinely prints
# one person's name two ways. The user's decision is to CARRY BOTH, first
# occurrence in name_as_printed and second in alt_name; the pairs are
# declared in REPEAT_PERSON_NAMES and held against the records by
# self_check(). Listed here for the reader who arrives at one of them:
#   - 13   Dzia˙ʼyotsʼa / Tsiaiutsa          (BOTH re-read 2026-07-29 and both
#          unambiguous; the lower carries no diacritics at all. The earlier
#          "upper reading is the less certain" is withdrawn)
#   - 54   Ma˙ʼrani / Ma˙ʼran˙i              (one raised dot apart; BOTH
#          occurrences re-read at high magnification on 2026-07-29 and both
#          are unambiguous, so the difference is the plate's, not ours)
#   - 125  Gowaʼk˙ʼd˙yăiʼ / Gowaʼkʼad˙zăiʼ   (both crops verified legible)
# Each record carries the coordinates of both occurrences. 169's two
# occurrences agree; it is named here only so nobody hunts for a fourth.
#
# Note this is the same phenomenon that shows up BETWEEN plates, where it is
# not a problem at all: 191 vs Gen. I 34, 198 vs Gen. I 42, 200 vs Gen. I 44,
# 202 vs Gen. I 48 all differ in a mark, and there each plate is simply
# recorded as it prints. Only the within-plate repeats force a choice.
#
# SETTLED 2026-07-29: 135 was read as "Săp" with a breve and 180 as "Säpʼᵃ"
# with a diaeresis, and the suspicion was that 135 had been misread against
# 180's better crop. It had. 135 is "Säpʼ" -- same diaeresis, same trailing
# apostrophe, no superscript a. They are still different people (135 Turkey,
# 180 Bear), so nothing about the structure changes; what changes is that the
# two names now differ by exactly the one glyph the plate actually prints
# differently, instead of by three.
#
# FONT COVERAGE IS NOT A PROBLEM. The cmap of both master faces
# (vendor/gentium/Gentium-{Regular,Italic}.ttf) was checked directly and
# carries U+014F, U+1D49 and -- checked 2026-07-29 for the codepoints the
# lower block and the Gate 1b re-read added -- U+00E4, U+02DA and U+02D8, as
# well as the marks already in use. THE READINGS ARE NOW FINAL, so Gate 4's
# font step is exactly one command: re-run scripts/subset_font.py. There is
# nothing to source. Do not judge this by looking at rendered text: macOS
# substitutes silently for any missing face.
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
# THE CHART NOW DRAWS THEM THERE TOO (2026-07-30). Until then all three roots
# rendered at generation 1, so 154+155 sat one column left of where the plate
# sets them and 232+233 two columns left -- the same "the block is right and its
# position is not" defect that 31 had, and the reason the user flagged 232+233.
# make_chart.py's TABLES entry now carries root_columns {154: 2, 232: 3}, which
# indents the .tree in the grid's own tokens. Note this field is STILL not a
# layout input: root_columns was set from the plate's measured indents (person 1
# at x 225, person 3 at x 1425, 154 at x 1340, 232 at x 2690) and the agreement
# with the generations derived here is a check, not a dependency.
#
# APPLIED 2026-07-29, once the brackets were encoded. The field was NOT
# hand-renumbered off column positions; it was DERIVED from the traced tree
# and then written back. The rule set is three lines:
#     generation(child)  = generation(mother) + 1
#     generation(mother) = generation(child)  - 1
#     generation(spouse) = generation(partner)
# seeded with person 1 = 1 and run to a fixed point over UNIONS and CHILDREN.
#
# That determines 272 of the 275 records and CONTRADICTS NONE of the upper
# block's 165 -- every upper value the tree derives is the value already
# stored, which is a real check on both the tracing and the earlier reading.
# The 110 it changes are all in the lower block and all by exactly +1, which
# is the conversion above falling out of the data rather than being asserted:
# 154+155 land at 2 and 232+233 at 3, the column each is printed in.
#
# THE THREE IT CANNOT REACH are 31, 32 and 97. 31 and 32 are the married-in
# couple whose parents the plate does not draw, so no path connects them to
# person 1, and their child 97 hangs off them. Their generation is the one
# thing here that IS read off the plate's column -- upper 4 and 4, and 5 for
# 97, exactly as the first reading recorded them. Left as they were.
#
# The maximum is 6, so the "six generations" in the page copy is correct.
# Note this field is not a layout input either way: make_chart.py reads it
# only for `n_gens = max(...)`, and the chart's columns come from walking
# UNIONS and CHILDREN.
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

# ---------------------------------------------------------------------------
# UNIONS  (each '+' line on the plate is a marriage)
# union_id, wife_id, husband_id, wife_marriage_order, husband_marriage_order, note
#   order = 1 unless the plate draws that person with more than one spouse
#   0 in an id field = spouse not shown on the plate
#
# HOW THESE WERE TRACED (2026-07-29). Not from the text and not from the clan:
# from the RULES. For each generation boundary a narrow strip of the bracket
# column was cut at native resolution -- about 260 px wide, so the vertical
# rule and every leader rule entering it are the only things in the frame --
# and then a 1550 px strip spanning both columns, which shows each mother's
# horizontal rule running from her line to her children's bracket. The clan
# was used afterwards, as the independent check the method intends, never as
# the evidence.
#
# That method caught one thing reading by row alignment would have got wrong:
# 31 sits INSIDE the vertical extent of 9+10's bracket, at the children's
# indent, between 29 and 33 -- and has no leader rule. The rule passes his row
# with nothing attached (verified at x 3580, y 120, 260 x 1500). He is not
# 9+10's son; he is a husband whose own parents the plate does not draw, the
# same pattern as 232+233 in the lower block. His clan is Water like theirs,
# so the clan check could not have found this.
#
# Re-verified 2026-07-30 on the bracket-column strip x 3320, y 500, 480 x 1100,
# which also corrected a detail this file had wrong: the stubs into 33 and into
# 35, 36, 38, 40 are on TWO DIFFERENT verticals, not one. 9+10's vertical takes
# 26, 29 and 33 and ends at 33; 11+12's begins at 35. 31's row lies between the
# stubs to 29 and 33 and takes neither.
#
# Where he is DRAWN is a separate question from whose son he is, and the two
# were conflated until 2026-07-30: he was made a root, which is the only way an
# unreachable person gets drawn at all, and a root is drawn at generation 1 --
# four columns left of where the plate sets him. UNATTACHED_BLOCKS above is
# what fixed that.
# ---------------------------------------------------------------------------
UNIONS = [
    # ---- upper block ----------------------------------------------------
    ("U01",   1,   2, 1, 1, ""),
    ("U02",   3,   4, 1, 1, ""),
    ("U03",   5,   6, 1, 1, ""),
    ("U04",   7,   8, 1, 1, ""),
    ("U05",   9,  10, 1, 1, ""),
    ("U06",  11,  12, 1, 1, ""),
    ("U07",  13,  14, 1, 1, "both are drawn again in the lower block as children of 154+155"),
    ("U08",  16,  15, 1, 1, ""),
    ("U09",  18,  17, 1, 1, ""),
    ("U10",  19,  20, 1, 1, "19 has two husbands drawn, 20 and 21"),
    ("U11",  19,  21, 2, 1, "19 has two husbands drawn, 20 and 21"),
    ("U12",  23,  22, 1, 1, ""),
    ("U13",  25,  24, 1, 1, ""),
    ("U14",  27,  26, 1, 1, "26 has two wives drawn, 27 and 28, and the plate "
                            "splits his children between their two lines"),
    ("U15",  28,  26, 1, 2, "26's second wife"),
    ("U16",  29,  30, 1, 1, ""),
    ("U17",  32,  31, 1, 1,
     "31 has no leader rule -- his parents are not drawn, so 31+32+97 is a "
     "FOURTH descent block and 31 is one of this table's roots. Re-verified "
     "2026-07-29 at x 3450, y 700 (1300 x 700): leader stubs run from the "
     "vertical rule into rows 33, 35, 36, 38 and 40, and 31's row has none, "
     "although it sits at the same indent as those five and inside the "
     "vertical's extent. The indent is what makes this look like a child line; "
     "the missing stub is what says it is not. 31 is Water as 9+10 are, so the "
     "clan check could not have caught it"),
    ("U18",  33,  34, 1, 1, ""),
    ("U19",  37,  36, 1, 1, ""),
    ("U20",  39,  38, 1, 1, "no children drawn for this marriage"),
    ("U21",  42,  43, 1, 1, ""),
    ("U22",  46,  45, 1, 1, ""),
    ("U23",  48,  47, 1, 1, "48 has two husbands drawn, 47 and 49; 49's '+' line "
                            "sits under 47, who is himself male, so 49 cannot be "
                            "47's spouse"),
    ("U24",  48,  49, 2, 1,
     "48's second husband. The plate prints three consecutive lines -- '47.' as "
     "the primary, then '+ 48.', then '+ 49.' (verified at x 3700, y 2150) -- so "
     "this marriage is drawn inside 47's block, not inside either partner's own. "
     "That is what drawn_under records. Without it neither partner is a block "
     "primary anywhere and 49 is never drawn at all", 47),
    ("U25",  52,  51, 1, 1, ""),
    ("U26",  53,  54, 1, 1, "53 has two husbands drawn, 54 and 55. 54 is drawn "
                            "again in the lower block as the son of 232+233"),
    ("U27",  53,  55, 2, 1, "53's second husband"),
    ("U28",  57,  56, 1, 1, ""),
    ("U29",  58,  59, 1, 1, ""),
    ("U30",  61,  60, 1, 1, "60 has two wives drawn, 61 and 62, and the plate "
                            "splits his children between their two lines"),
    ("U31",  62,  60, 1, 2, "60's second wife"),
    ("U32", 119, 120, 1, 1, ""),
    ("U33", 122, 123, 1, 1, ""),
    ("U34", 125, 126, 1, 1, "126 is drawn again in the lower block as a child of "
                            "158+160; there he is the primary and 125 the '+' line"),

    # ---- lower block ----------------------------------------------------
    ("U35", 154, 155, 1, 1, ""),
    ("U36", 157, 156, 1, 1, ""),
    ("U37", 159, 158, 1, 1, "158 has two wives drawn, 159 and 160, and the plate "
                            "splits his children between their two lines"),
    ("U38", 160, 158, 1, 2, "158's second wife"),
    ("U39", 163, 162, 1, 1, ""),
    ("U40", 164, 165, 1, 1, ""),
    ("U41", 232, 233, 1, 1, "no leader rule enters 232 -- her parents are not drawn"),
    ("U42", 167, 166, 1, 1, ""),
    ("U43", 169, 168, 2, 1, "169's second husband. Her line here carries 'For "
                            "first husband and descendants, see below'"),
    ("U44", 169, 183, 1, 1, "169's first husband. Her line there carries 'For "
                            "second husband and descendants, see above'. Each of "
                            "her two marriages has its own bracket in its own "
                            "place, so paternity IS assigned for both groups"),
    ("U45", 171, 170, 1, 1, ""),
    ("U46", 173, 172, 1, 1, ""),
    ("U47", 175, 174, 1, 1, ""),
    ("U48", 176, 177, 1, 1, ""),
    ("U49", 178, 179, 1, 1, ""),
    ("U50", 182, 181, 1, 1, ""),
    ("U51", 185, 184, 1, 1, ""),
    ("U52", 234,  54, 1, 2, "54's second wife. He is drawn in the upper block as "
                            "53's husband and here as the son of 232+233"),
    ("U53", 236, 235, 1, 1, ""),
    ("U54", 239, 238, 1, 1, ""),
    ("U55", 240, 241, 1, 1, ""),
    ("U56", 243, 242, 1, 1, ""),
    ("U57", 186, 187, 1, 1, ""),
    ("U58", 244, 245, 1, 1, "no children drawn for this marriage"),
    ("U59", 246, 247, 1, 1, "no children drawn for this marriage"),
    ("U60", 254, 255, 1, 1,
     "the plate draws a short rule from 235+236's sibling bracket to this '+' "
     "line, which it does for no other '+' line on the plate. It cannot mean "
     "255 is their child: every one of their children is Water, 236's clan, "
     "and 255 is Eagle. Recorded as 254's husband; the rule is an observation "
     "of the plate, not descent. Verified at x 4700, y 11520"),
    ("U61", 256, 257, 1, 1, ""),
]

# ---------------------------------------------------------------------------
# UNATTACHED BLOCKS -- where the plate PRINTS a couple whose descent it does
# not draw.
# union_id, primary, in the child column of, immediately after this child, note
#
# `primary` is the partner the plate sets on the upper line, the one WITHOUT
# the '+'. It cannot be derived: everywhere else on this plate the woman's
# line is the primary and her husband's is the '+' beneath it, and at 31+32
# Parsons does the opposite. Rooting at the wife would invert the two lines
# and show the reader something the plate does not.
#
# This is layout, not descent. The plate sets these lines at the children's
# indent, inside another bracket's vertical extent, with NO leader stub
# joining them to it: the vertical simply passes their row. Parsons is placing
# them on the page beside the family they married into, while saying nothing
# about whose children they are.
#
# It is recorded because the alternative is worse in both directions. Drawn as
# a descent block of their own -- which is what this table did until
# 2026-07-30 -- they land at generation 1, at the far left, four columns from
# where the plate sets them. Given a leader stub they would assert a descent
# the plate withholds. So the renderer puts the block in the right column and
# in the right place in the sibling order, and draws no stub.
#
# The vertical rule still runs past the row, exactly as on the plate, because
# the block sits BETWEEN two real children of the bracket.
# ---------------------------------------------------------------------------
UNATTACHED_BLOCKS = [
    ("U17", 31, "U05", 29,
     "31+32 and their child 97. The plate prints '31. M. Re˙ʼni. Water' with no "
     "'+' and no leader stub, between 29+30 and 33+34, who are the second and "
     "third children of 9+10. Re-verified 2026-07-30 on the bracket-column "
     "strip x 3320, y 500, 480 x 1100: one vertical carries stubs into 29 and "
     "33 and ENDS at 33; a separate vertical begins at 35 for 11+12's children. "
     "31's row lies between the two stubs and takes none. 31 is Water as 9+10 "
     "are, so the clan check can neither confirm nor deny this -- the evidence "
     "is the absent stub and nothing else."),
]

# ---------------------------------------------------------------------------
# CHILDREN  (each bracketed sibling group on the plate)
# union_id, mother_id, father_id, child_id, note
#   father_id = 0, union_id = "" when the plate does not let paternity be
#   assigned -- which here means the mother has two husbands drawn and only
#   one bracket, so the group hangs off her line alone. Table 1 treats its
#   68 -> 83, 84, 85 exactly this way.
# ---------------------------------------------------------------------------
_GROUPS = [
    # ---- upper block ----------------------------------------------------
    ("U01",   1,   2, [3, 5, 7]),
    ("U02",   3,   4, [9, 11]),
    ("U03",   5,   6, [13]),
    ("U04",   7,   8, [15, 17, 19, 22, 24]),
    ("U05",   9,  10, [26, 29, 33]),
    ("U06",  11,  12, [35, 36, 38, 40, 41, 42, 44]),
    ("U07",  13,  14, [45, 47, 50, 51, 53]),
    ("U08",  16,  15, [56, 58, 60, 63, 64]),
    ("U09",  18,  17, [65, 66]),
    ("",     19,   0, [67, 68, 69, 70, 71, 72, 73, 74]),
    ("U12",  23,  22, [75, 76, 77, 78, 79]),
    ("U13",  25,  24, [80, 81, 82]),
    ("U14",  27,  26, [83, 84]),
    ("U15",  28,  26, [85, 86, 87, 88, 89, 90]),
    ("U16",  29,  30, [91, 92, 93, 94, 95, 96]),
    ("U17",  32,  31, [97]),
    ("U18",  33,  34, [98, 99]),
    ("U19",  37,  36, [100]),
    ("U21",  42,  43, [101, 1010, 102, 103, 104, 105]),
    ("U22",  46,  45, [106, 107, 108, 109, 110, 111, 112, 113, 114, 115]),
    ("",     48,   0, [116, 117, 118]),
    ("U25",  52,  51, [119, 121]),
    ("",     53,   0, [122, 124, 125, 127]),
    ("U28",  57,  56, [128, 129]),
    ("U29",  58,  59, [130, 131, 132, 133, 134, 135, 136]),
    ("U30",  61,  60, [137, 138, 139]),
    ("U31",  62,  60, [140, 141, 142, 143]),
    ("U32", 119, 120, [144, 145, 146]),
    ("U33", 122, 123, [147, 148, 149, 150, 151]),
    ("U34", 125, 126, [152, 153]),

    # ---- lower block ----------------------------------------------------
    ("U35", 154, 155, [14, 156, 158, 161, 162, 164]),
    ("U36", 157, 156, [166, 168, 170, 172]),
    ("U37", 159, 158, [174, 176]),
    ("U38", 160, 158, [126, 178]),
    ("U39", 163, 162, [180, 181]),
    ("U40", 164, 165, [169, 184]),
    ("U41", 232, 233, [54, 235, 237, 238, 240, 242]),
    ("U42", 167, 166, [186, 188, 189, 190, 191, 192, 193, 194, 195]),
    ("U43", 169, 168, [196, 197, 198, 199, 200]),
    ("U44", 169, 183, [225, 226]),
    ("U45", 171, 170, [201, 202, 203, 204, 205, 206]),
    ("U46", 173, 172, [207, 208]),
    ("U47", 175, 174, [209, 210, 211]),
    ("U48", 176, 177, [212, 213, 214, 215, 216, 217]),
    ("U49", 178, 179, [218, 219]),
    ("U50", 182, 181, [220, 221, 222, 223, 224]),
    ("U51", 185, 184, [227, 228]),
    ("U52", 234,  54, [244, 246, 248, 249, 250, 251, 252, 253]),
    ("U53", 236, 235, [254, 256, 258, 259, 260]),
    ("U54", 239, 238, [261, 262, 263, 264]),
    ("U55", 240, 241, [265, 266, 267]),
    ("U56", 243, 242, [268, 269]),
    ("U57", 186, 187, [229, 230, 231]),
    ("U60", 254, 255, [270, 271, 272]),
    ("U61", 256, 257, [273, 274]),
]

_CHILD_NOTES = {
    13:  "drawn again in the lower block as a child of 154+155, carrying "
         "'For descendants, see above'",
    67:  "19 has two husbands drawn, 20 and 21, and the plate gives this group "
         "one bracket off her line; paternity is not assigned",
    116: "48 has two husbands drawn, 47 and 49; the plate gives this group one "
         "bracket off her line, so paternity is not assigned",
    122: "53 has two husbands drawn, 54 and 55, so paternity is not assigned. "
         "The lower block prints 'For descendants see 122, 147-151' on 53's "
         "line under 54, which independently confirms the group AND its "
         "grandchildren -- but it is printed on her line, where descendants "
         "always go, so it says nothing about which husband",
    125: "drawn again in the lower block, where 126 is the primary and 125 the "
         "'+' line",
}

CHILDREN = [
    (union_id, mother, father, child, _CHILD_NOTES.get(child, ""))
    for union_id, mother, father, kids in _GROUPS
    for child in kids
]

# ---------------------------------------------------------------------------
# Notes printed on the plate that are not tied to a single person.
#
# Each of these occupies a sibling slot -- a leader rule runs to it from a
# bracket exactly as it would to a person -- and stands in place of a group
# the plate draws elsewhere. They are not persons and carry no number.
# ---------------------------------------------------------------------------
PLATE_NOTES = [
    ("lower block, col. C", "For descendants, see above",
     "printed on 13's line, in place of the bracket to 45, 47, 50, 51, 53, "
     "which the upper block draws"),
    ("lower block, col. D", "For descendants, see above",
     "printed on 125's line, in place of the bracket to 152, 153, which the "
     "upper block draws"),
    ("lower block, col. D", "For descendants see 122, 147-151",
     "printed on 53's line under 54. The only cross-reference on the plate "
     "that points at this plate's own numbers, and it names both her child "
     "and that child's children"),
    ("lower block, col. C", "For first husband and descendants, see below",
     "printed under 169 where she is 168's wife"),
    ("lower block, col. C", "For second husband and descendants, see above",
     "printed under 169 where she is 183's wife"),
]

CLANS = ["Sun", "Lizard", "Oak", "Water", "Parrot", "Bear", "Badger", "Eagle",
         "Turkey", "Chaparral Cock", "Corn", "Turquoise", "Locust"]

# Three further words stand in the clan position on this plate and are NOT
# clans: "White" (179), "Mexican" (183) and "Mohave" (243). They are recorded
# as printed and deliberately left out of CLANS -- see the note above UNIONS.
# None of the three is a mother, so no child's clan is tested against one.
NON_CLAN_IN_CLAN_POSITION = ["White", "Mexican", "Mohave"]

ORTHOGRAPHY = [
    ("ʼ", "U+02BC", "modifier letter apostrophe", "glottal stop / raised apostrophe as printed"),
    ("˙", "U+02D9", "dot above", "raised dot: aspiration or length"),
    ("˚", "U+02DA", "ring above", "raised ring, at 244 only -- new to this plate"),
    ("˘", "U+02D8", "breve", "at 170 only -- a SPACING breve, over no letter"),
    ("ä", "U+00E4", "a with diaeresis", "at 180 only -- new to this plate"),
    ("ă", "U+0103", "a with breve", ""),
    ("ĕ", "U+0115", "e with breve", ""),
    ("ĭ", "U+012D", "i with breve", ""),
    ("Ĭ", "U+012C", "I with breve", "at 163"),
    ("ŏ", "U+014F", "o with breve", "at 14's second name"),
    ("ŭ", "U+016D", "u with breve", ""),
    ("ᶦ", "U+1DA6", "superscript i", ""),
    ("ᵃ", "U+1D43", "superscript a", ""),
    ("ᵉ", "U+1D49", "superscript e", "at 84 only"),
]

# ---------------------------------------------------------------------------
# ASCII folding, for matching against other spellings
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
    """Diacritic-free lowercase key for fuzzy matching."""
    out = name
    for src, dst in _FOLD.items():
        out = out.replace(src, dst)
    return "".join(c for c in out if c.isalnum()).lower()


def self_check() -> list[str]:
    """Structural checks that must hold for the transcription to be sound."""
    problems = []

    ids = [p[0] for p in PERSONS]
    if len(ids) != len(set(ids)):
        problems.append("PERSONS ids are not unique")

    # This plate's numbering is NOT a unique key -- Parsons numbers two people
    # 101 -- so the ids are the plate's numbers plus one synthetic id per
    # duplicate. The check is therefore "every plate number 1..274 is present
    # exactly once, plus exactly the synthetic ids DUPLICATE_PLATE_NUMBERS
    # declares", not Table 1's "ids == range(1, N+1)".
    synthetic = set(DUPLICATE_PLATE_NUMBERS)
    plate_numbers = sorted(set(ids) - synthetic)
    if plate_numbers != list(range(1, 275)):
        missing = [n for n in range(1, 275) if n not in set(plate_numbers)]
        extra = [n for n in plate_numbers if n > 274]
        problems.append(f"plate numbers are not exactly 1..274 (missing {missing}, extra {extra})")
    for sid, printed in DUPLICATE_PLATE_NUMBERS.items():
        if sid not in set(ids):
            problems.append(f"synthetic id {sid} is declared but not in PERSONS")
        if printed not in set(ids):
            problems.append(f"{sid} claims to print {printed}, which is not a person")

    # The three repeat people must actually carry both of the plate's settings.
    # This is here because the pair lives in two places -- the tuple and
    # REPEAT_PERSON_NAMES -- and a later edit to one is otherwise silent.
    by_id = {p[0]: p for p in PERSONS}
    for pid, (first, second) in REPEAT_PERSON_NAMES.items():
        if pid not in by_id:
            problems.append(f"REPEAT_PERSON_NAMES names {pid}, which is not a person")
            continue
        got = (by_id[pid][3], by_id[pid][4])
        if got != (first, second):
            problems.append(
                f"{pid}: record has {got!r} but REPEAT_PERSON_NAMES declares "
                f"{(first, second)!r}"
            )
        if first == second:
            problems.append(f"{pid} is listed as a repeat but both settings are identical")

    clan = {p[0]: p[6] for p in PERSONS}
    # Laguna clan membership is matrilineal: a child's clan is its mother's.
    for union_id, mother, father, child, _ in CHILDREN:
        if clan[child] and clan[mother] and clan[child] != clan[mother]:
            problems.append(
                f"clan mismatch: child {child} ({clan[child]}) "
                f"vs mother {mother} ({clan[mother]})"
            )

    kids = [c[3] for c in CHILDREN]
    if len(kids) != len(set(kids)):
        problems.append("a person appears as a child more than once")

    union_ids = [u[0] for u in UNIONS]
    if len(union_ids) != len(set(union_ids)):
        problems.append("UNIONS ids are not unique")
    known = set(union_ids)
    for union_id, mother, father, child, _ in CHILDREN:
        if union_id and union_id not in known:
            problems.append(f"child {child} cites union {union_id}, which does not exist")

    spouses = {i for u in UNIONS for i in (u[1], u[2]) if i}
    unplaced = set(ids) - set(kids) - spouses
    if unplaced:
        problems.append(f"persons neither child nor spouse: {sorted(unplaced)}")

    # UNATTACHED_BLOCKS is the only thing that puts these couples on the page
    # at all -- they are reachable from no bracket, so a stale entry here does
    # not misdraw them, it drops them silently. Hold every field against the
    # data: the union exists, the column it names exists, and the child it is
    # printed after really is a child of that column.
    for uid, primary, parent_uid, after, _note in UNATTACHED_BLOCKS:
        if uid not in known:
            problems.append(f"UNATTACHED_BLOCKS names union {uid}, which does not exist")
        if primary not in {i for u in UNIONS if u[0] == uid for i in (u[1], u[2])}:
            problems.append(f"{uid}: primary {primary} is not a partner in that union")
        if parent_uid not in known:
            problems.append(
                f"{uid} is drawn in the child column of {parent_uid}, which does not exist")
        siblings = [c[3] for c in CHILDREN if c[0] == parent_uid]
        if after not in siblings:
            problems.append(
                f"{uid} is drawn after {after}, who is not a child of {parent_uid} "
                f"(its children are {siblings})")
        # The bracket's bottom terminus is drawn from DOM position -- the last
        # node in the column is where the vertical stops. Splice an unattached
        # block in after the last child and the rule would run PAST the last
        # real child, down to a row it does not serve. On the plate the
        # vertical always ends on a child, so this can only be an encoding
        # error, and it is one the eye would not catch.
        elif after == siblings[-1]:
            problems.append(
                f"{uid} is drawn after {after}, the LAST child of {parent_uid}; the "
                "bracket's vertical would then extend past its own last child")
        # A block drawn inside someone else's column must not ALSO be a child
        # somewhere: that would be two placements for one couple.
        for pid in (u[1] for u in UNIONS if u[0] == uid):
            if pid in set(kids):
                problems.append(
                    f"{uid} is an unattached block but its wife {pid} is also a child")
        for pid in (u[2] for u in UNIONS if u[0] == uid):
            if pid in set(kids):
                problems.append(
                    f"{uid} is an unattached block but its husband {pid} is also a child")

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
