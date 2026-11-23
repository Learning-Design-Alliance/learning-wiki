---
type: claim
title: A counting construction proves that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice
description: A counting construction proves that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice
id: synchronized-global-pacing-insufficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: siddharth-aphale-2026
    resource: "https://doi.org/10.48550/arXiv.2607.26417"
    title: "Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)"
    author: Siddharth Aphale, Ayushman Singh
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# A counting construction proves that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` For every K > 1 there exists a two-context, two-level scaffold curriculum with per-context budget K+1 that a context-local schedule solves while every synchronized global schedule fails at least one context. [→ Siddharth Aphale 2026](#siddharth-aphale-2026)

## Evidence

### Siddharth Aphale 2026

Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)

`q1 · i?` · `causal · r2`

Analytical proof (Proposition 1, Appendix C.1): a synchronized schedule gives both contexts the same assisted count, but context a requires n1 = 1 and context b requires n1 = K > 1, so every synchronized schedule fails at least one context.

> "Every K >1 admits a two-context, two-level scaffold curriculum with per-context budgetK+ 1 such that a context-local schedule solves both contexts, while every synchronized global schedule fails at least one context."

## Discussion


## Related Claims
- [Scaffold access improves sparse-reward learning across six navigation and manipulation settings, enabling success in three where unassisted target-start training fails within the budget](scaffold-access-improves-sparse-reward-learning.md) — related
- [Pacing granularity must match heterogeneity: pooling contexts that learn at different rates under one label collapses the hard band, which per-context pacing handles](pacing-granularity-matches-heterogeneity.md) — related
- [Timing of support poses the assistance dilemma, and no empirically validated principles yet exist for when and how much support to give collaborating students](assistance-dilemma-timing-no-validated-principles.md) — related
- [A broad spectrum of system maturity exists across OPRA systems](opra-system-maturity-spectrum.md) — related
