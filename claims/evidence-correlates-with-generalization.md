---
type: claim
title: The Bayesian evidence for classification solutions is moderately well correlated with their generalization (test error), though the correlation is imperfect
description: The Bayesian evidence for classification solutions is moderately well correlated with their generalization (test error), though the correlation is imperfect
id: evidence-correlates-with-generalization
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
---

# The Bayesian evidence for classification solutions is moderately well correlated with their generalization (test error), though the correlation is imperfect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 1992 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1995**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across alternative solutions trained on the same data, log evidence showed a moderately good correlation with test error, attributed speculatively to inaccurate evidence evaluation under the quadratic approximation. [→ MacKay 1992](#mackay-1992)

## Evidence

### MacKay 1992

David J. C. MacKay. (1992). The Evidence Framework Applied to Classification Networks. Neural Computation 4, 720-736. https://doi.org/10.1162/neco.1992.4.5.720

`q2 · i?` · `theoretical · r3`

Numerical evaluation of the evidence for alternative solutions (N = 300 training points), plotted against test error using moderated outputs; solutions with detected hidden-unit symmetries were omitted because evidence evaluation is unreliable for them. No correlation coefficient is printed.

> "Figure 5 shows the log evidence for the solutions against the test error, and it can be seen that a moderately good correlation is obtained. The correlation is not perfect."

## Discussion


## Related Claims
- [The correlation between evidence and generalization improves as the number of training data points increases](evidence-generalization-correlation-improves-with-data.md) — related
- [Ranking classification solutions requires Occam's razor: solutions with smallest data error do not generalize best](occam-razor-data-error-not-generalization.md) — related
