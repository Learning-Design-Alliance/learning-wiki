---
type: claim
title: "LearnLens's modular pipeline outperforms direct-prompt baselines on scoring quality while matching latency and cost on 100 authentic student answers"
description: "LearnLens's modular pipeline outperforms direct-prompt baselines on scoring quality while matching latency and cost on 100 authentic student answers"
id: learnlens-modular-pipeline-beats-baselines-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: runcong-zhao-2025
    resource: "https://doi.org/10.48550/arxiv.2507.04295"
    title: "Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He. (2025). LearnLens: LLM-Enabled Personalised, Curriculum-Grounded Feedback with Educators in the Loop. https://arxiv.org/abs/2507.04295 [doi:10.48550/arxiv.2507.04295](https://doi.org/10.48550/arxiv.2507.04295)"
    author: Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LearnLens's modular pipeline outperforms direct-prompt baselines on scoring quality while matching latency and cost on 100 authentic student answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On 100 authentic student answers to a five-mark short-essay science question, LearnLens achieves MSE 3.19 (8–13% below any baseline), correlation 0.388, and exact and ±1 accuracies surpassing the best baseline QwQ-32B, with average latency 11.4 s and per-request cost $0.0099. [→ Runcong Zhao 2025](#runcong-zhao-2025)

## Evidence

### Runcong Zhao 2025

Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He. (2025). LearnLens: LLM-Enabled Personalised, Curriculum-Grounded Feedback with Educators in the Loop. https://arxiv.org/abs/2507.04295 [doi:10.48550/arxiv.2507.04295](https://doi.org/10.48550/arxiv.2507.04295)

`q2 · i?` · `design · r2`

Comparative evaluation on 100 authentic student answers to a five-mark short-essay science question, with baselines (LLaMA-3-8B-Instruct, Qwen2.5-32B-Instruct, QwQ-32B) using direct prompts without modular decomposition. The article reports MSE drops to 3.19 and correlation rises to 0.388 for LearnLens.

> "MSE drops to 3.19 (8–13 % below any baseline), correlation rises to 0.388, and both exact and ±1 accuracies surpass the best baseline (QwQ-32B). At the same time, average generation latency is 11.4 s, comparable to Qwen2.5-32B and four times faster than QwQ-32B, while the per-request cost ($0.0099) matches Qwen2.5-32B and is 72 % cheaper than QwQ-32B."

## Discussion


## Related Claims
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic](collearn-latency-cost-efficiency.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
