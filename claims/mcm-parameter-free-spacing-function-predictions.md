---
type: claim
title: "MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval"
description: "MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval"
id: mcm-parameter-free-spacing-function-predictions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-28
evidence_strength: moderate
newest_evidence: 2008
recheck_by: 2011
sources:
  - id: mozer-2008
    resource: "https://papers.nips.cc"
    title: "Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2008). Predicting the Optimal Spacing of Study: A Multiscale Context Model of Memory. https://papers.nips.cc"
    author: "Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MCM, with parameters fully determined by the forgetting function and one hand-tuned parameter, predicts the peaks of the spacing functions in Cepeda's experiments, with curvature of the peak decreasing and optimal ISI increasing with RI. [→ Mozer 2008](#mozer-2008)

## Evidence

### Mozer 2008

Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2008). Predicting the Optimal Spacing of Study: A Multiscale Context Model of Memory. https://papers.nips.cc

`q2 · i?` · `theoretical · r3`

Numerical simulation results shown in Figure 2, fitting MCM to the forgetting functions of Cepeda and colleagues' experiments (Swahili-English pairs, obscure facts, object names, and a study with 11 ISIs and four RIs) and predicting the spacing functions with no further fitting. No effect size is printed.

> "MCM predicts the spacing functions with absolutely spectacular precision, considering the predictions are fully constrained and parameter free. Moreover, MCM anticipates the peaks of the spacing functions, with the curvature of the peak decreasing with the RI, and the optimal ISI increasing with the RI."

## Discussion


## Related Claims
- [The Bayesian Kalman-filter multiscale model misses the peaks of the spacing functions and predicts an optimal ISI that is independent of or decreasing with RI, unlike MCM](kalman-filter-model-misses-spacing-peaks.md) — reports the opposite
- [MCM predicts different optimal ISIs for two different types of material studied with identical ISI and RI conditions](mcm-material-specific-peak-prediction.md) — a narrower finding that bears on this claim
- [The optimal interstudy interval increases as the retention interval increases](optimal-isi-increases-with-retention-interval.md) — a broader claim this one bears on
- [The lag effect is non-monotonic: beyond an optimal ISI, further increases in ISI reduce final-test accuracy for a given retention interval](non-monotonic-lag-effect-optimal-isi.md) — related
