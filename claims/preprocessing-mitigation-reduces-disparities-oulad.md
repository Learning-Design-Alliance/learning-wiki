---
type: claim
title: Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute
description: Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute
id: preprocessing-mitigation-reduces-disparities-oulad
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-15
recheck_by: 2028
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

# Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-15 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
<!-- title before 2026-10-15: Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy -->

## Subclaims
`q2 i?` Applying DIR, RW, and SUP reduced disparities in true positive rates (lower EOD), but effectiveness varied by attribute: DIR succeeded for gender, age and disability, SUP was particularly effective for IMD, and DIR and RW kept balanced accuracy relatively high; no statistical test of the accuracy change is reported. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `causal · r2`

Comparative analysis of bias mitigation techniques applied to LR models on OULAD, comparing fairness metrics (EOD) and balanced accuracy before and after mitigation (Figures 6-7). The article reports "decreased EOD values", with effectiveness varying by attribute: "DIR showed considerable success in mitigating biases related to gender, age, and disability, SUP was particularly effective in addressing socioeconomic disparities captured by the IMD." Balanced accuracy hovered around 0.78 for gender; for age and disability it varied widely across techniques, and DIR and RW maintained "relatively high balanced accuracy". Accuracy comparisons are read from figures, with no statistical test. No effect size is printed.

> "The application of methods such as DIR, RW, and SUP effectively reduced disparities in TPRs across demographic subgroups, as evidenced by the decreased EOD values. The effectiveness of these techniques varied across key demographic attributes, highlighting the need for context-specific approaches to algorithmic fairness."

## Discussion

## Related Claims

- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](ews-and-algorithm-less-accurate-black-students.md) — the general claim this finding bears on, with the studies behind it
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
- [Bias in predicting learning productivity, measured as accuracy differences across gender and parental educational background, was highly dependent on the ML method used](bias-dependent-on-ml-method.md) — related
