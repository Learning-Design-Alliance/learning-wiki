---
type: design
id: goal-free-user-interface-andes
title: Goal-free vs. goal-aligned user interfaces for step-based tutoring systems
description: "A goal-aligned user interface displays relevant goals as blank boxes or constrained entry locations that scaffold problem-solving steps; a goal-free user interface is \"essentially a blank canvas, with no visual indica..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: vanlehn-2015
    resource: "https://doi.org/10.1007/s40593-015-0067-7"
    title: "VanLehn, K. (2015). Reflections on Andes' Goal-free User Interface. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0067-7"
    author: VanLehn, K
---

# Goal-free vs. goal-aligned user interfaces for step-based tutoring systems

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A goal-aligned user interface displays relevant goals as blank boxes or constrained entry locations that scaffold problem-solving steps; a goal-free user interface is "essentially a blank canvas, with no visual indications of the goals that should be attempted next". Andes implemented the goal-free vision so users could enter steps anywhere and in any order, like paper, while the system still recognized goals and correctness. The design requires the system to do plan recognition, interpret composite steps, and support assessment without location-based goal cues.

## Design Implications

### Context
#### Requirements
- The tutoring system must provide goal scaffolding on demand via next-step and what's-wrong hint buttons
- The system must decompose large composite steps into primitive physics rules
- Immediate feedback keeps students on a recognizable solution path
#### Constraints
- Plan recognition works poorly because users often have no recognizable plan
- Embedded assessment (assignment of blame) is much harder because an incorrect step's location provides no information about the user's intended goal

### Target Learners
- introductory college students
- advanced high school physics students

### Learning Goals
- physics problem solving

### Claims
- [Plan Recognition Fails Goal Free Interface](../claims/plan-recognition-fails-goal-free-interface.md) [+M]
- [Shapiro Equation Decomposition Algorithm](../claims/shapiro-equation-decomposition-algorithm.md) [+M]
- [Heuristic Blame Assignment Kappa 078](../claims/heuristic-blame-assignment-kappa-078.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- VanLehn, K. (2015). Reflections on Andes' Goal-free User Interface. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0067-7
