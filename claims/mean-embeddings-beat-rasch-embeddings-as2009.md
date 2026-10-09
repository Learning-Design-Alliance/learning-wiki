---
type: claim
title: "Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation"
description: "Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation"
id: mean-embeddings-beat-rasch-embeddings-as2009
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: kai-neubauer-2026
    resource: "https://github.com/kainbr/kt_set_transformers"
    title: "Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers"
    author: Kai Neubauer, Yannick Rudolph, and Ulf Brefeld
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Mean embeddings with AKT's attention mechanism improve over the AKT baseline with Rasch embeddings on AS2009 in both AUC and accuracy. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q2 · i?` · `causal · r2`

Observation from the ablation study on AS2009: swapping AKT's Rasch embeddings for permutation-invariant mean embeddings raised AUC from 0.7840 to 0.7958 and accuracy from 0.7383 to 0.7464. The authors read this as "empirical evidence against the expanded representation"; no effect sizes are printed.

> "Mean embeddings with AKT’s attention mechanism im- prove over the AKT baseline with Rasch embeddings on AS2009 (AUC:0.7958±0.0011over 0.7840±0.0016; Accuracy:0.7464±0.0009over0.7383±0.0020)."

## Discussion


## Related Claims
- [The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work](expanded-representation-label-leakage-distribution-shift.md) — related
- [KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios](ktst-gains-largest-high-kc-ratio-datasets.md) — related
- [Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs](learnable-alibi-best-attention-ktst-ablation.md) — related
- [KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011](ktst-state-of-the-art-auc-pykt-benchmark.md) — related
