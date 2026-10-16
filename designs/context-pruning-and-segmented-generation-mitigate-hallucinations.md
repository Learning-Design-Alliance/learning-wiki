---
type: design
id: context-pruning-and-segmented-generation-mitigate-hallucinations
title: Mitigate LLM hallucinations in material generation by drastic context pruning and segmented, section-by-section generation rather than single-prompt deck generation
description: The architecture keeps only a condensed three-paragraph context summary carried forward, plans structure without code, and generates LaTeX and Python section by section in an iterative loop.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
sources:
  - id: henrique-mohallem-paiva-2026
    resource: "https://arxiv.org/abs/2608.07364"
    title: "Henrique Mohallem Paiva. (2026). Curriculum as Code: An AI-Assisted Architecture for Instructional Design in STEM Education. https://arxiv.org/abs/2608.07364"
    author: Henrique Mohallem Paiva
---

# Mitigate LLM hallucinations in material generation by drastic context pruning and segmented, section-by-section generation rather than single-prompt deck generation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The architecture keeps only a condensed three-paragraph context summary carried forward, plans structure without code, and generates LaTeX and Python section by section in an iterative loop. The article reports that "attempting to generate a full slide deck in a single prompt inevitably leads to token exhaustion and hallucinations", while feeding the model only isolated sections alongside a condensed summary kept attention focused and yielded accurate code outputs. Restricting the human-AI interface to plain text, Markdown, and source code further avoids formatting glitches.

## Design Implications

### Context
#### Requirements
- A Phase 1 condensed text summary as the only context carried into code generation, a structural skeleton produced before any code, and an automated secondary review agent plus human-in-the-loop validation
#### Constraints
- Generative models may show behavioral drift after provider updates, occasionally requiring minor prompt recalibrations; minor syntactic anomalies such as mismatched brackets still occur

### Target Learners
- Instructors and instructional designers producing STEM materials

### Learning Goals
- Production of mathematically accurate, visually consistent instructional materials

### Claims
- [No Conceptual Hallucinations 28 Contexts](../claims/no-conceptual-hallucinations-28-contexts.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Henrique Mohallem Paiva. (2026). Curriculum as Code: An AI-Assisted Architecture for Instructional Design in STEM Education. https://arxiv.org/abs/2608.07364
