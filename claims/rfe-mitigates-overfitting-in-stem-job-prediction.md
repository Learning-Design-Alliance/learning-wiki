---
type: claim
title: "Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE."
description: "Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE."
id: rfe-mitigates-overfitting-in-stem-job-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: yeung-2018
    resource: "https://arxiv.org/abs/1806.03256"
    title: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256"
    author: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Applying RFE to reduce feature dimensionality improves model performance, and after RFE the LR-DKT&SP model performs best on all evaluation measures (AP 0.458, AUC 0.694, combined score 1.280, RMSE 0.414). [→ Yeung 2018](#yeung-2018)

## Evidence

### Yeung 2018

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i?` · `associational · r1`

Dimensionality-reduction experiments using PCA, RFE and oversampling (Section 5.1, Table 3). The authors report "the RFE process is the most effective for relieving the overfitting issue", and after RFE, LR-DKT&SP's test AP, AUC and combined score rise from 0.341 to 0.458, 0.582 to 0.694 and 1.141 to 1.280 respectively, with RMSE reduced from 0.442 to 0.414.

> "Among all the attempted methods, the RFE process is the most eﬀective for relieving the overﬁtting issue and improving the model performance."

## Discussion


## Related Claims
- [Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.](combined-dkt-knowledge-state-features-improve-stem-job-prediction.md) — related
- [LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.](lda-projection-knowledge-state-separates-classes-better-than-profile.md) — related
- [The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.](overfitting-from-small-labeled-set-and-high-dimensionality.md) — related
