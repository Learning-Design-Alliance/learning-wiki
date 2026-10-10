---
type: design
id: elevate-teacher-interaction-layer
title: "Teacher Interaction Layer: a web-based configuration surface for pedagogical intent, persona, and role"
description: "The Teacher Interaction Layer is a lightweight web-based configuration page through which educators shape the virtual tutor's behavior; all settings are injected directly into the LLM system prompt."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: lorenzo-stacchio-2026
    resource: "https://arxiv.org/abs/2606.30662"
    title: "Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662"
    author: Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni
---

# Teacher Interaction Layer: a web-based configuration surface for pedagogical intent, persona, and role

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The Teacher Interaction Layer is a lightweight web-based configuration page through which educators shape the virtual tutor's behavior; all settings are injected directly into the LLM system prompt. It exposes personality presets (e.g., Neutral, Friendly, Patient, Verbose, Concise, plus a Custom option), thumbnail-based avatar appearance selection, a knowledge base selector, and teacher type. "The interface specifies the type of teacher through mutually exclusive radio-button options (e.g., professor (replicating lecture content), tutor (providing repeated explanations and scaffolding), and exam trainer", with a save action persisting settings as reproducible configuration artifacts.

## Design Implications

### Context
#### Requirements
- Settings must be persisted as configuration artifacts (templates, rule sets, corpus descriptors) interpreted by the server at runtime for traceability
#### Constraints
- Personality presets are deliberately constrained; styles beyond them require additional engineering inputs such as tailored prompt templates or policy rules

### Target Learners
- students in classrooms configured by their teachers

### Learning Goals
- consistent, pedagogically framed tutoring behavior matching classroom norms and assessment contexts

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662
