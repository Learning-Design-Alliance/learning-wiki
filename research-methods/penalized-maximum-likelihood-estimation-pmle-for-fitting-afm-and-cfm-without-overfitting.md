---
type: research-method
id: penalized-maximum-likelihood-estimation-pmle-for-fitting-afm-and-cfm-without-overfitting
title: Penalized Maximum Likelihood Estimation (PMLE) for fitting AFM and CFM without overfitting
description: PMLE is the estimation method the authors designed to fit the parameters of both models from data while overcoming overfitting.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-26
---

# Penalized Maximum Likelihood Estimation (PMLE) for fitting AFM and CFM without overfitting

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
PMLE is the estimation method the authors designed to fit the parameters of both models from data while overcoming overfitting. It penalizes the oversized student parameters in the joint estimation of student and skill parameters, subtracting a penalty term from the maximum likelihood. Maximizing the penalized likelihood is equivalent to finding a posterior mode for a Bayesian model with a normal prior on student proficiency and flat priors on skill difficulty and learning-rate parameters; a higher penalty value corresponds to lower prior variance, and the BFGS optimization algorithm is used in computing PMLE.

## Accounts
<!-- How each source describes or uses the method -->
- **Penalized Maximum Likelihood Estimation (PMLE) for fitting AFM and CFM without overfitting**: PMLE is the estimation method the authors designed to fit the parameters of both models from data while overcoming overfitting. It penalizes the oversized student parameters in the joint estimation of student and skill parameters, subtracting a penalty term from the maximum likelihood. Maximizing the penalized likelihood is equivalent to finding a posterior mode for a Bayesian model with a normal prior on student proficiency and flat priors on skill difficulty and learning-rate parameters; a higher penalty value corresponds to lower prior variance, and the BFGS optimization algorithm is used in computing PMLE. (Hao Cen et al. (2008))

### Claims

## Related Research Methods

- [Conjunctive Factor Model (CFM)](conjunctive-factor-model-cfm.md)

## Key Sources
- Hao Cen, Kenneth Koedinger, and Brian Junker. (2008). Comparing Two IRT Models for Conjunctive Skills. ITS 2008, LNCS 5091, pp. 796–798.
