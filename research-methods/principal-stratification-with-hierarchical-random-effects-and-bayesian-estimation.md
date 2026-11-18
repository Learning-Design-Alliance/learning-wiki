---
type: research-method
id: principal-stratification-with-hierarchical-random-effects-and-bayesian-estimation
title: Principal stratification with hierarchical random effects and Bayesian estimation
description: "The article develops a framework that models students as a mixture of latent subgroups, each defined by the pair of care types a child would receive with and without a Head Start offer (e.g., \"Center Compliers\" and \"Always Head Start\")."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-01
---

# Principal stratification with hierarchical random effects and Bayesian estimation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article develops a framework that models students as a mixture of latent subgroups, each defined by the pair of care types a child would receive with and without a Head Start offer (e.g., "Center Compliers" and "Always Head Start"). It combines a principal stratification framework with a hierarchical random effects model, jointly fitting a choice sub-model and an outcome sub-model via Hamiltonian Monte Carlo in Stan. The classic IV model is described as a special case.

## Accounts
<!-- How each source describes or uses the method -->
- **Principal stratification with hierarchical random effects and Bayesian estimation for latent care-setting subgroups**: The article develops a framework that models students as a mixture of latent subgroups, each defined by the pair of care types a child would receive with and without a Head Start offer (e.g., "Center Compliers" and "Always Head Start"). It combines a principal stratification framework with a hierarchical random effects model, jointly fitting a choice sub-model and an outcome sub-model via Hamiltonian Monte Carlo in Stan. The classic IV model is described as a special case. (Avi Feller et al. (2014))
- **Principal stratification framework for fuzzy RD designs using application status as an intermediate variable**: The article develops a framework "fully consistent with the Rubin Causal Model" in which grant application and receipt are post-assignment intermediate variables; principal stratification cross-classifies students into four latent strata by joint potential application statuses (compliant-, always-, never-, defiant-applicants), defining principal causal effects τg. Because application strata form a finer partition than receipt strata, the standard IV complier effect is a marginal weighted average, and ignoring application behavior loses information when effects are heterogeneous. A local overlap assumption and a local randomization assumption replace standard continuity assumptions, and a Bayesian hierarchical model adjusts for multiple comparisons when selecting the target subpopulation. (Fan Li et al. (2015))

### Claims
- [The effect of the offer of Head Start differs by the alternative child care type a child would otherwise receive](../claims/head-start-effect-varies-by-alternative-care-type.md) [+M]
- [Head Start shows larger effects on cognitive outcomes relative to non-center care than relative to center care, with non-zero effects only for Non-Center Compliers](../claims/head-start-larger-effect-noncenter-compliers.md) [+M]
- [University grants reduce dropout among students from families with economic measure around 15000 euros, with a 13.9% reduction for grant recipients](../claims/italian-university-grants-reduce-dropout-low-income.md) [+M]
- [Grant effect is larger for always-applicants (16.1% dropout reduction) than compliant-applicants, whose small effect dilutes the complier effect](../claims/grant-effect-larger-always-applicants.md) [+M]

## Related Research Methods

- [Three-method framework for causal analysis of EdTech log data from RCTs: matching, mediation, and principal stratification](three-method-framework-for-causal-analysis-of-edtech-log-data-from-rcts-matching-mediation.md)

## Key Sources
- Avi Feller, Todd Grindal, Luke Miratrix, Lindsay C. Page. (2014). Compared to what? Estimating Causal Effects for Latent Subgroups to Understand Variation in the Impacts of Head Start by Alternate Child Care Setting. SREE Spring 2014 Conference. https://www.sree.org
- Fan Li, Alessandra Mattei and Fabrizia Mealli. (2015). Evaluating the Causal Effect of University Grants on Student Dropout: Evidence from a Regression Discontinuity Design Using Principal Stratification. Submitted to the Annals of Applied Statistics. https://arxiv.org/abs/1507.04199
