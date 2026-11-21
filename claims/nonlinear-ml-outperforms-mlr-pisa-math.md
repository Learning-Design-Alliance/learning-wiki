---
type: claim
title: Non-linear ML models (RF, CatBoost, ANN) consistently outperform multiple linear regression in predicting PISA 2018 math scores across ten countries
description: Non-linear ML models (RF, CatBoost, ANN) consistently outperform multiple linear regression in predicting PISA 2018 math scores across ten countries
id: nonlinear-ml-outperforms-mlr-pisa-math
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: liu-liu-2026
    resource: "https://doi.org/10.1186/s40536-026-00320-y"
    title: "Liu Liu, Rui Dai. (2026). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. Originally published 2025. [doi:10.1186/s40536-026-00320-y](https://doi.org/10.1186/s40536-026-00320-y)"
    author: Liu Liu, Rui Dai
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: liu-liu-2026-2
    resource: "https://doi.org/10.1186/s40536-026-00320-y"
    title: "Liu Liu, Rui Dai. (2026). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. Originally published 2025. [doi:10.1186/s40536-026-00320-y](https://doi.org/10.1186/s40536-026-00320-y)"
    author: Liu Liu, Rui Dai
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Non-linear ML models (RF, CatBoost, ANN) consistently outperform multiple linear regression in predicting PISA 2018 math scores across ten countries

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random Forest, CatBoost, and ANN each outperformed the MLR baseline on held-out test data in every country studied. [→ Liu Liu 2026](#liu-liu-2026)
`q2 i?` Random Forest achieved the highest test R² in a majority of countries, explaining about 38% of variance in Hungary, Japan, and the Philippines versus about 17–29% for MLR. [→ Liu Liu 2026 (2)](#liu-liu-2026-2)

## Evidence

### Liu Liu 2026

Liu Liu, Rui Dai. (2026). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. Originally published 2025. [doi:10.1186/s40536-026-00320-y](https://doi.org/10.1186/s40536-026-00320-y)

`q2 · i?` · `associational · r2`

Held-out test-set evaluation (70/30 stratified by country) of four models on PISA 2018 math data for 67,329 students in ten countries, assessed with R² and MAE. The article reports the non-linear models "consistently outperformed" MLR; no formal significance tests were conducted.

> "Overall, the non-linear ML models – Random Forest, CatBoost, and the Artificial Neural Network – consistently outperformed the linear baseline model (MLR) in predicting mathematics scores."

### Liu Liu 2026 (2)

Liu Liu, Rui Dai. (2026). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. Originally published 2025. [doi:10.1186/s40536-026-00320-y](https://doi.org/10.1186/s40536-026-00320-y)

`q2 · i?` · `associational · r2`

Country-level test results (Table 2) show RF "achieved the highest test 𝑅2 values in a majority of countries"; the text adds RF explained about 38% of variance in Hungary, Japan, and the Philippines versus about 17–29% for MLR.

> "Among the ML models, Random Forest (RF) achieved the highest test 𝑅2 values in a majority of countries."

## Discussion


## Related Claims
- [Visual diagnostics show CatBoost predictions align tightly with actual scores, with regression-to-the-mean errors at the score extremes, while ANN predictions show greater scatter](catboost-hexbin-tight-alignment-tail-errors.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
