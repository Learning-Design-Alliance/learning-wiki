---
type: claim
title: Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books
description: Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books
id: structured-synthesis-beats-rephrasing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Full beats the Rephrase control on 25 of 28 benchmarks by +1.17 at comparable generation cost and identical training compute. [→ Jiawen Tao 2026](#jiawen-tao-2026)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

MoE mid-training study; Rephrase independently rewrites documents from the same retrieval pool under the same audience×style scheme without clustering, TOC planning, or book assembly, under the same 16B-token budget.

> "At comparable generation and identical training compute, Full beats Rephrase on 25/28 benchmarks ( +1.17), while Rephrase ties Natural Books (−0.08)."

## Discussion


## Related Claims
- [The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)](book-organization-transfers-llama3-8b.md) — related
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories](synthetic-textbooks-replace-natural-books-gain.md) — related
