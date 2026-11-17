---
type: design
id: statistical-entropy-temperature-derivation-spreadsheet
title: Statistical derivation of entropy and temperature from multiplicity counting
description: "The article develops entropy as S = k ln Ω, where Ω is the multiplicity of a macrostate, and derives temperature from entropy-vs-energy graphs: equilibrium occurs when total entropy is maximal, so the slopes of the tw..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: thomas-a-moore-and-daniel-v-schroeder-1997
    resource: "https://doi.org/10.1119/1.18490"
    title: "Thomas A. Moore and Daniel V. Schroeder. (1997). A different approach to introducing statistical mechanics. Am. J. Phys. 65 (1), 26–36. https://doi.org/10.1119/1.18490"
    author: Thomas A. Moore and Daniel V. Schroeder
---

# Statistical derivation of entropy and temperature from multiplicity counting

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article develops entropy as S = k ln Ω, where Ω is the multiplicity of a macrostate, and derives temperature from entropy-vs-energy graphs: equilibrium occurs when total entropy is maximal, so the slopes of the two solids' entropy graphs are equal in magnitude, and temperature is inversely related to slope, giving 1/T = dS/dU. Spreadsheet plots of SA, SB, and Stotal make this derivation concrete for students, bridging the classical and statistical approaches to entropy.

## Design Implications

### Context
#### Requirements
- A computational environment able to compute combinatoric multiplicity functions, such as a spreadsheet with binomial-coefficient functions
#### Constraints
- The derivation assumes weakly coupled subsystems with a clean separation of time scales; for strongly coupled systems this separation would not be possible

### Target Learners
- first-year calculus-based introductory physics students
- upper-division undergraduate physics students

### Learning Goals
- understand the statistical definition of entropy
- understand how the second law arises from multiplicity counting
- understand the theoretical definition of temperature

### Claims
- Interacting Einstein Solids Multiplicity Peak [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Thomas A. Moore and Daniel V. Schroeder. (1997). A different approach to introducing statistical mechanics. Am. J. Phys. 65 (1), 26–36. https://doi.org/10.1119/1.18490
