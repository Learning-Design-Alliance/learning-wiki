---
type: strategy
id: teacher-performance-summary-strategy
title: Provide teachers with LLM-generated performance summaries of class and per-question outcomes to guide instructional decisions
description: "Beyond student-facing feedback, the AAG system generates a \"Performance Summary\" for teachers, giving an overall view of how the class or an individual student performed relative to the assignment objectives."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: calvin-yeung-2025
    resource: "https://arxiv.org/abs/2501.14305"
    title: "Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. https://arxiv.org/abs/2501.14305"
    author: Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii
---

# Provide teachers with LLM-generated performance summaries of class and per-question outcomes to guide instructional decisions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 quant-synthesis), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Beyond student-facing feedback, the AAG system generates a "Performance Summary" for teachers, giving an overall view of how the class or an individual student performed relative to the assignment objectives. The summary includes "summary statistics for the assignment," a breakdown of each question, and an LLM-generated summary of common student issues drawn from the feedback delivered to students. The authors state this summary "equips teachers with valuable insights to guide their instructional decisions and support student improvement."

## Design Implications

### Context
#### Requirements
- The AAG pipeline must have graded the submissions and generated student feedback from which common issues can be summarized
#### Constraints
- 

### Target Learners
- instructors and teaching assistants in higher-education courses

### Target Learning Goals
- data-driven instructional adjustment based on class-wide and per-question performance insights

## Claims

- [Reviewed literature identifies personalisation, adaptive support, rapid feedback, and teacher-facing automation as recurring pedagogical opportunities of AI in mathematics education](../claims/ai-math-pedagogical-opportunities-personalisation-feedback.md) [+W]

## Related Strategies

- Aag Zero Shot Llm Grading System
- [Provide a cohort summary blueprinted report so teachers can identify gaps in teaching and trends in learner performance](cohort-summary-blueprinted-report-strategy.md)

## Examples
-

## Key Sources
- Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. https://arxiv.org/abs/2501.14305
