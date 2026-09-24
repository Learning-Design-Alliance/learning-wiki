# Source inclusion criteria

What a source needs in order to be ingested into this wiki, and the few reasons one is turned away.
The rejection codes in `sources/manifest.ndjson` (`okf_lib.REJECTION_CODES`) point at the numbered
exclusions below, so a rejection always says which rule it applied.

**The default is to include.** Anyone designing learning, in any setting, may use this wiki, so the
question a source has to answer is "does this help someone understand or design learning?", not "is
this the kind of learning we usually cover".

## A source is included when it meets all three

**I1. It is about learning, or about designing for it.** Any setting: schools, universities,
workplaces, the health professions, the military, museums and other informal settings, families,
sport, clinical and therapeutic settings, communities, online. Any age, and any domain being learned.
Sources about **the design process** are in, and so are sources about the people and processes that
produce learning more broadly: design thinking, agile and iterative design, instructional design
models, design-based research, design methods, teachers, programme evaluation. This is confirmed by
the maintainer.

**I2. It offers something that can be extracted.** That can be a finding, a reasoned argument, a
model or framework, a design process or method, a described practice, or a synthesis of other work.

**I3. It gives evidence for what it proposes, and that evidence can be logical.** A source needs
evidence, but not necessarily empirical evidence. Data, analysis and synthesis count, and so does a
reasoned argument that can be followed and disagreed with on its premises. A source that proposes a
claim on reasoning alone is included, and its claim is coded `q1` (theoretical argument) with no
effect size. How strong the evidence is does not decide inclusion. That is what the `q` code records.

**One argument is enough.** A source that makes a single argument is complete with a single claim.
Nothing requires a source to yield several.

## Every paradigm is in

Inclusion never depends on method. These are all eligible, each recorded honestly for what it is:

- experimental and quasi-experimental studies, and meta-analyses of them;
- correlational, observational and survey research;
- qualitative research, including small-n, case study, ethnography and interview studies;
- design-based research and design cases;
- theoretical and philosophical work, including ethics and critical perspectives;
- historical and conceptual analysis;
- narrative and systematic reviews.

A small-n qualitative study and an RCT answer different questions, and the wiki keeps both. The
evidence codes and the claim's scope carry the difference. Rejecting the study does not.

## Domain is never a reason to exclude

A narrow population or an unusual setting is a scope qualifier on the claim ("for surgical trainees",
"in a four-week immersion programme"). It is never a rejection reason. A claim page records where its
evidence comes from, and a designer decides whether that transfers to their setting. The wiki does
not decide it for them by leaving the source out.

## A source is excluded for one of four reasons

**E1. Opinion piece** (`opinion-piece`). The source asserts positions with no evidence of either
kind: no data, and no reasons. Examples are editorials, commentary and advocacy that state a view,
and reflective career essays. A position paper that argues its position is not E1. What separates
this from theoretical or philosophical work (I3, included) is *reasoning*. When in doubt, include.

**A widely cited opinion is ingested, as exactly what it is.** Much of what the field cites is
expert opinion that nobody has tested, and it gets cited *as if* it were evidence, often on the
author's reputation. Leaving those sources out would leave that gap invisible. So:

- An obscure opinion piece is rejected under E1.
- A **widely cited** opinion, meaning one **cited by five or more wiki pages**, is ingested on purpose. Its claim is coded `q1` (expert opinion is
  already part of that tier), and its evidence entry says plainly that **no evidence or argument was
  offered**. The claim's `## Discussion` says what evidence, if any, exists elsewhere. A downstream
  reader or agent then finds that citing it justifies nothing, however respected the author.

**E2. Not about learning or its design** (`out-of-scope`). Career advice, academic publishing and
journal selection, conferences, professional networking, hiring and job-role inventories, business
logistics. The test is the subject of the source, never its domain: a paper on how nurses learn a
procedure is in, and a paper on nursing staffing levels is not.

**E3. Nothing to extract** (`no-ingestable-content`). A pointer to content elsewhere, a bare
bibliography, a stub, a table of contents.

**E4. Already covered** (`already-covered`). The wiki already carries this source's contribution
from the same source, as a duplicate or another version of it. A *different* source making the same
point is not E4: it is more evidence, and belongs in the claim's `## Evidence`.

Failed runs (`parse-error`, `validation-error`, `no-contributions-extracted`) are not exclusions.
They say nothing about the source, and discovery retries them.

## Earlier rejections these criteria would decide differently

The manifest is append-only, so these stay as written. A re-review appends a new entry with
`log_source_review.py`, and discovery then treats the source as settled by that later entry.
From the 27 rejections written before these criteria:

**To re-review and include** (confirmed by the maintainer):

- *The Moral Dimensions of Instructional Design*: rejected as a "reflective/philosophical essay".
  Ethics is philosophy, and a claim resting on logical evidence is in (I3).
- *Design Thinking and Agile Design* and *Instructional Design Models*: rejected as process or
  project content. Studies of the design process are in (I1), and `processes/` and `methods/` exist
  for them.
- *The Development of Design-Based Research*: rejected as research methodology. It is about a
  design process (I1).

**Candidates, still undecided:**
- *A Survey of Educational Change Models*: rejected as organisational change. Adopting an
  innovation is learning by the adopters, and designers in organisations use these models.
- *Visualization as theory and experience* and *Methodological challenges of research on
  interdisciplinary learning*: borderline. They are methods for studying learning rather than for
  designing it, and I1 can reasonably be read either way.

The career, publishing, conference and networking rejections stand under E2. The IJSR position paper
with no findings stands under E1.
