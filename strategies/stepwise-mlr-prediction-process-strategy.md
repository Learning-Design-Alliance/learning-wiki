---
type: strategy
id: stepwise-mlr-prediction-process-strategy
title: Build program-specific predictive models via step-wise multivariate linear regression with an internal visualization tool
description: "The article describes a process used at JCESOM to predict students likely to struggle on standardized exams: \"capturing of student data that exist in several locations, curating it for analytical analysis, performing..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-09
sources:
  - id: gullo-charles-a-2016
    resource: "https://doi.org/10.3402/meo.v21.32516"
    title: "Gullo Charles A. (2016). The future is in the numbers: the power of predictive analysis in the biomedical educational environment. Medical Education Online. https://doi.org/10.3402/meo.v21.32516"
    author: Gullo Charles A
---

# Build program-specific predictive models via step-wise multivariate linear regression with an internal visualization tool

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article describes a process used at JCESOM to predict students likely to struggle on standardized exams: "capturing of student data that exist in several locations, curating it for analytical analysis, performing step-wise linear regression, and establishing an internal visualization tool for easy interrogation of the data". Variables are added one at a time and kept only if coefficients are positive and additive to the model; resulting equations are used to compute predicted scores for counseling at-risk students.

## Design Implications

### Context
#### Requirements
- Programs need access to student data from admissions, curricular assessments, and ideally post-graduation sources, with defined outcome variables (e.g., USMLE, COMLEX, NAPLEX)
#### Constraints
- Findings are institution-specific and may not be the same for different schools
- Assumptions such as independence of the independent variables (multicolinearity) need to be tested before use

### Target Learners
- biomedical and medical students

### Target Learning Goals
- predicting and remediating performance on national standardized licensing examinations

## Claims

- [Adding later curricular data strengthens prediction: second-year exams explained 53% of Step 1 variance, reported as significantly higher than first-year exams](../claims/ms2-exams-outpredict-ms1-exams-step1-ar2.md) [+W]
- [The strongest Step 1 prediction model combined the practice Step 1 exam with two basic science miniboards, achieving an adjusted R2 of 77%](../claims/step1-strongest-prediction-practice-exam-miniboards-ar2-77.md) [+W]
- [The strongest Step 2 prediction model combined Step 1 results with four clinical mini board results, achieving an adjusted R2 of 62%](../claims/step2-strongest-prediction-step1-plus-clinical-miniboards-ar2-62.md) [+W]
- [In multivariable regression, median MCAT is the only significant predictor of Step 1 score, with the model explaining 58.4% of variance](../claims/mcat-only-significant-step1-predictor.md) [+W]

## Related Strategies

- [Pool anonymized institutional data nationally to build more robust and validatable predictive models](pool-anonymized-national-biomedical-data-strategy.md)

## Examples
-

## Key Sources
- Gullo Charles A. (2016). The future is in the numbers: the power of predictive analysis in the biomedical educational environment. Medical Education Online. https://doi.org/10.3402/meo.v21.32516
