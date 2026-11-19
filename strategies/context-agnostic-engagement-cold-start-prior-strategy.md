---
type: strategy
id: context-agnostic-engagement-cold-start-prior-strategy
title: Use a context-agnostic engagement prediction model as a cold-start prior within an educational recommender system
description: "The article recommends deploying the context-agnostic engagement model inside an educational recommender system: \"It can act as a prior that mitigates cold-start problem both on user and content fronts.\" When new cont..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: sahan-bulathwela-2020
    resource: "https://arxiv.org/abs/2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. https://arxiv.org/abs/2006.00592"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
---

# Use a context-agnostic engagement prediction model as a cold-start prior within an educational recommender system

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 associational, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article recommends deploying the context-agnostic engagement model inside an educational recommender system: "It can act as a prior that mitigates cold-start problem both on user and content fronts." When new content is discovered frequently, the model "estimates how engaging materials are prior to exposing them to the learner population," balancing learner-satisfaction risk against fresh material. It can also complement topic-focused personalisation by accounting for stylistic and lingual features beyond topic coverage.

## Design Implications

### Context
#### Requirements
- A trained context-agnostic engagement model using easily automatable cross-modal features
- View-log or engagement signals from an OER platform to train the model
#### Constraints
- The model is trained on English lectures and English translations, which the authors state impacts generalisation ability
- Findings may not be directly applicable to other types of educational material or general purpose videos

### Target Learners
- online learners of open educational resources

### Target Learning Goals
- recommending engaging educational materials before personal data is available

## Claims

- [A common subject-agnostic engagement model can be assumed across knowledge areas, since subject-specific training does not improve accuracy](../claims/common-engagement-model-across-knowledge-areas.md) [+W]
- [The population-based engagement model outperforms per-learner personalised models when individual training data is limited (around 60 events)](../claims/population-model-better-in-cold-start.md) [+W]
- [Modeling knowledge transfer within and across domains alleviates the cold-start problem on unseen concepts](../claims/knowledge-transfer-alleviates-cold-start-kt.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. https://arxiv.org/abs/2006.00592
