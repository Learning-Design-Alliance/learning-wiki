---
type: theory
title: "Skill discovery BKT: end-to-end stochastic learning of the problem-KC assignment matrix with Gumbel-Softmax"
description: "This model estimates the binary problem-to-KC assignment matrix within a neural network framework by sampling each problem's KC assignment from a categorical distribution and backpropagating through samples using the..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: khajah-2024
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1"
    title: "Khajah, M. M. (2024). Supercharging BKT with Multidimensional Generalizable IRT and Skill Discovery. Journal of Educational Data Mining, Volume 16, No 1, 2024. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1"
    author: Khajah, M. M
---

# Skill discovery BKT: end-to-end stochastic learning of the problem-KC assignment matrix with Gumbel-Softmax

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This model estimates the binary problem-to-KC assignment matrix within a neural network framework by sampling each problem's KC assignment from a categorical distribution and backpropagating through samples using the Gumbel-Softmax re-parameterization trick, with a modified multi-KC BKT RNN cell whose state holds knowledge probabilities for all KCs. Problem input features can guide membership via a learnable membership function, and an auxiliary loss rewards assignments producing blocked KC sequences. The article calls this "a mechanism to estimate this discrete assignment matrix within an NN framework, which is a feat that, to our knowledge, has not been accomplished before."

## Design Implications

### Context
#### Requirements
- The whole model must be differentiable with respect to the sampled assignment matrix; soft assignments are used during training while sampled assignments are quantized to binary during evaluation
#### Constraints
- Each problem is assumed to map to only one underlying KC

### Target Learners
- students in intelligent tutoring systems

### Target Learning Objectives
- discovering knowledge component structure underlying practice data to improve performance prediction

### Claims
- [Skill Discovery Partially Recovers True Kc Assignments](../claims/skill-discovery-partially-recovers-true-kc-assignments.md) [+M]
- [Skill Discovery Matches Expert Skills Fewer Kcs](../claims/skill-discovery-matches-expert-skills-fewer-kcs.md) [+M]

## Related Theories

- [OptimNN: neural-network parameter generation (hypernetwork) for optimizing BKT](optimnn-hypernetwork-parameter-generation.md)
- [dAFM: a neural-network fusion of psychometric and connectionist modeling enabling backpropagation-based Q-matrix refinement](dafm-qmatrix-refinement-framework.md)

## Examples
-

## Key Sources
- Khajah, M. M. (2024). Supercharging BKT with Multidimensional Generalizable IRT and Skill Discovery. Journal of Educational Data Mining, Volume 16, No 1, 2024. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1
