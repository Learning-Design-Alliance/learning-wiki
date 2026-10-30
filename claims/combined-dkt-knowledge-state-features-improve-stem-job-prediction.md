---
type: claim
title: Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.
description: Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.
id: combined-dkt-knowledge-state-features-improve-stem-job-prediction
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

# Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Test results show models trained with DKT or DKT+ knowledge states, alone or combined with the student profile, generally perform better than models trained with the student profile alone. [→ Yeung 2018](#yeung-2018)

## Evidence

### Yeung 2018

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i?` · `associational · r1`

Cross-validation experiment comparing five feature sets (student profile, DKT, DKT+, and combined) across GBDT, LDA, LR and SVM classifiers, reported in Section 5.1 and Tables 2–3. The authors state that "the models trained with the DKT or DKT+ knowledge state, as well as the combined features, result in a higher performance than the models trained with the student profile alone."

> "Generally, the models trained with the DKT or DKT+ knowledge state, as well as the combined features, result in a higher performance than the models trained with the student proﬁle alone."

## Discussion


## Related Claims
- [LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.](lda-projection-knowledge-state-separates-classes-better-than-profile.md) — related
- [Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.](rfe-mitigates-overfitting-in-stem-job-prediction.md) — related
- [DKT+ knowledge states discriminate STEM from non-STEM students better than DKT knowledge states for the majority of mathematical skills.](dkt-plus-knowledge-state-better-discrimination-than-dkt.md) — related
- [STEM students show a higher mastery level and a higher learning gain in mathematics than non-STEM students.](stem-students-higher-mastery-and-learning-gain-in-mathematics.md) — related
