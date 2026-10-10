---
type: strategy
id: astra-adaptive-scenario-generation
title: "Adaptive scenario generation: introduce training scenarios targeting weaknesses identified from real-time performance metrics"
description: Rather than relying solely on fixed scenarios, ASTRA proposes automatically generating training situations from trainee performance.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: ethan-chew-2026
    resource: "https://arxiv.org/abs/2606.18319"
    title: "Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319"
    author: Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim
---

# Adaptive scenario generation: introduce training scenarios targeting weaknesses identified from real-time performance metrics

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Rather than relying solely on fixed scenarios, ASTRA proposes automatically generating training situations from trainee performance. "By analyzing real- time interactions and RT performance metrics, the system identifies performance gaps and dy- namically introduces scenarios that target specific weaknesses.", creating a closed-loop training environment that continuously adapts to trainee competency without direct instructor intervention. For example, a trainee struggling with altitude management may be presented with scenarios of increased altitude-control complexity.

## Design Implications

### Context
#### Requirements
- Real-time capture of trainee interactions and radiotelephony performance metrics to detect performance gaps
#### Constraints
- Presented as future work rather than an implemented and evaluated capability

### Target Learners
- Air traffic control operator trainees

### Target Learning Goals
- Closing individual performance gaps such as altitude management

## Related Strategies

- [Scenario Based Training](scenario-based-training.md)
- [Use AI-assisted hybrid evaluation (deterministic rules plus LLM analysis) to scale standardized radiotelephony assessment](hybrid-rule-llm-radiotelephony-evaluation.md)

## Examples
-

## Key Sources
- Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319
