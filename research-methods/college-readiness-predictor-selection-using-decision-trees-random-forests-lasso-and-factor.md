---
type: research-method
id: college-readiness-predictor-selection-using-decision-trees-random-forests-lasso-and-factor
title: College-readiness predictor selection using decision trees, random forests, lasso, and factor analysis
description: This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
---

# College-readiness predictor selection using decision trees, random forests, lasso, and factor analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 8 claims (5 for, 3 mixed) · 4 studies (4 associational), `q2`–`q3` · 0 of 4 report an effect size · 8 claims rest on one study

## Description
This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors."

## Accounts
<!-- How each source describes or uses the method -->
- **Data-reduction framework combining decision trees, random forests, lasso, and factor analysis to prioritize college-readiness predictors**: This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors." (James Soland (2017))
- **Develop system-level decision-tree models and a four-construct risk index to triage students for college-readiness supports**: The article argues educational systems can mine existing data at minimal cost because decision trees are easy to interpret and could be built by a state department of education or university system rather than individual administrators. It further recommends measuring a student's risk in each of the four constructs—academic preparation, aspirations and expectations, socioeconomic status, and teacher perceptions—and combining results "into an overall index of risk" used to triage the highest-risk students and support borderline ones, without complicated assessments. (James Soland (2017))

### Claims

- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](../claims/college-offtrack-classified-90-percent-accuracy.md) [+M]
- [The strongest college-readiness predictors measure four broad constructs: academic preparation, aspirations and expectations, socioeconomic status, and teacher perceptions](../claims/four-college-readiness-constructs-factor-analysis.md) [+M]
- [A few decision-tree splits identify very high-risk students, such as low-SES students who doubt they will reach college](../claims/few-splits-identify-high-risk-students.md) [+W]
- [Academic status shows a significant overall association with classification accuracy, but sex does not; individual status contrasts are exploratory](../claims/academic-status-omnibus-sex-null-ethical-judgment.md) [~W]
- [Predictive specificity was substantially higher for NSLP-eligible, English learner, disabled, and older-entry students, with the largest difference for middle school students with disabilities predicting college enrollment](../claims/predictive-specificity-higher-marginalized-groups.md) [+W]
- [CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance](../claims/feature-selection-reduces-tree-size-maintains-accuracy.md) [~W]
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](../claims/dt-competitive-with-black-box-classifiers.md) [~W]
- [The models' classification accuracy exceeds that of 97 percent of prior studies predicting high school completion](../claims/accuracy-exceeds-97-percent-of-prior-studies.md) [+W]

## Related Research Methods
-

## Key Sources
- James Soland. (2017). Combining Academic, Noncognitive, and College Knowledge Measures to Identify Students Not on Track For College: A Data-Driven Approach. Research & Practice in Assessment, Volume Twelve, Summer 2017. https://rpajournal.com
