---
type: claim
title: "Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded [0,1]K prediction outputs"
description: "Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded [0,1]K prediction outputs"
id: laplace-ldp-superior-gaussian-bounded-outputs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yagna-manasa-boyapati-2026
    resource: "https://arxiv.org/abs/2609.02947"
    title: "Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947"
    author: Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded [0,1]K prediction outputs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the ablation, Gaussian-DP yields MAE worse than both the single-LLM baseline and the full system on all three datasets. [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947

`q2 · i?` · `design · r2`

Ablation comparison (Table 4) of noise mechanisms under ε=2.0; Gaussian-DP MAE was 0.3147 (ASSIST09), 0.2943 (GSM8K), 0.3165 (UCI), worse than both the full system and the single-LLM baseline.

> "Gaussian noise under Rényi-DP accounting (Mironov, 2017) yields MAE worse than both the baseline and full system, confirming that Laplace-based LDP is superior for our bounded [0,1]K prediction setting."

## Discussion


## Related Claims
- [Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets](residual-correction-essential-heterogeneous-aggregation.md) — related
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) — related
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — related
