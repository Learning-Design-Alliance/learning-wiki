---
type: research-method
id: hierarchical-linear-modeling-hlm
title: Hierarchical linear modeling (HLM)
description: HLM is a regression framework developed specifically for hierarchical datasets that does not require the assumption of independence.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Hierarchical linear modeling (HLM)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 4 studies (3 associational, 1 causal), `q2`–`q3` · 0 of 4 report an effect size · 4 claims rest on one study

## Description
HLM is a regression framework developed specifically for hierarchical datasets that does not require the assumption of independence. It nests level-2 equations within the level-1 equation, allowing level-1 coefficients to vary across groups via random effects; level-1 variables with variance terms are "random slope variables" and those without are fixed. Coefficients combine each course's data with the grand mean using Bayes shrinkage estimators. The unconditional model yields the ICC, the share of total variance attributable to between-group variance.

## Accounts
<!-- How each source describes or uses the method -->
- **Hierarchical linear modeling framework: nested level-2 equations, fixed and random effects, shrinkage estimators, and the intraclass correlation coefficient**: HLM is a regression framework developed specifically for hierarchical datasets that does not require the assumption of independence. It nests level-2 equations within the level-1 equation, allowing level-1 coefficients to vary across groups via random effects; level-1 variables with variance terms are "random slope variables" and those without are fixed. Coefficients combine each course's data with the grand mean using Bayes shrinkage estimators. The unconditional model yields the ICC, the share of total variance attributable to between-group variance. (Ben Van Dusen et al. (2019))
- **Hierarchical linear modeling as a three-level framework for nested classroom data**: The article presents hierarchical linear modeling (HLM), also called multilevel modeling, as the statistical framework for data nested in clustered structures such as students within classes within schools. It explains that "HLM considers each of these sequential groupings to be a new level, where lower levels are nested within higher levels, and accounts for this nesting structure by associating each variable (and corresponding data) with the appropriate level." The framework allows cluster-specific intercepts and slopes, models coefficients as functions of higher-level predictors, and yields intraclass correlation coefficients that parse outcome variance across levels, information standard regression cannot provide. (Connor Gorman et al. (2016))
- **Use multi-level models rather than single-level regression when analyzing education datasets with hierarchical structures**: Because education datasets often nest students within courses, single-level models such as linear and logistic regression fail to account for that structure. The article's analysis of 112 physics courses showed single-level and multi-level models "produced significantly different findings" about collaborative learning without LAs, and the authors conclude the DBER community should use multi-level models to analyze datasets with hierarchical structures. (Van Dusen (2018))

### Claims
- [Hierarchical linear modeling shows 18% of variance in clinical practicum performance is attributable to differences between institutions (ICC = 0.18, p < 0.05)](../claims/hlm-institutional-variance-practicum.md) [+W]
- [ANS acuity (w) did not significantly improve within children over the six-month period in the session-level analysis, though a hierarchical linear model detected a linear increase in percent correct](../claims/no-significant-w-improvement-over-six-months.md) [+W]
- [CBT condition was a truly nonsignificant predictor of RBA pretest scores in hierarchical linear models](../claims/cbt-condition-nonsignificant-pretest-hlm.md) [+W]
- [Class size over the ranges studied does not have a significant effect on student grades in active-learning introductory physics courses](../claims/class-size-no-significant-effect-active-learning-physics-grades.md) [+M]

## Related Research Methods
-

## Key Sources
- Ben Van Dusen and Jayson Nissen. (2019). Modernizing use of regression models in physics education research: A review of hierarchical linear modeling. Physical Review Physics Education Research 15, 020108. https://doi.org/10.1103/PhysRevPhysEducRes.15.020108
- Connor Gorman, David Webb, Kevin Gee. (2016). Hierarchical Linear Modeling Approach to Measuring the Effects of Class Size and Other Classroom Characteristics on Student Learning in an Active-Learning Based Introductory Physics Course. University of California, Davis. https://scholar.google.com/scholar?q=Hierarchical+Linear+Modeling+Approach+to+Measuring+the+Effects+of+Class+Size
- Van Dusen, B. (2018). LASSO: A New Tool to Support Instructors and Researchers. APS Forum on Education Newsletter, Fall 2018. https://www.learningassistantalliance.org
