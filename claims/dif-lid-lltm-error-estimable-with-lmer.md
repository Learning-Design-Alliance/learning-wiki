---
type: claim
title: Differential item functioning, local item dependency, and the linear logistic test model with an error term can be formulated as lmer-estimable models
description: Differential item functioning, local item dependency, and the linear logistic test model with an error term can be formulated as lmer-estimable models
id: dif-lid-lltm-error-estimable-with-lmer
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

# Differential item functioning, local item dependency, and the linear logistic test model with an error term can be formulated as lmer-estimable models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The article presents the linear logistic test model with an error term, differential item functioning models, and local item dependency models as examples of IRT models that can be estimated within the lmer framework. [→ Boeck et al. 2011](#boeck-et-al-2011)

## Evidence

### Boeck et al. 2011

De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://doi.org/10.18637/jss.v039.i12

`q1 · i?` · `theoretical · r2`

Expository claim from the abstract listing exemplar models. The article states these are "Examples of models" explained in the paper with associated lmer code; it reports no empirical fitting results or effect sizes for them in the provided text.

> "Examples of models are the linear logistic test model with an error term, differential item functioning models, and local item dependency models."

## Discussion


## Related Claims
- [lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models](lmer-scope-excludes-2pl-3pl-polytomous.md) — related
- [The lmer-based framework yields three broad categories of IRT models: item covariate, person covariate, and person-by-item covariate models](three-irt-model-categories-lmer-framework.md) — a broader claim this one bears on
