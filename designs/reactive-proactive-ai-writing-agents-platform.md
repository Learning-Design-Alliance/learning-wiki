---
type: design
id: reactive-proactive-ai-writing-agents-platform
title: Reactive and proactive AI writing agents on a minimalist multimodal writing platform
description: "The study developed two AI agents that manipulated conversational initiative while holding other features constant: both used the same interface, visual inputs, VizChat architecture, Retrieval-Augmented Generation pip..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: yueqiao-jin-2025
    resource: "https://arxiv.org/abs/2507.04398"
    title: "Yueqiao Jin, Kaixun Yang, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan. (2025). The Agency Gap in AI-Supported Writing: How Reactive and Proactive Agent Designs Shape Multimodal Reasoning. https://arxiv.org/abs/2507.04398"
    author: Yueqiao Jin, Kaixun Yang, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan
---

# Reactive and proactive AI writing agents on a minimalist multimodal writing platform

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The study developed two AI agents that manipulated conversational initiative while holding other features constant: both used the same interface, visual inputs, VizChat architecture, Retrieval-Augmented Generation pipeline, visualisation knowledge base, and multimodal GPT-4o model. The reactive agent generated only when the learner messaged; the proactive agent followed an expert-authored conversational state sequence, initiating orientation and ordered guiding questions per visual and giving confirmatory, clarifying, or corrective feedback grounded in visual evidence. The platform comprised a display area, a writing space, and a condition-specific chat or instructions component.

## Design Implications

### Context
#### Requirements
- Requires the same underlying model, retrieval pipeline, and task materials across conditions so the contrast isolates who initiates and sequences support
#### Constraints
- The proactive sequence's triggering events, question order, target knowledge, and completion rules were fixed across participants; the prompt prohibited asking about non-displayed visuals and repeating questions

### Target Learners
- medical and nursing students interpreting healthcare simulation visualisations

### Learning Goals
- multimodal analytical writing from data visualisations

### Claims
- [Proactive Agent Dialogues Integrated Epistemic Reasoning](../claims/proactive-agent-dialogues-integrated-epistemic-reasoning.md) [+M]
- [Proactive Engagement Constructive Adequate Reasoning Link](../claims/proactive-engagement-constructive-adequate-reasoning-link.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yueqiao Jin, Kaixun Yang, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan. (2025). The Agency Gap in AI-Supported Writing: How Reactive and Proactive Agent Designs Shape Multimodal Reasoning. https://arxiv.org/abs/2507.04398
