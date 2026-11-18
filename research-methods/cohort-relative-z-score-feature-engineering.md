---
type: research-method
id: cohort-relative-z-score-feature-engineering
title: Cohort-relative z-score feature engineering
description: "This design pattern transforms raw behavioural and academic performance features (e.g., average grade, VLE resource access counts) into z-score standardised values relative to the learner's cohort, making them \"more generic, contextually meaningful and comparable across different cohorts.\" The artic"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Cohort-relative z-score feature engineering

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 associational, 1 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
This design pattern transforms raw behavioural and academic performance features (e.g., average grade, VLE resource access counts) into z-score standardised values relative to the learner's cohort, making them "more generic, contextually meaningful and comparable across different cohorts." The article states this conversion "converted the learner's absolute and mean values for a given feature into a form that captures the degree to which it deviates from the learner's cohort." The pattern increases descriptive power and model accuracy but trades off interpretability, which matters when features feed prescriptive feedback.

## Accounts
<!-- How each source describes or uses the method -->
- **Cohort-relative z-score feature engineering converts raw academic and behavioural features into course-agnostic values for predictive modelling**: This design pattern transforms raw behavioural and academic performance features (e.g., average grade, VLE resource access counts) into z-score standardised values relative to the learner's cohort, making them "more generic, contextually meaningful and comparable across different cohorts." The article states this conversion "converted the learner's absolute and mean values for a given feature into a form that captures the degree to which it deviates from the learner's cohort." The pattern increases descriptive power and model accuracy but trades off interpretability, which matters when features feed prescriptive feedback. (Teo Susnjak (2024))
- **Z-score normalization method for comparing grades across course offerings**: Because course grades are not normalized measurements, the article uses the standard score or "Z-score" to normalize students' grades within a single course offering, providing "a measure of what fraction of a standard deviation (σ) that a particular value (x) deviates from the mean (µ)." Mean Z-scores and standard errors are then computed separately for physics and math courses for groups of students defined by graduating degree and physics-declaration status, enabling normalized comparisons across groups. (John M. Aiken (2016))

### Claims
- [CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest](../claims/catboost-best-f1-programme-completion.md) [+M]
- [Z-score-normalized introductory math and physics grades differentiate physics degree earners (above average) from physics declarers who leave (below average)](../claims/normalized-grades-differentiate-physics-graduates.md) [+M]

## Related Research Methods
-

## Key Sources
- Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3
- John M. Aiken, Marcos D. Caballero. (2016). Methods for Analyzing Pathways through a Physics Major. https://arxiv.org/abs/1606.07170
