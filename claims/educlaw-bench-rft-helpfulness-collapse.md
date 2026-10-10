---
type: claim
title: "LoRA RFT with a helpfulness-weighted composite reward can collapse an adapter's pedagogy mid-training while responsiveness stays intact"
description: "LoRA RFT with a helpfulness-weighted composite reward can collapse an adapter's pedagogy mid-training while responsiveness stays intact"
id: educlaw-bench-rft-helpfulness-collapse
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
    kind: causal
    rigour: 2
---

# LoRA RFT with a helpfulness-weighted composite reward can collapse an adapter's pedagogy mid-training while responsiveness stays intact

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` After LoRA RFT on the Small tier, both adapters land near zero on Axis I yet diverge on helpfulness: metaclaw-rft holds Help flat (4.73→4.76) while openclaw-rl-rft collapses (3.19→2.30), with neither losing responsiveness. [→ Lee 2026](#lee-2026)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `causal · r2`

LoRA RFT (rank-16, 5 epochs) on the Small tier against a composite reward over per-scenario normalized Axes I–III, epoch-averaged (n= 275). "metaclaw-rft holds Help flat (4.73→4.76)" while openclaw-rl-rft's Help falls 3.19→2.30 with no recovery by epoch 3.

> "After train- ing both adapters land near zero on Axis I yet diverge on helpfulness, as metaclaw-rft holds Help flat (4.73→4.76) whileopenclaw-rl-rftcollapses,itsHelpfalling3.19→2.30"

## Discussion


## Related Claims
- [Tutoring quality belongs to the base model and agent harness together rather than either alone, as adapter rankings reorder across tiers](educlaw-bench-model-harness-interaction.md) — related
- [Responsiveness and helpfulness trade off: always-answer adapters score lowest on helpfulness while withholding adapters score highest](educlaw-bench-responsiveness-helpfulness-tradeoff.md) — related
