---
type: research-method
id: latent-principal-stratification
title: Latent principal stratification
description: This is a novel causal-inference framework combining principal stratification with item response theory and latent variable analysis.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Latent principal stratification

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
This is a novel causal-inference framework combining principal stratification with item response theory and latent variable analysis. Because students' propensity to master worked sections is never directly observed, the article embeds a Rasch model measuring latent mastery ηT inside the principal stratification model, so that "model-based measurement can account for variation in both the number of sections students work, and which sections students work, in addition to measurement error and missing data in general". The latent variable ηT is a baseline characteristic defined for all students but informed by mastery data only for treated students; the model is fitted simultaneously via MCMC in Stan, integrating over ηT for control students and treated students with missing mastery data.

## Accounts
<!-- How each source describes or uses the method -->
- **Latent principal stratification: embedding an IRT measurement model for a latent intermediate variable within a Bayesian principal stratification model**: This is a novel causal-inference framework combining principal stratification with item response theory and latent variable analysis. Because students' propensity to master worked sections is never directly observed, the article embeds a Rasch model measuring latent mastery ηT inside the principal stratification model, so that "model-based measurement can account for variation in both the number of sections students work, and which sections students work, in addition to measurement error and missing data in general". The latent variable ηT is a baseline characteristic defined for all students but informed by mastery data only for treated students; the model is fitted simultaneously via MCMC in Stan, integrating over ηT for control students and treated students with missing mastery data. (Adam C. Sales et al. (2017))

### Claims
- [In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range](../claims/cta1-effect-decreases-with-mastery-propensity.md) [+M]
- [The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)](../claims/mbar-confounded-eta-not.md) [+M]

## Related Research Methods
-

## Key Sources
- Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. https://arxiv.org/abs/1707.09308
