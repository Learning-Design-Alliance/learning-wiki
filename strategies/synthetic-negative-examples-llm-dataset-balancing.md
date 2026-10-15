---
type: strategy
id: synthetic-negative-examples-llm-dataset-balancing
title: Generate synthetic negative explanations with a small language model to balance imbalanced educational scoring datasets
description: To address class imbalance without oversampling techniques that require numerical features, the authors prompted a small language model (GPT-OSS 20b, chosen because it differs from the assessment model) to generate th...
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

# Generate synthetic negative explanations with a small language model to balance imbalanced educational scoring datasets

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To address class imbalance without oversampling techniques that require numerical features, the authors prompted a small language model (GPT-OSS 20b, chosen because it differs from the assessment model) to generate three distinct incorrect explanations for each code line. Verification showed quality: sampling 100 generated explanations, two annotators "confirmed that at least 95% of the sample had incorrect explanations with an agreement of 91%". Distributional comparison of similarity scores confirmed the negatives resembled authentic student errors.

## Design Implications

### Context
#### Requirements
- A generation model distinct from the assessment model
- Human annotation verification of generated negatives
#### Constraints
- Verification was brief: a sample of 100 explanations with 2 annotators; the authors call for more extensive pedagogical evaluation focused on student misconceptions

### Target Learners
- Novice programming students

### Target Learning Goals
- Automated assessment of student self-explanations

## Related Strategies

- [Define correctness explicitly in LLM-as-a-judge prompts, offering behavior-focused and construction-focused rubric variants](llm-judge-correctness-definition-prompts.md)
- [Use knowledge distillation with deliberately limited synthetic data to expand scarce labeled evaluation datasets](limited-distillation-for-scarce-evaluation-labels.md)

## Examples
-

## Key Sources
- Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614
