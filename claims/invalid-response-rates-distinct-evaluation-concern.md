---
type: claim
title: Response-format reliability is a distinct evaluation concern, with invalid response rates varying independently of model scale
description: Response-format reliability is a distinct evaluation concern, with invalid response rates varying independently of model scale
id: invalid-response-rates-distinct-evaluation-concern
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: luyao-zhu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.19088"
    title: "Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)"
    author: Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Response-format reliability is a distinct evaluation concern, with invalid response rates varying independently of model scale

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Invalid response rates across the 30 evaluated VLMs are highly skewed: most models fall below 1%, but Yi-VL-6b and DeepSeek-VL2-Tiny exceed 12%, and even GPT-5.6-Sol retains a 2.62% invalid rate, so response-format reliability constitutes a distinct evaluation concern alongside answer correctness. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)

`q2 · i?` · `design · r2`

Invalid response analysis across the 30 evaluated models (Figure 13), showing a highly skewed distribution. The article reports that Yi-VL-6b and DeepSeek-VL2-Tiny exceed 12% invalid rates while most models are below 1%, and that invalid rates are not determined solely by model scale.

> "Invalid responses are not determined solely by model scale: models within the same family vary substantially, and GPT-5.6-Sol retains a 2.62% invalid rate despite its strong task performance."

## Discussion


## Related Claims
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](vlm-performance-task-dependent-muse.md) — related
