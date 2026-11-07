---
type: claim
title: For Portuguese achievement prediction, EGWO-MLP obtains the lowest test error and standard deviation and outperforms most compared models
description: For Portuguese achievement prediction, EGWO-MLP obtains the lowest test error and standard deviation and outperforms most compared models
id: egwo-mlp-lowest-test-error-portuguese
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: song-yinqiu-2022
    resource: "https://doi.org/10.1371/journal.pone.0276943"
    title: "Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943"
    author: Song Yinqiu, Meng Xianqiu, Jiang Jianhua
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: song-yinqiu-2022-2
    resource: "https://doi.org/10.1371/journal.pone.0276943"
    title: "Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943"
    author: Song Yinqiu, Meng Xianqiu, Jiang Jianhua
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# For Portuguese achievement prediction, EGWO-MLP obtains the lowest test error and standard deviation and outperforms most compared models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` During Portuguese testing, EGWO-MLP obtains the lowest test error and standard deviation compared with the other algorithms-MLP models. [→ Song Yinqiu 2022](#song-yinqiu-2022)
`q2 i?` RM ANOVA on RANKS shows EGWO-MLP outperforms most of the compared models for Portuguese prediction. [→ Song Yinqiu 2022 (2)](#song-yinqiu-2022-2)

## Evidence

### Song Yinqiu 2022

Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943

`q2 · i?` · `design · r2`

Numerical simulation on the UCI Portuguese dataset (Tables 6 and 7, twenty runs) reports EGWO-MLP average test error 0.9751 with STD 0.5703, lower than all compared models, e.g. AGWO-MLP 7.1346 and DE-MLP 11.7115.

> "During the testing process, it is difficult for the compared models to achieve stable model optimization, and EGWO-MLP can obtain the lowest test error and standard deviation."

### Song Yinqiu 2022 (2)

Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943

`q2 · i?` · `design · r2`

Statistical tests (Table 8) show significant differences versus AGWO-MLP (P=0.003), GWO-MLP (P<0.001), DE-MLP (P=0.024), and GA-MLP (P=0.018); comparisons versus BA-MLP were not significant and versus PSO-MLP and SCA-MLP were not tested.

> "The experimental results show that its EGWO-MLP can outperform most of the compared models and has strong stability."

## Discussion


## Related Claims
- [The shrinking, resilient surrounding, and weighted candidate mechanisms accelerate convergence, avoid local stagnation, and balance exploration and exploitation](egwo-mechanisms-convergence-and-stagnation-avoidance.md) — related
- [EGWO-MLP shows a significant advantage in Mathematics achievement prediction over AGWO-MLP, GWO-MLP, and GA-MLP, but is worse than evolutionary algorithms in training](egwo-mlp-significant-advantage-mathematics.md) — related
