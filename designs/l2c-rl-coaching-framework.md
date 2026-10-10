---
type: design
id: l2c-rl-coaching-framework
title: "Learning to Coach (L2C): an RL pipeline combining adaptive blending, a skill-change PFA, and a surrogate reward"
description: "L2C is the article's trainable coaching framework built on the Coaching Game formalism."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: wei-wang-2026
    resource: "https://arxiv.org/abs/2606.25337"
    title: "Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337"
    author: Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam
---

# Learning to Coach (L2C): an RL pipeline combining adaptive blending, a skill-change PFA, and a surrogate reward

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
L2C is the article's trainable coaching framework built on the Coaching Game formalism. Its contributions are "threefold: (i) a closed-loop blending rule that adapts the assistance levelλto the coach's observations of both the physical environment and the learner behavior; (ii) a reformu-lation of theCoaching Gameto a single-agent POMDP, solvable via RL, through a probabilistic model of the coach's causal influence on learner skill; and (iii) a tractable surrogate reward that is provably consistent with the counterfactual V oI objective." A hybrid probabilistic finite-state automaton models skill change on success and failure events with sigmoid rates over skill; the coach policy is trained with PPO against skill improvement and deployed with Bayesian runtime skill inference and multimodal feedback.

## Design Implications

### Context
#### Requirements
- A pretrained expert policy to anchor the blending rule
- A learner model expressible as a skill-parameterized policy class
- Privileged access to learner skill during simulation training
#### Constraints
- The Boltzmann learner model is one tractable choice; the article states accurately modeling skill-conditioned learner behaviors remains an open problem
- Verbal and visual cues are predefined and triggered by fixed rules; only assistance modulation of physical control is learned

### Target Learners
- human learners practicing motor skills such as FPV drone racing, mostly novices

### Learning Goals
- accelerated development of independent motor-skill competence, measured by unassisted lap time and failure count

### Claims
- [L2C Within Subject Lap Time Failure Gains](../claims/l2c-within-subject-lap-time-failure-gains.md) [+M]
- [L2C Outperforms Rbf Mia Baselines](../claims/l2c-outperforms-rbf-mia-baselines.md) [+M]
- [L2C Adaptive Assistance By Skill And Context](../claims/l2c-adaptive-assistance-by-skill-and-context.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam. (2026). AI Coaching for Accelerating Human Skill Development with Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2606.25337
