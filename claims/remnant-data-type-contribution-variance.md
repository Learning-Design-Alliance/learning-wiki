---
type: claim
title: Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model
description: Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model
id: remnant-data-type-contribution-variance
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

# Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Comparing ReLOOP/ReLOOP+ fitted with different remnant-trained imputation models, the action-level model performed worst, the combined ensemble produced the greatest variance decrease, and the assignment-level model was nearly as good as the combined model. [→ Adam C. Sales 2023](#adam-c-sales-2023)

## Evidence

### Adam C. Sales 2023

Adam C. Sales, Ethan B. Prihar, Johann A. Gagnon-Bartsch, Neil T. Heffernan. (2023). Using Auxiliary Data to Boost Precision in the Analysis of A/B Tests on an Online Educational Platform: New Data and New Results. Journal of Educational Data Mining, Volume 15, No 2. https://osf.io/k8ph9/

`q2 · i?` · `causal · r2`

Numerical comparison (Figure 4) of sampling-variance ratios for ReLOOP and ReLOOP+ using imputation models trained on daily actions, student aggregates, prior assignments, or their combination, across the 227 contrasts. The pattern was consistent across the three comparisons shown; no effect size is printed.

> "Comparing across models fit in the remnant, the action-level model performed the worst, while the combined model was responsible for the greatest decrease in sampling variance. Interestingly, the assignment-level model performed nearly as well as the combined model, suggesting that action- and student-level data did not contribute substantially."

## Discussion


## Related Claims
- [Prior assignment statistics were the most predictive remnant data type for assignment performance, followed by prior student statistics, with daily action history least predictive; combining datasets improved predictions over any single dataset](prior-assignment-statistics-most-predictive.md) — related
- [Remnant-based adjustment still adds precision beyond within-sample-only machine-learning adjustment (LOOP), equivalent to roughly a 10–20% sample-size increase in about half of cases](reloop-gains-beyond-within-sample-loop.md) — related
- [Remnant-based covariate adjustment (ReLOOP/ReLOOP+) reduces estimated sampling variance in A/B effect estimates relative to t-tests, equivalent to roughly a 20% average sample-size increase](reloop-remnant-imputation-variance-reduction-vs-ttest.md) — related
