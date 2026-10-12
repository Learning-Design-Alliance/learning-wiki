---
type: claim
title: Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals
description: Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals
id: cfkg-component-ablation-complementary
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

# Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Removing the knowledge graph (CF-only, NDCG 0.584, HR 0.724) hurts more than removing collaborative filtering (KG-only, NDCG 0.604, HR 0.735); both fall below the full model's 0.625/0.751. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Component ablation (Table 7) comparing CF-only, KG-only, and the full CF–KG model under the same dataset split and protocol. The article reports KG-only reaches NDCG 0.604 and HR 0.735, better than CF-only but below the full model; no standardized effect size is printed.

> "The CF-only variant achieves an NDCG of 0.584 and an HR of 0.724, corresponding to decreases of 6.56% and 3.60%, respectively."

## Discussion


## Related Claims
- [CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT](cfkg-best-across-modalities.md) — related
- [Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)](cfkg-robust-modality-removal.md) — related
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders](cfkg-highest-coverage-cda.md) — related
- [The CF–KG hybrid model achieves the highest hit rate among all compared methods, rising from 0.718 to 0.751 across training](cfkg-highest-hit-rate.md) — related
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
