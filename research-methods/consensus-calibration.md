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
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Consensus calibration treats recalibration as a divide-and-conquer Bayesian computation: each time period is calibrated independently and the period posteriors are combined without revisiting earlier data. The procedure works in two layers — per-draw robust characteristic-curve linking to a common metric, then precision-weighted aggregation in which the prior contributed by each period is removed and a single consensus prior is reinstated. The article states that "The correction targets the posterior dispersion, not only its location", and that an update's cost scales with the new data rather than the full history.

## Accounts
<!-- How each source describes or uses the method -->
- **Consensus calibration: a divide-and-conquer Bayesian procedure that reconstructs the pooled posterior of an evolving IRT item bank from independently calibrated periods**: Consensus calibration treats recalibration as a divide-and-conquer Bayesian computation: each time period is calibrated independently and the period posteriors are combined without revisiting earlier data. The procedure works in two layers — per-draw robust characteristic-curve linking to a common metric, then precision-weighted aggregation in which the prior contributed by each period is removed and a single consensus prior is reinstated. The article states that "The correction targets the posterior dispersion, not only its location", and that an update's cost scales with the new data rather than the full history. (Paul A. Jewsbury et al. (2026))
- **Three-lever calibration recipe for LLM-as-judge suites: unanimous-fail panels, per-evaluator judge-model choice, and rubric softening (U/P/C)**: The article's account of calibrating a production LLM-as-judge suite treats each evaluator as a configurable instrument set by three levers. Panels repeat one judge model k times under a unanimous-fail rule with short-circuiting on the first passing verdict; judge models are chosen per evaluator (Sonnet 4.5 for semantic judgments, GPT-5.4 for structural and mathematical verification, Haiku 4.5 for lower cost); and rubrics are softened via three standard blocks: "U, require unambiguity—if the violation is a judgment call, pass; P, require pervasiveness—a single local instance is not enough, the failure must dominate the response; and C, simplify checklists." (Chris Rohlfs et al. (2026))

### Claims
- [Consensus calibration closely reproduces pooled-benchmark item-parameter means and standard deviations on an operational assessment](../claims/consensus-posterior-agrees-with-pooled-benchmark.md) [+M]
- [Consensus calibration shows mild under-dispersion relative to the pooled benchmark, strongest for sparsely observed items, consistent with residual prior over-counting](../claims/mild-under-dispersion-low-exposure-items.md) [~M]
- [Unanimous-fail panels alone reduced benchmark activation by approximately 40% on average for three Critical evaluators, but were insufficient on their own](../claims/unanimous-panels-40-percent-activation-reduction.md) [+M]
- [Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%](../claims/llm-judge-calibration-precision-gain-magicschool.md) [+M]

## Related Research Methods
-

## Key Sources
- Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen. (2026). Bayesian Consensus Calibration of Continuously Evolving IRT Item Banks. https://arxiv.org/abs/2609.13590v1
- Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478
