---
type: strategy
id: harness-annealing-training-recipe
title: "Harness Annealing Training recipe: explicit control supervision combined with a stronger-to-weaker harness curriculum, supplemented by stronger-source replay and cue dropout"
description: HAT converts teacher trajectories into decision-level records (OBS, THINK, ACT) in which targeted control judgments become supervised model outputs, then progressively introduces demonstrations collected under weaker...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: yingxuan-yang-2026
    resource: "https://arxiv.org/abs/2610.01235"
    title: "Yingxuan Yang, Huacan Chai, Ying Wen. (2026). Harness Annealing: Learning to Act with Less External Control. https://arxiv.org/abs/2610.01235"
    author: Yingxuan Yang, Huacan Chai, Ying Wen
---

# Harness Annealing Training recipe: explicit control supervision combined with a stronger-to-weaker harness curriculum, supplemented by stronger-source replay and cue dropout

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
HAT converts teacher trajectories into decision-level records (OBS, THINK, ACT) in which targeted control judgments become supervised model outputs, then progressively introduces demonstrations collected under weaker harnesses: starting from a Layered H4-trained checkpoint, stages introduce H3-, H2-, and H1-source records, with each stage's mixture combining "current-source records, stronger-source replay, and cue-dropout variants where applicable". The ordering "lets each stage build on its predecessor rather than requiring the initial model to learn all control responsibilities from tools-only demonstrations". Source labels survive rewriting and cue dropout, and every checkpoint is evaluated under all four deployment harnesses.

## Design Implications

### Context
#### Requirements
- A fixed bank of teacher trajectories collected under each source harness level (e.g., GPT-5.5 trajectories under all four source harnesses)
- Decision-level record construction (Layered supervision) that turns targeted control responsibilities into model outputs while retaining observed evidence as input
#### Constraints
- Later checkpoints receive more training and use different data mixtures; without equal-budget controls, observed differences cannot be attributed to the annealing order alone, nor can the contributions of replay and cue dropout be separated
- The curriculum does not assume that source records and deployment contexts are identical

### Target Learners
- Language-model agents being fine-tuned for multi-step tool-use tasks

### Target Learning Goals
- Internalizing runtime control decisions (verification, workflow, state) so they can be performed with less external support

### Affordances
- Harness Internalization Objective

## Claims


## Related Strategies
- 

## Examples
-

## Key Sources
- Yingxuan Yang, Huacan Chai, Ying Wen. (2026). Harness Annealing: Learning to Act with Less External Control. https://arxiv.org/abs/2610.01235
