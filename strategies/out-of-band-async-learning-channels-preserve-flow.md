---
type: strategy
id: out-of-band-async-learning-channels-preserve-flow
title: Deliver learning through asynchronous out-of-band channels that preserve developer flow
description: "The article recommends that learning interventions \"surface through out-of-band channels such as asynchronous queues, feeds, or peripheral panels, rather than through blocking dialogs or interruptive prompts\", so that..."
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

# Deliver learning through asynchronous out-of-band channels that preserve developer flow

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that learning interventions "surface through out-of-band channels such as asynchronous queues, feeds, or peripheral panels, rather than through blocking dialogs or interruptive prompts", so that "the developer should choose when to engage, not the system". SHIELD implements this via its Probe Queue and Microlearning Feed, where items remain available for engagement at a time of the developer's choosing.

## Design Implications

### Context
#### Requirements
- Interventions must live within the developer's day-to-day environment, such as the IDE, so they can be noticed and engaged with quickly without a context switch.
#### Constraints
- Surfacing too frequently trains developers to ignore the system, undermining the learning it aims to support.

### Target Learners
- Software developers working with AI coding agents in an IDE

### Target Learning Goals
- Contextual concept learning during agent-assisted development without flow disruption

## Related Strategies

- Six Principles Incidental Learning Developer Agent
- [Maintain a per-developer evolving concept map to triage teachable moments and calibrate interventions](evolving-concept-map-triage-teachable-moments.md)
- [Architect teacher-in-the-loop agentic AI with escalation protocols, guardrail adjustability, and state-interruptibility](teacher-in-the-loop-agentic-architecture.md)
- [Asynchronous Voice](asynchronous_voice.md)

## Examples
-

## Key Sources
- Rohit Mehra, Samdyuti Suri, Prithviraj K Tagadinamani, Kapil Singi, Vikrant Kaulgud, Adam P. Burden. (2026). Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development. https://arxiv.org/abs/2607.06101
