---
type: research-method
id: srjudge-three-stage-select-reason-judge-framework-for-fine-grained-knowledge-concept-taggi
title: "SRJudge: three-stage Select-Reason-Judge framework for fine-grained knowledge concept tagging"
description: SRJudge decomposes knowledge concept tagging into three stages.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SRJudge: three-stage Select-Reason-Judge framework for fine-grained knowledge concept tagging

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
SRJudge decomposes knowledge concept tagging into three stages. A fine-tuned BERT-based Selector first narrows the candidate space: "the Selector first picks K(≪ |Φ|)candidates ... reducing the decision space". A lightweight LLM Reasoner, trained with a pruned GRPO reinforcement-learning strategy and a task-specific reward combining format, accuracy and dynamic position rewards, recommends a concept with reasons over the shortlist. A frozen larger LLM Judger then evaluates the rationality of the reasoning and issues the final verdict from a global perspective. The framework addresses the problem that LLMs "struggle to select the correct concept from a large-scale candidate set due to the high dimensionality of the decision space".

## Accounts
<!-- How each source describes or uses the method -->
- **SRJudge: a three-stage Select-Reason-Judge framework for fine-grained knowledge concept tagging**: SRJudge decomposes knowledge concept tagging into three stages. A fine-tuned BERT-based Selector first narrows the candidate space: "the Selector first picks K(≪ |Φ|)candidates ... reducing the decision space". A lightweight LLM Reasoner, trained with a pruned GRPO reinforcement-learning strategy and a task-specific reward combining format, accuracy and dynamic position rewards, recommends a concept with reasons over the shortlist. A frozen larger LLM Judger then evaluates the rationality of the reasoning and issues the final verdict from a global perspective. The framework addresses the problem that LLMs "struggle to select the correct concept from a large-scale candidate set due to the high dimensionality of the decision space". (Zhiwei Yang et al. (2026))

### Claims

- [SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets](../claims/srjudge-outperforms-baselines-three-datasets.md) [+M]
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](../claims/srjudge-ablation-components-contribute.md) [+M]
- [SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets](../claims/srjudge-gains-hard-to-distinguish-samples.md) [+W]
- [A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs](../claims/dynamic-position-reward-improves-reasoner.md) [~W]
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](../claims/grpo-alone-inferior-to-sft-for-tagging.md) [~W]

## Related Research Methods
-

## Key Sources
- Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982
