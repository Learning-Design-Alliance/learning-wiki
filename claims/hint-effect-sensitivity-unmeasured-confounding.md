---
type: claim
title: Sensitivity analysis shows the negative hint-usage estimate is vulnerable to an unmeasured confounder as predictive as pretest, though not one as predictive as ethnicity
description: Sensitivity analysis shows the negative hint-usage estimate is vulnerable to an unmeasured confounder as predictive as pretest, though not one as predictive as ethnicity
id: hint-effect-sensitivity-unmeasured-confounding
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

# Sensitivity analysis shows the negative hint-usage estimate is vulnerable to an unmeasured confounder as predictive as pretest, though not one as predictive as ethnicity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under a Hosman et al. sensitivity analysis, allowing for an omitted covariate as important as pretest yields intervals including both large negative and substantial positive effects; allowing one as important as ethnicity leaves the OLS-weighted interval entirely negative. [→ Adam C Sales and John F Pane 2018](#adam-c-sales-and-john-f-pane-2018)

## Evidence

### Adam C Sales and John F Pane 2018

Adam C Sales and John F Pane. (2018). Student Log-Data from a Randomized Evaluation of Educational Technology: A Causal Case Study. [doi:10.48550/arXiv.1808.02528](https://doi.org/10.48550/arXiv.1808.02528)

`q2 · i?` · `causal · r2`

Sensitivity analysis of the matched observational study using the Hosman et al. (2010) method; the ethnicity-benchmarked OLS sensitivity interval was [-0.30,-0.05], while pretest-benchmarked intervals were much wider.

> "Allowing for the possible omission of such a covariate, the results suggest that requesting a large number of hints hurts students’ posttest scores. The size of the eﬀect may be as small as 5% of a standard deviation or as large as 30% of a standard deviation."

## Discussion


## Related Claims
- [Reassignment appears to lower posttest scores, though the effect varies substantially between classrooms and is sensitive to omitted covariates](reassignment-lowers-posttest-scores.md) — related
- [The estimated direct effect of CTA1 assignment holding hint usage at control levels is 0.18 standard deviations when covariate-adjusted, with confidence intervals crossing zero](mediation-direct-effect-cta1.md) — related
- [Mediation analysis estimates that hint availability lowers the CTA1 treatment effect, with an average indirect effect of -0.04 standard deviations](mediation-indirect-hint-effect-negative.md) — related
- [In a matched observational study within the CTA1 trial, being a high hint user is associated with posttest scores around 0.15 standard deviations lower](high-hint-users-lower-posttest-observational.md) — related
