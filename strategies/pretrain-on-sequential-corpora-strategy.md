---
type: strategy
id: pretrain-on-sequential-corpora-strategy
title: Pre-train an adaptive sequencing recommender on sequential course corpora before fine-tuning on a new adaptive learning corpus
description: The article recommends gathering a set of closely related sequential corpora and pre-training a recommender system on them before fine-tuning on a target adaptive learning task.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: jean-vassoyan-2024
    resource: "https://arxiv.org/abs/2411.11520"
    title: "Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). https://arxiv.org/abs/2411.11520"
    author: Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis
---

# Pre-train an adaptive sequencing recommender on sequential course corpora before fine-tuning on a new adaptive learning corpus

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The article recommends gathering a set of closely related sequential corpora and pre-training a recommender system on them before fine-tuning on a target adaptive learning task. This pre-training "does not involve any annotator to tag documents nor real students to interact with them, but requires a flexible enough recommender system". The two-stage pre-training first uses supervised learning to match an oracle's predictions, then applies REINFORCE to learn to make useful mistakes that provide information about student knowledge.

## Design Implications

### Context
#### Requirements
- A set of closely related sequential corpora as source tasks
- A flexible enough recommender system (e.g., GNN-based)
#### Constraints
- The method has been tested only on semi-synthetic data with simulated students

### Target Learners
- MOOC learners
- adaptive learning platform users

### Target Learning Goals
- improved sample efficiency in learning path personalization

## Claims

- [The pre-trained model generalized to unseen prior-knowledge distributions not encountered during pre-training](../claims/pretrained-model-generalizes-unseen-populations.md) [+W]
- [The pre-trained model showed relatively low variance despite using REINFORCE, which typically suffers from high variance](../claims/pretrained-model-low-variance-reinforce.md) [+W]
- [The pre-trained model maintained its lead throughout training and converged well above non-pre-trained counterparts](../claims/pretrained-model-maintains-lead-throughout-training.md) [+W]
- [The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns](../claims/pretrained-model-outperforms-baselines-all-scenarios.md) [+W]
- [Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime](../claims/pretraining-improves-sample-efficiency-adaptive-sequencing.md) [+W]
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](../claims/gnn-rl-policy-beats-random-small-data.md) [+W]
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](../claims/wikipedia2vec-embeddings-beat-onehot-overfit.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). https://arxiv.org/abs/2411.11520
