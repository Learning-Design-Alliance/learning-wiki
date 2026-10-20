---
type: claim
title: "The EduQwen 32B models achieve up to 96.52% accuracy on the CDPK Benchmark, surpassing the previous leaderboard leader Gemini-3 Pro at 90.55%"
description: "The EduQwen 32B models achieve up to 96.52% accuracy on the CDPK Benchmark, surpassing the previous leaderboard leader Gemini-3 Pro at 90.55%"
id: eduqwen-32b-sota-cdpk-benchmark
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

# The EduQwen 32B models achieve up to 96.52% accuracy on the CDPK Benchmark, surpassing the previous leaderboard leader Gemini-3 Pro at 90.55%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` EduQwen 32B-RL1, EduQwen 32B-SFT, and EduQwen 32B-SFT-RL2 each surpass all open-source and proprietary models on the CDPK Benchmark leaderboard, including Gemini-3 Pro at 90.55%. [→ Singh 2026](#singh-2026)

## Evidence

### Singh 2026

Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385 [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)

`q2 · i?` · `design · r2`

Benchmark evaluation of the three optimized models on the CDPK Benchmark, a publicly available collection of 920 teacher multiple-choice exam questions, scored by accuracy against a ground truth answer key. The final model reached "96.52% accuracy" versus Gemini-3 Pro's 90.55%. No effect size is printed.

> "EduQwen 32B-RL1 reaches 94.13% accuracy, EduQwen 32B-SFT reaches 96.20% accuracy, and with the optional second RL round, EduQwen 32B-SFT-RL2 reaches 96.52% accuracy, with all three models surpassing all open-source and proprietary systems currently listed on The Pedagogy Benchmark Leaderboard, including the previous best-performing Gemini-3 Pro at 90.55%."

## Discussion


## Related Claims
- [A single difficulty-weighted SFT run on a vision-language base model reaches 61.64% overall accuracy on TutorBench, surpassing Gemini-3 Pro (58.52%)](difficulty-weighted-sft-transfers-tutorbench.md) — related
- [The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark](domain-specialized-32b-outperforms-larger-models.md) — related
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
