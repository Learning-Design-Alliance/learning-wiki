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
> **Evidence** · 3 claims (3 for) · 4 studies (3 associational, 1 theoretical), `q2`–`q3` · 0 of 4 report an effect size · 2 claims rest on one study

## Description
The LR-Model is a statistical model underlying normalized gain scores, adopted from prior work by Navarrete. It assumes instruction delivers bounded knowledge, pretest X and posttest Y are errorless with 0 ≤ X ≤ Y ≤ 1, and that prior knowledge X and learning rate F are independent random variables. Its key hypothesis is that "the raw gains of knowledge G = Y − X are proportional to both the amount of unfamiliar knowledge (1 − X) encountered by the learner during the learning process and the learning rate F", giving Y = X + (1 − X)F. The learning rate F represents the learner's ability to acquire unfamiliar knowledge under a specific learning environment and is estimated empirically by ng or cng. This study extends the model with additive measurement errors to analyze the two estimators.

## Accounts
<!-- How each source describes or uses the method -->
- **Learning Rate Model (LR-Model)**: The LR-Model is a statistical model underlying normalized gain scores, adopted from prior work by Navarrete. It assumes instruction delivers bounded knowledge, pretest X and posttest Y are errorless with 0 ≤ X ≤ Y ≤ 1, and that prior knowledge X and learning rate F are independent random variables. Its key hypothesis is that "the raw gains of knowledge G = Y − X are proportional to both the amount of unfamiliar knowledge (1 − X) encountered by the learner during the learning process and the learning rate F", giving Y = X + (1 − X)F. The learning rate F represents the learner's ability to acquire unfamiliar knowledge under a specific learning environment and is estimated empirically by ng or cng. This study extends the model with additive measurement errors to analyze the two estimators. (Jairo Navarrete et al. (2024))
- **Measure individual rate of learning with a dynamic, model-based measure on a maximally novel task**: The article derives methodological requirements for measuring an individual's ability to consolidate instances. The measure "needs to be dynamic", capturing change in performance with practice rather than a single-point performance; improvement should be referenced to a model of learning, because simple difference scores are inevitably correlated with initial performance; and the task should be as novel as possible, independent of previously consolidated abilities. (Marinelli CV et al. (2021))

### Claims
- [Without measurement errors, both learning-rate estimators (average ngain and ngain of the average learner) are unbiased, and any difference between them is random](../claims/errorless-case-both-ngain-estimators-unbiased.md) [+M]
- [Measurement errors in pretest and posttest scores induce a spurious negative pretest-ngain correlation even when prior knowledge and learning rate are independent](../claims/measurement-errors-induce-spurious-pretest-ngain-correlation.md) [+M]
- [Individual power-fit learning parameters predict performance in item-based reading, spelling, and maths tasks across domains](../claims/learning-parameters-predict-item-based-tasks-cross-domain.md) [+M]

## Related Research Methods
-

## Key Sources
- Jairo Navarrete, Valentina Giaconi, Gonzalo Contador, Mariano Vazquez. (2024). Another reason why normalized gain should continue to be used to analyze concept inventories (and estimate learning rates). arXiv. https://arxiv.org/abs/2407.07730
- Marinelli CV, Angelelli P, Martelli M, Trenta M and Zoccolotti P (2021) Ability to Consolidate Instances as a Proxy for the Association Among Reading, Spelling, and Math Learning Skill. Front. Psychol. 12:761696. https://doi.org/10.3389/fpsyg.2021.761696
