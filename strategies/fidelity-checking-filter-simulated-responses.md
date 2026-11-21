---
type: strategy
id: fidelity-checking-filter-simulated-responses
title: Use a fidelity checking model to filter and regenerate outlier simulated responses before IRT fitting
description: "The article recommends adding a fidelity checking stage to the simulation pipeline: when the student simulator produces degenerate outputs such as passage repetition or irrelevant text, a checking model filters them o..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: alexander-scarlatos-2025
    resource: "https://arxiv.org/abs/2507.05129"
    title: "Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. https://arxiv.org/abs/2507.05129"
    author: Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan
---

# Use a fidelity checking model to filter and regenerate outlier simulated responses before IRT fitting

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends adding a fidelity checking stage to the simulation pipeline: when the student simulator produces degenerate outputs such as passage repetition or irrelevant text, a checking model filters them out and regeneration is triggered. This addresses the observed problem that "These outlier responses are often inaccurately scored by the scoring model, affecting downstream item difficulty prediction." The strategy targets simulation-based difficulty calibration workflows.

## Design Implications

### Context
#### Requirements
- A trained fidelity checking model capable of detecting degenerate or irrelevant generated responses
- A regeneration mechanism in the simulation loop
#### Constraints
- Proposed as a possible solution in future work; not evaluated in the current experiments

### Target Learners
- assessment developers calibrating open-ended items

### Target Learning Goals
- reliable automated item difficulty estimation

## Claims

- [SMART occasionally generates outlier responses with fidelity issues that are inaccurately scored and hurt difficulty prediction](../claims/smart-outlier-responses-fidelity-issues.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. https://arxiv.org/abs/2507.05129
