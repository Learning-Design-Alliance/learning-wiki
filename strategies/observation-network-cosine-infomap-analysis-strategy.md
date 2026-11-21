---
type: strategy
id: observation-network-cosine-infomap-analysis-strategy
title: Use classroom observation networks with cosine similarity, LANS sparsification, and Infomap clustering to characterize instructional practices
description: "The article's analysis pipeline represents each instructor's COPUS-coded observations as a directed, weighted network of transitions between instructor activities, then quantifies pairwise similarity."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: meagan-sundstrom-2025
    resource: "https://arxiv.org/abs/2510.01124"
    title: "Meagan Sundstrom, Justin Gambrell, Colin Green, Adrienne L. Traxler, and Eric Brewe. (2025). Beyond named methods: A typology of active learning based on classroom observation networks. https://arxiv.org/abs/2510.01124"
    author: Meagan Sundstrom, Justin Gambrell, Colin Green, Adrienne L. Traxler, and Eric Brewe
---

# Use classroom observation networks with cosine similarity, LANS sparsification, and Infomap clustering to characterize instructional practices

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (3 associational), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The article's analysis pipeline represents each instructor's COPUS-coded observations as a directed, weighted network of transitions between instructor activities, then quantifies pairwise similarity. As printed, the authors "quantify the extent to which instructors' observation networks are similar using cosine similarity," sparsify the similarity network with the locally adaptive network sparsification algorithm at alpha = 0.05, and apply Infomap community detection to identify instruction types. This captures the temporal and interactional nature of instruction that descriptive statistics obscure, and scales to many observations while allowing direct comparisons.

## Design Implications

### Context
#### Requirements
- Video or real-time observations coded with a structured, standardized protocol (the COPUS) providing codes at regular time intervals; transitions defined as a code newly appearing in the following two-minute interval
#### Constraints
- Instructor codes only; three rare instructor codes observed in less than 2% of intervals were excluded; cosine similarity was preferred over the Jaccard index because the Jaccard index was suppressed to low values for almost every pair

### Target Learners
- college science instructors

### Target Learning Goals
- characterizing and comparing instructional practices across classrooms

### Affordances
- Active Learning Instruction Typology Observation Networks

## Claims

- [Distinct COPUS codes characterize each active learning profile: lecture and clickers for the lecture-like profile, student presentations and whole-class discussion for Modeling Instruction, predictions for CRP labs, and group worksheets for recitations](../claims/copus-codes-distinguish-active-learning-profiles.md) [+W]
- [Student COPUS profiles looked nearly the same for Tutorials, ISLE recitations, and Context-Rich Problems discussion sections, suggesting the need for a more detailed observation instrument](../claims/calep-copus-profiles-indistinguishable-need-detail.md) [+W]
- [MAMCR fails to replicate for large FCI samples: Infomap with LANS sparsification consistently identified only one large community of incorrect answers](../claims/mamcr-fails-large-fci-samples.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Meagan Sundstrom, Justin Gambrell, Colin Green, Adrienne L. Traxler, and Eric Brewe. (2025). Beyond named methods: A typology of active learning based on classroom observation networks. https://arxiv.org/abs/2510.01124
