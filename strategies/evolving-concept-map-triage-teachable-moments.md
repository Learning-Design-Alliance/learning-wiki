---
type: strategy
id: evolving-concept-map-triage-teachable-moments
title: Maintain a per-developer evolving concept map to triage teachable moments and calibrate interventions
description: "SHIELD maintains a Developer's Evolving Concept Map, \"a per-developer representation of concepts the developer has previously demonstrated familiarity with, has been taught, or has been assessed on across past sessions\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: rohit-mehra-2026
    resource: "https://arxiv.org/abs/2607.06101"
    title: "Rohit Mehra, Samdyuti Suri, Prithviraj K Tagadinamani, Kapil Singi, Vikrant Kaulgud, Adam P. Burden. (2026). Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development. https://arxiv.org/abs/2607.06101"
    author: Rohit Mehra, Samdyuti Suri, Prithviraj K Tagadinamani, Kapil Singi, Vikrant Kaulgud, Adam P. Burden
---

# Maintain a per-developer evolving concept map to triage teachable moments and calibrate interventions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
SHIELD maintains a Developer's Evolving Concept Map, "a per-developer representation of concepts the developer has previously demonstrated familiarity with, has been taught, or has been assessed on across past sessions". The Teachability Triage Agent consults it to distinguish known concepts from genuine gaps, evaluates candidates against configurable teachability signals (complexity, novelty, transferability), and assessment outcomes update the map so concepts can be reinforced, deprioritized, or revisited.

## Design Implications

### Context
#### Requirements
- At cold start, the map can be initialized by analyzing code authored by the developer (not AI-generated), under the assumption that concepts present in that code are already familiar.
#### Constraints
- A concept absent from the map does not necessarily imply unfamiliarity, only that the system has not yet observed evidence of it, which motivates probe verification before teaching.

### Target Learners
- Software developers of varying expertise using AI coding agents

### Target Learning Goals
- Adaptive calibration of learning interventions to prior exposure and demonstrated familiarity

## Related Strategies

- Shield Multi Agent Incidental Learning System
- [Deliver learning through asynchronous out-of-band channels that preserve developer flow](out-of-band-async-learning-channels-preserve-flow.md)

## Examples
-

## Key Sources
- Rohit Mehra, Samdyuti Suri, Prithviraj K Tagadinamani, Kapil Singi, Vikrant Kaulgud, Adam P. Burden. (2026). Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development. https://arxiv.org/abs/2607.06101
