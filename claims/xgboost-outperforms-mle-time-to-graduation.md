---
type: claim
title: Gradient boosted trees (xgboost) outperform maximum-likelihood logistic regression at predicting graduating semester by out-of-sample F1-score, except in semesters 15-16
description: Gradient boosted trees (xgboost) outperform maximum-likelihood logistic regression at predicting graduating semester by out-of-sample F1-score, except in semesters 15-16
id: xgboost-outperforms-mle-time-to-graduation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: aiken-2020
    resource: "https://doi.org/10.1371/journal.pone.0242334"
    title: "Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)"
    author: Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Gradient boosted trees (xgboost) outperform maximum-likelihood logistic regression at predicting graduating semester by out-of-sample F1-score, except in semesters 15-16

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The xgboost model achieves higher out-of-sample F1-scores than logistic regression for semesters 5-14, with logistic regression slightly better in semesters 15-16. [→ Aiken 2020](#aiken-2020)

## Evidence

### Aiken 2020

Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)

`q2 · i?` · `associational · r2`

Out-of-sample evaluation of discrete-time hazard models on registrar data, with data split 50/50 into student-level training and test sets and F1 thresholds tuned on training data. The article reports xgboost "generally more effective than the logistic regression model except in the last semesters (15-16)"; no effect size is printed.

> "The xgboost model is generally more effective than the logistic regression model except in the last semesters (15-16) studied as assessed by the out-of-sample F1-score (Fig. 5)."

## Discussion


## Related Claims
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — a broader claim this one bears on
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91](xgboost-logreg-highest-f1-midterm-risk-prediction.md) — related
- [Xgboost more accurately predicts graduating semesters for female students, under-represented minority students, and students with missing high school GPA than logistic regression](xgboost-subgroup-recall-advantage.md) — a narrower finding that bears on this claim
- [Enrollment factors predict time-to-graduation about twice as strongly as preparation factors](enrollment-factors-outweigh-preparation-graduation-timing.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Statistical model choice affects both predictability and understanding of educational systems when sub-population data are unequal, per prior gradient-boosted time-to-graduation work](model-choice-subpopulation-understanding.md) — possibly the same claim (merge candidate)
