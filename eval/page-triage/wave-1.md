# Conversion wave 1 (2026-10-02)

The 15 most-linked canonical pages the triage (`triage.tsv`) found unconverted, rewritten to the
conditional-model format (`principle-pattern-authoring.md`) by one agent each from a brief (scratch, not
committed, adapted from the pair brief to single pages). Where a converted sibling existed, the page states the
more general relationship and places the sibling inside it.

| Page | Inbound | Converted sibling |
|---|---|---|
| principles/cognitive-load-management | 395 | principles/cognitive-load-theory |
| principles/annotating | 369 | |
| principles/check-ins | 361 | |
| principles/chunking | 353 | principles/cognitive-load-theory |
| principles/assessment-for-learning | 340 | principles/formative-assessment |
| principles/active-learning | 305 | |
| principles/clear-structure | 236 | |
| principles/collaborative-learning | 202 | principles/cooperative-learning |
| principles/building-empathy | 173 | |
| principles/accessible-vocabulary-syntax | 166 | |
| principles/authentic-audiences-purposes | 163 | |
| principles/activation | 158 | |
| patterns/case-based-learning | 151 | |
| principles/scaffolding | 145 | principles/scaffolding-and-fading |
| patterns/think-pair-share | 113 | |

**Checked by script against each old page**: no old line lost, no frontmatter key changed but description,
status and generated, no claim the page cited dropped, no marker above its cap, no broken link, every section
of the format present, and every number the new sections quote found on a cited claim page or the old page.
See the brief test below.

## What the wave found, open

**No claim tests the page's own relationship** on most of these pages; each says so plainly rather than
stretching a neighbour: annotating (learner-written notes), check-ins (a check-in routine), clear structure
(course and lesson organization), accessible vocabulary (simplified against original text, content held
constant), authentic audiences (real against simulated audiences; learning apart from the product), building
empathy, activation (activation against starting instruction), collaborative learning (collaborative against
individual work on the same task), case-based learning (the whole format), think-pair-share, scaffolding
(kinds of support compared, or a delayed classroom test), cognitive-load management (the sequence-level policy).

**Claims whose titles overstate their entries**: `annotating-improves-learning` (both entries are about
highlighting), `activation-improves-learning`, `experimenter-underlining-effective-as-student-underlining`
(one non-significant result, no n), `mismatched-graphic-organizers-increase-extraneous-load`,
`tutoring-effectiveness-comes-from-scaffolding-and-feedback`, `fiction-reading-improves-empathy` (measures
social-cognitive task performance), `scaffolding-improves-learning` (opens "provided the support is faded";
its Belland entry found no difference by fading), `interdependence-type-no-achievement-effect-asynchronous`
(title says adult reentry students; the entry says 280 undergraduate business majors).

**Stale text on claim pages** (a Discussion or status line saying there is no evidence beside entries):
`building-empathy-improves-intergroup-attitudes`, `case-based-learning-improves-exam-performance`,
`vocabulary-instruction-improves-comprehension`, `annotating-improves-learning`.

**Citations to check against Crossref**: `principles/accessible-vocabulary-syntax`'s frontmatter
`binder-2020` resource ends `…12319`, which does not resolve; its Key Sources `…12314` resolves to the Binder
paper (and Binder 2020 is about word-form transparency, off the page's topic). On `principles/building-empathy`
the Key Sources DOIs for Sachs (2019) and Setlhodi (2018) differ from the frontmatter `resource:` DOIs.

**Merge candidates**: `comparing-contrasting-cases-improves-learning`, `multiple-contrasting-cases-support-
abstraction` and `analogical-reasoning-improves-transfer` (the same Alfieri and Gentner entries);
`reading-literary-fiction-improves-theory-of-mind` and `fiction-reading-improves-empathy` (the same three
entries); `clear-structure-improves-learning` and `signaling-improves-learning`; the principles
`scaffolding` and `scaffolding-and-fading`, and `assessment-for-learning` and `formative-assessment`; about
eight near-duplicate strategy pages each for chunking, activating background knowledge and annotation.

**Other**: the claim `cognitive-load-management` shares its slug with the principle; `segmenting-improves-
multimedia-learning`'s summary says learner-paced where its entry says system-paced; `advance-organizers-improve-
learning`'s gains are larger for high-ability learners; `principles/case-studiescase-based-learning` has a
malformed slug; no pattern pairs with most of these principles.

## Brief test (2026-10-02)

Same design as the 2026-10-01 and -02 format studies (scratch only, so the briefs stay unseen by page writers):
30 new briefs, one complete and one sparse per page; Kimi K3 answered each from one version of the single page,
frontmatter and HTML comments stripped as a reader sees them (OLD = main before #155, NEW = after); Gemini 3.8
Flash and DeepSeek V4 Pro graded against every claim either version cites, on the six affordances plus accuracy,
decision value and brief fit, and blind in pairs, both orders. $4.25.

| | OLD | NEW |
|---|---|---|
| affordances /12 (all / complete / sparse) | 7.5 / 9.9 / 5.1 | 10.7 / 11.4 / 10.0 |
| accuracy | 3.95 | 4.78 |
| decision value | 4.15 | 4.78 |
| brief fit | 3.78 | 3.85 |
| blind pairs (all / complete / sparse) | 20 / 16 / 4 | **100** / 44 / 56 |

Both graders agree in direction on every measure; brief fit barely moves because DeepSeek scores it low for both
(about 2.6 against Gemini's 5). **DeepSeek's pairwise judgements lean to whichever answer comes first**: of its 60,
the unswapped order (OLD first) went to OLD in 14 briefs where the swapped order went to NEW. Gemini picked NEW
in both orders in 27 of 30 briefs. Unanimous on 16 of 30 briefs.

**Accessible vocabulary and syntax lost its complete brief 0–4**, the only unanimous loss: graders preferred the
old page's concrete plan (two versions of each item, explicit syntax unpacking, fading supports) and DeepSeek said
the new answer misapplied the input and cohesion claims. **Reworked** the same day: a "Default design, while the
relationship is untested" section restores the old guidance as six steps, each labelled with its evidence status,
and the evidence section now says how far the input and cohesion claims may be carried. Re-tested on both briefs
($0.21): the complete brief now ties the old page 2–2 and beats the first new version 4–0; the sparse brief beats
the old page 3–1 and loses to the first new version 1–3. One answer per arm, so read these as signals. Close
calls on clear structure and scaffolding (2–2, split by position) went to OLD only when it was shown first.

**The lesson repeats problem-based learning's**: where no claim tests the page's relationship, a rewrite that
leans only on neighbouring claims loses the concrete design the old page carried. Keep that design, labelled as a
proposal, rather than leaving the answerer only caveats.
