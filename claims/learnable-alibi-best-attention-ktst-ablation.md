---
type: claim
title: Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs
description: Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs
id: learnable-alibi-best-attention-ktst-ablation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: kai-neubauer-2026
    resource: "https://github.com/kainbr/kt_set_transformers"
    title: "Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers"
    author: Kai Neubauer, Yannick Rudolph, and Ulf Brefeld
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` In an ablation on AS2009, learnable ALiBi outperformed standard MHA with positional embeddings, AKT's attention mechanism, and fixed ALiBi, and setting query equal to key in cross-attention is favorable. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q2 · i?` · `causal · r?`

Ablation study on the AS2009 dataset comparing four attention mechanisms and cross-attention variants, each tested against learnable ALiBi (q=k) with one-sided paired t-tests and Holm-Bonferroni correction (alpha = 0.05). Learnable ALiBi (q=k) reached AUC 0.7993; no effect sizes are printed.

> "We observe thatlearnable ALiBiachieves the best performance and that using the same to- ken for bothkeyandqueryin the cross-attention is favorable."

## Discussion


## Related Claims
- [KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios](ktst-gains-largest-high-kc-ratio-datasets.md) — related
- [KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011](ktst-state-of-the-art-auc-pykt-benchmark.md) — related
- [Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation](mean-embeddings-beat-rasch-embeddings-as2009.md) — related
