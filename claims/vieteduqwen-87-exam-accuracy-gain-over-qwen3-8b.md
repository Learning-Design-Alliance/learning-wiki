---
type: claim
title: "VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model"
description: "VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model"
id: vieteduqwen-87-exam-accuracy-gain-over-qwen3-8b
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: thang-doan-viet-2026
    resource: "https://arxiv.org/abs/2607.28647"
    title: "Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647"
    author: Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Fine-tuning Qwen3-8B with SFT and DPO raises examination accuracy from 80.92% to 87.02% across four epochs on 3,119 exam questions. [→ Thang Doan Viet 2026](#thang-doan-viet-2026)

## Evidence

### Thang Doan Viet 2026

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

Benchmark evaluation of VietEduQwen on 3,119 questions from the 2025 Vietnamese National High School Examination covering eight subjects. Accuracy rose from "80.92% for the base Qwen3-8B model to 87.02% after Epoch 4"; the paper also reports it outperforming Gemma-2-9B and comparable to Gemini 3 Flash.

> "overall examination accuracy increases from 80.92% for the base Qwen3-8B model to 87.02% after Epoch 4, corresponding to a total gain of +6.10%."

## Discussion


## Related Claims
- [Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality](dpo-training-contributes-accuracy-and-pedagogical-tone.md) — related
- [VietEduQwen improves over its base model across all eight exam subjects, with the largest gains in STEM disciplines, and its residual errors concentrate in multi-step computation and cross-concept integration](vieteduqwen-subject-wise-stem-gains-error-modes.md) — a narrower finding that bears on this claim
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
