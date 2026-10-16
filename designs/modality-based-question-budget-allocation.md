---
type: design
id: modality-based-question-budget-allocation
title: Modality-based question budget allocation favoring mechanism slides over structural slides
description: The system allocates a bounded question budget per slide based on detected modality and pedagogical role.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: salsman-2026
    resource: "https://arxiv.org/abs/2605.26428"
    title: "Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428"
    author: Salsman, J
---

# Modality-based question budget allocation favoring mechanism slides over structural slides

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The system allocates a bounded question budget per slide based on detected modality and pedagogical role. The window planner prompt instructs: "Favor low budgets for title , agenda , transition , administrative , appendix , and r epe at ed recap slides ." and "Favor higher budgets for rich mechanism , comparison , result , diagram , chart , table , or s y n t h e s i s slides ." Budgets range from 0 to 5, and zero questions are explicitly acceptable, so generation effort concentrates on core pedagogical material.

## Design Implications

### Context
#### Requirements
- Slide modality types and deck roles must be drawn from the fixed label vocabularies defined in the window planner prompt
#### Constraints
- Budgets are capped between 0 and 5 per slide, though the deck synthesis prompt notes some slides may deserve more than three questions

### Target Learners
- undergraduate and graduate students in technical lecture courses

### Learning Goals
- balanced question coverage aligned with instructional importance across heterogeneous slide types

### Claims
- [Reconciliation Zero Budgets Structural Slides](../claims/reconciliation-zero-budgets-structural-slides.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428. [doi:10.48550/arxiv.2605.26428](https://doi.org/10.48550/arxiv.2605.26428)
