---
type: claim
title: The estimated direct effect of CTA1 assignment holding hint usage at control levels is 0.18 standard deviations when covariate-adjusted, with confidence intervals crossing zero
description: The estimated direct effect of CTA1 assignment holding hint usage at control levels is 0.18 standard deviations when covariate-adjusted, with confidence intervals crossing zero
id: mediation-direct-effect-cta1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2018
sources:
  - id: adam-c-sales-and-john-f-pane-2018
    resource: "https://doi.org/10.48550/arXiv.1808.02528"
    title: "Adam C Sales and John F Pane. (2018). Student Log-Data from a Randomized Evaluation of Educational Technology: A Causal Case Study. [doi:10.48550/arXiv.1808.02528](https://doi.org/10.48550/arXiv.1808.02528)"
    author: Adam C Sales and John F Pane
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The estimated direct effect of CTA1 assignment holding hint usage at control levels is 0.18 standard deviations when covariate-adjusted, with confidence intervals crossing zero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Regression estimation of the average direct effect E[ξ(0)] gave 0.14 (CI [-0.10,0.39]) unadjusted and 0.18 (CI [-0.03,0.39]) with covariates, both with confidence intervals crossing zero; no standardized effect size is printed for these estimates. [→ Adam C Sales and John F Pane 2018](#adam-c-sales-and-john-f-pane-2018)

## Evidence

### Adam C Sales and John F Pane 2018

Adam C Sales and John F Pane. (2018). Student Log-Data from a Randomized Evaluation of Educational Technology: A Causal Case Study. [doi:10.48550/arXiv.1808.02528](https://doi.org/10.48550/arXiv.1808.02528)

`q2 · i?` · `causal · r2`

OLS regression with school-level cluster-robust standard errors on 5,026 students (2,108 treatment, 2,918 control), estimating the effect of CTA1 assignment with hint usage held at H=0; the article prints "a direct eﬀect of 0.18±0.21" covariate-adjusted, with intervals including zero.

> "Using the clubSandwich package in R [Pustejovsky, 2018] to estimate standard errors, and 95% conﬁdence intervals, we estimated a direct eﬀect of 0.14±0.25. Adding covariates to the regression (6) estimates a direct eﬀect of 0.18±0.21."

## Discussion


## Related Claims
- [In a matched observational study within the CTA1 trial, being a high hint user is associated with posttest scores around 0.15 standard deviations lower](high-hint-users-lower-posttest-observational.md) — related
- [Mediation analysis estimates that hint availability lowers the CTA1 treatment effect, with an average indirect effect of -0.04 standard deviations](mediation-indirect-hint-effect-negative.md) — related
- [Sensitivity analysis shows the negative hint-usage estimate is vulnerable to an unmeasured confounder as predictive as pretest, though not one as predictive as ethnicity](hint-effect-sensitivity-unmeasured-confounding.md) — related
- [In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range](cta1-effect-decreases-with-mastery-propensity.md) — related
- [Principal stratification finds students with higher latent hint-requesting proclivity may have experienced larger CTA1 treatment effects, contradicting the other two analyses](principal-stratification-hint-proclivity-larger-effects.md) — related
- [A latent state-trait model with unmeasured persistent factors reproduces the exponential decay of experimental treatment effects that regression models miss](state-trait-model-reproduces-experimental-decay.md) — related
