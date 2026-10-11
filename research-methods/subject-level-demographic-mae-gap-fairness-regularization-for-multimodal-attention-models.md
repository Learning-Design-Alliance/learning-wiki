---
type: research-method
id: subject-level-demographic-mae-gap-fairness-regularization-for-multimodal-attention-models
title: Subject-level demographic MAE-gap fairness regularization for multimodal attention models
description: An in-processing fairness framework that adds a demographic disparity penalty to the training objective of a multimodal attention model.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Subject-level demographic MAE-gap fairness regularization for multimodal attention models

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An in-processing fairness framework that adds a demographic disparity penalty to the training objective of a multimodal attention model. Per-subject MAEs are averaged within each demographic group, and "The fairness penalty was defined as the gap between the highest and lowest group-level subject MAE", weighted by a trade-off parameter λ added to the weighted MSE task loss. Regularization is introduced after a two-epoch warm-up, with subject- and group-balanced batch sampling so every represented subject contributes equally to the penalty. λ is selected on validation data subject to a constraint that mean validation MAE increases by no more than 0.02 relative to the unregularized baseline.

## Accounts
<!-- How each source describes or uses the method -->
- **Subject-level demographic MAE-gap fairness regularization for multimodal attention models**: An in-processing fairness framework that adds a demographic disparity penalty to the training objective of a multimodal attention model. Per-subject MAEs are averaged within each demographic group, and "The fairness penalty was defined as the gap between the highest and lowest group-level subject MAE", weighted by a trade-off parameter λ added to the weighted MSE task loss. Regularization is introduced after a two-epoch warm-up, with subject- and group-balanced batch sampling so every represented subject contributes equally to the penalty. λ is selected on validation data subject to a constraint that mean validation MAE increases by no more than 0.02 relative to the unregularized baseline. (Christoforos Fragkiadakis et al. (2026))

### Claims
- [Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects](../claims/mae-gap-regularization-validation-gains-do-not-generalize.md) [~M]

## Related Research Methods
-

## Key Sources
- Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232
