---
type: strategy
id: selection-model-latent-covariate-control
title: Control for a student-level covariate by modeling its relationship with the latent student effect rather than adding it as a fixed effect in the mean structure
description: "This strategy uses the selection model's latent structure as a general mechanism for covariate control in value-added modeling."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-16
sources:
  - id: mccaffrey-2011
    resource: "https://doi.org/10.1214/10-AOAS405"
    title: "McCaffrey, D. F. and Lockwood, J. R. (2011). Missing data in value-added modeling of teacher effects. The Annals of Applied Statistics, 5(2A), 773-797. https://doi.org/10.1214/10-AOAS405"
    author: McCaffrey, D. F. and Lockwood, J. R
---

# Control for a student-level covariate by modeling its relationship with the latent student effect rather than adding it as a fixed effect in the mean structure

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 3 studies (2 theoretical, 1 associational), `q1`–`q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
This strategy uses the selection model's latent structure as a general mechanism for covariate control in value-added modeling. The article states that the selection model "provided a means of controlling for a student-level covariate (the number of observed test scores) by modeling the relationship between that variable and the latent student eﬀect rather than including it in the mean structure as ﬁxed eﬀect". The authors suggest this approach might be used more broadly for other variables, avoiding potential overcorrecting identified as a possible source of bias when covariates are included as fixed effects but teacher effects are random.

## Design Implications

### Context
#### Requirements
- A random effects model with a latent student effect into which the covariate's relationship can be modeled, estimated within a Bayesian framework
#### Constraints
- The article recommends this only as a potential advantage and broader possibility, not as a tested manipulation; in the reported analysis little was gained from fitting the more complex MNAR models

### Target Learners
- students in longitudinal achievement data systems linked to teachers

### Target Learning Goals
- estimating teacher or school effects on student achievement while controlling for student-level covariates

### Affordances
- [Mnar Extensions Sequential Multimembership Vam](../research-methods/value-added-modeling.md)

## Claims

- [Unprincipled inclusion of covariates ('garbage-can regression') can introduce rather than remove bias](../claims/garbage-can-regression-fallibility.md) [+W]
- [Allowing achievement data to be missing not at random has little impact on estimated teacher effects in value-added modeling, with MNAR and MAR estimates correlating at 0.98 or better](../claims/mnar-little-impact-teacher-effect-estimates.md) [+W]
- [The number of observed test scores depends on students' unobserved general achievement level, with higher-achieving students more likely to have complete data](../claims/observed-scores-depend-on-latent-achievement.md) [+W]
- [A random effects selection model allowing MNAR data fits longitudinal value-added achievement data better than the MAR model by DIC](../claims/selection-model-better-dic-than-mar.md) [+W]
- [Student growth modeling and teacher value-added modeling are complex due to non-random assignment, measurement error, multidimensionality, and covariates](../claims/growth-value-added-modeling-complexity-sources.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- McCaffrey, D. F. and Lockwood, J. R. (2011). Missing data in value-added modeling of teacher effects. The Annals of Applied Statistics, 5(2A), 773-797. https://doi.org/10.1214/10-AOAS405
