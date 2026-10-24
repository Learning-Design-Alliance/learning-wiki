---
type: claim
title: KT4EQG achieves the highest exam score across all knowledge modules on both XES3G5M and MOOCRADAR, outperforming all question-generation baselines
description: KT4EQG achieves the highest exam score across all knowledge modules on both XES3G5M and MOOCRADAR, outperforming all question-generation baselines
id: kt4eqg-highest-exam-score-all-modules
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: xinyi-gao-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23933"
    title: "Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933 [doi:10.48550/arxiv.2605.23933](https://doi.org/10.48550/arxiv.2605.23933)"
    author: Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# KT4EQG achieves the highest exam score across all knowledge modules on both XES3G5M and MOOCRADAR, outperforming all question-generation baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In simulated multi-round practice evaluations on XES3G5M and MOOCRADAR, KT4EQG attains the highest exam score in every knowledge module, exceeding all question-generation baselines. [→ Xinyi Gao 2026](#xinyi-gao-2026)

## Evidence

### Xinyi Gao 2026

Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933 [doi:10.48550/arxiv.2605.23933](https://doi.org/10.48550/arxiv.2605.23933)

`q2 · i?` · `design · r2`

Simulation-based evaluation using KT2 to simulate multi-round practice and score a fixed exam set; Table 1 reports exam scores per module, where "KT4EQG achieves the highest exam score across all modules". INITIAL, RANDOM, and ORACLE baselines were excluded from the ranking.

> "Table 1 shows the performance of all methods across all knowledge modules in XES3G5M and MOOCRADAR. KT4EQG achieves the highest exam score across all modules, consistently outperforming all question-generation baselines."

## Discussion


## Related Claims
- [Providing baselines with oracle knowledge-concept selection substantially improves their performance, identifying concept selection as a key bottleneck, though baselines with oracle KCs still trail KT4EQG](concept-selection-bottleneck-baselines.md) — related
- [KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase](consistent-gains-across-practice-rounds.md) — related
- [KT4EQG remains competitive when evaluated with alternative knowledge tracers (BKT and DKT), though its advantage varies across modules](kt4eqg-competitive-under-alternative-tracers.md) — related
- [KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones](adaptive-kc-selection-policy.md) — related
