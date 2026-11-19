---
type: claim
title: "Combining course and instructor predictors yields the highest student satisfaction prediction accuracies, improving over GTS-only or instructor-only features by approximately 5%-7%"
description: "Combining course and instructor predictors yields the highest student satisfaction prediction accuracies, improving over GTS-only or instructor-only features by approximately 5%-7%"
id: combined-course-instructor-predictors-highest-satisfaction-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: farzana-afrin-2020
    resource: "https://doi.org/10.48550/arXiv.2006.07860"
    title: "Farzana Afrin, Mohammad Saiedur Rahaman, Margaret Hamilton. (2020). Mining Student Responses to Infer Student Satisfaction Predictors. [doi:10.48550/arXiv.2006.07860](https://doi.org/10.48550/arXiv.2006.07860)"
    author: Farzana Afrin, Mohammad Saiedur Rahaman, Margaret Hamilton
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Combining course and instructor predictors yields the highest student satisfaction prediction accuracies, improving over GTS-only or instructor-only features by approximately 5%-7%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prediction accuracies for the five satisfaction aspects are highest when course (Q1-Q7) and instructor (Q13-Q28) predictors are combined, an improvement of approximately 5%-7% over GTS-only or instructor-only feature sets. [→ Farzana Afrin 2020](#farzana-afrin-2020)

## Evidence

### Farzana Afrin 2020

Farzana Afrin, Mohammad Saiedur Rahaman, Margaret Hamilton. (2020). Mining Student Responses to Infer Student Satisfaction Predictors. [doi:10.48550/arXiv.2006.07860](https://doi.org/10.48550/arXiv.2006.07860)

`q2 · i?` · `associational · r1`

Cross-validated classification experiments on the UCI student evaluation dataset (5820 responses) using Weka classifiers (SVM, MLP, Decision Tree, Random Forest, Decision Table, k-NN). Combined features gave SVM accuracies of "84.16%, 84.02%, 80.82% and 79.86%" for Q8, Q10, Q11, Q12 and Random Forest 80.86% for Q9.

> "the combination of course and instructor related predictors produces the highest prediction accuracies for student satisfaction prediction. In other words, an improvement of prediction accuracies can be seen by considering the course and instructor related predictors in comparison to results using only GTS features or only instructor related features. This improvement is approximately 5%-7% across all the aspects of student satisfaction."

## Discussion


## Related Claims
- [Satisfaction aspects are predictable from GTS-mapped and instructor-only feature sets at accuracies around 73%-78%, below the combined-feature results](gts-and-instructor-only-prediction-accuracies.md) — possibly the same claim (merge candidate)
