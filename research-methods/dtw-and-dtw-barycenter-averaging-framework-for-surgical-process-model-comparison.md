---
type: research-method
id: dtw-and-dtw-barycenter-averaging-framework-for-surgical-process-model-comparison
title: DTW and DTW barycenter averaging framework for surgical process model comparison
description: "The framework quantifies surgery as a surgical process model (SPM), a time series of surgical feature parameters capturing motion and position of instruments, then aligns resident and expert SPMs with dynamic time warping (DTW), which \"can align the lengths of sequences while matching similar parts "
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
---

# DTW and DTW barycenter averaging framework for surgical process model comparison

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework quantifies surgery as a surgical process model (SPM), a time series of surgical feature parameters capturing motion and position of instruments, then aligns resident and expert SPMs with dynamic time warping (DTW), which "can align the lengths of sequences while matching similar parts so that two sequences with different lengths are best matched". Because DTW only makes one-to-one comparisons, DTW barycenter averaging (DBA) builds a standard expert model from multiple expert sequences. Comparing a resident SPM against this standard identifies portions whose average cost exceeds an empirically set threshold, automatically locating improvement points.

## Accounts
<!-- How each source describes or uses the method -->
- **Surgical process model comparison via DTW and DTW barycenter averaging as a framework for automatic detection of surgical improvement points**: The framework quantifies surgery as a surgical process model (SPM), a time series of surgical feature parameters capturing motion and position of instruments, then aligns resident and expert SPMs with dynamic time warping (DTW), which "can align the lengths of sequences while matching similar parts so that two sequences with different lengths are best matched". Because DTW only makes one-to-one comparisons, DTW barycenter averaging (DBA) builds a standard expert model from multiple expert sequences. Comparing a resident SPM against this standard identifies portions whose average cost exceeds an empirically set threshold, automatically locating improvement points. (Yamaguchi Tomoko et al. (2022))

### Claims
- [Surgeries performed by experts show significantly lower cost (difference) from the standard process model than surgeries performed by residents](../claims/expert-spm-cost-lower-than-residents.md) [+M]
- [Comparing resident SPMs with the standard expert model detects 303 improvable portions, classifiable into six error categories, most involving dangers](../claims/spm-detects-303-error-portions-six-categories.md) [+M]

## Related Research Methods
-

## Key Sources
- Yamaguchi Tomoko, Nakamura Ryoichi, Kuboki Akihito, Otori Nobuyoshi. (2022). Clinical study of skill assessment based on time sequential measurement changes. Scientific Reports. https://doi.org/10.1038/s41598-022-10502-7
