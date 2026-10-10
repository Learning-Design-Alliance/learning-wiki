---
type: claim
title: "Percentile heuristics transferred from health behavior systematically overpredict weekly K-12 engagement and underperform XGBoost by 20-30%"
description: "Percentile heuristics transferred from health behavior systematically overpredict weekly K-12 engagement and underperform XGBoost by 20-30%"
id: percentile-heuristics-overpredict-weekly-engagement
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
  - id: eric-s-qiu-2026-2
    resource: "https://arxiv.org/abs/2605.12788"
    title: "Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788"
    author: Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Percentile heuristics transferred from health behavior systematically overpredict weekly K-12 engagement and underperform XGBoost by 20-30%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Adams-style P60 and P70 percentile predictors perform 4-33% worse than P50 across targets because their continuous-improvement assumption fails once growth slows. [→ Eric S. Qiu 2026](#eric-s-qiu-2026)
`q2 i?` XGBoost reduces MAE by 20-30% relative to Adams-P50, though it is weaker in the earliest weeks and underpredicts the skills target. [→ Eric S. Qiu 2026 (2)](#eric-s-qiu-2026-2)

## Evidence

### Eric S. Qiu 2026

Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788

`q2 · i?` · `associational · r2`

Weekly trend comparison of Adams percentile heuristics against ground-truth trajectories on the 30% student holdout (Fig. 2, Table 4); the article reports that Adams predictors "systematically overshoot" because engagement stabilizes or declines rather than continuously improving.

> "As a result, Adams predictors systematically overshoot: P60 and P70 in particular perform 4–33% worse than P50 across targets, and averaging across percentiles further degrades accuracy."

### Eric S. Qiu 2026 (2)

Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788

`q2 · i?` · `associational · r2`

Holdout comparison of the chosen XGBoost model against the three Adams variants (Table 4), showing "XGBoost reduces MAE by 20–30% relative to Adams-P50"; the article notes early-week weakness and systematic skills underprediction until trajectories stabilize around week 9.

> "XGBoost reduces MAE by 20–30% relative to Adams-P50, and by larger margins relative to Adams-P60 and P70 (Table 4)."

## Discussion


## Related Claims
- [Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered](ml-outperforms-heuristics-week-ahead-engagement-forecasting.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
