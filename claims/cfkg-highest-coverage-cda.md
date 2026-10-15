---
type: claim
title: The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders
description: The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders
id: cfkg-highest-coverage-cda
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

# The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On system-level coverage and cross-domain accuracy, the CF–KG model significantly outperforms all baselines, achieving Coverage of 0.736 and CDA of 0.741, versus up to 0.648 Coverage and 0.692 CDA for neural baselines. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Coverage and cross-domain accuracy comparison across all methods on the MARS English subset, reported in Fig. 4. Traditional models show Coverage below 0.60 and CDA around 0.62; neural models reach 0.648 and 0.692; the hybrid achieves the printed maxima. No standardized effect size is reported.

> "The proposed CF-KG model significantly outperforms all others, achieving the highest scores in both Coverage (0.736) and CDA (0.741)."

## Discussion


## Related Claims
- [CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT](cfkg-best-across-modalities.md) — related
- [The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training](cfkg-highest-hit-rate.md) — related
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
- [Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals](cfkg-component-ablation-complementary.md) — related
- [Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)](cfkg-robust-modality-removal.md) — related
