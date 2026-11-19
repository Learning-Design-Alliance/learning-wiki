---
type: claim
title: Attempt aggregation and the rank-based constraint each reduce fluctuations in discovered student knowledge states
description: Attempt aggregation and the rank-based constraint each reduce fluctuations in discovered student knowledge states
id: grate-aggregation-smooths-knowledge-fluctuations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
sources:
  - id: chunpai-wang-2021
    title: Chunpai Wang 2021
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chunpai-wang-2021-2
    title: Chunpai Wang 2021 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Attempt aggregation and the rank-based constraint each reduce fluctuations in discovered student knowledge states

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Removing the rank-based constraint yields higher fluctuations in student knowledge values, and removing aggregation also produces more fluctuations than the full model. [→ Chunpai Wang 2021](#chunpai-wang-2021)
`q2 i?` Highly fluctuating attempts in the no-aggregation model are aggregated together in the full model to create a smoother knowledge increase. [→ Chunpai Wang 2021 (2)](#chunpai-wang-2021-2)

## Evidence

### Chunpai Wang 2021

Chunpai Wang, Shaghayegh Sahebi, Siqian Zhao, Peter Brusilovsky, and Laura O. Moraes. 2021. Knowledge Tracing for Complex Problem Solving: Granular Rank-Based Tensor Factorization. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization (UMAP '21). https://doi.org/10.1145/3450613.3456831

`q2 · i?` · `design · r2`

Visualization of average student knowledge over attempts on the CSIntro dataset (Figure 3, GRATE-W/O-Rank) contrasted with the full model (Figure 2); the article reports higher fluctuations without the rank-based constraint, e.g. Concept 2 at Attempt 29 much higher than Attempts 28 and 30.

> "We can see that removing the rank-based constraint results in higher fluctuations in student knowledge values."

### Chunpai Wang 2021 (2)

Chunpai Wang, Shaghayegh Sahebi, Siqian Zhao, Peter Brusilovsky, and Laura O. Moraes. 2021. Knowledge Tracing for Complex Problem Solving: Granular Rank-Based Tensor Factorization. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization (UMAP '21). https://doi.org/10.1145/3450613.3456831

`q2 · i?` · `design · r2`

Comparison of the GRATE-W/O-Agg knowledge visualization (Figure 4) with the full model (Figure 2) on CSIntro; without aggregation, Concept 2 knowledge drops from k = 0.30 at Attempt 17 to k = 0.15 at 18 then rises to k = 0.20 at 19, while the full model aggregates these attempts.

> "However, in the full GRATE results in Figure 2, these fluctuations are considered to be insignificant, and Attempts 17, 18, and 19 are aggregated together."

## Discussion


## Related Claims
- [Both adaptive aggregation and the rank-based constraint are necessary for GRATE's performance](grate-ablation-both-components-necessary.md) — related
- [Latent concepts discovered by GRATE are meaningful and go beyond the labeled topics in the data](grate-latent-concepts-beyond-topics.md) — related
