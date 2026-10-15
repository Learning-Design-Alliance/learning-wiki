---
type: claim
title: "The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark"
description: "The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark"
id: domain-specialized-32b-outperforms-larger-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: singh-2026
    resource: "https://doi.org/10.48550/arxiv.2604.06385"
    title: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385 [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)"
    author: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The optimized dense 32-billion-parameter model outperforms the larger Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark. [→ Singh 2026](#singh-2026)

## Evidence

### Singh 2026

Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385 [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)

`q2 · i?` · `design · r2`

Results-section comparison of the EduQwen models against larger leaderboard models on the CDPK Benchmark, with printed accuracies for both named larger models. The comparison names two distinct sides: the 32B optimized model versus the larger models.

> "our optimization strategy applied to the dense 32-billion parameter model surpasses the performance of significantly larger models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%), demonstrating that domain-specialized optimization transforms smaller open-source models into true domain experts that are more cost-efficient than running very large models with broad general knowledge."

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [The EduQwen 32B models achieve up to 96.52% accuracy on the CDPK Benchmark, surpassing the previous leaderboard leader Gemini-3 Pro at 90.55%](eduqwen-32b-sota-cdpk-benchmark.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
