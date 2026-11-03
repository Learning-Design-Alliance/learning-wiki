---
type: strategy
id: iptw-six-step-procedure
title: Six-step procedure for applying inverse probability of treatment weighting to reduce selection bias in survey data
description: "The article lays out an implementable workflow for IPTW with large-scale survey data: \"(a) select covariates for the PS model, (b) estimate PSs, (c) check the overlap assumption and examine the overlap of PSs across g..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-02
sources:
  - id: crystal-d-bishop-2018
    resource: "https://doi.org/10.1177/1053815118793430"
    title: "Crystal D. Bishop, Walter L. Leite, and Patricia A. Snyder. (2018). Using Propensity Score Weighting to Reduce Selection Bias in Large-Scale Data Sets. Journal of Early Intervention. https://doi.org/10.1177/1053815118793430"
    author: Crystal D. Bishop, Walter L. Leite, and Patricia A. Snyder
---

# Six-step procedure for applying inverse probability of treatment weighting to reduce selection bias in survey data

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article lays out an implementable workflow for IPTW with large-scale survey data: "(a) select covariates for the PS model, (b) estimate PSs, (c) check the overlap assumption and examine the overlap of PSs across groups, (d) calculate inverse probability of treatment weights, (e) check for extreme weights, and (f) assess balance of covariates across the two treatment groups." Steps were implemented in R, with balance evaluated using standardized mean differences against What Works Clearinghouse standards.

## Design Implications

### Context
#### Requirements
- Inclusion of appropriate observed baseline covariates (potential and true confounders) in the PS model
- Checking covariate balance after applying the method, revising the PS model with interactions or nonlinear terms if balance is inadequate
#### Constraints
- The approach assumes no unmeasured true confounders, which the article says is unlikely to be met in practice
- It is aimed only at reducing selection bias; other validity threats must be controlled separately

### Target Learners
- researchers conducting secondary analyses of large-scale early intervention and early childhood survey data

### Target Learning Goals
- reducing selection bias to estimate plausible causal treatment effects from nonexperimental survey data

### Affordances
- Rubin Potential Outcomes Framework Ate Att

## Claims

- [Inverse-probability weights for attrition, non-consent, and non-response improved validity only to the extent the missing-data assumptions held](../claims/attrition-nonresponse-weights-validity.md) [~W]
- [Unmatched comparisons suggested increasingly aggressive NCLB treatment groups had higher mean PI gains, but these advantages mostly disappeared after matching, indicating selection bias](../claims/unmatched-gains-disappear-after-matching.md) [+W]

## Related Strategies

- [Use propensity score matching with ATT estimation to reduce selection bias when comparing childcare arrangements in longitudinal administrative data](propensity-matching-childcare-arrangement-comparison.md)

## Examples
-

## Key Sources
- Crystal D. Bishop, Walter L. Leite, and Patricia A. Snyder. (2018). Using Propensity Score Weighting to Reduce Selection Bias in Large-Scale Data Sets. Journal of Early Intervention. https://doi.org/10.1177/1053815118793430
