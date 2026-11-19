---
type: claim
title: Under time-varying treatment-confounder feedback, outcome regression is biased while IPTW yields unbiased estimates
description: Under time-varying treatment-confounder feedback, outcome regression is biased while IPTW yields unbiased estimates
id: iptw-unbiased-under-treatment-confounder-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: manie-tadayon-2021
    resource: "https://doi.org/10.48550/arXiv.2108.00654"
    title: "Manie Tadayon, Greg Pottie. (2021). Causal Inference in Educational Systems: A Graphical Modeling Approach. arXiv. [doi:10.48550/arXiv.2108.00654](https://doi.org/10.48550/arXiv.2108.00654)"
    author: Manie Tadayon, Greg Pottie
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Under time-varying treatment-confounder feedback, outcome regression is biased while IPTW yields unbiased estimates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a simulated feedback scenario, the outcome regression confidence intervals for X1, X2 and the intercept excluded the true values, whereas IPTW (marginal structural model) intervals contained them. [→ Manie Tadayon 2021](#manie-tadayon-2021)

## Evidence

### Manie Tadayon 2021

Manie Tadayon, Greg Pottie. (2021). Causal Inference in Educational Systems: A Graphical Modeling Approach. arXiv. [doi:10.48550/arXiv.2108.00654](https://doi.org/10.48550/arXiv.2108.00654)

`q2 · i?` · `theoretical · r3`

Simulation (N = 500) of a DAG with arrows from treatments back to confounders, comparing 95% confidence intervals from outcome regression and MSM(IPTW); e.g. the true intercept 2.13 fell outside the regression interval (4.92, 5.02) but inside the IPTW interval (1.910, 3.843).

> "According to this table, the outcome regression estimate is biased for the coefﬁcients ofX1,X2, and the intercept term, while IPTW estimates are unbiased for all the coefﬁcients."

## Discussion


## Related Claims
- [Stabilized IPTW achieved covariate balance on all variables, outperforming unstabilized IPTW, and was used for effect estimation](siptw-superior-balance-for-time-varying-treatment.md) — related
- [The Rothstein falsification test can reject value-added models even when estimated teacher effects are unbiased](rothstein-test-rejects-vams-without-bias.md) — related
