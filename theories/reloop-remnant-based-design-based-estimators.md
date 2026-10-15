---
type: theory
title: "ReLOOP/ReLOOP+: design-based causal estimators combining remnant-trained imputations with leave-one-out covariate adjustment"
description: "ReLOOP and ReLOOP+ are covariate-adjusted A/B test effect estimators that train an outcome-prediction model on 'remnant' users who were not randomized, generate predictions for experimental participants, and use those..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: adam-c-sales-2023
    resource: "https://osf.io/k8ph9/"
    title: "Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/"
    author: Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan
---

# ReLOOP/ReLOOP+: design-based causal estimators combining remnant-trained imputations with leave-one-out covariate adjustment

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
ReLOOP and ReLOOP+ are covariate-adjusted A/B test effect estimators that train an outcome-prediction model on 'remnant' users who were not randomized, generate predictions for experimental participants, and use those predictions as covariates in the LOOP leave-one-out estimator. ReLOOP adjusts only for remnant-based imputations via an OLS within-sample model; ReLOOP+ uses an ensemble of OLS and random forests to adjust for both imputations and within-sample covariates. The article states: "These estimators are design-based, exactly unbiased for the τRCT , give conservative standard error estimates, and make no modeling assumptions, beyond the design of the experiment itself." Unbiasedness holds regardless of imputation-model quality because treatment assignment is randomized and model parameters are estimated from separate samples.

## Design Implications

### Context
#### Requirements
- Bernoulli randomization with known assignment probability p
- Covariate and outcome data available for remnant users
- Leave-one-out sample splitting so imputation predictions are independent of treatment assignment
#### Constraints
- The article notes the naive remnant estimator can be biased if the remnant is unrepresentative or predictions biased, which rebar/LOOP correction addresses
- Conservative variance estimates may under-reject, giving confidence intervals that include the true parameter too often

### Target Learners
- students using online learning platforms participating in A/B tests

### Target Learning Objectives
- accurate, precise estimation of causal effects of educational conditions from platform experiments

### Claims


## Related Theories
- 

## Examples
-

## Key Sources
- Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/
