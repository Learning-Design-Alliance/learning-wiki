---
type: product
id: adaptive-learning-path-navigation-alpn
title: Adaptive Learning Path Navigation (ALPN)
description: A learning-path navigation system proposed by Chen et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Adaptive Learning Path Navigation (ALPN)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A learning-path navigation system proposed by Chen et al. that uses attentive knowledge tracing to estimate learner states and reinforcement learning to recommend exercises toward a mastery threshold.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ALPN: an adaptive learning path navigation framework coupling attentive knowledge tracing with reinforcement-learning exercise recommendation**: The Adaptive Learning Path Navigation (ALPN) system is a framework in which a pre-trained Attentive Knowledge Tracing (AKT) model serves as the environment and a reinforcement-learning agent recommends exercises. AKT "analyzes the student’s learning history and determines their initial knowledge state"; the agent then recommends material, the interaction is added to the history, and the knowledge state is reevaluated iteratively until the student's average pass rate reaches a threshold β. The framework continuously updates knowledge states so recommendations stay tailored to individual needs. (Jyun-Yi Chen et al. (2023))

### Claims
- [The ALPN-EPPO system outperforms the KT-KDM baseline in maximizing students' learning outcomes, by 8.2% on average](../claims/alpn-eppo-outperforms-ktkdm-learning-outcomes.md) [+W]
- [ALPN systems generate more diverse learning paths than KT-KDM, with ALPN-EPPO the most diverse (10.5% higher rate)](../claims/alpn-eppo-higher-learning-path-diversity.md) [+W]
- [ALPN-EPPO enables students to achieve their learning goals with the fewest number of learning activities among the compared systems](../claims/alpn-eppo-fewest-learning-activities.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Jyun-Yi Chen, Saeed Saeedvand, and I-Wei Lai. (2023). Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement Learning. https://arxiv.org/abs/2305.04475v2
