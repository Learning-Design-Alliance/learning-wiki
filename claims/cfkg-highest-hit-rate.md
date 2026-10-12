---
type: claim
title: The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training
description: The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training
id: cfkg-highest-hit-rate
status: draft
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

# The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On offline hit rate, the CF–KG model outperforms all baselines, starting from 0.718 and reaching 0.751 at epoch 40, while MLP-DNN reaches 0.710 and DL 0.721. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Hit-rate comparison across 40 training epochs on the preprocessed MARS English subset, reported in Fig. 3. The article prints baseline values (HMM 0.642 to 0.673; MLP 0.710; DL 0.721) and states the hybrid "starting from 0.718 and reaching 0.751"; no effect size is reported.

> "The CF-KG hybrid model outperforms all others, starting from 0.718 and reaching 0.751, which marks a notable performance advantage across the entire training process."

## Discussion


## Related Claims
- [CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT](cfkg-best-across-modalities.md) — related
- [The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders](cfkg-highest-coverage-cda.md) — related
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
- [Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals](cfkg-component-ablation-complementary.md) — related
