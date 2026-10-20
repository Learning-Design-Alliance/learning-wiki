---
type: claim
title: Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)
description: Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)
id: cfkg-robust-modality-removal
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

# Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Under modality ablation, CF–KG shows moderate degradation: removing text drops NDCG to 0.593 and HR to 0.721 (about 5.1% and 4.0% relative decreases), while removing interactive features has the smallest impact. [→ Bin Liu 2026](#bin-liu-2026)

## Evidence

### Bin Liu 2026

Bin Liu, Xiaoli Sun, Jia Song. (2026). A hybrid collaborative filtering and knowledge graph-based cross-domain recommendation method for multimodal teaching resources. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100678

`q2 · i?` · `design · r2`

Modality ablation study on CF–KG (Table 6) with three degraded variants (no text, no video, no interactive) on the same test set. Removing video yields NDCG 0.598/HR 0.727; removing interactive yields 0.604/0.731 with relative drops below 3.5 percent. No standardized effect size is printed.

> "When text features are removed, NDCG drops to 0.593 and HR to 0.721. This corresponds to relative decreases of approximately 5.1 percent in NDCG and 4.0 percent in HR, indicating that textual information contributes substantially to accurate ranking."

## Discussion


## Related Claims
- [CF–KG achieves the best NDCG and hit rate on text, video, and interactive resource subsets, with modest but consistent gains over KGAT](cfkg-best-across-modalities.md) — related
- [Both CF-only and KG-only ablated variants underperform the full CF–KG model, indicating complementary behavioral and semantic signals](cfkg-component-ablation-complementary.md) — related
- [The CF–KG model attains the highest coverage (0.736) and cross-domain accuracy (0.741) among all compared recommenders](cfkg-highest-coverage-cda.md) — related
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
