---
type: element
id: bfpack-r-package-bayes-factor-testing
title: "BFpack: an R package for Bayes factor hypothesis testing of common statistical testing problems"
description: BFpack is a software package for the R environment that performs Bayes factor hypothesis testing.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: mulder-2021
    resource: "https://doi.org/10.18637/jss.v100.i18"
    title: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18"
    author: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C"
---

# BFpack: an R package for Bayes factor hypothesis testing of common statistical testing problems

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
BFpack is a software package for the R environment that performs Bayes factor hypothesis testing. The article states: "In this paper we present a new R package called BFpack that contains functions for Bayes factor hypothesis testing for the many common testing problems." It covers common analyses such as linear regression, generalized linear models, (multivariate) analysis of (co)variance, correlation analysis, and random intercept models, using default priors and allowing data with observations missing at random.

## Design Implications

### Context
#### Requirements
- Requires the R statistical environment; analyses are carried out through the package's Bayes factor testing functions for common testing problems
#### Constraints
- The article notes that available software tools for Bayesian hypothesis testing were still limited at the time, positioning BFpack as filling that gap

### Target Learners
- Researchers and analysts in the social and behavioral sciences and related fields

### Target Learning Goals
- Statistical hypothesis testing and evaluation of competing scientific theories using Bayes factors

## Claims

- [BFpack handles common statistical analyses with default priors and data missing at random](../claims/bfpack-default-priors-missing-data.md) [+W]
- [BFpack provides both Bayesian exploratory and confirmatory hypothesis testing tools with equality and order constraints](../claims/bfpack-exploratory-confirmatory-testing-tools.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18
