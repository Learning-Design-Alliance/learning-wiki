---
type: design
id: evolving-knowledge-space-graph-model
title: Evolving Knowledge Space Graph (EKSG) model
description: The EKSG model is a graph-structured knowledge representation framework for adaptive intelligent tutoring in fast-changing domains, combining the structural clarity of ontologies with the adaptive potential of Compete...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: csépányi-fürjes-2026
    resource: "https://doi.org/10.1007/s11423-026-10639-6"
    title: "Csépányi-Fürjes, L., & Kovács, L. (2026). Intelligent tutoring in dynamic domains: a graph-based system for comparative analysis of adaptive algorithms with intuitionistic fuzzy logic and forgetting. Education Tech Research Dev. https://doi.org/10.1007/s11423-026-10639-6"
    author: "Csépányi-Fürjes, L., & Kovács, L"
---

# Evolving Knowledge Space Graph (EKSG) model

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The EKSG model is a graph-structured knowledge representation framework for adaptive intelligent tutoring in fast-changing domains, combining the structural clarity of ontologies with the adaptive potential of Competence-Based Knowledge Space Theory. The article describes it as "a Knowledge Space Theory (KST) based (Doignon & Falmagne, 1985) conceptual framework specifically designed to support adaptive intelligent tutoring in fast-changing domains" that "integrates principles of temporal graph theory to represent dynamically changing domains." In this study it is operationalized in the G4L system, with knowledge units, material units, and test units as graph nodes connected by prerequisite_of edges.

## Design Implications

### Context
#### Requirements
- A graph database to represent and query the prerequisite structure among knowledge units, as implemented in Neo4j
#### Constraints
- Before this study there was no publicly available implementation of the model and no empirical studies evaluating its practical feasibility or pedagogical utility

### Target Learners
- university students in fast-evolving domains such as computer science

### Learning Goals
- structured domain knowledge acquisition and adaptive learning pathways in dynamic curricula

### Claims
- [G4L Integrated Approach Supports Navigation](../claims/g4l-integrated-approach-supports-navigation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Csépányi-Fürjes, L., & Kovács, L. (2026). Intelligent tutoring in dynamic domains: a graph-based system for comparative analysis of adaptive algorithms with intuitionistic fuzzy logic and forgetting. Education Tech Research Dev. https://doi.org/10.1007/s11423-026-10639-6
