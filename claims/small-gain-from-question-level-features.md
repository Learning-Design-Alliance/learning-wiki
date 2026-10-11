---
type: claim
title: Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model
description: Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model
id: small-gain-from-question-level-features
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: benjamin-mawdsley-2026
    resource: "https://arxiv.org/abs/2607.26063"
    title: "Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063"
    author: Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` The improvement from adding per-question features to logistic regression is quite small, supporting the conclusion that overall mathematical competence is the dominant factor in predicting performance. [→ Benjamin Mawdsley 2026](#benjamin-mawdsley-2026)

## Evidence

### Benjamin Mawdsley 2026

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063

`q2 · i?` · `associational · r2`

Comparison of LogRegs (single average-grade feature) and LogRegm (19 per-question features) in the predictive evaluation; Table 1 shows accuracy 0.769±0.005 versus 0.778±0.005 with overlapping error bars. The improvement is described as "quite small".

> "Despite adding many more features, the performance improvement between a single feature logistic regression and a multi question performance is quite small, supporting the conclusion from [20] that the dominant factor in predicting performance is overall mathematical competence."

## Discussion


## Related Claims
- [Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance](cluster-profiles-dominated-by-overall-ability.md) — related
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets](time-window-features-null-for-lr-boost-nonlinear.md) — related
- [Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline](nonlinear-models-modest-auc-gains-over-logistic-baseline.md) — related
