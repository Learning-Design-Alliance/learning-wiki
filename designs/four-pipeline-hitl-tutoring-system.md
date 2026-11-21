---
type: design
id: four-pipeline-hitl-tutoring-system
title: Four-pipeline adaptive tutoring system with RAG and feedback tagging
description: "A \"modular web service built on Flask and MongoDB, augmented by a four-pipeline query manager\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: bhavishya-tarun-2025
    resource: "https://arxiv.org/abs/2508.11062"
    title: "Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. https://arxiv.org/abs/2508.11062"
    author: Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer
---

# Four-pipeline adaptive tutoring system with RAG and feedback tagging

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A "modular web service built on Flask and MongoDB, augmented by a four-pipeline query manager". Pipelines are Personalized + Feedback (metadata plus live tags), Personalized (onboarding metadata only), RAG (top ten textbook passages, cosine-similarity ≥ 0.8), and LLM (direct call). An onboarding questionnaire captures "Ruby/OOP experience, preferred learning style, common design challenges, and personal goals"; inline buttons offer five predefined feedback tags recorded in real time.

## Design Implications

### Context
#### Requirements
- A unified prompt template "to ensure a fair comparison across all four pipelines", instructing the model to answer only from provided textbook excerpts and conversation history
#### Constraints
- Evaluation was "confined to a single textbook domain" and relied on a GPT-based evaluator, "which may introduce both topical and evaluator bias"

### Target Learners
- STEM students in computer science courses

### Learning Goals
- Object-Oriented Design problem solving
- personalized explanation of course concepts

### Claims
- [Rag Grounding Near Perfect Correctness](../claims/rag-grounding-near-perfect-correctness.md) [+M]
- [Static Onboarding Metadata Highest Adaptability](../claims/static-onboarding-metadata-highest-adaptability.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. https://arxiv.org/abs/2508.11062
