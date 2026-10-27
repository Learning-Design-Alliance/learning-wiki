---
type: design
id: spreadsheet-cluster-grading-setup
title: Modular spreadsheet-based grading setup combining clustering, sampled manual grading, classification, and full review
description: A reusable grading workflow in which student answers are clustered (k-means on lemmatized unigrams), a sample is manually graded as training data, per-question classifiers score the remaining answers, and all scores a...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: rebecka-weegar-peter-idestam-almquist-2024
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
---

# Modular spreadsheet-based grading setup combining clustering, sampled manual grading, classification, and full review

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A reusable grading workflow in which student answers are clustered (k-means on lemmatized unigrams), a sample is manually graded as training data, per-question classifiers score the remaining answers, and all scores are reviewed in cluster order. The authors propose "a modular and reusable grading setup that can be used in a course setting without the need for specifically developed interfaces for grading"; a spreadsheet program displayed answers, scores, and comments.

## Design Implications

### Context
#### Requirements
- Clustering must allow manually setting the number of clusters and provide a measure of representativeness for selecting training answers
#### Constraints
- Evaluated on short answers (average 13 tokens) from one introductory computer science exam, mainly in Swedish

### Target Learners
- higher education students in comparatively large courses

### Learning Goals
- efficient and correct grading of short-answer exam questions

### Claims
- [Clustering Plus Score Suggestions Reduce Grading Time](../claims/clustering-plus-score-suggestions-reduce-grading-time.md) [+M]
- [Cluster Instance Sampling Minimizes Grading Work](../claims/cluster-instance-sampling-minimizes-grading-work.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1
