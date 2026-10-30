---
type: research-method
id: matrix-factorization-model-of-peer-assessment-with-ordinal-preference-learning
title: Matrix factorization model of peer assessment with ordinal preference learning
description: The article proposes representing peer assessment as a sparse three-dimensional matrix (graders × answers × labels) and completing it via matrix factorization.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-30
---

# Matrix factorization model of peer assessment with ordinal preference learning

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes representing peer assessment as a sparse three-dimensional matrix (graders × answers × labels) and completing it via matrix factorization. Answers are encoded as bag-of-words vectors and graders and labels as one-hot vectors, all embedded in a shared k-dimensional Euclidean space. The model is trained using stochastic gradient descent on a maximum-margin loss over preference judgments (pairs of answers where one grader rated one higher than another), rather than by regression on raw grade values, reflecting an ordinal rather than cardinal view of grading.

## Accounts
<!-- How each source describes or uses the method -->
- **Matrix factorization model of peer assessment with ordinal preference learning**: The article proposes representing peer assessment as a sparse three-dimensional matrix (graders × answers × labels) and completing it via matrix factorization. Answers are encoded as bag-of-words vectors and graders and labels as one-hot vectors, all embedded in a shared k-dimensional Euclidean space. The model is trained using stochastic gradient descent on a maximum-margin loss over preference judgments (pairs of answers where one grader rated one higher than another), rather than by regression on raw grade values, reflecting an ordinal rather than cardinal view of grading. (Luaces et al. (2018))

### Claims
- [A matrix factorization model trained on sparse peer assessment data can predict grades for answers from students who did not participate in grading, reducing the grading burden on students.](../claims/matrix-factorization-predicts-grades-for-nongrading-students.md) [+M]
- [A multitask matrix factorization approach that jointly learns grades across multiple assessment labels outperforms a single-task (binary relevance) baseline that learns each label separately.](../claims/multitask-matrix-factorization-outperforms-single-task-baseline.md) [+M]

## Related Research Methods
-

## Key Sources
- Luaces, O., Díez, J., & Bahamonde, A. (2018). A peer assessment method to provide feedback, consistent grading and reduce students’ burden in massive teaching settings. Computers & Education. https://doi.org/10.1016/j.compedu.2018.08.006
