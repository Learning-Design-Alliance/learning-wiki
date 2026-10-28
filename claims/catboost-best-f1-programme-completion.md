---
type: claim
title: CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest
description: CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest
id: catboost-best-f1-programme-completion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: teo-susnjak-2024
    resource: "https://doi.org/10.1007/s40593-023-00336-3"
    title: "Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3"
    author: Teo Susnjak
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across eight machine learning algorithms plus two baselines, CatBoost achieved the highest estimated generalisability F1-measure (94.5±0.6) on an unbalanced dataset of 14918 data points, slightly better than Random Forest (93.9±0.6). [→ Teo Susnjak 2024](#teo-susnjak-2024)

## Evidence

### Teo Susnjak 2024

Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3

`q2 · i?` · `design · r2`

Empirical model comparison (Step 3) on a real-world dataset of 14918 data points from ~7000 learners, evaluated with 10-fold cross-validation using F1-measure due to the unbalanced target variable. CatBoost reached F1 94.5±0.6, Accuracy 92.0±0.7, AUC 88.3±0.6. The authors note the advantage "can arguably be attributed to its inherent ability to handle both missing values and categorical data directly."

> "On average, the best-performing algorithm for this dataset is CatBoost, which is slightly better than Random Forest. Some of the performance advantages of CB can arguably be attributed to its inherent ability to handle both missing values and categorical data directly"

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — reports the opposite
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — reports the opposite
