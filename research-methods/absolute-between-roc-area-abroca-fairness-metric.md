---
type: research-method
id: absolute-between-roc-area-abroca-fairness-metric
title: Absolute Between-ROC Area (ABROCA) fairness metric
description: ABROCA is a fairness metric proposed by Gardner et al.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Absolute Between-ROC Area (ABROCA) fairness metric

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
ABROCA is a fairness metric proposed by Gardner et al. (2019) and adopted by several reviewed studies. "This metric measures the absolute value of the area between the baseline group ROC curve ROCb and the comparison group(s) ROCc. The lower the ABROCA value, the less unfair the algorithm." Unlike threshold-dependent metrics such as equalized odds, ABROCA evaluates model discrimination across all thresholds and can be computed directly from prediction modeling results with minimal computational requirement.

## Accounts
<!-- How each source describes or uses the method -->
- **ABROCA: Absolute Between-ROC Area fairness metric**: ABROCA is a fairness metric proposed by Gardner et al. (2019) and adopted by several reviewed studies. "This metric measures the absolute value of the area between the baseline group ROC curve ROCb and the comparison group(s) ROCc. The lower the ABROCA value, the less unfair the algorithm." Unlike threshold-dependent metrics such as equalized odds, ABROCA evaluates model discrimination across all thresholds and can be computed directly from prediction modeling results with minimal computational requirement. (Jamiu Adekunle Idowu (2024))

### Claims

- [Education algorithm fairness is measured with a diverse set of metrics, most commonly ABROCA, TPR/TNR, FPR/FNR disparity metrics, and group difference in performance](../claims/education-fairness-metrics-diverse-set.md) [+W]

## Related Research Methods
-

## Key Sources
- Jamiu Adekunle Idowu. (2024). Debiasing Education Algorithms. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00389-4
