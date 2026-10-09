---
type: claim
title: Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information
description: Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information
id: learning-activity-data-reduces-demographic-bias
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
---

# Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Models using learning activity data alongside demographics showed reduced potential bias from overreliance on demographic information, as seen in Stage 1 fairness levels. [→ Alison Cheng 2025](#alison-cheng-2025)

## Evidence

### Alison Cheng 2025

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Across the three-stage analysis of models trained on data from 215 AP Statistics students, the article reports that "incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information", with Stage 1 showing the least bias.

> "We discovered that incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information."

## Discussion


## Related Claims
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects](demographic-predictors-reduce-actionability.md) — a broader claim this one bears on
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](no-significant-performance-gain-later-stages.md) — related
- [Using demographic variables as predictors risks reinforcing biases embedded in training labels, including self-fulfilling prophecies](demographic-predictors-reinforce-training-label-bias.md) — a broader claim this one bears on
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
