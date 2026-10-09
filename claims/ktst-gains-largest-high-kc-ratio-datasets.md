---
type: claim
title: KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios
description: KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios
id: ktst-gains-largest-high-kc-ratio-datasets
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
    kind: design
    rigour: 2
---

# KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Differences between KTST and expanded-representation baselines are largest on EdNet, AL2005, and AS2009, the datasets with the highest average knowledge-components-per-question ratios. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q2 · i?` · `design · r2`

Benchmark results on EdNet, AL2005, and AS2009, which have average knowledge-components-per-question ratios of 2.24, 1.36, and 1.19 respectively. The article reports differences "most pronounced on EdNet", where only IEKT, LPKT, and QIKT approach KTST results; no effect sizes are printed.

> "The results confirm our hypothesis, with differences being most pronounced on EdNet, where IEKT, LPKT, and QIKT are the only baselines that are in the same ballpark as KTST results."

## Discussion


## Related Claims
- [The expanded interaction representation introduces label leakage and a training-evaluation distribution shift in prior knowledge tracing work](expanded-representation-label-leakage-distribution-shift.md) — related
- [Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation](mean-embeddings-beat-rasch-embeddings-as2009.md) — related
- [Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs](learnable-alibi-best-attention-ktst-ablation.md) — related
- [KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011](ktst-state-of-the-art-auc-pykt-benchmark.md) — a broader claim this one bears on
