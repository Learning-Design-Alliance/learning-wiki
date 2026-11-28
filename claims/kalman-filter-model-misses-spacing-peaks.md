---
type: claim
title: The Bayesian Kalman-filter multiscale model misses the peaks of the spacing functions and predicts an optimal ISI that is independent of or decreasing with RI, unlike MCM
description: The Bayesian Kalman-filter multiscale model misses the peaks of the spacing functions and predicts an optimal ISI that is independent of or decreasing with RI, unlike MCM
id: kalman-filter-model-misses-spacing-peaks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-28
evidence_strength: weak
newest_evidence: 2008
recheck_by: 2011
sources:
  - id: mozer-2008
    resource: "https://papers.nips.cc"
    title: "Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2008). Predicting the Optimal Spacing of Study: A Multiscale Context Model of Memory. https://papers.nips.cc"
    author: "Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# The Bayesian Kalman-filter multiscale model misses the peaks of the spacing functions and predicts an optimal ISI that is independent of or decreasing with RI, unlike MCM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In a least-squares fit to the Cepeda et al. (2008) data, the KF model shows a reasonable fit in sum-squared error but misses the peaks of the spacing functions and predicts a peak independent of RI; across parameterizations it generally predicts decreasing or constant optimal ISIs as RI increases. [→ Mozer 2008](#mozer-2008)

## Evidence

### Mozer 2008

Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2008). Predicting the Optimal Spacing of Study: A Multiscale Context Model of Memory. https://papers.nips.cc

`q1 · i?` · `theoretical · r3`

Numerical fitting of the Kording et al. (2007) Kalman-filter model, shown in Figure 2e, with six free parameters fit to the Cepeda et al. (2008) data. The article adds that exploring many parameterizations, the model "generally predicts decreasing or constant optimal ISIs as a function of the RI."

> "In terms of sum-squared error, the model shows a reasonable fit, but the model clearly misses the peaks of the spacing functions, and in fact predicts a peak that is independent of RI."

## Discussion


## Related Claims
- [MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval](mcm-parameter-free-spacing-function-predictions.md) — reports the opposite
- [The optimal gap increases as the retention interval increases, but the ratio of optimal gap to retention interval declines](optimal-gap-rises-with-retention-interval-ratio-declines.md) — reports the opposite
- [The optimal interstudy interval increases as the retention interval increases](optimal-isi-increases-with-retention-interval.md) — reports the opposite
