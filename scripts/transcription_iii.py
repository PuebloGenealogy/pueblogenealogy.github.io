"""
Verbatim transcription of Table 3, "Genealogy III", from
Elsie Clews Parsons, "Laguna Genealogies",
Anthropological Papers of the American Museum of Natural History, vol. 19, pt. 5
(1923), pp. 133-292.

Source image: sources/parsons-1923-table-3.jpg (3770 x 5503 px)
sha256 38d86b7a7b57ad24e4a25c0e22be0c36b866d38f18988aa960322e320420a200

Read tile by tile at native resolution. This file is the immutable 1923
baseline. Do NOT add research data here -- see the README's privacy boundary.

*** THIS MODULE IS NOT FINISHED. DO NOT REGISTER IT IN make_chart.py's TABLES. ***

ORTHOGRAPHY_VERIFIED is True as of 2026-07-31: the STRUCTURE is read and
checked, and the NAMES are now verified at 5x for **all 261 ids**.
What is still open is the CROSS-REFERENCE audit, not the orthography.
See "ORTHOGRAPHY" at the foot of this docstring.

THE SCAN
--------
3770 x 5503 is about a NINTH of Table 1's pixel count and half of Table 2's.
That makes this plate harder, not easier: tiles read comfortably at 1.5x for
structure, but every diacritic needs 6x. Tiling used here was 1250 x 620 native
at 1.5x, offsets top [1,500,...,4883] and left [0,840,1680,2520].

  sips trap: `--cropOffset 0 0` silently centre-crops the image instead of
  cropping at the origin. Use `1 1`.

Generation columns, native x of the (right-aligned) number:
g1 145 - g2 755 - g3 1293 - g4 1833 - g5 2377 - g6 2920 - g7 3467.
SEVEN generations, the deepest plate in the edition.

HOW THIS PLATE DIFFERS FROM TABLES 1, 2 AND 4
---------------------------------------------
1. IT ASSIGNS PATERNITY THAT TABLES 1 AND 2 LEFT OPEN. The leader rule reaching
   a sibling bracket sits on the line of the parent whose marriage the group
   belongs to. Where someone has two spouses, each spouse's own line either
   carries a leader (that marriage had issue) or does not. Confirmed on
   38/39/40, 62/63/64, 22/23/24 and 85/86/87.

   So 85/86/87 is the same SHAPE as Table 1's 83-85 -- a person with two
   spouses and one bracket -- but here 86's leader is on her own line, the line
   adjacent to husband 85, and 87 has no leader at all. NO EDITORIAL
   ATTRIBUTION IS NEEDED ANYWHERE ON THIS PLATE, and none is made.

2. FOUR COUPLES ARE PRINTED TWICE, each with the descendants line standing in
   for the bracket at the second occurrence. This is Genealogy II's
   SECOND_VISIT_OMITTED shape, four times over:

     7 + 8    issue drawn at the top of block 1; 8 recurs as a child of
              236 + 237, where 7's line reads "For her descendants, see above"
     91 + 92  issue drawn under 27 + 29; 92 recurs as a child of 30 + 31,
              "For her descendants, see above"
     124 +125 issue drawn under 43; 125 recurs as a child of 72 + 73,
              "For offspring, see above"
     152 +153 issue drawn under 68 + 69; 153 recurs as a child of 243 + 244,
              "For her descendants, see above"

   166 and 167 are each printed twice as well, but with no descendants line.
   PERSON 8 IS WHAT JOINS THE PLATE'S TWO BLOCKS: he is the husband of 7 in
   block 1 and a son of 236 + 237 in block 2.

3. TWO DESCENT BLOCKS, and the second one is INDENTED. 230 + 231 head a block
   the plate sets in the generation-2 column, not at the sheet's left edge --
   Genealogy II's root_columns case, not UNATTACHED_BLOCKS. 230's block is not
   descended from 1 + 2; it merely starts further in.

4. THE NUMBERING IS NOT A UNIQUE KEY, twice over. 258 and 259 are each printed
   on two different people, and 256 and 257 appear nowhere on the plate. Both
   pairs verified at 20x. See DUPLICATE_PLATE_NUMBERS. The edition states the
   fact and does not guess at the cause.

5. MANY ENTRIES CARRY NO SEX LETTER -- most of the unnamed g6/g7 children, plus
   155, 193, 195 and 260, which are named or numbered but printed with no F./M.
   Stored as empty, never guessed.

6. FOUR MISPRINTS TO REPRODUCE, NOT FIX -- see PLATE_MISPRINTS.

MISPRINTS
---------
a. 37's SEX LETTER. The plate prints "+ 37. M. Juana. d. Chaparral Cock". 37 is
   the mother of 109-112, whose clan is Chaparral Cock, where her husband 36 is
   Lizard; clan descent, the bracket and the name all make her female. Verified
   at 20x. Stored sex is "F" with the printed letter carried in PLATE_MISPRINTS
   so the chart can show what the plate shows.
b. 50's CLAN SPELLING: "Chapparral Cock", with a doubled p, where her own four
   children 135-138 and every other line on the plate print "Chaparral Cock".
   Verified at 20x.
c. 255's CLAN SPELLING: "Bager" for "Badger". Verified at 20x.
d. 258 / 259 printed twice each; 256 / 257 unused. See above.

TWO BRACKET READINGS THAT NEED A SECOND EYE
-------------------------------------------
Both are recorded in plate_note on the people concerned.

i.  43's two husbands. One unbroken vertical at native x 2267 runs from y 2157
    to y 2222 with stubs to 124 and 126, and TWO leaders enter it: 43's own line
    at 124's row and 45's line at 126's row. Encoded per the convention in (1)
    as 43 + 44 -> 124 and 43 + 45 -> 126. The alternative reading is a single
    undivided bracket of 43's two children with the father unstated.
ii. 22 and 25. Same shape: one unbroken, unoffset vertical at native x 1749 from
    y 4339 to y 4425, stubs to 80, 82 and 83, leaders entering at 80's row (22)
    and 83's row (25). Encoded as 22 -> 80, 82 and 25 -> 83. All three children
    are Corn, so clan descent cannot separate them.

    For contrast, 86's and 89's brackets at native x 2853 ARE visibly offset
    where they meet, so this plate does distinguish adjacent brackets when it
    means to -- which is what makes (i) and (ii) worth checking.

ORTHOGRAPHY -- WHY EVERY NAME BELOW WAS READ TWICE
--------------------------------------------------
At 1.5x this scan cannot separate `˙` U+02D9 (raised dot) from `ʼ` U+02BC
(apostrophe); the first pass defaulted to `ʼ` and was WRONG. At 6x the two are
plainly different:

    person 27 is Na˙ʼtsiwă, not Naʼʼtsiwă -- a round dot, then an apostrophe
    person 193 is Ko˙ri, with no apostrophe at all

and Genealogy II's 189, transcribed in this repo from a far larger scan, is
Ko˙ri too. This is the failure METHOD.md records for Table 1's #25.

A 5x pass (400-440 native px wide, rendered to 2200) separates them reliably,
and it has now been run over EVERY id on the plate, in three stretches:

  ids 1-84, 230-247   generations 1-4 of both blocks. Sixteen corrections:

    7 Kyi˙waaid˙yuwitsʼă   8 Dzaaiʼy˙unăiʼ      13 Saiyăpʼᵃ
   15 Iya˙ʼn˙ă            17 Waiʼs˙iro          20 Hi˙ʼn˙iăitsʼă
   22 Dzaiaaiʼdʼyuwitsʼă  32 Go˙tyʼi˙ăiʼ        43 Tsa˙kʼwiʼtsʼă
   45 Wi˙ʼsh˙gă           49 Koi˙ʼs             52 Shta˙ʼy˙ăi
   54 Kʼăya˙s˙iwă         62 Kwi˙ʼn˙yeʼtsʼa    232 Wa˙g˙ĕnidyuwitsʼă
  238 Ha˙d˙ăiʼyănyi

  ids 85-183, 248-257  generation 5. Twelve corrections:

   87 Ga˙ʼg˙iri          90 G˙yiʼmi           91 Id˙yim˙ĕ
   94 Tsshka˙a          104 Howa˙kʼa         143 Dziwi˙ʼᶦt˙yĭăi
  155 Yoʼsiro           164 Shtshowain˙ăʼ    168 Dziu˙ʼtyᶦty˙ᶦ
  169 E˙d˙ă             174 Owi˙ʼd˙zĭraiʼ    255 Ho˙py˙di˙wa

  ids 184-229, 258-261  generations 6-7. ONE correction:

  192 Kiwaʼdyuwi -- no raised dot between d and y. Genealogy II's 188, the
      same person, HAS one. The plates disagree and this file records what
      THIS plate prints; the divergence is in 192's plate_note.

Note 45 also lost a breve: the plate prints Wi˙ʼsh˙gă, not Wĭ˙ʼsh˙gă. And note
that a name being spelled one way here is not a claim it is spelled that way
where the plate prints the person twice -- 152 and 153 differ between their two
occurrences, which is recorded in their plate_note and is a finding about the
plate, not an unresolved reading.

ONE GLYPH IS STILL OPEN, and it is now a pattern rather than a single mark.
At 154, 156, 157, 228 and 242 the final mark reads as a TURNED comma (opening
quote) rather than the U+02BC used everywhere else -- five instances, enough
that it may be a distinct sort rather than print noise. ALL FIVE ARE LEFT AS
U+02BC; do not introduce a new codepoint on this evidence alone, and do not
"tidy" it away either. Resolving it needs a 20x look at the five against a
known U+02BC on the same line of type.

CROSS-REFERENCES STILL TO CHECK
-------------------------------
This is the remaining gate, and it is independent of the orthography above.
Cross-check the people this plate references into Genealogies I and II against
scripts/transcription.py and scripts/transcription_ii.py -- and where the two
plates disagree, RECORD WHAT THIS PLATE PRINTS.

transcription_ii.py records that Parsons's "See Gen. I, n" references run exact
through Genealogy I's person 53 and ONE HIGH from its person 66 onward. This
plate cites Gen. I at 8, 9, 20, 21, 31, 33, 34, 35, 37, 45, 47, 48, 78, 79, 90,
97, 98, 99, 100, 101, 103, 104 -- and at 149, which cannot resolve, Genealogy I
having 104 people. Person 173 is Yăaiʼdyidʼyuwi, whom Genealogy II's 204 cites
as Gen. I 49.

  173's "See Gen. I, 149" was RE-ZOOMED at 5x and is real -- it is what the
  plate prints, not a misreading of 49. It still does not resolve. The rest of
  the set has NOT been checked; do that before publishing.
"""

ORTHOGRAPHY_VERIFIED = True

# (id, generation, sex, name_as_printed, alt_name, age, clan,
#  vital_note, origin, cross_ref, plate_note)
#
# id == the plate's printed number everywhere except ids 256 and 257, which are
# synthetic: see DUPLICATE_PLATE_NUMBERS.
_P = [
    # ---- block 1, generation 1 -------------------------------------------
    (1,   1, "F", "",                      "", "",   "Corn",           "",        "",           "", "name printed as a dash"),
    (2,   1, "M", "",                      "", "",   "",               "",        "",           "", "name and clan both printed as dashes"),
    # ---- block 1, generation 2 -------------------------------------------
    (3,   2, "F", "",                      "", "",   "Corn",           "",        "",           "", "name printed as a dash"),
    (4,   2, "M", "",                      "", "",   "Oak",            "",        "",           "", "name printed as a dash"),
    (5,   2, "F", "",                      "", "",   "Corn",           "",        "",           "", "name printed as a dash"),
    (6,   2, "M", "",                      "", "",   "",               "",        "",           "", "name and clan both printed as dashes"),
    # ---- block 1, generation 3 -------------------------------------------
    (7,   3, "F", "Kyi˙waaid˙yuwitsʼă",   "", "",   "Corn",           "",        "",           "", "printed twice; drawn with issue at the head of block 1"),
    (8,   3, "M", "Dzaaiʼy˙unăiʼ",         "", "",   "Parrot",         "",        "Acoma",      "", "printed twice; a son of 236+237 in block 2 and the husband of 7 in block 1"),
    (9,   3, "M", "Garashdyiʼ",            "", "",   "Corn",           "",        "",           "", ""),
    (10,  3, "F", "Ais˙dyuwiʼtsʼa",        "", "",   "Lizard",         "",        "",           "", ""),
    (11,  3, "M", "Dyi˙ʼnă",               "", "",   "Corn",           "",        "",           "", ""),
    (12,  3, "F", "Goaiʼsdyuwitsʼa",       "", "",   "Water",          "",        "",           "", "no issue recorded"),
    (13,  3, "F", "Saiyăpʼᵃ",               "", "",   "Sun",            "",        "",           "", "second wife of 11"),
    (14,  3, "M", "A˙ʼtsʼăyĕ",             "", "",   "Corn",           "",        "",           "", ""),
    (15,  3, "F", "Iya˙ʼn˙ă",              "", "",   "Oak",            "d.",      "",           "", ""),
    (16,  3, "F", "Ĭya˙ʼsi",               "", "70", "Bear",           "",        "",           "", "second wife of 14"),
    (17,  3, "M", "Waiʼs˙iro",             "", "",   "Corn",           "",        "",           "", ""),
    (18,  3, "F", "Juana Maria",           "", "",   "Badger",         "",        "Zuñi",       "", ""),
    (19,  3, "M", "A˙ʼushuyăi",            "", "",   "Corn",           "",        "",           "", ""),
    (20,  3, "F", "Hi˙ʼn˙iăitsʼă",         "", "",   "Lizard",         "",        "",           "", "the plate prints '(Sister of 10)' beneath the name"),
    (21,  3, "F", "Dyia˙ʼro",              "", "",   "Sun",            "",        "",           "", "second wife of 19"),
    (22,  3, "F", "Dzaiaaiʼdʼyuwitsʼă",    "", "",   "Corn",           "d.",      "",           "", "her bracket and 25's share one unbroken vertical; see the docstring"),
    (23,  3, "M", "",                      "", "",   "Sun",            "",        "",           "", "name printed as a dash"),
    (24,  3, "M", "Ai˙ʼtyʼiai",            "", "",   "Turkey",         "",        "",           "", "second husband of 22; no issue recorded"),
    (25,  3, "F", "Wayaiduitsa",           "", "",   "Corn",           "",        "",           "", "her bracket and 22's share one unbroken vertical; see the docstring"),
    (26,  3, "M", "Oshăʼ",                 "", "",   "Eagle",          "",        "",           "", ""),
    # ---- block 1, generation 4 -------------------------------------------
    (27,  4, "M", "Na˙ʼtsiwă",             "", "",   "Corn",           "d. 1917", "",           "", ""),
    (28,  4, "F", "Shawiʼ",                "", "",   "Oak",            "d.",      "",           "", ""),
    (29,  4, "F", "Hanaiʼsitsʼa",          "", "",   "Water",          "d.",      "",           "", "second wife of 27"),
    (30,  4, "M", "Tsiwi˙ʼyai",            "", "67", "Corn",           "",        "",           "", ""),
    (31,  4, "F", "Lopez",                 "", "50", "Eagle",          "",        "Zuñi",       "", ""),
    (32,  4, "M", "Go˙tyʼi˙ăiʼ",            "", "65", "Corn",           "",        "",           "See Gen. II, 55", ""),
    (33,  4, "F", "Kawiʼtsʼirăiʼ",         "", "50", "Water",          "",        "",           "See Gen. II, 53", ""),
    (34,  4, "M", "Dyairiyăi",             "", "",   "Lizard",         "",        "",           "", ""),
    (35,  4, "F", "Dzioriăi",              "", "",   "Turkey",         "",        "",           "", ""),
    (36,  4, "M", "Gayaiʼd˙yai",           "", "",   "Lizard",         "d.",      "",           "", ""),
    (37,  4, "F", "Juana",                 "", "",   "Chaparral Cock", "d.",      "",           "", "the plate prints the sex letter as 'M.'; she is the mother of 109-112"),
    (38,  4, "F", "Dziomăiʼtsʼă",          "", "",   "Sun",            "d.",      "",           "", ""),
    (39,  4, "M", "Hiaiʼai",               "", "",   "Corn",           "",        "",           "", ""),
    (40,  4, "F", "Kăshiĕ˙ʼnă",            "", "",   "Parrot",         "",        "",           "", "second wife of 39"),
    (41,  4, "F", "Tsaiasdyuwitsʼă",       "", "",   "Sun",            "",        "",           "", ""),
    (42,  4, "M", "Ki˙ʼowăiʼ",             "", "",   "Bear",           "",        "",           "", ""),
    (43,  4, "F", "Tsa˙kʼwiʼtsʼă",         "", "",   "Oak",            "d.",      "",           "", "her bracket carries two leaders, hers and 45's; see the docstring"),
    (44,  4, "M", "Kʼawi˙ʼrăi",            "", "",   "Parrot",         "d.",      "",           "", ""),
    (45,  4, "M", "Wi˙ʼsh˙gă",             "", "",   "Antelope",       "d.",      "",           "", "second husband of 43; his line carries a leader into 43's bracket"),
    (46,  4, "F", "Shi˙ʼmănai",            "", "",   "Oak",            "",        "",           "", ""),
    (47,  4, "M", "Can Gunn",              "", "",   "White",          "",        "",           "", ""),
    (48,  4, "F", "Goyawe",                "", "",   "Oak",            "",        "",           "", "no spouse and no issue recorded"),
    (49,  4, "M", "Koi˙ʼs",                 "", "",   "Bear",           "",        "",           "", ""),
    (50,  4, "F", "Tsiwaiidyi",            "", "40", "Chaparral Cock", "",        "",           "", "the plate prints the clan as 'Chapparral Cock'; her own children print 'Chaparral Cock'"),
    (51,  4, "F", "Kio˙ʼtyʼiăi",           "", "",   "Bear",           "",        "",           "", ""),
    (52,  4, "M", "Shta˙ʼy˙ăi",            "", "35", "Sun",            "",        "",           "", ""),
    (53,  4, "F", "Shăaiʼdyidyuwitsʼă",    "", "",   "Bear",           "d.",      "",           "", ""),
    (54,  4, "M", "Kʼăya˙s˙iwă",           "", "",   "Bear",           "",        "",           "", ""),
    (55,  4, "F", "Gaiya˙ʼᵃtsʼimăi",       "", "",   "Bear",           "",        "",           "", ""),
    (56,  4, "M", "Găʼpydyĭwă",            "", "",   "Badger",         "",        "",           "", ""),
    (57,  4, "F", "Kaya˙ʼsh",              "", "",   "Chaparral Cock", "",        "",           "", ""),
    (58,  4, "F", "Dzaiʼᶦshdyiăiʼ",        "", "",   "Badger",         "",        "",           "", ""),
    (59,  4, "M", "Dziwa˙ʼhăyᵃᶦ",          "", "",   "Chaparral Cock", "",        "",           "", ""),
    (60,  4, "F", "Kʼapokaʼă",             "", "",   "Badger",         "d.",      "",           "", ""),
    (61,  4, "M", "Poraiga",               "", "",   "Corn",           "",        "",           "", ""),
    (62,  4, "F", "Kwi˙ʼn˙yeʼtsʼa",        "", "",   "Badger",         "d.",      "",           "", "no issue recorded"),
    (63,  4, "M", "Kaushtkună",            "", "",   "Chaparral Cock", "",        "",           "", ""),
    (64,  4, "F", "Shi˙ʼkʼăyăi",           "", "",   "Turkey",         "",        "",           "", "second wife of 63"),
    (65,  4, "M", "Kʼăwaiʼᶦsiyăi",         "", "",   "Badger",         "d.",      "",           "", ""),
    (66,  4, "F", "Kowaiʼd˙yuwitsʼă",      "", "",   "Water",          "",        "",           "", "no issue recorded"),
    (67,  4, "M", "Carlisle School Indian","", "",   "",               "",        "",           "", "second husband of 66; no clan printed"),
    (68,  4, "F", "Me˙yuʼshkʼa",           "", "65", "Lizard",         "",        "",           "", ""),
    (69,  4, "M", "Tsa˙sdiye",             "", "",   "Sun",            "d.",      "",           "", ""),
    (70,  4, "M", "Tᵃpinoshkă",            "", "",   "Lizard",         "",        "",           "", ""),
    (71,  4, "F", "Dyayonai",              "", "",   "Parrot",         "",        "",           "", ""),
    (72,  4, "F", "Lilly",                 "", "",   "Lizard",         "",        "",           "", ""),
    (73,  4, "M", "Kaaisiro",              "", "",   "Locust",         "d.",      "",           "", ""),
    (74,  4, "F", "Shayaʼai",              "", "",   "Sun",            "",        "",           "See Gen. I, 21; Gen. II, 171", ""),
    (75,  4, "M", "Kʼuʼna˙shᵘ",            "", "",   "Sun",            "",        "",           "See Gen. I, 20; Gen. II, 170", ""),
    (76,  4, "F", "Gwi˙ʼshkaiĕ",           "", "",   "Sun",            "",        "",           "", ""),
    (77,  4, "M", "Solomon Day",           "", "",   "Corn",           "",        "",           "", "no issue recorded"),
    (78,  4, "M", "Dyiamunyi",             "", "",   "Sun",            "",        "",           "", ""),
    (79,  4, "M", "",                      "", "",   "Sun",            "",        "",           "", "name printed as a dash"),
    (80,  4, "M", "Tsita",                 "", "",   "Corn",           "",        "",           "", ""),
    (81,  4, "F", "Koadyuma",              "", "",   "Parrot",         "",        "",           "", "no issue recorded"),
    (82,  4, "F", "",                      "", "",   "Corn",           "d.",      "",           "", "name printed as a dash"),
    (83,  4, "M", "Waiyais˙iro",           "", "",   "Corn",           "d.",      "",           "", ""),
    (84,  4, "F", "Kʼoaisiĕ",              "", "",   "Water",          "d.",      "",           "", ""),
    # ---- block 1, generation 5 -------------------------------------------
    (85,  5, "M", "Dzisᶦtyᵘʼ",             "", "",   "Oak",            "",        "",           "", ""),
    (86,  5, "F", "Kiwaityi",              "", "",   "Turquoise",      "",        "",           "", ""),
    (87,  5, "M", "Ga˙ʼg˙iri",             "", "",   "Turkey",         "",        "",           "", "second husband of 86; no issue recorded"),
    (88,  5, "F", "Annie",                 "", "",   "Oak",            "",        "",           "", ""),
    (89,  5, "F", "Nămăiʼ",                "", "40", "Oak",            "",        "",           "See Gen. I, 17; Gen. II, 167", ""),
    (90,  5, "M", "G˙yiʼmi",               "", "45", "Sun",            "",        "",           "See Gen. I, 16; Gen. II, 166", ""),
    (91,  5, "M", "Id˙yim˙ĕ",              "", "",   "Water",          "",        "",           "", "printed twice; drawn with issue under 27+29"),
    (92,  5, "F", "Gauw˙aiʼd˙yuwi",        "", "24", "Eagle",          "",        "",           "", "printed twice; her second line reads 'For her descendants, see above'"),
    (93,  5, "M", "San Juan",              "", "",   "Water",          "",        "",           "", ""),
    (94,  5, "M", "Tsshka˙a",              "", "",   "Water",          "",        "",           "", ""),
    (95,  5, "F", "Hiusdyawiʼtsʼa",        "", "",   "",               "",        "",           "", "no clan printed; no issue recorded"),
    (96,  5, "M", "",                      "", "",   "Water",          "",        "",           "", "name printed as a dash"),
    (97,  5, "F", "",                      "", "",   "Water",          "",        "",           "", "name printed as a dash"),
    (98,  5, "F", "Jsaishdyiăiʼ",          "", "18", "Eagle",          "",        "",           "", ""),
    (99,  5, "F", "Dzaăityʼid˙yuwitsʼă",   "", "",   "Eagle",          "d. 1918", "",           "", ""),
    (100, 5, "M", "",                      "", "",   "",               "",        "San Domingo","", "name printed as a dash; no clan printed"),
    (101, 5, "M", "Dziŏ˙kwid˙yuʼă",        "", "19", "Water",          "",        "",           "See Gen. II, 124", ""),
    (102, 5, "F", "Gowak˙ʼad˙yăi",         "", "18", "Water",          "",        "",           "See Gen. II, 125", ""),
    (103, 5, "M", "Yo˙ʼkwi",               "", "23", "Chaparral Cock", "",        "",           "See Gen. II, 126", ""),
    (104, 5, "F", "Howa˙kʼa",              "", "",   "Water",          "d. 1919, at 13", "",    "See Gen. II, 127", ""),
]

# 105-111: number, dash, clan. No names and no sex letters.
_P += [(i, 5, "", "", "", "", "Turkey", "", "", "", "name printed as a dash; no sex printed")
       for i in (105, 106, 107, 108)]
_P += [(i, 5, "", "", "", "", "Chaparral Cock", "", "", "", "name printed as a dash; no sex printed")
       for i in (109, 110, 111)]

_P += [
    (112, 5, "M", "Kaaigŭrŭr",             "", "",   "Chaparral Cock", "",        "", "", ""),
    (113, 5, "F", "Wakaĭ",                 "", "",   "Corn",           "",        "", "", ""),
    (114, 5, "M", "Witĕiĕ",                "", "",   "Sun",            "",        "", "", ""),
    (115, 5, "F", "Annie",                 "", "",   "Water",          "",        "", "", ""),
    (116, 5, "F", "Tsi˙ʼwaʼkʼă",           "", "25", "Parrot",         "",        "", "", ""),
    (117, 5, "M", "Sha˙shkᵃ",              "", "",   "Chaparral Cock", "",        "", "", ""),
    (118, 5, "F", "",                      "", "",   "Parrot",         "",        "", "", "name printed as a dash"),
]
_P += [(i, 5, "", "", "", "", "Sun", "", "", "", "name printed as a dash; no sex printed")
       for i in range(119, 124)]
_P += [
    (124, 5, "M", "Kaw˙a˙ʼkʼăyă",          "", "",   "Oak",            "",        "", "", "printed twice; drawn with issue under 43"),
    (125, 5, "F", "Dzi˙răi",               "", "",   "Lizard",         "",        "", "", "printed twice; her second line reads 'For offspring, see above'"),
    (126, 5, "F", "Dzaiʼch˙u",             "", "",   "Oak",            "d.",      "", "", ""),
]
_P += [(i, 5, "", "", "", "", "Oak", "", "", "", "name printed as a dash; no sex printed")
       for i in range(127, 135)]
_P += [
    (135, 5, "F", "", "", "", "Chaparral Cock", "", "", "", "name printed as a dash"),
    (136, 5, "M", "", "", "", "Chaparral Cock", "", "", "", "name printed as a dash"),
    (137, 5, "M", "", "", "", "Chaparral Cock", "", "", "", "name printed as a dash"),
    (138, 5, "M", "", "", "", "Chaparral Cock", "", "", "", "name printed as a dash"),
]
_P += [(i, 5, "", "", "", "", "Bear", "", "", "", "name printed as a dash; no sex printed")
       for i in (139, 140, 141)]
_P += [
    (142, 5, "",  "",                      "", "",   "Chaparral Cock", "", "", "", "name printed as a dash; no sex printed"),
    (143, 5, "M", "Dziwi˙ʼᶦt˙yĭăi",        "", "",   "Badger",         "", "", "", ""),
    (144, 5, "F", "",                      "", "",   "Badger",         "", "", "", "name printed as a dash"),
    (145, 5, "",  "",                      "", "",   "Badger",         "", "", "", "name printed as a dash; no sex printed"),
]
_P += [(i, 5, "", "", "", "", "Turkey", "", "", "", "name printed as a dash; no sex printed")
       for i in range(146, 152)]
_P += [
    (152, 5, "M", "Dzaiʼgai",              "", "",   "Lizard",         "",        "", "See Gen. I, 98", "printed twice; drawn with issue under 68+69. THE TWO OCCURRENCES ARE SPELLED DIFFERENTLY: under 68+69 the plate prints Dzaiʼgai, under 243+244 it prints Dzai˙ʼy˙ai. The first is recorded here. Re-zoom both before publishing"),
    (153, 5, "F", "Shumaiʼ",               "", "30", "Badger",         "",        "", "See Gen. I, 97", "printed twice; her second line reads 'For her descendants, see above'. THE TWO OCCURRENCES ARE SPELLED DIFFERENTLY: under 68+69 the plate prints Shumaiʼ with no age and 'See Gen. I, 97', under 243+244 Shu˙măĭʼ with the age 30 and 'See Gen. I, 9'. The first is recorded here"),
    (154, 5, "M", "Yaʼdôkyʼ",              "", "",   "Lizard",         "d.",      "", "", ""),
    (155, 5, "",  "Yoʼsiro",               "", "",   "Chaparral Cock", "d. 1914", "",
     "For first husband and descendants, see Gen. | II, 126, 158, 160 | For third husband and descendant, see Gen. | I, 8, 90",
     "no sex printed; the cross-reference is set over four lines, split here at the plate's own breaks"),
    (156, 5, "M", "Pʼĕʼnitsʼaʼyo",         "", "",   "Lizard",         "",        "", "", ""),
    (157, 5, "M", "Dziotyʼ",               "", "",   "Lizard",         "",        "", "", ""),
    (158, 5, "M", "Góa˙ʼtyʼiăi",           "", "",   "Lizard",         "",        "", "", ""),
    (159, 5, "F", "Kyiwisdyuwitsʼa",       "", "",   "Lizard",         "d. at 45","", "", ""),
    (160, 5, "M", "Oshare",                "", "",   "Parrot",         "",        "", "", ""),
    (161, 5, "F", "",                      "", "",   "Sun",            "",        "", "", "name printed as a dash"),
    (162, 5, "F", "Minni",                 "", "",   "Lizard",         "d.",      "", "See Gen. II, 27", ""),
    (163, 5, "M", "Dzaiʼsiyăiʼ",           "", "",   "Water",          "",        "", "See Gen. II, 26", ""),
    (164, 5, "M", "Shtshowain˙ăʼ",         "", "",   "Lizard",         "",        "", "", ""),
    (165, 5, "F", "Dyaioʼrăi",             "", "",   "Lizard",         "",        "", "", ""),
    (166, 5, "F", "Kowaiʼdyui",            "", "",   "Lizard",         "d. 1918", "", "", "printed twice, with no descendants line either time"),
    (167, 5, "M", "Dziwaiʼid˙yirăiʼ",      "", "",   "Water",          "",        "", "", "printed twice, with no descendants line either time"),
    (168, 5, "F", "Dziu˙ʼtyᶦty˙ᶦ",         "", "",   "Lizard",         "",        "", "", ""),
    (169, 5, "F", "E˙d˙ă",                 "", "",   "Lizard",         "",        "", "", ""),
    (170, 5, "M", "Dziwaiʼisiro",          "", "",   "Sun",            "",        "", "See Gen. I, 45; Gen. II, 191", ""),
    (171, 5, "F", "Kuyăiʼd˙yid˙uwĕʼ",      "", "",   "Sun",            "",        "", "See Gen. I, 48; Gen. II, 192", ""),
    (172, 5, "F", "Edna",                  "", "",   "Sun",            "",        "", "See Gen. II, 193", ""),
    (173, 5, "F", "Yăaiʼdyid˙yuwi",        "", "",   "Sun",            "",        "", "See Gen. I, 149; Gen. II, 194", "the Gen. I reference cannot resolve: Genealogy I has 104 people. Re-read at 6x"),
    (174, 5, "M", "Owi˙ʼd˙zĭraiʼ",         "", "",   "Sun",            "",        "", "See Gen. I, 47; Gen. II, 195", ""),
    (175, 5, "F", "",                      "", "",   "Sun",            "",        "", "", "name printed as a dash"),
    (176, 5, "",  "",                      "", "",   "Sun",            "",        "", "", "name printed as a dash; no sex printed"),
    (177, 5, "",  "",                      "", "",   "Sun",            "",        "", "", "name printed as a dash; no sex printed"),
    (178, 5, "F", "Hityi",                 "", "40", "Water",          "",        "", "", ""),
    (179, 5, "M", "Gaiʼsi˙wă",  "Bert Wetmore", "30", "Sun",           "",        "", "", "English name printed in parentheses on the plate"),
    (180, 5, "F", "Osharani",              "", "30", "Water",          "",        "", "", ""),
    (181, 5, "M", "Shkashi",               "", "",   "Water",          "",        "", "", ""),
    (182, 5, "F", "",                      "", "",   "Corn",           "",        "", "", "name printed as a dash; no issue recorded"),
    (183, 5, "M", "Shawisyiĕ",             "", "",   "Water",          "d. 1918", "", "", ""),
]
# ---- block 1, generation 6 ----------------------------------------------
_P += [(i, 6, "", "", "", "", "Turquoise", "", "", "", "name printed as a dash; no sex printed")
       for i in range(184, 190)]
_P += [
    (190, 6, "F", "Shăaityʼid˙yuweʼ",      "", "23", "Oak", "", "", "See Gen. II, 186", ""),
    (191, 6, "M", "Ramona",                "", "50", "Turkey", "", "Sant Ana", "See Gen. II, 187", ""),
    (192, 6, "F", "Kiwaʼdyuwi",            "", "22", "Oak", "", "", "See Gen. I, 33; Gen. II, 188",
     "this plate prints no raised dot between d and y, where Gen. II's 188 has one"),
    (193, 6, "",  "Ko˙ri",                 "", "21", "Oak", "", "", "See Gen. I, 31; Gen. II, 189", "no sex printed"),
    (194, 6, "M", "Tsiʼd˙yimĕʼ",           "", "17", "Oak", "", "", "See Gen. I, 34; Gen. II, 191", ""),
    (195, 6, "",  "Sha˙tyʼi",              "", "14", "Oak", "", "", "See Gen. I, 35; Gen. II, 192", "no sex printed"),
    (196, 6, "M", "Shka˙nai",              "", "",   "Oak", "", "", "", ""),
    (197, 6, "M", "Shkawaiyu",             "", "",   "Oak", "", "", "", ""),
    (198, 6, "M", "Dyăiʼtsdyămŭr",         "", "6",  "Oak", "", "", "See Gen. I, 37; Gen. II, 194", ""),
    (199, 6, "F", "Kyiwatyuwitsʼă",        "", "",   "Oak", "", "", "", ""),
    (200, 6, "M", "",                      "", "",   "Eagle", "", "", "", "name printed as a dash"),
    (201, 6, "M", "",                      "", "",   "Eagle", "", "", "", "name printed as a dash"),
    (202, 6, "M", "Tsiᶦshdyĭʼwă",          "", "3",  "Water", "", "", "See Gen. II, 152", ""),
    (203, 6, "F", "Gaiʼtsdyui",            "", "5 mos.", "Water", "", "", "See Gen. II, 153", ""),
    (204, 6, "",  "",                      "", "",   "Corn", "", "", "", "name printed as a dash; no sex printed"),
]
_P += [(i, 6, "", "", "", "", "Water", "", "", "", "name printed as a dash; no sex printed")
       for i in range(205, 212)]
_P += [
    (212, 6, "M", "Peauʼsiwă",             "", "",   "Parrot", "", "", "", ""),
    (213, 6, "F", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
]
_P += [(i, 6, "", "", "", "", "Lizard", "", "", "", "name printed as a dash; no sex printed")
       for i in range(214, 218)]
_P += [
    (218, 6, "F", "",                      "", "",   "Badger",         "", "", "See Gen. I, 101", "name printed as a dash"),
    (219, 6, "F", "",                      "", "",   "Badger",         "", "", "See Gen. I, 103", "name printed as a dash"),
    (220, 6, "F", "Dzitdziro",             "", "",   "Chaparral Cock", "", "", "", ""),
    (221, 6, "M", "Dzawaiʼd˙yăiʼ",         "", "",   "Sun",            "", "", "", ""),
    (222, 6, "F", "Dzaaiʼd˙yid˙yuwe",      "", "",   "Lizard",         "", "", "Gen. II, 83", "the cross-reference is printed without a leading 'See'"),
    (223, 6, "F", "Ha˙tsʼe",               "", "",   "Lizard",         "", "", "Gen. II, 84", "the cross-reference is printed without a leading 'See'"),
    (224, 6, "F", "Tsaaimadyaita",         "", "",   "Water",          "", "", "", ""),
    (225, 6, "M", "Aiyudyaisiwa",          "", "",   "Water",          "", "", "", ""),
    (226, 6, "M", "Watye",                 "", "5",  "Water",          "", "", "", ""),
    # ---- block 1, generation 7 -------------------------------------------
    (227, 7, "F", "Shawityi",              "", "6",  "Oak", "", "", "", ""),
    (228, 7, "M", "Awieʼ",                 "", "4",  "Oak", "", "", "", ""),
    (229, 7, "M", "Yoreni",                "", "1",  "Oak", "", "", "", ""),
    # ---- block 2, generation 2 (the plate indents this block) -------------
    (230, 2, "F", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
    (231, 2, "M", "Mariano Quedesanto",    "", "",   "Eagle",  "", "", "", ""),
    # ---- block 2, generation 3 -------------------------------------------
    (232, 3, "F", "Wa˙g˙ĕnidyuwitsʼă",     "", "",   "Parrot", "", "", "", ""),
    (233, 3, "M", "Shiwănă",               "", "",   "Oak",    "", "", "", ""),
    (234, 3, "F", "Lopina",                "", "",   "Parrot", "", "", "", "no issue recorded"),
    (235, 3, "M", "",                      "", "",   "Turkey", "", "", "", "name printed as a dash"),
    (236, 3, "F", "Kiwaʼaitsʼă",           "", "",   "Parrot", "", "", "", ""),
    (237, 3, "M", "Kʼaiyaiʼᶦtyʼiʼ",        "", "",   "Lizard", "", "", "", ""),
    # ---- block 2, generation 4 -------------------------------------------
    (238, 4, "M", "Ha˙d˙ăiʼyănyi",         "", "",   "Parrot", "", "", "", ""),
    (239, 4, "F", "",                      "", "",   "Water",  "", "", "", "name printed as a dash; no issue recorded"),
    (240, 4, "F", "Yo˙nimaitsʼă",          "", "48", "Parrot", "", "", "", ""),
    (241, 4, "M", "Tsaauʼs˙diyai", "Jefferson", "51", "Turkey", "", "", "", "English name printed in parentheses on the plate"),
    (242, 4, "M", "Shipʼaʼpʼ",             "", "",   "Parrot", "", "", "", "a full point is printed after the clan"),
    (243, 4, "M", "Dziwishpirăiʼ",         "", "70", "Parrot", "", "", "See Gen. I, 79", "the plate prints no point after the age"),
    (244, 4, "F", "Tsa˙tsʼiʼ",             "", "",   "Badger", "d. in 1905", "", "See Gen. I, 78", ""),
    (245, 4, "M", "Dolivio",               "", "",   "Parrot", "", "", "", ""),
    (246, 4, "M", "Dziwi˙ʼs˙iyăi",         "", "",   "Parrot", "", "", "", ""),
    (247, 4, "F", "Helena",                "", "",   "Chaparral Cock", "", "", "", "no issue recorded"),
    # ---- block 2, generation 5 -------------------------------------------
    (248, 5, "M", "Oyʼo˙ʼri",              "", "21", "Parrot", "", "", "", ""),
    (249, 5, "F", "Kyiaiʼsdyuwitsʼă",      "", "",   "Parrot", "", "", "", ""),
    (250, 5, "M", "Aʼud˙yăiʼ",             "", "",   "Bear",   "", "", "", ""),
    (251, 5, "M", "Tsiʼᶦsh",               "", "",   "Parrot", "", "", "", ""),
    (252, 5, "F", "Lope",                  "", "",   "Parrot", "", "", "", ""),
    (253, 5, "M", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
    (254, 5, "F", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
    (255, 5, "M", "Ho˙py˙di˙wa",           "", "25", "Badger", "", "", "See Gen. I, 99", "the plate prints the clan as 'Bager'"),
    # ids 256 and 257 are synthetic: the plate prints 258 and 259 here, and
    # prints those same two numbers again on 258 and 259 below.
    (256, 5, "F", "Dzaiʼsdyui",            "", "21", "Badger", "", "", "See Gen. I, 100", "the plate numbers this person 258; a different person is also numbered 258"),
    (257, 5, "M", "",                      "", "",   "",       "", "Zuñi", "See Gen. I, 101", "the plate numbers this person 259; a different person is also numbered 259. Name printed as a dash; no clan printed"),
    # ---- block 2, generation 6 -------------------------------------------
    (258, 6, "F", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
    (259, 6, "M", "",                      "", "",   "Parrot", "", "", "", "name printed as a dash"),
    (260, 6, "",  "",                      "", "",   "Parrot", "", "", "", "name printed as a dash; no sex printed"),
    (261, 6, "M", "",                      "", "",   "Badger", "", "", "See Gen. I, 104", "name printed as a dash"),
]

PERSONS = sorted(_P, key=lambda p: p[0])

# The plate prints these numbers on two different people each. Every place a
# number is SHOWN reads plate_number; every place one is KEYED reads id.
DUPLICATE_PLATE_NUMBERS = {256: "258", 257: "259"}

# What the plate prints where the transcription records something else.
PLATE_MISPRINTS = {
    "sex":  {37: "M."},
    "clan": {50: "Chapparral Cock", 255: "Bager"},
}

# (union_id, wife_id, husband_id, wife_order, husband_order, note)
UNIONS = [
    ("W01",   1,   2, 1, 1, ""),
    ("W02",   3,   4, 1, 1, ""),
    ("W03",   5,   6, 1, 1, ""),
    ("W04",   7,   8, 1, 1, "printed twice on the plate"),
    ("W05",  10,   9, 1, 1, ""),
    ("W06",  12,  11, 1, 1, "no issue recorded"),
    ("W07",  13,  11, 1, 2, "second wife of 11"),
    ("W08",  15,  14, 1, 1, ""),
    ("W09",  16,  14, 1, 2, "second wife of 14"),
    ("W10",  18,  17, 1, 1, ""),
    ("W11",  20,  19, 1, 1, ""),
    ("W12",  21,  19, 1, 2, "second wife of 19"),
    ("W13",  22,  23, 1, 1, ""),
    ("W14",  22,  24, 1, 1, "second husband of 22; no issue recorded"),
    ("W15",  25,  26, 1, 1, ""),
    ("W16",  28,  27, 1, 1, ""),
    ("W17",  29,  27, 1, 2, "second wife of 27"),
    ("W18",  31,  30, 1, 1, ""),
    ("W19",  33,  32, 1, 1, ""),
    ("W20",  35,  34, 1, 1, ""),
    ("W21",  37,  36, 1, 1, ""),
    ("W22",  38,  39, 1, 1, ""),
    ("W23",  40,  39, 1, 2, "second wife of 39"),
    ("W24",  41,  42, 1, 1, ""),
    ("W25",  43,  44, 1, 1, ""),
    ("W26",  43,  45, 2, 1, "second husband of 43"),
    ("W27",  46,  47, 1, 1, ""),
    ("W28",  50,  49, 1, 1, ""),
    ("W29",  51,  52, 1, 1, ""),
    ("W30",  57,  56, 1, 1, ""),
    ("W31",  58,  59, 1, 1, ""),
    ("W32",  60,  61, 1, 1, ""),
    ("W33",  62,  63, 1, 1, "no issue recorded"),
    ("W34",  64,  63, 1, 2, "second wife of 63"),
    ("W35",  66,  65, 1, 1, "no issue recorded"),
    ("W36",  66,  67, 2, 1, "second husband of 66; no issue recorded"),
    ("W37",  68,  69, 1, 1, ""),
    ("W38",  71,  70, 1, 1, ""),
    ("W39",  72,  73, 1, 1, ""),
    ("W40",  74,  75, 1, 1, ""),
    ("W41",  76,  77, 1, 1, "no issue recorded"),
    ("W42",  81,  80, 1, 1, "no issue recorded"),
    ("W43",  84,  83, 1, 1, ""),
    ("W44",  86,  85, 1, 1, ""),
    ("W45",  86,  87, 2, 1, "second husband of 86; no issue recorded"),
    ("W46",  89,  90, 1, 1, ""),
    ("W47",  92,  91, 1, 1, "printed twice on the plate"),
    ("W48",  95,  94, 1, 1, "no issue recorded"),
    ("W49",  99, 100, 1, 1, "no issue recorded"),
    ("W50", 102, 103, 1, 1, ""),
    ("W51", 113, 112, 1, 1, ""),
    ("W52", 115, 114, 1, 1, ""),
    ("W53", 116, 117, 1, 1, ""),
    ("W54", 125, 124, 1, 1, "printed twice on the plate"),
    ("W55", 153, 152, 1, 1, "printed twice on the plate"),
    ("W56", 155, 154, 1, 1, ""),
    ("W57", 161, 160, 1, 1, ""),
    ("W58", 162, 163, 1, 1, ""),
    ("W59", 166, 167, 1, 1, "both partners are printed twice on the plate"),
    ("W60", 178, 179, 1, 1, ""),
    ("W61", 182, 181, 1, 1, "no issue recorded"),
    ("W62", 190, 191, 1, 1, ""),
    ("W63", 230, 231, 1, 1, ""),
    ("W64", 232, 233, 1, 1, ""),
    ("W65", 234, 235, 1, 1, "no issue recorded"),
    ("W66", 236, 237, 1, 1, ""),
    ("W67", 239, 238, 1, 1, "no issue recorded"),
    ("W68", 240, 241, 1, 1, ""),
    ("W69", 244, 243, 1, 1, ""),
    ("W70", 247, 246, 1, 1, "no issue recorded"),
    ("W71", 249, 250, 1, 1, ""),
    ("W72", 256, 257, 1, 1, "the plate numbers these two 258 and 259"),
]

# (union_id, mother_id, father_id, [child ids])
_GROUPS = [
    ("W01",   1,   2, [3, 5]),
    ("W02",   3,   4, [7, 9, 11, 14, 17, 19]),
    ("W03",   5,   6, [22, 25]),
    ("W04",   7,   8, [27, 30, 32]),
    ("W05",  10,   9, [34, 36]),
    ("W07",  13,  11, [38, 41]),
    ("W08",  15,  14, [43, 46, 48]),
    ("W09",  16,  14, [49, 51, 53, 54, 55]),
    ("W10",  18,  17, [56, 58, 60, 62, 65]),
    ("W11",  20,  19, [68, 70, 72]),
    ("W12",  21,  19, [74, 76, 78, 79]),
    ("W13",  22,  23, [80, 82]),
    ("W15",  25,  26, [83]),
    ("W16",  28,  27, [85, 88, 89]),
    ("W17",  29,  27, [91, 93, 94, 96, 97]),
    ("W18",  31,  30, [92, 98, 99]),
    ("W19",  33,  32, [101, 102, 104]),
    ("W20",  35,  34, [105, 106, 107, 108]),
    ("W21",  37,  36, [109, 110, 111, 112]),
    ("W22",  38,  39, [114]),
    ("W23",  40,  39, [116, 118]),
    ("W24",  41,  42, list(range(119, 124))),
    ("W25",  43,  44, [124]),
    ("W26",  43,  45, [126]),
    ("W27",  46,  47, list(range(127, 135))),
    ("W28",  50,  49, [135, 136, 137, 138]),
    ("W29",  51,  52, [139, 140, 141]),
    ("W30",  57,  56, [142]),
    ("W31",  58,  59, [143, 144]),
    ("W32",  60,  61, [145]),
    ("W34",  64,  63, list(range(146, 152))),
    ("W37",  68,  69, [152, 154, 156, 157, 158, 159]),
    ("W38",  71,  70, [160]),
    ("W39",  72,  73, [162, 125, 164, 165, 166, 168, 169]),
    ("W40",  74,  75, list(range(170, 178))),
    ("W43",  84,  83, [178, 180, 181, 167, 183]),
    ("W44",  86,  85, list(range(184, 190))),
    ("W46",  89,  90, [190, 192, 193, 194, 195, 196, 197, 198, 199]),
    ("W47",  92,  91, [200, 201]),
    ("W50", 102, 103, [202, 203]),
    ("W51", 113, 112, [204]),
    ("W52", 115, 114, list(range(205, 212))),
    ("W53", 116, 117, [212, 213]),
    ("W54", 125, 124, list(range(214, 218))),
    ("W55", 153, 152, [218, 219]),
    ("W56", 155, 154, [220]),
    ("W57", 161, 160, [221]),
    ("W58", 162, 163, [222, 223]),
    ("W60", 178, 179, [224, 225, 226]),
    ("W62", 190, 191, [227, 228, 229]),
    ("W63", 230, 231, [232, 234, 236]),
    ("W64", 232, 233, [240, 242, 243, 245, 246]),
    ("W66", 236, 237, [238, 8]),
    ("W68", 240, 241, [248, 249, 251, 252, 253, 254]),
    ("W69", 244, 243, [153, 255, 256]),
    ("W71", 249, 250, [258, 259, 260]),
    ("W72", 256, 257, [261]),
]

CHILDREN = [(uid, m, f, c, "") for uid, m, f, cs in _GROUPS for c in cs]

PLATE_NOTES = [
    ("block 1, col. 3", "(Sister of 10)",
     "printed beneath 20's name"),
    ("block 1, col. 4", "For her descendants, see above",
     "printed opposite the second appearance of 92, in place of a sibling bracket"),
    ("block 1, col. 5", "For offspring, see above",
     "printed opposite the second appearance of 125"),
    ("block 2, col. 4", "For her descendants, see above",
     "printed opposite the second appearance of 153"),
    ("block 2, col. 3", "For her descendants, see above",
     "printed opposite the second appearance of 7"),
    ("block 1, col. 5", "For first husband and descendants, see Gen. II, 126, 158, 160",
     "printed under 155, set over two lines"),
    ("block 1, col. 5", "For third husband and descendant, see Gen. I, 8, 90",
     "printed under 155, set over two lines"),
]

CLANS = ["Corn", "Oak", "Parrot", "Lizard", "Water", "Sun", "Bear", "Badger",
         "Turkey", "Turquoise", "Eagle", "Chaparral Cock", "Antelope",
         "Locust", "White"]

ORTHOGRAPHY = [
    ("ʼ", "U+02BC", "modifier letter apostrophe", "glottal stop / raised apostrophe as printed"),
    ("˙", "U+02D9", "dot above", "raised dot: aspiration or length"),
    ("ă", "U+0103", "a with breve", ""),
    ("ĕ", "U+0115", "e with breve", ""),
    ("ĭ", "U+012D", "i with breve", ""),
    ("ŭ", "U+016D", "u with breve", "in 112 Kaaigŭrŭr, 198 Dyăiʼtsdyămŭr"),
    ("ô", "U+00F4", "o with circumflex", "in 154 Yaʼdôkyʼ"),
    ("ó", "U+00F3", "o with acute", "in 158 Góa˙ʼtyʼiăi"),
    ("ñ", "U+00F1", "n with tilde", "in Zuñi"),
    ("ᶦ", "U+1DA6", "superscript i", ""),
    ("ᵘ", "U+1D58", "superscript u", ""),
    ("ᵃ", "U+1D43", "superscript a", ""),
]

_FOLD = {
    "ʼ": "", "˙": "",
    "ă": "a", "Ă": "A", "ĕ": "e", "ĭ": "i", "ŭ": "u",
    "ä": "a", "ñ": "n", "ô": "o", "ó": "o", "ɪ": "i",
    "ᶦ": "i", "ᵘ": "u", "ᵃ": "a",
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
    if ids != list(range(1, 262)):
        problems.append("PERSONS ids are not exactly 1..261")

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
        dupes = sorted({k for k in kids if kids.count(k) > 1})
        problems.append(f"a person appears as a child more than once: {dupes}")

    uids = [u[0] for u in UNIONS]
    if len(uids) != len(set(uids)):
        problems.append("duplicate union ids")
    known = set(uids)
    for uid, *_ in CHILDREN:
        if uid and uid not in known:
            problems.append(f"CHILDREN references unknown union {uid}")

    spouses = {i for u in UNIONS for i in (u[1], u[2]) if i}
    unplaced = set(ids) - set(kids) - spouses
    if unplaced:
        problems.append(f"persons neither child nor spouse: {sorted(unplaced)}")

    # child entries + spouse-only entries must equal the number of persons
    spouse_only = spouses - set(kids)
    if len(kids) + len(spouse_only) != len(PERSONS):
        problems.append(
            f"arithmetic: {len(kids)} children + {len(spouse_only)} spouse-only "
            f"!= {len(PERSONS)} persons"
        )

    for pid in DUPLICATE_PLATE_NUMBERS:
        if pid not in clan:
            problems.append(f"DUPLICATE_PLATE_NUMBERS names unknown id {pid}")

    return problems


if __name__ == "__main__":
    issues = self_check()
    print(f"{len(PERSONS)} persons, {len(UNIONS)} unions, {len(CHILDREN)} child links")
    print(f"ORTHOGRAPHY_VERIFIED = {ORTHOGRAPHY_VERIFIED}")
    if issues:
        print("PROBLEMS:")
        for i in issues:
            print("  -", i)
    else:
        print("all structural checks pass")
