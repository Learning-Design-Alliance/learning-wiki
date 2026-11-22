---
type: strategy
id: expert-in-loop-llm-education-pipeline
title: Expert-in-the-loop pipeline for generating and refining educational content with LLMs
description: A human-in-the-loop pipeline combining LLM and expert input to generate stories and multiple-choice questions.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: hang-jiang-2024
    resource: "https://arxiv.org/abs/2402.17019"
    title: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. https://arxiv.org/abs/2402.17019"
    author: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara"
---

# Expert-in-the-loop pipeline for generating and refining educational content with LLMs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A human-in-the-loop pipeline combining LLM and expert input to generate stories and multiple-choice questions. Legal experts read concepts and stories, answer questions, and provide critiques; these suggestions are then used to prompt LLMs to improve the content. After one round of regeneration with expert advice, revised questions were 100% approved by experts, demonstrating the effectiveness of instructing GPT-4 with expert advice to revise questions.

## Design Implications

### Context
#### Requirements
- Legal experts to evaluate question quality, answer correctness, and provide improvement suggestions
- LLM capable of incorporating expert feedback in regeneration
#### Constraints
- Experts take around 6.5 minutes per concept to evaluate and write feedback, which may limit scalability

### Target Learners
- legal novices

### Target Learning Goals
- comprehension assessment of legal concepts

## Claims

- [Expert-in-the-loop revision substantially improves medical accuracy and educational quality of generated storylines](../claims/expert-revision-improves-generated-medical-storylines.md) [+W]

## Related Strategies

- [Human-in-the-loop validation workflow: hold all AI-generated teaching content in unreviewed status until a teacher manually approves it](human-in-the-loop-teacher-validation-workflow.md)
- [Use independent expert physician review as a governance safeguard before deploying LLM-generated questions to learners](expert-physician-review-governance.md)
- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)
- [Hybrid LLM translation with human-in-the-loop expert validation for onboarding documentation](hybrid-llm-human-translation-strategy.md)

## Examples
-

## Key Sources
- Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. https://arxiv.org/abs/2402.17019
