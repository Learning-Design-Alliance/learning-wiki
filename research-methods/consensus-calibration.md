---
type: research-method
id: consensus-calibration
title: Consensus calibration
description: "Consensus calibration treats recalibration as a divide-and-conquer Bayesian computation: each time period is calibrated independently and the period posteriors are combined without revisiting earlier data."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Consensus calibration

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Consensus calibration treats recalibration as a divide-and-conquer Bayesian computation: each time period is calibrated independently and the period posteriors are combined without revisiting earlier data. The procedure works in two layers — per-draw robust characteristic-curve linking to a common metric, then precision-weighted aggregation in which the prior contributed by each period is removed and a single consensus prior is reinstated. The article states that "The correction targets the posterior dispersion, not only its location", and that an update's cost scales with the new data rather than the full history.

## Accounts
<!-- How each source describes or uses the method -->
- **Consensus calibration: a divide-and-conquer Bayesian procedure that reconstructs the pooled posterior of an evolving IRT item bank from independently calibrated periods**: Consensus calibration treats recalibration as a divide-and-conquer Bayesian computation: each time period is calibrated independently and the period posteriors are combined without revisiting earlier data. The procedure works in two layers — per-draw robust characteristic-curve linking to a common metric, then precision-weighted aggregation in which the prior contributed by each period is removed and a single consensus prior is reinstated. The article states that "The correction targets the posterior dispersion, not only its location", and that an update's cost scales with the new data rather than the full history. (Paul A. Jewsbury et al. (2026))

### Claims
- [Consensus calibration closely reproduces pooled-benchmark item-parameter means and standard deviations on an operational assessment](../claims/consensus-posterior-agrees-with-pooled-benchmark.md) [+M]
- [Consensus calibration shows mild under-dispersion relative to the pooled benchmark, strongest for sparsely observed items, consistent with residual prior over-counting](../claims/mild-under-dispersion-low-exposure-items.md) [~M]

## Related Research Methods
-

## Key Sources
- Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen. (2026). Bayesian Consensus Calibration of Continuously Evolving IRT Item Banks. https://arxiv.org/abs/2609.13590v1
