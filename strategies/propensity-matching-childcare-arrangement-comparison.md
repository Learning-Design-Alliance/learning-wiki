---
type: strategy
id: propensity-matching-childcare-arrangement-comparison
title: Use propensity score matching with ATT estimation to reduce selection bias when comparing childcare arrangements in longitudinal administrative data
description: The article compares formal vs informal childcare by matching treated (formal) with untreated (informal) children on child, maternal/family and demographic covariates using kernel matching, then estimating the average...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
sources:
  - id: garon-carrier-2022
    resource: "https://doi.org/10.1016/j.learninstruc.2022.101615"
    title: "Garon-Carrier, G., Ansari, A., Letarte, M.-J., & Fitzpatrick, C. (2022). Early childcare enrollment and the pursuit of higher education: A Canadian longitudinal study. Learning and Instruction, 80. https://doi.org/10.1016/j.learninstruc.2022.101615"
    author: "Garon-Carrier, G., Ansari, A., Letarte, M.-J., & Fitzpatrick, C"
---

# Use propensity score matching with ATT estimation to reduce selection bias when comparing childcare arrangements in longitudinal administrative data

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article compares formal vs informal childcare by matching treated (formal) with untreated (informal) children on child, maternal/family and demographic covariates using kernel matching, then estimating the average treatment effect for the treated (ATT) on odds of higher education enrollment. The authors chose ATT because it "relaxes the conditional independence assumption" and "relaxes the overlap assumption" relative to ATE. Balancing tests confirmed post-matching covariate balance.

## Design Implications

### Context
#### Requirements
- Observed covariates covering child, maternal/family and demographic confounders
- Linked administrative outcome data (tax records for enrollment)
#### Constraints
- Cannot rule out selection on unmeasured confounders; childcare quality characteristics were unavailable in the database

### Target Learners
- Children in early childcare (24–36 months) and their families

### Target Learning Goals
- Predicting long-term educational attainment from early care arrangements

## Claims

- [Propensity score matching produced baseline-equivalent treatment and comparison groups on all measured variables](../claims/psm-baseline-equivalence-mtss-study.md) [+W]

## Related Strategies

- [Match statistical control methods to variable structure and measurement quality, preferring stratification, covariate adjustment, matching, or regression discontinuity accordingly](statistical-control-method-selection-strategy.md)

## Examples
-

## Key Sources
- Garon-Carrier, G., Ansari, A., Letarte, M.-J., & Fitzpatrick, C. (2022). Early childcare enrollment and the pursuit of higher education: A Canadian longitudinal study. Learning and Instruction, 80. https://doi.org/10.1016/j.learninstruc.2022.101615
