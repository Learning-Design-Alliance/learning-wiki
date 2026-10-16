---
type: strategy
id: cot-fewshot-selfconsistency-student-guidance
title: Guide student instruction with chain-of-thought decomposition, few-shot worked examples, and self-consistency over multiple LLM queries
description: To help students instruct the LLM effectively, the methodology applies three established prompting principles.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: xinming-yang-2025
    resource: "https://arxiv.org/abs/2508.05979"
    title: "Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979"
    author: Xinming Yang, Haasil Pujara, Jun Li
---

# Guide student instruction with chain-of-thought decomposition, few-shot worked examples, and self-consistency over multiple LLM queries

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (2 causal), `q2`–`q3` · 1 of 2 report an effect size · 2 claims rest on one study

## Description
To help students instruct the LLM effectively, the methodology applies three established prompting principles. Students are guided to structure answers "as a series of simple, sequential steps for the LLM to follow" (CoT, including the phrase "let's think step by step"), to provide "several examples of test cases with corresponding input-output pairs" with step-by-step solutions (few-shot), and the system applies self-consistency: "a student's prompt is sent to the LLM multiple times," with success requiring the number of correct outputs to meet a predefined threshold.

## Design Implications

### Context
#### Requirements
- Students must learn to structure instructions, since less-capable, more affordable LLMs are used and students can be frustrated when prompts they think are sufficient fail
#### Constraints
- A well-designed prompt can still produce an incorrect result due to the probabilistic nature of the model, which self-consistency mitigates but does not eliminate

### Target Learners
- undergraduate computer science students

### Target Learning Goals
- problem decomposition and procedural thinking; distinguishing LLM variability from flaws in one's own instructions

## Claims

- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](../claims/cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) [+W]
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](../claims/few-shot-prompting-no-f1-gain-reduces-overattribution.md) [~W]

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)

## Examples
-

## Key Sources
- Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979
