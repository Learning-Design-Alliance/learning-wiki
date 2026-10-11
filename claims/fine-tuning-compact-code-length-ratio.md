---
type: claim
title: "Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer"
description: "Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer"
id: fine-tuning-compact-code-length-ratio
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
---

# Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` On DSReal, Qwen2-VL-72B's outputs become substantially longer in failure cases (length ratio 4.01) than successful cases (1.52), while the fine-tuned Qwen2-VL-72B-TURTLE maintains a length ratio close to 1.0 across all cases. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626

`q2 · i?`

Code length analysis on DSReal computing length ratio (model-generated lines divided by reference-solution lines, comments and blank lines removed) for GPT-4o, Qwen2-VL-72B, and Qwen2-VL-72B-TURTLE. The article reports the base model's failure-case ratio of 4.01 versus 1.52 on successes, and that the fine-tuned model "maintains a length ratio close to 1.0 across all cases". No effect size is printed.

> "Qwen2-VL-72B exhibits a moderate length ratio on successful cases (ratio = 1.52), but its outputs become substantially longer in failure cases (ratio = 4.01), indicating a substantial increase in code verbosity upon failure."

## Discussion


## Related Claims
- [Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning](fine-tuning-improves-code-reasoning-alignment.md) — related
- [Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts](fine-tuning-synthetic-data-improves-turtleai.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
