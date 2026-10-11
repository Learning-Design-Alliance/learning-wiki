---
type: strategy
id: impasse-depth-type-analytics-escalation-signals
title: Use impasse depth and type as real-time learning-analytics signals to trigger graduated escalation of tutor support
description: The article recommends that learning analytics systems track impasse depth and type in tutoring dialogues in real time to flag students who remain stuck and support graduated escalation.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: ahtisham-2026
    resource: "https://arxiv.org/abs/2609.38346"
    title: "Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R. (2026). Examining Variation in How Guided AI Tutors Resolve Student Impasses. arXiv. https://arxiv.org/abs/2609.38346"
    author: "Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R"
---

# Use impasse depth and type as real-time learning-analytics signals to trigger graduated escalation of tutor support

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that learning analytics systems track impasse depth and type in tutoring dialogues in real time to flag students who remain stuck and support graduated escalation. As the Notes for Practice state, analytics can "track impasse depth and type in tutoring dialogues in real time to flag students who remain stuck", moving "from questioning to targeted error feedback and, when needed, worked sub-steps". Impasse depth and type are observable, turn-level dialogue signals derived from codebook-annotated logs.

## Design Implications

### Context
#### Requirements
- A dialogue annotation pipeline able to code impasse turns, types (conceptual error, expressed uncertainty, help-seeking), and depth from tutor-student logs
#### Constraints
- The authentic dialogue analyses are observational, so associations between tutor moves and recovery are not causal; recovery captures only next-turn correctness, not longer-term learning

### Target Learners
- undergraduate chemistry students in introductory general chemistry

### Target Learning Goals
- early identification of stalled tutoring interactions
- timely escalation of assistance before disengagement

### Affordances
- Graduated State Sensitive Assistance Llm Tutors

## Related Strategies
- 

## Examples
-

## Key Sources
- Ahtisham, B., Vanacore, K., Napoli, A., Arens, J., Ionova, K., Cohn, C., Salehi, S., & Kizilcec, R. (2026). Examining Variation in How Guided AI Tutors Resolve Student Impasses. arXiv. https://arxiv.org/abs/2609.38346
