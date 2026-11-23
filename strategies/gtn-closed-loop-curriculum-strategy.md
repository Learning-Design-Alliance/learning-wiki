---
type: strategy
id: gtn-closed-loop-curriculum-strategy
title: "Introduce a closed-loop curriculum in which the generator adapts generated samples to the learner's progress"
description: Among future directions, the authors propose extending GTNs with a curriculum that responds dynamically to learner performance during training.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: such-2019
    resource: "https://arxiv.org/abs/1912.07768"
    title: "Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. https://arxiv.org/abs/1912.07768"
    author: "Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J"
---

# Introduce a closed-loop curriculum in which the generator adapts generated samples to the learner's progress

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Among future directions, the authors propose extending GTNs with a curriculum that responds dynamically to learner performance during training. They suggest "a recurrent GTN that is conditioned on previous learner outputs could adapt its samples to be appropriately easier or more difﬁcult depending on an agent's learning progress, similar in spirit to the approach of a human tutor", and note such closed-loop teaching can improve learning. This is a forward-looking recommendation, not a tested result of the paper.

## Design Implications

### Context
#### Requirements
- Requires a generator (e.g. recurrent) that can condition on the learner's outputs during training
#### Constraints
- The article presents this as future work; no experiment in the paper tests closed-loop curricula

### Target Learners
- neural network learners and RL agents trained on generated data

### Target Learning Goals
- improving learning efficiency through adaptive difficulty of generated training data

### Affordances
- Generative Teaching Networks Framework

## Claims

- [A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants](../claims/gtn-full-curriculum-outperforms-other-variants.md) [+W]

## Related Strategies

- [Adaptive scenario generation: introduce training scenarios targeting weaknesses identified from real-time performance metrics](astra-adaptive-scenario-generation.md)

## Examples
-

## Key Sources
- Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. https://arxiv.org/abs/1912.07768. [doi:10.48550/arxiv.1912.07768](https://doi.org/10.48550/arxiv.1912.07768)
