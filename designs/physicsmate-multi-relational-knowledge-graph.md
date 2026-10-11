---
type: design
id: physicsmate-multi-relational-knowledge-graph
title: Multi-relational knowledge graph of the NCTB physics syllabus with ten ontological node types
description: The knowledge graph formalizes the 13-chapter NCTB syllabus as a multi-relational structure with 1,760 nodes across 10 ontological types (concepts, questions, quantities, figures, examples, entities, definitions, form...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: rashid-azraf-jahin-2026
    resource: "https://arxiv.org/abs/2610.00664v1"
    title: "Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664v1"
    author: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
---

# Multi-relational knowledge graph of the NCTB physics syllabus with ten ontological node types

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The knowledge graph formalizes the 13-chapter NCTB syllabus as a multi-relational structure with 1,760 nodes across 10 ontological types (concepts, questions, quantities, figures, examples, entities, definitions, formulas, laws, HSC topics) and 2,600 directed edges spanning 30 relation types. Relations include curricular hierarchy (part_of), applicability (applies_to), visual grounding (illustrates), example relations (example_of), dependency (depends_on) and provenance (derived_from). The graph serves as "a structured curricular index of the source material" used for category-level analysis, with every node traceable to source textbook pages.

## Design Implications

### Context
#### Requirements
- Extraction uses a predefined domain ontology and a fixed structured prompt so equivalent curricular facts receive consistent representation, and each record retains source-page provenance.
#### Constraints
- The 10-node ontology maps directly to STEM domains; non-STEM or humanities curricula would require restructuring the declarative and procedural primitives into causal, temporal and narrative relation types.

### Target Learners
- Grade 9-10 secondary physics students in Bengali-medium education

### Learning Goals
- Structured curricular knowledge representation enabling category-level evaluation of physics QA

### Claims
- [Structured Knowledge Benefits Most From Adaptation](../claims/structured-knowledge-benefits-most-from-adaptation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664v1
