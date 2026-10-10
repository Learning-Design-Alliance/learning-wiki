---
type: claim
title: Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories
description: Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories
id: synthetic-textbooks-replace-natural-books-gain
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

# Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Full improves 19 of 28 benchmarks over Natural Books with a +1.09 overall mean, improving all four category means. [→ Jiawen Tao 2026](#jiawen-tao-2026)
`q2 i?` Bootstrap intervals remain positive for all three aggregate comparisons, and one-sided sign tests give p=0.044, 0.0019, and 0.000014 for Full against Natural Books, Split, and Rephrase. [→ Jiawen Tao 2026 (2)](#jiawen-tao-2026-2)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

MoE mid-training study comparing the synthetic-book corpus against the original book slice under the same 16B-token allocation. The article reports the printed category deltas and 19/28 benchmark wins.

> "Full improves all four category means over Natural Books—STEM ( +1.86), reasoning (+1.49), code ( +1.07), and knowledge ( +0.43)—and 19/28 benchmarks ( +1.09 overall)."

### Jiawen Tao 2026 (2)

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Robustness check on the same results: benchmark-level bootstrap intervals remain positive for all three aggregate comparisons; the article notes this does not estimate training-run variance.

> "One-sided sign tests give p=0.044, 0.0019, and 0.000014 for Full against Natural Books, Split, and Rephrase, respectively."

## Discussion


## Related Claims
- [The book-organization benefit transfers to Llama3-8B, where Full outperforms RandomConcat (+0.86) and Natural Books (+1.51)](book-organization-transfers-llama3-8b.md) — related
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
- [Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books](structured-synthesis-beats-rephrasing.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
