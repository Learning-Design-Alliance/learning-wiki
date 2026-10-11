---
type: claim
title: "Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit"
description: "Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit"
id: pipeline-components-complementary-ablation
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
  - id: jiawen-tao-2026-2
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jiawen-tao-2026-3
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jiawen-tao-2026-4
    resource: "https://arxiv.org/abs/2607.28109"
    title: "Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109"
    author: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (4 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Removing TOC planning, clustering, and source chunks (Baseline C) drops overall judged quality from 9.38 to 6.12 (−3.26), the largest observed component effect. [→ Jiawen Tao 2026](#jiawen-tao-2026)
`q2 i?` Source chunks primarily improve specificity (+0.23), examples (+0.35), and factual accuracy (+0.32). [→ Jiawen Tao 2026 (2)](#jiawen-tao-2026-2)
`q2 i?` Cluster-informed TOC planning improves audience/style fit (+0.59), structure (+0.44), pedagogy (+0.23), and overall quality (+0.14) over discipline-name-only planning. [→ Jiawen Tao 2026 (3)](#jiawen-tao-2026-3)
`q2 i?` The TOC quality gate acts as a safety net: books from failed TOCs score lower on overall (−0.25), structure (−0.20), and pedagogy (−0.19), a smaller degradation than removing source chunks or cluster summaries. [→ Jiawen Tao 2026 (4)](#jiawen-tao-2026-4)

## Evidence

### Jiawen Tao 2026

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Component ablation on 100 matched book instances scored by Gemini-3.1-Pro on a 1–10 rubric; Baseline C generates an entire book without TOC planning, clustering, or source chunks.

> "Baseline C scores 6.12 overall versus 9.38 for Full (−3.26). Despite a∼30–40K-word length target, it still yields only∼56K characters (roughly 4× shorter than Full), with lower depth (5.86) and specificity (6.41)."

### Jiawen Tao 2026 (2)

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Same judged ablation; Baseline A keeps Full's cluster-informed TOC but removes source chunks, isolating retrieval grounding's contribution to domain-specific detail.

> "Full versus Baseline A isolates retrieval grounding: source chunks improve specificity (+0.23), examples (+0.35), and factual accuracy (+0.32), with smaller differences elsewhere."

### Jiawen Tao 2026 (3)

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Same judged ablation comparing Baseline A (cluster-informed TOC) against Baseline B (TOC from discipline name alone), neither using source chunks.

> "A improves audience/style fit (9.21 vs. 8.62, +0.59), structure (9.35 vs. 8.91, +0.44), pedagogy (9.23 vs. 9.00, +0.23), and overall quality (9.21 vs. 9.07, +0.14), showing that source coverage supports more targeted TOCs before any section text is generated."

### Jiawen Tao 2026 (4)

Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan. (2026). Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training. arXiv preprint. https://arxiv.org/abs/2607.28109

`q2 · i?` · `causal · r2`

Baseline D generates books from 200 failed TOCs, evaluated with the same judge and rubric as the other ablation conditions.

> "Relative to Full, they score lower on overall (−0.25), structure (−0.20), and pedagogy (−0.19). This smaller degradation than removing source chunks or cluster summaries makes the gate a safety net rather than the primary quality driver."

## Discussion


## Related Claims
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
- [Structured book synthesis outperforms matched independent document rephrasing (+1.17 mean), while rephrasing alone ties natural books](structured-synthesis-beats-rephrasing.md) — related
- [Section quality improves with more source chunks up to k=10, beyond which gains plateau](source-chunk-count-k10-plateau.md) — related
- [Replacing natural books with synthetic textbooks improves the 28-benchmark mean by +1.09, with gains spanning all four categories](synthetic-textbooks-replace-natural-books-gain.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
