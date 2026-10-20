---
type: claim
title: LLM Short-Answer Graders Can Reach Human Rater Agreement
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: llm-short-answer-graders-can-reach-human-rater-agreement
evidence_strength:
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480844"
    title: "David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# LLM Short-Answer Graders Can Reach Human Rater Agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

A large language model scoring free-text short answers against a rubric and a model answer can agree with a human grader about as closely as two human graders agree with each other.

## Subclaims

- Agreement should be read against a measured human-human ceiling, not against 1.0. Where that ceiling is unmeasured — which is the usual case, since most graded corpora carry one rater — an agreement figure states a level and not a quality.
- Which human is chosen as the reference materially changes the measured agreement. On the one corpus here with two independent raters (Mohler) the same grader scores 0.549 against one rater and 0.798 against the other, and on three further models the choice of rater moves agreement by 0.23–0.27 in quadratic-weighted kappa.
- Agreement statistics must be reported with a discrimination statistic beside them. A grader that hedges toward the middle of the scale posts a respectable kappa while having stopped distinguishing anything, and kappa alone conceals it.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `associational · r?`

A shipped LLM grading prompt scored public, teacher-graded corpora, and its agreement with the human marks (quadratic-weighted kappa, with bias and a spread ratio beside it) was read against human–human agreement measured on corpora with two or more raters (the article's Section 5.1): undergraduate computer-science answers with one teacher (JorGPT, a 150-answer stratified draw), data-structures answers with two independent raters (Mohler), whole Java programs with four raters (Menagerie), and a re-analysis of a deposit with four instructors on every item (HARMOGEN-R). Several figures are single runs. Observation records: `lazuli-grader-jorgpt-2026`, `lazuli-grader-mohler-2026` and `lazuli-grader-harmogen-2026` (supports), `lazuli-grader-menagerie-2026` (qualifies).

## Discussion

**Scope of the claim.** It is about *agreement on a rubric-scored ordinal scale for short free-text answers*, measured by quadratic-weighted kappa. It is not a claim that the grader is right, that it is fair, or that it is stable — those are separate propositions with separate evidence, and two of them come out considerably less well. It is also not a claim about production: the measurements are on university computer-science and data-structures corpora, other people's questions and other people's rubrics.

**Why the ceiling is the whole argument.** An agreement of 0.85 sounds like a 15% error rate and is not one. On the only corpus available with two independent raters, two graduate assistants marking the same answers to the same questions on the same course agreed at 0.519 — and lower still on the rows a consistency filter had removed, so the true figure is below that. Against a single human reference, much of what looks like machine error is disagreement the humans would have had with each other: if the grader's errors are independent of the raters', about half (0.45–0.55) of each of three graders' squared error against one human is that human's own disagreement with the others. The level is also a kappa statement: under Gwet's AC2 the same Mohler raters agree at 0.858, and no grader-versus-human comparison reverses.

**What the interventions found.** Four attempts on one model (Gemini 3.5 Flash Lite) detected no change in agreement: a stronger model tier, pooling three or four calls, anchor exemplars, and supplying the learner's previous attempt (three single runs, and an interval on the last that leaves room for a gain of +0.056). They are not four nulls: on a harsh second model the anchor exemplars did raise QWK by 0.033, and on the Mohler corpus sibling course context raised it by up to 0.035 in a single run. A rescaling applied after grading did move agreement: fitting each grader's unlabeled marks to the teacher's mean and standard deviation, without information about the student, raised QWK by 0.047 to 0.132 on the models that mark below the teacher or compress the scale, and by 0.008 on Gemini, which already used the teacher's spread.

**What would falsify or bound this.** A well-moderated rater pair working to a shared rubric with adjudication would presumably agree far better than 0.519, and the claim should then be read against that higher bar. The corpora here record no rubric, training or moderation for their raters, so this is agreement between two people doing a job rather than agreement under a characterised protocol. On near-closed items the bar is high: on HARMOGEN-R, half multiple choice, four instructors agree at 0.981, and reaching that ceiling is a much weaker statement than reaching one of about 0.5.

**It does not extend to large artefacts or craft rubrics.** This release also had three models grade 60 whole student programs on four rubric dimensions, and in kappa every model agreed with the human graders far less than the humans agreed with each other (QWK 0.058 to 0.233 against 0.438, on fourteen levels); under AC2 no difference was resolved on fourteen levels. The claim is about short free-text answers judged on content.

## Related Claims

- [Human graders of open-ended work agree with each other less than treating one grade as ground truth implies.](expert-human-graders-agree-with-each-other-far-less-than-assumed.md) — the ceiling this claim is read against
- [Pooling repeated LLM grades does not improve agreement.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — one of the four attempts that detected no change in the residual gap
- [Graded exemplars shift an LLM grader by the level they are marked at.](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — another, and the one that separates calibration from agreement
- [Peer feedback accuracy depends on expertise.](peer-feedback-accuracy-depends-on-expertise.md) — the same question about human raters
