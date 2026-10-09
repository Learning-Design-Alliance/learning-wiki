---
type: theory
title: Dependence-based image-role taxonomy for visual math items
description: "The article operationalizes a four-code taxonomy of image roles in math problems: REQUIRED, USEFUL, NOTREQUIRED, and INSUFFICIENT."
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

# Dependence-based image-role taxonomy for visual math items

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article operationalizes a four-code taxonomy of image roles in math problems: REQUIRED, USEFUL, NOTREQUIRED, and INSUFFICIENT. An item is REQUIRED when "At least one task-critical quantity, relation, label, or structural constraint is present only in the image and cannot be recovered from the text alone without inventing information"; USEFUL items are solvable from text with a redundant-but-helpful figure. A conservative flag-then-review refinement downgraded six items, yielding 376 Required items of 541 image-containing items (69.5%). An independent second-rater audit (n=153) yielded 88.2% agreement with Cohen's κ=0.764 on the Required-vs-non-Required boundary.

## Design Implications

### Context
#### Requirements
- A frozen operational codebook applied before reliability auditing, with decision rules documented and disagreements reported via confusion matrices
#### Constraints
- Image-role labeling necessarily involves judgment; labels are treated as operational categories rather than objective ground truth, and disagreements concentrated near the Required–Useful boundary

### Target Learners
- middle-school mathematics students (Grades 6–8)

### Target Learning Objectives
- determining which math problems require visual information for a unique solution

### Claims

- [Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items](../claims/mllms-refuse-without-required-figures.md) [+W]
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](../claims/moderate-cross-model-agreement-solvability.md) [+W]
- [With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models](../claims/reasoning-mllms-higher-accuracy-image-required-math.md) [+W]
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](../claims/visual-misread-dominant-non-reasoning-failure.md) [+W]

## Related Theories
- 

## Examples

- [Gold and ultra-gold benchmark subsets of consistently solved image-Required items](../elements/gold-ultra-gold-benchmark-subsets.md)
- [Use refusal-first behavior and description-substitution experiments to support accessible visual math](../strategies/refusal-first-description-substitution-accessibility.md)

## Key Sources
- Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/
