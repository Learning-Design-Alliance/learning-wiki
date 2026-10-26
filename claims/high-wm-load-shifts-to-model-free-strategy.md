---
type: claim
title: High WM load shifts learners from model-based toward model-free reinforcement learning strategies
description: High WM load shifts learners from model-based toward model-free reinforcement learning strategies
id: high-wm-load-shifts-to-model-free-strategy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: chengyan-yang-2025
    resource: "https://doi.org/10.1038/s41539-025-00363-w"
    title: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w"
    author: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu"
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: chengyan-yang-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00363-w"
    title: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w"
    author: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# High WM load shifts learners from model-based toward model-free reinforcement learning strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` The mixing weight, representing the degree of model-based control, was significantly reduced under high WM load (d = 0.98). [→ Chengyan Yang 2025](#chengyan-yang-2025)
`q3 i?` GLMMs corroborated this: under low load previous rewards affected stay probability without state-similarity interactions (model-based pattern), whereas under high load a significant reward × state-similarity interaction emerged (model-free pattern). [→ Chengyan Yang 2025 (2)](#chengyan-yang-2025-2)

## Evidence

### Chengyan Yang 2025

Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w

`q3 · i3` · `causal · r2`

Paired t-tests on dual-system RL model parameters from 50 participants. The article reports the mixing weight "was also signiﬁcantly reduced in the high WM load condition", with t(49) = 6.95, d = 0.98, and a Wilcoxon test r = 0.79.

> "the mixing weight, which represented the degree of model-based control, was also signiﬁcantly reduced in the high WM load condition compared to that observed in the low WM load condition (t(49) = 6.95, p < 0.001, d = 0.98; W = 1140, p < 0.001, r = 0.79)"

### Chengyan Yang 2025 (2)

Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w

`q3 · i?` · `causal · r2`

Separate GLMMs on trial-level stay probabilities for each WM load condition. Under high load the optimal model showed a significant prevrew × same interaction (β = 0.357, p < 0.001), a model-free signature; under low load previous rewards had a significant positive effect (β = 1.330, p < 0.001) with no significant interaction.

> "The optimal model indi- cated signi ﬁcant main effects for both previous rewards ( β = 0.572, p < 0.001) and state similarity ( β = 0.844, p < 0.001), along with a sig- niﬁcant interaction effect between them (β = 0.357, p < 0.001), indicating that the in ﬂuence of previous reward was ampli ﬁed when participants encountered identical states"

## Discussion


## Related Claims
- [Exploitation (inverse temperature) and information utilization (learning rate) correlate with reward acquisition under both WM loads](inverse-temperature-learning-rate-correlate-reward.md) — related
- [Model-based strategy use and intelligence positively predict RL learning performance, while WM load negatively predicts it](mixing-weight-intelligence-predict-rl-performance.md) — related
- [Model-based strategy use partially mediates the effect of WM load on RL learning performance](model-based-strategy-mediation-wm-load-performance.md) — related
- [Participants earned higher corrected reward rates under low WM load than high WM load in a two-stage RL task](low-wm-load-higher-corrected-reward-rate.md) — related
- [Intelligence correlates with RL performance under low WM load but not under high WM load](intelligence-performance-correlation-varies-by-wm-load.md) — related
