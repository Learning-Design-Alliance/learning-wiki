---
type: strategy
id: propensity-score-matching-selection-bias
title: Use propensity-score matching to minimize selection bias when randomized control groups are unavailable
description: Propensity-score matching is a type of nonrandomized study that can minimize selection bias and estimate treatment effects on outcomes by matching students inside the treatment group with doppelgangers in a comparator...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: jim-greer-mary-mark-2015
    resource: "https://doi.org/10.1007/s40593-015-0043-2"
    title: "Jim Greer & Mary Mark. (2015). Evaluation Methods for Intelligent Tutoring Systems Revisited. Int J Artif Intell Educ 26:387–392. https://doi.org/10.1007/s40593-015-0043-2"
    author: "Jim Greer & Mary Mark"
---

# Use propensity-score matching to minimize selection bias when randomized control groups are unavailable

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 causal), `q2`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Propensity-score matching is a type of nonrandomized study that can minimize selection bias and estimate treatment effects on outcomes by matching students inside the treatment group with doppelgangers in a comparator group. Only corresponding students with a high degree of similarity on relevant variables should be paired. The authors note it "has been only recently applied in the evaluation of learning environments, in particular in studying MOOCs".

## Design Implications

### Context
#### Requirements
- A comparator group much larger than the treatment group so a representative set of comparators can be identified as the control
- Pairing only students with high similarity on relevant variables
#### Constraints
- Recently applied only, particularly in MOOC contexts where large subject groups and big data make well-matched comparators feasible

### Target Learners
- learners in quasi-experimental studies of learning environments, e.g. MOOC participants

### Target Learning Goals
- estimating effects of educational interventions despite selection bias

## Claims

- [Propensity score matching produced baseline-equivalent treatment and comparison groups on all measured variables](../claims/psm-baseline-equivalence-mtss-study.md) [+W]
- [Propensity score analysis estimated a Texas generalizability index of 0.91, and post-stratification yielded a population average treatment effect of 1.47 versus a conventional estimate of 1.44](../claims/propensity-score-population-treatment-effect.md) [+W]

## Related Strategies

- [Use propensity score matching with ATT estimation to reduce selection bias when comparing childcare arrangements in longitudinal administrative data](propensity-matching-childcare-arrangement-comparison.md)
- [Match statistical control methods to variable structure and measurement quality, preferring stratification, covariate adjustment, matching, or regression discontinuity accordingly](statistical-control-method-selection-strategy.md)
- [Use prospective longitudinal designs with propensity score equating on comprehensive baseline covariates to estimate causal effects of early grade retention](prospective-propensity-design-retention-effects.md)

## Examples
-

## Key Sources
- Jim Greer & Mary Mark. (2015). Evaluation Methods for Intelligent Tutoring Systems Revisited. Int J Artif Intell Educ 26:387–392. https://doi.org/10.1007/s40593-015-0043-2
