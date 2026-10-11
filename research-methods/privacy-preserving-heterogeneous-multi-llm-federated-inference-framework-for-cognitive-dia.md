---
type: research-method
id: privacy-preserving-heterogeneous-multi-llm-federated-inference-framework-for-cognitive-dia
title: Privacy-preserving heterogeneous multi-LLM federated inference framework for cognitive diagnosis
description: A four-stage framework in which heterogeneous commercial LLMs (LLaMA-3.3-70B, GPT-4o-mini, Claude-3-Haiku) independently predict student knowledge states via engineered prompts, add calibrated Laplace noise locally to their prediction outputs, and aggregate with residual correction.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Privacy-preserving heterogeneous multi-LLM federated inference framework for cognitive diagnosis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A four-stage framework in which heterogeneous commercial LLMs (LLaMA-3.3-70B, GPT-4o-mini, Claude-3-Haiku) independently predict student knowledge states via engineered prompts, add calibrated Laplace noise locally to their prediction outputs, and aggregate with residual correction. The article describes it as "the first privacy-preserving heterogeneous multi-LLM federated inference framework for cognitive diagnosis", operating entirely at the prediction level with models frozen and accessible only via black-box APIs. It integrates Q-matrix theory to constrain prompts to relevant concepts and rests on an honest-but-curious trust paradigm.

## Accounts
<!-- How each source describes or uses the method -->
- **Privacy-preserving heterogeneous multi-LLM federated inference framework for cognitive diagnosis**: A four-stage framework in which heterogeneous commercial LLMs (LLaMA-3.3-70B, GPT-4o-mini, Claude-3-Haiku) independently predict student knowledge states via engineered prompts, add calibrated Laplace noise locally to their prediction outputs, and aggregate with residual correction. The article describes it as "the first privacy-preserving heterogeneous multi-LLM federated inference framework for cognitive diagnosis", operating entirely at the prediction level with models frozen and accessible only via black-box APIs. It integrates Q-matrix theory to constrain prompts to relevant concepts and rests on an honest-but-curious trust paradigm. (Yagna Manasa Boyapati et al. (2026))

### Claims
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](../claims/multi-llm-federated-cognitive-diagnosis-improvement.md) [+M]
- [Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets](../claims/residual-correction-essential-heterogeneous-aggregation.md) [+M]
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](../claims/privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) [+M]

## Related Research Methods
-

## Key Sources
- Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947
