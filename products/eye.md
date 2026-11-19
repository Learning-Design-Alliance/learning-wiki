---
type: product
id: eye
title: Eye
description: Eye is an interactive visual interpreter developed by Aman Bansal and colleagues that runs in a web browser to show C++ execution, call stacks, data-structure states, and operation steps for CS2 learners.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Eye

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Eye is an interactive visual interpreter developed by Aman Bansal and colleagues that runs in a web browser to show C++ execution, call stacks, data-structure states, and operation steps for CS2 learners.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Three-module architecture with Canonical Code and Graphics Representations**: Eye's implementation is divided into three independent modules connected by two intermediate representations. Module 1 parses source code into an abstract syntax tree; Module 2 executes the AST and emits a Canonical Graphics Representation in JSON, including program-aware features; Module 3 renders CGR in HTML5, CSS, and JavaScript with next/previous frame buttons. The article defines that "Canonical Code Representation (CCR): It represents the source code in a format that is language independent", which lets new languages be added by changing only module 1, and CGR decouples graphics from execution so instructors can modify the display. (Aman Bansal et al. (2021))
- **Six design properties for adoptable program visualization tools (P1-P6)**: The article enumerates six properties it argues any visualization tool needs for widespread adoption: completeness (CS2 data-structure coverage), flexibility (modifiable display beyond CSS), awareness (program-aware features like explanatory text and variable scoping), accessibility (runs in a web browser), modularity (new languages with minimal back-end changes), and interactivity (moving back and forth through frames). The article asserts "It should be interactive, allowing the beginners to go back and forth as per their convenience" and shows Eye satisfies all six in a comparison table against Jeliot 3, jGRASP, Jsvee, Python Tutor, UUhistle, and ViLLE. (Aman Bansal et al. (2021))

### Claims
- [Using Eye for debugging data-structure programs reduces the fraction of debug time spent on a problem, with a marginal p-value of 0.0578](../claims/eye-reduces-debug-time-fraction.md) [+W]
- [Using Eye to understand new code did not significantly improve quiz comprehension scores in a fixed time (p = 0.446)](../claims/eye-comprehension-quiz-not-significant.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Aman Bansal, Preey Shah, and Sahil Shah. (2021). Eye: Program Visualizer for CS2. arXiv preprint. https://arxiv.org/abs/2101.12089
