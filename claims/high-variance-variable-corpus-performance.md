---
type: claim
title: Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return
description: Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return
id: high-variance-variable-corpus-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: jean-vassoyan-2023
    resource: "https://doi.org/10.48550/arXiv.2305.06398"
    title: "Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)"
    author: Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Policy performance varies strongly across corpora and shows extremely high variance, with only Corpus 2 reliably reaching the maximum achievable return

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Best performance was achieved on Corpus 2, the only corpus where the model reached the maximum achievable return most of the time, while episodic return variance was extremely high on almost all other corpora. [→ Jean Vassoyan 2023](#jean-vassoyan-2023)
`q2 i?` Corpus size and graph diameter alone do not account for performance variability: corpora 3 and 6 have similar document counts but very different results, and corpora 2 and 6 share equal diameter yet differ widely in normalized return. [→ Jean Vassoyan 2023](#jean-vassoyan-2023)

## Evidence

### Jean Vassoyan 2023

Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)

`q2 · i?` · `causal · r1`

Results discussion (§5.2) over 25 averaged seeds. The paper adds that "one cannot ignore the extremely high variance of the episodic return for almost all corpora (except for Corpus 2)", partly attributed to REINFORCE's instability, and that document count alone does not explain variability.

> "Best performance was achieved on Corpus 2. Indeed, it is the only one for which our model managed to reach the maximum achievable return most of the time."

## Discussion


## Related Claims
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](gnn-rl-policy-beats-random-small-data.md) — related
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — a broader claim this one bears on
- [Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection](llm-detection-variability-across-corpus.md) — related
- [Wikipedia2Vec keyword embeddings yield higher episodic returns than one-hot keyword encodings, but the model appears to overfit each corpus rather than leverage entity relationships](wikipedia2vec-embeddings-beat-onehot-overfit.md) — related
