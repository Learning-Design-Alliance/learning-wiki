---
type: design
id: dimensional-analysis-symbolic-regression-prompting-framework
title: Dimensional-analysis-guided symbolic regression via staged prompt engineering as a learning mechanism
description: "The article's organising framework treats symbolic regression — finding a human-readable formula fitting input-output data — as a learning activity, with dimensional analysis constraining the LLM's search to physicall..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: yufan-zhu-2024
    resource: "https://arxiv.org/abs/2407.00065"
    title: "Yufan Zhu, Zi-Yu Khoo, Jonathan Sze Choong Low, Stéphane Bressan. (2024). A Personalised Learning Tool for Physics Undergraduate Students Built On a Large Language Model for Symbolic Regression. arXiv preprint. https://arxiv.org/abs/2407.00065"
    author: Yufan Zhu, Zi-Yu Khoo, Jonathan Sze Choong Low, Stéphane Bressan
---

# Dimensional-analysis-guided symbolic regression via staged prompt engineering as a learning mechanism

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's organising framework treats symbolic regression — finding a human-readable formula fitting input-output data — as a learning activity, with dimensional analysis constraining the LLM's search to physically meaningful expressions. Four prompting variants cross single-stage versus multi-stage prompting with general dimensional analysis versus Rayleigh's Method, in which a dependent variable is expressed as a power product of independent variables with exponents solved by dimensional homogeneity. The framework motivates the tool as letting students "infer and understand the underlying principles from empirical data".

## Design Implications

### Context
#### Requirements
- Prompts must supply regressors and response variables with their dimensions, plus a dataset of variable values
- Rayleigh variants require formulating the equation as a power product and solving for dimensionally homogeneous exponents
#### Constraints
- Symbolic regression is an NP-hard problem, requiring a complex search through an extensive space of mathematical expressions
- Single-stage prompting efficacy can be sensitive to the selection of exemplars

### Target Learners
- undergraduate physics students

### Learning Goals
- data-driven and exploratory understanding of physics laws
- qualitative reasoning about physical quantities

### Claims
- [Single Stage Rayleigh Fewer Prompts](../claims/single-stage-rayleigh-fewer-prompts.md) [+M]
- [Dimensional Analysis Prompting Good Accuracy](../claims/dimensional-analysis-prompting-good-accuracy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yufan Zhu, Zi-Yu Khoo, Jonathan Sze Choong Low, Stéphane Bressan. (2024). A Personalised Learning Tool for Physics Undergraduate Students Built On a Large Language Model for Symbolic Regression. arXiv preprint. https://arxiv.org/abs/2407.00065
