---
type: design
id: deterministic-pedagogical-orchestration-architecture
title: Deterministic pedagogical orchestration architecture with the LLM as linguistic executor
description: "The architecture separates pedagogical orchestration from text generation: instructional decisions (intent recognition, concept selection, chunk typing, prompt structure) are handled by deterministic modules, and the..."
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

# Deterministic pedagogical orchestration architecture with the LLM as linguistic executor

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The architecture separates pedagogical orchestration from text generation: instructional decisions (intent recognition, concept selection, chunk typing, prompt structure) are handled by deterministic modules, and the LLM is restricted to controlled disambiguation and surface-form generation. The pipeline proceeds through six stages: intent detection, concept detection, constrained retrieval, didactic resolution, prompt construction, and LLM generation. This separation, in the authors' words, "ensures pedagogical traceability (every decision maps to an explicit rule), enforces correctness through deterministic unit-testable logic, and makes the pipeline model-agnostic". It was designed to operate without commercial LLM budget or GPU infrastructure.

## Design Implications

### Context
#### Requirements
- A formalisation of the instructor's own pedagogical reasoning: intents, a domain ontology, and an instructor-authored structured editorial corpus
- Detection lexicons calibrated to the course vocabulary and language
#### Constraints
- Adapting to a new course requires the instructor to formalise their own pedagogical practice, not merely configure a tool
- Courses centred on theorem derivation, algorithmic processes, or code production may require different taxonomies and retrieval strategies

### Target Learners
- University students in a French-language dimensional modelling course

### Learning Goals
- Answering conceptual questions in dimensional modelling in line with the instructor's didactic practice

### Claims
- [Semantic Retrieval Insufficient Pedagogical Content](../claims/semantic-retrieval-insufficient-pedagogical-content.md) [+M]
- [Pattern Detector High Precision Low Coverage](../claims/pattern-detector-high-precision-low-coverage.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598
