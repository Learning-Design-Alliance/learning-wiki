---
type: design
id: three-question-types-legal-concepts
title: Three question types for assessing legal concept understanding
description: "Inspired by pedagogical research on cognitive learning aspects, the authors create three question types for assessing learners' understanding: concept questions for definition understanding, prediction questions for a..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: hang-jiang-2024
    resource: "https://arxiv.org/abs/2402.17019"
    title: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. https://arxiv.org/abs/2402.17019"
    author: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara"
---

# Three question types for assessing legal concept understanding

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Inspired by pedagogical research on cognitive learning aspects, the authors create three question types for assessing learners' understanding: concept questions for definition understanding, prediction questions for applying the concept to scenarios, and limitation questions for evaluating and analyzing the concept's shortcomings. Each type is generated as a multiple-choice question with a suggested answer and explanation, conditioned on the concept, definition, and story.

## Design Implications

### Context
#### Requirements
- Questions conditioned on corresponding concept, definition, and story
- Expert critique to verify answerability and correctness
#### Constraints
- Limitation questions are challenging for LLMs to generate because not all concepts have apparent limitations or exceptions; they receive lower quality ratings

### Target Learners
- legal novices

### Learning Goals
- definition understanding
- application to scenarios
- evaluating concept limitations

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. https://arxiv.org/abs/2402.17019
