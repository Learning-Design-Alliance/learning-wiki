---
type: claim
title: Linear regression on continuous laboratory grades fit poorly (R2 = 0.056), motivating the binary median-split classification outcome
description: Linear regression on continuous laboratory grades fit poorly (R2 = 0.056), motivating the binary median-split classification outcome
id: linear-regression-poor-fit-lab-grades-median-split
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2019
sources:
  - id: robert-solli-2019
    resource: "https://doi.org/10.1119/perc.2018.pr.solli"
    title: "Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)"
    author: Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Linear regression on continuous laboratory grades fit poorly (R2 = 0.056), motivating the binary median-split classification outcome

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Linear regression models on the laboratory grades fit ill (R2 = 0.056), which is why the outcome was represented as a binary value split at the median. [→ Robert Solli 2019](#robert-solli-2019)

## Evidence

### Robert Solli 2019

Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)

`q2 · i?` · `associational · r2`

Secondary analysis in the methods discussion: representing the dependent variable as a median-split binary value 'might be ill suited to the problem', but was chosen because linear regression on the grades fit ill (R2 = 0.056).

> "Additionally the eﬀect of representing the dependent variable as a binary value split at the median of the score might be ill suited to the problem; however, this was chosen due to ill ﬁtting linear regression models (R2 = 0.056)."

## Discussion


## Related Claims
- [Lr Clickstream Features Fail Predict Lab Performance](lr-clickstream-features-fail-predict-lab-performance.md)
- [Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)](keystroke-classification-weak-auc.md) — related
