---
type: claim
title: DKT-based environments converge faster in training, but DKT struggles to estimate higher knowledge levels, unlike the more comprehensive AKT assessments
description: DKT-based environments converge faster in training, but DKT struggles to estimate higher knowledge levels, unlike the more comprehensive AKT assessments
id: dkt-faster-convergence-but-poor-high-level-estimates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: jyun-yi-chen-2023
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: jyun-yi-chen-2023-2
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: jyun-yi-chen-2023-3
    resource: "https://doi.org/10.48550/arXiv.2305.04475"
    title: "Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)"
    author: Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# DKT-based environments converge faster in training, but DKT struggles to estimate higher knowledge levels, unlike the more comprehensive AKT assessments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The output distributions of DKT and AKT over the same group of students differed significantly in standard deviation, with AKT assessing knowledge backgrounds more comprehensively. [→ Jyun-Yi Chen 2023](#jyun-yi-chen-2023)
`q1 i?` The KT-KDM system with DKT as its environment converged faster during training because its environment exhibits a lower complexity level. [→ Jyun-Yi Chen 2023 (2)](#jyun-yi-chen-2023-2)
`q1 i?` The authors interpret this as DKT struggling to estimate higher levels of knowledge regardless of how well students perform. [→ Jyun-Yi Chen 2023 (3)](#jyun-yi-chen-2023-3)

## Evidence

### Jyun-Yi Chen 2023

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

Statistical analysis of the initial knowledge levels of sampled students during training in ALPN-A2C and KT-KDM (Figure 4). The article reports "a signiﬁcant difference in the standard deviations of the out put distributions between the DKT and AKT", with AKT assessing knowledge backgrounds more comprehensively.

> "It means there is a signiﬁcant difference in the standard deviations of the out put distributions between the DKT and AKT."

### Jyun-Yi Chen 2023 (2)

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

The authors' interpretation of the training curves and distribution plots: KT-KDM's DKT environment "is able to converge faster during training" because it "exhibits a lower complexity level".

> "Therefore, the KT-KDM system with DKT as the environment is able to converge faster during training, as its environment exhibits a lower complexity level."

### Jyun-Yi Chen 2023 (3)

Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. [doi:10.48550/arXiv.2305.04475](https://doi.org/10.48550/arXiv.2305.04475)

`q1 · i?` · `design · r2`

The authors' interpretation of the same distribution analysis: "DKT struggles to estimate higher levels of knowledge, regardless of how well students perform in their learning activities", motivating the choice of AKT.

> "However, this also indicates that DKT struggles to estimate higher levels of knowledge, regardless of how well students perform in their learning activities."

## Discussion


## Related Claims
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [Context-aware question and response representations improve AKT's prediction over raw embeddings](akt-context-aware-representations-improve-prediction.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC](akt-monotonic-attention-beats-positional-encoding.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
