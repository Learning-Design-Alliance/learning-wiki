---
type: claim
title: Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)
description: Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)
id: book-structure-preservation-improves-mid-training
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
  - id: jiawen-tao-2026-2
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` On a 3B-active MoE model, keeping TOC-planned textbooks as complete documents outperforms treating each section as an independent document on 22 of 28 benchmarks, with a +1.02 overall mean gain. [→ Jiawen Tao 2026](#jiawen-tao-2026)
`q2 i?` A length-matched RandomConcat control that joins sections from different books ties Split but trails Full by 1.01, indicating the benefit comes from planned adjacency rather than document length alone. [→ Jiawen Tao 2026 (2)](#jiawen-tao-2026-2)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Matched mid-training comparison on a 3B-active MoE (30B total) with a fixed 200B-token mix; only the 16B-token book slice differs. The article reports "Full exceeds content-identical Split on 22/28 benchmarks (+1.02)" with category means as printed.

> "Full exceeds content-identical Split on 22/28 benchmarks (+1.02), leading every category mean (code +2.23, reasoning +1.35, knowledge +0.61, STEM +0.56)."

### Jiawen Tao 2026 (2)

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Same MoE study; RandomConcat regroups Split sections across books to match Full's length distribution. The article reports RandomConcat "ties Split (54.89 vs. 54.88)" while trailing Full by 1.01.

> "Length-matched RandomConcat ties Split (54.89 vs. 54.88) but trails Full by 1.01 (21/28 wins; Appendix E), supporting planned adjacency beyond length matching and fewer resets."

## Discussion


## Related Claims
- [Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books](structured-synthesis-beats-rephrasing.md) — related
- [Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories](synthetic-textbooks-replace-natural-books-gain.md) — related
- [Section quality improves with more source chunks up to k=10, beyond which gains plateau](source-chunk-count-k10-plateau.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)](book-organization-transfers-llama3-8b.md) — related
