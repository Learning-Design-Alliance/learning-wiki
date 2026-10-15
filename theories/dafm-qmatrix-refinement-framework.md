---
type: theory
title: "dAFM: a neural-network fusion of psychometric and connectionist modeling enabling backpropagation-based Q-matrix refinement"
description: "dAFM augments the Additive Factors Model, whose \"calculations and constraints we show can be exactly replicated within the framework of neural networks\", by representing the Q-matrix as a weight coefficient matrix (WQ..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: pardos-2018
    resource: "https://github.com/CAHLR/dAFM"
    title: "Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM"
    author: "Pardos, Z. A., & Dadu, A"
---

# dAFM: a neural-network fusion of psychometric and connectionist modeling enabling backpropagation-based Q-matrix refinement

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
dAFM augments the Additive Factors Model, whose "calculations and constraints we show can be exactly replicated within the framework of neural networks", by representing the Q-matrix as a weight coefficient matrix (WQk) adjustable by backpropagation and by computing student KC opportunity counts dynamically with an identity-weight RNN counter as the Q-matrix changes. The model retains AFM's logistic formulation predicting correctness from student ability, KC difficulties, and KC growth rates multiplied by opportunity counts. It was evaluated in six variants on five Cognitive Tutor and ASSISTments datasets, comparing refinement of an expert Q-matrix against learning one from scratch.

## Design Implications

### Context
#### Requirements
- Requires item-level response sequences with timestamps so the RNN counter can accumulate KC opportunity counts, and an initial Q-matrix (expert or random) to initialize WQk
- Requires choosing an activation function for the qk layer; the article uses linear or ReLU since sigmoid suffered convergence problems
#### Constraints
- Does not support expansion of the number of KCs, though contraction is possible if all items become unmapped from a KC
- Never observes correctness of a response in its input, only as an output label, unlike BKT, PFA, and DKT
- Refinements ought to be validated by other means in addition to predictive generalization before valid inference conditions are understood

### Target Learners
- middle and high school mathematics students using Cognitive Tutor and ASSISTments tutoring systems

### Target Learning Objectives
- accurate prediction of student first-attempt correctness
- refined item-to-knowledge-component associations for adaptive mastery-based instruction

### Claims


## Related Theories

- [Skill discovery BKT: end-to-end stochastic learning of the problem-KC assignment matrix with Gumbel-Softmax](skill-discovery-bkt-gumbel-softmax.md)

## Examples
-

## Key Sources
- Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM
