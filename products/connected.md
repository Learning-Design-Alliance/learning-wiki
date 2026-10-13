---
type: product
id: connected
title: ConnectED
description: ConnectED is a web application developed by Thang Doan Viet et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# ConnectED

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
ConnectED is a web application developed by Thang Doan Viet et al. that enables teachers to create and review curriculum-aligned lessons and deliver interactive activities, AI hints, emotional support, and class-level learning analytics to secondary students.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ConnectED web application with student-facing Playground interactive learning environment**: ConnectED is a web application that supports curriculum-aligned lesson creation and real-time classroom use, delivering lesson artifacts to students through an interactive environment called Playground. After a teacher approves a lesson, students engage via quizzes, review slides, and flashcards while VietEduQwen provides step-by-step hints and emotionally supportive feedback; the system "collects structured learning signals that teachers can use to guide lesson refinement". The frontend is React/TypeScript with a FastAPI backend, Celery workers, Redis, and MongoDB. Implementation details: teacher-in-the-loop review at every step, lesson repository for reuse, and class-level learning analytics. (Thang Doan Viet et al. (2026))

### Claims

- [Removing teacher-in-the-loop review or the curriculum checker significantly lowers teacher satisfaction, and replacing ADDIE orchestration with unstructured prompting yields the lowest satisfaction and longest preparation time](../claims/system-ablation-teacher-oversight-and-addie-orchestration-value.md) [+W]
- [ConnectED reduces 45-minute lesson preparation time to approximately 15–20 minutes in-system, versus 3–4 hours for manual preparation](../claims/connected-reduces-lesson-preparation-time.md) [+W]
- [Teachers and students report strong satisfaction with ConnectED, with 94% of teachers willing to reuse it](../claims/connected-high-teacher-student-satisfaction.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Thang Doan Viet, Anh Nguyen Hoang, Tinh Luong Son, Anh Hoang Thi Ngoc, Huyen Giang Thi Thu, Tai Le Quy. (2026). ConnectED: A Curriculum-Aligned AI System for Vietnamese Instructional Lesson Planning and Student Learning. arXiv. https://arxiv.org/abs/2607.28647
