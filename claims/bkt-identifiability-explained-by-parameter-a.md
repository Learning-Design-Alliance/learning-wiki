---
type: claim
title: The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms
description: The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms
id: bkt-identifiability-explained-by-parameter-a
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

# The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Different combinations of P(G) and P(L0) that give the same value of A produce models with exactly the same functional form, explaining the degenerate solutions of the identifiability problem. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. *Journal of Educational Data Mining, 5*(2). [doi:10.5281/zenodo.3554629](https://doi.org/10.5281/zenodo.3554629)

`q2 · i?` · `theoretical · r3`

Analytical argument (Section 3): because A = (1−P(S)−P(G))(1−P(L0)), all points along the curve in Fig. 2 correspond to identical models; the article notes Beck and Chang observed multiple P(G)/P(L0) combinations giving the same error rate but did not explain the origin of the degeneracy.

> "From Eqn. (6), we see that diﬀrent combinations of P (G) and P (L0) that give the same value for A will result in models that have the exact same functional form."

## Discussion

## Related Claims

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima — related
- Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses — related
- [A Hidden Markov Model over knowledge states identifies Analytical Thinking (A5) as the learning bottleneck with the lowest forward transition probability](hmm-identifies-a5-bottleneck.md) — related
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
- [Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior](kt-algorithm-fixed-point-parameter-constraints.md) — related
- [Individualized Knowledge Tracing parameters fit student data significantly better and change mastery-learning practice decisions for many students](individualized-kt-parameters-change-practice-decisions.md) — related
