---
type: design
id: physics-star-framework
title: "Physics-STAR: a STAR-structured prompt framework guiding LLM tutoring in three personalized steps"
description: Physics-STAR is a prompt-engineering framework that structures LLM inputs for personalized physics tutoring.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: zhoumingju-jiang-2024
    resource: "https://dl.acm.org"
    title: "Zhoumingju Jiang, Mengjun Jiang. (2024). Beyond Answers: LLM-Powered Tutoring System in Physics Education for Deep Learning and Precise Understanding. ACM, New York, NY, USA. https://dl.acm.org"
    author: Zhoumingju Jiang, Mengjun Jiang
---

# Physics-STAR: a STAR-structured prompt framework guiding LLM tutoring in three personalized steps

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Physics-STAR is a prompt-engineering framework that structures LLM inputs for personalized physics tutoring. It "draw[s] on the Situation-Task-Action-Result(STAR) approach" and "provides an adaptable structure for LLM input in three steps of personalized tutoring": knowledge explanation, error analysis, and review suggestion. Each step's prompt has four sections (situation, task, action, result), and the review-suggestion loop repeats error analysis and review when students fail similar-question checks. The framework was implemented with GPT-4o and evaluated against teacher lecture and generic LLM tutoring.

## Design Implications

### Context
#### Requirements
- LLM inputs must be structured as situation, task, action, and result sections for each of the three tutoring steps
- students engage in question-and-answer sessions with the tutoring system according to the provided prompts
#### Constraints
- evaluated only with GPT-4o and twelve high school sophomores reviewing gravity and spaceflight content

### Target Learners
- high school physics students

### Learning Goals
- precise understanding of physics concepts
- learning from mistakes
- applying mathematical models to solve problems

### Claims
- [Physics Star Higher Information Question Scores](../claims/physics-star-higher-information-question-scores.md) [+M]
- [Physics Star Reduced Information Question Time](../claims/physics-star-reduced-information-question-time.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhoumingju Jiang, Mengjun Jiang. (2024). Beyond Answers: LLM-Powered Tutoring System in Physics Education for Deep Learning and Precise Understanding. ACM, New York, NY, USA. https://dl.acm.org
