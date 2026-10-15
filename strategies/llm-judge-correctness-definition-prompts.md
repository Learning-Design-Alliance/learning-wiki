---
type: strategy
id: llm-judge-correctness-definition-prompts
title: Define correctness explicitly in LLM-as-a-judge prompts, offering behavior-focused and construction-focused rubric variants
description: The LLM-as-a-judge approach prompts the model with the program description, the code line with its number, and the student explanation, asking only for a correctness judgment.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: arun-balajiee-lekshmi-narayanan-2026
    resource: "https://arxiv.org/abs/2605.21614"
    title: "Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614"
    author: Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky
---

# Define correctness explicitly in LLM-as-a-judge prompts, offering behavior-focused and construction-focused rubric variants

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The LLM-as-a-judge approach prompts the model with the program description, the code line with its number, and the student explanation, asking only for a correctness judgment. After manually reviewing 200 student explanations, the authors observed two explanation styles and "developed 3 versions of the LLM prompt, each with a different definition of correctness": No Definition, Construction (the line's role in solving the problem), and Code Behavior (the result of executing the line). The behavior-focused variant performed best.

## Design Implications

### Context
#### Requirements
- Prompt context including program description, line number, and student explanation
- Rubrics balancing instructor expectations and student understanding
#### Constraints
- The construction-focused definition underperformed on this dataset, whose explanations emphasized syntax and code behavior

### Target Learners
- Novice programming students

### Target Learning Goals
- Automated scoring of code self-explanations

## Related Strategies

- [Design CT rubrics and prompts to explicitly operationalize integrated constructs and demand parameter-interaction reasoning](explicit-rubrics-for-integrated-ct-constructs.md)
- [Generate synthetic negative explanations with a small language model to balance imbalanced educational scoring datasets](synthetic-negative-examples-llm-dataset-balancing.md)

## Examples
-

## Key Sources
- Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614
