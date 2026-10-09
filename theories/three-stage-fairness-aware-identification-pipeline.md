---
type: theory
title: Three-stage fairness-aware analytical pipeline for early at-risk student identification
description: "The article proposes an analytical framework that identifies at-risk students at three points in a course: a Demog stage using demographic information only, Stage 1 adding learning activities up to the first unit revi..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: alison-cheng-2025
    resource: "https://doi.org/10.18608/jla.2025.8761"
    title: "Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761"
    author: Alison Cheng, Bo Pei and Cheng Liu
---

# Three-stage fairness-aware analytical pipeline for early at-risk student identification

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (6 for, 2 mixed) · 3 studies (1 causal, 1 associational, 1 design), `q2` · 1 of 3 report an effect size · 8 claims rest on one study

## Description
The article proposes an analytical framework that identifies at-risk students at three points in a course: a Demog stage using demographic information only, Stage 1 adding learning activities up to the first unit review assignment, and Stage 2 adding activities up to the second assignment. At each stage, four ML models are trained and evaluated on predictive performance and four fairness metrics across race, gender, and lunch-eligibility groups, with bias mitigation applied. The article states the framework consists of "three stages of analysis" and applies "bias mitigation strategies (i.e., ThresholdOptimizer, a commonly used post-processing mitigation approach)" to examine accuracy–fairness trade-offs.

## Design Implications

### Context
#### Requirements
- Consent/assent and demographic self-report surveys from students
- At least two completed end-of-unit review assignments and recorded online practice activity data
- Stratified train/test splits and grid-search hyperparameter tuning with cross-validation
#### Constraints
- Evaluated on 215 AP Statistics students from seven Indiana high schools in 2019–2020; the fourth assignment was dropped due to COVID-19
- Fairness thresholds set at below 0.20 following prior literature

### Target Learners
- High school students in Advanced Placement courses

### Target Learning Objectives
- Early identification of students at risk of scoring below 3 on the AP exam to enable timely support

### Claims

- [Stage1 Optimal Early At Risk Identification](../claims/stage1-optimal-early-at-risk-identification.md) [+M]
- [Thresholdoptimizer Reduces Bias Accuracy Tradeoff](../claims/thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) [+M]
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](../claims/data-balancing-improves-accuracy-increases-bias.md) [~M]
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](../claims/learning-activity-data-reduces-demographic-bias.md) [+W]
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](../claims/no-significant-performance-gain-later-stages.md) [+W]
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](../claims/removing-race-feature-little-performance-impact.md) [~W]
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](../claims/preprocessing-mitigation-reduces-disparities-oulad.md) [+W]
- [Early-stage performance data is particularly important for predicting attrition, while demographic data has limited predictive value once performance data is available](../claims/performance-data-dominates-demographics-in-dropout-prediction.md) [+W]

## Related Theories

- [Accuracy-fairness trade-off framework for educational predictive models using group fairness metrics](accuracy-fairness-tradeoff-group-fairness-framework.md)

## Examples

- [Regularly audit ML models for fairness and proactively apply bias mitigation during model training](../strategies/regular-fairness-audits-and-proactive-bias-mitigation.md)

## Key Sources
- Alison Cheng, Bo Pei and Cheng Liu. (2025). Balancing Act: Early, Fair, and Accurate Identification of At-Risk Students. Journal of Learning Analytics, 12(3), 47–65. https://doi.org/10.18608/jla.2025.8761
