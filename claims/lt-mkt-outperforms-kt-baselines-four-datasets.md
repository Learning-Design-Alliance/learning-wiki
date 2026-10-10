---
type: claim
title: LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines
description: LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines
id: lt-mkt-outperforms-kt-baselines-four-datasets
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: haotian-zhang-2026
    resource: "https://arxiv.org/abs/2608.24005"
    title: "Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005"
    author: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`

## Subclaims
`q3 i?` LT-MKT consistently achieves the best AUC, ACC and RMSE on JuniorH, SeniorH, PTADiscJP and PTADiscDS, with improvements significant at p < 0.05. [→ Haotian Zhang 2026](#haotian-zhang-2026)

## Evidence

### Haotian Zhang 2026

Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005

`q3 · i?` · `design · r2`

Comparison of LT-MKT against eleven baselines (DKT, GKT, AKT, SINKT, promptKT, TransKT, etc.) on four datasets, with "LT-MKT consistently achieves the best performance across all datasets and evaluation metrics"; Table 2 marks all LT-MKT results with * indicating p-value < 0.05 in the t-test.

> "First, LT-MKT consistently achieves the best performance across all datasets and evaluation metrics, demonstrating the effectiveness of explicitly modeling cognitive load and knowledge transfer in multi-domain knowledge tracing."

## Discussion


## Related Claims
- [A qualitative case study shows LT-MKT jointly captures beneficial knowledge transfer and load-induced learning friction](case-study-transfer-and-load-friction.md) — related
- [Modeling knowledge transfer within and across domains alleviates the cold-start problem on unseen concepts](knowledge-transfer-alleviates-cold-start-kt.md) — a narrower finding that bears on this claim
- [Performance is best at moderate difficulty granularity and a limited recent window for domain transitions](moderate-difficulty-granularity-window-optimal.md) — related
