---
type: strategy
id: statistical-control-method-selection-strategy
title: Match statistical control methods to variable structure and measurement quality, preferring stratification, covariate adjustment, matching, or regression discontinuity accordingly
description: "The article outlines implementable options for blocking back-door paths when randomization is infeasible: group-specific (stratified) analyses, third-variable inclusion in regression, matching (noting nearest neighbou..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: weidlich-2022
    resource: "https://doi.org/10.18608/jla.2022.7577"
    title: "Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577"
    author: Weidlich, J., Gašević, D., Drachsler, H
---

# Match statistical control methods to variable structure and measurement quality, preferring stratification, covariate adjustment, matching, or regression discontinuity accordingly

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article outlines implementable options for blocking back-door paths when randomization is infeasible: group-specific (stratified) analyses, third-variable inclusion in regression, matching (noting nearest neighbour matching using Mahalanobis distance outperformed propensity score matching in one cited comparison), and regression discontinuity when treatment is assigned by a cutoff. Each method carries stated assumptions and drawbacks that researchers should weigh against their data structure.

## Design Implications

### Context
#### Requirements
- A putative confounding variable must be measured with high reliability for statistical control to reduce spurious association
#### Constraints
- Stratification works best for categorical variables and loses power with many strata; covariate adjustment assumes linearity and risks the Table 2 fallacy and construct-validity distortion; regression discontinuity has limited statistical power and requires a defensible cutoff

### Target Learners
- learning analytics researchers

### Target Learning Goals
- estimating causal effects of analytics interventions from observational data

## Related Strategies
- 

## Examples
-

## Key Sources
- Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577
