---
type: design
id: cogevolution-agent-framework
title: "CogEvolution framework: ICAP perception, IRT-based memory retrieval, and evolutionary cognitive state update"
description: CogEvolution is a generative educational agent architecture that shifts from static personas to dynamic cognitive flow.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: wei-zhang-2026
    resource: "https://arxiv.org/abs/2604.14786v1"
    title: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786v1"
    author: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang"
---

# CogEvolution framework: ICAP perception, IRT-based memory retrieval, and evolutionary cognitive state update

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
CogEvolution is a generative educational agent architecture that shifts from static personas to dynamic cognitive flow. It "consists of three highly coupled components": a Cognitive Adapter for depth perception mapping interaction features to a probability distribution over the four ICAP levels; an IRT-Driven Memory Retrieval Module that scores hybrid semantic and structural (item-characteristic-curve) similarity to decide whether to reuse an old schema or trigger confusion and exploration; and an Evolutionary Cognitive State Update Mechanism using a mutation-selection-update cycle in which LLM-generated cognitive hypotheses are fitness-evaluated under a ZPD constraint and integrated with a step size set by the ICAP-based cognitive evolution rate. The update magnitude depends on cognitive engagement depth: passive participation yields minor mutations while constructive participation allows significant structural restructuring.

## Design Implications

### Context
#### Requirements
- Perceived cognitive conflict (input not fully explained by the current knowledge structure) to trigger mutation
- A ZPD-formalized search radius constraining hypothesis fitness, penalizing excessive leaps or stagnation
- A memory bank of interaction quadruples and a structural-similarity threshold for schema reuse
#### Constraints
- Evaluated on eighth-grade mathematics practice data (CogMath-948); the article's claims are about simulated student cognitive evolution in that setting

### Target Learners
- simulated eighth-grade math students
- novice teachers via student simulation

### Learning Goals
- modeling knowledge internalization, transfer, and cognitive state transitions during practice

### Claims
- [Cogevolution Mistake Precision Beats Kt Baseline](../claims/cogevolution-mistake-precision-beats-kt-baseline.md) [+M]
- [Cogevolution Learning Curve Power Law Fit](../claims/cogevolution-learning-curve-power-law-fit.md) [+M]
- [Cogevolution Ablation Module Contributions](../claims/cogevolution-ablation-module-contributions.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786v1
