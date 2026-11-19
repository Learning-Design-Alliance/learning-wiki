---
type: design
id: six-linear-corpora-benchmark
title: Six semi-synthetic linear corpora built from real e-learning platform courses with hand-tagged keywords
description: "The evaluation environment consists of six 'linear' corpora: regular courses divided so each subsection is one document, designed to be followed in a single pre-defined order, leaving practically no room for personali..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: jean-vassoyan-2023
    resource: "https://arxiv.org/abs/2305.06398"
    title: "Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2305.06398"
    author: Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger
---

# Six semi-synthetic linear corpora built from real e-learning platform courses with hand-tagged keywords

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The evaluation environment consists of six 'linear' corpora: regular courses divided so each subsection is one document, designed to be followed in a single pre-defined order, leaving practically no room for personalization. "Six corpora were constructed this way: three about data science (1-3) and three about programming (4-6)" from a popular e-learning platform. Keywords were tagged by hand to avoid noise, and Table 1 reports document, keyword, edge and diameter statistics; Corpus 5 is disconnected.

## Design Implications

### Context
#### Requirements
- Simulated learners that return feedback f◦ only when documents are recommended in the corpus's original order
#### Constraints
- Linear structure means the experiment assesses structure recovery, not personalization or generalization capability

### Target Learners
- Simulated learners modeling students of data science and programming courses

### Learning Goals
- Sequencing resources in a corpus's intended prerequisite order

### Claims
- [Gnn Rl Policy Beats Random Small Data](../claims/gnn-rl-policy-beats-random-small-data.md) [+M]
- [Gnn Policy Fails Disconnected Graph](../claims/gnn-policy-fails-disconnected-graph.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2305.06398
