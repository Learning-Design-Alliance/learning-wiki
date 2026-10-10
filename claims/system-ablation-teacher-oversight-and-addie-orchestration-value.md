---
type: claim
title: Removing teacher-in-the-loop review or the curriculum checker significantly lowers teacher satisfaction, and replacing ADDIE orchestration with unstructured prompting yields the lowest satisfaction and longest preparation time
description: Removing teacher-in-the-loop review or the curriculum checker significantly lowers teacher satisfaction, and replacing ADDIE orchestration with unstructured prompting yields the lowest satisfaction and longest prepara...
id: system-ablation-teacher-oversight-and-addie-orchestration-value
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

# Removing teacher-in-the-loop review or the curriculum checker significantly lowers teacher satisfaction, and replacing ADDIE orchestration with unstructured prompting yields the lowest satisfaction and longest preparation time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Removing the teacher-in-the-loop review stage causes a statistically significant drop in teacher satisfaction (p<0.05, Wilcoxon signed-rank test, n=18), despite marginally reducing preparation time. [→ Thang Doan Viet 2026](#thang-doan-viet-2026)
`q2 i?` Replacing full ADDIE orchestration with unstructured prompting (Generic LLM workflow) substantially increases preparation time (90–120 minutes) and achieves the lowest satisfaction (3.6±0.8, p<0.01). [→ Thang Doan Viet 2026 (2)](#thang-doan-viet-2026-2)

## Evidence

### Thang Doan Viet 2026

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

System-level ablation (Table 4) with 18 teachers, comparing variants against the full pipeline using Wilcoxon signed-rank tests. Satisfaction fell from 4.7±0.4 to 3.9±0.6 without teacher-in-the-loop review; the authors conclude teachers "value control over AI outputs even at the cost of additional time".

> "Removing the teacher-in-the-loop review stage reduces preparation time marginally but causes a statistically significant drop in teacher satisfaction (p<0.05, Wilcoxon signed-rank test [48])"

### Thang Doan Viet 2026 (2)

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647

`q2 · i?` · `design · r2`

System-level ablation (Table 4): the Generic LLM workflow took 90–120 minutes with satisfaction 3.6±0.8 (p<0.01 vs. full pipeline), the lowest of all variants. The authors state this demonstrates ADDIE orchestration "contributes independent value beyond model capability alone".

> "Replacing the full ADDIE orchestration layer with unstructured prompting of the same VietEduQwen model (theGeneric LLM workflowrow)substantially increases preparation time and achieves the lowest satisfaction score"

## Discussion


## Related Claims
- [Teachers and students report strong satisfaction with ConnectED, with 94% of teachers willing to reuse it](connected-high-teacher-student-satisfaction.md) — related
- [ConnectED reduces 45-minute lesson preparation time to approximately 15–20 minutes in-system, versus 3–4 hours for manual preparation](connected-reduces-lesson-preparation-time.md) — related
- [Implementing a student-made glossary significantly lowered first-year engineering students' satisfaction with the M-Tutor tutorial](glossary-intervention-lowered-satisfaction-m-tutor.md) — related
