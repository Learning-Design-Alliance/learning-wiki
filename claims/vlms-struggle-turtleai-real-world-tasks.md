---
type: claim
title: Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6
description: Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6
id: vlms-struggle-turtleai-real-world-tasks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the real-world dataset DSReal, the top-performing model o3 achieves only a 40.2% symbolic success rate on tasks designed for students in grades 3-6. [→ Chao Wen 2026](#chao-wen-2026)
`q2 i?` On the full TURTLEAI-DS dataset, the highest base-model symbolic success rate is 15.9% (o4-mini), and most models fall below 30% on real-world tasks. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626 [doi:10.48550/arxiv.2606.03626](https://doi.org/10.48550/arxiv.2606.03626)

`q2 · i?` · `design · r2`

Benchmark evaluation of 20+ VLMs on TURTLEAI-DSReal (102 real-world tasks), reporting symbolic and embedding-based success rates with greedy decoding. The evaluation found "only a 40.2% symbolic success rate" for the best model, o3; on the full dataset the best base model reached 15.9% (o4-mini) and Qwen2.5-VL 6.80%. No effect size is reported.

> "On the real-world dataset DSReal containing tasks designed for students in grades 3-6, even the top-performing model, o3, achieves only a 40.2% symbolic success rate, suggesting current VLMs are still far from ready for classroom deployment."

## Discussion


## Related Claims
- [Fine-tuning primarily improves alignment between code generation and visual reasoning rather than visual understanding or spatial reasoning](fine-tuning-improves-code-reasoning-alignment.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
- [Fine-tuning VLMs on synthetic data from TURTLEAI-Datagen improves performance on TURTLEAI, raising symbolic success rates by over 10% over base counterparts](fine-tuning-synthetic-data-improves-turtleai.md) — related
- [Fine-tuning on clean synthetic data yields limited gains on hand-drawn tasks, indicating limited robustness to out-of-distribution hand-drawn inputs](fine-tuning-limited-gains-hand-drawn-tasks.md) — related
- [Model performance varies by task category, with Basic Geometry easiest and Spiral consistently the most challenging category](spiral-hardest-basic-geometry-easiest-categories.md) — related
- [Fine-tuning is associated with more compact generated code, with the fine-tuned Qwen2-VL-72B maintaining a length ratio near 1.0 while the base model's failed outputs become substantially longer](fine-tuning-compact-code-length-ratio.md) — related
