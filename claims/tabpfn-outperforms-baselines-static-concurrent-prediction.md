---
type: claim
title: In static concurrent prediction, TabPFN outperformed Random Forest, XGBoost and Linear Regression across the four emotional and proficiency targets
description: In static concurrent prediction, TabPFN outperformed Random Forest, XGBoost and Linear Regression across the four emotional and proficiency targets
id: tabpfn-outperforms-baselines-static-concurrent-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: peng-wang-2026
    resource: "https://doi.org/10.1007/s10648-026-10141-8"
    title: "Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8"
    author: Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# In static concurrent prediction, TabPFN outperformed Random Forest, XGBoost and Linear Regression across the four emotional and proficiency targets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Cross-validated comparison of four models showed TabPFN consistently outperformed Random Forest, XGBoost and Linear Regression, particularly for anxiety and boredom; the static TabPFN explained 65.1% of variance in enjoyment, 59.6% in boredom, 51.5% in self-perceived proficiency, and 45.8% in anxiety. [→ Peng Wang 2026](#peng-wang-2026)

## Evidence

### Peng Wang 2026

Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8

`q2 · i?` · `associational · r1`

Cross-validated static concurrent prediction (Fig. 2) comparing TabPFN, Random Forest, XGBoost and Linear Regression on identical feature sets; Linear Regression lagged notably behind, which the authors attribute to non-linear relationships.

> "Across all targets, TabPFN consistently outperformed the alternative models, particularly for more complex emotional states such as anxiety and boredom."

## Discussion


## Related Claims
- [Time-series forecasting with TabPFN-TS markedly improves prediction of next-episode emotions and perceived proficiency over a static model (e.g., anxiety R² 0.458→0.866; boredom 0.596→0.953)](tabpfn-ts-forecasting-l2-emotions-high-accuracy.md) — related
- [DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success](dmo-gru-lowest-regression-error-highest-r2.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
