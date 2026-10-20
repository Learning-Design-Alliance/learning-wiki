---
type: claim
title: ConnectED reduces 45-minute lesson preparation time to approximately 15–20 minutes in-system, versus 3–4 hours for manual preparation
description: ConnectED reduces 45-minute lesson preparation time to approximately 15–20 minutes in-system, versus 3–4 hours for manual preparation
id: connected-reduces-lesson-preparation-time
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: thang-doan-viet-2026
    resource: "https://doi.org/10.48550/arxiv.2607.28647"
    title: "Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647 [doi:10.48550/arxiv.2607.28647](https://doi.org/10.48550/arxiv.2607.28647)"
    author: Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ConnectED reduces 45-minute lesson preparation time to approximately 15–20 minutes in-system, versus 3–4 hours for manual preparation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` End-to-end lesson preparation time drops from 3–4 hours manually to roughly 15–20 minutes with ConnectED, a 9–12× speedup. [→ Thang Doan Viet 2026](#thang-doan-viet-2026)

## Evidence

### Thang Doan Viet 2026

Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647 [doi:10.48550/arxiv.2607.28647](https://doi.org/10.48550/arxiv.2607.28647)

`q2 · i?` · `design · r2`

Efficiency measurement using in-system logs collected during teacher-led sessions, timing production of a complete 45-minute Official Dispatch 5512-compliant lesson including teacher review. Preparation took "approximately 15–20 minutes" versus 3–4 hours manually; the conclusion section cites 30–45 minutes and a 5–8× figure.

> "ConnectED achieves a substantial efficiency gain, reducing lesson planning time from 3–4 hours under manual preparation to approximately 15–20 minutes, corresponding to a 9–12×speedup."

## Discussion


## Related Claims
- [Removing teacher-in-the-loop review or the curriculum checker significantly lowers teacher satisfaction, and replacing ADDIE orchestration with unstructured prompting yields the lowest satisfaction and longest preparation time](system-ablation-teacher-oversight-and-addie-orchestration-value.md) — related
- [In a one-year PBL deployment, the AI-assisted pipeline was associated with instructor preparation time falling from an average of eight hours to two hours per instruction (an estimated 75% reduction).](ai-pipeline-75-percent-prep-time-reduction.md) — related
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
