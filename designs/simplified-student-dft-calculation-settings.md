---
type: design
id: simplified-student-dft-calculation-settings
title: Simplified student DFT calculation settings that reduce week-long computations to minutes
description: "Appendix A describes the parameter simplifications that make the project attainable in one week: a coarser real-space grid (\"the student project only has 17% of the grid points compared to the research projects\"), use..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: jonas-ericsson-2016
    resource: "https://arxiv.org/abs/1603.08363"
    title: "Jonas Ericsson, Teodor Husmark, Christoffer Mathiesen, Benjamin Sepahvand, Øyvind Borck, Linda Gunnarsson, Pär Lydmark, and Elsebeth Schröder. (2016). Involving high school students in computational physics university research: Theory calculations of toluene adsorbed on graphene. arXiv preprint. https://arxiv.org/abs/1603.08363"
    author: Jonas Ericsson, Teodor Husmark, Christoffer Mathiesen, Benjamin Sepahvand, Øyvind Borck, Linda Gunnarsson, Pär Lydmark, and Elsebeth Schröder
---

# Simplified student DFT calculation settings that reduce week-long computations to minutes

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Appendix A describes the parameter simplifications that make the project attainable in one week: a coarser real-space grid ("the student project only has 17% of the grid points compared to the research projects"), use of only the Γ k-point, and a looser energy convergence threshold (n = 6 versus n = 7). Together, all simplifications "reduce week-long calculations to calculations of 10–30 minutes, albeit at the loss of some of the accuracy", yet the accuracy remains sufficient for the students to obtain meaningful results.

## Design Implications

### Context
#### Requirements
- The open-source DFT code GPAW and the Python computational environment ASE, plus a national computational cluster for parallelized computations (smaller calculations can also run on student laptops given sufficient patience)
#### Constraints
- The simplifications come at the loss of some accuracy, and the path to convergence in parameter setting is not necessarily monotonous, so care must be taken for full convergence

### Target Learners
- high school students

### Learning Goals
- hands-on experience with state-of-the-art calculational tools in materials research
- applied quantum physics

### Claims
- 

## Related Designs
- [Forskarkursen High School Research Course](forskarkursen-high-school-research-course.md)

## Examples
-

## Key Sources
- Jonas Ericsson, Teodor Husmark, Christoffer Mathiesen, Benjamin Sepahvand, Øyvind Borck, Linda Gunnarsson, Pär Lydmark, and Elsebeth Schröder. (2016). Involving high school students in computational physics university research: Theory calculations of toluene adsorbed on graphene. arXiv preprint. https://arxiv.org/abs/1603.08363
