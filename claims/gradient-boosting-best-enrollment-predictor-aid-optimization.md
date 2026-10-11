---
type: claim
title: Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96
description: Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96
id: gradient-boosting-best-enrollment-predictor-aid-optimization
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: vinhthuy-phan-2022
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609"
    title: "Vinhthuy Phan, Laura Wright, Bridgette Decent. (2022). Optimizing Financial Aid Allocation to Improve Access and Affordability to Higher Education. Journal of Educational Data Mining, Volume 14, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609"
    author: Vinhthuy Phan, Laura Wright, Bridgette Decent
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Among six popular classifiers compared with cross-validation, gradient boosting and XGB tied for the highest performance across balanced accuracy, F-score and AUC, and all classifiers beat the baselines. [→ Vinhthuy Phan 2022](#vinhthuy-phan-2022)

## Evidence

### Vinhthuy Phan 2022

Vinhthuy Phan, Laura Wright, Bridgette Decent. (2022). Optimizing Financial Aid Allocation to Improve Access and Affordability to Higher Education. Journal of Educational Data Mining, Volume 14, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609

`q2 · i?` · `design · r2`

Comparison of six optimized classifiers on 7,564 Fall 2020 FAFSA-filing first-time freshmen applicants (2,340 enrolled), using 10-fold cross validation. Table 1 reports gradient boosting and XGB at balanced accuracy 0.91, F-score 0.88, AUC 0.96, versus 0.50 for both baselines; the article states "All classifiers performed significantly better than the two baselines."

> "Gradient Boosting (Schapire, 2013) and Extreme Gradient Boosting (Chen and Guestrin, 2016) had the same highest performance across all three metrics (balanced accuracy, F-score, and AUC)."

## Discussion


## Related Claims
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Applicants' enrollment decisions depend most on 'other financing sources' (typically loans), with feature importance 0.712, far exceeding federal and institutional aid features](other-financing-sources-dominant-enrollment-feature.md) — related
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](college-offtrack-classified-90-percent-accuracy.md) — related
- [Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing](retrospective-prediction-high-divergence-questions-auc-077.md) — related
