---
type: strategy
id: ui-localization-as-intervention-activity
title: UI-localization of the learning tool as a non-code intervention activity
description: "LoopCAT's English, Catalan, and Turkish interface catalogs make the application itself available as teaching material."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: dogru-2026
    resource: "https://arxiv.org/abs/2609.00344"
    title: "Dogru, G., & Martín Mor, A. (2026). From Tool Use to Technological Agency: LoopCAT as a Local-First, Open-Source Tool for Translation Technology Education. https://arxiv.org/abs/2609.00344"
    author: "Dogru, G., & Martín Mor, A"
---

# UI-localization of the learning tool as a non-code intervention activity

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
LoopCAT's English, Catalan, and Turkish interface catalogs make the application itself available as teaching material. Students can translate English UI strings into another language, review automatically generated target drafts, import their revisions, and test the interface. This provides "a concrete non-code form of intervention: students can improve the environment in which they work and explain how a wording choice affects an action."

## Design Implications

### Context
#### Requirements
- Students should use a dedicated profile with teaching data and a distinct locale identifier
- A complete classroom copy must be maintained outside the profile because reimporting replaces the whole catalog
#### Constraints
- Runtime import does not enforce placeholder matching
- The repository's separate validator permits empty target values
- Module-level checks establish technical feasibility, not successful classroom deployment

### Target Learners
- translation students, including those who do not know Catalan or Turkish

### Target Learning Goals
- software localization skills
- understanding how wording choices affect interface actions
- non-code contribution to open-source software

## Related Strategies

- [Six-session teaching sequence for translation technology education](six-session-loopcat-teaching-sequence.md)
- [Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives](ai-nocode-lab-software-development.md)
- [Adapting a sanitized development episode into an evaluative exercise on AI-proposed changes](ai-co-creation-episode-as-teaching-exercise.md)

## Examples
-

## Key Sources
- Dogru, G., & Martín Mor, A. (2026). From Tool Use to Technological Agency: LoopCAT as a Local-First, Open-Source Tool for Translation Technology Education. https://arxiv.org/abs/2609.00344
