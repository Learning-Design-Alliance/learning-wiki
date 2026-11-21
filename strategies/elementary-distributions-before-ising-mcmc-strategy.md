---
type: strategy
id: elementary-distributions-before-ising-mcmc-strategy
title: Introduce MCMC with elementary distributions and repeated random-walk design practice before advanced models like the Ising model
description: This teaching strategy replaces the common practice of posting students directly with the Ising model or classical particle systems.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: wenlong-wang-2022
    resource: "https://arxiv.org/abs/2204.10145"
    title: "Wenlong Wang. (2022). An effective introduction to the Markov Chain Monte Carlo method. arXiv preprint. https://arxiv.org/abs/2204.10145"
    author: Wenlong Wang
---

# Introduce MCMC with elementary distributions and repeated random-walk design practice before advanced models like the Ising model

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
This teaching strategy replaces the common practice of posting students directly with the Ising model or classical particle systems. Instead, students first design random walk rules for two- and three-state systems, compute acceptance probabilities from detailed balance, and practise with "a good number of examples" including the underlying stochastic matrices. The author argues the usual fast-paced approach risks that "a student may not be able to fully digest the principles of the MCMC method", and that the stochastic matrix is sometimes entirely omitted. The simple setting also dissolves the tricky concept that a rejected state counts again in the chain.

## Design Implications

### Context
#### Requirements
- Instructor presents the two-state population dynamics first, then three-state design exercises, before generalizing to many states
#### Constraints
- Intended for students studying MCMC for the first time; students with suitable background may move faster to advanced topics

### Target Learners
- senior undergraduate physics students encountering MCMC for the first time

### Target Learning Goals
- design valid MCMC random walk rules
- understand proposal and acceptance probabilities
- understand the underlying stochastic matrix

### Affordances
- [Population Dynamics Mcmc Teaching Framework](../designs/population-dynamics-mcmc-teaching-framework.md)

## Related Strategies

- [Teach data analysis methods through simplified implementations of advanced algorithms such as Metropolis-Hastings](simplified-algorithm-implementations-teaching-strategy.md)

## Examples
-

## Key Sources
- Wenlong Wang. (2022). An effective introduction to the Markov Chain Monte Carlo method. arXiv preprint. https://arxiv.org/abs/2204.10145
