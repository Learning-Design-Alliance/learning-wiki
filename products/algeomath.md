---
type: product
id: algeomath
title: Algeomath
description: Algeomath is a Korean interactive mathematics education tool used to deliver web-based problem-solving activities, record learner work, and support automated grading and feedback.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Algeomath

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
Algeomath is a Korean interactive mathematics education tool used to deliver web-based problem-solving activities, record learner work, and support automated grading and feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Algeomath-based web platform with automated grading, progressive feedback, and LLM rubric evaluation**: The study implemented its tasks on a web-based environment built on Algeomath, described as "a Korean online tool designed for interactive math edu- cation", with a block coding workspace on the left and problem statement and response fields on the right. The platform records all intermediate responses, applies rule-based scoring for objective correctness, uses few-shot LLM prompting for open-ended explanations, and stores submissions, grading outcomes, and feedback text as evidence for rubric-based judgments. A FastAPI backend grades and assembles evidence, the LLM provides rubric-aligned judgments, and PostgreSQL stores results. (Yong Oh Lee et al. (2025))

### Claims
- [LLM-derived rubric scores show strong agreement with expert judgments in a field study of middle school students](../claims/llm-rubric-scores-agree-with-expert-judgments.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Yong Oh Lee, Byeonghun Bang, Sejun Oh. (2025). LLM-Driven Rubric-Based Assessment of Algebraic Competence in Multi-Stage Block Coding Tasks with Design and Field Evaluation. https://www.algeomath.kr/
