---
type: strategy
id: collapsed-gibbs-sampling-writing-process-hmm
title: Use collapsed Gibbs sampling for parameter estimation in the time- and learner-dependent HMM
description: "The article proposes \"a collapsed Gibbs sampling algorithm as the parameter estimation method for the proposed model.\" This strategy implements Bayesian parameter estimation for the extended Gaussian HMM so that seque..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: uto-2020
    resource: "https://doi.org/10.1007/s40593-019-00189-9"
    title: "Uto, M., Miyazawa, Y., Kato, Y., Nakajima, K., & Kuwata, H. (2020). Time- and Learner-Dependent Hidden Markov Model for Writing Process Analysis Using Keystroke Log Data. Int J Artif Intell Educ, 30, 271–298. https://doi.org/10.1007/s40593-019-00189-9"
    author: "Uto, M., Miyazawa, Y., Kato, Y., Nakajima, K., & Kuwata, H"
---

# Use collapsed Gibbs sampling for parameter estimation in the time- and learner-dependent HMM

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes "a collapsed Gibbs sampling algorithm as the parameter estimation method for the proposed model." This strategy implements Bayesian parameter estimation for the extended Gaussian HMM so that sequence patterns of writing subtasks can be inferred from keystroke logs at scale.

## Design Implications

### Context
#### Requirements
- Markov chain Monte Carlo machinery for Bayesian inference on the proposed model
#### Constraints
- 

### Target Learners
- researchers and system developers analyzing writing processes

### Target Learning Goals
- estimating writing-process sequence patterns

## Claims

- [The proposed model's effectiveness was demonstrated by applying it to actual keystroke log datasets](../claims/tdlhmm-effectiveness-demonstrated-keystroke-datasets.md) [+W]

## Related Strategies

- [Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM](fit-a-fix-one-parameter-alternative-to-dirichlet-priors.md)

## Examples
-

## Key Sources
- Uto, M., Miyazawa, Y., Kato, Y., Nakajima, K., & Kuwata, H. (2020). Time- and Learner-Dependent Hidden Markov Model for Writing Process Analysis Using Keystroke Log Data. Int J Artif Intell Educ, 30, 271–298. https://doi.org/10.1007/s40593-019-00189-9
