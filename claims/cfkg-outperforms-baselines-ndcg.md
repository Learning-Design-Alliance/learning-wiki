---
type: claim
title: The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40
description: The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40
id: cfkg-outperforms-baselines-ndcg
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

# The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On offline NDCG over historical interaction logs, the proposed CF–KG model consistently outperforms all eight baselines, converging to about 0.625, roughly a 7–8% relative improvement over the best neural baseline. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Offline comparative experiment on the English subset of the MARS dataset (4,800 users, 14,200 resources, 132,000 interactions) comparing CF–KG against eight baselines under the same protocol. The text reports the model "steadily increases to about 0.625 at epoch 40" while the DL baseline converges near 0.581; no standardized effect size is printed.

> "The proposed CF–KG model consistently outperforms all baselines. It starts from a competitive NDCG and steadily increases to about 0.625 at epoch 40, which corresponds to roughly a 7–8% relative improvement over the best neural baseline."

## Discussion


## Related Claims
- [CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT](cfkg-best-across-modalities.md) — related
- [The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders](cfkg-highest-coverage-cda.md) — related
- [The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training](cfkg-highest-hit-rate.md) — related
- [Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals](cfkg-component-ablation-complementary.md) — related
- [Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)](cfkg-robust-modality-removal.md) — related
