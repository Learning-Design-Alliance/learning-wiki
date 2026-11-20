---
type: design
id: llm-dimensional-analysis-physics-learning-tool
title: LLM-based personalised learning tool for undergraduate physics using dimensional-analysis-guided symbolic regression
description: The article introduces a personalised learning tool built on a Large Language Model that supports students completing homework with problems interleaved from undergraduate physics courses.
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

# LLM-based personalised learning tool for undergraduate physics using dimensional-analysis-guided symbolic regression

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article introduces a personalised learning tool built on a Large Language Model that supports students completing homework with problems interleaved from undergraduate physics courses. It "leverages the dimensional analysis method", combining LLMs for symbolic regression with dimensional analysis via prompt engineering, so students can infer relationships between physics variables from data rather than only applying established equations. The tool was implemented with GPT-4 and a Wolfram Alpha Plugin and evaluated on 26 equations from the Feynman Lectures.

## Design Implications

### Context
#### Requirements
- An LLM (GPT-4) with a computational plugin (Wolfram Alpha Plugin) to perform the mathematical and symbolic operations needed for coefficient regression
#### Constraints
- Variables are obfuscated with generic names to prevent the model from relying on prior physics knowledge
- Evaluated only on equations from the Feynman Lectures that are solvable by dimensional analysis

### Target Learners
- undergraduate physics students

### Learning Goals
- qualitative thinking and problem-solving for complex physical phenomena
- understanding relationships between physics variables

### Claims
- [Two Stage Rayleigh Highest Success Rate](../claims/two-stage-rayleigh-highest-success-rate.md) [+M]
- Llm Methods Faster Than Ai Feynman [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yufan Zhu, Zi-Yu Khoo, Jonathan Sze Choong Low, Stéphane Bressan. (2024). A Personalised Learning Tool for Physics Undergraduate Students Built On a Large Language Model for Symbolic Regression. arXiv preprint. https://arxiv.org/abs/2407.00065
