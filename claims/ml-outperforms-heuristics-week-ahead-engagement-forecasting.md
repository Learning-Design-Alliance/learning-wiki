---
type: claim
title: "Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered"
description: "Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered"
id: ml-outperforms-heuristics-week-ahead-engagement-forecasting
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: eric-s-qiu-2026
    resource: "https://arxiv.org/abs/2605.12788"
    title: "Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788"
    author: Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Supervised feature-based models substantially outperform heuristic baselines on week-ahead engagement forecasting, reducing error by 22% for minutes and 33% for skills. [→ Eric S. Qiu 2026](#eric-s-qiu-2026)

## Evidence

### Eric S. Qiu 2026

Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788

`q2 · i?` · `associational · r2`

Benchmark of fifteen predictors (regressions, decision trees, neural networks) on ITS logs from 425 middle-school students, with student-level splits; the article reports that on average, error falls by "22%for minutes and33%for skills" relative to baselines, with bootstrap CIs excluding zero.

> "On average, error falls by22%for minutes and33%for skills."

## Discussion


## Related Claims
- [Ablations show every feature group contributes to skills forecasting, while recent engagement activity alone nearly suffices for minutes](ablation-feature-groups-engagement-forecasting.md) — related
- [Effort forecasting is driven by recent engagement activity while progress forecasting depends more on learner-centered signals such as ability, difficulty, and consistency](effort-vs-progress-distinct-feature-drivers.md) — related
- [Percentile heuristics transferred from health behavior systematically overpredict weekly K-12 engagement and underperform XGBoost by 20-30%](percentile-heuristics-overpredict-weekly-engagement.md) — related
