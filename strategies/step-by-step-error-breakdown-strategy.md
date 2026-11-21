---
type: strategy
id: step-by-step-error-breakdown-strategy
title: Guide students through step-by-step error breakdowns instead of presenting correct answers
description: The authors recommend that AI tutoring systems analyze the causes of student errors rather than only retrieving answers.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zhoumingju-jiang-2024
    resource: "https://dl.acm.org"
    title: "Zhoumingju Jiang, Mengjun Jiang. (2024). Beyond Answers: LLM-Powered Tutoring System in Physics Education for Deep Learning and Precise Understanding. ACM, New York, NY, USA. https://dl.acm.org"
    author: Zhoumingju Jiang, Mengjun Jiang
---

# Guide students through step-by-step error breakdowns instead of presenting correct answers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The authors recommend that AI tutoring systems analyze the causes of student errors rather than only retrieving answers. They propose that "instead of simply presenting the correct answer, AI could guide students through a step-by-step breakdown of their errors, highlighting misconceptions and providing explanations that reinforce conceptual understanding." Systems should also prompt students to reflect on why an answer is correct or incorrect, turning mistakes into learning moments. This is the design rationale behind Physics-STAR's error-analysis step.

## Design Implications

### Context
#### Requirements
- the LLM must receive a description of the student's problem-solving process with errors as prompt input
#### Constraints
- recommended for conceptually demanding subjects such as physics; the article presents it as a design direction, not a separately tested feature

### Target Learners
- high school physics students

### Target Learning Goals
- understanding and correcting mistakes
- developing critical thinking and reflective practice

## Claims

- [Physics-STAR LLM tutoring produced higher post-test scores on information-based physics questions than generic LLM tutoring or teacher lecture](../claims/physics-star-higher-information-question-scores.md) [+W]
- [Physics-STAR tutoring reduced time spent on information-based questions relative to the other two tutoring methods](../claims/physics-star-reduced-information-question-time.md) [+W]

## Related Strategies

- [Questioning Techniques to Address Errors](questioning_techniques_to_address_errors.md)
- [Design learning-oriented LLM prompts around guided questions, step-by-step support, reflection, and a thinking partner rather than direct answers](learning-oriented-llm-prompt-strategy.md)
- [Behavioral Feedback for Correct and Incorrect Responses](behavioral-feedback-for-responses.md)
- [Adapt the grading system to rate explanation quality and detected errors, exchanging two unassisted problems for four worked examples](grade-worked-example-explanations-and-error-detection.md)

## Examples
-

## Key Sources
- Zhoumingju Jiang, Mengjun Jiang. (2024). Beyond Answers: LLM-Powered Tutoring System in Physics Education for Deep Learning and Precise Understanding. ACM, New York, NY, USA. https://dl.acm.org
