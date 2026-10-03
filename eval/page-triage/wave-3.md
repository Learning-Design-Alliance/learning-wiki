# Conversion wave 3 (2026-10-02)

The next 15 canonical pages by inbound links after wave 2 (`wave-2.md`). Four higher-ranked pages were skipped:
`principles/behaviorism` and `principles/social-learning` read as theories rather than principles;
`principles/explaining-their-thinking` overlaps self-explanation; `principles/self-regulation` duplicates the
converted `self-regulated-learning`. `patterns/adaptive-learning` (a 1 KB stub) and `principles/case-studiescase-based-learning`
(a malformed slug whose pattern is converted) were left for a fold rather than a conversion.

**The brief changed in one way, aimed at brief fit**, which waves 1 and 2 left flat (3.75 → 3.68 in wave 2): every
page now carries `## Fitting the design to a situation` (after the default design on a principle; after the
sequence on a pattern). It names **the three facts that most change the decision**, each with the question to ask
when a brief leaves it out, and gives a table `| If the brief says… | Then change… | Basis |` covering learner
expertise, age or stage, kind of goal, setting and mode, time, group size or no teacher, stakes, and one constraint
common in the topic. Each Basis cell is a claim link with a capped marker or says the row is untested, and any claim
carried to a population or setting it did not test says so. The default design and sequence give concrete
quantities where the old page or a claim gives them, and a pattern's illustrative instance is set somewhere unlike
the evidence.

| Page | Inbound | Related converted pages | Situation rows (on a claim) |
|---|---|---|---|
| principles/guided-practice | 28 | scaffolding-and-fading, worked-examples, direct-instruction | 10 (7) |
| principles/error-analysis | 26 | immediate-feedback | 10 (7) |
| principles/cognitive-activation | 25 | active-learning | 11 (7) |
| principles/goal-setting-monitoring | 22 | self-regulated-learning | 10 (8) |
| patterns/blended-learning | 22 | active-learning, self-regulated-learning, community-of-inquiry | 10 (4) |
| patterns/concept-attainment | 21 | inquiry-based-learning, analogical-reasoning | 10 (5) |
| principles/cognitive-flexibility | 20 | analogical-reasoning | 10 (8) |
| patterns/elaboration-theory | 20 | 4C/ID, clear-structure, chunking | 10 (6) |
| principles/multimodal-instruction | 18 | multimedia-learning | 10 (7) |
| principles/game-based-learning | 18 | | 10 (4) |
| patterns/constructive-alignment | 18 | assessment-for-learning, competency-based-assessment | 10 (6) |
| principles/reflection | 15 | self-regulated-learning | 10 (8) |
| principles/experiential-learning | 15 | inquiry-based-learning, problem-based-learning | 11 (6) |
| patterns/structured-academic-controversy | 15 | debate, cooperative-learning | 11 (5) |
| principles/epistemic-cognition | 13 | inquiry-based-learning | 10 (6) |

"On a claim" counts rows whose Basis cell links a claim; most of those say how far the claim is being carried.
94 of 153 rows cite a claim, 59 are labelled untested. Checked by script as waves 1 and 2 were: no old line lost,
no frontmatter key changed but description, status and generated, no cited claim dropped, no marker above cap, no
broken link, every section present (every principle has a default design), and every quoted number found on a
cited claim page or the old page.

**No claim tests the page's relationship as a whole on 13 of the 15** (all but goal setting, where two meta-analyses
test goals on work and health tasks rather than learning, and cognitive flexibility, with one small trial). Each
says so and keeps a labelled default design or sequence.

## Brief test (2026-10-02)

Same design as waves 1 and 2 (scratch only): 30 new briefs written before any draft existed, one complete and one
sparse per page, set where the brief's facts should change the design (an evening adult maths class with anxious
learners, a hospital sepsis rollout across shifts, refugees not literate in their first language). Kimi K3 answered
from one version of the page (OLD = main before this change, NEW = after); Gemini 3.8 Flash and DeepSeek V4 Pro
graded against every claim either version cites, and blind in pairs, both orders. Two measures were added for this
wave's aim: an anchored **situation fit** score (5 = at least three design choices changed because of named facts in
the brief, and says which; 3 = mentions the facts but the design would barely differ elsewhere) and, in each pair, a
separate question on which answer is more fitted to the situation. $4.58.

| | OLD | NEW |
|---|---|---|
| affordances /12 (all / complete / sparse) | 5.8 / 7.6 / 3.9 | 8.8 / 10.1 / 7.4 |
| accuracy (1–5) | 4.07 | 4.52 |
| decision value (1–5) | 4.05 | 4.52 |
| brief fit (all / complete / sparse) | 3.78 / 3.90 / 3.67 | 3.88 / 4.07 / 3.70 |
| situation fit, anchored (all / complete / sparse) | 3.82 / 4.00 / 3.63 | 3.90 / 4.13 / 3.67 |
| blind pairs (all / complete / sparse) | 19 / 14 / 5 | **101 / 46 / 55** |

Blind pairs: **101–19 for the new pages** (complete 46–14, sparse 55–5); all four judgements agree on 20 of 30
briefs. Median answer length 556 words (OLD) and 611 (NEW). DeepSeek picked the answer shown first in 39 of 60
pairs, Gemini in 30 of 60.

**What this says about situation fit: a small gain on complete briefs, none on sparse ones, and the measures are
weak.**

- On complete briefs both fit scores rose a little (brief fit 3.90 → 4.07, situation fit 4.00 → 4.13), with
  DeepSeek, the grader that does not give everything 5, moving 2.80 → 3.13 and 3.07 → 3.27. In wave 2 brief fit
  had fallen (3.75 → 3.68). On sparse briefs DeepSeek scored the new pages lower (2.80 → 2.40).
- **The scale is saturated for one grader and the separate fit question is not independent.** Gemini scores 4.7–5.0
  for both versions. The pairwise "more fitted" pick matched the overall pick in 118 of 120 judgements, so its 99–21
  repeats the overall result rather than measuring fit apart from it. A better test of fit needs a grader that sees
  the same answer against two different briefs, or briefs that differ only in one fact.
- So the situation section did not make answers markedly more fitted. It did not cost accuracy or decision value,
  which rose as in earlier waves, though by less than in wave 2 (accuracy +0.45 against +0.84).

**Where the new page lost.** Guided practice lost both briefs 1–3: graders preferred the old page's concrete
three-week fading arc for a Year 4 class and its workplace ramp, and called the new answers cautious; one judgement
says a new answer "leaks internal prompt artifacts (e.g. 'observation table', 'default steps')", that is, it echoed
the page's section names to the designer. Error analysis's complete brief (adult equivalency maths) lost 1–3: the old
answer broke sign errors into their kinds, the new one led with the evidence's limits. Both are the wave 1 lesson
again: **a page whose default design is less concrete than the old guidance loses**, and the situation table did not
make up for it. The complete briefs for game-based learning, reflection and elaboration theory split 2–2.

## Rework of the two losing pages (2026-10-03)

Read against the old answers that beat them, both losses had the same gap: **no dose or progression across
sessions.** The old guided-practice answer gave a three-week arc for withdrawing support; the old error-analysis answer
gave 20–30-minute segments within each session and a progression from a fictional peer's errors to the learner's
own. Both new pages planned one session. Changes (all labelled untested proposals, scratch re-test $1.11):

- **Error analysis**: two default-design steps, building the examples from the learners' own diagnostic errors
  sorted by the step where each goes wrong, and a dose and progression across sessions.
- **Guided practice**: default-design steps for items where the step is not needed (practising the decision) and an
  arc for withdrawing support across sessions; a think-aloud at the decision point when re-modelling. **The
  three-in-four success figure is gone from the design**: both graders called it an arbitrary import from retrieval
  practice, so the claim stays cited for what it is and the threshold is set locally. A new situation row covers
  many-step or costly-error tasks (more rounds, a stricter release criterion, supervised unassisted work, and what
  "working alone" means), which the old answer had elicited for the workplace brief. The classroom row now has the
  teacher scan every learner's attempt at once rather than leaning on peer checking, which graders thought unsafe
  for 8-year-olds holding a common misconception.

Re-tested on the same briefs, the reworked page against the old one (one fresh answer per run, both graders, both
orders):

| Brief | Wave 3 | After rework |
|---|---|---|
| Error analysis, complete (adult equivalency maths) | 1–3 | **3–1** |
| Error analysis, sparse | 3–1 | 3–1 |
| Guided practice, complete (Year 4 subtraction) | 1–3 | 2–2, 1–3, then **4–0** after the classroom row |
| Guided practice, sparse (new hires) | 1–3 | 1–3, **3–1** after the success-rate and stakes changes, 2–2 |

One answer per run moves a brief by about one judgement either way, so read the direction, not a single cell.
**What remains, and is not the pages': answers cite the page's own structure to the designer** ("page, step 4",
"the observation table", "the classroom row"), and graders mark that down as meta-commentary. The answer prompt asks
for answers from the page, and the new pages' numbered steps and named rows invite it; every converted page is
exposed to it, and it affects old-versus-new comparisons in the old pages' favour. A test that tells the answerer
to write for a designer who has not seen the page would separate the two.

## Open findings from the agents

- **Citation mismatches between frontmatter and Key Sources** (left unchanged; each needs a Crossref check):
  Jacobson & Spiro on cognitive-flexibility (`4T1B-6E7P-7J9M-3X4M` against `4t1b-hbp0-3f7e-j4pn`); Numrich on
  guided-practice (`tesj.254` against `tesj.258`); Gellevij (`…599506`/`…599507`) and Givens (ISBN ending `1464-9`
  against `0246-4`) on multimodal-instruction; Reigeluth on elaboration-theory (`BF02984376` against `bf02984374`,
  and Reigeluth 1979 listed twice).
- **`patterns/constructive-alignment` was cut off mid-link on main** since its creation (`assessment-for-learning-impro`),
  so it never had Claims, Related, Examples or Key Sources sections. The conversion keeps the fragment in its
  deprecated block. Biggs (1996) is cited only in frontmatter and has no claim page.
- **Claim titles that overstate their evidence**: `practice-presence-raises-cbi-posttest-achievement` says "with
  feedback", which its entry never describes; `tutoring-effectiveness-comes-from-scaffolding-and-feedback` (its
  Discussion supports scaffolding only); `reflective-practice-evidence-mixed-in-professional-education` (its
  Discussion says the meta-analysis does not show "mixed"); `theorem-theses-confirmed-by-survey` (it measured stated
  priorities); `structured-discussion-methods-improve-comprehension` names SAC, which neither entry tests;
  the checklist source-evaluation claim; `whole-task-performance-improves-transfer` (a design argument, as before).
- **A claim contradicting its own entry**: `erroneous-examples-build-conceptual-knowledge` says "middle-school" and
  "especially on transfer"; its entry is grades 4–5 and does not mention transfer, and its Discussion's novice
  caution has no basis in the entry. error-analysis now calls that caution a precaution.
- **Stale claim text**: `cognitive-flexibility-theory-multiple-cases` ("stub currently has no evidence entries"),
  `considering-the-opposite-reduces-bias`, and `reflective-practice-improves-outcomes-when-structured` ("needs
  primary evidence entries") all have entries.
- **Merge candidates**: `civic-online-reasoning-instruction-improves-evaluation` and
  `lateral-reading-improves-source-evaluation` (same three entries); `structured-discussion-methods-improve-comprehension`
  and `discussion-quality-drives-comprehension`; `goal-setting-improves-performance` and `specific-difficult-goals-…`;
  the self-explanation family; `interleaved-practice-improves-retention` and `interleaving-improves-inductive-learning`;
  `matching-instruction-to-styles-no-effect` and the learning-styles claim.
- **A wrong link on a claim page**: the Discussion of `blended-learning-improves-outcomes` labels a link "flipped"
  that points at `patterns/blended-learning`.
- **Pages that are not what their kind says**: `patterns/guided-practice-four-purposes` is a claim about teacher
  learning; `patterns/game-based-mastery-learning` reads as gamification; `fading-based-scaffolding-approaches-serious-games`
  describes one paper. "Cognitive flexibility" also names an executive function: the kindergarten literacy claims
  are about that sense and are named on the page, not linked.
- **Unconverted neighbours** worth the next wave: `principles/sequencing` (elaboration theory's principle),
  `patterns/experiential-learning-cycle` (experiential learning's pattern), `principles/evaluating-sources`.
