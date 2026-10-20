---
type: claim
title: Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning
description: Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning
id: fine-tuning-improves-code-reasoning-alignment
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
    kind: causal
    rigour: 1
---

# Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Fine-tuning increases Qwen2-VL-72B's success rate on DSReal from 10.8% to 35.3%, mainly by reducing programming errors from 30.4% to 6.9%, while visual understanding and spatial reasoning errors remain largely unchanged. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)

`q2 · i?` · `causal · r1`

Failure-type distribution analysis on DSReal comparing base and fine-tuned Qwen2-VL-72B (Figure 6). The comparison showed fine-tuning "increases the success rate from 10.8% to 35.3%", driven by reduced programming errors; visual understanding and spatial reasoning errors remained largely unchanged. No effect size is printed.

> "By comparing Qwen2-VL-72B and Qwen2-VL-72B-TURTLE, we observe that fine-tuning increases the success rate from 10.8% to 35.3%, mainly by reducing programming errors (from 30.4% to 6.9%)."

## Discussion


## Related Claims
- [Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer](fine-tuning-compact-code-length-ratio.md) — related
- [Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts](fine-tuning-synthetic-data-improves-turtleai.md) — related
- [Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs](fine-tuning-limited-gains-hand-drawn-tasks.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
- [Embodied teaching actions are spatially accurate across models, but temporal action–speech alignment remains more variable](lecturaagents-taq-spatial-strong-temporal-variable.md) — related
