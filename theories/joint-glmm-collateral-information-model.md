---
type: theory
title: Joint GLMM model regressing person ability and speed on person covariates for IRT estimation with collateral information
description: "The article applies a multivariate joint model under the generalized linear mixed models framework that \"simultaneously models binary item response and continuous RT response on test items that nested within person\" (..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: wang-2011
    resource: "https://www.nwea.org/research/publication/incorporating-person-covariates-and-response-times-as-collateral-information-to-improve-person-and-item-parameter-estimations/"
    title: "Wang, S., & Jiao, H. (2011). Incorporating Person Covariates and Response Times as Collateral Information to Improve Person and Item Parameter Estimations. Paper presented at the annual meeting of the National Council on Measurement in Education, New Orleans, LA. https://www.nwea.org/research/publication/incorporating-person-covariates-and-response-times-as-collateral-information-to-improve-person-and-item-parameter-estimations/"
    author: "Wang, S., & Jiao, H"
---

# Joint GLMM model regressing person ability and speed on person covariates for IRT estimation with collateral information

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article applies a multivariate joint model under the generalized linear mixed models framework that "simultaneously models binary item response and continuous RT response on test items that nested within person" (Klein Entink, Fox, & van der Linden, 2009). A Rasch logit submodel for responses and a lognormal submodel for response times are joined, with a covariance parameter ρ modeling ability-speed dependence. Person covariates (cross-test raw score, gender, ethnicity) enter as fixed-effect regressions on the random ability and speed effects, and the full model is fit with SAS PROC GLIMMIX via restricted maximum likelihood.

## Design Implications

### Context
#### Requirements
- Computerized administration that records item-level response times, plus matched student covariate data (cross-test scores, gender, ethnicity) for the same examinees
#### Constraints
- The GLIMMIX procedure sometimes cannot converge when the number of items and observations becomes large or in case of many missing data

### Target Learners
- K-12 students taking computerized achievement tests

### Target Learning Objectives
- Accurate estimation of person ability and item difficulty parameters in educational assessment

### Claims

- [Collateral Information Improves Joint Model Fit](../claims/collateral-information-improves-joint-model-fit.md) [+M]
- [Negative Ability Speed Correlation Li52 Stronger](../claims/negative-ability-speed-correlation-li52-stronger.md) [+M]
- [Adding collateral information has little effect on ability and item parameter estimates but more effect on speed parameter estimates](../claims/ci-effects-small-on-ability-item-larger-on-speed.md) [+W]
- [Scores from a different subject test can serve as collateral information: mathematics scores can improve reading item parameter estimation and vice versa](../claims/cross-test-scores-as-collateral-information.md) [+W]

## Related Theories
- 

## Examples
-

## Key Sources
- Wang, S., & Jiao, H. (2011). Incorporating Person Covariates and Response Times as Collateral Information to Improve Person and Item Parameter Estimations. Paper presented at the annual meeting of the National Council on Measurement in Education, New Orleans, LA. https://www.nwea.org/research/publication/incorporating-person-covariates-and-response-times-as-collateral-information-to-improve-person-and-item-parameter-estimations/
