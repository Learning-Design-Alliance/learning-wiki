---
type: claim
title: Structural stability in the model is decided by a convex hull constraint on the resultant center of mass
description: Structural stability in the model is decided by a convex hull constraint on the resultant center of mass
id: convex-hull-com-stability-constraint
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: abhishek-jaiswal-2026
    resource: "https://doi.org/10.48550/arxiv.2609.20349"
    title: "Abhishek Jaiswal, Zoe Falomir. (2026). A Qualitative Model for Reasoning about Path and Support. arXiv preprint. https://arxiv.org/abs/2609.20349 [doi:10.48550/arxiv.2609.20349](https://doi.org/10.48550/arxiv.2609.20349)"
    author: Abhishek Jaiswal, Zoe Falomir
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Structural stability in the model is decided by a convex hull constraint on the resultant center of mass

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` A sub-stack of blocks is stable if and only if its resultant center of mass lies within the horizontal bounds of its supporting cells. [→ Abhishek Jaiswal 2026](#abhishek-jaiswal-2026)

## Evidence

### Abhishek Jaiswal 2026

Abhishek Jaiswal, Zoe Falomir. (2026). A Qualitative Model for Reasoning about Path and Support. arXiv preprint. https://arxiv.org/abs/2609.20349 [doi:10.48550/arxiv.2609.20349](https://doi.org/10.48550/arxiv.2609.20349)

`q1 · i?` · `design · r1`

Analytical stability formalization (Section 5): the solver aggregates loads and moments recursively from top to bottom of each stack, computes an effective COM per sub-stack, and applies the convex hull criterion; for bridges, a lever rule distributes weight between the two outermost supports. This is a printed derivation, not an empirical test.

> "A sub-stack of blocks is considered stable if, and only if, its resultant center of mass is contained within the bounds of its support geometry"

## Discussion


## Related Claims

- [The physical stability of material artifacts such as stacked tickertape strips and worksheets stabilizes students' attention, action, and knowledge use](material-artifact-stability-stabilizes-thinking.md) — related
- Changes in the constraints of activity (attention, object location, interaction patterns) provide opportunities for new locally stable patterns of thinking to take hold — related
- [Material arrangement of artifacts (strips centered and ordered by length, worksheets held close) affords and stabilizes the initial pattern of activity; later decentralization enables new patterns](material-arrangement-affords-stability.md) — related
- [Cell affordances determine agent movement: ramps trigger automatic diagonal transitions during path traversal](ramp-affordances-trigger-diagonal-moves.md)
- [The hybrid qualitative-COM solver solves arbitrary Camelot Jr. configuration challenges within the game's problem space](camelot-jr-solver-solves-arbitrary-configurations.md)
