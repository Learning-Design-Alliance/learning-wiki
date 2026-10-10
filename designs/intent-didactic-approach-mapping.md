---
type: design
id: intent-didactic-approach-mapping
title: Intent-to-didactic-approach mapping structuring responses by Bloom level and typed chunk selection
description: "The system elicited the instructor's actual response practice into a small set of declarative didactic approaches (Definition, Identification, Illustration, Explanation, Comparison, Complex synthesis), each targeting..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: laurent-brisson-2026
    resource: "https://arxiv.org/abs/2607.22598"
    title: "Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598"
    author: Laurent Brisson, Maria Teresa Segarra and Gregory Smits
---

# Intent-to-didactic-approach mapping structuring responses by Bloom level and typed chunk selection

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system elicited the instructor's actual response practice into a small set of declarative didactic approaches (Definition, Identification, Illustration, Explanation, Comparison, Complex synthesis), each targeting a Bloom level and defining core chunk types that structure the generated response plus an ontology-enrichment strategy. Five pedagogical intents form the exhaustive set: DEFINE, EXPLAIN, ILLUSTRATE, COMPARE, and IDENTIFY, where "IDENTIFY is the inverse of DEFINE". Constrained retrieval selects content by metadata filters on chunk type and concept id rather than unconstrained similarity.

## Design Implications

### Context
#### Requirements
- A knowledge graph of concepts with structural and didactic relations curated by the instructor
- An editorial corpus segmented into nine typed chunks with concept-identifier metadata
#### Constraints
- If constrained retrieval returns no chunk for a required type, the system returns a static reformulation message rather than silently switching to unconstrained retrieval

### Target Learners
- University students asking conceptual questions about course content

### Learning Goals
- Responses structured to the pedagogical intent and Bloom level of the student's question

### Claims
- [Deterministic Pedagogical Orchestration Architecture](deterministic-pedagogical-orchestration-architecture.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598
