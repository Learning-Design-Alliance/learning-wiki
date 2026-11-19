---
type: strategy
id: eye-deployment-integration-strategy
title: Deploy program visualizers via online-judge IDE integration and extend to more languages and data structures
description: "The authors recommend extending Eye's reach by integrating it into online programming websites and adding visualizations for more data structures and libraries in languages like Python and Java."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: aman-bansal-2021
    resource: "https://arxiv.org/abs/2101.12089"
    title: "Aman Bansal, Preey Shah, and Sahil Shah. (2021). Eye: Program Visualizer for CS2. arXiv preprint. https://arxiv.org/abs/2101.12089"
    author: Aman Bansal, Preey Shah, and Sahil Shah
---

# Deploy program visualizers via online-judge IDE integration and extend to more languages and data structures

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors recommend extending Eye's reach by integrating it into online programming websites and adding visualizations for more data structures and libraries in languages like Python and Java. They state that "extensive deployment on online programming websites can be done through integration with their IDEs (Integrated Development Environment) which requires a change in the display module." They also plan a formal study of teaching efficacy once classes reopen.

## Design Implications

### Context
#### Requirements
- Integration with online judges requires changes only in the display module thanks to the modular design
#### Constraints
- A formal study evaluating efficacy in teaching has not yet been conducted; the current evaluation covered debugging and comprehension only

### Target Learners
- Beginner programmers practicing on online programming websites

### Target Learning Goals
- Self-learning of coding, debugging, and understanding others' solutions

## Claims

- [Using Eye to understand new code did not significantly improve quiz comprehension scores in a fixed time (p = 0.446)](../claims/eye-comprehension-quiz-not-significant.md) [-W]
- [Using Eye for debugging data-structure programs reduces the fraction of debug time spent on a problem, with a marginal p-value of 0.0578](../claims/eye-reduces-debug-time-fraction.md) [+W]
- [Subjects estimated that debugging with Eye reduces frustration by 61.43% on average](../claims/eye-survey-frustration-reduction.md) [+W]

## Related Strategies
- Eye Program Visualizer Tool

## Examples
-

## Key Sources
- Aman Bansal, Preey Shah, and Sahil Shah. (2021). Eye: Program Visualizer for CS2. arXiv preprint. https://arxiv.org/abs/2101.12089
