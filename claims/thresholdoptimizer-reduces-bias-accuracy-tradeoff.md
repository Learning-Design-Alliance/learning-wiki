---
type: claim
title: Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop
description: Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop
id: thresholdoptimizer-reduces-bias-accuracy-tradeoff
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

# Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Applying ThresholdOptimizer produced a significant decrease in Demog_Parity_Diffs bias at all stages (p-value < 0.005) with very large effect sizes, but increased PPDs bias. [→ Alison Cheng 2025](#alison-cheng-2025)
`q2 i?` Post-processing mitigation involved a trade-off: improving predictive fairness across groups might compromise some prediction accuracy. [→ Alison Cheng 2025 (2)](#alison-cheng-2025-2)

## Evidence

### Alison Cheng 2025

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i3` · `design · r2`

Comparison of mitigated versus unmitigated models on the balanced dataset across three stages. The article reports "a significant decrease in bias level on Demog_Parity_Diffs" with very large effect sizes (Cohen's d = 4.510, 5.753, 5.839), while PPDs bias increased across stages.

> "a significant decrease in bias level on Demog_Parity_Diffs has been observed at all stages  (p-value < 0.005), with very large effect size at the Demog Stage (Cohen’s d = 4.510), Stage 1 (Cohen’s d = 5.753), and Stage 2 (Cohen’s d = 5.839)."

### Alison Cheng 2025 (2)

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

After applying ThresholdOptimizer, the article observed "a slight drop in performance on some metrics (e.g., Precision, Accuracy) at the Demog Stage and Stage 1", indicating a fairness–accuracy trade-off.

> "This suggests a trade-off between predictive performance and fairness level — improving predictive fairness across groups might compromise some prediction accuracy, which is particularly relevant when the model predictions have a high reliance on demographic information."

## Discussion


## Related Claims
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
