---
type: claim
title: "Unprincipled inclusion of covariates ('garbage-can regression') can introduce rather than remove bias"
description: "Unprincipled inclusion of covariates ('garbage-can regression') can introduce rather than remove bias"
id: garbage-can-regression-fallibility
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
sources:
  - id: weidlich-2024
    resource: "https://doi.org/10.1007/s11423-023-10241-0"
    title: "Weidlich, J., Hicks, B., & Drachsler, H. (2024). Causal reasoning with causal graphs in educational technology research. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10241-0"
    author: "Weidlich, J., Hicks, B., & Drachsler, H."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# Unprincipled inclusion of covariates ('garbage-can regression') can introduce rather than remove bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`

## Subclaims
`q1 i?` Indiscriminate covariate inclusion can block genuine causal pathways or open spurious ones, so covariate selection must be guided by the assumed causal graph rather than by availability. [→ Weidlich 2024](#weidlich-2024)

## Evidence

### Weidlich 2024

Weidlich, J., Hicks, B., & Drachsler, H. (2024). Causal reasoning with causal graphs in educational technology research. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10241-0

`q1 · i?` · `theoretical · r3`

Theoretical argument in the DAGS for analysis section: the paper criticizes the assumption that "controlling cannot do harm but only good", noting that covariates can lead to overcontrol or endogenous selection bias.

> "This unprincipled, overeager approach, sometimes called garbage-can regression (Achen, 2005), was already criticized by Meehl (1970), and its fallibility is apparent given the graphical causal inference framework presented here (Lee, 2012; Pearl, 2009;  Rohrer, 2018)."

## Discussion


## Related Claims
- [Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success](m-bias-gasevic-2016-lms-behaviour.md) — a narrower finding that bears on this claim
- [A low alpha for an error-prone covariate can attenuate, inflate, or artificially produce a spurious effect (phantom effect) in the coefficient of a perfectly reliable predictor](low-alpha-covariate-phantom-effect.md) — related
- [Student growth modeling and teacher value-added modeling are complex due to non-random assignment, measurement error, multidimensionality, and covariates](growth-value-added-modeling-complexity-sources.md) — related
- [For the DESI example, both approaches would show negative bias under the assumed data-generating model, so the observed positive coefficients make a positive true effect of teacher support likely, though its exact size remains inestimable](desi-revisited-positive-true-effect-likely-bias-negative.md) — related
