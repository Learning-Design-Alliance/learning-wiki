---
type: strategy
id: irt-as-covariate-structure-lmer-strategy
title: Formulate IRT models as covariate structures (mode of covariate, fixed vs random effects) and fit them with lmer
description: "The article's implementable recipe is to express an item response model by choosing covariates and their effects, then fit it with lmer."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: de-boeck-2011
    resource: "https://www.jstatsoft.org/article/view/v039i12"
    title: "De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://www.jstatsoft.org/article/view/v039i12"
    author: "De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I"
---

# Formulate IRT models as covariate structures (mode of covariate, fixed vs random effects) and fit them with lmer

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's implementable recipe is to express an item response model by choosing covariates and their effects, then fit it with lmer. It distinguishes "the kind of covariates -- their mode (person, item, person-by-item), and their being external vs. internal to responses" from "the kind of effects the covariates have -- fixed vs. random", and explains each model with its associated lmer code.

## Design Implications

### Context
#### Requirements
- Analysts must be able to express their model within the generalized linear mixed modeling framework that lmer implements
#### Constraints
- Models outside the univariate GLMM class, such as two-parameter, three-parameter, and polytomous models, cannot be handled this way

### Target Learners
- educational and psychological researchers analyzing item response data

### Target Learning Goals
- specifying and estimating item response models for measurement of person ability and item effects

### Affordances
- [Glmm Covariate Irt Framework Lmer](../research-methods/a-covariate-based-irt-framework-grounded-in-generalized-linear-mixed-modeling.md)

## Claims

- [lmer cannot estimate two-parameter, three-parameter, or polytomous IRT models because lme4 handles only univariate generalized linear mixed models](../claims/lmer-scope-excludes-2pl-3pl-polytomous.md) [-W]

## Related Strategies

- [Control for a student-level covariate by modeling its relationship with the latent student effect rather than adding it as a fixed effect in the mean structure](selection-model-latent-covariate-control.md)

## Examples
-

## Key Sources
- De Boeck, P., Bakker, M., Zwitser, R., Nivard, M., Hofman, A., Tuerlinckx, F., & Partchev, I. (2011). The estimation of item response models with the lmer function from the lme4 package in R. Journal of Statistical Software, 39(12), 1-28. https://www.jstatsoft.org/article/view/v039i12
