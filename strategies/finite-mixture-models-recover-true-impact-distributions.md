---
type: strategy
id: finite-mixture-models-recover-true-impact-distributions
title: Use finite mixture models to attempt recovery of the distribution of true site-specific impacts from estimates contaminated by normal sampling error
description: "As forward-looking work, the author reports that \"finite mixture models (FMM) may hold promise\" for separating the distribution of true site-specific impacts from normal sampling errors."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
sources:
  - id: henry-may-2014
    resource: "https://eric.ed.gov/?id=ED562702"
    title: "Henry May. (2014). Distortions in Distributions of Impact Estimates in Multi-Site Trials: The Central Limit Theorem is Not Your Friend. SREE Fall 2014 Conference. https://eric.ed.gov/?id=ED562702"
    author: Henry May
---

# Use finite mixture models to attempt recovery of the distribution of true site-specific impacts from estimates contaminated by normal sampling error

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
As forward-looking work, the author reports that "finite mixture models (FMM) may hold promise" for separating the distribution of true site-specific impacts from normal sampling errors. The approach exploits the fact that each observed estimate is the sum of points from two distributions, one of which (the error distribution) is normal with known mean and variance, which may allow recovery of the unknown distribution of true treatment effects.

## Design Implications

### Context
#### Requirements
- The typical FMM parameterization must be adapted because each data point is a sum of points from two distinct distributions rather than an observation from one distribution
#### Constraints
- The article presents this as exploratory future work between now and the fall SREE conference, not as a validated method

### Target Learners
- researchers analyzing multi-site randomized trials of educational interventions

### Target Learning Goals
- accurate estimation of cross-site variation in program impacts on learning outcomes

## Claims

- [Random effects HLM models produce an unbiased estimate of the variance of true site-specific impacts regardless of the shape of the true distribution](../claims/hlm-unbiased-variance-true-impacts.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Henry May. (2014). Distortions in Distributions of Impact Estimates in Multi-Site Trials: The Central Limit Theorem is Not Your Friend. SREE Fall 2014 Conference. https://eric.ed.gov/?id=ED562702
