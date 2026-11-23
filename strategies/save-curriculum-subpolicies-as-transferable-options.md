---
type: strategy
id: save-curriculum-subpolicies-as-transferable-options
title: Save the sub-policies learned by an evolving curriculum policy as reusable options for transfer to tasks requiring similar options
description: "The authors identify a by-product of their evolving-policy approach: because the final task policy is composed of sub-policies learned between sub-goals, those sub-policies can be preserved and reused."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: manan-tomar-2019
    resource: "https://arxiv.org/abs/1905.07193"
    title: "Manan Tomar, Akhil Sathuluri, Balaraman Ravindran. (2019). MaMiC: Macro and Micro Curriculum for Robotic Reinforcement Learning. Proc. of the 18th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2019). https://arxiv.org/abs/1905.07193"
    author: Manan Tomar, Akhil Sathuluri, Balaraman Ravindran
---

# Save the sub-policies learned by an evolving curriculum policy as reusable options for transfer to tasks requiring similar options

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors identify a by-product of their evolving-policy approach: because the final task policy is composed of sub-policies learned between sub-goals, those sub-policies can be preserved and reused. As they state, "the sub policies can be saved as learnt options ([ 25], [2]) and then used for transfer to tasks which define a different meaning but require similar options". This makes the dual curriculum a source of transferable skills rather than only a training accelerator for a single task. The strategy is presented as a forward-looking use of the framework rather than a tested transfer result.

## Design Implications

### Context
#### Requirements
- A curriculum-trained policy whose sub-policies have been learned between discovered sub-goals, so they can be packaged as options
#### Constraints
- The paper presents this as a by-product and future direction, not as a demonstrated transfer experiment

### Target Learners
- Reinforcement learning agents trained with curriculum methods

### Target Learning Goals
- Transferring learned skills to new tasks that require similar component skills

### Affordances
- Mamic Dual Curriculum Framework

## Related Strategies

- [Use perceived task-difficulty recognition output in three ways to support Vygotsky-based task sequencing: personalised adaptive threshold, threshold correction, and misconception detection](task-difficulty-recognition-supports-task-sequencing.md)

## Examples
-

## Key Sources
- Manan Tomar, Akhil Sathuluri, Balaraman Ravindran. (2019). MaMiC: Macro and Micro Curriculum for Robotic Reinforcement Learning. Proc. of the 18th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2019). https://arxiv.org/abs/1905.07193
