---
type: strategy
id: recall-probability-item-selection-strategy
title: Optimize which items appear in each study session using recall-probability-based selection probabilities
description: "Instead of scheduling when to study, this strategy selects which questions to present in each session according to a closed-form selection probability based on each item's estimated recall probability."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: utkarsh-upadhyay-2020
    resource: "https://arxiv.org/abs/2010.04430"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2020). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. https://arxiv.org/abs/2010.04430"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez
---

# Optimize which items appear in each study session using recall-probability-based selection probabilities

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Instead of scheduling when to study, this strategy selects which questions to present in each session according to a closed-form selection probability based on each item's estimated recall probability. The article shows the "optimal selection probability is given by" p*_i(t) = 1/√q (1−m_i(t)), so harder-to-recall items are more likely to be selected, with q controlling session length. It was implemented as Algorithm 1 in the learning app's study sessions.

## Design Implications

### Context
#### Requirements
- Per-item recall probability estimates from a fitted forgetting curve model.
- A tuning parameter q ≥ 1 to keep selection probabilities within [0, 1].
#### Constraints
- The learner chooses when to study; the algorithm controls only item selection within sessions.
- A marginally higher algorithm complexity initially caused over/under flow problems in the app.

### Target Learners
- adult learners using spaced repetition study apps

### Target Learning Goals
- improved long-term retention and learner engagement

### Affordances
- [Select Optimal Item Selection Theory](../products/select-algorithm-and-open-source-trial-dataset.md)

## Claims

- [Select-optimized learners are about 50% more likely to return to the app within 4–7 days than random-group learners](../claims/select-increases-app-engagement-50-percent.md) [+W]
- [Select reduces median empirical forgetting rate 48% below random selection and 40% below difficulty-based selection, with significant differences in 75% of comparisons](../claims/select-lower-forgetting-rate-than-difficulty-and-random.md) [+W]
- [ML-optimized item selection helps learners retain content 67% longer than a difficulty-based selection heuristic after controlling for study length and frequency](../claims/select-ml-item-selection-67-percent-longer-retention.md) [+W]

## Related Strategies

- [Sequence practice items with an ML algorithm that prioritizes questions by predicted recall probability rather than fixing the rate of study](ml-item-selection-strategy.md)

## Examples
-

## Key Sources
- Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2020). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. https://arxiv.org/abs/2010.04430
