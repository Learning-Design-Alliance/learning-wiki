---
type: claim
title: A fractal-clustered link matrix yields a reasonable recall function but loses the decreasing term entry rate
description: A fractal-clustered link matrix yields a reasonable recall function but loses the decreasing term entry rate
id: fractal-matrix-solves-gamma-loses-rate-decline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2002
sources:
  - id: beatty-2002
    resource: "https://doi.org/10.1119/1.1482067"
    title: "Beatty, I. D., Gerace, W. J., & Dufresne, R. J. (2002). Measuring and Modeling Physics Students' Conceptual Knowledge Structures Through Term Association Times. UMass Physics Education Research Group. [doi:10.1119/1.1482067](https://doi.org/10.1119/1.1482067)"
    author: "Beatty, I. D., Gerace, W. J., & Dufresne, R. J."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A fractal-clustered link matrix yields a reasonable recall function but loses the decreasing term entry rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2002 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Combining a deterministic geometric-fractal matrix with random link strengths distributes selected link strengths across a wider range, but the resulting simulated data lack the systematic decrease in term entry rate seen in student data. [→ Beatty 2002](#beatty-2002)

## Evidence

### Beatty 2002

Beatty, I. D., Gerace, W. J., & Dufresne, R. J. (2002). Measuring and Modeling Physics Students' Conceptual Knowledge Structures Through Term Association Times. UMass Physics Education Research Group. [doi:10.1119/1.1482067](https://doi.org/10.1119/1.1482067)

`q1 · i?` · `design · r2`

Numerical model runs with a fractal matrix (e.g., N = 256, rho = 1, lambda = 0.01 and lambda = 0.4). With lambda = 0.4 the link strengths were approximately 0.45 and greater, softly peaked around 0.65, mappable to thinking times with a far less extreme recall function than the amorphous matrix required.

> "This approach to generating a synthetic link matrix, with a combination of fractal-algorithm and random link strengths, thus appears to solve the large- γ problem. The price paid is that the resulting distribution does not show a systematic decrease in term entry rate"

## Discussion


## Related Claims
- [An amorphous random link matrix requires an unacceptably extreme recall-function exponent](amorphous-matrix-requires-huge-gamma.md) — related
- [Community detection yields 15 communities (modularity ≈ 0.600), but some conceptually related physics terms are not clustered together](physics-term-communities-modularity-0-600.md) — related
- [FTE term entry rate decreases over the task while short times persist throughout](fte-entry-rate-decreases-clusters-persist.md) — related
