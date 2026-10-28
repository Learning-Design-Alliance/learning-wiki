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
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This design pattern transforms raw behavioural and academic performance features (e.g., average grade, VLE resource access counts) into z-score standardised values relative to the learner's cohort, making them "more generic, contextually meaningful and comparable across different cohorts." The article states this conversion "converted the learner's absolute and mean values for a given feature into a form that captures the degree to which it deviates from the learner's cohort." The pattern increases descriptive power and model accuracy but trades off interpretability, which matters when features feed prescriptive feedback.

## Accounts
<!-- How each source describes or uses the method -->
- **Cohort-relative z-score feature engineering converts raw academic and behavioural features into course-agnostic values for predictive modelling**: This design pattern transforms raw behavioural and academic performance features (e.g., average grade, VLE resource access counts) into z-score standardised values relative to the learner's cohort, making them "more generic, contextually meaningful and comparable across different cohorts." The article states this conversion "converted the learner's absolute and mean values for a given feature into a form that captures the degree to which it deviates from the learner's cohort." The pattern increases descriptive power and model accuracy but trades off interpretability, which matters when features feed prescriptive feedback. (Teo Susnjak (2024))

### Claims
- [CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest](../claims/catboost-best-f1-programme-completion.md) [+M]

## Related Research Methods
-

## Key Sources
- Teo Susnjak. (2024). Beyond Predictive Learning Analytics Modelling and onto Explainable Artificial Intelligence with Prescriptive Analytics and ChatGPT. Int J Artif Intell Educ 34:452–482. https://doi.org/10.1007/s40593-023-00336-3
