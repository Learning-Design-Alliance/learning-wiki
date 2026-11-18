---
type: claim
title: Mediation analysis estimates that hint availability lowers the CTA1 treatment effect, with an average indirect effect of -0.04 standard deviations
description: Mediation analysis estimates that hint availability lowers the CTA1 treatment effect, with an average indirect effect of -0.04 standard deviations
id: mediation-indirect-hint-effect-negative
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

# Mediation analysis estimates that hint availability lowers the CTA1 treatment effect, with an average indirect effect of -0.04 standard deviations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Assuming matched ignorability, the estimated average indirect effect of CTA1 through hint requesting is -0.04 (SE 0.02), implying CTA1 works despite rather than because of hints; no standardized effect-size statistic is printed, so no effect size is coded. [→ Adam C Sales and John F Pane 2018](#adam-c-sales-and-john-f-pane-2018)

## Evidence

### Adam C Sales and John F Pane 2018

Adam C Sales and John F Pane. (2018). Student Log-Data from a Randomized Evaluation of Educational Technology: A Causal Case Study. [doi:10.48550/arXiv.1808.02528](https://doi.org/10.48550/arXiv.1808.02528)

`q2 · i?` · `causal · r2`

Causal mediation analysis using matching-based imputation of Y(1,0) for treated high hint users; the article prints "an average indirect eﬀect of -0.04, with a standard error of 0.02," derived from the TOT estimate of -0.14 times the 0.30 proportion of high hint users. No standardized effect-size statistic is printed.

> "In Table 2, we estimated the TOT as -0.14 with a standard error of 0.06. That implies an average indirect eﬀect of -0.04, with a standard error of 0.02."

## Discussion


## Related Claims
- [In a matched observational study within the CTA1 trial, being a high hint user is associated with posttest scores around 0.15 standard deviations lower](high-hint-users-lower-posttest-observational.md) — related
- [The estimated direct effect of CTA1 assignment holding hint usage at control levels is 0.18 standard deviations when covariate-adjusted, with confidence intervals crossing zero](mediation-direct-effect-cta1.md) — related
- [Principal stratification finds students with higher latent hint-requesting proclivity may have experienced larger CTA1 treatment effects, contradicting the other two analyses](principal-stratification-hint-proclivity-larger-effects.md) — reports the opposite
- [Sensitivity analysis shows the negative hint-usage estimate is vulnerable to an unmeasured confounder as predictive as pretest, though not one as predictive as ethnicity](hint-effect-sensitivity-unmeasured-confounding.md) — related
