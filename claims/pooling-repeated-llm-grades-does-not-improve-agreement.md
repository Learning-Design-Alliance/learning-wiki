---
type: claim
title: Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: pooling-repeated-llm-grades-does-not-improve-agreement
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

# Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

On short free-text answers, taking the median or mean of several LLM grades for the same answer does not improve agreement with a human grader in kappa, error or correlation, does not remove the grader's systematic bias, and only marginally reduces how often the same work receives a different mark. Measured on one model and one corpus of short answers; whether pooling helps on long, noisier work was not tested in this release, so the claim is scoped to short answers.

## Subclaims

- Pooling across *different* models can be worse than using the best model alone: the weaker members' votes drag the estimate down.
- Bias is untouched by pooling, which is the diagnostic. Averaging removes variance; a grader that is systematically generous is generous in every draw.
- Pooling is a variance reduction, so it should be judged separately on agreement and on self-consistency. It fails on both here, but for different reasons, and the second failure is the more interesting one.
- The agreement null holds in correlation as well as kappa on short answers. Averaging compresses scores and kappa penalises compression, so kappa can hide a ranking gain; on the short-answer corpus it hides almost nothing (nine passes: Pearson r +0.0035, inside a pre-set ±0.01 equivalence margin), because repeated grades of one answer rarely differ and never straddle the human mark.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Pooled estimators (median and mean of three passes, and a cross-model pool) against a single call on the same 150 stratified answers from a public, teacher-graded corpus of undergraduate computer-science answers, on Gemini 3.5 Flash Lite in single runs, with re-grade flip rates on 100 answers and a later re-run of nine passes read in Pearson r with intervals resampling students. These results are in the release's evidence records and interpretation, not in its article. Observation record: `lazuli-grader-jorgpt-2026`.

## Discussion

**Scope of the claim.** Self-consistency by majority vote is a well-established technique for reasoning tasks with a verifiable answer, where independent errors cancel. This claim is about *rubric scoring*, where the residual disagreement with a human reference is dominated by systematic error and by noise in the reference itself — neither of which averaging can reach. It is not a claim that self-consistency does not work in general.

**Why it fails on stability too, which is less obvious.** Learners do not complain that their grade is wrong; they complain that the same work got a different mark. That is a variance phenomenon and pooling is a variance reduction, so it should help, and it barely does: pure re-grade flips fall from a quarter to a fifth, within the standard error at the sample size measured. Against reformatted resubmissions it does essentially nothing, because a reformat *shifts* where the grader settles rather than resampling it, and pooling averages around a centre rather than moving the centre back.

**What follows practically.** Three or four model calls per grade is a three- or fourfold cost increase for no measurable return on either objective. If the budget exists, it buys more as a better model tier, which does move calibration. And the stability problem has a cheaper and complete answer: do not re-grade unchanged content at all.

**What kappa cannot see, and where it might matter.** Pooling was first measured in kappa only, and kappa penalises the compression averaging creates, so a ranking gain could hide behind it. Re-run on the short-answer corpus with nine passes and read in *r*, the gain is +0.0035 (learner-clustered 95% interval +0.0026 to +0.0048), kappa +0.007, mean absolute error unchanged. The reason is the grader's per-item noise: on short answers the nine passes of one answer have a standard deviation of 0.18 points and no answer's passes straddle the human mark, so there is nothing for averaging to cancel. Items where a grader's per-item noise is larger, such as whole programs, could behave differently; that is outside what this release reports.

**Where pooling might still earn its place.** Near a threshold — a pass mark, an unlock condition — the quantity that matters is not mean agreement but the probability of landing on the wrong side of one boundary, and a blanket k=3 is the wrong shape for that anyway. Targeted self-consistency near thresholds only was not tested here and remains open.

## Related Claims

- [LLM short-answer graders can reach human rater agreement.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — why there is little residual agreement left to win
- [Surface formatting changes shift LLM grades without penalising them.](surface-formatting-changes-shift-llm-grades-without-penalising-them.md) — the instability pooling was expected to fix
- [Graded exemplars shift an LLM grader by the level they are marked at.](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — what to spend the budget on instead
