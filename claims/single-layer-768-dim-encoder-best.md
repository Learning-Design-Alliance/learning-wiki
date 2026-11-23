---
type: claim
title: Single-layer sequence encoders with 768-dimensional embeddings consistently achieved the best probe performance; added transformer depth degraded results
description: Single-layer sequence encoders with 768-dimensional embeddings consistently achieved the best probe performance; added transformer depth degraded results
id: single-layer-768-dim-encoder-best
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: siddhartha-pradhan-2026
    resource: "https://doi.org/10.48550/arXiv.2604.08693"
    title: "Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar. (2026). Towards Generalizable Representations of Mathematical Solution Strategies. arXiv. [doi:10.48550/arXiv.2604.08693](https://doi.org/10.48550/arXiv.2604.08693)"
    author: Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Single-layer sequence encoders with 768-dimensional embeddings consistently achieved the best probe performance; added transformer depth degraded results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across encoder configurations, models with L=1 and k=768 consistently achieved the best performance. [→ Siddhartha Pradhan 2026](#siddhartha-pradhan-2026)

## Evidence

### Siddhartha Pradhan 2026

Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar. (2026). Towards Generalizable Representations of Mathematical Solution Strategies. arXiv. [doi:10.48550/arXiv.2604.08693](https://doi.org/10.48550/arXiv.2604.08693)

`q2 · i?` · `design · r2`

Grid search over 36 configurations (three frozen encoders, transformer layers L in {1,2,4}, embedding dimension k in {128,256,512,768}), each trained with early stopping on validation loss. The article reports "models withL= 1 andk= 768 consistently achieved the best performance."

> "models withL= 1 andk= 768 consistently achieved the best performance."

## Discussion


## Related Claims
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [Reducing BERT to a single encoder layer (BERT (1)) decreases classification performance by .05 points in weighted F1 average compared to the full 12-layer model](bert-encoder-layer-count-affects-classification-performance.md) — reports the opposite
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — related
- [The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones](frozen-layer-count-depends-on-data-complexity-and-volume.md) — related
