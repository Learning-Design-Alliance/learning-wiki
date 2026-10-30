---
type: claim
title: "Theorem 1 bounds the maximum individual collusion gain of the grouping-based anti-collusion scheme by (1 - 1/Q)/(M2 - M1 + 1), e.g. below 3.6% for M2 = 60, M1 = 40, Q = 4."
description: Theorem 1 bounds the maximum individual collusion gain of the grouping-based anti-collusion scheme by (1 - 1/Q)/(M2 - M1 + 1), e.g.
id: theorem1-collusion-gain-upper-bound
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: mengzhou-li-2021
    resource: "https://doi.org/10.1038/s41539-020-00083-3"
    title: "Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3"
    author: Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Theorem 1 bounds the maximum individual collusion gain of the grouping-based anti-collusion scheme by (1 - 1/Q)/(M2 - M1 + 1), e.g. below 3.6% for M2 = 60, M1 = 40, Q = 4.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Under the stated assumptions, using the GAS the maximum individual collusion gain can be controlled to be no larger than (1 - 1/Q)/(M2 - M1 + 1). [→ Mengzhou Li 2021](#mengzhou-li-2021)

## Evidence

### Mengzhou Li 2021

Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3

`q1 · i?` · `design · r2`

An analytical theorem (Supplementary Note 1) proved for the idealized DOT scenario with M1 questions drawn from a pool of M2 MCQs with Q choices. The article notes the bound is "practically powerful", giving a theoretical maximum individual collusion gain below 3.6% for M2 = 60, M1 = 40, Q = 4.

> "Given sequences of M 1 questions from the bank of M 2 MCQs with one and only one correct choice out of Q choices for each question, the maximum individual collusion gain can be controlled to be no larger than (1 − 1/Q)/(M2 − M1 + 1) using the GAS"

## Discussion


## Related Claims
- [Numerical simulations over 500 instances show optimized DOT assignments reduce the mean average collusion gain by about three orders of magnitude, robust to noisy competence estimates and stable across class sizes from N = 20 to N = 500.](dot-simulation-robustness-class-sizes.md) — related
- [In a real undergraduate final exam, the DOT optimized question assignment reduced the average collusion gain to 0.0073% from 19.23% under the conventional simultaneous common-question scenario.](dot-final-exam-collusion-gain-three-orders-reduction.md) — related
