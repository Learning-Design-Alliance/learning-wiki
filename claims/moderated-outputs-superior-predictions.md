---
type: claim
title: Moderated outputs, obtained by marginalizing over parameter uncertainty, give superior test predictions to most-probable outputs in nearly all cases, especially for underdetermined networks
description: Moderated outputs, obtained by marginalizing over parameter uncertainty, give superior test predictions to most-probable outputs in nearly all cases, especially for underdetermined networks
id: moderated-outputs-superior-predictions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: moderate
newest_evidence: 1992
sources:
  - id: mackay-1992
    resource: "https://doi.org/10.1162/neco.1992.4.5.720"
    title: "David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720"
    author: David J. C. MacKay
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Moderated outputs, obtained by marginalizing over parameter uncertainty, give superior test predictions to most-probable outputs in nearly all cases, especially for underdetermined networks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 1992 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For a hundred trained networks, test error using moderated outputs was superior to that using most-probable outputs in nearly all cases, with the largest improvement for underdetermined networks. [→ MacKay 1992](#mackay-1992)

## Evidence

### MacKay 1992

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `causal · r1`

Numerical demonstration: several hundred networks with one hidden layer were trained on a two-class toy problem, and test error (value of G on 5000 test points) of "most probable" versus "moderated" outputs was compared for a hundred networks; moderated predictions were "in nearly all cases superior". No effect size is printed.

> "It can be seen that the predictions given by the moderated outputs are in nearly all cases superior. The improvement is most substantial for underdetermined networks with relatively poor performance."

## Discussion


## Related Claims
- [The mean marginal information gain criterion for active data selection prefers samples where the decision boundary is uncertain, improving on sampling on and near decision boundaries, but may give artifacts for poorly matched models](mean-marginal-information-gain-active-selection.md) — related
