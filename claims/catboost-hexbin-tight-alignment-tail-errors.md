---
type: claim
title: Visual diagnostics show CatBoost predictions align tightly with actual scores, with regression-to-the-mean errors at the score extremes, while ANN predictions show greater scatter
description: Visual diagnostics show CatBoost predictions align tightly with actual scores, with regression-to-the-mean errors at the score extremes, while ANN predictions show greater scatter
id: catboost-hexbin-tight-alignment-tail-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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
---

# Visual diagnostics show CatBoost predictions align tightly with actual scores, with regression-to-the-mean errors at the score extremes, while ANN predictions show greater scatter

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` CatBoost underpredicted the very top scores and overpredicted the very low scores, and its predictions were more tightly packed around the diagonal than the ANN's. [→ Liu Liu 2026](#liu-liu-2026)

## Evidence

### Liu Liu 2026

Liu Liu, Rui Dai. (2026). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. Originally published 2025. [doi:10.1186/s40536-026-00320-y](https://doi.org/10.1186/s40536-026-00320-y)

`q2 · i?` · `associational · r2`

Hexagonal bin scatterplots of predicted vs. actual scores (Supplementary Figure A3; Figure 6 for Argentina). The article reports the tail tendency above and that the ANN's point cloud was more spread out around the diagonal than CatBoost's.

> "We observed a slight tendency for CatBoost to underpredict the very top scores and overpredict the very low scores"

## Discussion


## Related Claims
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [Non-linear ML models (RF, CatBoost, ANN) consistently outperform multiple linear regression in predicting PISA 2018 math scores across ten countries](nonlinear-ml-outperforms-mlr-pisa-math.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
