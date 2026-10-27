---
type: strategy
id: reference-solution-latex-prompting-strategy
title: Include the official reference solution in the LLM prompt and convert solutions to LaTeX to bypass image-recognition limits
description: "Because state-of-the-art LLMs and VLMs cannot reliably interpret circuit diagrams or handwritten solution images, the article's workflow converts both official and student solutions to LaTeX with the Mathpix snipping..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: liangliang-chen-2025
    resource: "https://doi.org/10.1007/s40593-025-00501-w"
    title: "Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang. (2025). Benchmarking Large Language Models on Homework Assessment in Circuit Analysis. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00501-w"
    author: Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang
---

# Include the official reference solution in the LLM prompt and convert solutions to LaTeX to bypass image-recognition limits

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (2 design, 1 associational), `q1`–`q2` · 1 of 3 report an effect size · 3 claims rest on one study

## Description
Because state-of-the-art LLMs and VLMs cannot reliably interpret circuit diagrams or handwritten solution images, the article's workflow converts both official and student solutions to LaTeX with the Mathpix snipping tool and includes the official reference solution directly in the prompt, "bypassing the need for LLMs to interpret circuit diagrams." A structured prompt template then asks the LLM to assess five metrics: completeness, method, final answer, arithmetic error, and units.

## Design Implications

### Context
#### Requirements
- Access to official reference solutions with final answers
- Conversion of handwritten and typed solutions to LaTeX (e.g., via the Mathpix snipping tool)
- A prompt template specifying the five assessment metrics and error-handling notes
#### Constraints
- Not applicable to problems requiring assessment of circuit diagrams or Bode plots, which the article excludes due to limited image-recognition capacity
- Reliability depends on the quality of the LaTeX conversion

### Target Learners
- undergraduate electrical engineering students

### Target Learning Goals
- reliable automated feedback on homework solutions in circuit analysis

## Claims

- [State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems](../claims/vlm-cannot-interpret-circuit-diagrams.md) [+W]
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](../claims/ai-systems-misinterpret-stem-diagrams.md) [+W]
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](../claims/multimodality-size-reasoning-mixed-effects.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang. (2025). Benchmarking Large Language Models on Homework Assessment in Circuit Analysis. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00501-w
