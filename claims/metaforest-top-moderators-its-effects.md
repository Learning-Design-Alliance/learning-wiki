---
type: claim
title: MetaForest identifies worked-out examples, intervention duration, intervention condition, learning outcome type, and immediate measurement as the most important moderators
description: MetaForest identifies worked-out examples, intervention duration, intervention condition, learning outcome type, and immediate measurement as the most important moderators
id: metaforest-top-moderators-its-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: walter-l-leite-2025
    resource: "https://arxiv.org/abs/2511.04997"
    title: "Walter L. Leite, Huibin Zhang, Shibani Rana, Yide Hao, Amber D. Hatch, Lingchen Kong, Huan Kuang. (2025). Do intelligent tutoring systems benefit K-12 students? A meta-analysis and evaluation of heterogeneity of treatment effects in the U.S. https://arxiv.org/abs/2511.04997"
    author: Walter L. Leite, Huibin Zhang, Shibani Rana, Yide Hao, Amber D. Hatch, Lingchen Kong, Huan Kuang
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# MetaForest identifies worked-out examples, intervention duration, intervention condition, learning outcome type, and immediate measurement as the most important moderators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Permutation importance ranked the worked-out example indicator first, followed by math ITS, intervention duration, intervention condition, and immediate measurement. [→ Walter L. Leite 2025](#walter-l-leite-2025)

## Evidence

### Walter L. Leite 2025

Walter L. Leite, Huibin Zhang, Shibani Rana, Yide Hao, Amber D. Hatch, Lingchen Kong, Huan Kuang. (2025). Do intelligent tutoring systems benefit K-12 students? A meta-analysis and evaluation of heterogeneity of treatment effects in the U.S. https://arxiv.org/abs/2511.04997

`q2 · i?` · `quant-synthesis · r2`

MetaForest random-forest analysis of all U, T, O, and S moderators, fit 10 times with different seeds; each iteration converged with approximately 10,000 trees. Median out-of-bag R² was 0.09 and median cross-validated R² was 0.25; the ranking was stable across runs.

> "Based on permutation importance, the indicator of the ITS providing worked-out examples was ranked 1st as the most influential moderator. The dummy indicator of math ITS, intervention duration, intervention condition, and immediate measurement were ranked 2nd, 3rd, 4th, and 5th, respectively."

## Discussion


## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — a broader claim this one bears on
- [Permutation importance analysis identifies which writing features drive each rubric scoring model, supporting interpretability of the deep learning black box](permutation-importance-rubric-interpretability.md) — related
- [For activity-defined engagement prediction in DTA logs, the activity-only Baseline remained strongest, and permutation importance was dominated by activity indicators](activity-baseline-strongest-engagement-prediction.md) — related
- [Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting](episode-features-predictive-importance-beyond-semantics.md) — related
