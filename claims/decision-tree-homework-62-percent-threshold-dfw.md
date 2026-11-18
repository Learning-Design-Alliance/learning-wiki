---
type: claim
title: "A decision tree trained on Sample 2 week-2 data identifies a homework average of 62% as the highest-level threshold for classifying students at risk of a DFW outcome"
description: "A decision tree trained on Sample 2 week-2 data identifies a homework average of 62% as the highest-level threshold for classifying students at risk of a DFW outcome"
id: decision-tree-homework-62-percent-threshold-dfw
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: jie-yang-2020
    resource: "https://doi.org/10.1103/physrevphyseducres.16.020130"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A decision tree trained on Sample 2 week-2 data identifies a homework average of 62% as the highest-level threshold for classifying students at risk of a DFW outcome

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The week-2 decision tree for Sample 2 sets homework average above or below 62% at the root node and shows homework average, CGPA, and percent of hours completed as important for classifying DFW risk. [→ Jie Yang 2020](#jie-yang-2020)

## Evidence

### Jie Yang 2020

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Decision-tree analysis of the Sample 2 week-2 training dataset (Fig. 3). The article reports the tree "shows that homework average, CGPA, and the percent of hours completed were important" for DFW classification, with the root node splitting on a 62% homework threshold.

> "The tree shows that homework average, CGPA, and the percent of hours completed were important in the decision to classify a student at risk of a DFW outcome."

## Discussion


## Related Claims
- [Combining institutional and in-class data gave the highest DFW classification performance in Sample 2, improving over institutional-only models by 3% in week 1 to 18% in week 8](institutional-plus-inclass-data-highest-dfw-performance.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
