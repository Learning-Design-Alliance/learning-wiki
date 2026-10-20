---
type: claim
title: Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups
description: Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups
id: baseline-ml-models-biased-tpr-oulad
status: review
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
    kind: design
    rigour: 2
---

# Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A baseline logistic-regression classifier trained on OULAD showed unequal true-positive rates across gender, age, IMD, and disability subgroups, indicating disparate impact; the authors say the same holds for standard models such as XGBoost but show subgroup rates only for LR. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `design · r2`

Baseline LR and XGBoost classifiers were trained on OULAD (25,690 students); group-specific TPRs are shown in Figure 6 for the LR classifiers only (baseline and bias-mitigated), with Tukey's range tests for pairwise TPR/FPR differences. The discussion says standard approaches "such as LR and XGBoost, can exhibit biased performance", but no subgroup TPRs are shown for XGBoost. The article reports "unequal true positive rates (TPRs)" across subgroups. No effect size is printed.

> "The plots reveal biases in the baseline classifier performance across different subgroups. As evident from the varying prevalence rates and unequal true positive rates (TPRs). These biases suggest disparate impact based on factors such as sex, age, index of multiple deprivation and disability."

## Discussion


## Related Claims
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
