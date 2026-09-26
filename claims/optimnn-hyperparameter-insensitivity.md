---
type: claim
title: OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT
description: OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT
id: optimnn-hyperparameter-insensitivity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: badrinath-2023
    resource: "https://github.com/abadrinath947/OptimNN"
    title: "Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN"
    author: Badrinath, A. and Pardos, Z.
    q: 2
    i: 1
---

# OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` In ablations on AST09, OptimNN reaches an optimal model after one epoch regardless of learning rate, while SGD fails within 12 epochs for 3 of 4 learning rates; varying layers and hidden size has effectively no effect on OptimNN performance. [→ Badrinath 2023](#badrinath-2023)

## Evidence

### Badrinath 2023

Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN

`q2 · i1`

Ablation studies (Section 6.5, Table 5, Figure 6) on AST09 varying layers, hidden size, and learning rate (1e-4 to 1e-2). The paper reports "effectively no difference on the performance in any metric" across layers and embedding dimensions for OptimNN.

> "OptimNN yields an optimal model after simply 1 epoch of training regardless of the learning rate and SGD fails to do so within 12 epochs for 3 of 4 learning rates."

## Discussion


## Related Claims
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related
- [OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets](optimnn-lower-rmse-than-em-cgd-sgd.md) — related
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
