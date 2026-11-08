---
type: claim
title: EGWO-MLP shows a significant advantage in Mathematics achievement prediction over AGWO-MLP, GWO-MLP, and GA-MLP, but is worse than evolutionary algorithms in training
description: EGWO-MLP shows a significant advantage in Mathematics achievement prediction over AGWO-MLP, GWO-MLP, and GA-MLP, but is worse than evolutionary algorithms in training
id: egwo-mlp-significant-advantage-mathematics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: mixed
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

# EGWO-MLP shows a significant advantage in Mathematics achievement prediction over AGWO-MLP, GWO-MLP, and GA-MLP, but is worse than evolutionary algorithms in training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Mathematics subject achievement prediction, EGWO-MLP obtains the best results among swarm intelligence optimization algorithms but is worse than the evolutionary algorithms, and achieves the smallest standard deviation in training error rate. [→ Song Yinqiu 2022](#song-yinqiu-2022)
`q2 i?` RM ANOVA on RANKS shows EGWO-MLP is superior to AGWO-MLP, GWO-MLP, and GA-MLP models for Mathematics prediction. [→ Song Yinqiu 2022 (2)](#song-yinqiu-2022-2)

## Evidence

### Song Yinqiu 2022

Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943

`q2 · i?` · `design · r2`

Numerical simulation on the UCI Mathematics dataset (Tables 3 and 4, twenty runs) shows EGWO-MLP average training error 0.2276 versus GWO-MLP 0.2000, and EGWO-MLP "can get the smallest standard deviation (std) in the training error rate" among the compared models.

> "the EGWO-MLP model among the swarm intelligence optimization algorithms can obtain the best results. It is worse than the evolutionary algorithms. However, according to the standard deviation, EGWO-MLP can get the smallest standard deviation (std) in the training error rate."

### Song Yinqiu 2022 (2)

Song Yinqiu, Meng Xianqiu, Jiang Jianhua. (2022). Multi-Layer Perception model with Elastic Grey Wolf Optimization to predict student achievement. PLoS One. https://doi.org/10.1371/journal.pone.0276943

`q2 · i?` · `design · r2`

Statistical test results (Table 5) report significant rank-sum differences for EGWO-MLP versus AGWO-MLP (P<0.001), GWO-MLP (P=0.002), BA-MLP (P=0.038), and GA-MLP (P<0.001); comparisons versus DE-MLP and others were not significant or not tested.

> "we choose the ANOVA on the RANKS test. And the experimental results are shown in Table 5, demonstrating that EGWO-MLP is superior to AGWO-MLP, GWO-MLP, and GA-MLP models."

## Discussion


## Related Claims
- [The shrinking, resilient surrounding, and weighted candidate mechanisms accelerate convergence, avoid local stagnation, and balance exploration and exploitation](egwo-mechanisms-convergence-and-stagnation-avoidance.md) — related
- [For Portuguese achievement prediction, EGWO-MLP obtains the lowest test error and standard deviation and outperforms most compared models](egwo-mlp-lowest-test-error-portuguese.md) — related
