---
type: claim
title: Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships
description: Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships
id: wikipedia2vec-embeddings-beat-onehot-overfit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
newest_evidence: 2023
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

# Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In an ablation on all six corpora, the policy with Wikipedia2Vec keyword features outperformed the same policy with one-hot keyword encodings, yet the authors attribute the advantage to overfitting rather than to genuine use of semantic structure. [→ Jean Vassoyan 2023](#jean-vassoyan-2023)

## Evidence

### Jean Vassoyan 2023

Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)

`q2 · i?` · `design · r2`

Ablation study (§5.2, Table 2) comparing Wikipedia2Vec versus one-hot keyword features across the six corpora; e.g. Corpus 1 shows 16.48±2.66 versus 13.36±1.74. The paper states embeddings "performed signiﬁcantly better on each corpus" but suspects overﬁtting.

> "Even though the approach with embeddings performed signiﬁcantly better on each corpus, the high error margins and the similarity between trends suggest that our model was not truly able to leverage high level information"

## Discussion


## Related Claims
- [Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return](high-variance-variable-corpus-performance.md) — related
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](gnn-rl-policy-beats-random-small-data.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime](pretraining-improves-sample-efficiency-adaptive-sequencing.md) — related
- [Word2Vec analogies reveal societal stereotypes encoded in training data, such as completing 'man : surgeon :: woman : ?' with 'nurse'](word2vec-analogy-gender-bias.md) — related
