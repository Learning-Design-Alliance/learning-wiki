---
type: strategy
id: fit-a-fix-one-parameter-alternative-to-dirichlet-priors
title: Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM
description: Because the HMM form of BKT is a three-parameter exponential, the article recommends fitting only the combination A and then recovering the fourth parameter algebraically.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: brett-van-de-sande-2013
    resource: "https://doi.org/10.5281/zenodo.3554629"
    title: "Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, 5(2). https://doi.org/10.5281/zenodo.3554629"
    author: "Van de Sande, B."
---

# Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because the HMM form of BKT is a three-parameter exponential, the article recommends fitting only the combination A and then recovering the fourth parameter algebraically. If P(G) or P(L0) is needed as output, the article suggests finding A by the fitting process, fixing P(G) or P(L0) by some external constraint, and using Eqn. (6) to find the remaining variable. This is presented as an alternative to the Dirichlet priors approach that is much easier to implement and does not modify the model itself.

## Design Implications

### Context
#### Requirements
- A fitting procedure (RSS or maximum likelihood) over the reduced three-parameter form
- An external constraint to fix either P(G) or P(L0)
#### Constraints
- Applies to the hidden Markov model form of BKT, not to the Knowledge Tracing Algorithm form, which needs all four parameters

### Target Learners
- researchers fitting BKT models to student performance data

### Target Learning Goals
- accurate and stable estimation of BKT model parameters from student data

## Related Strategies

- [Initialize BKT parameters from simulated student data when no human data is available](initialize-bkt-parameters-from-simulated-data.md)

## Examples
-

## Key Sources
- Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, 5(2). https://doi.org/10.5281/zenodo.3554629 <!-- corrected 2026-10-05: was the JEDM homepage; DataCite (Zenodo) DOI verified -->
