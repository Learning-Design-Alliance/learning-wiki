---
type: claim
title: CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT
description: CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT
id: cfkg-best-across-modalities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: bin-liu-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100678"
    title: "Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678"
    author: Bin Liu, Xiaoli Sun, Jia Song
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When the test set is partitioned by dominant modality, CF–KG achieves the best NDCG/HR on all three subsets (0.602/0.738 text, 0.624/0.756 video, 0.596/0.742 interactive), modestly but consistently above KGAT. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Modality-aware evaluation (Table 5) partitioning the test set into text, video, and interactive subsets, comparing eight baselines plus CF–KG under the same protocol. The article states improvements over KGAT are "modest but consistent"; no effect size is printed.

> "CF–KG achieves the best NDCG/HR results, namely 0.602/0.738 for text, 0.624/0.756 for video, and 0.596/0.742 for interactive resources. Compared with KGAT, the improvements are modest but consistent"

## Discussion


## Related Claims
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
- [Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)](cfkg-robust-modality-removal.md) — related
- [The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training](cfkg-highest-hit-rate.md) — related
- [Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals](cfkg-component-ablation-complementary.md) — related
- [The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders](cfkg-highest-coverage-cda.md) — related
