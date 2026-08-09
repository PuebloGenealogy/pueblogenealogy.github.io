# Editorial method

How the plates in this edition were read, encoded and verified — so that any
reading can be checked, and so that later tables are made the same way as the
first.

The governing principle: **this edition reproduces the plate, it does not
improve it.** Where Parsons printed an error, the error is reproduced and
annotated. A reader who compares this edition against the scan should find no
silent differences.

Where she recorded nothing, nothing is supplied **in the chart**. The chart is
the transcription and carries only what the plate carries. The apparatus
alongside it may go further — see *Editorial attribution* below — but only
where the addition is marked on the page, explained in a footnote, and absent
from the chart. The word that matters in the principle is *silent*.

## The source

Table 1 was transcribed from a 16172 × 11798 px scan of the foldout plate,
kept in `sources/` so every reading can be checked against it. The scan is part
of the edition, not a working file: an edition that cannot be audited against
its source is an assertion rather than a transcription.

## Reading

The plate was read by eye from tiles cropped at native resolution — about 45 of
them for Table 1 — not by OCR.

This is a deliberate choice, not a limitation. OCR fails twice on this material.
It drops or mangles the Americanist phonetic diacritics, which are the whole
point of a phonetic transcription; and it discards the bracket geometry, which
is where the genealogical relationships actually live. A perfect character
recognition of this plate would still lose the genealogy.

Six glyphs in Table 1 were ambiguous at first pass and were resolved by cropping
tighter and looking again — among them #25 `Kaaiʼdziăi˙s˙iwă`, where what looks
like a diaeresis is a plain `i` followed by a raised dot (U+02D9).

## Orthography

Characters are stored as the specific Unicode codepoints Parsons's typography
calls for, listed in `ORTHOGRAPHY` in `scripts/transcription.py`: U+02BC for the
raised apostrophe, U+02D9 for the raised dot, the breve vowels, and the
superscript letters from Unicode's Phonetic Extensions.

Those last three — `ᶦ ᵘ ᵃ` — are absent from most serif faces, so the published
pages embed a subset of SIL Gentium. Without it the diacritics would render as
empty boxes on many systems, which would corrupt the transcription visually
while leaving the data intact.

A parallel ASCII folding (`fold()`) strips the diacritics for matching against
census spellings. It is a search key, never a reading.

## Encoding

The plate is a bracket diagram; the data is stored normalised, as three tables:

- **PERSONS** — one row per numbered individual, with the name exactly as
  printed, plus age, clan, vital note, origin and any cross-reference
- **UNIONS** — one row per marriage
- **CHILDREN** — one row per parent–child link

This separation is what allows the same data to be rendered as a chart, exported
as a spreadsheet, and checked mechanically. The plate's own numbering is
preserved throughout; nothing is renumbered.

Conventions:

- A dash where a name should be means Parsons recorded no name — stored as an
  empty value, not as a dash
- `d.` means the person had already died when Parsons recorded the genealogy,
  during her fieldwork of 1918–19. It bounds the death rather than leaving it
  open: `d.` alone means she did not record the year, `d. 1913` that she did
- A parenthesised English name, such as "Hazel" at 90, is plate data and is
  stored as an alternate name
- A person appearing twice on the plate is stored once; the repetition becomes a
  cross-reference, as the plate itself does
- Where paternity is not assignable, the sibling group hangs off the mother's
  line alone, with no father recorded. That is what the transcription stores
  and what the chart draws; where the apparatus goes further, see below

## Editorial attribution

The transcription records what the plate shows. Twice, so far, the plate leaves a
question open that evidence outside it can answer, and this edition answers it —
in the apparatus only, never in the chart.

Both cases have the same shape: a woman with two husbands on the plate, one
bracket, and no statement of which marriage the children belong to. The
transcription therefore records no father in either, and **the chart draws the
single bracket the plate draws**.

- **83–85 on Table 1.** Person 68 has two husbands, 69 and 70. In the register
  and the person cards the edition attributes 83 and 84 to her marriage with 69,
  and 85 to her marriage with 70.
- **116–118 on Table 2.** Person 48 has two husbands, 47 and 49. The edition
  attributes all three children to her marriage with 49.

**The two rest on different kinds of evidence, and the difference is the point
of rule 4 below.** Table 1's is external documentary research, which this
edition does not publish. Table 2's is Parsons's own text: at p. 195, writing on
inheritance, she records that in one instance noted — "Gen. II, 47" — the sheep
and fields passed to his widow for want of offspring. That names this man, on
this genealogy, as having died childless, so 116–118 are not his and 49 is the
only other husband the plate gives 48. The footnote quotes and cites her, and a
reader can weigh it without taking the edition's word for anything.

Table 2's attribution was **deliberately not made** when the plate was first
published, on 2026-07-30, because no source for it had been found in Parsons's
text and rule 3 requires a footnote that can say what the reading rests on. The
general rule that produced that decision still stands — *an attribution that
cannot be footnoted is not made* — and it was satisfied, not waived, when the
passage was found.

Four rules govern all of this, and a future attribution must meet all four:

1. **The chart never carries it.** The chart is the transcription. An
   attribution that changed a bracket would make the page disagree with the
   scan, which is the one thing the edition exists not to do.
2. **It is declared as data, outside the transcription module.** The map lives
   in `make_chart.py`'s `TABLES` entry, beside the table's other editorial
   material. `scripts/transcription*.py` holds the plate and only the plate.
3. **Every row it produces is marked** with a dagger linking to a footnote that
   says the attribution is editorial and that the plate does not state it.
   Plate-attested groups sit unmarked beside marked ones, so the difference is
   visible rather than asserted. The mark appears at **both ends** — on the
   parents' `Children` rows and on each child's own `Parents` row — because an
   attribution visible from one side only is one a reader can miss entirely by
   arriving from the other.

   **The dagger marks the pairing, not the mother.** She is the plate's own
   bracket and is never in doubt; what the edition supplies is which marriage
   the children belong to. Each footnote says so, so `Parents†` cannot be read
   as doubt about the mother. It sits on the row rather than on the father's
   chip for that reason and one mechanical one: the person card's rows are
   anchors, an `<a>` dagger cannot nest inside the chip's `<a>`, and a bare
   `<span>` would leave the card with a mark that goes nowhere.
4. **A published source is cited; unpublished records are not reproduced.**
   Which of the two applies depends on where the evidence comes from, and the
   distinction is not negotiable in either direction.
   - Where the evidence is **already published** — Parsons's own 1923 text, or
     any other printed source — the footnote **quotes it and gives the page**,
     as Table 2's does. An attribution a reader can check is worth more than one
     they must accept.
   - Where the evidence is **external documentary research**, as Table 1's is,
     it falls under *What is published* below: it stays in the git-ignored
     workbook. The footnote says that a reading rests on evidence outside the
     plate, names no source, and stops there. The build refuses output that
     would go further.

   One practical consequence of quoting a printed source: the leak gate's prose
   check does not know the difference between Parsons's vocabulary and a
   researcher's, so a quotation may trip it. The fix is to allowlist the exact
   phrase in `RESEARCH_PROSE_ALLOWED`, never to loosen the pattern — the gate
   must keep failing closed on every other use of the word.

## Identity across plates

The four plates are four independent numberings. A person drawn on more than one
of them therefore has more than one number, and nothing in a number says so —
Genealogy I's 73, Genealogy II's 160 and Genealogy III's 155 are one woman, and
only Parsons's cross-references say it.

**In the charts and the register, the edition carries exactly what she prints.**
A cross-reference row is transcribed where the plate sets one and nowhere else,
and no two entries are merged: the plate is four documents, and the edition
reproduces four documents. Nothing in this section changes that, and the rule
below does not apply to any chart page.

The **search** page is where identity has to be decided, because searching by
name across four plates means answering whether two entries are two records of
one person or two people. The four plates carry **713 entries** and **620
people**: 79 are drawn more than once. Parsons cross-references **65** of them
herself. The remaining **14** are set out below.

### The rule

**An entry is a plate entry, and only the plates may say that two of them are
one person.** Two entries are joined where a printed cross-reference resolves —
and a printed reference is confirmed against the entry it lands on by name, sex
and clan before it is followed, never trusted for its number, which is displaced
on three of the four plates. Where a reference will not resolve it is
**reported, not guessed**: three do not resolve today and each is named on the
page. Two entries from the same plate are two people. A shared name is not
evidence and never joins anything — see *Namesakes* below.

### The fourteen

Of these, **two are Parsons's own** and are listed here only because she states
them through a person's second husband rather than by name, so no automatic
match on names finds them:

| Entries | Evidence |
|---|---|
| I·12 = II·19 | I·12 prints *"For second husband and offspring see Gen. II, 21, 74"*; II·19 is the woman whose second husband is 21 |
| II·163 = III·16 | II·163 prints *"For second husband and descendants, see Gen. III, 14, 49-55, 135-141"*; III·16 is the woman married to 14 with exactly those children |

**The other twelve the plates do not print.** They are the edition's own, and
every one of them is a family joined as a family — never a lone name:

| Entries | Evidence |
|---|---|
| II·123 = IV·17 | father. Same name, clan, sex and age, and the same wife by name |
| II·122 = IV·18 | mother. Spelt `Dzaid˙yuwiʼ` on II and `Dzaidʼyuwiʼ` on IV; same clan, sex and age, and the same husband |
| II·147–151 = IV·54–58 | their five children. Same clan and sex throughout, same name, the same two parents by name on both plates, and the same age on three of the five |
| II·229 = III·227 | one of three siblings. Same name, clan, sex and age, and the same two parents by name |
| II·231 = III·229 | the second. Same name, clan, sex and age, and the same two parents by name |
| II·230 = III·228 | the third. Spelt `Awie˙` on II and `Awieʽ` on III; same clan, sex and age, and the same two parents by name |
| II·174 = III·52 | husband. Spelt `Shta˙ʼyăi` on II and `Shta˙ʼy˙ăi` on III; same sex, and the same wife |
| II·175 = III·51 | his wife. Spelt `Kio˙ʼd˙yiăi` on II and `Kio˙ʼtyʼiăi` on III; same clan and sex, and the same husband |

Eight rest on a name the two plates spell identically. **Four do not** — the
plates differ in their diacritics, and only the diacritic-free search key
matches. Those four are listed by hand for that reason: a rule keyed on the
printed name would have collapsed the five children while leaving their mother
standing as two women, which is the shape of error this whole section exists to
prevent.

### What governs them

The four rules of *Editorial attribution* above govern these too. Two of them
apply with no change and two need saying differently:

1. **The chart never carries it.** Unchanged, and stronger here: no chart page,
   register entry or person card is affected by any join. The identifications
   exist on the search page and in its index, and nowhere else in the edition.
2. **Declared as data, outside the transcription module.** Unchanged in
   substance, different in place: the map is `INFERRED_IDENTITIES` in the
   finding aid's `build.py`, one line per decision with its evidence beside it.
   It is a list and not a rule, so any single join can be withdrawn by deleting
   its line. `scripts/transcription*.py` still holds the plate and only the
   plate.
3. **Every row it produces is marked.** A join the plates do not print carries a
   ringed **NOT PRINTED** marker wherever it appears, and says it is identified
   by the edition rather than by Parsons. In the index it carries
   `"source": "inferred"` and **quotes nothing**, because there is nothing
   printed to quote; a printed join quotes the plate's own words. A regression
   test asserts both, so an inferred join cannot come to look like Parsons's.
4. **A published source is cited.** The evidence here is the plates themselves,
   which are published, so it is quoted in full above and on the page. **No
   identification in this edition rests on external documentary research**, and
   none may: the joins are made from names, clans, sexes, ages and relatives as
   printed, and census or civil records are not evidence a reader could check
   against the source this edition transcribes. That boundary is *What is
   published* below, and it is not weakened by the search page — the finding aid
   reads the published pages and nothing else, and runs the same leak gate over
   everything it writes.

### Namesakes: the joins deliberately not made

The search results sort by name, so two people who share one land next to each
other and read as a duplicate. Leaving that unexplained would be its own
assertion, so every such pair is adjudicated by hand and the finding is shown on
the row. There are three, and the verdicts are not interchangeable:

| Pair | Verdict | Finding |
|---|---|---|
| I·52 / III·250 | distinct | One is a boy of 4; the other has a wife and three children, in the same 1918–19 fieldwork |
| II·83 / II·144 | distinct | Two Lizard girls of one name **on one plate**, a generation apart, with different mothers. Parsons separates them herself: II·83 goes over to Genealogy III as 222, II·144 does not |
| II·182 / IV·69 | **open** | Nothing contradicts them, and no relative of either is drawn on the other plate. Name, sex and clan are the whole of the evidence, which is not enough |

**An open pair is shown as open.** It is not joined, and it is not given a
settled pair's calm — the two verdicts carry different marks in different
colours, at the row and at the note. Agreeing on a name, a sex and a clan is
precisely the inference this edition refuses; a pair where that is all there is
stays two entries and says why.

Seven further cross-plate name collisions exist — I·87/II·23, I·13 and I·96
against III·37, II·12/IV·68, II·73/III·166, I·41/II·209, I·57/IV·7 — and none is
adjudicated, because each disagrees on sex or on clan and so is never a namesake
under the rule. The reader sees the difference in the row itself.

## Verification

Four structural checks run on every build (`self_check()`), and the workbook will
not build unless they pass:

1. ids are exactly `1..N`, each appearing once
2. **every child's clan equals its mother's clan**
3. no person appears as a child more than once
4. no person is orphaned — everyone is someone's child or someone's spouse

The second is the important one. Laguna clan membership is matrilineal, so clan
is not merely another field to be copied: it is an independent signal about
structure. If a bracket is misread — a sibling group attached to the wrong
mother — the child's clan will contradict hers, and the check fails. All 27
unions in Table 1 pass it. That agreement between two independently transcribed
things is the main evidence that the structure is right.

A simple arithmetic check runs alongside: child entries plus spouse-only entries
must equal the number of persons. For Table 1, 80 + 24 = 104.

## Layout

The chart reproduces the plate's five-column grid rather than approximating it.
Every node contributes exactly one connector stub plus one fixed-width block, so
generation *d* lands at the same horizontal position on every path — which is
why 5 aligns with 65 and 13 with 80, as on the plate. Column drift measures 0 px
at every generation.

Sibling brackets hang off the **mother's** line, not the top of a block, and the
leader rules that fill each gap run from that same line. This was wrong in an
early draft and is the kind of error that looks like a styling detail while
actually asserting a different genealogy.

The dashed rule separating the two families is an editorial addition, marked as
such in the page footer. It is the only *visual* mark inside the plate's frame
that is not on the plate. The reading apparatus around the frame — the
generation ruler, the person-number links (each number is an anchor, `#p13`),
and the generated register below the chart — is 2026 editorial furniture, not
plate content, and the footer discloses it as such. The numbers themselves,
and every character of every line, remain exactly as printed.

## What is published

The published edition is **the transcription only**. Research annotations —
English names identified from other sources, census matches — stay in a
git-ignored workbook and never reach the website.

This is enforced structurally rather than by discipline. The public build reads
the transcription module, which has no research columns to read, so no code path
connects the two. As a backstop the build inspects its own output and deletes
any page that carries research, checking two different things:

- **Research markup** — the classes a rendered English name or census match
  would carry.
- **Research prose** — the vocabulary that research is written *in*. This is
  the way it would realistically escape: not a stray field, but a footnote
  explaining *why* a reading was made. Such a sentence carries no markup at
  all, and until 2026-07-28 nothing would have stopped it. The sweep now covers
  every page in `docs/`, not only the table pages, and fails closed: the
  handful of sentences that legitimately discuss the boundary are allowlisted
  by exact phrase, so rewording them stops the build until the new wording is
  allowlisted too.

The reason for the care: the repository is public, git history is permanent, and
some of the people who might be identified through this research have living
descendants.

## Provenance

This is Laguna Pueblo material, and Parsons's Laguna fieldwork is contested —
she published information members of the community regarded as restricted. This
edition transcribes an already published source and adds nothing to the public
record about the community. It is offered as a finding aid to the printed
document.

The 1923 publication is in the public domain in the United States. The
transcription, encoding and layout are released under CC BY 4.0. Corrections are
recorded as dated commits, so the edition carries its own revision history and
any reading can be traced to when and why it changed.
