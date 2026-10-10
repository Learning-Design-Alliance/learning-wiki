---
type: design
id: graphrag-textbook-retrieval-math-tutor
title: GraphRAG textbook knowledge retrieval for grounded tutoring
description: The system implements Retrieval-Augmented Generation via the GraphRAG framework, in which textbook material is represented as a knowledge graph to provide contextually relevant information to the Tutor Agent and cours...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: jarosław-a-chudziak-and-adam-kostka-2025
    resource: "https://arxiv.org/abs/2507.12484"
    title: "Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484"
    author: Jarosław A. Chudziak and Adam Kostka
---

# GraphRAG textbook knowledge retrieval for grounded tutoring

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system implements Retrieval-Augmented Generation via the GraphRAG framework, in which textbook material is represented as a knowledge graph to provide contextually relevant information to the Tutor Agent and course-generation pipeline. The authors chose GraphRAG over normal vector RAG on the argument that its graph structure better represents educational content relations for contextual tutoring. The Tutor Agent retrieves textbook data to ground its responses, and the course pipeline accesses GraphRAG data when constructing structured learning plans.

## Design Implications

### Context
#### Requirements
- Textbook material represented as a knowledge graph to provide structured educational content
#### Constraints
- The article notes future work will explore the potential of different RAG architectures

### Target Learners
- mathematics students using the tutoring platform

### Learning Goals
- grounding tutor responses and generated courses in course textbook content

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484
