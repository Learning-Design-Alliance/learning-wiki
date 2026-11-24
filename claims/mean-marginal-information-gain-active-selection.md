---
type: claim
title: The mean marginal information gain criterion for active data selection prefers samples where the decision boundary is uncertain, improving on sampling on and near decision boundaries, but may give artifacts for poorly matched models
description: The mean marginal information gain criterion for active data selection prefers samples where the decision boundary is uncertain, improving on sampling on and near decision boundaries, but may give artifacts for poorly...
id: mean-marginal-information-gain-active-selection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: weak
newest_evidence: 1992
recheck_by: 1995
sources:
  - id: mackay-1992
    resource: "https://doi.org/10.1162/neco.1992.4.5.720"
    title: "David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720"
    author: David J. C. MacKay
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: mackay-1992-2
    resource: "https://doi.org/10.1162/neco.1992.4.5.720"
    title: "David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720"
    author: David J. C. MacKay
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# The mean marginal information gain criterion for active data selection prefers samples where the decision boundary is uncertain, improving on sampling on and near decision boundaries, but may give artifacts for poorly matched models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q2`
> **Currency** · newest study 1992 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1995**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The derived criterion shows a striking correlation between regions of moderated-output uncertainty and high expected information gain, offering improvements over boundary sampling. [→ MacKay 1992](#mackay-1992)
`q2 i?` The criterion can produce artifacts — long ridges of high utility far outside the region of interest — when applied to models poorly matched to the real world. [→ MacKay 1992 (2)](#mackay-1992-2)

## Evidence

### MacKay 1992

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `theoretical · r3`

Numerical demonstration (Figure 7): expected mean marginal information gain computed over a region of interest of 100 test-set points for the toy-problem network, plotted in grey scale; high-utility regions coincide with uncertain moderated outputs and sparse training data. No effect size is printed.

> "A striking correlation can be seen between the regions in which the moderated output is uncertain and regions of high expected information gain. In addition the expected information gain tends to increase in regions where the training data were sparse."

### MacKay 1992 (2)

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `theoretical · r3`

The same numerical demonstration revealed implausible high-utility ridges far from the data; the author favors the explanation that mean marginal information assumes the model is true, concluding it is likely most useful only for models well matched to the real world. The Taylor approximation was found never more than a factor of two wrong.

> "The regions of greatest expected information gain lie outside the region of interest to the right and left; these regions extend in long straight ridges hundreds of units away from the data."

## Discussion


## Related Claims
- [In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context](baseline-boundary-testing-homework-context.md) — related
- [Moderated outputs, obtained by marginalizing over parameter uncertainty, give superior test predictions to most-probable outputs in nearly all cases, especially for underdetermined networks](moderated-outputs-superior-predictions.md) — related
