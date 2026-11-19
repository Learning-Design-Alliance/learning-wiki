---
type: design
id: nn-supervised-learning-workflow-fresnel
title: Supervised neural-network learning workflow for diffraction-pattern prediction
description: "The article describes the supervised learning pipeline the students followed: generating an ensemble of intensity profiles sampled in 150 values along the spatial dimension, using wavelength and distance as inputs and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: c-finot-and-s-boscolo-2022
    resource: "https://arxiv.org/abs/2203.06034"
    title: "C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. https://arxiv.org/abs/2203.06034"
    author: C Finot and S Boscolo
---

# Supervised neural-network learning workflow for diffraction-pattern prediction

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes the supervised learning pipeline the students followed: generating an ensemble of intensity profiles sampled in 150 values along the spatial dimension, using wavelength and distance as inputs and the discretised pattern as output, normalising "the input and output variables" typically to [-1,1], training by backpropagation with mean squared error, and testing on a held-out validation set. "Typically, we used 80% of the database for training and the remaining 20% for testing." Bayesian backpropagation and regularisation appeared robust in Matlab; Levenberg-Marquardt gave the most suitable results in Octave.

## Design Implications

### Context
#### Requirements
- A sufficiently large set of training data
- Normalisation of input and output variables prior to training
- A validation dataset to flag problems like overfitting
#### Constraints
- In Octave, normalisation must be explicitly programmed, whereas in Matlab it can be transparent to the user

### Target Learners
- undergraduate physics students

### Learning Goals
- understanding the supervised machine-learning process
- cross-validation and generalisation
- backpropagation training

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. https://arxiv.org/abs/2203.06034
