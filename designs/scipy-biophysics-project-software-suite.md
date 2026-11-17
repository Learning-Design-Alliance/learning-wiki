---
type: design
id: scipy-biophysics-project-software-suite
title: A suite of modifiable Python/SciPy biophysics simulations and projects spanning imaging, diffusion, macromolecules, motors, and neurons
description: The article introduces a set of biophysics educational materials built on SciPy and Visual Python, covering topics from x-ray diffraction to the Hodgkin Huxley equations.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: j-m-deutsch-2013
    resource: "https://arxiv.org/abs/1303.0453"
    title: "J. M. Deutsch. (2013). Biophysics software for interdisciplinary education and research. https://arxiv.org/abs/1303.0453"
    author: J. M. Deutsch
---

# A suite of modifiable Python/SciPy biophysics simulations and projects spanning imaging, diffusion, macromolecules, motors, and neurons

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article introduces a set of biophysics educational materials built on SciPy and Visual Python, covering topics from x-ray diffraction to the Hodgkin Huxley equations. The projects use software written in SciPy "to serve multiple functions: sometimes to perform simulations that act as artiﬁcial experimental input, sometimes used to analyze data, and to gain theoretical and intuitive understanding of biophysical processes in a way that requires active learning." The code is deliberately simple early in the course and grows more advanced, with C code integrated via weave for efficiency.

## Design Implications

### Context
#### Requirements
- Students need some programming proficiency; teams normally include one student with prior programming exposure
- Instructors must install SciPy and Visual Python on students' own computers
#### Constraints
- Installation of SciPy and Visual Python was the most difficult part of the course; Mac operating systems were the most problematic, with graphics-card and library incompatibility issues

### Target Learners
- upper-division and graduate undergraduates in physics, biology, and biochemistry

### Learning Goals
- biophysical processes and physical laws
- mathematical analysis
- software development
- interdisciplinary collaboration

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- J. M. Deutsch. (2013). Biophysics software for interdisciplinary education and research. https://arxiv.org/abs/1303.0453
