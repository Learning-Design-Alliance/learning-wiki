---
type: design
id: bidirectional-distillation-active-learning-framework
title: Bidirectional knowledge-distillation framework imitating human active learning
description: "A machine training framework in which two small student models are trained on data and then exchange knowledge bidirectionally via knowledge distillation, implemented as mean squared error loss between the two models'..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: jaeseo-lim-2020
    resource: "https://arxiv.org/abs/2011.03733"
    title: "Jaeseo Lim, Hwiyeol Jo, Byoung-Tak Zhang, Jooyong Park. (2020). Human-Like Active Learning: Machines Simulating the Human Learning Process. 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada. https://arxiv.org/abs/2011.03733"
    author: Jaeseo Lim, Hwiyeol Jo, Byoung-Tak Zhang, Jooyong Park
---

# Bidirectional knowledge-distillation framework imitating human active learning

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A machine training framework in which two small student models are trained on data and then exchange knowledge bidirectionally via knowledge distillation, implemented as mean squared error loss between the two models' prediction scores. The article explains that "in order to implement discussion, we simply made the knowledge transfer (distillation) in bidirectional ways," imitating students using their knowledge interactively, while constraining training capacity to mirror the limited learning time of the human active condition. It was evaluated against a passive teacher-to-student distillation framework on five text-classification datasets.

## Design Implications

### Context
#### Requirements
- A teacher model with larger capacity for the passive condition; two smaller student models for the active condition; Adam optimization with shared hyperparameters
#### Constraints
- Evaluated only on text classification tasks; the article notes Experiment 1 is open-ended QA but basic tasks were used for simplicity

### Target Learners
- machine learning systems simulating novice human learners

### Learning Goals
- improved classification performance through human-like active knowledge exchange

### Claims
- Machine Active Distillation Beats Passive [+M]
- Passive Distillation Par With Conventional [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jaeseo Lim, Hwiyeol Jo, Byoung-Tak Zhang, Jooyong Park. (2020). Human-Like Active Learning: Machines Simulating the Human Learning Process. 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada. https://arxiv.org/abs/2011.03733
