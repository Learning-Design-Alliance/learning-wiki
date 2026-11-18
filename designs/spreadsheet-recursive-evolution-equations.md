---
type: design
id: spreadsheet-recursive-evolution-equations
title: Spreadsheet as a recursive-algorithm environment for numerical solutions of evolution equations
description: "The spreadsheet is the computer support selected for the numerical analysis, chosen 'because it is largely used in school contexts and because we consider it an ideal environment for an intuitive approach to numerical..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: emilio-balzano-2017
    resource: "https://arxiv.org/abs/1705.11141"
    title: "Emilio Balzano, Eliana D'Ambrosio, Rodofo Figari. (2017). An algorithm-based introduction to the evolution of physical systems. https://arxiv.org/abs/1705.11141"
    author: "Emilio Balzano, Eliana D'Ambrosio, Rodofo Figari"
---

# Spreadsheet as a recursive-algorithm environment for numerical solutions of evolution equations

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The spreadsheet is the computer support selected for the numerical analysis, chosen 'because it is largely used in school contexts and because we consider it an ideal environment for an intuitive approach to numerical solutions of the diﬀerential equations that govern a theory'. Recursion formulas are written via relative references and each computational step consists in copying and pasting the previous line, so students can implement the algorithms without previous knowledge of programming languages and focus on dynamical features of the evolution.

## Design Implications

### Context
#### Requirements
- Recursion formulas written via relative references, with fixed parameters appearing as absolute references
- Spreadsheet use is already presented in high school
#### Constraints
- An implicit space discretization is implied by the choice of the maximum number of decimal places allowed in the spreadsheet

### Target Learners
- high school students
- high school science teachers

### Learning Goals
- implementing recurrence relations computing approximate solutions of dynamical laws
- graphical representation of solutions at any future time

### Claims
- 

## Related Designs

- [Discretized space-time recurrence framework for classical, stochastic and quantum evolution](discretized-space-time-recurrence-framework.md)

## Examples
-

## Key Sources
- Emilio Balzano, Eliana D'Ambrosio, Rodofo Figari. (2017). An algorithm-based introduction to the evolution of physical systems. https://arxiv.org/abs/1705.11141
