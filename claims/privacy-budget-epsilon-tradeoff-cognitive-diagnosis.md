---
type: claim
title: ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09
description: ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09
id: privacy-budget-epsilon-tradeoff-cognitive-diagnosis
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
    kind: design
    rigour: 2
---

# ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On ASSIST09, ε=2.0 retains a 14.19% improvement with 0.19% privacy cost, ε=1.0 retains 7.38%, and ε=0.5 yields −3.69% (worse than baseline). [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i?` · `design · r2`

Privacy–utility tradeoff analysis on ASSIST09 under local differential privacy (Table 3), where "ε= 2.0 setting provides the best balance"; stricter budgets degrade performance, with ε=0.5 introducing excessive noise (−3.69%).

> "The ε= 2.0 setting provides the best balance: 14.19% improvement with only marginal degradation relative to the non-private model (0.19% privacy cost on ASSIST09)."

## Discussion


## Related Claims
- [Laplace-based local differential privacy outperforms Gaussian noise under Rényi-DP accounting for bounded (0,1)K prediction outputs](laplace-ldp-superior-gaussian-bounded-outputs.md) — related
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — related
- [Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets](residual-correction-essential-heterogeneous-aggregation.md) — related
- [Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89](statistical-significance-federated-diagnosis-gains.md) — related
