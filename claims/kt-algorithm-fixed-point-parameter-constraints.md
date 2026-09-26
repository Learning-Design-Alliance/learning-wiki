---
type: claim
title: Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior
description: Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior
id: kt-algorithm-fixed-point-parameter-constraints
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: brett-van-de-sande-2013
    resource: "https://jedm.educationaldatamining.org"
    title: "Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org"
    author: Brett Van de Sande
    q: 2
    i: "?"
  - id: brett-van-de-sande-2013-2
    resource: "https://jedm.educationaldatamining.org"
    title: "Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org"
    author: Brett Van de Sande
    q: 2
    i: "?"
---

# Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` For P(Lj|Oj) to remain in [0,1] and converge properly, the parameters must satisfy P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)); the P(T) constraint completely supersedes the other. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)
`q2 i?` With parameters consistent with negative learning (P(S)+P(G)>1), the algorithm's behavior inverts: P(Lj|Oj) decreases for correct steps and increases for incorrect steps. [→ Brett Van de Sande 2013 (2)](#brett-van-de-sande-2013-2)

## Evidence

### Brett Van de Sande 2013

Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org

`q2 · i?`

Analytical fixed point analysis (Section 4) of the recursion relations Eqns. (11) and (12), illustrated in Fig. 3: stable fixed points at 1 and at (1−P(G))P(T)/(1−P(G)−P(S)) yield the constraints (15) and (16); Fig. 4 plots the allowed region.

> "In order for P (Lj|Oj) to remain in the interval [0 , 1] for any starting value P (L0)∈ [0, 1] and any sequence of correct/incorrect steps Oj, we need the stable ﬁxed point (14) to lie in the interval [0 , 1] and the unstable ﬁxed point (13) to remain negative."

### Brett Van de Sande 2013 (2)

Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org

`q2 · i?`

Analytical result (Section 4): under negative-learning parameters the recursion behavior inverts, so correct responses lower the knowledge estimate and incorrect responses raise it — the 'empirically degenerate' behavior Baker, Corbett, and Aleven defined.

> "If we instead choose parameters consistent with negative learning,P (S)+P (G)> 1, we ﬁnd that the behavior of P (Lj|Oj) becomes inverted: P (Lj|Oj) decreases for correct steps and increases for incorrect steps."

## Discussion


## Related Claims
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
