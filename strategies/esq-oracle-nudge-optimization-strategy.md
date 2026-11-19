---
type: strategy
id: esq-oracle-nudge-optimization-strategy
title: Use ESQ as an oracle to recommend nudges by optimizing state changes for a desired score improvement
description: "The article recommends treating the fitted ESQ model as an Oracle that returns the reward function for a given student state, then solving an inverse problem: minimize a loss over the anticipated state change δx neede..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: chintan-donda-sayan-dasgupta-soma-s-dhavala-keyur-faldu-aditi-avasthi-2020
    resource: "https://arxiv.org/abs/2010.02629"
    title: "Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi. (2020). A FRAMEWORK FOR PREDICTING, INTERPRETING, AND IMPROVING LEARNING OUTCOMES. arXiv preprint. https://arxiv.org/abs/2010.02629"
    author: Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi
---

# Use ESQ as an oracle to recommend nudges by optimizing state changes for a desired score improvement

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends treating the fitted ESQ model as an Oracle that returns the reward function for a given student state, then solving an inverse problem: minimize a loss over the anticipated state change δx needed to achieve a desired score improvement δy. Because this resembles coordinate descent, one feature is varied at a time to find perturbations that improve the current score; in Fig. 9 the article shows affected features which improve the current score by more than 10 points. Nudges reach learners through messaging (e.g. feedback about careless mistakes) or a gaming mode where learners play with simulated actions and pick a suitable one. The authors state the formalism can easily be incorporated into a Reinforcement Learning paradigm.

## Design Implications

### Context
#### Requirements
- A trained ESQ prediction model acting as the Oracle/reward function
- Feature attributions that identify actionable features
- A delivery channel such as platform messaging to reach learners
#### Constraints
- The nudges model can figure out what the state should be but does not influence the state directly; influence happens via messaging or gaming mode
- The article notes the causal link between an action and an affecting feature must be established for direct influence

### Target Learners
- Learners on an online learning platform preparing for tests

### Target Learning Goals
- Improving test scores (as a proxy for learning outcomes) through targeted behavioral nudges

### Affordances
- [Network Of Models Esq Framework](../research-methods/network-of-models-architecture-for-learning-outcome-prediction-with-esq-as-an-oracle.md)

## Related Strategies

- [Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)](zpd-masked-rl-content-sequencing.md)
- [Align AI learning-support communication and nudges with empirically observed usage windows and adapt support to learner groups](align-ai-support-nudges-observed-usage-windows.md)

## Examples
-

## Key Sources
- Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi. (2020). A FRAMEWORK FOR PREDICTING, INTERPRETING, AND IMPROVING LEARNING OUTCOMES. arXiv preprint. https://arxiv.org/abs/2010.02629
