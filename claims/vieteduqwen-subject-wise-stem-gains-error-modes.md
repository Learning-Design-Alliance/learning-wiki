---
type: claim
title: VietEduQwen improves over its base model across all eight exam subjects, with the largest gains in STEM disciplines, and its residual errors concentrate in multi-step computation and cross-concept integration
description: VietEduQwen improves over its base model across all eight exam subjects, with the largest gains in STEM disciplines, and its residual errors concentrate in multi-step computation and cross-concept integration
id: vieteduqwen-subject-wise-stem-gains-error-modes
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
  - id: thang-doan-viet-2026-2
    resource: "https://arxiv.org/abs/2607.28647"
    title: "Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647"
    author: Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# VietEduQwen improves over its base model across all eight exam subjects, with the largest gains in STEM disciplines, and its residual errors concentrate in multi-step computation and cross-concept integration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` VietEduQwen consistently improves over Qwen3-8B across all eight subjects, with the largest gains in Mathematics, Physics, and Chemistry. [→ Thang Doan Viet 2026](#thang-doan-viet-2026)
`q2 i?` Of 200 sampled errors, approximately 41% involve multi-step numerical computation and 33% involve integration across two or more textbook concepts. [→ Thang Doan Viet 2026 (2)](#thang-doan-viet-2026-2)

## Evidence

### Thang Doan Viet 2026

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

Subject-wise accuracy analysis across eight examination subjects, presented in Fig. 7. The text reports the model "consistently improves over the base Qwen3-8B model across all subjects" and narrows the gap with commercial baselines in STEM.

> "VietEduQwen consistently improves over the base Qwen3-8B model across all subjects. The largest gains are observed in STEM disciplines, particularly Mathematics, Physics, and Chemistry, where VietEduQwen substantially narrows the performance gap with Gemini-2.5 and Gemini-3 variants."

### Thang Doan Viet 2026 (2)

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

Manual error analysis of a random sample of 200 errors from VietEduQwen's incorrect predictions. The authors report "Approximately 41% involve multi-step numerical computation" and a further 33% cross-concept integration failures; the remaining 26% span reading comprehension, unit conversion, and ambiguous distractors.

> "Approximately 41% involve multi-step numerical computation where intermediate rounding or sign errors propagate to incorrect final answers. A further 33% involve questions requiring integration of information across two or more textbook concepts"

## Discussion


## Related Claims
- [VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model](vieteduqwen-87-exam-accuracy-gain-over-qwen3-8b.md) — a broader claim this one bears on
