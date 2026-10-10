---
type: strategy
id: hybrid-rule-llm-radiotelephony-evaluation
title: Use AI-assisted hybrid evaluation (deterministic rules plus LLM analysis) to scale standardized radiotelephony assessment
description: "ASTRA's evaluation workflow assesses each trainee command through a hybrid of deterministic rules and LLMs: rule-based penalties enforce ICAO phraseology and numerical correctness, while a DSPy-optimized LLM evaluates..."
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

# Use AI-assisted hybrid evaluation (deterministic rules plus LLM analysis) to scale standardized radiotelephony assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
ASTRA's evaluation workflow assesses each trainee command through a hybrid of deterministic rules and LLMs: rule-based penalties enforce ICAO phraseology and numerical correctness, while a DSPy-optimized LLM evaluates semantic correctness, contextual intent, and linguistic nuance, with BERT-based semantic similarity providing a consistent similarity signal. "This hybrid approach ensures bothprecision(through rule enforcement) andflexibility(through contextual reasoning)", and the framework scores five metrics — accuracy, brevity, completeness, safety adherence, and route compliance — on a 0-100 scale with weighted penalty aggregation.

## Design Implications

### Context
#### Requirements
- Structured prompting via DSPy to constrain LLM outputs and reduce evaluation variability
- BERT-based contextual embeddings to stabilize semantic similarity assessment
#### Constraints
- The framework covers only aspects objectively inferable from radiotelephony and simulator state; higher-order competencies like planning ability and conflict resolution are outside scope
- Rule-based approaches alone cannot effectively capture linguistic variation and contextual intent

### Target Learners
- Air traffic control operator trainees

### Target Learning Goals
- ICAO-standard radiotelephony phraseology and structure
- Safety-compliant, route-consistent control instructions

## Related Strategies

- [Adaptive scenario generation: introduce training scenarios targeting weaknesses identified from real-time performance metrics](astra-adaptive-scenario-generation.md)

## Examples
-

## Key Sources
- Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319
