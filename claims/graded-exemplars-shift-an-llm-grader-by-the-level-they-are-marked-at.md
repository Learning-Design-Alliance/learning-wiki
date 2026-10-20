---
type: claim
title: Graded Exemplars Shift an LLM Grader by the Level They Are Marked At
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at
evidence_strength:
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480844"
    title: "David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Graded Exemplars Shift an LLM Grader by the Level They Are Marked At

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

Showing an LLM grader a small set of human-graded answers spanning the scale shifts its grade by the level those answers are marked at. On one model and draw that removed almost all of its generosity and left its agreement with the human grader unchanged; on a harsh second model the exemplars raised agreement (QWK +0.033 [+0.005, +0.068]) without resolvably moving bias. The shift comes from the grades attached to those answers, not from the extra context.

## Subclaims

- Calibration and agreement are different quantities and can move independently. An intervention that fixes one may do nothing at all for the other.
- On Gemini, the same exemplars with their grades stripped make the grader *more* generous and slightly worse on agreement — worse than showing nothing.
- On the original draw the bias change was the same size as the gain from moving to a stronger, more expensive model tier.
- The correct pairing of answer and mark matters: with the same marks shuffled across the answers the grader kept only about a third of the shift (37%, 95% interval 2% to 60%).
- The grader adopts the level the examples are marked at, right or wrong: 0.39 points per point of shown level on identical work on Gemini 3.5 Flash Lite, 0.16 on GPT-4.1-mini. The examples therefore apply a roughly fixed shift (−0.34 on Gemini) that cancelled the generosity on one draw, overshot on a wider one, and did not resolvably move a harsh second model's bias (−0.06 [−0.17, +0.03]) while raising its QWK by 0.033.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Within-item arms on one public, teacher-graded corpus of undergraduate computer-science answers (the article's Section 5.4): three teacher-graded answers to the same question (lowest, median, highest) shown with their marks, without them, with the marks deranged among the three, or with every mark shifted two points up or down. The original arms were one run on 150 answers; a pre-registered follow-up ran on 600 answers on Gemini 3.5 Flash Lite, with intervals resampling questions, and as a directional check on 146 answers on GPT-4.1-mini. Observation record: `lazuli-grader-jorgpt-2026`.

## Discussion

**Scope of the claim.** Three human-graded answers to the same question — low, middle, high — presented before marking, always in that order. It is not a claim about few-shot prompting in general, and not about exemplars drawn from a different question or a different course. The shift was measured on one model with a check on a second; its generality across models is not established.

**What the ungraded arm can and cannot show.** Stripping the grades reverses the effect and leaves the grader worse than the control, so the result is not "more context helps". But the ungraded arm also drops a closing instruction to grade on the examples' scale, so on its own it cannot say whether the marks or the instruction do the work. The shuffled- and shifted-mark arms, which keep the instruction, show the marks do, through their pairing with the answers and through their level.

**Why bias deserves separate attention from agreement.** Quadratic-weighted kappa penalises a constant offset only through its square relative to the score variance (it equals 2s_xy / (s_x² + s_y² + d²); Fleiss & Cohen 1973; Lin 1989). On this corpus removing a 0.32-point offset is worth 0.0065 of kappa, while a constant offset is exactly what a learner experiences when their score is compared against a pass mark or an unlock condition. A grader running a third of a grade point generous passes people who should not pass and is nearly invisible to the metric most often reported.

**The design consequence for anyone building this.** Graded example answers are not a reliable means of correcting a grader that marks too high or too low, because they shift marks by a roughly fixed amount rather than removing the grader's own offset, and examples marked too low cost accuracy (shifted two points down, MAE worsened by 0.24 and QWK by 0.043). A rescaling of the marks to the human scores' mean and spread, fitted without information about the student, corrects an offset directly; it needs a sample of human-scored answers from the students it will grade.

## Related Claims

- [LLM short-answer graders agree with one human rater more, and the other less, than the two raters agree with each other.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — why the agreement half of this result is unsurprising
- [Pooling repeated LLM grades does not improve agreement on short answers.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — the other candidate for the same budget
- [Showing an LLM grader a learner's prior performance biases the grade.](showing-a-grader-a-learners-prior-performance-biases-the-grade.md) — context about the work shifts the grade by its marked level; context about the learner shifts it by who the learner is said to be
- [Rubrics improve peer feedback quality.](rubrics-improve-peer-feedback-quality.md) — the same mechanism, in human assessors
