---
type: claim
title: Model-based strategy use partially mediates the effect of WM load on RL learning performance
description: Model-based strategy use partially mediates the effect of WM load on RL learning performance
id: model-based-strategy-mediation-wm-load-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: chengyan-yang-2025
    resource: "https://doi.org/10.1038/s41539-025-00363-w"
    title: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w"
    author: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: chengyan-yang-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00363-w"
    title: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w"
    author: "Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Model-based strategy use partially mediates the effect of WM load on RL learning performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`–`q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Bootstrapped mediation showed WM load negatively predicted mixing weight (path a = −0.232), which positively predicted reward rate (path b = 0.090); the indirect effect (ACME = −0.021) accounted for 24% of the total effect, with the direct effect remaining significant. [→ Chengyan Yang 2025](#chengyan-yang-2025)
`q2 i?` A Monte Carlo simulation with 1000 replications estimated the mediation analysis had 96.4% statistical power to detect the ACME at the study's sample size. [→ Chengyan Yang 2025 (2)](#chengyan-yang-2025-2)

## Evidence

### Chengyan Yang 2025

Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w

`q3 · i?` · `causal · r2`

Exploratory mediation analysis (1000 bootstrap samples) testing whether mixing weight mediated the WM load effect on corrected reward rate. The direct effect (ADE = −0.066) remained significant, indicating partial mediation; total effect = −0.087.

> "WM load negatively predicted mixing weight (path a= −0.232, p < 0.001), which in turn positively predicted reward rate (path b = 0.090, p < 0.001). The indirect effect (ACME =−0.021, 95% CI [−0.037, −0.008], p = 0.002) accounted for 24% of the total effect (Proportion Mediated)"

### Chengyan Yang 2025 (2)

Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w

`q2 · i?` · `causal · r2`

Monte Carlo simulation with 1000 replications using the observed path coefficients and N = 100 (50 per condition) to estimate power for the mediation test. The article cautions the mediation results should be interpreted with caution given the relatively small sample size.

> "The results demonstrated that the current media- tion analysis achieved a statistical power of 96.4% (α = 0.05) for detecting the ACME, given the speci ﬁed model parameters and sample size."

## Discussion


## Related Claims
- [High WM load shifts learners from model-based toward model-free reinforcement learning strategies](high-wm-load-shifts-to-model-free-strategy.md) — related
- [Intelligence correlates with RL performance under low WM load but not under high WM load](intelligence-performance-correlation-varies-by-wm-load.md) — related
- [Participants earned higher corrected reward rates under low WM load than high WM load in a two-stage RL task](low-wm-load-higher-corrected-reward-rate.md) — related
- [Model-based strategy use and intelligence positively predict RL learning performance, while WM load negatively predicts it](mixing-weight-intelligence-predict-rl-performance.md) — related
