---
type: claim
title: "The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately"
description: "The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately"
id: kt-algorithm-no-identifiability-problem
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: brett-van-de-sande-2013
    resource: "https://doi.org/10.5281/zenodo.3554629"
    title: "Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. *Journal of Educational Data Mining, 5*(2). [doi:10.5281/zenodo.3554629](https://doi.org/10.5281/zenodo.3554629)"
    author: Van de Sande, B.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` So long as there are both correct and incorrect steps, no redefinition of 1−P(Lj|Oj) can be compensated by redefining other parameters in both recursion equations, so all four model parameters are needed. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. *Journal of Educational Data Mining, 5*(2). [doi:10.5281/zenodo.3554629](https://doi.org/10.5281/zenodo.3554629)

`q2 · i?` · `theoretical · r3`

Analytical argument (Section 4): P(G) appears with a different functional form in the numerator of each of Eqns. (11) and (12), so 'all four model parameters are needed to deﬁne the behavior of the Knowledge Tracing Algorithm.'

> "Finally, the “Identiﬁability Problem” for the Knowledge Tracing Algorithm does not exist, so long as there are both correct and incorrect steps."

## Discussion


## Related Claims
- [Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior](kt-algorithm-fixed-point-parameter-constraints.md) — related
- BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses — related
- [A Hidden Markov Model over knowledge states identifies Analytical Thinking (A5) as the learning bottleneck with the lowest forward transition probability](hmm-identifies-a5-bottleneck.md) — related
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](bkt-identifiability-explained-by-parameter-a.md) — related
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
