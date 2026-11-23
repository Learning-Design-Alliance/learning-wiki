---
type: strategy
id: imputation-with-missingness-indicators
title: Impute missing data and add missingness indicator columns, then explicitly report the missing-data treatment
description: For quantitative PER data with missing values, the article recommends imputing missing entries and adding a column flagging which values were imputed, since imputed-value indicators can aid prediction when data are no...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: john-m-aiken-2021
    resource: "https://arxiv.org/abs/2106.11038"
    title: "John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. https://arxiv.org/abs/2106.11038"
    author: John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero
---

# Impute missing data and add missingness indicator columns, then explicitly report the missing-data treatment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
For quantitative PER data with missing values, the article recommends imputing missing entries and adding a column flagging which values were imputed, since imputed-value indicators can aid prediction when data are not missing completely at random. It states: "If applicable, we recommend using an imputation method of the authors’ choice (e.g., multiple imputation [43] or K-nearest neighbors [44])" and, because "There is no universal solution to missing data", that "it is extremely important to report the treatment of missing data in the analysis."

## Design Implications

### Context
#### Requirements
- An additional column is created to identify whether the data are imputed or not for each imputed variable
- Row-wise deletion is reasonable only when data are missing in low amounts
#### Constraints
- In some cases there may be too much missing data and imputing may bias the results

### Target Learners
- students in multi-institution physics courses whose survey responses contain missing data

### Target Learning Goals
- unbiased predictive modeling of outcomes such as concept inventory post-test scores

## Claims

- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](../claims/mean-imputation-sufficient-auxiliary-model.md) [~W]
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](../claims/rct-only-all-covariates-hurt-precision.md) [~W]

## Related Strategies

- [Use multiple imputation and non-response probability weighting to estimate unbiased impacts on classroom quality](multiple-imputation-nonresponse-weighting-quality-impacts.md)
- [Adopt multiple imputation and improve missing-data reporting practices in PER quantitative studies](adopt-mi-improve-missing-data-reporting-strategy.md)

## Examples
-

## Key Sources
- John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. https://arxiv.org/abs/2106.11038
