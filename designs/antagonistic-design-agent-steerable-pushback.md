---
type: design
id: antagonistic-design-agent-steerable-pushback
title: Antagonistic AI design agent with steerable stakeholder pushback in Miro
description: An LLM-powered agent built in Miro (Next.js, Miro SDK, GPT-4.1, Whisper, GPT-4o) that enacts constructive conflict for interaction design students.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: howard-ziyu-han-2026
    resource: "https://arxiv.org/abs/2608.04166"
    title: "Howard Ziyu Han, Nikolas Martelaro. (2026). Enacting Constructive Conflicts with AI Agents to Enhance Reconsideration among Novice Interaction Designers. https://arxiv.org/abs/2608.04166"
    author: Howard Ziyu Han, Nikolas Martelaro
---

# Antagonistic AI design agent with steerable stakeholder pushback in Miro

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An LLM-powered agent built in Miro (Next.js, Miro SDK, GPT-4.1, Whisper, GPT-4o) that enacts constructive conflict for interaction design students. In the Agent Intervention Space, "the agent generates a first round of four pushback points anchored in the designer's current proposal; the designer interacts with those points to steer the design direction; the agent then generates a second round informed by that steering." Each pushback point pairs a stakeholder perspective with a specific challenge. Designers steer via point-level tagging (useful, not useful, custom) and stance-level Consensus and Command frames. A sub-agent retrieves a database of prior constructive-conflict examples to ground critiques.

## Design Implications

### Context
#### Requirements
- Multimodal context gathering (text, visuals, think-aloud) so pushback is anchored in the designer's contextual exploration
- Steering mechanisms (tagging and Consensus/Command frames) so designers retain agency while engaging with critique
#### Constraints
- The agent could not infer relationships between linked ideas from think-aloud input
- It cannot show how common, important, or grounded synthetic concerns are in lived experience and does not substitute for engagement with the real public
- A few Miro actions not exposed by the open API were handled by the researcher via a predefined, bias-avoiding protocol

### Target Learners
- Novice interaction designers (design students trained in interaction design but novices at navigating stakeholder conflict)

### Learning Goals
- Engaging constructively with multi-stakeholder tension during early design ideation
- Reconsidering and revising design decisions in light of stakeholder pushback

### Claims
- [Antagonistic Agent Broadens Stakeholder Coverage](../claims/antagonistic-agent-broadens-stakeholder-coverage.md) [+M]
- [Idea Deletion Requires Stakeholder Friction](../claims/idea-deletion-requires-stakeholder-friction.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Howard Ziyu Han, Nikolas Martelaro. (2026). Enacting Constructive Conflicts with AI Agents to Enhance Reconsideration among Novice Interaction Designers. https://arxiv.org/abs/2608.04166
