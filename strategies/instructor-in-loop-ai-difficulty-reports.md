---
type: strategy
id: instructor-in-loop-ai-difficulty-reports
title: Position the instructor as human-in-the-loop reviewer of AI-generated difficulty reports before any feedback reaches students
description: "In this strategy, the instructor first reviews the student's raw attempt history, then optionally invokes AI-assisted analysis to obtain a labeled difficulty report, and approves it before feedback reaches the student."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: daniel-prol-2026
    resource: "https://arxiv.org/abs/2609.15944"
    title: "Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944"
    author: Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour
---

# Position the instructor as human-in-the-loop reviewer of AI-generated difficulty reports before any feedback reaches students

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
In this strategy, the instructor first reviews the student's raw attempt history, then optionally invokes AI-assisted analysis to obtain a labeled difficulty report, and approves it before feedback reaches the student. The article's workflow specifies that "the instructor reviews the student's raw attempt history, optionally invokes the AI-assisted analysis to obtain a labeled difficulty report, and approves it before any feedback reaches the student". This reflects the concerns that AI feedback can be technically correct yet unhelpful, and that instructors are better positioned to judge whether a detected pattern is pedagogically meaningful given course context. Both deployed instructors supplemented AI reports by reviewing interaction traces before deciding on feedback.

## Design Implications

### Context
#### Requirements
- Instructor access to per-student attempt histories and activity logs via the dashboard
- The AI pipeline runs only when an instructor explicitly invokes it
#### Constraints
- The extent to which this visualization can be most effective is an area that requires more investigation, per the authors

### Target Learners
- university instructors of programming courses

### Target Learning Goals
- identifying recurring student difficulty patterns to inform targeted intervention decisions

## Related Strategies

- [Human-in-the-loop validation workflow: hold all AI-generated teaching content in unreviewed status until a teacher manually approves it](human-in-the-loop-teacher-validation-workflow.md)

## Examples
-

## Key Sources
- Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944
