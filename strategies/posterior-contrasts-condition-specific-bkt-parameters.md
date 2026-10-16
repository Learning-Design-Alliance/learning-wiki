---
type: strategy
id: posterior-contrasts-condition-specific-bkt-parameters
title: Use posterior credible intervals on condition-specific BKT parameter contrasts to compare experimental conditions
description: "The article demonstrates a concrete analysis recipe for educational experiments: fit a Multi BKT model with MCMC, compute marginal parameter estimates by averaging posterior draws over the levels of the complementary..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: siddhartha-pradhan-2026
    resource: "https://arxiv.org/abs/2605.23048"
    title: "Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales. (2026). StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing. https://arxiv.org/abs/2605.23048"
    author: Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales
---

# Use posterior credible intervals on condition-specific BKT parameter contrasts to compare experimental conditions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article demonstrates a concrete analysis recipe for educational experiments: fit a Multi BKT model with MCMC, compute marginal parameter estimates by averaging posterior draws over the levels of the complementary factor, define each congruency effect as the difference between a condition's marginal estimate and its neutral baseline, and summarize each contrast with the mean and 95% credible interval. "Credible intervals that excluded zero were interpreted as evidence that the associated perceptual cue was related with a systematic change in the corresponding BKT parameter relative to the neutral condition."

## Design Implications

### Context
#### Requirements
- Requires posterior draws (e.g., MCMC) rather than EM point estimates, since point estimates are inadequate for comparing parameters across conditions, particularly when some conditions contain relatively few observations
#### Constraints
- 

### Target Learners
- experimental study participants, e.g., sixth-grade students solving order-of-operations problems

### Target Learning Goals
- quantifying how instructional manipulations affect latent learning, forgetting, guessing, and slipping processes

### Affordances
- [Bayesian Bkt Formulation Uncertainty](../theories/bayesian-knowledge-tracing-two-state-model.md)

## Related Strategies

- [Initialize BKT parameters from simulated student data when no human data is available](initialize-bkt-parameters-from-simulated-data.md)

## Examples
-

## Key Sources
- Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales. (2026). StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing. https://arxiv.org/abs/2605.23048
