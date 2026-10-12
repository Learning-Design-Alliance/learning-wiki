---
type: claim
title: Model performance varies by task category, with Basic Geometry easiest and Spiral consistently the most challenging category
description: Model performance varies by task category, with Basic Geometry easiest and Spiral consistently the most challenging category
id: spiral-hardest-basic-geometry-easiest-categories
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

# Model performance varies by task category, with Basic Geometry easiest and Spiral consistently the most challenging category

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across the six task categories, models perform best on Basic Geometry, while Spiral is consistently the most challenging category for all models. [→ Chao Wen 2026](#chao-wen-2026)

## Evidence

### Chao Wen 2026

Chao Wen, Jacqueline Staub, and Adish Singla. (2026). TURTLEAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics. https://arxiv.org/abs/2606.03626

`q2 · i?` · `design · r2`

Fine-grained analysis of symbolic success rates across task categories (Figure 5a) for representative VLMs including o3, GPT-5, GPT-4o, and Qwen2-VL-72B variants. The article found "Spiral is consistently the most challenging category", attributing this to long-horizon sequential control; Composite tasks were not uniformly harder than single-transformation tasks. No effect size is printed.

> "Across task categories (see Figure 5a), models perform best on Basic Geometry, while Spiral is consistently the most challenging category for all models, as it requires long-horizon, sequential control with tightly coupled steps."

## Discussion


## Related Claims
- [Across frontier LLMs, Counseling is the easiest educational activity center (average 8.78) while Assessment and Research are hardest (8.42), and performance degrades from Easy to Hard difficulty](center-difficulty-difficulty-degradation-llms.md) — related
- [Lower-performing LLMs show higher variance across pedagogy subject categories and peak in Technology and General categories](low-performing-models-subject-variance-technology-general.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
