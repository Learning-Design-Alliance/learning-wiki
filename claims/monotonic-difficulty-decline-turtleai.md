---
type: claim
title: Success rates decrease monotonically from easy to medium to hard difficulty levels across all models
description: Success rates decrease monotonically from easy to medium to hard difficulty levels across all models
id: monotonic-difficulty-decline-turtleai
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chao-wen-2026
    resource: "https://arxiv.org/abs/2606.03626"
    title: "Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626"
    author: Chao Wen, Jacqueline Staub, and Adish Singla
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Success rates decrease monotonically from easy to medium to hard difficulty levels across all models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All models exhibit a clear monotonic trend, with success rates highest on easy tasks and decreasing on medium and hard tasks. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626

`q2 · i?` · `design · r2`

Fine-grained analysis of symbolic success rates across the three labeled difficulty levels (Figure 5b) for representative VLMs. The article reports "a clear monotonic trend, with success rates highest on easy tasks and decreasing on medium and hard tasks", supporting the validity of the difficulty labeling. No effect size is printed.

> "Across difficulty levels (see Figure 5b), all models exhibit a clear monotonic trend, with success rates highest on easy tasks and decreasing on medium and hard tasks, suggesting that the difficulty levels in our datasets capture meaningful differences in task complexity."

## Discussion


## Related Claims
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
- [Across frontier LLMs, Counseling is the easiest educational activity center (average 8.78) while Assessment and Research are hardest (8.42), and performance degrades from Easy to Hard difficulty](center-difficulty-difficulty-degradation-llms.md) — related
- [Task difficulty increases hesitations, with significantly more hesitations on Medium and Hard tasks than Easy tasks](task-difficulty-increases-hesitations-scratch-videos.md) — related
