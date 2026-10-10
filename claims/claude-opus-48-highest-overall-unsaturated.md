---
type: claim
title: Claude Opus 4.8 has the highest overall score (0.803) and is the only model ranking in the top three on all three stages, yet does not saturate situated tutoring (0.773) or workflows (0.704)
description: Claude Opus 4.8 has the highest overall score (0.803) and is the only model ranking in the top three on all three stages, yet does not saturate situated tutoring (0.773) or workflows (0.704)
id: claude-opus-48-highest-overall-unsaturated
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

# Claude Opus 4.8 has the highest overall score (0.803) and is the only model ranking in the top three on all three stages, yet does not saturate situated tutoring (0.773) or workflows (0.704)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` The highest-scoring model overall (0.803) still falls short on Stage 2 tutoring (0.773) and Stage 3 workflows (0.704), showing even strong profiles do not saturate the matched contracts. [→ Zixin Chen 2026](#zixin-chen-2026)

## Evidence

### Zixin Chen 2026

Zixin Chen, Peng Liu, Rui Sheng, Haobo Li, Jianhong Tu, Xiaodong Deng, Kashun Shum, Dayiheng Liu, Huamin Qu. (2026). Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows. Preprint. https://arxiv.org/abs/2605.14322

`q2 · i?` · `design · r?`

Leaderboard result from the 17-model evaluation (Table 6). The article reports the overall point estimate and the Stage 2 and Stage 3 scores for the top model, and notes all four Gemini variants rank lower on Stage 3 than Stage 2, with Gemini-2.5-Pro second on tutoring (0.769) but 12th on workflows (0.477).

> "Claude Opus 4.8 has the highest overall point estimate (0.803) and is the only model whose point estimates rank in the top three on all three stages. Even this broadly strong profile does not saturate the matched situated-tutoring or workflow contracts, scoring 0.773 and 0.704, respectively."

## Discussion


## Related Claims
- [Across 17 frontier models, Stage 1 pedagogical-judgment scores are high (mean 0.893) while rank correlations with Stage 2 (ρ=0.24) and Stage 3 (ρ=0.21) are weak, with workflow scores topping out at 0.704](teacharena-stage-rank-reshuffling.md) — related
- [In the S0-54 tutoring episode, the learner reaches the correct posterior (1/6) yet the three Stage 2 evidence scopes yield different diagnoses, with full trajectory credit withheld because part of the interpretation remains tutor-owned](s0-54-mixed-diagnosis-correct-answer.md) — related
- [The strategic surface learner is the lowest-scoring Stage 2 profile for 15 of 17 models, averaging 0.702 versus 0.757 across the other profiles](strategic-surface-learner-lowest-stage2-profile.md) — related
