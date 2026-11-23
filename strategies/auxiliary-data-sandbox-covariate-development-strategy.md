---
type: strategy
id: auxiliary-data-sandbox-covariate-development-strategy
title: Use publicly available auxiliary data as a flexible sandbox for covariate development in educational RCT analysis
description: "The article recommends treating large, publicly available observational data on schools similar to RCT schools as a \"sandbox\" where pre-processing, missing-value handling, algorithm choice and covariate selection can..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: c-z-mann-2024
    resource: "https://github.com/manncz/aeis-aux-rct"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
---

# Use publicly available auxiliary data as a flexible sandbox for covariate development in educational RCT analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 2 mixed) · 2 studies (1 causal, 1 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article recommends treating large, publicly available observational data on schools similar to RCT schools as a "sandbox" where pre-processing, missing-value handling, algorithm choice and covariate selection can be explored freely, "as long as the experimental outcomes are not touched". Predictions from the resulting auxiliary model then serve as a pre-treatment covariate in the design-based paired-trial estimator, improving precision without bias. The authors found random forests preferable for being easy to fit and interpretable via variable importance.

## Design Implications

### Context
#### Requirements
- Auxiliary and RCT samples must share the outcome of interest and covariates available in the RCT; there needs to be overlap in school characteristics and a similar predictor-outcome relationship between auxiliary and RCT schools.
#### Constraints
- The treatment need not be present in the auxiliary data, but analyses of experimental data themselves must be pre-specified and not changed once experimental data is in hand.
- Full replication data was not provided, to protect the identities of the CTAI study schools.

### Target Learners
- middle and high schools in efficacy trials of educational interventions

### Target Learning Goals
- precise estimation of intervention effects on standardized mathematics achievement outcomes

## Claims

- [Random forest models consistently out-perform neural networks for predicting the math TAKS passing rate in the auxiliary data](../claims/random-forests-outperform-neural-nets-auxiliary.md) [+W]
- [A random forest with all available auxiliary predictors predicts math TAKS passing rates better than OLS with the pretest alone](../claims/rf-all-predictors-beats-pretest-auxiliary.md) [+W]
- [Random forest imputation of missing predictor values does not meaningfully improve auxiliary model performance over simple mean imputation](../claims/mean-imputation-sufficient-auxiliary-model.md) [~W]
- [Variable importance patterns differ between middle and high schools: student cohort matters for middle schools while demographics rise for high schools](../claims/cohort-importance-middle-school-auxiliary-model.md) [+W]
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](../claims/rct-only-all-covariates-hurt-precision.md) [+W]
- [Imputing missing predictor values without conditioning on the outcome variable biases estimates toward zero even when data are missing completely at random](../claims/imputation-omitting-outcome-biases-toward-zero.md) [~W]

## Related Strategies

- [Impute missing data and add missingness indicator columns, then explicitly report the missing-data treatment](imputation-with-missingness-indicators.md)

## Examples
-

## Key Sources
- C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)
