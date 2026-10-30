---
type: strategy
id: subset-peer-assessment-burden-reduction
title: Reduce student grading burden by requiring only a subset of students to participate in peer assessment
description: Rather than requiring every student to grade peers, the method trains a model on assessments from a subset of students and uses it to grade the remaining answers automatically.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
sources:
  - id: luaces-2018
    resource: "https://doi.org/10.1016/j.compedu.2018.07.016"
    title: "Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.07.016"
    author: "Luaces, O., Díez, J., & Bahamonde, A"
---

# Reduce student grading burden by requiring only a subset of students to participate in peer assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Rather than requiring every student to grade peers, the method trains a model on assessments from a subset of students and uses it to grade the remaining answers automatically. The article reports that this relieves part of the students of the assessment task, reducing the overall burden in massive teaching settings while still producing grades and feedback for all answers.

## Design Implications

### Context
#### Requirements
- A trained model capable of generalizing grading criteria from the participating subset to non-participating students' answers.
#### Constraints
- 

### Target Learners
- students in massive open or large-enrollment courses

### Target Learning Goals
- open-response assignment grading

## Claims

- [A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.](../claims/matrix-factorization-predicts-grades-for-nongrading-students.md) [+W]
- [A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.](../claims/multitask-matrix-factorization-outperforms-single-task-baseline.md) [+W]
- [Peer assessment systems can generate explanatory feedback for students by having graders assess multiple labeled aspects of an answer, not just an overall grade.](../claims/peer-assessment-multi-label-feedback.md) [+W]
- [AGE reduces teacher grading burden by requiring only 1% of student answers in the UNT dataset to be graded](../claims/age-grades-only-one-percent-unt.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.07.016
