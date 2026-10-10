---
type: claim
title: "Responsiveness and helpfulness trade off: always-answer adapters score lowest on helpfulness while withholding adapters score highest"
description: "Responsiveness and helpfulness trade off: always-answer adapters score lowest on helpfulness while withholding adapters score highest"
id: educlaw-bench-responsiveness-helpfulness-tradeoff
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

# Responsiveness and helpfulness trade off: always-answer adapters score lowest on helpfulness while withholding adapters score highest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the frontier tiers, the always-answer adapters (picoclaw, deeptutor, ironclaw) score lowest on Helpfulness (3.8–4.6) while the withholding adapters (openclaw, zeroclaw) score highest (5.6–6.1), with direct leakage staying negligible (0.05% hand-over). [→ Lee 2026](#lee-2026)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Benchmark results on frontier tiers showing the inverse relationship between responsiveness (fraction of help-requests answered) and helpfulness (29-item LearnLM rubric). Always-answer adapters reach near-100% responsiveness but score 1.5–2 points lower on helpfulness.

> "Responsiveness spans25–100%and runs inversely to Helpfulness on the frontier tiers, where the always-answer adapters (picoclaw, deeptutor, ironclaw) scorelowestonHelp(3.8–4.6)andthewithholdingadapters (openclaw,zeroclaw)highest(5.6–6.1),whiledirectleakage staysnegligible(0.05%hand-over)."

## Discussion


## Related Claims
- [LoRA RFT with a helpfulness-weighted composite reward can collapse an adapter's pedagogy mid-training while responsiveness stays intact](educlaw-bench-rft-helpfulness-collapse.md) — related
