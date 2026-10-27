---
type: design
id: gold-mining-hidden-agent-rl-task
title: Three-territory gold-mining reinforcement learning task with hidden agents
description: A developmental adaptation of the Dorfman et al.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: alexandra-o-cohen-2020
    resource: "https://doi.org/10.1038/s41539-020-00075-3"
    title: "Alexandra O. Cohen, Kate Nussenbaum, Hayley M. Dorfman, Samuel J. Gershman and Catherine A. Hartley. (2020). The rational use of causal inference to guide reinforcement learning strengthens with age. npj Science of Learning 5:16. https://doi.org/10.1038/s41539-020-00075-3"
    author: Alexandra O. Cohen, Kate Nussenbaum, Hayley M. Dorfman, Samuel J. Gershman and Catherine A. Hartley
---

# Three-territory gold-mining reinforcement learning task with hidden agents

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A developmental adaptation of the Dorfman et al. task in which participants choose between two mines with fixed reward probabilities (80% vs 20% gold) across three 50-trial blocks. Each block occurs in a territory visited by a hidden agent that intervenes on 30% of trials: a Millionaire who adds gold, a Robber who replaces gold with rocks, or a Sheriff who intervenes randomly. After each outcome participants report whether the agent caused it. The task measures learning via optimal choice and causal attribution via forced judgments, supporting computational model comparison across ages.

## Design Implications

### Context
#### Requirements
- Participants must understand task instructions; piloting indicated age 7 was the youngest age at which children reliably understood the instructions, and experimenter corrections occurred only during practice trials.
#### Constraints
- The exact intervention probability (30%) was not told to participants; intervention was invisible and ambiguous on each trial.

### Target Learners
- children ages 7-12
- adolescents ages 13-17
- adults ages 18-25

### Learning Goals
- reinforcement learning from positive and negative feedback
- causal attribution of outcomes to external agents

### Claims
- [Attribution Alignment Hidden Agent Structure](../claims/attribution-alignment-hidden-agent-structure.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Alexandra O. Cohen, Kate Nussenbaum, Hayley M. Dorfman, Samuel J. Gershman and Catherine A. Hartley. (2020). The rational use of causal inference to guide reinforcement learning strengthens with age. npj Science of Learning 5:16. https://doi.org/10.1038/s41539-020-00075-3
