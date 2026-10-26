---
type: claim
title: Numerical simulations over 500 instances show optimized DOT assignments reduce the mean average collusion gain by about three orders of magnitude, robust to noisy competence estimates and stable across class sizes from N = 20 to N = 500.
description: Numerical simulations over 500 instances show optimized DOT assignments reduce the mean average collusion gain by about three orders of magnitude, robust to noisy competence estimates and stable across class sizes fro...
id: dot-simulation-robustness-class-sizes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: mengzhou-li-2021
    resource: "https://doi.org/10.1038/s41539-020-00083-3"
    title: "Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3"
    author: Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: mengzhou-li-2021-2
    resource: "https://doi.org/10.1038/s41539-020-00083-3"
    title: "Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3"
    author: Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Numerical simulations over 500 instances show optimized DOT assignments reduce the mean average collusion gain by about three orders of magnitude, robust to noisy competence estimates and stable across class sizes from N = 20 to N = 500.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` In simulation with random Gaussian-distributed competence profiles, the mean of the average collusion gain was reduced from 0.16278 (no prevention) to 0.00007 (optimized) over 500 instances. [→ Mengzhou Li 2021](#mengzhou-li-2021)
`q1 i?` Across four class sizes from N = 20 to N = 500, the mean of the average collusion gain under optimized assignments remained at a very small level. [→ Mengzhou Li 2021 (2)](#mengzhou-li-2021-2)

## Evidence

### Mengzhou Li 2021

Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3

`q1 · i?` · `design · r2`

Numerical simulation over 500 random Gaussian competence profiles (mu0 = (1 + 1/Q)/2, sigma0 = (1 - 1/Q)/6) with heuristic colluding matrix P, comparing no prevention (mean 0.16278) with optimized assignments (mean 0.00007), reported in Table 1b.

> "It can be observed in this case that the mean of the average collusion gain can be reduced by three orders of magnitude with tiny standard deviations, suggesting that our DOT designs are not only effective but also stable in controlling the collusion gain."

### Mengzhou Li 2021 (2)

Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3

`q1 · i?` · `design · r2`

Simulation of optimized assignments for four class sizes (N = 20, 40, 100, 500) over 500 random competence profiles each, reported in Table 1c; the mean average collusion gain stayed at a very small level across all sizes.

> "We further changed the number of students to those of four typical class sizes from N = 20 to N = 500 as shown in Table 1c, and the mean of the average collusion gain remains at a very small level which implies the practical applicability of our method in dealing with a wide range of class sizes."

## Discussion


## Related Claims
- [In a real undergraduate final exam, the DOT optimized question assignment reduced the average collusion gain to 0.0073% from 19.23% under the conventional simultaneous common-question scenario.](dot-final-exam-collusion-gain-three-orders-reduction.md) — related
- [Post-exam analyses found no evidence of significant collusion: paired tests of identical incorrect answers were below the 0.05 significance threshold at every false discovery rate, and the Wilcoxon signed-rank test on first-versus-last-20-question correctness yielded p = 0.3133.](dot-post-exam-no-significant-collusion.md) — related
- [Theorem 1 bounds the maximum individual collusion gain of the grouping-based anti-collusion scheme by (1 - 1/Q)/(M2 - M1 + 1), e.g. below 3.6% for M2 = 60, M1 = 40, Q = 4.](theorem1-collusion-gain-upper-bound.md) — related
