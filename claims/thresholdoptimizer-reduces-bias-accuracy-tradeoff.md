---
type: claim
title: Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop
description: Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop
id: thresholdoptimizer-reduces-bias-accuracy-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-09
recheck_by: 2028
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
> **Currency** · newest study 2025 · checked against its sources 2026-10-09 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

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

- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](ews-and-algorithm-less-accurate-black-students.md) — the general claim this finding bears on, with the studies behind it
- [Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](stage1-optimal-early-at-risk-identification.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — a broader claim this one bears on
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](learning-activity-data-reduces-demographic-bias.md) — related
- [Education algorithm fairness is measured with a diverse set of metrics, most commonly ABROCA, TPR/TNR, FPR/FNR disparity metrics, and group difference in performance](education-fairness-metrics-diverse-set.md) — related
- [Most reviewed education-fairness studies found no strict tradeoff between fairness and accuracy](no-strict-fairness-accuracy-tradeoff.md) — related
