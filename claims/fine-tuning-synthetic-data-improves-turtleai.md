---
type: claim
title: "Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts"
description: "Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts"
id: fine-tuning-synthetic-data-improves-turtleai
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chao-wen-2026
    resource: "https://doi.org/10.48550/arxiv.2606.03626"
    title: "Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)"
    author: Chao Wen, Jacqueline Staub, and Adish Singla
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Fine-tuning models (Pixtral-12B-TURTLE, Qwen2-VL-7B-TURTLE, Qwen2-VL-72B-TURTLE) consistently improves symbolic success rates by over 10% over their base counterparts on TURTLEAI-DS. [→ Chao Wen 2026](#chao-wen-2026)
`q2 i?` Fine-tuning Qwen2-VL-72B on synthetic data yields roughly a 20% improvement on real-world tasks. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)

`q2 · i?` · `design · r2`

Main results table comparing fine-tuned models (trained on TURTLEAI-Train, 738k samples) against base models across DSReal, DSCraft, DSSyn, and the full dataset. For example, Qwen2-VL-72B-TURTLE reached 35.29% symbolic success on DSReal versus 11.76% for the base model; the article reports "increasing symbolic success rates by over 10%". No effect size is printed.

> "Fine-tuning models (e.g., Pixtral-12B-TURTLE, Qwen2-VL-7B-TURTLE, and Qwen2-VL-72B-TURTLE) consistently improves performance on TURTLEAI-DS, increasing symbolic success rates by over 10% over their base counterparts."

## Discussion


## Related Claims
- [Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer](fine-tuning-compact-code-length-ratio.md) — related
- [Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning](fine-tuning-improves-code-reasoning-alignment.md) — related
- [Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs](fine-tuning-limited-gains-hand-drawn-tasks.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
