---
type: claim
title: The ML-LVM yields lower parameter bias and higher coverage rates for regression weights predicting learning outcomes than the PS two-step method
description: The ML-LVM yields lower parameter bias and higher coverage rates for regression weights predicting learning outcomes than the PS two-step method
id: ml-lvm-outcome-regression-bias-coverage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
evidence_strength: moderate
sources:
  - id: julian-f-lohmann-2025
    resource: "https://doi.org/10.1007/s10648-025-10029-z"
    title: "Julian F. Lohmann, Nils Machts, Jens Möller, Steffen Zitzmann. (2025). A More Comprehensive, More Reliable Multilevel Approach for Assessing and Modeling Teacher Judgment Accuracy Using Latent Variables. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10029-z"
    author: Julian F. Lohmann, Nils Machts, Jens Möller, Steffen Zitzmann
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The ML-LVM yields lower parameter bias and higher coverage rates for regression weights predicting learning outcomes than the PS two-step method

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In simulation study 3, regression weights relating judgment accuracy components to learning outcomes showed smaller bias for the ML-LVM in almost all conditions, and the PS method showed consistently smaller 95% confidence-interval coverage rates. [→ Julian F. Lohmann 2025](#julian-f-lohmann-2025)

## Evidence

### Julian F. Lohmann 2025

Julian F. Lohmann, Nils Machts, Jens Möller, Steffen Zitzmann. (2025). A More Comprehensive, More Reliable Multilevel Approach for Assessing and Modeling Teacher Judgment Accuracy Using Latent Variables. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10029-z

`q2 · i?` · `design · r2`

Simulation study 3 simulated three outcome variables each strongly predicted by one component (β = 0.5) under four sample-size conditions, comparing ML-LVM and PS regression estimates on bias, RMSE, and coverage. The article reports "the two-step PS method showed consistently smaller coverage rates" and that PS regression weights were strongly underestimated (bias consistently above ± 10% and negative).

> "As assumed, the two-step PS method showed consistently smaller coverage rates indicating that the true values of the simulated regression weights were less frequently included in the model-implied 95% confidence intervals than for the ML-LVM."

## Discussion


## Related Claims
- [The ML-LVM yields higher true-positive rates for detecting moderation effects of judgment accuracy components than the PS method across most conditions](ml-lvm-higher-moderation-power.md) — related
- [The ML-LVM provides more accurate individual-level estimates of judgment accuracy components than the person-score (PS) two-step method](ml-lvm-more-accurate-individual-level-estimates.md) — related
- [The PS method shows systematic overestimation of the differentiation component that exceeds the 10% bias threshold in small and medium level-1 samples](ps-method-differentiation-overestimation.md) — related
- [Unilevel OLS regression and four-level multilevel analysis of the same content analysis data yield differing p-values, especially for parameters that are not highly significant.](ols-versus-multilevel-p-values-differ.md) — related
