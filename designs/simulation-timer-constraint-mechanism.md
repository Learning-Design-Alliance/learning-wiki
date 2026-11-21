---
type: design
id: simulation-timer-constraint-mechanism
title: "Constraint-based simulation design: decoupling pendulum release from timing start prevents a reaction-time-limited measurement dead end"
description: "This account explains the simulation's advantage through one specific designed constraint: students using the simulation were required to use the built-in timer, which \"forced the students using the simulation to firs..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: jeff-bale-2026
    resource: "https://arxiv.org/abs/2605.30624"
    title: "Jeff Bale, James Day, J. Ives, and D. A. Bonn. (2026). Constraints From Simulation Improve Experiential Outcomes in Laboratory Environment. arXiv. https://arxiv.org/abs/2605.30624"
    author: Jeff Bale, James Day, J. Ives, and D. A. Bonn
---

# Constraint-based simulation design: decoupling pendulum release from timing start prevents a reaction-time-limited measurement dead end

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This account explains the simulation's advantage through one specific designed constraint: students using the simulation were required to use the built-in timer, which "forced the students using the simulation to first start it swinging, and then subsequently pick an instance to start the timer and begin counting cycles." This decouples release from timing onset, blocking the synchronization strategy that traps physical-apparatus users in a "low-precision measurement dead end" while leaving all higher-order choices (timing start point, cycles, trials) to students. The authors argue this makes the timing method the most compelling explanation for the outcome difference.

## Design Implications

### Context
#### Requirements
- The simulation must include a built-in timer that is internally consistent, requiring mouse-click start and stop separate from pendulum release
- Students must retain autonomy over other experimental design choices such as number of cycles and trials
#### Constraints
- The internal timer is internally consistent but not externally consistent with an independent timer
- The account is offered as the most compelling explanation given matched amplitude decay, not as a directly tested manipulation

### Target Learners
- first-year undergraduate general science majors in an inquiry-based physics lab

### Learning Goals
- high-precision measurement and iterative experimental refinement
- data-driven reasoning about model failure

### Claims
- Simulation Timing More Reproducible Than Physical [+M]
- [Simulation Better Strategy By Round Three](../claims/simulation-better-strategy-by-round-three.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jeff Bale, James Day, J. Ives, and D. A. Bonn. (2026). Constraints From Simulation Improve Experiential Outcomes in Laboratory Environment. arXiv. https://arxiv.org/abs/2605.30624
