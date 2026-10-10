---
type: claim
title: "CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)"
description: "CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)"
id: catboost-best-performing-risk-classifier
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: gomathy-ramaswami-2023
    resource: "https://doi.org/10.18608/jla.2023.7935"
    title: "Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani. (2023). Effectiveness of a Learning Analytics Dashboard for Increasing Student Engagement Levels. Journal of Learning Analytics, 10(3). https://doi.org/10.18608/jla.2023.7935"
    author: Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` CatBoost outperformed k-nearest neighbours, Naïve Bayes, logistic regression, and random forest on F-measure, accuracy, and AUC in a modified 10-fold cross-validation across seven courses. [→ Gomathy Ramaswami 2023](#gomathy-ramaswami-2023)

## Evidence

### Gomathy Ramaswami 2023

Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani. (2023). Effectiveness of a Learning Analytics Dashboard for Increasing Student Engagement Levels. Journal of Learning Analytics, 10(3). https://doi.org/10.18608/jla.2023.7935

`q2 · i?` · `causal · r1`

Model evaluation using a modified k-fold cross-validation training on nine course deliveries and testing on the hold-out course, repeated 10 times. CatBoost scored F-measure .77±.02, accuracy 78±2.1%, AUC .87±.02, the highest among the five algorithms compared in Table 2.

> "Given that CatBoost achieved the highest scores, the models from this algorithm were selected to identify the at-risk students and to display its outputs on the dashboard."

## Discussion


## Related Claims
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96](gradient-boosting-best-enrollment-predictor-aid-optimization.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset](simple-classifiers-beat-tree-based-cheating-risk.md) — reports the opposite
