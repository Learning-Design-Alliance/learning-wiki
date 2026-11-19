---
type: strategy
id: three-day-ml-optics-research-project
title: Use a known physics problem with a well-known analytical solution as a testbed for a short supervised research project introducing machine learning to students without prior ML background
description: "The article describes a three-day supervised research project for final-year Bachelor's physics students with no prior machine-learning knowledge, using straight-edge Fresnel diffraction as a testbed."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: c-finot-and-s-boscolo-2022
    resource: "https://arxiv.org/abs/2201.03431"
    title: "C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. https://arxiv.org/abs/2201.03431"
    author: C Finot and S Boscolo
---

# Use a known physics problem with a well-known analytical solution as a testbed for a short supervised research project introducing machine learning to students without prior ML background

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article describes a three-day supervised research project for final-year Bachelor's physics students with no prior machine-learning knowledge, using straight-edge Fresnel diffraction as a testbed. Students generate training data from the analytical solution, train and validate networks, and tackle an inverse problem. The authors report that "The main outcome from the project was a demystification of machine learning" and that students saw implementation requires only a few lines of coding from suitable libraries.

## Design Implications

### Context
#### Requirements
- Students familiar with the underlying physics problem in lecture and tutorial classes
- Basic programming experience; the students knew Matlab using GNU Octave
#### Constraints
- The project did not optimise the techniques chosen and did not cover convolutional neural networks or deep learning
- More advanced models needed for the noisy inverse problem were beyond the short project's scope

### Target Learners
- final-year undergraduate physics students

### Target Learning Goals
- basic steps of a machine-learning process
- role of input data in predictive modelling
- limits of machine learning imposed by underlying physics

## Claims

- [Model error varies by more than two orders of magnitude with network size, small datasets induce overlearning, and training time depends quasi-linearly on dataset size](../claims/nn-dataset-size-fresnel.md) [+W]
- [Neural-network predictions agree with the analytical solution within the training domain and can extrapolate when the wavelength-distance product falls within the support of the training distribution, but fail when it does not](../claims/nn-extrapolation-lambda-z-support.md) [+W]

## Related Strategies

- [Design exercises that ask students to match or beat the performance of a published paper, and seed proposed solutions with deliberate poor choices for students to improve.](match-or-beat-published-paper-exercises.md)

## Examples
-

## Key Sources
- C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. https://arxiv.org/abs/2201.03431
