---
type: design
id: nmc2025-three-mode-workflow
title: "Three-mode graduated workflow: known-material simulation, AI-guided discovery, and frontier material setup"
description: NMC2025 organizes the learning journey into three operational modes of increasing learner autonomy.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: barrionuevo-2025
    resource: "https://unizar.es"
    title: "Barrionuevo, S. D., & Aguirre, M. H. (2025). AI-Guided Quantum Material Simulator for Education. Case Example: The Neuromorphic Materials Calculator 2025. https://unizar.es"
    author: "Barrionuevo, S. D., & Aguirre, M. H"
---

# Three-mode graduated workflow: known-material simulation, AI-guided discovery, and frontier material setup

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
NMC2025 organizes the learning journey into three operational modes of increasing learner autonomy. As the results section states, "The system begins with the Welcome module, which orients the student and allows the selection of one of three operational modes": Existing Materials (simulation from a Materials Project ID with AI-justified parameters), Exploring Options (literature-backed AI material discovery cross-validated via MPRester), and Pushing Frontier (guided manual entry of custom, unpublished material systems with iterative AI parameter review). The pattern scales scaffolding from database defaults to expert-level free-form setup.

## Design Implications

### Context
#### Requirements
- Access to the Materials Project database API and an LLM API so that suggestions and parameter critiques include scientific references.
#### Constraints
- The ad hoc input generator currently assumes a basic lattice (ibrav=1, cubic) unless additional symmetry information is given; its literature-evaluation step is a placeholder noted for future enhancement.

### Target Learners
- undergraduate through graduate students, with Pushing Frontier aimed at advanced learners

### Learning Goals
- translating application needs into materials criteria
- DFT parameter selection
- iterative hypothesis refinement

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Barrionuevo, S. D., & Aguirre, M. H. (2025). AI-Guided Quantum Material Simulator for Education. Case Example: The Neuromorphic Materials Calculator 2025. https://unizar.es. [doi:10.48550/arxiv.2509.20372](https://doi.org/10.48550/arxiv.2509.20372)
