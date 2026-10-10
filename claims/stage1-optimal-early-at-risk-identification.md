---
type: claim
title: Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness
description: Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness
id: stage1-optimal-early-at-risk-identification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: alison-cheng-2025
    resource: "https://doi.org/10.18608/jla.2025.8761"
    title: "Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761"
    author: Alison Cheng, Bo Pei and Cheng Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alison-cheng-2025-2
    resource: "https://doi.org/10.18608/jla.2025.8761"
    title: "Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761"
    author: Alison Cheng, Bo Pei and Cheng Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Models at Stage 1 showed the least bias on average, with all fairness values below the 0.20 threshold, and comparable predictive performance to later stages. [→ Alison Cheng 2025](#alison-cheng-2025)
`q2 i?` Early predictions at Stage 1 achieved accuracy similar to predictions using more data at later stages, making it the optimal identification point. [→ Alison Cheng 2025 (2)](#alison-cheng-2025-2)

## Evidence

### Alison Cheng 2025

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Analysis of four ML models trained on data from 215 AP Statistics students, evaluated with four fairness metrics across three stages. The article reports "the models at Stage 1 have the least bias, on average" with all values under 0.20.

> "Notably, the models at Stage 1 have the least bias, on average, compared to the Demog Stage and Stage 2 , with all values falling below the 0.20 threshold ."

### Alison Cheng 2025 (2)

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Comparison of model performance across stages on the imbalanced dataset showed Stage 1 predictions achieved "similar levels of accuracy to those using more data at a later stage", supporting Stage 1 as the optimal identification point.

> "In addition, the models at Stage 1 also have a comp arable performance with that of Stage 2 and the Demog Stage, which means that early predictions can achieve similar levels of accuracy to those using more data at a later stage."

## Discussion


## Related Claims
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](no-significant-performance-gain-later-stages.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](learning-activity-data-reduces-demographic-bias.md) — related
- [Achievement gap estimates are widely used to measure the effectiveness and fairness of the education system, so their accuracy and unbiasedness are necessary for appropriate conclusions](gap-estimates-accuracy-necessary-for-conclusions.md) — related
- [Stakeholder groups converged on recommendations for timelier results, removal of racial and cultural bias, and more useful, accessible results](stakeholder-recommendations-timely-unbiased-accessible-results.md) — related
