---
type: design
id: population-dynamics-mcmc-teaching-framework
title: "Population-dynamics progression framework for introducing MCMC: two states, three states, then many discrete and continuous states"
description: This framework teaches Markov Chain Monte Carlo through an analogy between population flow between cities and the random walk of a single walker in a state space.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: wenlong-wang-2022
    resource: "https://arxiv.org/abs/2204.10145"
    title: "Wenlong Wang. (2022). An effective introduction to the Markov Chain Monte Carlo method. arXiv preprint. https://arxiv.org/abs/2204.10145"
    author: Wenlong Wang
---

# Population-dynamics progression framework for introducing MCMC: two states, three states, then many discrete and continuous states

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
This framework teaches Markov Chain Monte Carlo through an analogy between population flow between cities and the random walk of a single walker in a state space. It progresses from a two-state Bernoulli example, to three states introducing ergodicity and balance conditions, to the geometric and Gaussian distributions, covering "all the essential concepts of Markov Chain Monte Carlo without loss of generality". The author reports that "most senior undergraduate students in physics can closely follow these materials without much diﬃculty". The framework deliberately avoids technical overhead of standard examples such as the Ising model.

## Design Implications

### Context
#### Requirements
- Readers already familiar with simple sampling of uniform distributions, random numbers, distribution transformations, and the central limit theorem for iid data
#### Constraints
- Aimed at first-time MCMC learners in physics and related fields; students with suitable background may be introduced to Ising-model-style treatments instead

### Target Learners
- senior undergraduate students in physics
- undergraduate students in mathematics and chemistry

### Learning Goals
- understand the principles of the Markov Chain Monte Carlo method
- design random walk rules satisfying ergodicity and balance conditions
- analyze correlated MCMC data

### Claims
- Two State Population Dynamics Equilibrium Sampling [+M]
- Balance Condition Yields Metropolis Heat Bath [+M]
- Ergodicity Balance Guarantee Convergence [+M]
- Correlated Mcmc Data Effective Sample Size [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Wenlong Wang. (2022). An effective introduction to the Markov Chain Monte Carlo method. arXiv preprint. https://arxiv.org/abs/2204.10145
