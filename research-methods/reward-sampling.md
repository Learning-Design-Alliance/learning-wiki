---
type: research-method
id: reward-sampling
title: Reward sampling
description: "Reward sampling is a Monte-Carlo sampling framework that allocates a limited expert-human budget to the responses most likely to improve a test-taker's aggregate score."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Reward sampling

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Reward sampling is a Monte-Carlo sampling framework that allocates a limited expert-human budget to the responses most likely to improve a test-taker's aggregate score. For each record it computes an expected reward, "the magnitude of the change in the global score that would occur when a local response is changed as a result of human correction of machine score", weighted by the probability of each possible ground-truth class from a human-machine agreement matrix. Rewards are additively smoothed and normalized into a sampling distribution. The article positions it between machine-only and full double-scoring paradigms.

## Accounts
<!-- How each source describes or uses the method -->
- **Reward sampling: Monte-Carlo sampling of responses for human scoring based on expected change in the global score**: Reward sampling is a Monte-Carlo sampling framework that allocates a limited expert-human budget to the responses most likely to improve a test-taker's aggregate score. For each record it computes an expected reward, "the magnitude of the change in the global score that would occur when a local response is changed as a result of human correction of machine score", weighted by the probability of each possible ground-truth class from a human-machine agreement matrix. Rewards are additively smoothed and normalized into a sampling distribution. The article positions it between machine-only and full double-scoring paradigms. (Yaman Kumar Singla et al. (2022))

### Claims
- [Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines](../claims/reward-sampling-improves-automated-scoring-accuracy-qwk.md) [+M]
- [Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows](../claims/reward-sampling-gains-largest-below-30-percent-budget.md) [~M]

## Related Research Methods
-

## Key Sources
- Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. https://arxiv.org/abs/2111.08906
