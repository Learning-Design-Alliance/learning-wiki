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
> **Evidence** · 7 claims (5 for, 1 mixed, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 7 claims rest on one study

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

- [Dafm Fine Tuned Improves Prediction Over Afm](../claims/dafm-fine-tuned-improves-prediction-over-afm.md) [+M]
- [Expert Refined Qmatrix Beats Ground Up Learning](../claims/expert-refined-qmatrix-beats-ground-up-learning.md) [+M]
- [Base AFM with its expert Q-matrix generalizes better than a ground-up learned Q-matrix only on the large Cognitive Tutor Bridge datasets](../claims/afm-beats-random-init-only-on-large-cogtutor-datasets.md) [+W]
- [Qualitative inspection shows dAFM refinement remaps a Geometry problem's items toward side-identification KCs with plausible but partly spurious associations](../claims/dafm-qualitative-remapping-triangle-rectangle.md) [~W]
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](../claims/embedding-clustered-qmatrices-null-versus-dafm.md) [+W]
- [Training dAFM with individualized student ability estimates yields essentially no prediction benefit over average ability](../claims/individualized-ability-no-benefit-dafm.md) [-W]
- [Replacing the linear qk activation with ReLU sacrifices very little predictive accuracy while prohibiting negative Q-matrix values](../claims/relu-activation-preserves-dafm-accuracy.md) [+W]

## Related Theories

- [Skill discovery BKT: end-to-end stochastic learning of the problem-KC assignment matrix with Gumbel-Softmax](skill-discovery-bkt-gumbel-softmax.md)

## Examples
-

## Key Sources
- Pardos, Z. A., & Dadu, A. (2018). dAFM: Fusing Psychometric and Connectionist Modeling for Q-matrix Refinement. Journal of Educational Data Mining, Volume 10, No 2. https://github.com/CAHLR/dAFM
