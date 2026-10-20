---
type: claim
title: "Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets"
description: "Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets"
id: residual-correction-essential-heterogeneous-aggregation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yagna-manasa-boyapati-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02947"
    title: "Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)"
    author: Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In the ablation study, federation with DP but without residual correction produces MAE worse than the single-LLM baseline on all three datasets, with UCI showing the largest degradation (0.2997 vs. 0.1132). [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i?` · `causal · r2`

Ablation study (Table 4) with six conditions decomposing each component's contribution; the article concludes "naive averaging of heterogeneous LLM outputs without correction is harmful" because heterogeneous LLMs differ in calibration, granularity, and systematic biases.

> "removing RC while retaining LDP (ε=2.0) yields MAE worse than the single-LLM baseline across all datasets, with the UCI dataset showing the most dramatic degradation (w/o RC: 0.2997 vs. 0.1132 baseline)"

## Discussion


## Related Claims
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — related
- [Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded (0,1)K prediction outputs](laplace-ldp-superior-gaussian-bounded-outputs.md) — related
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — related
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) — related
- [Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89](statistical-significance-federated-diagnosis-gains.md) — related
