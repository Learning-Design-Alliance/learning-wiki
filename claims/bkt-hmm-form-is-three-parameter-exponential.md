---
type: claim
title: The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number
description: The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number
id: bkt-hmm-form-is-three-parameter-exponential
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

# The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` The probability of a correct response P(Cj) under the HMM form of BKT has the functional form of an exponential and depends on only three parameters: P(S), P(T), and the combined constant A. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org

`q2 · i?`

Analytical derivation (Section 2): the recursion for P(Lj) is solved exactly, giving P(Cj) = 1 − P(S) − A·e^(−βj), so 'P (Cj) is an exponential' as shown in Fig. 1. No data are fit; this is a closed-form result under the model.

> "Note that the form of P (Cj), as a function of j, depends on only three parameters: P (S), P (T ), and (1−P (S)−P (G)) (1−P (L0))."

## Discussion


## Related Claims
- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](bkt-identifiability-explained-by-parameter-a.md) — related
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
