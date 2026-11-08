---
type: design
id: logistic-regression-preparedness-model-bio101
title: Logistic regression preparedness model predicting probability of achieving a C+ or better in Bio101
description: A logistic regression model trained on 2013–2016 cohort data (n = 638) using sex, first-generation status, Pell eligibility, underrepresented minority status, athlete status, high school calculus grade, unweighted cor...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: hawkins-whitney-2021
    resource: "https://doi.org/10.1187/cbe.20-06-0117"
    title: "Hawkins Whitney, W.; Goddard, K.; Favero, C. (2021). A Cocurricular Program That Encourages Specific Study Skills and Habits Improves Academic Performance and Retention of First-Year Undergraduates in Introductory Biology. CBE—Life Sciences Education. https://doi.org/10.1187/cbe.20-06-0117"
    author: Hawkins Whitney, W.; Goddard, K.; Favero, C
---

# Logistic regression preparedness model predicting probability of achieving a C+ or better in Bio101

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A logistic regression model trained on 2013–2016 cohort data (n = 638) using sex, first-generation status, Pell eligibility, underrepresented minority status, athlete status, high school calculus grade, unweighted core high school GPA, and SAT score to predict each student's probability of achieving a C+ or better. The article reports that "For the 2017 cohort, the model correctly classified students in 84% of cases." Students were then banded into low (≤25%), medium (26–84%), and high (≥85%) preparedness groups to target recruitment and compare outcomes.

## Design Implications

### Context
#### Requirements
- Multiple years of prior cohort data with demographic and academic variables to train the model
- Concordance tables to convert ACT scores and post-2016 SAT scores; a second model omitting testing for students without scores
#### Constraints
- The authors recommend institutions "consider which variables might be applicable on their own campuses and build a model that best predicts the performance of their own students"
- Neither SAT nor ACT scores were available for a small percentage of test-optional students

### Target Learners
- First-year, first-time undergraduates entering a STEM gateway course

### Learning Goals
- Early identification of students likely to struggle so support can be offered before failure

### Claims
- [Full participants in an 8-week cocurricular study-skills program scored higher than nonparticipants on exam 2 at low and medium preparedness, and on final grade only at medium preparedness, in introductory biology](../claims/coc-improves-grades-low-medium-preparedness.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hawkins Whitney, W.; Goddard, K.; Favero, C. (2021). A Cocurricular Program That Encourages Specific Study Skills and Habits Improves Academic Performance and Retention of First-Year Undergraduates in Introductory Biology. CBE—Life Sciences Education. https://doi.org/10.1187/cbe.20-06-0117
