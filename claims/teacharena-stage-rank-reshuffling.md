---
type: claim
title: Across 17 frontier models, Stage 1 pedagogical-judgment scores are high (mean 0.893) while rank correlations with Stage 2 (ρ=0.24) and Stage 3 (ρ=0.21) are weak, with workflow scores topping out at 0.704
description: Across 17 frontier models, Stage 1 pedagogical-judgment scores are high (mean 0.893) while rank correlations with Stage 2 (ρ=0.24) and Stage 3 (ρ=0.21) are weak, with workflow scores topping out at 0.704
id: teacharena-stage-rank-reshuffling
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: zixin-chen-2026
    resource: "https://arxiv.org/abs/2605.14322"
    title: "Zixin Chen, Peng Liu, Rui Sheng, Haobo Li, Jianhong Tu, Xiaodong Deng, Kashun Shum, Dayiheng Liu, Huamin Qu. (2026). Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows. Preprint. https://arxiv.org/abs/2605.14322"
    author: Zixin Chen, Peng Liu, Rui Sheng, Haobo Li, Jianhong Tu, Xiaodong Deng, Kashun Shum, Dayiheng Liu, Huamin Qu
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Across 17 frontier models, Stage 1 pedagogical-judgment scores are high (mean 0.893) while rank correlations with Stage 2 (ρ=0.24) and Stage 3 (ρ=0.21) are weak, with workflow scores topping out at 0.704

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` Model rankings reshuffle across the three benchmark stages: Stage 2 correlates weakly with Stage 1 (ρ=0.24) and Stage 3 (ρ=0.21), while Stages 1 and 3 correlate more closely (ρ=0.58), and the median gap between a model's best and worst stage rank is seven positions. [→ Zixin Chen 2026](#zixin-chen-2026)
`q2 i?` Stage 1 scores are high under the bounded-evidence contract (mean 0.893; range 0.799–0.947), while no model exceeds 0.704 on Stage 3 workflows. [→ Zixin Chen 2026](#zixin-chen-2026)

## Evidence

### Zixin Chen 2026

Zixin Chen, Peng Liu, Rui Sheng, Haobo Li, Jianhong Tu, Xiaodong Deng, Kashun Shum, Dayiheng Liu, Huamin Qu. (2026). Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows. Preprint. https://arxiv.org/abs/2605.14322

`q2 · i?` · `design · r?`

Evaluation of 17 frontier models on the TEACHARENA leaderboard (Table 6), a benchmark evaluation rather than a human experiment. The article reports "mean 0.893" on Stage 1, weak rank correlations between Stage 2 and Stages 1 and 3, and a median best-to-worst stage-rank gap of seven positions; workflow scores top out at 0.704.

> "Stage 1 scores are high under its bounded-evidence contract (mean 0.893; range 0.799–0.947), while stage-resolved reporting reveals substantial rank variation. The descriptive rank correlations are weak between Stage 2 and both Stage 1 (ρ= 0.24 ) and Stage 3 (ρ= 0.21 )"

## Discussion


## Related Claims
- [Claude Opus 4.8 has the highest overall score (0.803) and is the only model ranking in the top three on all three stages, yet does not saturate situated tutoring (0.773) or workflows (0.704)](claude-opus-48-highest-overall-unsaturated.md) — related
- [The six long-chain Stage 3 workflows average 0.321 versus 0.559 across all other Stage 3 tasks and are the lowest-scoring family for 15 of 17 models](long-chain-workflows-lowest-stage3-family.md) — related
