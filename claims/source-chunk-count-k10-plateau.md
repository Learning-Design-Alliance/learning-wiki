---
type: claim
title: Section quality improves with more source chunks up to k=10, beyond which gains plateau
description: Section quality improves with more source chunks up to k=10, beyond which gains plateau
id: source-chunk-count-k10-plateau
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: jiawen-tao-2026
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Section quality improves with more source chunks up to k=10, beyond which gains plateau

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` From k=1 to k=10 source chunks, overall, structure, and educational quality scores improve by +0.22, +0.16, and +0.13 on a 1–5 rubric; from 10 to 30 chunks overall improves only +0.05. [→ Jiawen Tao 2026](#jiawen-tao-2026)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Intrinsic-quality ablation: 400 individual sections generated with k∈{1,3,5,10,20,30} source chunks, judged by Gemini-3.1-Pro on a fixed 1–5 rubric at the section level. The article reports the printed score deltas.

> "From k=1 to k=10, overall, structure, and educational scores improve by +0.22, +0.16, and +0.13. From 10 to 30 chunks, overall improves only +0.05 while breadth and depth change by <0.02 ; k=20 nearly doubles input for a +0.009 overall gain."

## Discussion


## Related Claims
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
