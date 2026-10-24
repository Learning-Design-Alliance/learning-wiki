---
type: claim
title: Time-series forecasting with TabPFN-TS markedly improves prediction of next-episode emotions and perceived proficiency over a static model (e.g., anxiety R² 0.458→0.866; boredom 0.596→0.953)
description: Time-series forecasting with TabPFN-TS markedly improves prediction of next-episode emotions and perceived proficiency over a static model (e.g., anxiety R² 0.458→0.866; boredom 0.596→0.953)
id: tabpfn-ts-forecasting-l2-emotions-high-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: peng-wang-2026
    resource: "https://doi.org/10.1007/s10648-026-10141-8"
    title: "Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8"
    author: Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: peng-wang-2026-2
    resource: "https://doi.org/10.1007/s10648-026-10141-8"
    title: "Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8"
    author: Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Time-series forecasting with TabPFN-TS markedly improves prediction of next-episode emotions and perceived proficiency over a static model (e.g., anxiety R² 0.458→0.866; boredom 0.596→0.953)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training TabPFN-TS on each learner's first 85 episodes and forecasting the final 20 raised within-dataset R² from the static model: anxiety 0.458→0.866, boredom 0.596→0.953, self-perceived proficiency 0.515→0.832, enjoyment 0.651→0.934. [→ Peng Wang 2026](#peng-wang-2026)
`q2 i?` Against an individual-mean baseline, TabPFN-TS achieved skill scores of 0.740–0.782 and MAE of 0.26–0.32 on the 0–10 scale across the four targets. [→ Peng Wang 2026 (2)](#peng-wang-2026-2)

## Evidence

### Peng Wang 2026

Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8

`q2 · i?` · `associational · r2`

Time-aware TabPFN-TS forecasting using recent history and dynamic emotional profiles, trained on the first 85 episodes per learner; the article notes R² is used only for within-dataset comparison.

> "Relative to a static model, out-of-sample fit improved markedly, with R² increasing as a within-dataset comparator: anxiety: 0.458→0.866; boredom: 0.596→0.953; self-perceived proficiency: 0.515→0.832; enjoyment: 0.651→0.934."

### Peng Wang 2026 (2)

Peng Wang, Lesya Ganushchak, Camille Welie, Roel van Steensel. (2026). Emotions Are Not Random: Machine Learning Reveals Predictable Patterns in a 21-Day Second Language Learning Trajectory. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10141-8

`q2 · i?` · `associational · r1`

Benchmark of the sequence model against an individual-mean baseline; the article states the MAE of 0.26 to 0.32 is small relative to the 0–10 scale, indicating good short-horizon accuracy within this dataset.

> "The model consistently achieved high relative skill scores and low errors across all measured states—anxiety (0.771/0.319/0.765), boredom (0.782/0.283/0.689), enjoyment (0.772/0.277/0.674), and self-perceived proficiency (0.740/0.263/0.635), reported as skill score/MAE/RMSE."

## Discussion


## Related Claims
- [Adult L2 learners' momentary emotions cluster into five profiles, dominated by a low-arousal 'Routine but Pleasant' state (57.8% of episodes), challenging anxiety-centred paradigms](five-emotional-profiles-l2-routine-but-pleasant-dominant.md) — related
- [In static concurrent prediction, TabPFN outperformed Random Forest, XGBoost and Linear Regression across the four emotional and proficiency targets](tabpfn-outperforms-baselines-static-concurrent-prediction.md) — related
- [During the course, curiosity, enjoyment, confusion and anxiety decreased over time, boredom increased, and surprise and frustration remained stationary.](time-trends-epistemic-emotions-decline-course.md) — related
