---
type: claim
title: "The GNN policy fails to recommend beyond a disconnected document node: on the disconnected Corpus 5 it stalled at the 10th document"
description: "The GNN policy fails to recommend beyond a disconnected document node: on the disconnected Corpus 5 it stalled at the 10th document"
id: gnn-policy-fails-disconnected-graph
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
    kind: design
    rigour: 2
---

# The GNN policy fails to recommend beyond a disconnected document node: on the disconnected Corpus 5 it stalled at the 10th document

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Corpus 5, the only disconnected corpus, the policy's episodic return fell below 10, indicating it failed to make recommendations beyond the 10th document because the disconnected node receives no message-passing information. [→ Jean Vassoyan 2023](#jean-vassoyan-2023)

## Evidence

### Jean Vassoyan 2023

Jean Vassoyan, Jill-Jênn Vie, Pirmin Lemberger. (2023). Towards Scalable Adaptive Learning with Graph Neural Networks and Reinforcement Learning. arXiv preprint. [doi:10.48550/arXiv.2305.06398](https://doi.org/10.48550/arXiv.2305.06398)

`q2 · i?` · `design · r2`

Simulation result (§5.2) on Corpus 5, whose graph is disconnected. The paper explains that "since this document is disconnected from the rest of the graph, it does not beneﬁt from message-passing" and receives no feedback information from other documents.

> "it was disconnected at the 11 th document, which is consistent with the performance of the model: indeed, episodic return lower than 10 indicates that it failed to make recommendations beyond the 10 th document."

## Discussion


## Related Claims
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](gnn-rl-policy-beats-random-small-data.md) — related
