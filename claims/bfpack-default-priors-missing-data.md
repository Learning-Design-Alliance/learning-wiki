---
type: claim
title: BFpack handles common statistical analyses with default priors and data missing at random
description: BFpack handles common statistical analyses with default priors and data missing at random
id: bfpack-default-priors-missing-data
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: mulder-2021
    resource: "https://doi.org/10.18637/jss.v100.i18"
    title: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18"
    author: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C."
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# BFpack handles common statistical analyses with default priors and data missing at random

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q2`

## Subclaims
`q2 i?` BFpack supports common statistical analyses (linear regression, generalized linear models, (multivariate) analysis of (co)variance, correlation analysis, random intercept models) using default priors and while allowing data to contain missing observations that are missing at random. [→ Mulder 2021](#mulder-2021)

## Evidence

### Mulder 2021

Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18

`q2 · i?` · `design · r1`

Descriptive statement from the article's abstract enumerating the analyses BFpack covers. The package uses "default priors" and allows "data to contain missing observations that are missing at random." This is a capability description, not an empirical test.

> "common statistical analyses, such as linear regression, generalized linear models, (multivariate) analysis of (co)variance, correlation analysis, and random intercept models, (iv) using default priors, and (v) while allowing data to contain missing observations that are missing at random"

## Discussion


## Related Claims
- [Linear regression outperformed equipercentile and mean-sigma equating for predicting ARM scores and was selected as the final linking model](linear-regression-selected-linking-model.md) — related
- [A linear regression on skill variables (n, dim, pc) predicts the minimum RSS value for BKT-BF training with high predictive ability](linear-regression-predicts-minimum-rss-bkt-bf.md) — related
- [BFpack provides both Bayesian exploratory and confirmatory hypothesis testing tools with equality and order constraints](bfpack-exploratory-confirmatory-testing-tools.md) — related
