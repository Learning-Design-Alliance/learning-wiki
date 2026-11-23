---
type: design
id: deliverygym-weakness-diagnosis-curriculum
title: "Weakness-diagnosis adaptive curriculum: diagnosing recurring failures from executed trajectories and generating targeted training tasks"
description: "DeliveryGym's adaptive curriculum closes the learning loop by adjusting future training tasks through weakness diagnosis and targeted task generation while city layouts, simulator dynamics, and the evaluation suite re..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: haoqiang-kang-2026
    resource: "https://arxiv.org/abs/2609.19801"
    title: "Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. https://arxiv.org/abs/2609.19801"
    author: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
---

# Weakness-diagnosis adaptive curriculum: diagnosing recurring failures from executed trajectories and generating targeted training tasks

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
DeliveryGym's adaptive curriculum closes the learning loop by adjusting future training tasks through weakness diagnosis and targeted task generation while city layouts, simulator dynamics, and the evaluation suite remain fixed. "The environment diagnoses weaknesses from the current policy's on-policy trajectories on fixed training probes for traffic compliance, obstacle recovery, and multi-order planning": after every 200 training trajectories, simulator assertions score these probes and update a smoothed failure rate per skill, and larger deficits receive more targeted practice. The generator samples new task instances within predefined parameter ranges, adjusting order load, deadlines, battery levels, and traffic; 70% of training groups target skills according to the updated weakness profile and the remaining 30% use the base distribution, with a feasibility filter retaining safe, profitable tasks.

## Design Implications

### Context
#### Requirements
- Fixed training probes with simulator assertions per skill, updated after every 200 training trajectories; a task generator with predefined parameter ranges and a feasibility filter.
#### Constraints
- The distribution adapts to the policy, but city geometry and the generation rules stay fixed; evaluation tasks and held-out cities remain disjoint from training.

### Target Learners
- LLM/VLM-based embodied agents undergoing online RL

### Learning Goals
- Traffic compliance, obstacle recovery and rerouting, and multi-order delivery coordination under shared constraints

### Claims
- [Adaptive Curriculum Improves Shift Income](../claims/adaptive-curriculum-improves-shift-income.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. https://arxiv.org/abs/2609.19801
