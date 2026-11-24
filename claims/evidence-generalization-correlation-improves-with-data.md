---
type: claim
title: The correlation between evidence and generalization improves as the number of training data points increases
description: The correlation between evidence and generalization improves as the number of training data points increases
id: evidence-generalization-correlation-improves-with-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: weak
newest_evidence: 1992
sources:
  - id: mackay-1992
    resource: "https://doi.org/10.1162/neco.1992.4.5.720"
    title: "David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720"
    author: David J. C. MacKay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The correlation between evidence and generalization improves as the number of training data points increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 1992 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Plotting test error against log evidence for N = 150, 300 and 600 data points showed the correlation improving with the amount of data. [→ MacKay 1992](#mackay-1992)

## Evidence

### MacKay 1992

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `design · r2`

Numerical comparison across training-set sizes (N = 150, 300, 600) for a typical 10-hidden-unit network, showing the evidence-generalization correlation strengthening with more data; the article notes only about 25% of data points fall in informative decision regions. No correlation coefficient is printed.

> "Figure 6 explores the dependence of the correlation between evidence and generalization on the amount of data. It can be seen that the correlation improves as the number of data points in the test set increases."

## Discussion


## Related Claims
- [The Bayesian evidence for classification solutions is moderately well correlated with their generalization (test error), though the correlation is imperfect](evidence-correlates-with-generalization.md) — related
