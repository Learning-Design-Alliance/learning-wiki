---
type: strategy
id: refusal-first-description-substitution-accessibility
title: Use refusal-first behavior and description-substitution experiments to support accessible visual math
description: "For accessibility, the article recommends that systems \"elicit the missing figure (or a structured textual description) rather than speculate\" when a required image is unavailable."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: croteau-2026
    resource: "https://osf.io/ct7bg/"
    title: "Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/"
    author: "Croteau, E., & Heffernan, N"
---

# Use refusal-first behavior and description-substitution experiments to support accessible visual math

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For accessibility, the article recommends that systems "elicit the missing figure (or a structured textual description) rather than speculate" when a required image is unavailable. The released gold and ultra-gold subsets are proposed as "an ideal testbed for textual description substitution", where randomized comparisons of vetted human descriptions versus original figures could measure effects on accuracy, stability, and refusal rates, with input from blind or low-vision users. A follow-up direction is exploring whether model-generated alt text approaches human quality.

## Design Implications

### Context
#### Requirements
- Access to vetted human (or model-assisted) textual descriptions that preserve task-relevant visual structure, and logging of accuracy, stability, and refusal under substitution
#### Constraints
- The article did not itself explore alt-text generation, scaffolding prompts, or human-LLM collaboration, naming these as future work

### Target Learners
- blind or low-vision middle-school mathematics students

### Target Learning Goals
- accessing image-dependent middle-school math problems through alternative representations

## Related Strategies
- 

## Examples
-

## Key Sources
- Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/
