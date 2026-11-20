---
type: strategy
id: petal-x-design-decisions-strategy
title: Design risk-explanation visuals with external consistency to established clinical charts, grid lines for what-if reasoning, and legends mapping encodings to risk levels
description: "The article's design decisions for Petal-X include reusing \"the age-dependent color scale used by ESC GSCs and mobile app\" (red/orange/green for very high/high/low-to-moderate risk) to achieve external consistency and..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: diego-rojo-2024
    resource: "https://arxiv.org/abs/2406.18690"
    title: "Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. https://arxiv.org/abs/2406.18690"
    author: Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert
---

# Design risk-explanation visuals with external consistency to established clinical charts, grid lines for what-if reasoning, and legends mapping encodings to risk levels

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article's design decisions for Petal-X include reusing "the age-dependent color scale used by ESC GSCs and mobile app" (red/orange/green for very high/high/low-to-moderate risk) to achieve external consistency and avoid confounding elements in the evaluation, a petal-shaped grid with dotted lines at normalized values 0, 0.25, 0.5, 0.75, and 1 labeled with denormalized values to help users project risk reduction, and lobe risk legends plus per-petal labels with risk factor names and patient values.

## Design Implications

### Context
#### Requirements
- Access to the established clinical visualization's color conventions for external consistency
- A validated surrogate model whose coefficients map to petal angles and lengths
#### Constraints
- In the evaluated version, neither total CVD risk nor individual risk factor contributions were provided numerically, to test the area encoding itself

### Target Learners
- healthcare professionals and patients

### Target Learning Goals
- interpreting risk factor contributions and projected risk reductions

### Affordances

## Claims

- [Healthcare students using Petal-X complete risk-factor contribution (T1) and what-if comparison (T2) tasks significantly faster than those using graphical score charts](../claims/petal-x-faster-contribution-whatif-tasks.md) [+M]
- [No statistically significant difference between Petal-X and graphical score charts in perceived transparency, trust, or intent to use, with Bayes factors favoring the null](../claims/petal-x-no-subjective-difference.md) [~M]
- [The linear-regression surrogate of SCORE2 and its Petal-X approximation achieve fidelity comparable to or slightly higher than SCORE2 graphical score charts](../claims/petal-x-surrogate-fidelity-comparable-gsc.md) [~M]

## Related Strategies

- [Visualizing](visualizing.md)

## Examples
-

## Key Sources
- Diego Rojo, Houda Lamqaddam, Lucija Gosak, and Katrien Verbert. (2024). Petal-X: Human-Centered Visual Explanations to Improve Cardiovascular Risk Communication. https://arxiv.org/abs/2406.18690
