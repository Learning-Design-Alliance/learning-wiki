---
type: claim
title: "In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range"
description: "In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range"
id: cta1-effect-decreases-with-mastery-propensity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2017
sources:
  - id: adam-c-sales-2017
    resource: "https://doi.org/10.48550/arXiv.1707.09308"
    title: "Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)"
    author: Adam C. Sales, and John F Pane
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A difference of one IQR in latent mastery propensity ηT was associated with a reduction of 0.083 in the treatment effect size (posterior SD 0.066; 95% credible interval [-0.212, 0.045]; slope negative in about 89% of MCMC runs). [→ Adam C. Sales 2017](#adam-c-sales-2017)

## Evidence

### Adam C. Sales 2017

Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)

`q2 · i?` · `causal · r2`

Bayesian latent principal stratification analysis of log data from the randomized CTA1 high school trial (year two, n = 5308). The posterior mean slope for τ(ηT) was negative: "a reduction of 0.083 in the eﬀect size" per IQR of ηT, with posterior SD 0.066. No standardized effect size is printed.

> "Specifically, a diﬀerence of one IQR in ηT was associated with a reduction of 0.083 in the eﬀect size with a posterior standard deviation of 0.066."

## Discussion


## Related Claims
- [Students with higher pretest scores, who are white or Asian, male, or gifted are more likely to master worked CTA1 sections; covariates explain about 39% of variance in mastery propensity](covariates-predict-cta1-mastery-propensity.md) — related
- [The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)](mbar-confounded-eta-not.md) — related
- [Latent mastery propensity ηT correlates positively with post-test scores in both treatment and control groups, with a slightly lower slope in the treatment group](eta-positive-with-posttest-both-groups.md) — related
