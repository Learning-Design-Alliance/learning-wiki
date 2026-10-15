---
type: claim
title: "Injecting the collaborative prior redistributes AKT's attention from local recency bias toward long-range dependencies"
description: "Injecting the collaborative prior redistributes AKT's attention from local recency bias toward long-range dependencies"
id: mbp-kt-attention-recency-to-long-range
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: yuhao-jia-2026
    resource: "https://doi.org/10.48550/arxiv.2605.08697"
    title: "Yuhao Jia, Duantengchuan Li, Jinsong Chen, Zhongjie Mao, Mingwen Tong, Yue Li, Xiaoguang Wang. (2026). MBP-KT: Learning Global Collaborative Information from Meta-Behavioral Pattern for Enhanced Knowledge Tracing. Preprint. https://arxiv.org/abs/2605.08697 [doi:10.48550/arxiv.2605.08697](https://doi.org/10.48550/arxiv.2605.08697)"
    author: Yuhao Jia, Duantengchuan Li, Jinsong Chen, Zhongjie Mao, Mingwen Tong, Yue Li, Xiaoguang Wang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Injecting the collaborative prior redistributes AKT's attention from local recency bias toward long-range dependencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Qualitative attention visualization shows the baseline AKT concentrates attention along the diagonal (immediate past steps), while the enhanced variant exhibits a structural redistribution activating long-range dependencies. [→ Yuhao Jia 2026](#yuhao-jia-2026)

## Evidence

### Yuhao Jia 2026

Yuhao Jia, Duantengchuan Li, Jinsong Chen, Zhongjie Mao, Mingwen Tong, Yue Li, Xiaoguang Wang. (2026). MBP-KT: Learning Global Collaborative Information from Meta-Behavioral Pattern for Enhanced Knowledge Tracing. Preprint. https://arxiv.org/abs/2605.08697 [doi:10.48550/arxiv.2605.08697](https://doi.org/10.48550/arxiv.2605.08697)

`q1 · i?` · `design · r2`

Qualitative analysis (Appendix B.5, Figure 10) extracting last-layer attention weight matrices from baseline AKT and AKT+MBP-KT on a sampled sequence. The difference map highlights "the suppression of local recency bias (blue, negative) and the activation of long-range dependencies (red/orange, positive)."

> "The baseline model predominantly exhibits a localized recency bias. It concentrates its attention weights densely along the diagonal (immediate past steps) while failing to retrieve relevant long-range historical context"

## Discussion


## Related Claims
- [There is no universal optimal injection position for the collaborative prior; effectiveness is an architecture-sensitive design choice](injection-strategy-architecture-sensitive.md) — related
- Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation — related
- [Injecting MBP-KT's global collaborative information consistently improves KT models across RNN, memory-network, Transformer and state-based backbones](mbp-kt-consistently-improves-kt-backbones.md) — related
- [MBP-KT yields significantly greater improvements for learners with fewer interaction records than for learners with more records](mbp-kt-greater-gains-sparse-learners.md) — related
