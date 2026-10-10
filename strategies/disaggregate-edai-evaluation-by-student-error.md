---
type: strategy
id: disaggregate-edai-evaluation-by-student-error
title: Disaggregate evaluation of educational AI by student error and proficiency before classroom deployment
description: The article recommends that evaluation of AI in education report performance separately for student subgroups defined by demonstrated proficiency and error status, rather than only aggregate accuracy.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: li-lucy-2026
    resource: "https://arxiv.org/abs/2603.00925"
    title: "Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925"
    author: Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo
---

# Disaggregate evaluation of educational AI by student error and proficiency before classroom deployment

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that evaluation of AI in education report performance separately for student subgroups defined by demonstrated proficiency and error status, rather than only aggregate accuracy. It argues this "pinpoints whether models can actually discern when a student may need pedagogical support (F2), and whether they equitably serve students across different levels of proficiency (F1)". The authors apply this approach by re-running an existing benchmark evaluation disaggregated by student error across five analyses.

## Design Implications

### Context
#### Requirements
- Benchmark data annotated with student error or proficiency labels
- Evaluation approach re-appliable across education-related benchmarks
#### Constraints
- Findings derive from one English benchmark on one learning platform and may not map directly onto other languages and contexts

### Target Learners
- K-12 mathematics students, particularly those requiring additional pedagogical support

### Target Learning Goals
- Accurate AI assessment of student errors and correctness in math

## Related Strategies

- [Benchmark AI assistants on specialized educational tasks before classroom deployment](benchmark-ai-assistants-before-classroom-deployment.md)

## Examples
-

## Key Sources
- Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925
