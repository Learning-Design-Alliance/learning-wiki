---
type: claim
title: Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques
description: Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques
id: cpp-postprocessing-accuracy-fairness-tradeoff
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

# Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The CPP method exhibited significant drops in balanced accuracy coupled with higher EOD values, particularly for age, IMD, and disability attributes. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `causal · r2`

Accuracy-fairness trade-off analysis of LR models with four mitigation techniques on OULAD, plotted as BAcc versus EOD per demographic attribute (Figure 7). The article reports CPP "exhibited significant drops in accuracy" for age, IMD, and disability. No effect size is printed.

> "While some bias mitigation techniques, such as DIR and RW, improved fairness metrics (EOD) while maintaining relatively high balanced accuracy (BAcc), others, like CPP, exhibited significant drops in accuracy coupled with higher EOD values."

## Discussion


## Related Claims
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
