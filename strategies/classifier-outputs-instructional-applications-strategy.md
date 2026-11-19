---
type: strategy
id: classifier-outputs-instructional-applications-strategy
title: Use classification model outputs (variable importance, success probabilities, decision trees) to allocate resources, revise homework policy, and target communication with at-risk students
description: "The article describes three classroom analyses and applications of a constructed classifier at Institution 1: computing variable importance to shape institutional data requests, assigning each student an individual su..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: jie-yang-2020
    resource: "https://arxiv.org/abs/2007.13575"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. https://arxiv.org/abs/2007.13575"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
---

# Use classification model outputs (variable importance, success probabilities, decision trees) to allocate resources, revise homework policy, and target communication with at-risk students

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (8 for) · 3 studies (3 associational), `q2` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
The article describes three classroom analyses and applications of a constructed classifier at Institution 1: computing variable importance to shape institutional data requests, assigning each student an individual success probability that can be updated as the semester progresses, and using decision-tree thresholds to guide policy. Applications include assigning experienced teaching assistants and Learning Assistants to at-risk laboratory sections, a homework reworking policy for grades below 60%, and targeted communication with at-risk students. The applications are "designed around the principle that any additional instructional activity must potentially benefit all students".

## Design Implications

### Context
#### Requirements
- Requires access to institutional data, which the article recommends gathering through a departmental data committee or staff, and a trained classification model
#### Constraints
- The article states the models are far from perfect, so all students may actually be at risk and interventions must be available to any student; classifiers must be rebuilt after successful interventions change student outcomes

### Target Learners
- students in large introductory calculus-based physics service courses

### Target Learning Goals
- directing educational interventions and resources to students at risk of a DFW outcome

## Claims

- [A decision tree trained on Sample 2 week-2 data identifies a homework average of 62% as the highest-level threshold for classifying students at risk of a DFW outcome](../claims/decision-tree-homework-62-percent-threshold-dfw.md) [+W]
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](../claims/default-rf-poor-dfw-tuning-raises-43-percent.md) [+W]
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](../claims/demographic-variables-low-importance-dfw-models.md) [+W]
- [In-class-only DFW models perform more weakly than institutional-only models early in the semester but exceed them after the first test in week 5](../claims/inclass-only-models-exceed-institutional-after-test1.md) [+W]
- [Combining institutional and in-class data gave the highest DFW classification performance in Sample 2, improving over institutional-only models by 3% in week 1 to 18% in week 8](../claims/institutional-plus-inclass-data-highest-dfw-performance.md) [+W]
- [A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification](../claims/restricted-variable-set-reduces-dfw-accuracy-7-percent.md) [+W]
- [Biology and Introduction to Health Sciences midterm scores are the strongest predictors of at-risk classification, with SHAP analyses showing the largest case-level impact](../claims/biology-intro-midterms-strongest-predictors.md) [+W]
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](../claims/dt-competitive-with-black-box-classifiers.md) [+W]

## Related Strategies

- [Use classification results only to support, not to exclude, students: keep interventions open to all while encouraging the most at-risk students to use them](ethical-use-classification-open-to-all-students.md)

## Examples
-

## Key Sources
- Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. https://arxiv.org/abs/2007.13575
