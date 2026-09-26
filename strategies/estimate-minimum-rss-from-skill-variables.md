---
type: strategy
id: estimate-minimum-rss-from-skill-variables
title: "Estimate a skill's minimum BKT-BF RSS a priori from dim, n, and percent_correct before running the full grid search"
description: "The paper's proposed approach: rather than finding the parameter values that provide the lowest RSS by exhaustive search, estimate the minimum RSS value from a priori known skill variables."
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

# Estimate a skill's minimum BKT-BF RSS a priori from dim, n, and percent_correct before running the full grid search

> **Strategy** · [All strategies](index.md)

## Description
The paper's proposed approach: rather than finding the parameter values that provide the lowest RSS by exhaustive search, estimate the minimum RSS value from a priori known skill variables. Three variables are used — dim (number of questions tagged with the skill), n (total responses, the product of students and dim), and percent_correct (pc) — chosen because they are "pieces of information that one may have easy access to before computing BKT-BF." A linear model trained on these variables predicts any skill's minimum RSS, enabling quicker convergence of a modified BKT-BF and reduced computational cost.

## Design Implications

### Context
#### Requirements
- Skill-level values of dim, n, and percent_correct before fitting
- A trained linear model (second-degree polynomial on pc) relating these variables to minimum RMSE/RSS
#### Constraints
- Model developed and validated on a single dataset (Psychology MOOC GT Spring 2013); authors state a different dataset is needed to be more certain
- Uses RMSE rather than RSS directly; conversion requires a transformation involving dim and n
- BKT-BF grid used a step much larger than recommended

### Target Learners
- educational data mining researchers
- cognitive tutor system developers

### Target Learning Goals
- reducing computational cost of BKT parameter fitting
- predicting minimum RSS for skill-level model training

## Related Strategies
- 

## Examples
-

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf
