---
type: strategy
id: bootstrapping-baseline-annotated-corpus
title: Deploy a minimal baseline chatbot to bootstrap its own annotated evaluation corpus and improve incrementally
description: The article proposes an incremental methodology in which a minimal deterministic baseline is deployed in production and its logged questions, annotated post-hoc, become the training and evaluation resources for subseq...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: laurent-brisson-2026
    resource: "https://arxiv.org/abs/2607.22598"
    title: "Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598"
    author: Laurent Brisson, Maria Teresa Segarra and Gregory Smits
---

# Deploy a minimal baseline chatbot to bootstrap its own annotated evaluation corpus and improve incrementally

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes an incremental methodology in which a minimal deterministic baseline is deployed in production and its logged questions, annotated post-hoc, become the training and evaluation resources for subsequent iterations. The authors state that "the deployed baseline itself produces the annotated resources that subsequent iterations consume", raising the question of the minimal viable system that can seed its own iterative refinement. The annotated corpus of 195 authentic queries supports improvement paths such as supervised classifiers or selective LLM fallback, each independently evaluable with the same modular protocol.

## Design Implications

### Context
#### Requirements
- Questions logged with informed consent and annotated post-hoc by the instructor
- A modular evaluation protocol so each iteration remains independently evaluable
#### Constraints
- Adapting the system to another course requires constructing a domain ontology, authoring a structured editorial corpus, and calibrating detection lexicons, steps involving pedagogical expertise that cannot be automated away

### Target Learners
- University students in domain-specific courses

### Target Learning Goals
- Continuously improving pedagogical routing accuracy of a course chatbot under operational constraints

## Related Strategies

- [Evaluate AI systems before deploying them with students](evaluate-ai-before-deployment-with-students.md)

## Examples
-

## Key Sources
- Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598
