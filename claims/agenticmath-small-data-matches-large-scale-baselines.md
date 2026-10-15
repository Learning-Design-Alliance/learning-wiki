---
type: claim
title: Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks
description: Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks
id: agenticmath-small-data-matches-large-scale-baselines
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
    kind: causal
    rigour: 2
---

# Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` AgenticMath-Llama3-8B fine-tuned on 90K samples achieves an average score of 40.3, surpassing Llama3-8B-DART-Math trained on 590K samples (39.7) and other large-scale Llama3 baselines. [→ Xianyang Liu 2025](#xianyang-liu-2025)

## Evidence

### Xianyang Liu 2025

Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)

`q2 · i?` · `causal · r2`

Benchmark evaluation (Table 2) comparing AgenticMath fine-tuned Llama3-8B at 30K/60K/90K samples against large-scale baselines (400K-2.3M) across six math benchmarks; the text reports "AgenticMath-Llama3-8B (90K) achieves 40.3" versus DART-Math's 39.7 at 590K.

> "AgenticMath-Llama3-8B (90K) achieves 40.3, surpassing Llama3-8B-DART-Math (590K, 39.7) and all other large-scale Llama3 baselines."

## Discussion


## Related Claims
- [Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks](agenticmath-data-size-positive-correlation-accuracy.md) — related
- [At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks](agenticmath-sota-at-small-data-scales.md) — related
