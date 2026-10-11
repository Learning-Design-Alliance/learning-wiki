---
type: design
id: subject-aware-prompt-routing-framework
title: Subject-aware adaptive prompt routing framework for LLM tutoring
description: "The article formalizes adaptive prompt selection as a contextual bandit routing problem: the router observes a pedagogical input fusing a topic embedding with a learnable subject embedding, and selects a tutoring prom..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: po-chin-chang-2026
    resource: "https://arxiv.org/abs/2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
---

# Subject-aware adaptive prompt routing framework for LLM tutoring

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article formalizes adaptive prompt selection as a contextual bandit routing problem: the router observes a pedagogical input fusing a topic embedding with a learnable subject embedding, and selects a tutoring prompt from a pool of 20 pedagogical prompts. Feedback comes from an LLM evaluator that decomposes instructional efficacy into 14 observable criteria grounded in educational theory, weighted by correlation with human labels. The authors state they "formulate adaptive tutoring as aprompt routingproblem, using topic and subject information as input."

## Design Implications

### Context
#### Requirements
- A pool of expert-verified pedagogical prompts
- An LLM evaluator score calibrated against human-labeled learning outcomes
- A simulation environment for safe pre-training before live deployment
#### Constraints
- Relies on a discrete prompt pool, preventing novel or hybrid instruction strategies
- Real-world data sparsity slows online convergence and limits statistical power
- Router develops bias toward strategies that perform well across the most common subjects

### Target Learners
- Dutch high-school students

### Learning Goals
- Subject-specific tutoring across 13 high-school subjects
- Transition to formal practice exercises

### Claims
- [Prompt Router Beats Static Baselines Simulation](../claims/prompt-router-beats-static-baselines-simulation.md) [+M]
- [Router Subject Strategy Alignment Simulation](../claims/router-subject-strategy-alignment-simulation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138
