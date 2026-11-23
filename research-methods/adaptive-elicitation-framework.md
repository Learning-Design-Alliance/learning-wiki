---
type: research-method
id: adaptive-elicitation-framework
title: Adaptive elicitation framework
description: "The framework replaces direct probabilistic modeling of a latent entity (a student's skill profile, a patient's health status, a respondent's opinions) with a predictive view: a language model meta-trained on historical question–answer trajectories simulates future answers, and conditional entropy o"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Adaptive elicitation framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The framework replaces direct probabilistic modeling of a latent entity (a student's skill profile, a patient's health status, a respondent's opinions) with a predictive view: a language model meta-trained on historical question–answer trajectories simulates future answers, and conditional entropy over those simulated answers serves as the uncertainty measure. The article states it adopts "a predictive view of uncertainty that avoids the need to directly model latent variables." Question selection then maximizes Expected Information Gain, computed via autoregressive forward simulation, using greedy or MCTS policies. It can be applied directly on top of pre-trained LLMs.

## Accounts
<!-- How each source describes or uses the method -->
- **Adaptive elicitation framework: a predictive view of latent uncertainty using meta-learned LLM forward simulation**: The framework replaces direct probabilistic modeling of a latent entity (a student's skill profile, a patient's health status, a respondent's opinions) with a predictive view: a language model meta-trained on historical question–answer trajectories simulates future answers, and conditional entropy over those simulated answers serves as the uncertainty measure. The article states it adopts "a predictive view of uncertainty that avoids the need to directly model latent variables." Question selection then maximizes Expected Information Gain, computed via autoregressive forward simulation, using greedy or MCTS policies. It can be applied directly on top of pre-trained LLMs. (Jimmy Wang* et al. (2025))

### Claims

## Related Research Methods
-

## Key Sources
- Jimmy Wang*, Thomas Zollo*, Richard Zemel, Hongseok Namkoong. (2025). Adaptive Elicitation of Latent Information Using Natural Language. Published as a conference paper at ICML 2025. https://arxiv.org/abs/2504.04204
