---
type: claim
title: "Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89"
description: "Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89"
id: statistical-significance-federated-diagnosis-gains
status: draft
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
    i: 3
    kind: design
    rigour: 2
---

# Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Paired t-tests show p<0.001 with Cohen's d=0.85 for ε=2.0 on ASSIST09, p<0.01 with d=0.62 on GSM8K, and p<0.001 with d=0.78 on UCI; the non-private ASSIST09 result shows d=0.89. [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i3` · `design · r2`

Statistical significance analysis (Appendix C) using paired t-tests; ASSIST09 non-private federation showed p<0.001 with Cohen's d=0.89, and similar significance was observed across GSM8K (p<0.01, d=0.62) and UCI (p<0.001, d=0.78).

> "For ε= 2.0 (MAE 0.2068 versus baseline 0.2410), significance re- mains strong atp<0.001 with Cohen’sd= 0.85 , meaning that a moderate level of differential pri- vacy ensures the preservation of statistical signif- icance"

## Discussion


## Related Claims
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — a broader claim this one bears on
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) — related
- [Improvements over baselines are statistically significant, with Cohen's d ranging from 1.2 to 1.8 for key metrics](statistical-significance-effect-sizes-key-metrics.md) — related
