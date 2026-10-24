---
type: claim
title: Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost
description: Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost
id: multi-llm-federated-cognitive-diagnosis-improvement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yagna-manasa-boyapati-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02947"
    title: "Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)"
    author: Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across ASSIST09, GSM8K, and UCI datasets, the heterogeneous federation achieves an average 11.99% MAE improvement over single-LLM baselines at ε=2.0 with 0.46% average privacy cost. [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i?` · `design · r2`

Evaluation across three educational benchmarks (ASSIST09, GSM8K, UCI Student Performance) comparing the federated framework to single-LLM baselines, reporting "11.99% average im- provement with 0.46% privacy cost at ε= 2.0". Per-dataset gains were 14.19% (ASSIST09), 7.39% (GSM8K), and 14.40% (UCI).

> "Overall, 11.99% average im- provement with 0.46% privacy cost at ε= 2.0 demonstrates broad generalization across mathe- matics, reasoning, and holistic assessment domains."

## Discussion


## Related Claims
- [Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded (0,1)K prediction outputs](laplace-ldp-superior-gaussian-bounded-outputs.md) — related
- [Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89](statistical-significance-federated-diagnosis-gains.md) — a narrower finding that bears on this claim
- [Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets](residual-correction-essential-heterogeneous-aggregation.md) — related
- [The framework generalizes under automatically generated Q-matrices without requiring expert annotation](automatic-qmatrix-extraction-generalization.md) — related
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) — related
- [The framework scales gracefully: MAE degrades by less than 2% from 10K to 100K EdNet interactions with near-linear processing time](ednet-scalability-federated-diagnosis.md) — related
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — possibly the same claim (merge candidate)
