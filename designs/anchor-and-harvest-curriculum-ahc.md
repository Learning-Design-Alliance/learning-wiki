---
type: design
id: anchor-and-harvest-curriculum-ahc
title: "Anchor-and-Harvest Curriculum (AHC): a rule-based, non-LLM curriculum system for Craftax-Full"
description: "AHC is a domain-informed, rule-based training system for Craftax-Full that, as the abstract states, \"combines achievement-oriented tasks, harvested initial-state progress, difficulty adaptation, bounded selection, and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: zhu-2026
    resource: "https://arxiv.org/abs/2610.15328"
    title: "Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. https://arxiv.org/abs/2610.15328"
    author: Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi
---

# Anchor-and-Harvest Curriculum (AHC): a rule-based, non-LLM curriculum system for Craftax-Full

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
AHC is a domain-informed, rule-based training system for Craftax-Full that, as the abstract states, "combines achievement-oriented tasks, harvested initial-state progress, difficulty adaptation, bounded selection, and original-task practice." It enumerates achievement, family, and depth units from Craftax's fixed achievement set, harvests five-part progress signatures from session-ending training states, assembles practice start states by combining those signatures with procedurally generated floor-indexed worlds, anneals a difficulty parameter toward native dynamics, and always appends an original-task anchor using ordinary resets. It performs no LLM inference and keeps all 43 actions available during training and evaluation.

## Design Implications

### Context
#### Requirements
- Requires engine knowledge of recipes, floors, and achievement dependencies in the form of a hand-specified prerequisite graph, plus harvested training progress and modified training dynamics
#### Constraints
- The article states AHC relies on domain-specific task rules and that transfer to other environments is untested; its native evaluation does not make training conditions identical to native PPO

### Target Learners
- PPO-GTrXL reinforcement-learning agents in Craftax-Symbolic-v1

### Learning Goals
- Acquiring the 67 Craftax achievements, including deep-floor entry and combat skills, under a fixed rollout budget

### Claims
- [Ahc Beats Native Ppo Craftax](../claims/ahc-beats-native-ppo-craftax.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhu, Jiayu; Li, Luyuan; Shi, Yuyuan; Dong, Hanyi. (2026). Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax. https://arxiv.org/abs/2610.15328. [doi:10.48550/arxiv.2610.15328](https://doi.org/10.48550/arxiv.2610.15328)
