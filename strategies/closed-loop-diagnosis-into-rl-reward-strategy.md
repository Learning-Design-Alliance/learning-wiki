---
type: strategy
id: closed-loop-diagnosis-into-rl-reward-strategy
title: Closed-loop integration of cognitive diagnosis outputs into RL reward functions for adaptive scheduling
description: A design strategy where cognitive diagnosis outputs (weak knowledge points, forgetting parameters, mastery probabilities) directly inform the reinforcement learning reward function for task scheduling.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: an-jie-2026
    resource: "https://doi.org/10.1186/s12909-026-09002-3"
    title: "An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun (2026). Rebuilding ability acquisition in medical imaging teaching: a multi-level AI-driven teaching paradigm based on cognitive-information theory. BMC Medical Education. https://doi.org/10.1186/s12909-026-09002-3"
    author: An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun
---

# Closed-loop integration of cognitive diagnosis outputs into RL reward functions for adaptive scheduling

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 review), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A design strategy where cognitive diagnosis outputs (weak knowledge points, forgetting parameters, mastery probabilities) directly inform the reinforcement learning reward function for task scheduling. The reward function integrates learning gain, task efficiency, and cognitive load: R = w1·ΔK – w2·CL + w3·E, with weights w1=0.5, w2=0.3, w3=0.2 determined through pre-experiments. This addresses the 'state-scheduling mismatch' in prior work where diagnosis and scheduling were treated as separate components.

## Design Implications

### Context
#### Requirements
- Real-time cognitive diagnosis module outputting mastery probabilities and misjudgment types
- PPO-based scheduling framework with custom state space (15 features) and reward function
- Pre-experiment calibration of reward function weights
#### Constraints
- Reward weights were tuned for medical imaging course scheduling specifically

### Target Learners
- Postgraduate medical imaging students

### Target Learning Goals
- Personalized task sequencing
- Cognitive load management
- Forgetting remediation

### Affordances
- [Three Level Four Module Ai Teaching Paradigm](../designs/three-level-four-module-ai-teaching-paradigm.md)

## Claims

- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](../claims/rl-reward-misalignment-failure-modes.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- An Jie, Leng Xi, Liu Yujie, Zhou Jie, Liang Yi, Chen Yuna, Qiu Shijun (2026). Rebuilding ability acquisition in medical imaging teaching: a multi-level AI-driven teaching paradigm based on cognitive-information theory. BMC Medical Education. https://doi.org/10.1186/s12909-026-09002-3
