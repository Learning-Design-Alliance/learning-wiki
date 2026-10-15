---
type: claim
title: Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs
description: Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs
id: fine-tuning-limited-gains-hand-drawn-tasks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: chao-wen-2026
    resource: "https://doi.org/10.48550/arxiv.2606.03626"
    title: "Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)"
    author: Chao Wen, Jacqueline Staub, and Adish Singla
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Performance improvements from fine-tuning mainly come from DSReal and DSSyn, while performance on the hand-drawn DSCraft dataset remains low. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)

`q2 · i?` · `causal · r1`

Main-results analysis across dataset types: DSCraft contains hand-drawn renderings of the same 102 DSReal tasks. The article reports fine-tuned models' performance "on DSCraft re- mains low" (e.g., Qwen2-VL-72B-TURTLE at 6.86% symbolic versus 35.29% on DSReal). No effect size is printed.

> "However, perfor- mance improvements mainly come from DSReal and DSSyn, while performance on DSCraft re- mains low, indicating that fine-tuning primarily improves performance on clean and synthetic in- puts but does not fully address robustness to out-of- distribution hand-drawn tasks."

## Discussion


## Related Claims
- [Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning](fine-tuning-improves-code-reasoning-alignment.md) — related
- [Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts](fine-tuning-synthetic-data-improves-turtleai.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
- [The v2 synthetic generator was tuned for stricter trace-data realism with more incorrect code, retries, and longer dialogues](astra-v2-generator-stricter-realism.md) — related
