---
type: strategy
id: measure-performance-first-strategy
title: Teach performance measurement before parallelism and template-based alternatives
description: "The APC devotes a half-day lesson to performance measurements and multi-core/SIMD techniques, reflecting that HEP codes are \"embarassingly parallel single node applications heavy on I/O\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: s-kluth-2015
    resource: "https://arxiv.org/abs/1505.04604"
    title: "S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach. (2015). How do particle physicists learn the programming concepts they need? https://arxiv.org/abs/1505.04604"
    author: S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach
---

# Teach performance measurement before parallelism and template-based alternatives

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The APC devotes a half-day lesson to performance measurements and multi-core/SIMD techniques, reflecting that HEP codes are "embarassingly parallel single node applications heavy on I/O". The school emphasizes "the importance of measurements ﬁrst over the common trend to exploit parallelism and related low-level CPU features at will", warning that premature parallelization is a common culprit wasting beginners' time and producing overly complex code. OpenMP, auto-vectorisation and, if time permits, SSE intrinsics are taught, and a slide-free live-coding session introduces templates and the curiously-recurring-template pattern.

## Design Implications

### Context
#### Requirements
- Open-source and free performance evaluation tools such as iperf and valgrind
#### Constraints
- SSE intrinsics are taught only if time permits
- The template session applies to runtime feature selection by virtual inheritance as used in the majority of HEP codes

### Target Learners
- young physicists writing performance-sensitive HEP analysis and simulation code

### Target Learning Goals
- performance evaluation and modern C++ techniques for multi-core and SIMD

## Claims

- [APC participants rated the course content as relevant to their work and would recommend it](../claims/apc-survey-relevance-recommendation.md) [+W]

## Related Strategies

- [Extension activities: building code from scratch, measuring runtime, the Verlet algorithm, and multi-body extensions](simulation-course-extension-activities.md)

## Examples
-

## Key Sources
- S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach. (2015). How do particle physicists learn the programming concepts they need? https://arxiv.org/abs/1505.04604
