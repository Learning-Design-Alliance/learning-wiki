---
type: research-method
id: learning-rate-model-lr-model
title: Learning Rate Model (LR-Model)
description: The LR-Model is a statistical model underlying normalized gain scores, adopted from prior work by Navarrete.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Learning Rate Model (LR-Model)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The LR-Model is a statistical model underlying normalized gain scores, adopted from prior work by Navarrete. It assumes instruction delivers bounded knowledge, pretest X and posttest Y are errorless with 0 ≤ X ≤ Y ≤ 1, and that prior knowledge X and learning rate F are independent random variables. Its key hypothesis is that "the raw gains of knowledge G = Y − X are proportional to both the amount of unfamiliar knowledge (1 − X) encountered by the learner during the learning process and the learning rate F", giving Y = X + (1 − X)F. The learning rate F represents the learner's ability to acquire unfamiliar knowledge under a specific learning environment and is estimated empirically by ng or cng. This study extends the model with additive measurement errors to analyze the two estimators.

## Accounts
<!-- How each source describes or uses the method -->
- **Learning Rate Model (LR-Model)**: The LR-Model is a statistical model underlying normalized gain scores, adopted from prior work by Navarrete. It assumes instruction delivers bounded knowledge, pretest X and posttest Y are errorless with 0 ≤ X ≤ Y ≤ 1, and that prior knowledge X and learning rate F are independent random variables. Its key hypothesis is that "the raw gains of knowledge G = Y − X are proportional to both the amount of unfamiliar knowledge (1 − X) encountered by the learner during the learning process and the learning rate F", giving Y = X + (1 − X)F. The learning rate F represents the learner's ability to acquire unfamiliar knowledge under a specific learning environment and is estimated empirically by ng or cng. This study extends the model with additive measurement errors to analyze the two estimators. (Jairo Navarrete et al. (2024))

### Claims
- [Without measurement errors, both learning-rate estimators (average ngain and ngain of the average learner) are unbiased, and any difference between them is random](../claims/errorless-case-both-ngain-estimators-unbiased.md) [+M]
- [Measurement errors in pretest and posttest scores induce a spurious negative pretest-ngain correlation even when prior knowledge and learning rate are independent](../claims/measurement-errors-induce-spurious-pretest-ngain-correlation.md) [+M]

## Related Research Methods
-

## Key Sources
- Jairo Navarrete, Valentina Giaconi, Gonzalo Contador, Mariano Vazquez. (2024). Another reason why normalized gain should continue to be used to analyze concept inventories (and estimate learning rates). arXiv. https://arxiv.org/abs/2407.07730
