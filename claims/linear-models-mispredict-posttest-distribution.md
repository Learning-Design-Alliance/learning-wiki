---
type: claim
title: "OLS and hierarchical linear models over-predict post-test scores in the 30-60% range and under-predict higher scores on LASSO data"
description: "OLS and hierarchical linear models over-predict post-test scores in the 30-60% range and under-predict higher scores on LASSO data"
id: linear-models-mispredict-posttest-distribution
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: john-m-aiken-2021
    resource: "https://doi.org/10.1103/physrevphyseducres.17.020104"
    title: "John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)"
    author: John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# OLS and hierarchical linear models over-predict post-test scores in the 30-60% range and under-predict higher scores on LASSO data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The ordinary least squares and hierarchical models over predict scores in the 30-60% range and under predict higher scores, while the gradient boosted and mixed effects predicted distributions are close in shape to the true values. [→ John M. Aiken 2021](#john-m-aiken-2021)

## Evidence

### John M. Aiken 2021

John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)

`q2 · i?` · `theoretical · r3`

Visual comparison of out-of-sample predicted post-score distributions (kernel density estimates, Fig. 3) from the LASSO study's three models against true values, showing the boosted and mixed-effects curves track the true distribution while the linear models mispredict mid-range and high scores.

> "Visually, the out-of-sample post-score distribution predicted by the gradient boosted model and the mixed eﬀects model is close in shape to the true values (Fig. 3). The ordinary least squares and hierarchical models over predict scores in the 30-60% range and under predict higher scores."

## Discussion


## Related Claims
- [Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores](gradient-boosted-lower-error-lasso-posttest.md) — related
- [Out-of-sample residual patterns differ across model types: OLS under-predicts low scores, and the mixed-effects model does not produce normally distributed residuals](lasso-residual-patterns-model-type.md) — related
