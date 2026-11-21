---
type: research-method
id: sequential-versus-graph-corpus-partitioning-framework-for-transfer-learning-in-adaptive-ed
title: Sequential-versus-graph corpus partitioning framework for transfer learning in adaptive educational recommendation
description: The article sets up a mathematical framework modeling a student population interacting with a distribution of educational corpora as a collection of POMDPs.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Sequential-versus-graph corpus partitioning framework for transfer learning in adaptive educational recommendation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article sets up a mathematical framework modeling a student population interacting with a distribution of educational corpora as a collection of POMDPs. It partitions the domain into "sequential corpora", which are "designed to be fully completed, following an identical path for each student", and "graph corpora", which "can be browsed in multiple ways" and are "much more suited for adaptive learning". Sequential corpora serve as source tasks for pre-training because they represent massive amounts of data and allow bypassing extensive expert tagging, while graph corpora are the target tasks for the recommendation engine.

## Accounts
<!-- How each source describes or uses the method -->
- **A mathematical framework partitioning educational corpora into sequential (source) and graph (target) tasks for transfer learning in adaptive learning**: The article sets up a mathematical framework modeling a student population interacting with a distribution of educational corpora as a collection of POMDPs. It partitions the domain into "sequential corpora", which are "designed to be fully completed, following an identical path for each student", and "graph corpora", which "can be browsed in multiple ways" and are "much more suited for adaptive learning". Sequential corpora serve as source tasks for pre-training because they represent massive amounts of data and allow bypassing extensive expert tagging, while graph corpora are the target tasks for the recommendation engine. (Jean Vassoyan et al. (2024))

### Claims

- [Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime](../claims/pretraining-improves-sample-efficiency-adaptive-sequencing.md) [+M]
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](../claims/gnn-rl-policy-beats-random-small-data.md) [+W]
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](../claims/wikipedia2vec-embeddings-beat-onehot-overfit.md) [+W]
- [Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return](../claims/high-variance-variable-corpus-performance.md) [+W]

## Related Research Methods
-

## Key Sources
- Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). https://arxiv.org/abs/2411.11520
