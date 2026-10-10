---
type: claim
title: "A Bayesian DINA model converges successfully on educational response data with 91.3% sparsity where the EM algorithm failed"
description: "A Bayesian DINA model converges successfully on educational response data with 91.3% sparsity where the EM algorithm failed"
id: bayesian-dina-converges-sparse-data
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: feng-z-and-huang-k-2026
    title: Feng Z and Huang K 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A Bayesian DINA model converges successfully on educational response data with 91.3% sparsity where the EM algorithm failed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The Bayesian DINA model achieved convergence on the EdNet dataset (N = 5,000, sparsity 91.3%) with all R-hat values below 1.01 and effective sample sizes above 200. [→ Feng Z and Huang K 2026](#feng-z-and-huang-k-2026)

## Evidence

### Feng Z and Huang K 2026

Feng Z and Huang K (2026) Bayesian cognitive diagnosis optimizes personalized learning paths via mediation of cognitive load and Hidden Markov Model state transitions. Front. Psychol. 17:1879982. https://doi.org/10.3389/fpsyg.2026.1879982

`q2 · i?` · `causal · r2`

MCMC estimation of the Bayesian DINA model on a filtered EdNet KT1 sample of 5,000 students and 582 items with 91.3% matrix sparsity. The article reports "R-hat values for all parameters ranged from 1.002 to 1.008" and effective sample sizes all greater than 200, answering the paper's first research question.

> "The Bayesian DINA model converged successfully on the EdNet dataset (N = 5,000, sparsity = 91.3%). The R-hat values for all parameters ranged from 1.002 to 1.008, all below the convergence threshold of 1.01"

## Discussion


## Related Claims
- [A convergence screen excluding non-converged (item, parameter) pairs removed 1.9% of pairs from the benchmark comparison](convergence-screen-removed-1-9-percent-pairs.md) — related
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
