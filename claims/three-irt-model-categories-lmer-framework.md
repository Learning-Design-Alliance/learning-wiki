---
type: claim
title: "The lmer-based framework yields three broad categories of IRT models: item covariate, person covariate, and person-by-item covariate models"
description: "The lmer-based framework yields three broad categories of IRT models: item covariate, person covariate, and person-by-item covariate models"
id: three-irt-model-categories-lmer-framework
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

# The lmer-based framework yields three broad categories of IRT models: item covariate, person covariate, and person-by-item covariate models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Within the generalized linear mixed modeling framework, IRT models are organized into three broad categories: item covariate models, person covariate models, and person-by-item covariate models, each containing three types of more specific models. [→ Boeck et al. 2011](#boeck-et-al-2011)

## Evidence

### Boeck et al. 2011

De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://doi.org/10.18637/jss.v039.i12

`q1 · i?` · `theoretical · r2`

Expository description from the article's abstract of the taxonomy it develops. The article states that "three broad categories of models are described" and that within each category "three types of more specific models are discussed"; no empirical test or effect size is reported for the taxonomy itself.

> "Based on this framework, three broad categories of models are described: Item covariate models, person covariate models, and person-by-item covariate models, and within each category three types of more specific models are discussed."

## Discussion


## Related Claims
- [Differential item functioning, local item dependency, and the linear logistic test model with an error term can be formulated as lmer-estimable models](dif-lid-lltm-error-estimable-with-lmer.md) — a narrower finding that bears on this claim
- [lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models](lmer-scope-excludes-2pl-3pl-polytomous.md) — related
