---
type: claim
title: Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity
description: Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity
id: data-balancing-improves-accuracy-increases-bias
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
    i: 3
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

# Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Models trained on the balanced dataset showed significant performance improvements with large effect sizes (larger than 0.80) on each metric at each stage. [→ Alison Cheng 2025](#alison-cheng-2025)
`q2 i?` Training on the balanced dataset produced a significant increase in bias under Demog_Parity_Diffs (p-value < 0.005) at all stages, showing balancing alone does not mitigate bias. [→ Alison Cheng 2025 (2)](#alison-cheng-2025-2)

## Evidence

### Alison Cheng 2025

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i3` · `design · r2`

Comparison of models trained on RandomOverSampler-balanced versus imbalanced datasets across three stages and four metrics. The article reports "a large Cohen’s d for each metric at each stage (i.e., larger than 0.80)", i.e., Cohen's d larger than 0.80.

> "Apart from the significant differences in performance under most metrics, we also found a large Cohen’s d for each metric at each stage (i.e., larger than 0.80), indicating strong effect sizes."

### Alison Cheng 2025 (2)

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Fairness comparison between models trained on balanced and imbalanced datasets showed "a significant increase in bias under the Demog_Parity_Diffs (p-value < 0.005) metric for all stages", with other metrics showing non-significant increases in bias.

> "Table 3 shows a significant increase in bias under the Demog_Parity_Diffs (p-value < 0.005) metric for all stages."

## Discussion


## Related Claims
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](no-significant-performance-gain-later-stages.md) — related
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](learning-activity-data-reduces-demographic-bias.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
