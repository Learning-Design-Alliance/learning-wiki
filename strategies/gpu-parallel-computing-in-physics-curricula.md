---
type: strategy
id: gpu-parallel-computing-in-physics-curricula
title: Introduce GPU parallel computing techniques into graduate and advanced undergraduate physics curricula
description: The article advocates bringing high-performance parallel computing into the physics classroom using affordable graphics cards, arguing that the learning curve for entry is no longer steep for those familiar with progr...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: matjaˇz-perc-2017
    resource: "https://arxiv.org/abs/1704.08098"
    title: "Matjaˇz Perc. (2017). High-performance parallel computing in the classroom using the public goods game as an example. https://arxiv.org/abs/1704.08098"
    author: Matjaˇz Perc
---

# Introduce GPU parallel computing techniques into graduate and advanced undergraduate physics curricula

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article advocates bringing high-performance parallel computing into the physics classroom using affordable graphics cards, arguing that the learning curve for entry is no longer steep for those familiar with programming and that live classroom demonstration of phenomena otherwise out of reach becomes possible. As printed, "The time is thus ripe for these programming techniques to be introduced into graduate and advanced undergraduate curricula, giving students the chance to learn the beneﬁts of parallel computing from the onset of their physics education". The public goods game example and released source code serve as entry material.

## Design Implications

### Context
#### Requirements
- Graphics cards supporting CUDA, available from hundred euros upward
- Familiarity with programming; the CUDA environment integrates with existing compilers
#### Constraints
- At L = 4096 simulation time is still somewhat too long for classroom demonstrations, though such large lattice sizes are rarely needed

### Target Learners
- graduate students
- advanced undergraduate physics students

### Target Learning Goals
- parallel computing
- Monte Carlo methods in statistical physics

## Claims

- [The GPU re-write of the solver was not complicated, especially with guidance, and served as a useful exercise for understanding GPU computation](../claims/gpu-rewrite-not-complicated-useful-exercise.md) [+W]

## Related Strategies

- [Use GPU-accelerated simulations to show state-of-the-art code running in real time in lectures and classrooms](gpu-real-time-demonstrations-teaching.md)

## Examples
-

## Key Sources
- Matjaˇz Perc. (2017). High-performance parallel computing in the classroom using the public goods game as an example. https://arxiv.org/abs/1704.08098
