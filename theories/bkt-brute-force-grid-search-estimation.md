---
type: theory
title: "BKT Brute Force (BKT-BF): grid-search parameter estimation minimizing Residual Sum of Squares"
description: "BKT-BF is an algorithm to estimate BKT parameter values by brute force: a grid of possible parameter values is set, and for each combination a Residual Sum of Squares (RSS) value is obtained; \"the combination of value..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L"
---

# BKT Brute Force (BKT-BF): grid-search parameter estimation minimizing Residual Sum of Squares

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study, `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
BKT-BF is an algorithm to estimate BKT parameter values by brute force: a grid of possible parameter values is set, and for each combination a Residual Sum of Squares (RSS) value is obtained; "the combination of values resulting in the lowest Residual Sum of Squares (RSS) value for a skill is the one that will be used in BKT." The RSS is computed from observed answers Oi,t and the BKT-derived likelihood of a correct answer Ci,j, normalized by students and dim. In this study, grids used values 0.05–0.95 (step 0.15) for L0 and T, and bounded 0.05–0.30 (step 0.05) for G and S to avoid model degeneracy, yielding 1764 RSS values per skill.

## Design Implications

### Context
#### Requirements
- A grid of candidate parameter values
- Student response data for skill-tagged questions
- Computation over all grid combinations to obtain RSS values
#### Constraints
- Very expensive in computational cost, as all brute force algorithms are
- Does not help the identifiability problem of BKT
- In this study a step much larger than the one recommended by the algorithm was used

### Target Learners
- researchers and course designers fitting student models to skill-tagged response data

### Target Learning Objectives
- estimating BKT parameters (L0, T, G, S) for knowledge inference

### Claims

- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](../claims/bkt-bf-cost-identifiability-em-local-minima.md) [+W]
- [The very high adjusted R² of the RSS-estimation model may indicate BKT works better when percent correct is very high, leaving little room for T and G](../claims/high-pc-bkt-little-room-t-g.md) [~W]
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](../claims/linear-regression-predicts-minimum-rss-bkt-bf.md) [+W]
- [In a preliminary PCA, RMSE is highly correlated with the slip parameter S, while T and G appear orthogonal to RMSE](../claims/pca-rmse-correlates-slip-orthogonal-t-g.md) [~W]

## Related Theories

- [Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories](bkt-two-state-hmm-student-model.md)

## Examples

- [Estimate a skill's minimum BKT-BF RSS a priori from dim, n, and percent_correct before running the full grid search](../strategies/estimate-minimum-rss-from-skill-variables.md)

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf
