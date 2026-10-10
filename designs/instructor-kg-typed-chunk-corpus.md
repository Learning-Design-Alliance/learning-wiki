---
type: design
id: instructor-kg-typed-chunk-corpus
title: Instructor-curated knowledge graph and dual-readability typed chunk corpus for a dimensional modelling course
description: The course knowledge is represented as a lightweight knowledge graph containing 43 concepts organised into thematic groups, connected through structural relations (is a, part of) and didactic relations (precedes, conf...
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

# Instructor-curated knowledge graph and dual-readability typed chunk corpus for a dimensional modelling course

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The course knowledge is represented as a lightweight knowledge graph containing 43 concepts organised into thematic groups, connected through structural relations (is a, part of) and didactic relations (precedes, confused with, mutually exclusive with) curated by the instructor. The course material is authored as structured Markdown revised "for dual readability: human and machine", with each concept on a dedicated page, content segmented into nine chunk types determined by the markup itself, and every chunk indexed in a ChromaDB store with concept id and chunk type as filterable attributes. Every answer is grounded in this instructor-authored material with permalinks to the relevant teaching pages.

## Design Implications

### Context
#### Requirements
- Each new content source must be indexed with concept identifiers and chunk types so constrained retrieval continues to operate on pedagogical role
#### Constraints
- The current corpus is mono-authored, originating solely from the instructor's teaching notes

### Target Learners
- University students in the dimensional modelling course

### Learning Goals
- Grounding chatbot answers in verified curricular content with permalinks to teaching pages

### Claims
- [Deterministic Pedagogical Orchestration Architecture](deterministic-pedagogical-orchestration-architecture.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598
