---
type: design
id: structured-form-based-prompting-interface-chatgpt
title: Structured form-based prompting interface with integrated ChatGPT API
description: A structured interface built on the ChatGPT API that acts as a reflective layer for prompting during programming labs.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: brender-2025
    resource: "https://arxiv.org/abs/2507.07767v2"
    title: "Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. https://arxiv.org/abs/2507.07767v2"
    author: Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E
---

# Structured form-based prompting interface with integrated ChatGPT API

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A structured interface built on the ChatGPT API that acts as a reflective layer for prompting during programming labs. Students first select a prompt category (Understanding, Implementing, or Debugging), then complete a structured form that decomposes the prompt into blank-based fields; the fields are compiled into a single prompt sent to the GPT model. The article states the interface did not alter or constrain the underlying knowledge base of the GPT model, and that it was designed to encourage metacognitive engagement by having students reflect on and refine their own prompts.

## Design Implications

### Context
#### Requirements
- Students must select a prompt category and complete the structured form fields before a prompt is submitted to the ChatGPT API.
#### Constraints
- The interface did not alter or constrain the underlying knowledge base of the GPT model.
- Two intervention sessions were not sufficient for students to adopt new behaviors, per the authors.

### Target Learners
- graduate-level university students in robotics/computing courses

### Learning Goals
- productive LLM prompting behaviors
- conceptual understanding of robotics algorithms

### Claims
- [Structured Interface Clear Development Prompts No Transfer](../claims/structured-interface-clear-development-prompts-no-transfer.md) [+M]
- [Structured Prompting Interface No Learning Performance Difference](../claims/structured-prompting-interface-no-learning-performance-difference.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. https://arxiv.org/abs/2507.07767v2. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)
