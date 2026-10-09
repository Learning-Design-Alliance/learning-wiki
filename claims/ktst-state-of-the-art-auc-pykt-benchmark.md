---
type: claim
title: KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011
description: KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011
id: ktst-state-of-the-art-auc-pykt-benchmark
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

# KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` KTST variants reach the highest AUC on the reported benchmark datasets, with the exception of Statics2011, and accuracy results are similar. [→ Kai Neubauer 2026](#kai-neubauer-2026)

## Evidence

### Kai Neubauer 2026

Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

`q2 · i?` · `design · r2`

Benchmark evaluation on the pyKT framework with eight publicly available datasets and 22 reproduced baselines; KTST (mean), (unique), and (MHSA) were compared against baselines using one-sided paired t-tests with Holm-Bonferroni correction. The article reports "state-of-the-art AUC results on all datasets except Statics2011"; no effect sizes are printed.

> "KTST models achieve state-of-the-art AUC results on all datasets except Statics2011. For accuracy, the results are similar."

## Discussion


## Related Claims
- [KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios](ktst-gains-largest-high-kc-ratio-datasets.md) — a narrower finding that bears on this claim
- [Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs](learnable-alibi-best-attention-ktst-ablation.md) — related
- [SAKT underperforms DKT on all nine datasets, contradicting previously reported results](sakt-underperforms-dkt-all-datasets.md) — related
- [Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation](mean-embeddings-beat-rasch-embeddings-as2009.md) — related
