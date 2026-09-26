---
type: claim
title: "BKTransformer's generated parameters evolve intuitively with student response sequences, supporting interpretability of mastery and correctness predictions"
description: "BKTransformer's generated parameters evolve intuitively with student response sequences, supporting interpretability of mastery and correctness predictions"
id: bkt-parameter-evolution-interpretability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: weak
sources:
  - id: badrinath-2023
    resource: "https://github.com/abadrinath947/OptimNN"
    title: "Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN"
    author: Badrinath, A. and Pardos, Z.
    q: 2
    i: 1
---

# BKTransformer's generated parameters evolve intuitively with student response sequences, supporting interpretability of mastery and correctness predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` In sample test sequences from AST09, mastery and correctness probabilities fall with consecutive incorrect responses while slip rate rises, and tend toward zero after 25 consecutive incorrect responses. [→ Badrinath 2023](#badrinath-2023)

## Evidence

### Badrinath 2023

Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN

`q2 · i1`

Qualitative analysis of parameter evolution (Section 6.4, Figure 5) on two test student sequences from AST09. In one sequence, after three incorrect responses the predicted correctness and mastery "drop by over 20%", with slip probability increasing by roughly 10%.

> "both the masteryP (Lt) and correctness probabilityP (obst) reduce with each incorrect response and tend towards zero, indicating no eventual likelihood of mastery or correctness."

## Discussion


## Related Claims
-
