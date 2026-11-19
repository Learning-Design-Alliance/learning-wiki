---
type: claim
title: "Both adaptive aggregation and the rank-based constraint are necessary for GRATE's performance"
description: "Both adaptive aggregation and the rank-based constraint are necessary for GRATE's performance"
id: grate-ablation-both-components-necessary
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: chunpai-wang-2021
    title: Chunpai Wang 2021
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Both adaptive aggregation and the rank-based constraint are necessary for GRATE's performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Removing either the aggregation component (GRATE-W/O-Agg) or the rank-based component (GRATE-W/O-Rank) degrades performance prediction relative to the full model in all datasets. [→ Chunpai Wang 2021](#chunpai-wang-2021)

## Evidence

### Chunpai Wang 2021

Chunpai Wang, Shaghayegh Sahebi, Siqian Zhao, Peter Brusilovsky, and Laura O. Moraes. 2021. Knowledge Tracing for Complex Problem Solving: Granular Rank-Based Tensor Factorization. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization (UMAP '21). https://doi.org/10.1145/3450613.3456831

`q2 · i?` · `design · r2`

Ablation study comparing the full GRATE model against GRATE-W/O-Agg and GRATE-W/O-Rank on the performance prediction task over five folds with 95% confidence intervals; full GRATE achieved RMSE 0.2033 (MORF), 0.3726 (CSIntro), and AUC 0.7035 (MasteryGrids).

> "As indicated, the full model performed better than both GRATE-W/O-Agg and GRATE-W/O-Rank in all datasets. This shows that neither of these two components was dispensable for student knowledge modeling"

## Discussion


## Related Claims
- [Attempt aggregation and the rank-based constraint each reduce fluctuations in discovered student knowledge states](grate-aggregation-smooths-knowledge-fluctuations.md) — related
- [GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets](grate-outperforms-kt-baselines-performance-prediction.md) — related
