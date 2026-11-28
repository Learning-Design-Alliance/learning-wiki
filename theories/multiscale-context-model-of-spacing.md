---
type: theory
id: multiscale-context-model-of-spacing
title: Multiscale Context Model of Spacing
description: "Memory traces are held by pools of context units that decay on many time scales; a study episode strengthens the slow pools only when the fast ones no longer hold the item, so wider spacing shifts the trace to slower-decaying pools and the optimal gap grows with the retention interval."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-11-28
---

# Multiscale Context Model of Spacing

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 quant-synthesis, 1 theoretical), `q1`–`q3` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The Multiscale Context Model (MCM) of Mozer, Pashler, Cepeda, Lindsey and Vul (2009) predicts the spacing function: final recall as a function of the gap between study sessions, for a given retention interval. It joins two earlier models. From Raaijmakers' SAM model it takes contextual drift and the retrieval-dependent update (a restudy strengthens the trace less if the item could still be retrieved). From Staddon's multiple time-scale (MTS) model it takes a cascade of leaky integrators with different time constants and an error-correcting update, in which a slow integrator is boosted only to the extent that faster ones fail to represent the item when it is studied. MCM is a network whose input layer is N pools of context units, each pool decaying exponentially with its own time constant.

Short gaps are handled by the fast pools, so the trace decays quickly; longer gaps push the trace into slow pools, so it lasts. The authors' aim was prediction rather than post-hoc fitting: four parameters are fitted to the forgetting function measured for the material after a single study session, one more (the size of the update after a successful recall) was hand-tuned once and held fixed, and MCM then predicts the spacing function with nothing left free. In their report its predictions matched the peaks of seven published spacing functions, with the optimal gap increasing with the retention interval, and it predicted different optimal gaps for two kinds of material studied under the same conditions. A Bayesian multiscale model built on a Kalman filter missed those peaks.

## Implications

### Context
- Two study sessions separated by a gap (ISI), then a test after a retention interval (RI); the forgetting function for the specific material must be measured first.
- Mozer et al. note that SAM explains spacing on one time scale but not across time scales, because its single exponential context drift bounds the time scale it can operate on; MCM's several time constants remove that limit.

### Target Learners
- Adult learners of verbal material in the laboratory and online studies the spacing functions came from.

### Target Learning Objectives
- Choosing the gap between study sessions for a given retention interval and material.

## Claims
- [MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval](../claims/mcm-parameter-free-spacing-function-predictions.md) [+M]
- [MCM predicts different optimal ISIs for two different types of material studied with identical ISI and RI conditions](../claims/mcm-material-specific-peak-prediction.md) [+M]
- [The Bayesian Kalman-filter multiscale model misses the peaks of the spacing functions and predicts an optimal ISI that is independent of or decreasing with RI, unlike MCM](../claims/kalman-filter-model-misses-spacing-peaks.md) [+W]
- [Spacing effects occur on many time scales, and the single-scale SAM model cannot explain effects across different time scales](../claims/sam-single-time-scale-limitation.md) [+W]
- [The lag effect is non-monotonic: beyond an optimal ISI, further increases in ISI reduce final-test accuracy for a given retention interval](../claims/non-monotonic-lag-effect-optimal-isi.md) [+M]

## Related Theories
- [Activation-Based ACT-R Model of the Spacing Effect](act-r-activation-model-of-spacing.md): a rival computational account.
- [Power Law of Forgetting](power-law-of-forgetting.md): summing exponential decays on several time scales yields a curve of this family.
- [Study-Phase Retrieval (Reminding) Account of the Spacing Effect](study-phase-retrieval-account-of-spacing.md): shares the retrieval-dependent update.

## Examples
- [Spaced learning](../patterns/spaced-learning.md)

## Key Sources
- Mozer, M. C., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2009). Predicting the optimal spacing of study: A multiscale context model of memory. *Advances in Neural Information Processing Systems 22* (conference paper; no DOI found). https://papers.nips.cc
