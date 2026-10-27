---
type: claim
title: Machine learning models predict MOOC certificate purchasing with accuracies of 0.82–0.91 using only time spent on each course step
description: Machine learning models predict MOOC certificate purchasing with accuracies of 0.82–0.91 using only time spent on each course step
id: ml-predicts-mooc-purchase-time-spent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: alshehri-2021
    resource: "https://doi.org/10.1007/s40593-021-00246-2"
    title: "Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D. (2021). Towards Designing Profitable Courses: Predicting Student Purchasing Behaviour in MOOCs. International Journal of Artificial Intelligence in Education, 31, 215–233. https://doi.org/10.1007/s40593-021-00246-2"
    author: "Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Machine learning models predict MOOC certificate purchasing with accuracies of 0.82–0.91 using only time spent on each course step

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Four ML algorithms (RandomForest, GradientBoosting, AdaBoost, XGBoost) predicted course purchasability from step-level time-spent features with accuracies between 0.82 and 0.91. [→ Alshehri 2021](#alshehri-2021)

## Evidence

### Alshehri 2021

Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D. (2021). Towards Designing Profitable Courses: Predicting Student Purchasing Behaviour in MOOCs. International Journal of Artificial Intelligence in Education, 31, 215–233. https://doi.org/10.1007/s40593-021-00246-2

`q2 · i?` · `associational · r2`

Predictive modelling study on FutureLearn clickstream data from 23 runs of 5 University of Warwick courses, evaluating four algorithms with train/test split and 10-fold cross validation. The authors report "promising accuracies, between 0.82 and 0.91" using time spent per step alone; no effect size is printed.

> "Our proposed model achieved promising accuracies, between 0.82 and 0.91, using the time spent on each step only."

## Discussion


## Related Claims
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — reports the opposite
- [MOOC certificate purchasing is rare: under 1% of enrolled learners purchase, with completion around 10%](mooc-purchase-rate-under-one-percent.md) — related
- [The run number (delivery iteration) is among the most representative features for predicting MOOC purchasing behaviour](run-number-top-purchase-predictor.md) — related
