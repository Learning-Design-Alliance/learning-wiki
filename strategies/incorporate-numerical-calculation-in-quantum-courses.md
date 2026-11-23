---
type: strategy
id: incorporate-numerical-calculation-in-quantum-courses
title: Incorporate numerical calculation into introductory quantum courses to counteract abstraction-driven misconceptions
description: The article recommends adding a computational component to introductory quantum courses, following educators and textbook authors who have stressed this approach.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
sources:
  - id: r-garcia-2007
    resource: "https://arxiv.org/abs/0704.1622"
    title: "R. Garcia, A. Zozulya, and J. Stickney. (2007). MATLAB codes for teaching quantum physics: Part 1. https://arxiv.org/abs/0704.1622"
    author: R. Garcia, A. Zozulya, and J. Stickney
---

# Incorporate numerical calculation into introductory quantum courses to counteract abstraction-driven misconceptions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends adding a computational component to introductory quantum courses, following educators and textbook authors who have stressed this approach. The stated motive is that computer representation makes kets concretely column vectors, bras row vectors, and operators matrices, counteracting novice errors like conflating Ψ(x) with |Ψ⟩. A further stated benefit is that students feel "empowered to solve real problems that may not have simple, analytic solutions". The article operationalizes this with six MATLAB exercises tied to Griffiths' text.

## Design Implications

### Context
#### Requirements
- A programming environment whose syntax suits matrix operations; the authors chose MATLAB for its simple matrix syntax and easy plotting
#### Constraints
- Exercises emphasize pedagogy over numerical efficiency, so efficient ODE solvers and finite-element methods are omitted
- Units are chosen with ℏ = m = 1 to keep equations familiar; dimensionless rescaling is deferred to more advanced courses

### Target Learners
- beginning (junior-level) quantum mechanics students

### Target Learning Goals
- accept on an intuitive level that functions are like vectors and differential operators are like matrices
- solve 1D quantum problems numerically

## Claims

- [Numerical exercises empower beginning quantum students to solve real problems without analytic solutions](../claims/computational-aspect-empowers-quantum-students.md) [+W]
- [Numerical computation fosters student acceptance that kets are column vectors, bras row vectors, and operators matrices](../claims/numerical-computation-builds-ket-matrix-intuition.md) [+W]

## Related Strategies

- [Incorporate computation into an existing classical mechanics course through in-class demonstrations followed by student projects that progress from template modification to independent construction](demonstration-template-to-independent-projects.md)
- [Use a simple computational exercise that can be 'tweaked' with a few lines of code to solve a different, equally intensive problem almost for free](notebook-tweak-almost-for-free-strategy.md)
- [Teach quantum bound states by embedding arbitrary potentials in an infinite square well basis and solving truncated matrix diagonalization problems](square-well-basis-matrix-diagonalization-instruction-strategy.md)
- [Undergraduate project assignment investigating exact calculation of numbers beyond floating point precision in Fortran](arbitrary-precision-undergraduate-project-assignment.md)
- [Use simple spreadsheet-based numerical simulation of orbital systems as an engaging team-based learning activity](spreadsheet-numerical-simulation-team-learning-strategy.md)
- [Design all introductory computational assignments to be completable in spreadsheets so students without programming background can participate.](spreadsheet-first-computational-assignments-strategy.md)
- [Teaching sequence: discretize the evolution equations, implement the recurrences in a spreadsheet, and compare classical, stochastic and quantum solutions](spreadsheet-recurrence-teaching-sequence.md)
- [Pairing the simulator's visual plot with terminal readouts of intermediate vector quantities to make electric-field computation visible](plot-plus-terminal-intermediate-quantities-strategy.md)
- [Have players compare expected with software-computed outcomes to reflect on and retrace quantum-operation misunderstandings](expected-vs-computed-outcome-reflection.md)
- [Pair traditional quantum computation lecture topics with hands-on activities on real quantum systems](pair-lectures-with-hands-on-quantum-activities.md)
- [Use the analog classical computer thought experiment with explicit floating-point discussion to teach the quantum-classical distinction](analog-classical-computer-thought-experiment-strategy.md)
- [Incorporate quantum spin into existing curriculum through magnetism and real-world applications like MRI](quantum-spin-curriculum-integration-mri-magnetism.md)
- [Embed quantum computing modules into existing statistical physics courses rather than teaching quantum computing in isolation](embed-qc-in-statistical-physics-courses-strategy.md)
- [Follow a five-step modeling-to-analysis sequence when introducing numerical simulation of physical problems](five-step-numerical-modeling-sequence.md)
- [Teach computational physics through detailed step-by-step construction of a numerical solution to a challenging problem](step-by-step-numerical-solution-teaching-strategy.md)

## Examples
-

## Key Sources
- R. Garcia, A. Zozulya, and J. Stickney. (2007). MATLAB codes for teaching quantum physics: Part 1. https://arxiv.org/abs/0704.1622
