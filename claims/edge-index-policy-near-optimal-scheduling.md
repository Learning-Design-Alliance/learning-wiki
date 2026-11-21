---
type: claim
title: The EDGE index policy is a near-optimal (1/(1+ϵ))-approximation to the optimal budgeted scheduling policy under separable gains
description: The EDGE index policy is a near-optimal (1/(1+ϵ))-approximation to the optimal budgeted scheduling policy under separable gains
id: edge-index-policy-near-optimal-scheduling
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: ananda-prakash-verma-2025
    resource: "https://doi.org/10.48550/arXiv.2508.07224"
    title: "Ananda Prakash Verma. (2025). EDGE: A Theoretical Framework for Misconception-Aware Adaptive Learning. arXiv:2508.07224. [doi:10.48550/arXiv.2508.07224](https://doi.org/10.48550/arXiv.2508.07224)"
    author: Ananda Prakash Verma
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# The EDGE index policy is a near-optimal (1/(1+ϵ))-approximation to the optimal budgeted scheduling policy under separable gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` If expected one-step gains decompose as a concave function of ability plus a convex retention penalty, with misconceptions entering additively via a bounded corrective term, the priority-index scheduler is a 1/(1+ϵ)-approximation to the optimal policy. [→ Ananda Prakash Verma 2025](#ananda-prakash-verma-2025)

## Evidence

### Ananda Prakash Verma 2025

Ananda Prakash Verma. (2025). EDGE: A Theoretical Framework for Misconception-Aware Adaptive Learning. arXiv:2508.07224. [doi:10.48550/arXiv.2508.07224](https://doi.org/10.48550/arXiv.2508.07224)

`q1 · i?` · `theoretical · r2`

Theorem 1, an analytical result derived via Lagrangian relaxation of the budgeted restless bandit under separability assumptions. The scheduler selects the B topics with highest priority index I combining gain, cost, and a hazard term for retrieval urgency.

> "If Gu,t(x) decomposes as a concave function of µ plus a convex penalty in ρ and misconceptions enter G additively via a bounded corrective term, then the index policy (10) is a 1 /(1 + ϵ)-approximation to the optimal policy for some ϵ = O(maxt var(∆Gu,t))."

## Discussion


## Related Claims
- [Counterfactual items reduce a targeted misconception posterior faster than items that do not violate the shortcut (proven bound)](counterfactual-advantage-over-standard-items.md) — related
- [Selecting 2PL items near ability equal to difficulty maximizes Fisher information, which EDGE respects while adding misconception-corrective gains](item-selection-near-ability-maximizes-information.md) — related
- [EdgeScore is monotone nondecreasing in its mastery, retention, pace, and confidence components and Lipschitz continuous (proven)](edgescore-monotone-lipschitz-guarantee.md) — related
