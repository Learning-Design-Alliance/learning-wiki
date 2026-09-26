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
-
