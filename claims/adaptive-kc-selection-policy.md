---
type: claim
title: "KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones"
description: "KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones"
id: adaptive-kc-selection-policy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Analysis of selected KCs on the Application Module shows selection favors higher-mastery KCs for weaker students and shifts toward more challenging KCs as student mastery increases. [→ Xinyi Gao 2026](#xinyi-gao-2026)

## Evidence

### Xinyi Gao 2026

Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933 [doi:10.48550/arxiv.2605.23933](https://doi.org/10.48550/arxiv.2605.23933)

`q2 · i?` · `design · r2`

Analysis of the KC selected for each truncated history on the Application Module, with students ranked by initial mastery and candidate KCs ranked by mastery probability (66 candidate KCs); the smoothed trend in Figure 3 shows "a clear adaptive pattern".

> "For weaker students, the selection tends to favor KCs with higher mastery levels and avoid concepts that are too difficult. For students with higher mastery, the selection progressively shifts toward more challenging KCs."

## Discussion


## Related Claims
- [Providing baselines with oracle knowledge-concept selection substantially improves their performance, identifying concept selection as a key bottleneck, though baselines with oracle KCs still trail KT4EQG](concept-selection-bottleneck-baselines.md) — related
- [KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase](consistent-gains-across-practice-rounds.md) — related
- CLST's predicted mastery levels track response correctness and move similarly for related knowledge components — related
