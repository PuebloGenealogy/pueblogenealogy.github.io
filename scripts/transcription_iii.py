"""
Verbatim transcription of Table 3, "Genealogy III", from
Elsie Clews Parsons, "Laguna Genealogies",
Anthropological Papers of the American Museum of Natural History, vol. 19, pt. 5
(1923), pp. 133-292.

Source image: sources/parsons-1923-table-3.jpg (3770 x 5503 px)
sha256 38d86b7a7b57ad24e4a25c0e22be0c36b866d38f18988aa960322e320420a200

Read tile by tile at native resolution. This file is the immutable 1923
baseline. Do NOT add research data here -- see the README's privacy boundary.

*** THIS MODULE IS FINISHED, REGISTERED IN make_chart.py's TABLES, AND LIVE. ***
Genealogy III was published 2026-07-31. Structure, orthography and the
cross-reference audit are all closed. ONE reading is still open and it is a
glyph, not a placement: the turned-comma mark at 154, 156, 157, 228 and 242.
See "ORTHOGRAPHY" at the foot of this docstring.

ORTHOGRAPHY_VERIFIED is True as of 2026-07-31: the STRUCTURE is read and
checked, and the NAMES are verified at 5x for **all 261 ids**.

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
              230 + 231, where 7's line reads "For her descendants, see above"
     91 + 92  issue drawn under 27 + 29; 92 recurs as a child of 30 + 31,
              "For her descendants, see above"
     124 +125 issue drawn under 43; 125 recurs as a child of 72 + 73,
              "For offspring, see above"
     152 +153 issue drawn under 68 + 69; 153 recurs as a child of 243 + 244,
              "For her descendants, see above"

   166 and 167 are each printed twice as well, but with no descendants line.
   PERSON 8 IS WHAT JOINS THE PLATE'S TWO BLOCKS: he is the husband of 7 in
   block 1 and a son of 230 + 231 in block 2.

   HE WAS READ AS A SON OF 236 + 237 UNTIL 2026-08-17, and so was 238. The
   plate hangs one vertical off 230's line and five stubs enter it -- 232,
   234, 236, 238 and 8, skipping 239, who is a spouse. 238 and 8 are set in
   the same column as 232, 234 and 236, where children of 236 + 237 would be
   indented one column further in, as 240 is; and 236's line carries no
   leader to a bracket of her own. Nothing structural could see the error:
   230, 236, 238 and 8 are all Parrot, so clan descent cannot discriminate,
   and the counts close either way. It was found by the plate audit reporting
   five stubs against three children and settled by the user reading the
   scan. 236 + 237 have no recorded issue.

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

WHAT REGISTRATION SHOWED (2026-07-31; this is now the published state)
------------------------------------------------------------------
Registered in TABLES as roots [1, 230] with root_columns {230: 2}, this plate
builds and draws all 261 people, and column drift measures 0 px within each
block at a 425.59 px step. It did NOT on the first attempt: fifteen people --
40, 64, 67, 87, 116-118, 146-151, 212-213 -- reached the page from nothing,
which is what the four drawn_under values on W23, W34, W36 and W45 fix. Those
four are PLATE READINGS, taken from the scan at the generation-4 and -5
columns, and they have not been checked by a second reader.

subset_font.py reports this plate needs exactly two characters the subset does
not already carry: `ó` and `ô`. Run it BEFORE the build that registers the
plate, never after -- see CLAUDE.md.

TWO BRACKET READINGS, BOTH NOW SETTLED BY THE USER ON THE SCAN
--------------------------------------------------------------------
Both are recorded in plate_note on the people concerned.

i.  SETTLED BY THE USER, 2026-07-31. 43's two husbands, and the reading below
    is the one that stands: 43 + 44 -> 124 and 43 + 45 -> 126, encoded as
    unions W25 and W26. This is the case LEADER_ON_SPOUSE_ROW exists for --
    45's leader sits on his own line, not 43's, so without it the renderer
    gave both unions mother_row 0 and stranded the first group.
    One unbroken vertical at native x 2267 runs
    from y 2157 to y 2222 with stubs to 124 and 126, and TWO leaders enter it:
    43's own line at 124's row and 45's line at 126's row. Encoded per the
    convention in (1) as 43 + 44 -> 124 and 43 + 45 -> 126. The alternative
    reading is a single undivided bracket of 43's two children with the father
    unstated.
ii. SETTLED BY THE USER, 2026-07-31, AND IT IS A MISPRINT. 22 and 25. One
    unbroken, unoffset vertical at native x 1749 from y 4339 to y 4425, stubs to
    80, 82 and 83, leaders entering at 80's row (22) and 83's row (25). All
    three children are Corn, so clan descent cannot separate them.

    The user read the plate and ruled: 80 and 82 are 22's, 83 is 25's, and THE
    VERTICAL IS DRAWN FURTHER THAN IT SHOULD BE. 22's bracket ought to terminate
    after 82; the plate carries it on down to 83, which belongs to 25's leader.
    So the continuous rule is a printing error, not evidence of one group.
    Encoded as 22 -> 80, 82 and 25 -> 83, which is what this file already held.

    NOTE WHAT THE CHART THEREFORE DOES: it draws TWO brackets where the plate
    draws one continuous vertical. That is the one place on this plate where the
    drawn structure departs from the scan, and it rests on the user's reading.
    It is not a candidate for PLATE_MISPRINTS, which carries printed TEXT the
    data contradicts (a sex letter, a clan spelling); this is a rule, and
    make_chart.py does not read that table anyway.

    For contrast, 86's and 89's brackets at native x 2853 ARE visibly offset
    where they meet, and the 77-79 bracket's vertical sits visibly left of this
    one. So the plate does distinguish adjacent brackets when it means to --
    which is what makes (i) worth checking and what makes (ii) an error.

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

THE SECOND SORT IS REAL, AND ALL FIVE INSTANCES ARE NOW SETTLED. 2026-08-08.
At 154, 156, 157, 228 and 242 a mark reads as a reversed comma rather than the
U+02BC used everywhere else. The plate scan could not resolve it -- see the
closed record below -- but the user PHOTOGRAPHED the lines and the photographs
decide it. ALL FIVE now carry U+02BD, MODIFIER LETTER REVERSED COMMA:

  154  Yaʼdôkyʽ        156  Pʽĕʼnitsʼaʼyo      157  Dziotyʽ
  228  Awieʽ           242  Shipʼaʼpʽ

Note the earlier description of 156 was WRONG about position: its odd mark is
the FIRST one, after the P, not a final one. Its other three marks are ordinary
U+02BC. Everywhere else the odd mark IS the final one.

HOW IT WAS DECIDED, so a later session need not re-derive it. Each mark was
flood-filled at NATIVE resolution -- no upscaling enters the measurement, which
is what invalidated the earlier attempt -- and reduced to three numbers: the
mark's height in rows, the horizontal centroid of its bottom third minus that of
its top third, and its ink mass top third / bottom third. Heights are only
comparable WITHIN one photograph; the drift and the mass are not.

  first photograph, lines 156-159
  156 after P   50 rows   drift +3.0 px RIGHT   ink 339 / 212   questioned
  157 final     54 rows   drift +5.6 px RIGHT   ink 433 / 317   questioned
  156 after e   77 rows   drift -21.3 px LEFT   ink 512 / 220   known U+02BC
  156 after s   70 rows   drift -7.9 px LEFT    ink 582 / 195   known U+02BC
  156 after a   78 rows   drift -21.5 px LEFT   ink 564 / 291   known U+02BC
  159 in witsʼa 69 rows   drift -9.0 px LEFT    ink 523 / 179   the control

  IMG_3041, lines 154-159 -- carries 154 AND replicates 156 and 157
  154 final     28 rows   drift +3.7 px RIGHT   ink 116 /  70   questioned
  154 after Ya  37 rows   drift -8.4 px LEFT    ink 131 / 103   known U+02BC
  156 after P   23 rows   drift +2.4 px RIGHT   ink  64 /  38   replication
  157 final     24 rows   drift +3.2 px RIGHT   ink  90 /  65   replication
  156 after s   31 rows   drift -3.2 px LEFT    ink 124 /  50   known U+02BC
  159 in witsʼa 31 rows   drift -4.1 px LEFT    ink 120 /  51   the control

  IMG_3039, lines 242-244 -- 242 carries BOTH sorts in one word
  242 final     49 rows   drift +4.5 px RIGHT   ink 368 / 303   questioned
  242 after Ship 66 rows  drift -8.0 px LEFT    ink 547 / 267   known U+02BC
  242 after a   70 rows   drift -21.0 px LEFT   ink 477 / 334   known U+02BC

  IMG_3038, lines 227-229 -- 228, and NO control in frame
  228 final     58 rows   drift +6.0 px RIGHT   ink 545 / 411   questioned

228 IS THE ONE WITH A CAVEAT, and it does not change the answer. Neither 227 nor
229 contains an apostrophe, so nothing in its frame is a control. The two
discriminators that decide it are scale-free and both place it with the
questioned group: the tail sweeps RIGHT, and it is TOP-HEAVY, so the mark is a
mirror rather than a rotation. Its height normalised against the period in its
own photograph is 1.45, inside the questioned band rather than the control band
-- but that normalisation is not tight across photographs, so treat it as
corroboration and not as proof.

TWO THINGS THE SECOND ROUND ADDED. 156 and 157 REPLICATE from an independent
photograph at roughly half the pixel scale, so the method is not living at the
edge of the resolution. And the failure mode is worth naming: the first crop box
for 159 in IMG_3041 caught the `s` of `wits` and read +8.9 px RIGHT. That was a
bad box, not a finding. The flood fill will measure whatever blob it is given --
LOOK AT THE CROP before believing a number.

Three findings, and the third is what makes it certain rather than probable:

  1. Every known U+02BC sweeps its tail down-LEFT; both questioned marks sweep
     down-RIGHT. No exceptions either way.
  2. BOTH sorts are top-heavy, so the questioned mark is not the apostrophe
     rotated 180 degrees -- it is the apostrophe MIRRORED. That is what picks
     U+02BD over U+02BB: U+02BB and U+2018 are bulb-at-BOTTOM (measured off the
     Times outlines as mass 1488 top / 4863 bottom), which top-heaviness rules
     out.
  3. The questioned sort is physically SMALLER -- 50 and 54 rows against 69-78.
     A different piece of type, not the same sort worn or over-inked.

And the cleanest evidence needs no control from another line at all: 156
contains BOTH sorts inside one word, mark 1 against marks 2-4.

The positions also read as Boas-school notation, which corroborates without
being evidence on its own: `Pʽ` is an aspirated stop, `Dziotyʽ` a word-final
aspirated stop, and the U+02BC marks are glottalisation.

CLOSED RECORD -- why the SCAN cannot do this, kept so nobody re-crops it.
The 20x test was run 2026-07-31 on 157 against 159, native crops at x 2452/2524,
y 3460/3509. A mark on the scan is about TEN PIXELS of ink; at 20x the
questioned mark and the known U+02BC are the same amorphous blob, and the
difference that looks convincing at 6x-8x is the upscaler inventing an edge.
That remains true. sources/parsons-1923-table-3.jpg is 3770 x 5503, a ninth of
Table 1's pixel count. DO NOT RE-CROP IT -- what settled this was a new
photograph, not a bigger magnification of the old one.

NOTHING IS OPEN. All five are photographed and measured. Do not re-open this on
the strength of a crop of the scan.

CROSS-REFERENCES -- AUDITED 2026-07-31
--------------------------------------
All 51 person-level references plus the two prose references under 155 were
matched against transcription.py and transcription_ii.py by NAME, SEX and
CLAN, in the way transcription_ii.py's CROSS_REF_OFFSET block was built.
NOTHING BELOW IS CORRECTED IN THE DATA. cross_ref carries what the plate
prints; the finding lives in the plate_note beside it.

THE HEADLINE IS A NEGATIVE RESULT, AND IT MATTERS.
transcription_ii.py records that Genealogy II's references into Genealogy I
run exact through person 53 and ONE HIGH from person 66 onward. THIS PLATE
DOES NOT SHARE THAT DISPLACEMENT. Its references into Genealogy I are exact
right across the displaced range -- 78, 79, 97, 98, 99, 100, 101, 103, 104 all
name the person Genealogy I finally printed under that number, matched by name
where there is one and by sex and clan where the name is a dash. So Genealogy
III was numbered against the FINAL Genealogy I and Genealogy II was not. Do not
carry Genealogy II's offset over to this plate.

FOUR EXCEPTIONS, and no two are the same kind of error:

a. 170-174: the Gen. II half of five consecutive references is TEN LOW. The
   Gen. I half of those lines is exact EXCEPT 173's, which is (c) below --
   an earlier wording of this paragraph said the Gen. I half was exact
   throughout, and that contradicted (c). Corrected 2026-07-31.
   plate prints Gen. II 191, 192, 193, 194, 195; the people it names are
   Genealogy II's 201-205 (Dziwaiʼi˙siro, Kuyăiʼd˙yid˙uweʼ, Edna,
   Yăaiʼdyid˙yuwi, Owi˙ʼd˙zĭraiʼ -- all Sun, in that order, an exact
   five-for-five match). The Gen. I half of the same lines is exact. RE-READ ON
   THE SCAN at x 2330, y 3890: the plate really does print 191-195. Note what
   makes this findable at all -- Gen. II 191-195 are a group of Oak people whom
   this plate ALSO cites correctly, from its own 194, 195 and 198.

b. 218: "See Gen. I, 101" is ONE LOW. 101 is the father, "--- of Zuñi", already
   cited from 257. The person is Genealogy I's 102. Her sisters 219 and 261
   cite 103 and 104 exactly, so this is an isolated slip, not a run.

c. 173: "See Gen. I, 149" cannot resolve -- Genealogy I has 104 people -- and
   was re-read at 5x, so 149 is what the plate prints. The person is Genealogy
   I's 49, which is how Genealogy II's own 204 cites her.

d. The prose note under 155, "For third husband and descendant, see Gen. I,
   8, 90": the husband is exact, the descendant is ONE HIGH. Genealogy I's
   73+8 have one child, 89. This is the ONLY place on this plate where Genealogy
   II's +1 displacement appears, and it is a third-plate attestation of it.

VERIFIED CLEAN: the other prose note under 155, "For first husband and
descendants, see Gen. II, 126, 158, 160" -- all three resolve, 160 being 155
herself.

WHERE THE PLATES SPELL A NAME DIFFERENTLY, THIS FILE KEEPS THIS PLATE'S
SPELLING, as the rule requires. Seven references land on the right person under
a spelling the other plate does not share -- and one of the seven is this
repo's doing, not Parsons's:

   75  Kʼuʼna˙shᵘ        Gen. II 170  Kʼuʼn˙ash˘
  101  Dziŏ˙kwid˙yuʼă    Gen. II 124  Dzĭo˙kwid˙yuʼă
  102  Gowak˙ʼad˙yăi     Gen. II 125  Gowaʼk˙ʼd˙yăiʼ
  162  Minni             Gen. II  27  Mini
  171  Kuyăiʼd˙yid˙uwĕʼ  Gen. I   48  Kuyăiʼd˙yid˙yuweʼ
  223  Ha˙tsʼe           Gen. II  84  Ha˙tsʼᵉ
  191  Ramona            Gen. II 187  "Ramona of Sant Ana"  <- NOT a plate
        divergence: both plates print the same thing, and this file stores
        "of Sant Ana" in the origin field where transcription_ii.py keeps it
        in the name. Do not "reconcile" the two by editing either name.

Every other divergent-looking pair folds to the same key and is not a
divergence at all -- 152, 153, 192, 194, 255 among them.

SETTLED 2026-07-31 (the user's call): (a)-(d) DO get a footnote on the published
page, as Genealogy II's displacement did. It is a single `#note-crossref` entry
in the apparatus, in this table's TABLES["iii"]["notes"] -- the negative result
first, then the four exceptions and the person each reference actually reaches.
Nothing on the chart changes and no reference is corrected in the data.
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
    (8,   3, "M", "Dzaaiʼy˙unăiʼ",         "", "",   "Parrot",         "",        "Acoma",      "", "printed twice; a son of 230+231 in block 2 and the husband of 7 in block 1"),
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
    (22,  3, "F", "Dzaiaaiʼdʼyuwitsʼă",    "", "",   "Corn",           "d.",      "",           "", "her bracket runs 80, 82; the plate draws its vertical on past 82 to 83, which is 25's child. Over-drawn rule, confirmed 2026-07-31"),
    (23,  3, "M", "",                      "", "",   "Sun",            "",        "",           "", "name printed as a dash"),
    (24,  3, "M", "Ai˙ʼtyʼiai",            "", "",   "Turkey",         "",        "",           "", "second husband of 22; no issue recorded"),
    (25,  3, "F", "Wayaiduitsa",           "", "",   "Corn",           "",        "",           "", "83 is hers; her leader enters at his row. The plate runs 22's vertical down past 82 to reach him. Over-drawn rule, confirmed 2026-07-31"),
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
    (154, 5, "M", "Yaʼdôkyʽ",              "", "",   "Lizard",         "d.",      "", "", ""),
    (155, 5, "",  "Yoʼsiro",               "", "",   "Chaparral Cock", "d. 1914", "",
     "For first husband and descendants, see Gen. | II, 126, 158, 160 | For third husband and descendant, see Gen. | I, 8, 90",
     "no sex printed; the cross-reference is set over four lines, split here at the plate's own breaks"),
    (156, 5, "M", "Pʽĕʼnitsʼaʼyo",         "", "",   "Lizard",         "",        "", "", ""),
    (157, 5, "M", "Dziotyʽ",               "", "",   "Lizard",         "",        "", "", ""),
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
    # 170-174: the Gen. II half of these five references is TEN LOW. Audited
    # 2026-07-31 and re-read on the scan at x 2330, y 3890 -- the plate really
    # does print 191-195, and the people it names are Genealogy II's 201-205.
    # See "CROSS-REFERENCES" in the docstring. Recorded as printed.
    (170, 5, "M", "Dziwaiʼisiro",          "", "",   "Sun",            "",        "", "See Gen. I, 45; Gen. II, 191",
     "the Gen. I reference is exact; the Gen. II reference names Gen. II's 201, Dziwaiʼi˙siro, M, Sun -- ten higher than the 191 printed"),
    (171, 5, "F", "Kuyăiʼd˙yid˙uwĕʼ",      "", "",   "Sun",            "",        "", "See Gen. I, 48; Gen. II, 192",
     "the Gen. I reference is exact; the Gen. II reference names Gen. II's 202, Kuyăiʼd˙yid˙uweʼ, F, Sun -- ten higher than the 192 printed"),
    (172, 5, "F", "Edna",                  "", "",   "Sun",            "",        "", "See Gen. II, 193",
     "the reference names Gen. II's 203, Edna, F, Sun -- ten higher than the 193 printed"),
    (173, 5, "F", "Yăaiʼdyid˙yuwi",        "", "",   "Sun",            "",        "", "See Gen. I, 149; Gen. II, 194",
     "BOTH references are wrong, in different ways. 'Gen. I, 149' cannot resolve -- Genealogy I has 104 people -- and was re-read at 5x, so 149 is what the plate prints; the person named is Genealogy I's 49, Yăaiʼdyid˙yuwi, F, Sun, age 7, which is how Genealogy II's own 204 cites her. The Gen. II reference names Gen. II's 204 -- ten higher than the 194 printed"),
    (174, 5, "M", "Owi˙ʼd˙zĭraiʼ",         "", "",   "Sun",            "",        "", "See Gen. I, 47; Gen. II, 195",
     "the Gen. I reference is exact; the Gen. II reference names Gen. II's 205, Owi˙ʼd˙zĭraiʼ, M, Sun -- ten higher than the 195 printed"),
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
    (218, 6, "F", "",                      "", "",   "Badger",         "", "", "See Gen. I, 101",
     "name printed as a dash. The reference is ONE LOW: Genealogy I's 101 is the father, '--- of Zuñi', M, no clan, and this plate already cites him at 257. The person here is Genealogy I's 102, F, Badger, age 5 -- her sisters 219 and 261 cite 103 and 104 exactly. Recorded as printed"),
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
    (228, 7, "M", "Awieʽ",                 "", "4",  "Oak", "", "", "", ""),
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
    (238, 3, "M", "Ha˙d˙ăiʼyănyi",         "", "",   "Parrot", "", "", "", ""),
    (239, 3, "F", "",                      "", "",   "Water",  "", "", "", "name printed as a dash; no issue recorded"),
    (240, 4, "F", "Yo˙nimaitsʼă",          "", "48", "Parrot", "", "", "", ""),
    (241, 4, "M", "Tsaauʼs˙diyai", "Jefferson", "51", "Turkey", "", "", "", "English name printed in parentheses on the plate"),
    (242, 4, "M", "Shipʼaʼpʽ",             "", "",   "Parrot", "", "", "", "a full point is printed after the clan"),
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

# What the plate prints where the transcription records something else. The
# PLATE's value is what the page shows -- ringed in --sic with an annotation
# row, exactly as Genealogy I's misprinted number 68 is -- while the data below
# keeps the reading the plate's own bracket and clan descent establish, because
# that is what the structure is computed from. Read by make_chart.py.
PLATE_MISPRINTS = {
    "sex":  {37: "M."},
    "clan": {50: "Chapparral Cock", 255: "Bager"},
}

# Unions whose sibling bracket the plate hangs off the '+' SPOUSE's line rather
# than off the mother's. This plate draws the leader from the line of the parent
# whose marriage the group belongs to (docstring, point 1), so a woman's second
# husband carries his own leader; every other plate in the edition hangs every
# bracket on the mother's row and declares none of these.
#
# W26 is the only one on this plate: 43 has two husbands and issue by both, and
# the plate puts 124's leader on her line and 126's on 45's. Without this entry
# both groups claim row 0, the second cannot start there, and make_chart.py's
# push logic moves 43's own line down five rows to meet it -- stranding 124's
# bracket on 15's line, so the page says 124 is 14+15's child. Found 2026-07-31
# on the first full preview; the same failure CLAUDE.md records for Gen. II's
# 169, which was sidestepped there because Parsons prints her twice.
LEADER_ON_SPOUSE_ROW = {"W26"}

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
    ("W23",  40,  39, 1, 2, "second wife of 39. The plate prints '+ 40.' inside 38's "
     "block, below 38's own bracket; neither partner is a block primary anywhere, so "
     "without drawn_under 40 and her children 116, 118 are never drawn", 38),
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
    ("W34",  64,  63, 1, 2, "second wife of 63. The plate prints 62, '+ 63.', '+ 64.' "
     "as three consecutive lines, so this marriage is drawn inside 62's block", 62),
    ("W35",  66,  65, 1, 1, "no issue recorded"),
    ("W36",  66,  67, 2, 1, "second husband of 66; no issue recorded. The plate prints "
     "65, '+ 66.', '+ 67.' as three consecutive lines, so this marriage is drawn "
     "inside 65's block", 65),
    ("W37",  68,  69, 1, 1, ""),
    ("W38",  71,  70, 1, 1, ""),
    ("W39",  72,  73, 1, 1, ""),
    ("W40",  74,  75, 1, 1, ""),
    ("W41",  76,  77, 1, 1, "no issue recorded"),
    ("W42",  81,  80, 1, 1, "no issue recorded"),
    ("W43",  84,  83, 1, 1, ""),
    ("W44",  86,  85, 1, 1, ""),
    ("W45",  86,  87, 2, 1, "second husband of 86; no issue recorded. The plate prints "
     "85, '+ 86.', '+ 87.' as three consecutive lines, so this marriage is drawn "
     "inside 85's block", 85),
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
    ("W66", 236, 237, 1, 1, "no issue recorded"),
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
    ("W63", 230, 231, [232, 234, 236, 238, 8]),
    ("W64", 232, 233, [240, 242, 243, 245, 246]),
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
     "printed under 155, set over two lines. AUDITED 2026-07-31 and exact: "
     "Genealogy II's 160 is 155 herself (Yo˙ʼs˙iro, F, Chaparral Cock, d. 1914), "
     "her union U38 there is with 158 (Niʼʼy˙ŭyăiʼ, M, Parrot) and its child is "
     "126 (Yo˙ʼkwi, M, Chaparral Cock). All three numbers resolve"),
    ("block 1, col. 5", "For third husband and descendant, see Gen. I, 8, 90",
     "printed under 155, set over two lines. AUDITED 2026-07-31: the husband is "
     "exact -- Genealogy I's 8 is Yu˙si, M, Water -- but the DESCENDANT IS ONE "
     "HIGH. Genealogy I's union U22 is 73 (Yo˙ʼs˙iro, i.e. 155) + 8, and its only "
     "child is 89, a girl the plate leaves unnamed and unclanned. Genealogy I's "
     "90 is Heʼsa (Hazel), F, Badger, a child of 76+67 and no relation. This is "
     "the SAME +1 displacement transcription_ii.py records as CROSS_REF_OFFSET, "
     "and it is the only place on this plate where it appears. Recorded as printed"),
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
    ("ô", "U+00F4", "o with circumflex", "in 154 Yaʼdôkyʽ"),
    ("ó", "U+00F3", "o with acute", "in 158 Góa˙ʼtyʼiăi"),
    ("ñ", "U+00F1", "n with tilde", "in Zuñi"),
    ("ᶦ", "U+1DA6", "superscript i", ""),
    ("ᵘ", "U+1D58", "superscript u", ""),
    ("ᵃ", "U+1D43", "superscript a", ""),
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

    for field, entries in PLATE_MISPRINTS.items():
        if field not in ("sex", "clan"):
            problems.append(f"PLATE_MISPRINTS field {field!r} is not one the "
                            "renderer knows how to ring")
        for pid, printed in entries.items():
            if pid not in clan:
                problems.append(f"PLATE_MISPRINTS names unknown id {pid}")
            elif str(printed).strip().rstrip(".") == str(
                    dict(sex={p[0]: p[2] for p in PERSONS},
                         clan=clan).get(field, {}).get(pid, "")).strip():
                # An entry that agrees with the data rings a value for no
                # reason and points the reader at a note about nothing.
                problems.append(f"PLATE_MISPRINTS {field} {pid} repeats the "
                                "transcribed value; it records a DIFFERENCE")

    # A bracket can only hang off a spouse's line if there is a spouse line to
    # hang it on and children to bracket. The one that matters is not checkable
    # here -- whether the plate really draws that leader from his row -- so this
    # guards the mechanics and the docstring carries the reading.
    by_uid = {u[0]: u for u in UNIONS}
    with_issue = {c[0] for c in CHILDREN if c[0]}
    for uid in LEADER_ON_SPOUSE_ROW:
        u = by_uid.get(uid)
        if not u:
            problems.append(f"LEADER_ON_SPOUSE_ROW names unknown union {uid}")
        elif not (u[1] and u[2]):
            problems.append(f"LEADER_ON_SPOUSE_ROW {uid} has no '+' spouse line")
        elif uid not in with_issue:
            problems.append(f"LEADER_ON_SPOUSE_ROW {uid} brackets no children")

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
