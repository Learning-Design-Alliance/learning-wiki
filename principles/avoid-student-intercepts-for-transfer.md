---
type: principle
id: avoid-student-intercepts-for-transfer
title: Avoid fixed or random student intercepts in learner models intended to transfer to new student populations
description: The article argues that to be maximally applicable, a learner model needs to adapt to student differences without requiring student parameters estimated from prior data.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: philip-i-pavlik-2021
    resource: "https://doi.org/10.1109/TLT.2021.3128569"
    title: "Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569"
    author: Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams
---

# Avoid fixed or random student intercepts in learner models intended to transfer to new student populations

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study, `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article argues that to be maximally applicable, a learner model needs to adapt to student differences without requiring student parameters estimated from prior data. The main-comparison models avoid student parameters as a partial solution to the cold start problem that occurs when models are transferred between different populations of students, instead using dynamic adaptive features like propdec at the student level.

## Design Implications

### Context
#### Requirements
- A dynamic adaptive feature (e.g., propdec or logitdec) that captures student variability from the practice sequence itself
#### Constraints
- A pretest could be used to estimate student-level intercept values, but this possibility is not addressed in the article

### Target Learners
- new students in populations unseen during model fitting

### Target Learning Objectives
- generalizable prediction of student performance in adaptive systems

### Claims
- [Propdec Colinear With Student Intercept](../claims/propdec-colinear-with-student-intercept.md) [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569
