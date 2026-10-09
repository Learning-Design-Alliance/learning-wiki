---
type: element
id: gold-ultra-gold-benchmark-subsets
title: Gold and ultra-gold benchmark subsets of consistently solved image-Required items
description: "The article identifies and releases two reproducible benchmark subsets of image-Required items: \"61ultra-golditems solved 3/3 by all six models and 76golditems solved by all six at majority-correct\"."
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

# Gold and ultra-gold benchmark subsets of consistently solved image-Required items

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article identifies and releases two reproducible benchmark subsets of image-Required items: "61ultra-golditems solved 3/3 by all six models and 76golditems solved by all six at majority-correct". These subsets support future diagnostics and comparisons beyond single-shot accuracy, and the authors propose them as a testbed for description-substitution experiments comparing original figures to vetted textual descriptions while monitoring accuracy, stability, and refusal. Code, prompts, and summary artifacts are released at the stated OSF link.

## Design Implications

### Context
#### Requirements
- Items must be from the final Required set and evaluated under the shared prompt and scoring protocol with three runs per condition
#### Constraints
- Subsets derive from a single curriculum (Illustrative Mathematics Grades 6–8) and current model checkpoints, which the authors note are evolving rapidly

### Target Learners
- middle-school mathematics students (Grades 6–8)

### Target Learning Goals
- image-dependent middle-school mathematics problem solving

## Claims

- [Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items](../claims/mllms-refuse-without-required-figures.md) [+W]
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](../claims/moderate-cross-model-agreement-solvability.md) [+W]
- [With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models](../claims/reasoning-mllms-higher-accuracy-image-required-math.md) [+W]
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](../claims/visual-misread-dominant-non-reasoning-failure.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/
