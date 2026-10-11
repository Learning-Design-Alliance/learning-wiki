---
type: claim
title: Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality
description: Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality
id: dpo-training-contributes-accuracy-and-pedagogical-tone
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

# Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Dropping DPO from training lowers accuracy from 87.02% to 85.91% and yields qualitatively lower pedagogical tone as rated by two annotators on 50 sampled responses. [→ Thang Doan Viet 2026](#thang-doan-viet-2026)

## Evidence

### Thang Doan Viet 2026

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

Model-level ablation (Table 3): full VietEduQwen rated High pedagogical quality at 87.02% accuracy; SFT-only reached 85.91% (Medium); base Qwen3-8B 80.92% (Very low). Quality ratings came from "two independent annotators rating a sample of 50 responses".

> "Removing the DPO objective reduces accuracy by 1.11 percentage points (from 87.02% to 85.91%) and leads to qualitatively degraded pedagogical tone, as assessed by two independent annotators rating a sample of 50 responses on a three-level scale"

## Discussion


## Related Claims
- [VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model](vieteduqwen-87-exam-accuracy-gain-over-qwen3-8b.md) — related
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
