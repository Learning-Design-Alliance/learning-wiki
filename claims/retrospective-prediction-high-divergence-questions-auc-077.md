---
type: claim
title: Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing
description: Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing
id: retrospective-prediction-high-divergence-questions-auc-077
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: yubo-li-2026
    resource: "https://arxiv.org/abs/2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Gradient boosting on question and observed-coverage features achieves test AUC 0.774 and average precision 0.570 for predicting top-quartile divergence among 441 questions. [→ Yubo Li 2026](#yubo-li-2026)

## Evidence

### Yubo Li 2026

Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606

`q2 · i?` · `associational · r2`

Retrospective predictive analysis on one stratified 75/25 question-level split (seed 42) of the audited corpus, restricted to 441 questions with at least 30 non-absent pairs, of which 113 fall in the top divergence quartile. The article states there is no external-center or prospective validation.

> "gradient boosting achieves test AUC 0.774 and average precision 0.570; logistic regression achieves 0.763 and 0.541."

## Discussion


## Related Claims
- [Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96](gradient-boosting-best-enrollment-predictor-aid-optimization.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset](simple-classifiers-beat-tree-based-cheating-risk.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries](pattern-detector-high-precision-low-coverage.md) — related
