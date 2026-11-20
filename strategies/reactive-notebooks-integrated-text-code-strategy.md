---
type: strategy
id: reactive-notebooks-integrated-text-code-strategy
title: Use reactive notebooks integrating explanatory text and code to support engagement and exploration
description: Deliver course material in reactive Pluto.jl notebooks that combine lecture notes and code in a single file, with plotting code hidden but revealable.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: luc-t-paoli-2023
    resource: "https://arxiv.org/abs/2310.13234"
    title: "Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker. (2023). Confronting the thermodynamics knowledge gap: A short course on computational thermodynamics in Julia. https://arxiv.org/abs/2310.13234"
    author: Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker
---

# Use reactive notebooks integrating explanatory text and code to support engagement and exploration

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Deliver course material in reactive Pluto.jl notebooks that combine lecture notes and code in a single file, with plotting code hidden but revealable. When students modify code and re-run a cell, "the entire notebook 'reacts' to update every other cell block, including the hidden plotting code", so figures update automatically based on their changes. The authors believe reactive notebooks allow students to engage more intently with lecture material and foster independent learning, and they used this format for exercises with real-time feedback text boxes.

## Design Implications

### Context
#### Requirements
- A detailed set of instructions for installing and using the code environment should be prepared and made available, as was done on the GitHub repository
#### Constraints
- The authors note that similar functionalities are available in more commonly used interactive environments such as Jupyter notebooks, but sequential interactive notebooks do not allow the dynamic updating behaviour

### Target Learners
- advanced undergraduate students
- graduate students

### Target Learning Goals
- computational thermodynamics
- coding familiarity
- independent exploration of models

## Claims

- [A short course on computational thermodynamics produced a near-total increase in students' self-perceived confidence in mastering and applying computational thermodynamics concepts](../claims/computational-thermodynamics-course-confidence-increase.md) [+W]
- [Students in the Julia-based course did not find setting up the environment or learning Julia syntax to be significant activation barriers](../claims/julia-setup-syntax-not-activation-barriers.md) [+W]
- [Students responded very positively to the course's content arrangement, with progression as the guiding design principle](../claims/progression-principle-well-received.md) [+W]
- [Lack of documentation was rated a more significant barrier for Julia than for Python in the pilot course](../claims/julia-documentation-barrier.md) [~W]

## Related Strategies

- [Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning](python-quantum-libraries-simulation-exercises.md)

## Examples
-

## Key Sources
- Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker. (2023). Confronting the thermodynamics knowledge gap: A short course on computational thermodynamics in Julia. https://arxiv.org/abs/2310.13234
