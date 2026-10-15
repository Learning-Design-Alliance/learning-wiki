---
type: claim
title: "The framework scales gracefully: MAE degrades by less than 2% from 10K to 100K EdNet interactions with near-linear processing time"
description: "The framework scales gracefully: MAE degrades by less than 2% from 10K to 100K EdNet interactions with near-linear processing time"
id: ednet-scalability-federated-diagnosis
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: yagna-manasa-boyapati-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02947"
    title: "Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)"
    author: Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The framework scales gracefully: MAE degrades by less than 2% from 10K to 100K EdNet interactions with near-linear processing time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On sampled EdNet subsets of increasing size (10K, 50K, 100K interactions), MAE degrades by less than 2% and processing time scales nearly linearly with student count. [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i?` · `design · r2`

Scalability analysis on EdNet (over 1.3 million student interactions, 188 knowledge topics), sampling three subsets of increasing size to allay concerns about small-scale evaluation of the primary benchmarks.

> "MAE degrades by less than 2% from the 10K to 100K setting, and processing time scales nearly linearly with student count, confirming practical deployability at scale beyond our primary benchmarks."

## Discussion


## Related Claims
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — related
