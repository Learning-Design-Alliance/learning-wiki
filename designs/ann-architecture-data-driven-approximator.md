---
type: design
id: ann-architecture-data-driven-approximator
title: Artificial neural network architecture as a data-driven approximator for experimental physics data
description: The article presents the ANN as a layered computational model inspired by the human brain, consisting of input, hidden, and output layers of interconnected nodes.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: saralasrita-mohanty-2026
    resource: "https://arxiv.org/abs/2503.23506"
    title: "Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2026). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. https://arxiv.org/abs/2503.23506"
    author: Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty
---

# Artificial neural network architecture as a data-driven approximator for experimental physics data

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article presents the ANN as a layered computational model inspired by the human brain, consisting of input, hidden, and output layers of interconnected nodes. Inputs are scaled with weights and combined with biases, and an activation function transforms the weighted sum: "y=ϕ(Σw ixi +b)". In the compound pendulum application, three experimentally measured parameters (angular displacement, effective length, time period) feed a single hidden layer of nine tanh neurons with a linear output neuron, trained via the Levenberg–Marquardt algorithm on min-max normalized data split 70/15/15 into training, validation, and test sets.

## Design Implications

### Context
#### Requirements
- Training data of sufficient quality, quantity, and variability
- Suitable choice of hidden-layer size and activation functions
- Basic knowledge of Python and TensorFlow to construct and train the model
#### Constraints
- A conventional ANN does not explicitly incorporate governing physical laws and may produce predictions that are mathematically accurate but not necessarily physically interpretable
- Performance depends strongly on the quality, quantity, and variability of the training data
- Without controlled complexity the ANN may overfit experimental noise

### Target Learners
- second/third-year undergraduate physics and engineering students

### Learning Goals
- regression, training, validation, overfitting, generalization, and data-driven analysis of experimental data

### Claims
- Ann Predicts G Matching Experimental Compound Pendulum [+M]
- [Hidden Node Count Ann Overfitting Underfitting](../claims/hidden-node-count-ann-overfitting-underfitting.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2026). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. https://arxiv.org/abs/2503.23506
