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
