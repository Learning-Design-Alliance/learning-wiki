---
type: claim
title: "Pacing granularity must match heterogeneity: pooling contexts that learn at different rates under one label collapses the hard band, which per-context pacing handles"
description: "Pacing granularity must match heterogeneity: pooling contexts that learn at different rates under one label collapses the hard band, which per-context pacing handles"
id: pacing-granularity-matches-heterogeneity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: siddharth-aphale-2026
    resource: "https://doi.org/10.48550/arXiv.2607.26417"
    title: "Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)"
    author: Siddharth Aphale, Ayushman Singh
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: siddharth-aphale-2026-2
    resource: "https://doi.org/10.48550/arXiv.2607.26417"
    title: "Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)"
    author: Siddharth Aphale, Ayushman Singh
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Pacing granularity must match heterogeneity: pooling contexts that learn at different rates under one label collapses the hard band, which per-context pacing handles

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a PickAndPlace bank with bimodal goal height under one label, the pooled group frontier reaches worst-band AUC 0.000 while the per-context controller reaches 0.701. [→ Siddharth Aphale 2026](#siddharth-aphale-2026)
`q2 i?` Group-level pacing works when labels reflect actual learning differences: on Meta-World the group frontier wins all six seeds, while on the constructed conflict the controller beats it in sample efficiency. [→ Siddharth Aphale 2026 (2)](#siddharth-aphale-2026-2)

## Evidence

### Siddharth Aphale 2026

Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)

`q2 · i?` · `causal · r2`

Within-group conflict simulation over six seeds with SAC+HER: the pooled frontier's worst-band AUC of 0.000 versus the controller's 0.701, a paired difference of +0.69 [0.47,0.74]; the controller wins every paired worst-band comparison.

> "In a PickAndPlace bank with bimodal goal height under one label, the pooled frontier has a worst-band AUC of 0.000, while our controller reaches 0.701 (paired ∆ = +0.69 [0.47,0.74] over six seeds; Fig. 4, right)."

### Siddharth Aphale 2026 (2)

Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. [doi:10.48550/arXiv.2607.26417](https://doi.org/10.48550/arXiv.2607.26417)

`q2 · i?` · `causal · r2`

Two six-seed conflict simulations comparing per-context and oracle-label group frontiers: the controller leads on the constructed conflict (0.378 vs 0.229) while the group frontier leads on Meta-World (+0.10 [0.03,0.22]).

> "On the constructed conflict, our controller is more sample-efficient than the oracle-label group frontier (worst-group AUC 0.378 vs. 0.229; paired ∆ = +0.18 [0.04,0.29] over six seeds). On Meta-World, the group frontier wins all six seeds (group frontier minus our controller: ∆ = +0.10 [0.03,0.22] )."

## Discussion


## Related Claims
- Local bidirectional frontiers drive the conflict gain: calibrated sampling and antistall improve reliability, and retreat matters on coarse ladders — related
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [A counting construction proves that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice](synchronized-global-pacing-insufficiency.md) — related
