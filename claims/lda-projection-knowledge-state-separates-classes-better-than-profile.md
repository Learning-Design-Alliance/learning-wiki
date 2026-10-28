---
type: claim
title: LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.
description: LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.
id: lda-projection-knowledge-state-separates-classes-better-than-profile
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2018
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

# LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` LDA-projected histograms show the student profile largely overlaps between classes, while DKT or DKT+ knowledge states result in a better separation between STEM and non-STEM classes. [→ Yeung 2018](#yeung-2018)

## Evidence

### Yeung 2018

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i?` · `associational · r1`

Supervised LDA projection of student profile and DKT/DKT+ knowledge states into one dimension, visualized as histograms in Figure 2 (Section 5.2.1). The authors report "using the knowledge state obtained in the DKT or DKT+ models results in a better separation between STEM and non-STEM classes".

> "On the other hand, using the knowledge state obtained in the DKT or DKT+ models re-sults in a better separation between STEM and non-STEM classes, implying that the student’s knowledge state in math-ematics provides a rudimentary diﬀerentiation on whether a student is likely to pursue a career in the STEM ﬁeld."

## Discussion


## Related Claims
- [Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.](combined-dkt-knowledge-state-features-improve-stem-job-prediction.md) — related
- [DKT+ knowledge states discriminate STEM from non-STEM students better than DKT knowledge states for the majority of mathematical skills.](dkt-plus-knowledge-state-better-discrimination-than-dkt.md) — related
- [Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.](rfe-mitigates-overfitting-in-stem-job-prediction.md) — related
