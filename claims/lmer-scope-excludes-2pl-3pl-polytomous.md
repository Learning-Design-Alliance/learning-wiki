---
type: claim
title: lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models
description: lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models
id: lmer-scope-excludes-2pl-3pl-polytomous
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2011
sources:
  - id: boeck-et-al-2011
    resource: "https://doi.org/10.18637/jss.v039.i12"
    title: "De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://doi.org/10.18637/jss.v039.i12"
    author: "De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Because the lme4 package is limited to univariate generalized linear mixed models, two-parameter and three-parameter IRT models and item response models for polytomous response data fall outside what lmer can estimate. [→ Boeck et al. 2011](#boeck-et-al-2011)

## Evidence

### Boeck et al. 2011

De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://doi.org/10.18637/jss.v039.i12

`q1 · i?` · `theoretical · r2`

Stated scope limitation from the article's abstract. The article attributes the exclusion to the package design, noting the lme4 package is "for univariate generalized linear mixed models"; no empirical demonstration of the limitation is reported.

> "Because the lme4 package is for univariate generalized linear mixed models, neither the two-parameter, and three-parameter models, nor the item response models for polytomous response data, can be estimated with the lmer function."

## Discussion


## Related Claims
- [Differential item functioning, local item dependency, and the linear logistic test model with an error term can be formulated as lmer-estimable models](dif-lid-lltm-error-estimable-with-lmer.md) — related
- [The lmer-based framework yields three broad categories of IRT models: item covariate, person covariate, and person-by-item covariate models](three-irt-model-categories-lmer-framework.md) — related
