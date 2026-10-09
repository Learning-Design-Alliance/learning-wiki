---
type: claim
title: Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy
description: Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy
id: preprocessing-mitigation-reduces-disparities-oulad
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: raymond-a-opoku-2025
    resource: "https://doi.org/10.18608/jla.2025.8543"
    title: "Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543"
    author: Raymond A. Opoku, Bo Pei and Wanli Xing
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Applying DIR, RW, and SUP decreased EOD values across demographic subgroups without significantly compromising balanced accuracy. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `causal · r2`

Comparative analysis of bias mitigation techniques applied to LR models on OULAD, comparing fairness metrics (EOD) and balanced accuracy before and after mitigation (Figures 6-7). The article reports "decreased EOD values" with accuracy around 0.78 for gender. No effect size is printed.

> "The application of methods such as DIR, RW, and SUP effectively reduced disparities in TPRs across demographic subgroups, as evidenced by the decreased EOD values. The effectiveness of these techniques varied across key demographic attributes, highlighting the need for context-specific approaches to algorithmic fairness."

## Discussion


## Related Claims
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
