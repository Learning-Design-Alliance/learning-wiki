---
type: claim
title: The ensemble learner attains the highest classification accuracy and AUC for predicting a non-repeatable grade (C or better)
description: The ensemble learner attains the highest classification accuracy and AUC for predicting a non-repeatable grade (C or better)
id: ensemble-highest-classification-nonrepeatable-grade
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: beemer-2018
    resource: "https://doi.org/10.1007/s40593-017-0148-x"
    title: "Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A. (2018). Ensemble Learning for Estimating Individualized Treatment Effects in Student Success Studies. International Journal of Artificial Intelligence in Education, 28, 315–335. https://doi.org/10.1007/s40593-017-0148-x"
    author: "Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The ensemble learner attains the highest classification accuracy and AUC for predicting a non-repeatable grade (C or better)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For the binary 'C' or better outcome, the averaged-probability ensemble with a 0.77 threshold achieved the highest accuracy (80.52%) and AUC (0.82) among the learners compared. [→ Beemer 2018](#beemer-2018)

## Evidence

### Beemer 2018

Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A. (2018). Ensemble Learning for Estimating Individualized Treatment Effects in Student Success Studies. International Journal of Artificial Intelligence in Education, 28, 315–335. https://doi.org/10.1007/s40593-017-0148-x

`q2 · i?` · `associational · r2`

Classification comparison for the non-repeatable grade outcome using an averaged-probability ensemble with an 'optimal' threshold of 0.77 from the OptimalCutpoints package. Table 2 reports ensemble accuracy of 80.52% and AUC 0.82, and ROC curves in Fig. 2 show the ensemble "has the highest classification success".

> "Under this threshold, the ensemble learner has the highest classification success. Figure 2 presents ROC curves for the ensemble learner and the individual learners."

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — reports the opposite
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Optimal ensemble threshold value is 0.7, with accuracy declining beyond it](ensemble-threshold-0-7-optimal.md) — reports the opposite
