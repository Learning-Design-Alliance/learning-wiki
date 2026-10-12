---
type: claim
title: All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks
description: All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks
id: vlms-struggle-spatial-reasoning-visual-precision
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
  - id: chao-wen-2026-2
    resource: "https://arxiv.org/abs/2606.03626"
    title: "Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626"
    author: Chao Wen, Jacqueline Staub, and Adish Singla
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` All models struggle with spatial reasoning — reasoning about relative positions, distances, angles, and sizes of patterns in the image. [→ Chao Wen 2026](#chao-wen-2026)
`q2 i?` Despite correct visual reasoning, models fail to achieve low-level visual accuracy, ignoring tiny details like angles and relative positions. [→ Chao Wen 2026 (2)](#chao-wen-2026-2)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626

`q2 · i?` · `design · r2`

Systematic manual failure analysis on DSReal for GPT-4o, Qwen2-VL-72B, and Qwen2-VL-72B-TURTLE, attributing each failure case to a failure type. The analysis found "all models struggle with spatial reasoning"; the authors suggest this might be due to scarcity of training data capturing spatial relationships. No effect size is printed.

> "We find that all models struggle with spatial reasoning, which is the ability to reason about the spatial relationships among different patterns in the image, such as relative positions, distances, angles, and sizes of patterns."

### Chao Wen 2026 (2)

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626

`q2 · i?` · `design · r2`

Same manual failure analysis on DSReal: models can often replicate the intended image from a high-level perspective but fail low-level visual accuracy, such as ignoring tiny details like angles and relative positions. No effect size is printed.

> "We find that despite correct visual reasoning, models still face difficulties in achieving visual precision during replication."

## Discussion


## Related Claims
- [Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer](fine-tuning-compact-code-length-ratio.md) — related
- [Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning](fine-tuning-improves-code-reasoning-alignment.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
- [Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check](checkwise-backtranslation-spatial-strong-angle-weak.md) — related
- [All evaluated GenAI systems scored noticeably lower on graphics-related questions requiring interpretation of JavaFX output](genai-weak-visual-reasoning-javafx-questions.md) — related
- [Viewpoint-aware spatial reasoning is a persistent bottleneck with poor calibration of spatial uncertainty](viewpoint-aware-spatial-reasoning-bottleneck.md) — a broader claim this one bears on
