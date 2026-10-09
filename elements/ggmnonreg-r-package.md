---
type: element
id: ggmnonreg-r-package
title: "GGMnonreg: an R package for non-regularized Gaussian graphical modeling of low-dimensional data"
description: GGMnonreg is an R package that implements Gaussian graphical modeling without regularization.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: donald-williams-2021
    resource: "https://doi.org/10.21105/joss.03308"
    title: "Donald Williams. (2021). GGMnonreg: Non-regularized Gaussian graphical models in R. Journal of Open Source Software, 6(67), 3308. https://doi.org/10.21105/joss.03308"
    author: Donald Williams
---

# GGMnonreg: an R package for non-regularized Gaussian graphical modeling of low-dimensional data

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
GGMnonreg is an R package that implements Gaussian graphical modeling without regularization. The article states that "The primary purpose of GGMnonreg is to provide methods that were specifically designed for low-dimensional data (e.g., those common in the social-behavioral sciences)", where data are long or low-dimensional (p < n). It represents variables such as symptoms or cortical regions as nodes and connections as edges graphically representing the conditional dependence structure.

## Design Implications

### Context
#### Requirements
- Applicable to low-dimensional data where the number of variables is fewer than the number of observations (p < n)
#### Constraints
- 

### Target Learners
- researchers in the social-behavioral sciences

### Target Learning Goals
- characterizing multivariate conditional dependence structures among variables

## Claims

- [Non-regularized graphical model methods are specifically designed for low-dimensional data common in the social-behavioral sciences](../claims/ggmnonreg-designed-for-low-dimensional-data.md) [+W]
- [Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates](../claims/regularization-drawbacks-uncertainty-false-positives.md) [+W]
- [The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks](../claims/frequentist-glasso-difficulty-uncertainty-centrality.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Donald Williams. (2021). GGMnonreg: Non-regularized Gaussian graphical models in R. Journal of Open Source Software, 6(67), 3308. https://doi.org/10.21105/joss.03308
