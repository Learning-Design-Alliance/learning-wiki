---
type: claim
title: The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)
description: The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)
id: book-organization-transfers-llama3-8b
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

# The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On Llama3-8B mid-training, Full scores 40.96 versus 40.10 for RandomConcat and 39.45 for Natural Books, winning 20 of 28 benchmarks with a 95% CI of [+0.44,+1.30] over RandomConcat. [→ Jiawen Tao 2026](#jiawen-tao-2026)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Transfer check: three Llama3-8B mid-training runs on a 100B-token mixture with an 8B-token book slice, holding data order, steps, optimizer, and schedule fixed. The article reports the printed means, CI, and p-value.

> "On Llama3-8B, Full scores 40.96, versus 40.10 for RandomConcat and 39.45 for Natural Books ( +0.86; 20/28 wins; 95% CI [+0.44,+1.30]; p=0.018; Table 4)."

## Discussion


## Related Claims
- [Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories](synthetic-textbooks-replace-natural-books-gain.md) — related
- [Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books](structured-synthesis-beats-rephrasing.md) — related
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
