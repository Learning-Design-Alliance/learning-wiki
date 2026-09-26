---
type: claim
title: Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses
description: Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses
id: bkt-mastery-floor-above-learn-rate
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
    q: 1
    i: 1
---

# Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case · `i1` small

## Subclaims
`q1 i?` Analytically, for any non-degenerate learned BKT parameters with P(G)<0.5, P(S)<0.5, and forgetting below 1-P(T), the mastery probability P(Lt) exceeds P(T) for all t, even when every response is incorrect. [→ Badrinath 2023](#badrinath-2023)

## Evidence

### Badrinath 2023

Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN

`q1 · i1`

Analytical derivation (Section 4.1 and Appendix A) of the BKT posterior and limit for a student answering all questions incorrectly. The paper shows "the mastery probability P (Lt)>P (T ) for allt", and illustrates with a learned learn rate of 0.887 where mastery converges to 1.

> "the eventual probability of mastery P (L∞) converges to greater than the learned value ofP (T ). In fact, the mastery probability P (Lt)>P (T ) for allt."

## Discussion


## Related Claims
- [MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons](ms-bkt-estimates-fluctuate-less-than-bkt.md) — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- [Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior](kt-algorithm-fixed-point-parameter-constraints.md) — related
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](bkt-identifiability-explained-by-parameter-a.md) — related
- [BKTransformer's generated parameters evolve intuitively with student response sequences, supporting interpretability of mastery and correctness predictions](bkt-parameter-evolution-interpretability.md) — reports the opposite
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
