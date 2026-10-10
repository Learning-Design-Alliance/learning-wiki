---
type: claim
title: Ablations show every feature group contributes to skills forecasting, while recent engagement activity alone nearly suffices for minutes
description: Ablations show every feature group contributes to skills forecasting, while recent engagement activity alone nearly suffices for minutes
id: ablation-feature-groups-engagement-forecasting
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# Ablations show every feature group contributes to skills forecasting, while recent engagement activity alone nearly suffices for minutes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Removing any single feature group yields small MAE losses; for skills, dropping engagement activity causes the largest loss (>1%) and other groups 0.6-0.8% each, while for minutes all removals cause losses under 1%. [→ Eric S. Qiu 2026](#eric-s-qiu-2026)

## Evidence

### Eric S. Qiu 2026

Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers. (2026). From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning. https://arxiv.org/abs/2605.12788

`q2 · i?` · `associational · r2`

Ablation study (Table 5) retraining models with each feature group removed and comparing MAE to the full model with bootstrap significance tests; the article reports that for skills "every group contributes" with engagement activity removal the largest loss.

> "Forskills, every group contributes: dropping engagement activity features yields the largest loss (>1%), but AFM, gaps, and prior achievement features also provide meaningful differences (0.6–0.8% each)."

## Discussion


## Related Claims
- [Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered](ml-outperforms-heuristics-week-ahead-engagement-forecasting.md) — related
- [Effort forecasting is driven by recent engagement activity while progress forecasting depends more on learner-centered signals such as ability, difficulty, and consistency](effort-vs-progress-distinct-feature-drivers.md) — related
