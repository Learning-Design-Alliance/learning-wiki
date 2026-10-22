---
type: research-method
id: multilevel-latent-variable-model-ml-lvm-of-judgment-accuracy
title: Multilevel latent variable model (ML-LVM) of judgment accuracy
description: "The article introduces the ML-LVM, in which each rater's judgments are modeled with a rater-specific bivariate normal distribution whose mean, variance, and covariance parameters correspond to the level, differentiation, and rank components of judgment accuracy."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-22
---

# Multilevel latent variable model (ML-LVM) of judgment accuracy

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article introduces the ML-LVM, in which each rater's judgments are modeled with a rater-specific bivariate normal distribution whose mean, variance, and covariance parameters correspond to the level, differentiation, and rank components of judgment accuracy. The three components follow a multivariate normal distribution across raters, so the model yields both population-level means and variances quantifying between-rater differences. The authors note that in a traditional two-step approach, person-specific scores 'are calculated in the first stage for each teacher separately and then treated as observed variables in subsequent analyses,' which the ML-LVM avoids by accounting for sampling error from a limited number of judgments. Estimation uses Bayesian MCMC in Stan.

## Accounts
<!-- How each source describes or uses the method -->
- **A multilevel latent variable model (ML-LVM) of judgment accuracy that represents rank, level, and differentiation components as raters' latent abilities**: The article introduces the ML-LVM, in which each rater's judgments are modeled with a rater-specific bivariate normal distribution whose mean, variance, and covariance parameters correspond to the level, differentiation, and rank components of judgment accuracy. The three components follow a multivariate normal distribution across raters, so the model yields both population-level means and variances quantifying between-rater differences. The authors note that in a traditional two-step approach, person-specific scores 'are calculated in the first stage for each teacher separately and then treated as observed variables in subsequent analyses,' which the ML-LVM avoids by accounting for sampling error from a limited number of judgments. Estimation uses Bayesian MCMC in Stan. (Julian F. Lohmann et al. (2025))

### Claims

- [The ML-LVM provides more accurate individual-level estimates of judgment accuracy components than the person-score (PS) two-step method](../claims/ml-lvm-more-accurate-individual-level-estimates.md) [+W]
- [The ML-LVM yields lower parameter bias and higher coverage rates for regression weights predicting learning outcomes than the PS two-step method](../claims/ml-lvm-outcome-regression-bias-coverage.md) [+W]
- [The ML-LVM yields higher true-positive rates for detecting moderation effects of judgment accuracy components than the PS method across most conditions](../claims/ml-lvm-higher-moderation-power.md) [+W]
- [The PS method shows systematic overestimation of the differentiation component that exceeds the 10% bias threshold in small and medium level-1 samples](../claims/ps-method-differentiation-overestimation.md) [+W]

## Related Research Methods

- [Multilevel latent covariate model for unbiased estimation of class-level climate–outcome relations](multilevel-latent-covariate-model-for-unbiased-estimation-of-class-level-climateoutcome-re.md)

## Key Sources
- Julian F. Lohmann, Nils Machts, Jens Möller, Steffen Zitzmann. (2025). A More Comprehensive, More Reliable Multilevel Approach for Assessing and Modeling Teacher Judgment Accuracy Using Latent Variables. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10029-z
