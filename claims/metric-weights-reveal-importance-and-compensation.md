---
type: claim
title: "Metric weights reveal each metric's relative importance and expose compensation between metrics, allowing trainees to see how strong performance on one metric offsets weakness in another"
description: "Metric weights reveal each metric's relative importance and expose compensation between metrics, allowing trainees to see how strong performance on one metric offsets weakness in another"
id: metric-weights-reveal-importance-and-compensation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: mirchi-n-2020
    resource: "https://doi.org/10.1371/journal.pone.0229596"
    title: "Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596"
    author: Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Metric weights reveal each metric's relative importance and expose compensation between metrics, allowing trainees to see how strong performance on one metric offsets weakness in another

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Because the model output combines metrics with weights, the Virtual Operative Assistant can show how good performance in one metric may compensate for poor performance in another. [→ Mirchi N 2020](#mirchi-n-2020)

## Evidence

### Mirchi N 2020

Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596

`q2 · i?` · `design · r2`

Authors' analysis of the platform's individual metric scoring feature (Discussion): a metric whose weight has a larger magnitude "will play a greater role in the algorithm's decision-making process", and metric-wise feedback exposes overcompensation situations.

> "The Virtual Operative Assistant not only reveals significant metrics, but also incorporates the relationship between different metrics rather than assessing each metric individually. This allows trainees to understand how good performance in one metric may be compensating for a poor performance in another."

## Discussion


## Related Claims
- [Blinded expert OSATS ratings favored the VOA group on overall performance and economy of movement despite measured efficiency losses, exposing a limitation of granular metric-based assessment](osats-economy-of-movement-discrepancy.md) — related
- [Regression tree and non-linear optimization analyses identify Casper as the dominant admission metric, with optimal weights of 0.84 for Casper and 0.16 for GPA](casper-dominant-admission-weight-0-84.md) — related
