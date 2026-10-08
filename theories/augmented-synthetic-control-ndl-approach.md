---
type: theory
title: Augmented synthetic control method for estimating counterfactual outcomes of no-deadlines programs
description: "The memo applies the augmented synthetic control method (Ben-Michael, Feller, and Rothstein 2021a), which the article says uses \"a specifically weighted average of comparison units for which the pre-implementation out..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: fesler-2022
    resource: "https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future"
    title: "Fesler, Lily and Lindsay Fox. (2022). No-deadlines Synthetic Control and Exploratory Outcomes Analysis and Recommendations for a Future Rigorous Evaluation [Memorandum]. Alexandria, VA: National Science Foundation. https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future"
    author: Fesler, Lily and Lindsay Fox
---

# Augmented synthetic control method for estimating counterfactual outcomes of no-deadlines programs

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The memo applies the augmented synthetic control method (Ben-Michael, Feller, and Rothstein 2021a), which the article says uses "a specifically weighted average of comparison units for which the pre-implementation outcome trends match those of the treated units." Weighted comparison-unit outcomes in post-implementation periods estimate the treated units' counterfactuals. Ridge regression generates weights, and the other focal outcomes are included as covariates. Comparison programs are restricted to the same directorate so directorate-wide changes affect both treated and comparison programs.

## Design Implications

### Context
#### Requirements
- Enough pre- and post-treatment data for each cohort (the memo requires at least six years pre- and three years post-implementation) and enough comparison units
- Comparison programs in the same directorate as the NDL program
#### Constraints
- The memo states its data include six to nine pre-intervention years and three to seven comparison programs, both smaller than typical synthetic control studies, creating risks of poor counterfactuals and overfitting
- Programs switching to NDL mid-fiscal-year were removed

### Target Learners
- NSF program officers and evaluation staff

### Target Learning Objectives
- Estimating impacts of no-deadlines submission policies on proposal volume, quality, reviewer burden, collaboration, and requested funding

### Claims
- [Synthetic Control Poor Fit Bio Few Comparisons](../claims/synthetic-control-poor-fit-bio-few-comparisons.md) [~M]
- [Ndl Reduced Proposal Volume Geo Exploratory](../claims/ndl-reduced-proposal-volume-geo-exploratory.md) [+M]

## Related Theories
- 

## Examples

- [Design considerations for a future rigorous evaluation of no-deadlines approaches](../strategies/future-rigorous-ndl-evaluation-considerations.md)

## Key Sources
- Fesler, Lily and Lindsay Fox. (2022). No-deadlines Synthetic Control and Exploratory Outcomes Analysis and Recommendations for a Future Rigorous Evaluation [Memorandum]. Alexandria, VA: National Science Foundation. https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future
