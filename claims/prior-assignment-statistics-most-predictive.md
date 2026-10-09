---
type: claim
title: Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset
description: Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predicti...
id: prior-assignment-statistics-most-predictive
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: adam-c-sales-2023
    resource: "https://osf.io/k8ph9/"
    title: "Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/"
    author: Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In 5-fold cross-validation, prior assignment statistics predicted students' next-assignment performance best, prior student statistics second, and daily action history least; the combined dataset yielded higher-quality predictions than any individual dataset. [→ Adam C. Sales 2023](#adam-c-sales-2023)

## Evidence

### Adam C. Sales 2023

Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

`q2 · i?` · `causal · r2`

5-fold cross-validation of the four imputation models on remnant data (Table 2), reporting completion AUC (combined 0.770), completion accuracy, completion R², and problems-to-mastery MSE and R². Metrics are descriptive model-quality indices; no effect size is printed.

> "Based on Table 2, statistics on prior assignments were the most predictive of students' assignment performance, followed by the students' overall prior performance statistics, and then their daily action history, which was the least predictive of their performance on their next assignment. Combining these datasets together led to predictions of a higher quality than any individual dataset could achieve."

## Discussion


## Related Claims
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](remnant-data-type-contribution-variance.md) — related
