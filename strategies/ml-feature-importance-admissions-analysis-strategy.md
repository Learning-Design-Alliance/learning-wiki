---
type: strategy
id: ml-feature-importance-admissions-analysis-strategy
title: Use machine learning feature-importance analysis of real application data to elucidate which admissions factors drive acceptance decisions
description: "The article demonstrates a strategy for studying graduate admissions: collect real application data, engineer comparable factors from heterogeneous inputs, and apply a conditional inference forest with AUC-based featu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: nicholas-t-young-and-marcos-d-caballero-2019
    resource: "https://arxiv.org/abs/1907.01570"
    title: "Nicholas T. Young and Marcos D. Caballero. (2019). Using machine learning to understand physics graduate school admissions. https://arxiv.org/abs/1907.01570"
    author: Nicholas T. Young and Marcos D. Caballero
---

# Use machine learning feature-importance analysis of real application data to elucidate which admissions factors drive acceptance decisions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The article demonstrates a strategy for studying graduate admissions: collect real application data, engineer comparable factors from heterogeneous inputs, and apply a conditional inference forest with AUC-based feature importance and recursive backward elimination. It states that "graduate admissions is an ideal target for machine learning" because applications mix numerical, categorical, and open-ended data. The approach lets factors of different scales be compared on one importance scale.

## Design Implications

### Context
#### Requirements
- Access to admissions data including applicant GPAs, institutions, GRE scores, and research interests
- Use of a feature-importance measure less biased when input features differ in scale, such as the AUC-based importance the article uses
#### Constraints
- The article notes feature importances can be inflated when features are correlated, and its correlation-controlling methods require data with no missing values
- The model only had access to a subset of the information available to faculty evaluators, so meaningful features could lie in unavailable data

### Target Learners
- physics PhD program applicants

### Target Learning Goals
- understanding and improving graduate admissions processes

## Claims

- [Institutional and departmental characteristics of applicants' undergraduate institutions were not meaningful to the admissions model](../claims/institutional-characteristics-not-meaningful-admissions-model.md) [+W]
- [Physics GRE score and undergraduate GPA are the only meaningful admissions factors at the studied program](../claims/physics-gre-and-gpa-only-meaningful-admissions-factors.md) [+W]
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](../claims/random-forest-predicts-physics-phd-admissions-75-8-percent.md) [+W]
- [Admissions predictions show a rough physics GRE cutoff around 700 that high GPA can partially compensate below](../claims/rough-physics-gre-cutoff-700-gpa-compensation.md) [+W]
- [A two-factor model using only undergraduate GPA and physics GRE matches the full model's predictive performance](../claims/two-factor-gpa-physics-gre-model-matches-full-model.md) [+W]
- [The studied program appears to weight verbal GRE more than the average program, possibly because domestic-only data omit TOEFL effects](../claims/verbal-gre-emphasis-domestic-applicants-toefl-hypothesis.md) [+W]
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](../claims/dt-competitive-with-black-box-classifiers.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Nicholas T. Young and Marcos D. Caballero. (2019). Using machine learning to understand physics graduate school admissions. https://arxiv.org/abs/1907.01570
