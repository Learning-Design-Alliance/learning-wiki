---
type: claim
title: "Ranking classification solutions requires Occam's razor: solutions with smallest data error do not generalize best"
description: "Ranking classification solutions requires Occam's razor: solutions with smallest data error do not generalize best"
id: occam-razor-data-error-not-generalization
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
    kind: theoretical
    rigour: 3
---

# Ranking classification solutions requires Occam's razor: solutions with smallest data error do not generalize best

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 1992 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Plotting test error against data error for alternative solutions showed that the solutions with smallest data error do not generalize best, motivating a fit-versus-complexity balance. [→ MacKay 1992](#mackay-1992)

## Evidence

### MacKay 1992

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `theoretical · r3`

Numerical scatter of test error versus data error for alternative solutions to the toy classification problem, illustrating that best data fit is not best generalization; the article presents this as motivation for the Bayesian Occam's razor embodied in the evidence. No statistics are printed.

> "Figure 4 shows the test error (calculated using the moderated outputs) of the solutions against the data error, and the "Occam's razor" problem can be seen: the solutions with smallest data error do not generalize best."

## Discussion


## Related Claims
- [The Bayesian evidence for classification solutions is moderately well correlated with their generalization (test error), though the correlation is imperfect](evidence-correlates-with-generalization.md) — related
- [Surprisal-based model selection adds an Occam-factor penalty for superfluous fit-parameters on top of goodness of fit](kl-divergence-model-selection-occam-penalty.md) — related
