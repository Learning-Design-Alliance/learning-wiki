---
type: claim
title: At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks
description: At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks
id: agenticmath-sota-at-small-data-scales
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: xianyang-liu-2025
    resource: "https://doi.org/10.48550/arxiv.2510.19361"
    title: "Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)"
    author: Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` With 30K samples, AgenticMath-Qwen2.5-3B reaches 53.7 average accuracy, surpassing MathFusion by over 15 points. [→ Xianyang Liu 2025](#xianyang-liu-2025)

## Evidence

### Xianyang Liu 2025

Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)

`q2 · i?` · `design · r2`

Evaluation across in-domain (MATH, GSM8K) and out-of-domain benchmarks (Table 1) at 30K and 60K scales on Qwen2.5-3B, DeepSeekMath-7B, Mistral-7B, and Llama3-8B; the text reports "AgenticMath-Qwen2.5-3B reaches 53.7 average accuracy" at 30K.

> "with 30K samples, AgenticMath-Qwen2.5-3B reaches 53.7 average accuracy, surpassing MathFusion by over 15 points."

## Discussion


## Related Claims
- [Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks](agenticmath-data-size-positive-correlation-accuracy.md) — related
- [Under the same teacher model, AgenticMath outperforms prior data-generation methods, indicating gains arise from framework design rather than teacher strength](agenticmath-gains-not-from-stronger-teacher.md) — related
- [Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks](agenticmath-small-data-matches-large-scale-baselines.md) — related
