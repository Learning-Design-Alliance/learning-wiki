---
type: claim
title: "Satisfaction aspects are predictable from GTS-mapped and instructor-only feature sets at accuracies around 73%-78%, below the combined-feature results"
description: "Satisfaction aspects are predictable from GTS-mapped and instructor-only feature sets at accuracies around 73%-78%, below the combined-feature results"
id: gts-and-instructor-only-prediction-accuracies
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
    rigour: 2
---

# Satisfaction aspects are predictable from GTS-mapped and instructor-only feature sets at accuracies around 73%-78%, below the combined-feature results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using GTS features only, SVM achieved maximum accuracies of 76.01% (Q8), 77.85% (Q10), 76.10% (Q11), 75.34% (Q12), and k-NN (k=10) 75.94% (Q9); instructor-only features gave a maximum of 78.40% (Q10, Decision Table). [→ Farzana Afrin 2020](#farzana-afrin-2020)

## Evidence

### Farzana Afrin 2020

Farzana Afrin, Mohammad Saiedur Rahaman, Margaret Hamilton. (2020). Mining Student Responses to Infer Student Satisfaction Predictors. [doi:10.48550/arXiv.2006.07860](https://doi.org/10.48550/arXiv.2006.07860)

`q2 · i?` · `associational · r2`

Stratified cross-validated classification using nine features mapped to the six Good Teaching Score statements (GTS-1 to GTS-6 mapped to Q16-Q18, Q25, Q28, Q21-Q24, Q27), results in Table II. Instructor-only results (Q13-Q28) are reported separately in Table III.

> "the maximum prediction accuracies produced by the SVM algorithm for the satisfaction aspect features of Q8, Q10, Q11, and Q12 are 76.01%, 77.85%, 76.10% and 75.34% respectively. For the overall student satisfaction aspect represented by Q9, k-NN (k =10) produces the highest prediction accuracy of 75.94%."

## Discussion


## Related Claims
- [Combining course and instructor predictors yields the highest student satisfaction prediction accuracies, improving over GTS-only or instructor-only features by approximately 5%-7%](combined-course-instructor-predictors-highest-satisfaction-accuracy.md) — possibly the same claim (merge candidate)
- [The five satisfaction aspects are highly positively inter-correlated (coefficients above 0.8), and attendance correlates positively with perceived course difficulty (0.44)](satisfaction-aspects-high-intercorrelation.md) — related
