---
type: theory
title: Technical Taxonomy of Fundamental Knowledge Tracing Models
description: "The survey's first organizing axis sorts fundamental KT models by technical route: \"the proposed taxonomy splits existing KT methods into three categories\" — Bayesian models built on probability models, logistic model..."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# Technical Taxonomy of Fundamental Knowledge Tracing Models

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study, `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The survey's first organizing axis sorts fundamental KT models by technical route: "the proposed taxonomy splits existing KT methods into three categories" — Bayesian models built on probability models, logistic models built on logistic functions, and deep learning models built on neural networks. It further divides the deep learning branch into deep, memory-aware, attentive and graph-based knowledge tracing, according to four types of neural networks.

## Design Implications

### Context
#### Requirements
- Bayesian models: Bayesian knowledge tracing and dynamic Bayesian knowledge tracing
- Logistic models: learning factor analysis, performance factor analysis, and knowledge tracing machines
- Deep learning models: deep knowledge tracing (RNN/LSTM), memory-aware knowledge tracing (memory networks), attentive knowledge tracing (self-attention), and graph-based knowledge tracing (graph neural networks)
#### Constraints
- The survey states that deep learning models remain notoriously difficult to interpret owing to their end-to-end learning strategy

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims
- [Deep Learning Knowledge Tracing Outperforms But Lacks Interpretability](../claims/deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) [~W]
- [No Single Knowledge Tracing Model Is Always Best](../claims/no-single-knowledge-tracing-model-is-always-best.md) [~W]

## Related Theories
- [Knowledge Tracing Learner Modeling Task](knowledge-tracing-learner-modeling-task.md)
- [Bayesian Knowledge Tracing Two State Model](bayesian-knowledge-tracing-two-state-model.md)
- [Logistic Knowledge Tracing Models](logistic-knowledge-tracing-models.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
