---
type: design
id: jill-watson-prompt-personalization-module
title: Jill Watson prompt-engineering personalization module integrated with the RAG pipeline
description: A modular personalization component for the Jill Watson virtual teaching assistant that encodes learner attributes in an engineered prompt conditioning the underlying LLM at runtime.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: saptarshi-basu-2026
    resource: "https://arxiv.org/abs/2609.03402"
    title: "Saptarshi Basu, Sandeep Kakar, Ashok Goel. (2026). A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant. https://arxiv.org/abs/2609.03402"
    author: Saptarshi Basu, Sandeep Kakar, Ashok Goel
---

# Jill Watson prompt-engineering personalization module integrated with the RAG pipeline

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A modular personalization component for the Jill Watson virtual teaching assistant that encodes learner attributes in an engineered prompt conditioning the underlying LLM at runtime. The article states it is "integrated with Jill Watson's retrieval-augmented generation (RAG) pipeline and course-specific knowledge base, allowing personalization to modify the form and presentation of responses while preserving grounding in retrieved instructional content." It enables "scalable personalization without modifying or retraining the underlying LLM" and is designed for integration into the deployed Jill Watson architecture.

## Design Implications

### Context
#### Requirements
- Learner preferences must be updatable through the Jill Watson interface and incorporated into prompts at runtime
- A course-specific knowledge base and RAG pipeline must supply the shared instructional content
#### Constraints
- The module personalizes response form and presentation, not the retrieved content itself
- Deployment integration is targeted for Spring 2027 with a Georgia Tech pilot in Summer 2027

### Target Learners
- students in courses using the Jill Watson AI teaching assistant across institutions

### Learning Goals
- course-grounded question answering tailored to individual learner preferences and question complexity

### Claims
- [Prompt Personalization Measurable Response Variation](../claims/prompt-personalization-measurable-response-variation.md) [+M]
- [Semantic Grounding With Surface Variation](../claims/semantic-grounding-with-surface-variation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Saptarshi Basu, Sandeep Kakar, Ashok Goel. (2026). A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant. https://arxiv.org/abs/2609.03402
