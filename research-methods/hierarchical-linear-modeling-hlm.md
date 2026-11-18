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
> **Evidence** · 3 claims (3 for) · 3 studies (2 associational, 1 causal), `q2`–`q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
HLM is a regression framework developed specifically for hierarchical datasets that does not require the assumption of independence. It nests level-2 equations within the level-1 equation, allowing level-1 coefficients to vary across groups via random effects; level-1 variables with variance terms are "random slope variables" and those without are fixed. Coefficients combine each course's data with the grand mean using Bayes shrinkage estimators. The unconditional model yields the ICC, the share of total variance attributable to between-group variance.

## Accounts
<!-- How each source describes or uses the method -->
- **Hierarchical linear modeling framework: nested level-2 equations, fixed and random effects, shrinkage estimators, and the intraclass correlation coefficient**: HLM is a regression framework developed specifically for hierarchical datasets that does not require the assumption of independence. It nests level-2 equations within the level-1 equation, allowing level-1 coefficients to vary across groups via random effects; level-1 variables with variance terms are "random slope variables" and those without are fixed. Coefficients combine each course's data with the grand mean using Bayes shrinkage estimators. The unconditional model yields the ICC, the share of total variance attributable to between-group variance. (Ben Van Dusen et al. (2019))

### Claims

- [Hierarchical linear modeling shows 18% of variance in clinical practicum performance is attributable to differences between institutions (ICC = 0.18, p < 0.05)](../claims/hlm-institutional-variance-practicum.md) [+W]
- [ANS acuity (w) did not significantly improve within children over the six-month period in the session-level analysis, though a hierarchical linear model detected a linear increase in percent correct](../claims/no-significant-w-improvement-over-six-months.md) [+W]
- [CBT condition was a truly nonsignificant predictor of RBA pretest scores in hierarchical linear models](../claims/cbt-condition-nonsignificant-pretest-hlm.md) [+W]

## Related Research Methods
-

## Key Sources
- Ben Van Dusen and Jayson Nissen. (2019). Modernizing use of regression models in physics education research: A review of hierarchical linear modeling. Physical Review Physics Education Research 15, 020108. https://doi.org/10.1103/PhysRevPhysEducRes.15.020108
