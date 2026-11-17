---
type: claim
title: For the present case the GP algorithm should not be run for fewer than 10 generations
description: For the present case the GP algorithm should not be run for fewer than 10 generations
id: gp-minimum-ten-generations-boundary
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

# For the present case the GP algorithm should not be run for fewer than 10 generations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Running the GP algorithm for fewer than 10 generations left the solution insufficiently converged in the reported case. [→ J.O. Orove 2015](#jo-orove-2015)

## Evidence

### J.O. Orove 2015

J.O. Orove, N.E. Osegi, B.O. Eke. (2015). A Multi-Gene Genetic Programming Application for Predicting Students Failure at School. Originally published 2013. [doi:10.48550/arXiv.1503.03211](https://doi.org/10.48550/arXiv.1503.03211)

`q1 · i?` · `design · r2`

Numerical observation from the convergence curves (Figure 8) of the GPSFARPS run. The article qualifies this boundary as applying "for the present case", i.e. the reported data set and parameter settings.

> "it can also be seen that the algorithm should not be run for less than 10 generations for the present case, as the solution would not have converged sufficiently by then."

## Discussion


## Related Claims
- [GPSFARPS simulations show fast convergence of the multi-gene GP run at about 30 generations from a specified maximum of 500](gpsfarps-fast-convergence-30-generations.md) — related
- [The multi-gene GP system minimized the evolved model to 4 of 6 predictor variables while predicting student failure rate](gpsfarps-minimal-model-four-predictors.md) — related
