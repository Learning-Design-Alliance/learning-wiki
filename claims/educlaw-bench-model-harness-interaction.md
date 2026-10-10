---
type: claim
title: Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers
description: Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers
id: educlaw-bench-model-harness-interaction
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
---

# Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` No adapter leads Axis I (learning gain) on more than one base-model tier, so base model and harness interact rather than contribute separably, and single-tier leaderboards mis-rank systems. [→ Lee 2026](#lee-2026)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Benchmark evaluation of 10 agent adapters across 3 base-model tiers over 55 scenarios, each averaged over 4 students. The authors report that "No adapter leads Axis Ionmorethanonetier", demonstrating that "base model and harnessinteractratherthancontributeseparably."

> "No adapter leads Axis Ionmorethanonetier (openclawonSolar-pro3+0.36%,zeroclawonCodex-gpt5.5 −0.08%, metaclaw on Qwen3+0.64%), so base model and harnessinteractratherthancontributeseparably"

## Discussion


## Related Claims
- [Almost no model-and-harness combination sustains tutoring over the full 30-day horizon, as learning plateaus within 5–10 days](educlaw-bench-plateau-within-days.md) — related
- [LoRA RFT with a helpfulness-weighted composite reward can collapse an adapter's pedagogy mid-training while responsiveness stays intact](educlaw-bench-rft-helpfulness-collapse.md) — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — related
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
