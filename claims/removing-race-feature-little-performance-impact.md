---
type: claim
title: Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects
description: Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects
id: removing-race-feature-little-performance-impact
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: mixed
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

# Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Removing race from the balanced dataset produced only a slight, non-significant drop in model performance at Stage 1, with small effect sizes. [→ Alison Cheng 2025](#alison-cheng-2025)
`q2 i?` At Stage 1, no significant fairness differences were observed after removing race, with slight bias decreases on three metrics but a slight increase on Eq_Opp_Diffs. [→ Alison Cheng 2025 (2)](#alison-cheng-2025-2)

## Evidence

### Alison Cheng 2025

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Comparison of mitigated models before and after removing race at Stage 1 showed slight drops on most metrics, e.g., Balanced Accuracy (t-statistics = –0.196, Cohen's d = 0.139), indicating "removing race had little impact on predictive performance at Stage 1".

> "The relatively sma ll effect siz e indicates that removing race had little impact on predictive performance at Stage 1."

### Alison Cheng 2025 (2)

Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761

`q2 · i?` · `design · r2`

Fairness comparison after removing race showed "no significant differences are observed on bias level at Stage 1" (p-value > 0.05), with slight decreases in bias for Demog_Parity_Diffs, Avg_Odds_Diffs, and PPDs, but a slight increase for Eq_Opp_Diffs.

> "Compared with Figure 6(b), no significant differences are observed on bias level at Stage 1."

## Discussion


## Related Claims
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](learning-activity-data-reduces-demographic-bias.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction](mixed-evidence-demographic-predictor-performance.md) — a broader claim this one bears on
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
