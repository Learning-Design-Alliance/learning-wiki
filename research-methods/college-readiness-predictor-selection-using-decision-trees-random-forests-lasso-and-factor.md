---
type: research-method
id: college-readiness-predictor-selection-using-decision-trees-random-forests-lasso-and-factor
title: College-readiness predictor selection using decision trees, random forests, lasso, and factor analysis
description: This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
---

# College-readiness predictor selection using decision trees, random forests, lasso, and factor analysis

> **Research Method** · [All research methods](index.md)

## Description
This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors."

## Accounts
<!-- How each source describes or uses the method -->
- **Data-reduction framework combining decision trees, random forests, lasso, and factor analysis to prioritize college-readiness predictors**: This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors." (James Soland (2017))

### Claims
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](../claims/college-offtrack-classified-90-percent-accuracy.md) [+M]
- [The strongest college-readiness predictors measure four broad constructs: academic preparation, aspirations and expectations, socioeconomic status, and teacher perceptions](../claims/four-college-readiness-constructs-factor-analysis.md) [+M]

## Related Research Methods
-

## Key Sources
- James Soland. (2017). Combining Academic, Noncognitive, and College Knowledge Measures to Identify Students Not on Track For College: A Data-Driven Approach. Research & Practice in Assessment, Volume Twelve, Summer 2017. https://rpajournal.com
