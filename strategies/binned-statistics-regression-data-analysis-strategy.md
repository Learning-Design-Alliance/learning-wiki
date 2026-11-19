---
type: strategy
id: binned-statistics-regression-data-analysis-strategy
title: Teach binned statistics on irregular repeat data followed by least-squares regression as a gentle introduction to data analysis
description: The article recommends having students merge repeat data sets recorded at arbitrary values of ∆T, combine them into bins using a Python implementation of binned statistics, and then perform a least-squares regression...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: will-yeadon-and-mark-quinn-2021
    resource: "https://arxiv.org/abs/2105.08142"
    title: "Will Yeadon and Mark Quinn. (2021). Thermodynamics education for energy transformation: a Stirling Engine experiment. https://arxiv.org/abs/2105.08142"
    author: Will Yeadon and Mark Quinn
---

# Teach binned statistics on irregular repeat data followed by least-squares regression as a gentle introduction to data analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends having students merge repeat data sets recorded at arbitrary values of ∆T, combine them into bins using a Python implementation of binned statistics, and then perform a least-squares regression of f² against ∆T to extract the engine efficiency from the gradient. "The combining of repeat data at arbitrary values of ∆T presents an opportunity to teach a useful analysis method called binned statistics." The article provides the Python binning script in Appendix B, and notes the regression approach is standard in most physics courses and available in all analysis software.

## Design Implications

### Context
#### Requirements
- Repeat data sets recorded at arbitrary ∆T values sampled at a constant rate, and access to the Python programming language for the binning algorithm.
- Students equate the theoretical model to the linear function y = mx + c and use error propagation on the gradient to determine η ± ∆η.
#### Constraints
- The article notes the binned data's larger error bars clearly represent a systematic error between repeats, visible as divergence of measurements at higher ∆T.

### Target Learners
- first year undergraduate physics students

### Target Learning Goals
- statistical data analysis
- regression analysis
- handling irregular experimental data

## Related Strategies

- [Integrate the engine experiment into a multi-session sequence building DC circuit, oscilloscope, and data-analysis skills](multi-session-skills-integration-strategy.md)

## Examples
-

## Key Sources
- Will Yeadon and Mark Quinn. (2021). Thermodynamics education for energy transformation: a Stirling Engine experiment. https://arxiv.org/abs/2105.08142
