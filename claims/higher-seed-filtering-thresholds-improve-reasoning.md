---
type: claim
title: Higher seed-problem filtering thresholds yield better downstream reasoning performance, indicating problem quality directly impacts results
description: Higher seed-problem filtering thresholds yield better downstream reasoning performance, indicating problem quality directly impacts results
id: higher-seed-filtering-thresholds-improve-reasoning
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

# Higher seed-problem filtering thresholds yield better downstream reasoning performance, indicating problem quality directly impacts results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Using Mistral-7B, raising the Stage 1 filtering threshold from score 2 to 3 to 4 improves average benchmark accuracy (33.4, 34.9, 35.0). [→ Xianyang Liu 2025](#xianyang-liu-2025)

## Evidence

### Xianyang Liu 2025

Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361 [doi:10.48550/arxiv.2510.19361](https://doi.org/10.48550/arxiv.2510.19361)

`q2 · i?` · `design · r2`

Threshold sensitivity experiment with Mistral-7B at a fixed 30K dataset (Table 4): score thresholds of 2, 3, and 4 yield average scores of 33.4, 34.9, and 35.0 respectively, though the main experiments adopt threshold 3.

> "Table 4 shows that the use of higher thresholds for the filtering of seed problems leads to better results, confirming that the quality of the selected problems directly impacts the performance of reasoning."

## Discussion


## Related Claims
- [Each AgenticMath component contributes performance gains, with the review-revise loop playing a particularly important role](agenticmath-ablation-all-modules-contribute.md) — related
- [Raising the answer-confidence threshold reduces the number of retained MCQs but substantially improves their quality](answer-confidence-threshold-trades-quantity-for-quality.md) — related
- [Instances occurred where the Teacher LLM directly provided the final answer, bypassing the intended cognitive process, and can be programmatically filtered](collaborative-cheating-teacher-provides-answer.md) — related
