---
type: claim
title: Almost no model-and-harness combination sustains tutoring over the full 30-day horizon, as learning plateaus within 5–10 days
description: Almost no model-and-harness combination sustains tutoring over the full 30-day horizon, as learning plateaus within 5–10 days
id: educlaw-bench-plateau-within-days
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: lee-2026
    resource: "https://arxiv.org/abs/2608.03206"
    title: "Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206"
    author: Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: lee-2026-2
    resource: "https://arxiv.org/abs/2608.03206"
    title: "Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206"
    author: Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Almost no model-and-harness combination sustains tutoring over the full 30-day horizon, as learning plateaus within 5–10 days

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Every agent plateaus in per-day student accuracy within 5–10 virtual days far below the ideal-learning reference, so almost no combination converts the full 30 days into sustained gain. [→ Lee 2026](#lee-2026)
`q2 i?` 53.3% of runs produce no learning gain (∆Solve ≤ 0) and 48.5% show no curriculum structure (Gagné below 1.5). [→ Lee 2026 (2)](#lee-2026-2)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Per-day student accuracy trajectories over 30 virtual days on the Codex tier with three representative adapters. Every adapter plateaus by day 5–10, with openclaw moving only from 0.28 to 0.29.

> "Overthefullhorizonthe leftpanelofFigure2showseveryagentplateauswithin5–10 days far below steady learning (openclaw0.28→0.29)."

### Lee 2026 (2)

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Analysis of four pedagogical failure modes across runs on the Codex tier. "thedominantfailuresarestructural" with no-curriculum affecting 48.5% and no-learning-gain affecting 53.3% of runs. metaclaw is the only adapter to mostly escape the no-curriculum mode (10% of runs).

> "butthedominantfailuresarestructural, with48.5%of runs showing no curriculum (Gagné below 1.5) and53.3%producing no learning gain (∆Solve≤0)"

## Discussion


## Related Claims
- [Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers](educlaw-bench-model-harness-interaction.md) — related
- [The simulated learner tracks a real-student KT model with calibration error 0.049, and the helpfulness rubric transfers to real classroom transcripts](educlaw-bench-simulator-calibration.md) — related
- [Learning paths used for SRL improved accuracy and performance without increasing effort, and tutoring-system benefits required sustained practice](learning-paths-srl-accuracy-without-effort.md) — related
