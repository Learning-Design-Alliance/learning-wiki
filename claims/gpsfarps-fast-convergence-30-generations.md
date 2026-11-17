---
type: claim
title: GPSFARPS simulations show fast convergence of the multi-gene GP run at about 30 generations from a specified maximum of 500
description: GPSFARPS simulations show fast convergence of the multi-gene GP run at about 30 generations from a specified maximum of 500
id: gpsfarps-fast-convergence-30-generations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2015
sources:
  - id: jo-orove-2015
    resource: "https://doi.org/10.48550/arXiv.1503.03211"
    title: "J.O. Orove, N.E. Osegi, B.O. Eke. (2015). A Multi-Gene Genetic Programming Application for Predicting Students Failure at School. Originally published 2013. [doi:10.48550/arXiv.1503.03211](https://doi.org/10.48550/arXiv.1503.03211)"
    author: J.O. Orove, N.E. Osegi, B.O. Eke
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# GPSFARPS simulations show fast convergence of the multi-gene GP run at about 30 generations from a specified maximum of 500

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` In GPSFARPS simulations on student raw score data, the multi-gene GP algorithm converged at about 30 generations out of a maximum specified generation of 500. [→ J.O. Orove 2015](#jo-orove-2015)

## Evidence

### J.O. Orove 2015

J.O. Orove, N.E. Osegi, B.O. Eke. (2015). A Multi-Gene Genetic Programming Application for Predicting Students Failure at School. Originally published 2013. [doi:10.48550/arXiv.1503.03211](https://doi.org/10.48550/arXiv.1503.03211)

`q1 · i?` · `design · r2`

Numerical simulation result from the GPSFARPS run on the sample student raw score data (Table 1) with the Table 2 parameter settings. The convergence curves in Figure 8 show that "3 0 generations is sufficient for the convergence of the algorithm", with the objective function changing little near the end of the run.

> "The MGGP convergence characteristics in Figure 8  also indicate that , 3 0 generations is sufficient for the convergence of the algorithm."

## Discussion


## Related Claims
- [For the present case the GP algorithm should not be run for fewer than 10 generations](gp-minimum-ten-generations-boundary.md) — related
- [The multi-gene GP system minimized the evolved model to 4 of 6 predictor variables while predicting student failure rate](gpsfarps-minimal-model-four-predictors.md) — related
- [Evolved multi-gene GP solutions exhibit an accuracy-complexity trade-off with a non-dominated Pareto front](mggp-pareto-accuracy-complexity-tradeoff.md) — related
