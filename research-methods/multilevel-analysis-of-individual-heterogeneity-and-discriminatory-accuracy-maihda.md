---
type: research-method
id: multilevel-analysis-of-individual-heterogeneity-and-discriminatory-accuracy-maihda
title: Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy (MAIHDA)
description: MAIHDA (Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy) is a statistical framework in which individuals are nested within intersectional strata defined by combinations of social categories.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-21
---

# Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy (MAIHDA)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 7 claims (6 for, 1 mixed) · 3 studies (1 causal, 1 review, 1 associational), `q2` · 0 of 3 report an effect size · 7 claims rest on one study

## Description
MAIHDA (Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy) is a statistical framework in which individuals are nested within intersectional strata defined by combinations of social categories. It partitions variance within and between strata, yielding global measures (VPC, adjusted VPC, PCV) and specific measures (strata means and strata-level residuals) of intersectionality. The article introduces it to educational psychology, noting that 'the intersectional MAIHDA approach is considered the "new gold standard" for studying social inequalities in epidemiology (Merlo, 2018)'.

## Accounts
<!-- How each source describes or uses the method -->
- **The MAIHDA approach models individuals nested within intersectional strata to quantify intersectional effects and discriminatory accuracy**: MAIHDA (Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy) is a statistical framework in which individuals are nested within intersectional strata defined by combinations of social categories. It partitions variance within and between strata, yielding global measures (VPC, adjusted VPC, PCV) and specific measures (strata means and strata-level residuals) of intersectionality. The article introduces it to educational psychology, noting that 'the intersectional MAIHDA approach is considered the "new gold standard" for studying social inequalities in epidemiology (Merlo, 2018)'. (Keller et al. (2023))
- **Intersectional MAIHDA: multilevel analysis of individual heterogeneity and discriminatory accuracy for quantitative intersectional analysis**: Intersectional MAIHDA is a multilevel linear regression approach that treats intersecting social positions as distinct contextual strata (like schools) within which individuals are nested. Model 1 estimates between-strata variation via the variance partitioning coefficient and empirical Bayes predicted stratum means; Model 2 adds main-effect covariates so that stratum random effects capture interaction effects, assessed via the proportional change in variance (PCV). The article introduces it to educational research, arguing it treats "the social categories within which individuals belong... as a feature of their intersectional stratum, rather than of the individuals themselves", avoiding victim-blaming and reference-category norm problems. (Lucy Prior et al. (2022))
- **MAIHDA as a theoretically engaged multilevel approach to intersectional quantitative modeling**: MAIHDA nests individuals within their social identities, combining additive main effects with variance terms for each strata so that shrinkage (partial pooling) informs each strata's prediction from other strata. In this study it is instantiated as "a Bayesian cross-classified multilevel model that nested students (level 1) within courses (level 2a) and strata (level 2b)". The framework includes all strata regardless of sample size, reduces model terms and power requirements, and supports within-group variance analysis. (Van Dusen et al. (2023))
- **MAIHDA: Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy**: MAIHDA is a statistical modeling method designed for intersectional research that leverages multilevel modeling to nest individuals within social strata. Rather than using multiple interaction terms, it nests individuals within strata and, by introducing a group-level error term, "captures the unique outcomes for each identity combination, simplifying model complexity while addressing intersectionality." This study implemented it as a Bayesian three-level cross-classified model (tests within students, cross-classified by course and strata) using brms with 25 multiply-imputed datasets. (Vy Le et al. (2026))

### Claims
- [The variance partition coefficient from the simple intersectional model quantifies how useful intersectional strata are for predicting educational outcomes](../claims/vpc-measures-strata-discriminatory-accuracy.md) [+W]
- [MAIHDA is more scalable and parsimonious than the traditional regression approach with full interaction terms](../claims/maihda-more-scalable-parsimonious-than-regression.md) [+W]
- [Precision-weighted shrinkage in MAIHDA yields reliable conservative estimates for small strata and helps solve the multiple-testing problem](../claims/maihda-shrinkage-small-strata-advantages.md) [+W]
- [Intersectional strata explain around 30% (age 11) and 25% (age 16) of the overall variance in London students' achievement](../claims/intersectional-strata-vpc-achievement-london.md) [+M]
- [Additive main effects of the sociodemographic components explain almost all intersectional stratum variance in achievement (PCV approximately 97% at age 11 and 96% at age 16)](../claims/additive-main-effects-dominate-intersectional-variance.md) [+M]
- [MAIHDA models produce more accurate predicted strata outcomes than fixed effects models across total sample sizes, with the advantage shrinking as total sample size grows](../claims/maihda-more-accurate-than-fixed-effects-strata.md) [+M]
- [MAIHDA shows a small consistent negative bias in mean true error for strata sample sizes below ten individuals](../claims/maihda-negative-bias-tiny-strata.md) [~M]

## Related Research Methods
-

## Key Sources
- Keller, L., Lüdtke, O., Preckel, F., & Brunner, M. (2023). Educational Inequalities at the Intersection of Multiple Social Categories: An Introduction and Systematic Review of the Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy (MAIHDA) Approach. Educational Psychology Review. https://doi.org/10.1007/s10648-023-09733-5
- Lucy Prior, Clare Evans, Juan Merlo and George Leckie. (2022). Sociodemographic inequalities in student achievement: An intersectional multilevel analysis of individual heterogeneity and discriminatory accuracy (MAIHDA) with application to students in London, England.
- Van Dusen, B., Cian, H., Nissen, J., Arellano, L., & Woods, A. (2023). Comparing the efficacy of fixed effect and MAIHDA models in predicting outcomes for intersectional social strata.
- Vy Le, Grace Angell, Jayson Nissen, Ben Van Dusen. (2026). Challenging Data Aggregation Practices: A MAIHDA Study of Asian Student Outcomes in Introductory Physics.
