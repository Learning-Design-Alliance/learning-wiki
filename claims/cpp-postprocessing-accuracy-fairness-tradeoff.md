---
type: claim
title: Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction
description: Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction
id: cpp-postprocessing-accuracy-fairness-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-20
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

# Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The CPP method showed lower balanced accuracy coupled with higher EOD for the age and IMD attributes, and the largest disparity for disability, where balanced accuracy and EOD varied widely across techniques. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `causal · r2`

Accuracy-fairness trade-off analysis of LR models with four mitigation techniques on OULAD, plotted as BAcc versus EOD per demographic attribute (Figure 7). The article reports that CPP showed lower accuracy and higher EOD for age and IMD ("a significant drop in accuracy coupled with a higher EOD" for IMD), and the largest disparity for disability, where it does not separately describe the accuracy and EOD values. These are readings of the Figure 7 plot; no test of the trade-off and no effect size is printed for them.

> "While some bias mitigation techniques, such as DIR and RW, improved fairness metrics (EOD) while maintaining relatively high balanced accuracy (BAcc), others, like CPP, exhibited significant drops in accuracy coupled with higher EOD values."

## Discussion


## Related Claims
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — a broader claim this one bears on
