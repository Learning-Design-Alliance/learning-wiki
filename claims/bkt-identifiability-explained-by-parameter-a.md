---
type: claim
title: The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms
description: The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms
id: bkt-identifiability-explained-by-parameter-a
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

# The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Different combinations of P(G) and P(L0) that give the same value of A produce models with exactly the same functional form, explaining the degenerate solutions of the identifiability problem. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org

`q2 · i?`

Analytical argument (Section 3): because A = (1−P(S)−P(G))(1−P(L0)), all points along the curve in Fig. 2 correspond to identical models; the article notes Beck and Chang observed multiple P(G)/P(L0) combinations giving the same error rate but did not explain the origin of the degeneracy.

> "From Eqn. (6), we see that diﬀrent combinations of P (G) and P (L0) that give the same value for A will result in models that have the exact same functional form."

## Discussion


## Related Claims
- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
