---
type: claim
title: Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime
description: Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime
id: pretraining-improves-sample-efficiency-adaptive-sequencing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jean-vassoyan-2024
    resource: "https://doi.org/10.48550/arXiv.2411.11520"
    title: "Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). [doi:10.48550/arXiv.2411.11520](https://doi.org/10.48550/arXiv.2411.11520)"
    author: Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A recommender system pre-trained on sequential corpora transfers its knowledge to a new adaptive learning corpus and benefits from a considerable increase in sample efficiency, especially in the small data regime. [→ Jean Vassoyan 2024](#jean-vassoyan-2024)

## Evidence

### Jean Vassoyan 2024

Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). [doi:10.48550/arXiv.2411.11520](https://doi.org/10.48550/arXiv.2411.11520)

`q2 · i?` · `causal · r2`

This is the paper's central experimental claim, tested on semi-synthetic data with simulated students. The pre-trained model was compared against three baselines across three prior-knowledge scenarios, showing that "a recommender system pretrained on a set of educational corpora (source tasks) can transfer its knowledge to a brand new adaptive learning corpus (target task)".

> "Then we show experimentally that a recommender system pretrained on a set of educational corpora (source tasks) can transfer its knowledge to a brand new adaptive learning corpus (target task) and benefit from a considerable increase in sample efficiency, especially in the small data regime."

## Discussion


## Related Claims
- [Existing deep sequential knowledge tracing encoders treat concept nodes as isolated deterministic vectors, limiting handling of structural sparsity and epistemic uncertainty](kt-encoders-entity-isolated-deterministic-limits.md) — related
- [Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition](tutor-model-sample-efficiency-classroom-insufficient.md) — related
- [The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns](pretrained-model-outperforms-baselines-all-scenarios.md) — possibly the same claim (merge candidate)
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](gnn-rl-policy-beats-random-small-data.md) — related
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](wikipedia2vec-embeddings-beat-onehot-overfit.md) — related
