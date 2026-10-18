---
type: claim
title: On the ASSISTments 2020 dataset, StanBKT inference methods achieve nearly identical predictive performance while differing mainly in fit time
description: On the ASSISTments 2020 dataset, StanBKT inference methods achieve nearly identical predictive performance while differing mainly in fit time
id: stanbkt-methods-comparable-predictive-performance-assistments-2020
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: siddhartha-pradhan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23048"
    title: "Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales. (2026). StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing. https://arxiv.org/abs/2605.23048 [doi:10.48550/arxiv.2605.23048](https://doi.org/10.48550/arxiv.2605.23048)"
    author: Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the ASSISTments 2020 dataset, StanBKT inference methods achieve nearly identical predictive performance while differing mainly in fit time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` MCMC, variational inference, Pathfinder, and MAP in StanBKT, and EM in pyBKT, produced nearly identical accuracy, AUC, and RMSE on the ASSISTments 2020 test set, with fit times ranging from 3.35 s (pyBKT) to 822 s (MCMC). [→ Siddhartha Pradhan 2026](#siddhartha-pradhan-2026)

## Evidence

### Siddhartha Pradhan 2026

Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales. (2026). StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing. https://arxiv.org/abs/2605.23048 [doi:10.48550/arxiv.2605.23048](https://doi.org/10.48550/arxiv.2605.23048)

`q2 · i?` · `design · r2`

Scalability evaluation on the ASSISTments 2020 dataset (794,158 training and 189,082 test interactions, split at the student level), comparing StanBKT MCMC, Pathfinder, variational, and MAP against pyBKT EM using the standard BKT model with forgetting. "Predictive performance was nearly identical across all methods"; e.g., accuracy 0.694 and AUC 0.711 for all methods, with fit times from 3.35 s to 822 s.

> "Predictive performance was nearly identical across all methods, with accuracy, AUC, and RMSE differing by only a few decimal places. The primary distinction lies in computational cost."

## Discussion

## Related Claims

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it
- BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima — related
- OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets — related
- The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin — related
- [Formalisation of theory offers generative models, counterfactual reasoning, and optimal-performance yardsticks unavailable to verbal accounts](benefits-of-formal-modelling-theory.md) — related
