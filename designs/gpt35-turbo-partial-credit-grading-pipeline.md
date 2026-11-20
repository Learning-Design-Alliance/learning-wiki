---
type: design
id: gpt35-turbo-partial-credit-grading-pipeline
title: GPT-3.5 Turbo AI grading pipeline with three prompt versions (Naive, Detailed-rubric, Scaffolded COT)
description: The system is a GPT-3.5 Turbo deployment in completion mode, accessed via the Microsoft Azure platform through the LangChain AzureOpenAI python API, with all data kept on university-owned secure servers.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics"
    author: Zhongzhou Chen and Tong Wan
---

# GPT-3.5 Turbo AI grading pipeline with three prompt versions (Naive, Detailed-rubric, Scaffolded COT)

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The system is a GPT-3.5 Turbo deployment in completion mode, accessed via the Microsoft Azure platform through the LangChain AzureOpenAI python API, with all data kept on university-owned secure servers. The article develops and tests three prompt versions — "Naïve COT", "Detailed-rubric COT", and "Scaffolded COT" — each with identical contextual information, general grading instructions, and problem statement components but different rubric and grading-requirement components. It grades student explanations on a three-item binary rubric for a water-slide conceptual question.

## Design Implications

### Context
#### Requirements
- Rubric items with binary 1/0 ratings, evaluated on percent agreement, mean simple matching distance, and quadratic weighted kappa against human raters
#### Constraints
- The study tested one physics conceptual problem and only explanations from students who answered the multiple-choice question incorrectly (N = 40)

### Target Learners
- undergraduate students in a 99-enrollment calculus-based introductory physics course

### Learning Goals
- automated partial-credit grading of written explanations to reduce instructor and teaching-assistant grading load in large-enrollment courses

### Claims
- [Scaffolded Cot Human Level Agreement Gpt35 Grading](../claims/scaffolded-cot-human-level-agreement-gpt35-grading.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics
