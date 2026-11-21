---
type: claim
title: A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners
description: A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners
id: gnn-rl-policy-beats-random-small-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-11-20
recheck_by: 2026
sources:
  - id: jean-vassoyan-2023
    resource: "https://doi.org/10.48550/arXiv.2305.06398"
    title: "Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)"
    author: Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six semi-synthetic corpora, the GNN RL policy recovered a significant part of each corpus's original document order, achieving average episodic return over 10 on most corpora while the uniform random policy stayed at an expected return of 1. [→ Jean Vassoyan 2023](#jean-vassoyan-2023)

## Evidence

### Jean Vassoyan 2023

Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)

`q2 · i?` · `design · r2`

Simulation study (§5.2): the GNN policy trained with REINFORCE over 50 episodes (~50 simulated students) per corpus, returns averaged over 25 random seeds. The paper reports the agent succeeded in recovering a "significant part of the original order of each corpus", with average return over 10 versus 1 for random.

> "Most of the time, it achieved average return over 10 whereas the random policy was stuck in an expected return of 1."

## Discussion


## Related Claims
- [The GNN policy fails to recommend beyond a disconnected document node: on the disconnected Corpus 5 it stalled at the 10th document](gnn-policy-fails-disconnected-graph.md) — related
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](clustering-recovers-expert-bundles.md) — related
- [A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness](semi-supervised-deep-learning-unbiased-ability-estimates.md) — related
- [Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return](high-variance-variable-corpus-performance.md) — related
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](wikipedia2vec-embeddings-beat-onehot-overfit.md) — related
- [The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns](pretrained-model-outperforms-baselines-all-scenarios.md) — related
- [Moodle's built-in randomization is insufficient for Statistics courses, while moodlequizR provides far greater randomization](moodlequizr-randomization-exceeds-moodle-builtin.md) — related
- [Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime](pretraining-improves-sample-efficiency-adaptive-sequencing.md) — related
