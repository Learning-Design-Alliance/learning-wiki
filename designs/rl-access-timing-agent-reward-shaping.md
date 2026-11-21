---
type: design
id: rl-access-timing-agent-reward-shaping
title: RL-based access-timing agent with pedagogically shaped reward (PPO over BKT-simulated students)
description: "The article's central framework models the question of when to grant GenAI access as a Markov decision process solved with reinforcement learning."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: janne-rotter-2026
    resource: "https://arxiv.org/abs/2605.15850"
    title: "Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo. (2026). Access Timing as Scaffolding: A Reinforcement Learning Approach to GenAI in Education. https://arxiv.org/abs/2605.15850"
    author: Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo
---

# RL-based access-timing agent with pedagogically shaped reward (PPO over BKT-simulated students)

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article's central framework models the question of when to grant GenAI access as a Markov decision process solved with reinforcement learning. "The RL agent utilizes Proximal Policy Optimization (PPO) [82] to learn a policy that determines when students should be allowed to use GenAI during the learn-ing task." States include failed attempts, time on task, prior GenAI use, and current understanding; actions are allowing or denying usage. The reward is a sum of components grounded in learning goals, efficiency, metacognition, productive failure, and cognitive load, and the agent is trained on Bayesian Knowledge Tracing simulations of student behaviour.

## Design Implications

### Context
#### Requirements
- Simulated student models (BKT with KT-IDEM and retake extension) parameterized from a pilot study to train the policy before deployment
- A strictly linear task structure so the agent can assume sequential task completion for training
#### Constraints
- Findings reveal PPO outperformed DQN and A2C only in the given context
- Reward components are conceptually explained, with the complete formal definition deferred to the appendix

### Target Learners
- higher education students

### Learning Goals
- text comprehension
- metacognitive engagement
- balanced GenAI use

### Claims
- [Rl Timed Genai Access Beats Always Allow Posttest](../claims/rl-timed-genai-access-beats-always-allow-posttest.md) [+M]
- [Rl Timed Access Metacognitive Accuracy Vs Always](../claims/rl-timed-access-metacognitive-accuracy-vs-always.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo. (2026). Access Timing as Scaffolding: A Reinforcement Learning Approach to GenAI in Education. https://arxiv.org/abs/2605.15850
