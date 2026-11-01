---
type: research-method
id: pwrd-aggregation-power-maximizing-weighting-for-repeated-measurements-with-delayed-effects
title: "PWRD aggregation: power-maximizing weighting for repeated measurements with delayed effects"
description: PWRD (power-maximizing weighting for repeated measurements with delayed effects) aggregation is a statistical scheme for randomized trials and quasi-experiments with longitudinal data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-01
---

# PWRD aggregation: power-maximizing weighting for repeated measurements with delayed effects

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
PWRD (power-maximizing weighting for repeated measurements with delayed effects) aggregation is a statistical scheme for randomized trials and quasi-experiments with longitudinal data. It computes separate ITT effect estimates for each cohort-year of follow-up and combines them with weights proportional to expected effect size and estimate precision: "the 'signal-to-noise' ratio of test statistics centered around ^Dagg will be maximized by weights proportional both to the expected sizes of cohort-year effects, p, and also to the relative precisions of estimated cohort-year effects, R". Expected effect sizes come from the proportion of students eligible for supplemental instruction, derived from the intervention's theory of change. The method maintains the intention-to-treat perspective and is designed for hypothesis testing, usable alongside standard estimation.

## Accounts
<!-- How each source describes or uses the method -->
- **PWRD aggregation: a method converting an intervention's theory of change into power-maximizing weights for aggregating cohort-year ITT effect estimates**: PWRD (power-maximizing weighting for repeated measurements with delayed effects) aggregation is a statistical scheme for randomized trials and quasi-experiments with longitudinal data. It computes separate ITT effect estimates for each cohort-year of follow-up and combines them with weights proportional to expected effect size and estimate precision: "the 'signal-to-noise' ratio of test statistics centered around ^Dagg will be maximized by weights proportional both to the expected sizes of cohort-year effects, p, and also to the relative precisions of estimated cohort-year effects, R". Expected effect sizes come from the proportion of students eligible for supplemental instruction, derived from the intervention's theory of change. The method maintains the intention-to-treat perspective and is designed for hypothesis testing, usable alongside standard estimation. (Timothy Lycurgus et al. (2022))

### Claims

- [In simulations where the theory of change holds, PWRD aggregation outperforms standard analysis methods, with a 35-50% power increase for medium effect sizes](../claims/pwrd-increases-power-when-theory-holds.md) [+M]
- [Under within-cluster interference (a negative spillover effect on non-eligible treatment students), PWRD aggregation's power advantage over traditional methods grows, roughly doubling power for large effect sizes](../claims/pwrd-advantage-under-spillover.md) [+W]
- [When the theory of change entirely fails (effects neither stacked nor persistent), standard methods outperform PWRD aggregation but the improvement never exceeds 3%](../claims/pwrd-small-loss-when-theory-fails.md) [~W]

## Related Research Methods

- [Design-based RCT analysis with grouped administrative data](design-based-rct-analysis-with-grouped-administrative-data.md)

## Key Sources
- Timothy Lycurgus, Ben B. Hansen, and Mark White. (2022). Conjuring Power from a Theory of Change: The PWRD Method for Trials with Anticipated Variation in Effects. Journal of Research on Educational Effectiveness. https://doi.org/10.1080/19345747.2022.2142178
