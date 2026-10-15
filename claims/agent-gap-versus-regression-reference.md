---
type: claim
title: "The agent's predictions show a performance gap versus a regression reference that uses real students' post-test data"
description: "The agent's predictions show a performance gap versus a regression reference that uses real students' post-test data"
id: agent-gap-versus-regression-reference
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jianxiao-jiang-2025
    resource: "https://doi.org/10.48550/arxiv.2510.09183"
    title: "Jianxiao Jiang, Yu Zhang. (2025). Student Development Agent: Risk-free Simulation for Evaluating AIED Innovations. Preprint. https://arxiv.org/abs/2510.09183 [doi:10.48550/arxiv.2510.09183](https://doi.org/10.48550/arxiv.2510.09183)"
    author: Jianxiao Jiang, Yu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The agent's predictions show a performance gap versus a regression reference that uses real students' post-test data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When compared to the regression reference fitted on real post-test outcomes, the agent methods exhibited larger errors, e.g., motivation RMSE 9.31 versus regression's 5.93. [→ Jianxiao Jiang 2025](#jianxiao-jiang-2025)

## Evidence

### Jianxiao Jiang 2025

Jianxiao Jiang, Yu Zhang. (2025). Student Development Agent: Risk-free Simulation for Evaluating AIED Innovations. Preprint. https://arxiv.org/abs/2510.09183 [doi:10.48550/arxiv.2510.09183](https://doi.org/10.48550/arxiv.2510.09183)

`q2 · i?` · `design · r2`

A multivariate linear regression fitted with real students' post-test scores serves as a high-level reference requiring administration of the innovation to real students. The article attributes the gap to regression incorporating post-test scores, which naturally strengthens its prediction indicators; no effect sizes are printed.

> "However, when compared to the reference method Regression, our methods exhibited a performance gap."

## Discussion


## Related Claims
- [In the MAIC case study, student development agent predictions (Concept and Scales methods) outperformed the mean baseline across all five non-cognitive dimensions on RMSE and MAE](agent-beats-mean-baseline-rmse-mae.md) — related
- [Predicted post-test distributions differed significantly from real distributions in four dimensions, with no significant difference only for Technology Acceptance](agent-distribution-significance-only-tech-acceptance.md) — related
