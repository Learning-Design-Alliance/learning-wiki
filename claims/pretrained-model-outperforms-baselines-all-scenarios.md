---
type: claim
title: The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns
description: The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns
id: pretrained-model-outperforms-baselines-all-scenarios
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
    rigour: 1
---

# The pre-trained model outperformed all baselines in all three prior-knowledge scenarios on final episodic returns

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The pre-trained model outperformed all other approaches in all scenarios, with the gap most pronounced at the beginning of training. [→ Jean Vassoyan 2024](#jean-vassoyan-2024)

## Evidence

### Jean Vassoyan 2024

Jean Vassoyan, Anan Schütt, Jill-Jênn Vie, Arun-Balajiee Lekshmi-Narayanan, Elisabeth André, Nicolas Vayatis. (2024). A Pre-Trained Graph-Based Model for Adaptive Sequencing of Educational Documents. NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment (FM-Assess). [doi:10.48550/arXiv.2411.11520](https://doi.org/10.48550/arXiv.2411.11520)

`q2 · i?` · `causal · r1`

Comparison of four recommendation engines (ours, Vassoyan et al., CMAB, Bassen et al.) across three prior-knowledge scenarios. Final episodic returns in Table 1 show the pre-trained model achieving the highest scores in each scenario (e.g., 24.81 vs 18.63, 18.34, 8.02 in the 'None' scenario).

> "The first observation that can be made from these plots is that our pre-trained model outperformed all other approaches in all scenarios. As expected, the performance gap was most pronounced at the beginning of the training sessions, where our model benefited from a strong warm start."

## Discussion


## Related Claims
- [The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7](ppo-outperforms-random-baseline-reward.md) — related
- [A GNN-based RL recommender learns to recover corpus structure and substantially outperforms a uniform random policy in the small-data regime on simulated learners](gnn-rl-policy-beats-random-small-data.md) — related
- [Pre-training a recommender system on sequential corpora improves sample efficiency for adaptive learning path personalization in the small data regime](pretraining-improves-sample-efficiency-adaptive-sequencing.md) — possibly the same claim (merge candidate)
- [Adding pretrained auxiliary KCs to a PPO-based recommendation policy consistently improves simulated student learning outcomes](aux-kcs-improve-ppo-recommendation.md) — related
