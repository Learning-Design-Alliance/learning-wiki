---
type: claim
title: Imputing missing predictor values without conditioning on the outcome variable biases estimates toward zero even when data are missing completely at random
description: Imputing missing predictor values without conditioning on the outcome variable biases estimates toward zero even when data are missing completely at random
id: imputation-omitting-outcome-biases-toward-zero
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: m-b-weissman-2021
    resource: "https://doi.org/10.48550/arXiv.2110.04266"
    title: "M. B. Weissman. (2021). Invalid Methods of Causal Inference in Physics Education Research. [doi:10.48550/arXiv.2110.04266](https://doi.org/10.48550/arXiv.2110.04266)"
    author: M. B. Weissman
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: m-b-weissman-2021-2
    resource: "https://doi.org/10.48550/arXiv.2110.04266"
    title: "M. B. Weissman. (2021). Invalid Methods of Causal Inference in Physics Education Research. [doi:10.48550/arXiv.2110.04266](https://doi.org/10.48550/arXiv.2110.04266)"
    author: M. B. Weissman
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Imputing missing predictor values without conditioning on the outcome variable biases estimates toward zero even when data are missing completely at random

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a bivariate-normal toy example with 25% of X missing completely at random, imputing missing X values solely from the distribution of X reduces the sample correlation to 0.75r, a bias toward zero, while conditioning on both X and Y yields an unbiased estimate r. [→ M. B. Weissman 2021](#m-b-weissman-2021)
`q2 i?` In multivariable regression, imputing a missing predictor conditioned only on the other predictors reduces the model's R2, so omitting outcome variables from the conditioning biases estimates to become less predictive. [→ M. B. Weissman 2021 (2)](#m-b-weissman-2021-2)

## Evidence

### M. B. Weissman 2021

M. B. Weissman. (2021). Invalid Methods of Causal Inference in Physics Education Research. [doi:10.48550/arXiv.2110.04266](https://doi.org/10.48550/arXiv.2110.04266)

`q2 · i?` · `theoretical · r3`

An analytical derivation assuming large-N bivariate normal variables X and Y with correlation r, with 25% of X values missing completely at random. The author shows algebraically that X-only imputation gives correlation 0.75r while conditioning on both X and Y recovers r.

> "Including them will be expected to reduce the correlation coefficient to 0.75r in the sample that includes imputed points, i.e. to give an estimate biased toward zero."

### M. B. Weissman 2021 (2)

M. B. Weissman. (2021). Invalid Methods of Causal Inference in Physics Education Research. [doi:10.48550/arXiv.2110.04266](https://doi.org/10.48550/arXiv.2110.04266)

`q2 · i?` · `theoretical · r3`

Extension of the derivation to several correlated predictors under multivariate normality and missing-completely-at-random assumptions. Linear-regression imputation conditioned on the outcome and other predictors preserves all covariances and does not bias coefficient estimates.

> "Thus omitting outcome variables from the conditioning biases estimates to become less predictive even in the simplest, least problematic cases."

## Discussion


## Related Claims
- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](mean-imputation-sufficient-auxiliary-model.md) — related
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](rct-only-all-covariates-hurt-precision.md) — related
