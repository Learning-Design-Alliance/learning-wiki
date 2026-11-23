---
type: design
id: gc-agents-bayesian-goal-inference-framework
title: Goal-conditioned teacher-learner agents with Bayesian Goal Inference for pedagogy and pragmatism
description: The article introduces a novel family of goal-conditioned agents (GC-agents) that can act both as teachers and learners, leveraging action with demonstrations and language with instructions as two communication modali...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: hugo-caselles-dupré-2023
    resource: "https://arxiv.org/abs/2308.10842"
    title: "Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani. (2023). Show and Tell: Enhancing Agent Communication and Learning through Action and Language. arXiv. https://arxiv.org/abs/2308.10842"
    author: Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani
---

# Goal-conditioned teacher-learner agents with Bayesian Goal Inference for pedagogy and pragmatism

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article introduces a novel family of goal-conditioned agents (GC-agents) that can act both as teachers and learners, leveraging action with demonstrations and language with instructions as two communication modalities. The communication process works as follows: the teacher delivers a teaching signal (demonstration or instruction), and the learner, "employing Bayesian Goal Inference, attempts to predict the underlying goal associated with the teaching signal", retrying until it infers the goal. Demonstrations are added to the learner's replay buffer; instructions provide a curriculum of subgoals; the learner then pursues the predicted goal and updates its policy with reinforcement learning. Introducing goals is what enables pedagogy from the teacher side and pragmatism from the learner side.

## Design Implications

### Context
#### Requirements
- Agents must be goal-conditioned, able to address a variety of goals
- The learner must be able to infer goals from teaching signals via Bayesian Goal Inference
- Policy updates via reinforcement learning techniques
#### Constraints
- Evaluated in the Fetch Block Stacking environment (stacking three cubes in configurations including pyramids and stacks)

### Target Learners
- reinforcement learning agents (robotic learners)

### Learning Goals
- learning to stack cubes in goal configurations; effective communication and teaching between agents

### Claims
- [Pedagogy Pragmatism Increase Gc Agent Efficiency](../claims/pedagogy-pragmatism-increase-gc-agent-efficiency.md) [+M]
- [Mixing Demonstrations Instructions Superior](../claims/mixing-demonstrations-instructions-superior.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani. (2023). Show and Tell: Enhancing Agent Communication and Learning through Action and Language. arXiv. https://arxiv.org/abs/2308.10842
