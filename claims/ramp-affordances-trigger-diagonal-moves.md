---
type: claim
title: "Cell affordances determine agent movement: ramps trigger automatic diagonal transitions during path traversal"
description: "Cell affordances determine agent movement: ramps trigger automatic diagonal transitions during path traversal"
id: ramp-affordances-trigger-diagonal-moves
status: draft
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

# Cell affordances determine agent movement: ramps trigger automatic diagonal transitions during path traversal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` Landing on a downward-sloping ramp cell triggers an automatic move-diagonal-down, and landing on an ascending ramp cell triggers an automatic move-diagonal-up. [→ Abhishek Jaiswal 2026](#abhishek-jaiswal-2026)

## Evidence

### Abhishek Jaiswal 2026

Abhishek Jaiswal, Zoe Falomir. (2026). A Qualitative Model for Reasoning about Path and Support. arXiv preprint. https://arxiv.org/abs/2609.20349 [doi:10.48550/arxiv.2609.20349](https://doi.org/10.48550/arxiv.2609.20349)

`q1 · i?` · `design · r1`

Descriptive walkthrough in Section 6 of the agent's traversal in the Figure 1 example challenge: two move-right actions from the Knight's initial position lead onto ramp cells that trigger automatic diagonal moves, and the agent reaches the Princess. This is a worked example of the model's transition rules, not an empirical measurement.

> "It lands on a cell above the downward ramp, which automatically triggers amove-diagonal-downaction. Subsequently, it lands on an upward ramp, triggering amove-diagonal-upaction and enabling the agent to successfully reach the Princess."

## Discussion


## Related Claims

- [The hybrid qualitative-COM solver solves arbitrary Camelot Jr. configuration challenges within the game's problem space](camelot-jr-solver-solves-arbitrary-configurations.md)
- [Structural stability in the model is decided by a convex hull constraint on the resultant center of mass](convex-hull-com-stability-constraint.md)
