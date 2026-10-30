---
type: claim
title: Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: human-graders-agree-less-than-single-grade-ground-truth-implies
aliases: [expert-human-graders-agree-with-each-other-far-less-than-assumed]
evidence_strength:
newest_evidence: 2026
recheck_by: 2029
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

# Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

Two graders applying the same scheme to the same open-ended work agree with each other considerably less than the treatment of human grades as ground truth implies: pooled agreement below 0.52 in quadratic-weighted kappa on two corpora, with pairs from 0.035 to 0.730. How much less depends on the task, and the level depends on the statistic. Neither corpus records whether its graders were experts or trained.

## Subclaims

- A single human grade is not ground truth. It is one draw from a distribution whose spread is rarely measured, because measuring it requires paying two people to grade the same work.
- Agreement is not one number. Across 42 grader pairs marking the same work to the same rubric, pairwise agreement ranged from near zero to substantial (quadratic-weighted kappa 0.035 to 0.730, median 0.410).
- Agreement depends on what the rubric asks. On one corpus scoring four dimensions separately, the most nearly objective dimension agreed best and the most interpretive worst: correctness 0.486, documentation 0.368, on the same work by the same graders (14-level scale; this per-dimension breakdown is in the release's evidence records, not its article).
- Where a second rater is unavailable, agreement figures computed against the single rater available carry an unmeasured component of that rater's own noise. Where it could be measured here, about half (0.45–0.55) of each of three LLM graders' squared error against one human was that human's own disagreement with the other raters, if the grader's errors are independent of the raters'.
- Filters applied to a graded corpus for data quality can remove precisely the cases the raters disagreed on, biasing any measured ceiling upward.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `associational · r?`

Agreement between human raters computed from public deposits with no model involved (the article's Section 5.1): two independent raters on 1,727 data-structures short answers (Mohler), 28 recruited graders on 279 Java programs scored on four rubric dimensions (Menagerie, 6,600 co-grading pairs), and four instructors on every item of a half multiple-choice corpus (HARMOGEN-R), each in quadratic-weighted kappa with Gwet's AC2 beside it as a robustness check. Observation records: `lazuli-grader-mohler-2026` and `lazuli-grader-menagerie-2026` (supports), `lazuli-grader-harmogen-2026` (qualifies).

## Discussion

**Scope of the claim.** It is about open-ended work (short free-text answers, and whole programs judged on rubric dimensions) scored on an ordinal scale by graders working independently. It is not a claim about well-moderated high-stakes marking with adjudication, double-blind second marking and a published rubric — a process designed to produce agreement will produce more of it, and the claim is bounded accordingly.

**Why it matters beyond grading research.** Agreement with a human rater is the usual check on an AI grader, and the release's reading is that agreement with one human is a weak instrument on short free-text answers: on the corpora where it could be measured, much of a grader's residual disagreement with one human is noise in the human reference. It follows (the wiki's inference, not the source's) that a model tuned to match one rater's grades is tuned partly to that rater's noise, and that an apparent gap between machine and human performance is partly the gap between two humans.

**The measurement problem this creates.** Once the reference is noisy, agreement alone says less, and the article recommends reporting other properties beside it: the grader's signed error for weaker and stronger work, its run-to-run variation, and whether its marks change on identical work when information about the student is added. The last two need no human reference grades, and the article recommends the identical-work check alongside agreement for any AI grader. It also recommends stating the reliability of the human reference beside any agreement figure.

**Replication.** The evidence is two independent corpora, and the second is the stronger instrument: 28 graders recruited expressly for a grader-consistency study, four raters on almost every item (three on 32 of 1,116), four rubric dimensions scored separately. On a scale collapsed to match the first corpus's granularity it agrees *less*, not more (0.465 against 0.519). Both put pooled agreement below 0.52; per pair on the second it ranges from 0.035 to 0.730. The second corpus's own authors, reading the same grades, conclude that graders "can not agree on the grade to give a piece of student work"; that rests on the same data, so it is not an independent replication.

**The level belongs to the statistic too.** The figures above are quadratic-weighted kappa. Under Gwet's AC2, whose chance term does not come from the observed marginals, the same raters agree at 0.858 on the first corpus and 0.887 on the second (five levels; 0.749 on fourteen), with pairs from 0.609 to 0.916. The difference is the kappa paradox: the first corpus's marks bunch at the top, and on a draw stratified to flatten them the two statistics agree (0.531 and 0.562). So "below 0.52" is a statement about kappa, and the level should not be quoted without its statistic. What the claim is used for survives the change: no grader-versus-human comparison reverses, and the choice of human reference still moves a grader's agreement by 0.23–0.28. AC2 is not the better yardstick for graders: it scores a constant grader above the humans.

**The ceiling belongs to the task.** A third corpus, HARMOGEN-R, found four instructors agreeing at QWK 0.981 on a corpus where half the responses were a bare multiple-choice letter, and at 0.942 on its genuinely open items. Near-closed items produce near-perfect agreement. So the low figures here describe open-ended judgement, not human graders in general, and a machine agreement figure is readable only against the ceiling for its own task.

**What would bound this.** The two corpora behind the low figures are computing coursework — short text answers in one, Java submissions in the other — and neither records whether its graders were instructors, teaching assistants or students, which matters a great deal for what a low figure means. Neither says anything about high-stakes marking with published rubrics, double-blind second marking and adjudication, which is a process designed to produce agreement and can be expected to produce more of it.

## Related Claims

- [LLM short-answer graders agree with one human rater more, and the other less, than the two raters agree with each other.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — the claim this one is the reference level for
- [Peer feedback accuracy depends on expertise.](peer-feedback-accuracy-depends-on-expertise.md) — variation between human assessors from the other direction
- [Rubrics improve peer feedback quality.](rubrics-improve-peer-feedback-quality.md) — the intervention that would be expected to raise the ceiling
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](closed-llm-graders-below-human-floor.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [The TA ground truth was produced under a one-rater-per-item design with co-grading, an exceptions log, instructor audit, and student review, with an estimated grading-error rate of about 0.1% in the student-inspected subsample](ta-ground-truth-one-rater-per-item-error-rate.md) — related
- [Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers](pooling-repeated-llm-grades-does-not-improve-agreement.md) — related
- [Instructor-confirmed grading errors occurred at roughly 0.02–0.04% of rubric line items across the term](lata-instructor-confirmed-error-rate.md) — related
- [After studying the composition scale, normal-school students double-rated 32 seventh-grade compositions, each composition being rated by two students with the second rater rating a different set](witham-double-rating-32-compositions.md) — related
- [Peer graders in these MOOCs score more leniently and with greater dispersion than the instructor](peer-grading-lenient-high-dispersion-moocs.md) — a narrower finding that bears on this claim
- [Kappa agreement with human experts shows a system is neither much worse nor much better than experts, but not that experts are a desirable comparison basis](kappa-expert-agreement-limits.md) — related
- [Expert graders show high agreement among themselves when scoring a written exam on first degree equations](expert-inter-rater-agreement-high-written-exam.md) — related
- [Peer assessment systems can generate explanatory feedback for students by having graders assess multiple labeled aspects of an answer, not just an overall grade.](peer-assessment-multi-label-feedback.md) — related
