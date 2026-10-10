---
type: claim
title: Performance is best at moderate difficulty granularity and a limited recent window for domain transitions
description: Performance is best at moderate difficulty granularity and a limited recent window for domain transitions
id: moderate-difficulty-granularity-window-optimal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: haotian-zhang-2026
    resource: "https://arxiv.org/abs/2608.24005"
    title: "Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005"
    author: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Performance is best at moderate difficulty granularity and a limited recent window for domain transitions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` LT-MKT achieves best overall performance at moderate λP and around ws = 20; too small or too large values of either degrade performance. [→ Haotian Zhang 2026](#haotian-zhang-2026)

## Evidence

### Haotian Zhang 2026

Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005

`q2 · i?` · `design · r2`

Parameter sensitivity analysis varying λP in {10, 30, 50, 70} with ws = 20, and ws in {5, 10, 20, 40} with λP = 30 (Figure 6); the article reports best performance "when 𝜆𝑃 is set to a moderate value" and generally around ws = 20.

> "As shown in Figure 6, LT-MKT achieves the best overall performance when 𝜆𝑃 is set to a moderate value. When 𝜆𝑃 is too small, questions with different empirical difficulty levels are compressed into coarse categories"

## Discussion


## Related Claims
- [A qualitative case study shows LT-MKT jointly captures beneficial knowledge transfer and load-induced learning friction](case-study-transfer-and-load-friction.md) — related
- [LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines](lt-mkt-outperforms-kt-baselines-four-datasets.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
