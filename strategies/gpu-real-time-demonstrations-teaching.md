---
type: strategy
id: gpu-real-time-demonstrations-teaching
title: Use GPU-accelerated simulations to show state-of-the-art code running in real time in lectures and classrooms
description: The article proposes that desktop-level GPU speedups change what can be demonstrated interactively in teaching settings.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: knut-s-gjerden-2013
    resource: "https://arxiv.org/abs/1305.3625"
    title: "Knut S. Gjerden. (2013). Making the case of GPUs in courses on computational physics. https://arxiv.org/abs/1305.3625"
    author: Knut S. Gjerden
---

# Use GPU-accelerated simulations to show state-of-the-art code running in real time in lectures and classrooms

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article proposes that desktop-level GPU speedups change what can be demonstrated interactively in teaching settings. It states the result "could have major implications for interactive teaching in lecture halls, classrooms or computer rooms" and invites instructors to imagine being "not ... limited to demonstrating textbook models, but able to show relevant, state-of-the-art code to your students, possibly even running in real-time." The strategy is to bring research-grade GPU-accelerated simulations into live teaching sessions.

## Design Implications

### Context
#### Requirements
- A computer with a graphics card usable for general-purpose computing, and simulation code whose costly elements have been ported to GPU libraries.
#### Constraints
- The article notes the benefit applies in some cases, where speedup means the difference between running test systems and full-scale simulations on a desktop computer.

### Target Learners
- physics students in lecture halls, classrooms or computer rooms

### Target Learning Goals
- understanding state-of-the-art computational models through real-time demonstration

## Claims

- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](../claims/elevate-prototype-near-real-time-consumer-hardware.md) [+W]
- [VLab-HV's Light version maintains 30 fps on low-end systems with 8 GB RAM and integrated GPUs](../claims/vlab-hv-light-version-30fps-low-end.md) [+W]

## Related Strategies

- [Introduce GPU parallel computing techniques into graduate and advanced undergraduate physics curricula](gpu-parallel-computing-in-physics-curricula.md)
- [Real-time lecture demonstrations deriving theoretical predictions and testing them numerically with modifiable code](real-time-lecture-simulation-demonstrations.md)

## Examples
-

## Key Sources
- Knut S. Gjerden. (2013). Making the case of GPUs in courses on computational physics. https://arxiv.org/abs/1305.3625
