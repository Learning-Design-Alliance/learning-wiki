---
type: design
id: rl-pedagogical-policy-optimization-framework
title: RL-based adaptive pedagogical policy optimization framework for narrative tutoring
description: A framework in which a reinforcement learning agent learns a decision policy that maps an eight-dimensional learner state (grade, pre-score, step, failed attempts, NLP sentiment and help scores, anxiety score) to one...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: sherry-ruan-2023
    resource: "https://arxiv.org/abs/2304.04933"
    title: "Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2023). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. https://arxiv.org/abs/2304.04933"
    author: Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill
---

# RL-based adaptive pedagogical policy optimization framework for narrative tutoring

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A framework in which a reinforcement learning agent learns a decision policy that maps an eight-dimensional learner state (grade, pre-score, step, failed attempts, NLP sentiment and help scores, anxiety score) to one of four pedagogical actions: "providing direct hints, generic encouragement, and guided prompts that scaﬀold the student", "or passive positive acknowledgment". The policy is trained with PPO against a reward combining clipped pretest-to-posttest gains, a tiny hint penalty, a small bonus for helpfulness ratings, and a quit penalty, after simulator-based pre-tuning. The article pairs the learned policy with explainable-AI attribution to inspect what differentiation the policy performs.

## Design Implications

### Context
#### Requirements
- A reward function capturing desired outcomes (learning gains, hint cost, helpfulness, non-quit)
- A feature space describing learner state, here an eight-dimensional state space
- Simulator-based pre-tuning of policy hyperparameters before real-world deployment
#### Constraints
- During online learning the policy had not converged by the end of study 1, with significant variability across 28 policy updates after 10 subjects each
- Small update batches (10 trajectories) make gradients noisy, and shifting pretest distributions across rolling recruitment complicate learning

### Target Learners
- elementary school students in grades 3-5 (roughly ages 9-12) learning mathematics

### Learning Goals
- understanding the concept of volume, including measurement and multiplication knowledge components

### Claims
- [Rl Tutor Benefits Low Pretest Students](../claims/rl-tutor-benefits-low-pretest-students.md) [+M]
- [Integrated Gradient Policy Feature Importance](../claims/integrated-gradient-policy-feature-importance.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2023). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. https://arxiv.org/abs/2304.04933
