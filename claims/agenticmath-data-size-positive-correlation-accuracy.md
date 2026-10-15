---
type: claim
title: Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks
description: Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks
id: agenticmath-data-size-positive-correlation-accuracy
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

# Increasing AgenticMath-generated training data from 7.5K to 22.5K samples yields consistent accuracy gains for Llama3-8B across benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Llama3-8B shows consistent accuracy gains on MATH, DeepMind-Mathematics, CollegeMath, TheoremQA, and OlympiadBench-Math as the training dataset grows in 2.5K increments. [→ Xianyang Liu 2025](#xianyang-liu-2025)

## Evidence

### Xianyang Liu 2025

Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)

`q2 · i?` · `design · r2`

Scaling analysis (Figure 2) starting from 7.5K MATH samples and adding synthetic data in increments of 2.5K up to 22.5K total, plotting Llama3-8B accuracy across five benchmarks as training size increases.

> "Llama3-8B shows consistent accuracy gains on different benchmarks as the dataset grows, confirming a strong positive correlation between training size and reasoning ability."

## Discussion


## Related Claims
- [Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks](agenticmath-small-data-matches-large-scale-baselines.md) — related
- [At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks](agenticmath-sota-at-small-data-scales.md) — related
