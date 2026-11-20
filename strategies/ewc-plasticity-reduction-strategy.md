---
type: strategy
id: ewc-plasticity-reduction-strategy
title: Reverse-engineer human-like critical period effects in language models by regularizing plasticity partway through training
description: The article proposes simulating a maturational decrease in plasticity by adding an Elastic Weight Consolidation regularizer to the loss after L1 training is complete, penalizing deviations from a prior over the parame...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: ionut-constantinescu-2024
    resource: "https://arxiv.org/abs/2407.19325"
    title: "Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2024). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. https://arxiv.org/abs/2407.19325"
    author: Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt
---

# Reverse-engineer human-like critical period effects in language models by regularizing plasticity partway through training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes simulating a maturational decrease in plasticity by adding an Elastic Weight Consolidation regularizer to the loss after L1 training is complete, penalizing deviations from a prior over the parameter space defined in terms of L1 training. This makes LMs more developmentally plausible: "we can reverse-engineer the CP by introducing a regularizer partway through training to simulate a maturational decrease in plasticity". The regularization strength λ controls the trade-off between preserving L1 and enabling L2 learning.

## Design Implications

### Context
#### Requirements
- A trained L1 checkpoint from which the Fisher Information Matrix can be estimated
- A chosen λ balancing L1 preservation against L2 learnability
#### Constraints
- The article states EWC can be viewed only as a computational-level model of an innate biological CP
- The reduction in plasticity is not progressive, but changes only once, after L1 has been fully trained

### Target Learners
- computational modelers of language acquisition

### Target Learning Goals
- simulating human-like critical period effects in artificial language learners

### Affordances
- [Strong Innate Experiential Claims Cp](../theories/language-acquisition-theory.md)

## Claims

- [Critical period effects are not a necessary consequence of successful statistical learning, refuting the strong experiential claim](../claims/refutes-strong-experiential-claim.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2024). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. https://arxiv.org/abs/2407.19325
