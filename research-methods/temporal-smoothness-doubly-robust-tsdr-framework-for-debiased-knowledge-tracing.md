---
type: research-method
id: temporal-smoothness-doubly-robust-tsdr-framework-for-debiased-knowledge-tracing
title: Temporal Smoothness Doubly Robust (TSDR) framework for debiased knowledge tracing
description: "TSDR is a model-agnostic debiasing framework for knowledge tracing that integrates a doubly robust estimator — combining Inverse Propensity Weighting with error imputation — with a temporal smoothness regularizer on the imputation model's latent trajectory."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# Temporal Smoothness Doubly Robust (TSDR) framework for debiased knowledge tracing

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
TSDR is a model-agnostic debiasing framework for knowledge tracing that integrates a doubly robust estimator — combining Inverse Propensity Weighting with error imputation — with a temporal smoothness regularizer on the imputation model's latent trajectory. The article states that "TSDR jointly optimizes the KT predictor and the imputation model with a smoothness regularizer, effectively reducing variance while preserving the unbiasedness guarantee of DR." It treats each time step's knowledge state as a temporal "user" and co-optimizes propensity, imputation, and KT models via an alternating strategy. The smoothness constraint is motivated by the Power Law of Practice, characterizing skill acquisition as a smooth power-function trajectory.

## Accounts
<!-- How each source describes or uses the method -->
- **Temporal Smoothness Doubly Robust (TSDR) framework for debiased knowledge tracing**: TSDR is a model-agnostic debiasing framework for knowledge tracing that integrates a doubly robust estimator — combining Inverse Propensity Weighting with error imputation — with a temporal smoothness regularizer on the imputation model's latent trajectory. The article states that "TSDR jointly optimizes the KT predictor and the imputation model with a smoothness regularizer, effectively reducing variance while preserving the unbiasedness guarantee of DR." It treats each time step's knowledge state as a temporal "user" and co-optimizes propensity, imputation, and KT models via an alternating strategy. The smoothness constraint is motivated by the Power Law of Practice, characterizing skill acquisition as a smooth power-function trajectory. (Peilin Zhan et al. (2026))

### Claims
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](../claims/tsdr-improves-kt-backbone-auc-benchmarks.md) [+M]
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](../claims/tsdr-robust-across-mnar-spectrum.md) [+M]

## Related Research Methods
-

## Key Sources
- Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958
