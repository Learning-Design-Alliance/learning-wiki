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
Sources about the people and processes that produce learning (designers, teachers, design processes,
design methods, programme evaluation) count as well.

**I2. It offers something that can be extracted.** That can be a finding, a reasoned argument, a
model or framework, a design process or method, a described practice, or a synthesis of other work.

**I3. Its basis can be stated.** It can say what its contribution rests on: data, analysis, a
developed argument, or the sources it synthesises. How strong that basis is does not decide
inclusion. That is what the `q` code records.

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

**E1. Opinion piece** (`opinion-piece`). The source asserts positions without evidence and without a
developed argument: editorials, commentary, advocacy, position papers that report no data, reflective
career essays. What separates this from theoretical or philosophical work (I3, included) is
*reasoning*. A philosophical paper builds an argument, engages other work and can be disagreed with
on its reasons. An opinion piece states a view. When in doubt, include it and code it `q1`.

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
Candidates, from the 27 rejections written before these criteria:

- *The Moral Dimensions of Instructional Design*: rejected as a "reflective/philosophical essay".
  Under I3 and the paradigm rule, a developed ethical argument is in.
- *Design Thinking and Agile Design* and *Instructional Design Models*: rejected as process or
  project content. The wiki has since gained `processes/` and `methods/` for exactly this.
- *The Development of Design-Based Research*: rejected as research methodology. Design-based
  research is a design method in its own right.
- *A Survey of Educational Change Models*: rejected as organisational change. Adopting an
  innovation is learning by the adopters, and designers in organisations use these models.
- *Visualization as theory and experience* and *Methodological challenges of research on
  interdisciplinary learning*: borderline. They are methods for studying learning rather than for
  designing it, and I1 can reasonably be read either way.

The career, publishing, conference and networking rejections stand under E2. The IJSR position paper
with no findings stands under E1.
