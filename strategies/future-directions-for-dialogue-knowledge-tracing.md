---
type: strategy
id: future-directions-for-dialogue-knowledge-tracing
title: Future Directions for Dialogue Knowledge Tracing
description: The article closes with avenues for future work on dialogueKT.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# Future Directions for Dialogue Knowledge Tracing

> **Strategy** · [All strategies](index.md)

## Description
The article closes with avenues for future work on dialogueKT. First, "we can jointly model tutor moves and student knowledge states to analyze what types of tutor moves are effective at improving student knowledge". Second, student affect dynamics should be accounted for, possibly with audio and video. Third, the scope can extend to other subjects and multi-student dialogues. Fourth, work should test whether estimated knowledge states are useful for personalization, teacher support, or powering simulated student agents.

## Design Implications

### Context
#### Requirements
- Tutoring dialogue data with more turns; the authors call on researchers with access to longer dialogues to use their publicly available implementation.
#### Constraints
- The current work only focuses on math dialogues between a single student and tutor.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Goals
- Personalization, teacher support, and training AI-based tutors from estimated student knowledge states

## Related Strategies
- [Dialogue Knowledge Tracing Framework](../theories/dialogue-knowledge-tracing-framework.md)
- [Llmkt Llm Based Knowledge Tracing](../elements/llmkt-llm-based-knowledge-tracing.md)
- [Personalization](../principles/personalization.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
