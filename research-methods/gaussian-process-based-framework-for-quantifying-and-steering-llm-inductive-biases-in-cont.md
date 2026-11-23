---
type: research-method
id: gaussian-process-based-framework-for-quantifying-and-steering-llm-inductive-biases-in-cont
title: Gaussian-Process-based framework for quantifying and steering LLM inductive biases in continuous function learning
description: The article proposes a unified testbed that casts in-context learning as non-parametric regression under known GP priors.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Gaussian-Process-based framework for quantifying and steering LLM inductive biases in continuous function learning

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The article proposes a unified testbed that casts in-context learning as non-parametric regression under known GP priors. It combines learning-curve evaluation against two references — GP regression as an empirical lower bound and a derived 1-NN rule as a data-driven upper bound — with a likelihood-based inductive-bias analysis: "given a history of demonstrations, we compute the GP posterior predictive distribution under diﬀerent kernel families and record the log-likelihood of the model’s prediction". Aggregating these likelihoods identifies which kernels best explain model behavior, and the resulting bias map is used to target post-training curricula at the kernels under which base models are least consistent.

## Accounts
<!-- How each source describes or uses the method -->
- **Gaussian-Process-based framework for quantifying and steering LLM inductive biases in continuous function learning**: The article proposes a unified testbed that casts in-context learning as non-parametric regression under known GP priors. It combines learning-curve evaluation against two references — GP regression as an empirical lower bound and a derived 1-NN rule as a data-driven upper bound — with a likelihood-based inductive-bias analysis: "given a history of demonstrations, we compute the GP posterior predictive distribution under diﬀerent kernel families and record the log-likelihood of the model’s prediction". Aggregating these likelihoods identifies which kernels best explain model behavior, and the resulting bias map is used to target post-training curricula at the kernels under which base models are least consistent. (Elif Akata et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Elif Akata, Konstantinos Voudouris, Vincent Fortuin, Eric Schulz. (2026). In-Context Function Learning in Large Language Models. AISTATS 2026. https://arxiv.org/abs/2602.11863
