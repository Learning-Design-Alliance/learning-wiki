---
type: strategy
id: system-of-least-prompts-graceful-exit
title: "System of Least Prompts: a four-step graduated scaffolding hierarchy ending in graceful exit with direct instruction"
description: "When a student struggles, the AI proctor employs the System of Least Prompts, \"offering a strict hierarchy of scaffolding\": a general nudge, a specific cue, a targeted scaffold, and finally direct instruction."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: ilya-mikhelson-2026
    resource: "https://arxiv.org/abs/2607.29624"
    title: "Ilya Mikhelson. (2026). The Theoretical Foundation of Socratic Tests: Dynamic, Multimodal, Conversational Examinations. https://arxiv.org/abs/2607.29624"
    author: Ilya Mikhelson
---

# System of Least Prompts: a four-step graduated scaffolding hierarchy ending in graceful exit with direct instruction

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When a student struggles, the AI proctor employs the System of Least Prompts, "offering a strict hierarchy of scaffolding": a general nudge, a specific cue, a targeted scaffold, and finally direct instruction. Exhausting the hierarchy triggers a Graceful Exit that finalizes the score for that interaction (awarding zero earned points, logged via the shadow ledger) but supplies the missing knowledge so the conversation proceeds, preventing a momentary recall lapse from capping the student's overall demonstration of mastery.

## Design Implications

### Context
#### Requirements
- An AI proctor that logs hint counts deterministically and can supply missing foundational knowledge without terminating the topic
#### Constraints
- Exhausting the hierarchy finalizes only that interaction's score; the proctor continues generating parallel prompts within the tier until the evidence buffer is satisfied

### Target Learners
- higher education students being assessed conversationally

### Target Learning Goals
- moving from unassisted to assisted performance within the zone of proximal development

### Affordances
- [Socratic Test Framework Bloom Solo Zpd](../research-methods/the-socratic-test-framework.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Ilya Mikhelson. (2026). The Theoretical Foundation of Socratic Tests: Dynamic, Multimodal, Conversational Examinations. https://arxiv.org/abs/2607.29624
