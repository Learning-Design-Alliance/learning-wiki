---
type: design
id: its-prototype-genai-access-timing
title: Custom Intelligent Tutoring System integrating RL access control with an off-the-shelf Mistral LLM
description: A custom-built Intelligent Tutoring System hosted locally that integrates all procedural steps of the study except the distractor task.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: janne-rotter-2026
    resource: "https://arxiv.org/abs/2605.15850"
    title: "Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo. (2026). Access Timing as Scaffolding: A Reinforcement Learning Approach to GenAI in Education. https://arxiv.org/abs/2605.15850"
    author: Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo
---

# Custom Intelligent Tutoring System integrating RL access control with an off-the-shelf Mistral LLM

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A custom-built Intelligent Tutoring System hosted locally that integrates all procedural steps of the study except the distractor task. "It is implemented using an AngularJS architecture and deployed as a locally hosted web interface, which includes comprehensive logging functionalities for capturing all relevant interaction data." The GenAI available to participants was the Mistral 3 14B LLM accessed via the OpenRouter API, chosen partly for EU data-protection compliance. The system delivered three text-and-multiple-choice learning tasks on social media and self-image, adapted from tested NHS and Canadian digital-media-literacy workshops.

## Design Implications

### Context
#### Requirements
- Standardized laboratory computers and a fixed browser and screen resolution to mitigate confounds
- Comprehensive logging of AI requests, content, and task times
#### Constraints
- The ITS design builds significantly upon the system developed by Koch et al.

### Target Learners
- university students aged 18-39

### Learning Goals
- text comprehension of social media effects on self-image

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Janne Rotter, Pau Benazet i Montobbio, Davinia Hernández-Leo. (2026). Access Timing as Scaffolding: A Reinforcement Learning Approach to GenAI in Education. https://arxiv.org/abs/2605.15850
