---
type: claim
title: "The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately"
description: "The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately"
id: kt-algorithm-no-identifiability-problem
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
---

# The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` So long as there are both correct and incorrect steps, no redefinition of 1−P(Lj|Oj) can be compensated by redefining other parameters in both recursion equations, so all four model parameters are needed. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org

`q2 · i?`

Analytical argument (Section 4): P(G) appears with a different functional form in the numerator of each of Eqns. (11) and (12), so 'all four model parameters are needed to deﬁne the behavior of the Knowledge Tracing Algorithm.'

> "Finally, the “Identiﬁability Problem” for the Knowledge Tracing Algorithm does not exist, so long as there are both correct and incorrect steps."

## Discussion


## Related Claims
- [Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior](kt-algorithm-fixed-point-parameter-constraints.md) — related
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
