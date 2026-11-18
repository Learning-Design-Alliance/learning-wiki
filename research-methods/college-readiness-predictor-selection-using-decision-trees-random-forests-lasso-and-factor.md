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
> **Evidence** · 14 claims (11 for, 3 mixed) · 5 studies (5 associational), `q2`–`q3` · 1 of 5 report an effect size · 14 claims rest on one study

## Description
This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors."

## Accounts
<!-- How each source describes or uses the method -->
- **Data-reduction framework combining decision trees, random forests, lasso, and factor analysis to prioritize college-readiness predictors**: This framework uses data reduction to select, from thousands of measures, the variables that maximize classification accuracy for college enrollment and persistence. Decision trees recursively split on the variable maximizing information about the outcome using the Gini index, with mean reduction in the Gini index (MDGI) as a variable-importance measure; random forests replicate trees to counteract sensitivity to the first split, and lasso provides a regression-based alternative. A subsequent factor analysis (bifactor model) identifies what the retained predictors measure. The article uses it to show that "enrolling in college and persisting for a semester can be predicted with almost 90 percent accuracy using a small set of predictors." (James Soland (2017))
- **Develop system-level decision-tree models and a four-construct risk index to triage students for college-readiness supports**: The article argues educational systems can mine existing data at minimal cost because decision trees are easy to interpret and could be built by a state department of education or university system rather than individual administrators. It further recommends measuring a student's risk in each of the four constructs—academic preparation, aspirations and expectations, socioeconomic status, and teacher perceptions—and combining results "into an overall index of risk" used to triage the highest-risk students and support borderline ones, without complicated assessments. (James Soland (2017))
- **Predictive machine-learning modeling (random forest with hold-out evaluation) as an approach for physics education research**: The article introduces a modeling approach for PER in which a random forest classifier — an ensemble of decision trees whose mode output forms the prediction — is fit to registrar data and evaluated on sequestered "hold out" data. This yields "a direct quantiﬁable “performance measure”" such as accuracy and AUC that can compare models across settings, unlike traditional linear models assessed mainly by odds ratios, p-values, and goodness-of-fit. Feature importances are relative to the other features in the model. (John M. Aiken et al. (2019))

### Claims
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](../claims/college-offtrack-classified-90-percent-accuracy.md) [+M]
- [The strongest college-readiness predictors measure four broad constructs: academic preparation, aspirations and expectations, socioeconomic status, and teacher perceptions](../claims/four-college-readiness-constructs-factor-analysis.md) [+M]
- [A few decision-tree splits identify very high-risk students, such as low-SES students who doubt they will reach college](../claims/few-splits-identify-high-risk-students.md) [+W]
- [Academic status shows a significant overall association with classification accuracy, but sex does not; individual status contrasts are exploratory](../claims/academic-status-omnibus-sex-null-ethical-judgment.md) [~W]
- [Predictive specificity was substantially higher for NSLP-eligible, English learner, disabled, and older-entry students, with the largest difference for middle school students with disabilities predicting college enrollment](../claims/predictive-specificity-higher-marginalized-groups.md) [+W]
- [CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance](../claims/feature-selection-reduces-tree-size-maintains-accuracy.md) [~W]
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](../claims/dt-competitive-with-black-box-classifiers.md) [~W]
- [The models' classification accuracy exceeds that of 97 percent of prior studies predicting high school completion](../claims/accuracy-exceeds-97-percent-of-prior-studies.md) [+W]
- [Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree](../claims/modern-physics-course-most-important-predictor-physics-degree.md) [+M]
- [Taking an engineering course while registered as a physics major is the second most important predictor of switching from physics to an engineering degree](../claims/engineering-course-while-physics-major-predicts-switch.md) [+M]
- [Grades in introductory physics and calculus, course timing, gender, and ethnicity have negligible effect sizes and much smaller roles in predicting physics versus engineering graduation](../claims/grades-demographics-negligible-effect-physics-degree.md) [+M]
- [Taking modern physics has the highest, though still relatively small, effect size in a contingency table analysis of physics versus engineering graduates](../claims/modern-physics-highest-effect-size-contingency.md) [+M]
- [Recursive feature elimination finds the optimum predictive model uses only two features — taking modern physics and taking an engineering course as a physics major](../claims/rfe-two-feature-optimum-model.md) [+M]
- [High school GPA and MSU math placement scores add no predictive power to models of physics versus engineering graduation](../claims/prior-preparation-features-no-predictive-gain.md) [+M]

## Related Research Methods
-

## Key Sources
- James Soland. (2017). Combining Academic, Noncognitive, and College Knowledge Measures to Identify Students Not on Track For College: A Data-Driven Approach. Research & Practice in Assessment, Volume Twelve, Summer 2017. https://rpajournal.com
- John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Modeling student pathways in a physics bachelor's degree program. https://arxiv.org/abs/1810.11272
