---
type: claim
title: Resource allocation across education sessions can be formulated and solved as a convex optimization problem maximizing terminal student sentiment
description: Resource allocation across education sessions can be formulated and solved as a convex optimization problem maximizing terminal student sentiment
id: convex-optimization-resource-allocation-sentiment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: yuchen-wang-2025
    resource: "https://doi.org/10.48550/arXiv.2509.23996"
    title: "Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)"
    author: Yuchen Wang, Pei-Duo Yu, Chee Wei Tan
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
  - id: yuchen-wang-2025-2
    resource: "https://doi.org/10.48550/arXiv.2509.23996"
    title: "Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)"
    author: Yuchen Wang, Pei-Duo Yu, Chee Wei Tan
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Resource allocation across education sessions can be formulated and solved as a convex optimization problem maximizing terminal student sentiment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under a concave priority function g and a concave objective, optimal allocation of theory and application resources per session is a convex optimization problem. [→ Yuchen Wang 2025](#yuchen-wang-2025)
`q1 i?` Under a power-function influence model, the optimizer produces more flexible allocation trajectories, particularly for students with strong resource dependencies. [→ Yuchen Wang 2025 (2)](#yuchen-wang-2025-2)

## Evidence

### Yuchen Wang 2025

Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)

`q1 · i?` · `theoretical · r2`

Analytical formulation of educational resource allocation over n sessions with normalized resource sums and a priority-ranking constraint, illustrated with 30 sessions and two resource types (Theory and Application). The formulation is conditional on concavity of g and f, as the article states the problem "can be formulated as a convex optimization problem" only under those conditions.

> "This problem can be formulated as a convex optimization problem [26], subject to the constraints on resource allocation and priority ranking as discussed above, provided the functiong(·)is concave andf(·)is chosen such that the objective is concave."

### Yuchen Wang 2025 (2)

Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)

`q1 · i?` · `design · r1`

Numerical optimization results shown in Fig. 7 for the power-function influence model (k = 0.5) with 30 sessions and two resource types; the article describes the trajectories as "more flexible allocation trajectories" than the linear model's, not as an analytic derivation.

> "As illustrated in Figure 7, the power function model produces more flexible allocation trajectories, particularly benefiting students with strong resource dependencies."

## Discussion


## Related Claims
- [Optimal AI allocation concentrates resources on components above a common residual-gap threshold, yielding over 14% greater gain than proportional allocation](optimal-ai-allocation-exceeds-proportional.md) — related
- [Additional AI-assisted learning budget yields diminishing returns in final mastery](diminishing-returns-ai-budget.md) — related
