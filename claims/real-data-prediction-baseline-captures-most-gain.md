---
type: claim
title: On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits
description: On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits
id: real-data-prediction-baseline-captures-most-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
newest_evidence: 2015
sources:
  - id: pelánek-2015
    resource: "https://doi.org/10.1007/s40593-015-0048-x"
    title: "Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x"
    author: "Pelánek, R., & Jarušek, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: pelánek-2015-2
    resource: "https://doi.org/10.1007/s40593-015-0048-x"
    title: "Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x"
    author: "Pelánek, R., & Jarušek, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Model predictions on real Problem Solving Tutor data improve clearly over mean time, but most improvement is captured by the baseline predictor, and the basic model's additional gain, while consistent, is small. [→ Pelánek 2015](#pelanek-2015)
`q2 i?` The model with learning leads to slightly worse predictions than the basic model, slightly overfitting the data. [→ Pelánek 2015 (2)](#pelanek-2015-2)

## Evidence

### Pelánek 2015

Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x

`q2 · i?` · `design · r2`

Evaluation on real data from 8 most-solved problem types using repeated random subsample cross-validation (10 repetitions, 70% training students, last 20% of attempts as test), measured by RMSE (Table 3). The "models provide clear improvement over the use of a mean time".

> "The results show that the models provide clear improvement over the use of a mean time as a predictor. Most of the improvement is, however, captured by the baseline model."

### Pelánek 2015 (2)

Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x

`q2 · i?` · `design · r2`

Same cross-validated RMSE evaluation over real tutor data: the learning extension scored slightly worse RMSE than the basic model; "the model with more parameters slightly overfits the data". Fine-tuned gradient descent later improved some problems.

> "The model with learning even leads to slightly worse results than the basic model – on the current dataset the model with more parameters slightly overfits the data."

## Discussion


## Related Claims
- [Keystroke-feature regression models fail to predict final writing grade at any point during the writing process](keystroke-regression-does-not-beat-grade-baseline.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)](keystroke-classification-weak-auc.md) — related
