---
type: claim
title: KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase
description: KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase
id: consistent-gains-across-practice-rounds
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: xinyi-gao-2026
    resource: "https://arxiv.org/abs/2605.23933"
    title: "Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933"
    author: Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across k = 10, 20, and 30 practice rounds, all methods improve with more rounds, but QWEN3-8B without oracle KC selection shows only marginal gains while KT4EQG achieves the highest exam score at every round. [→ Xinyi Gao 2026](#xinyi-gao-2026)

## Evidence

### Xinyi Gao 2026

Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933

`q2 · i?` · `design · r2`

Simulation varying the number of practice rounds (k = 10, 20, 30) on a representative module from each dataset, reported in Figure 2; the text states "KT4EQG achieves the highest exam score across all practice rounds".

> "Without oracle KC selection, QWEN3-8B shows only marginal gains as practice rounds increase, suggesting that poorly selected KCs provide limited cumulative learning benefit even with more practice. In contrast, methods with oracle KC exhibit substantially greater improvement. KT4EQG achieves the highest exam score across all practice rounds"

## Discussion


## Related Claims
- [KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones](adaptive-kc-selection-policy.md) — related
- [Providing baselines with oracle knowledge-concept selection substantially improves their performance, identifying concept selection as a key bottleneck, though baselines with oracle KCs still trail KT4EQG](concept-selection-bottleneck-baselines.md) — related
- [KT4EQG achieves the highest exam score across all knowledge modules on both XES3G5M and MOOCRADAR, outperforming all question-generation baselines](kt4eqg-highest-exam-score-all-modules.md) — related
- [Without alignment training, generated questions collapse to similar content regardless of the intended knowledge concept, whereas KT4EQG questions spread across many verified KCs](alignment-training-prevents-question-collapse.md) — related
- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](alignment-rl-improves-concept-alignment.md) — related
- [KT4EQG remains competitive when evaluated with alternative knowledge tracers (BKT and DKT), though its advantage varies across modules](kt4eqg-competitive-under-alternative-tracers.md) — related
