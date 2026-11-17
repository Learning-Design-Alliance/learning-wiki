---
type: strategy
id: pyro-regression-testing-version-control-strategy
title: Built-in regression testing and distributed version control to teach software engineering practices
description: "pyro teaches basic software-engineering safety practices in three ways: open-source BSD-3 release so that sharing of code helps find bugs; built-in regression testing where \"the current results will be compared zone-b..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: zingale-2014
    resource: "https://arxiv.org/abs/1306.6883"
    title: "Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883"
    author: Zingale, M
---

# Built-in regression testing and distributed version control to teach software engineering practices

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
pyro teaches basic software-engineering safety practices in three ways: open-source BSD-3 release so that sharing of code helps find bugs; built-in regression testing where "the current results will be compared zone-by-zone with the stored benchmark, and any differences will be reported"; and distribution via git so that "each student's clone of the pyro repo acts as its own git repo that they can interact with directly". The author reports that in several graduate classes many students were simply unaware of version control, and once introduced many began using it for their own projects.

## Design Implications

### Context
#### Requirements
- A stored benchmark solution generated with the --make benchmark option; a git repository for students to clone
#### Constraints
- Comparing bit-for-bit in each zone may not agree across different platforms because of floating point differences, so unique benchmarks may need to be made on each platform

### Target Learners
- astronomy students
- graduate students learning programming practices

### Target Learning Goals
- learning version control
- learning regression testing and verification and validation practices

## Claims

- [The pyro compressible-hydrodynamics verification tests reproduce analytic reference solutions (Sod shock tube, Sedov-Taylor blast wave, single-mode Rayleigh-Taylor)](../claims/pyro-compressible-tests-match-analytic-solutions.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)
