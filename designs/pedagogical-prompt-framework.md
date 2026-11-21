---
type: design
id: pedagogical-prompt-framework
title: "Pedagogical prompting: a theoretically grounded framework of prompts that direct LLMs to act as tutors"
description: "Pedagogical prompting is a concept for crafting prompts that guide LLMs to \"act as a tutor and generate responses that facilitate suitable learning activities aligned with the learner's current stage\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: ruiwei-xiao-2025
    resource: "https://arxiv.org/abs/2506.19107"
    title: "Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper. (2025). Improving Student-AI Interaction Through Pedagogical Prompting: An Example in Computer Science Education. arXiv preprint. https://arxiv.org/abs/2506.19107"
    author: Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper
---

# Pedagogical prompting: a theoretically grounded framework of prompts that direct LLMs to act as tutors

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
Pedagogical prompting is a concept for crafting prompts that guide LLMs to "act as a tutor and generate responses that facilitate suitable learning activities aligned with the learner's current stage". A pedagogical prompt has six essential components in two categories: a learning context of five components (AI's role, learner's level, problem context, challenge articulation, guardrails) and a learner-instructed tutoring protocol. The tutoring protocol choice should be aligned with the student's current learning context and supported by learning science frameworks such as KLI. The concept was instantiated in early undergraduate CS education as a proof-of-concept.

## Design Implications

### Context
#### Requirements
- The learner must specify the five learning context components and a tutoring protocol for the prompt to be well-formed
#### Constraints
- The article's implementation is scoped to early undergraduate CS education; the concept is described as broadly applicable but only this context was evaluated

### Target Learners
- early undergraduate CS novices (CS1/CS2)

### Learning Goals
- learning-oriented LLM-based help-seeking and prompt writing

### Claims
- [Pedagogical Prompting Intervention Improves Prompt Writing](../claims/pedagogical-prompting-intervention-improves-prompt-writing.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper. (2025). Improving Student-AI Interaction Through Pedagogical Prompting: An Example in Computer Science Education. arXiv preprint. https://arxiv.org/abs/2506.19107
