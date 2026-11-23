---
type: design
id: llm-npc-score-feedback-model-pattern
title: LLM-based NPC score feedback model combining safety gate, difficulty multiplier and multi-component evaluation
description: "A reusable scoring pattern for LLM-driven dialogue games: each round's score is computed as a safety gate (0 or 1) times a difficulty multiplier (0.8, 1, 1.2) times an evaluation score capped at 10, where the evaluati..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: ting-chen-hsu-2026
    resource: "https://arxiv.org/abs/2605.11562"
    title: "Ting-Chen Hsu. (2026). A generative AI driven interactive narrative serious game for stress relief and its randomized controlled pilot study. https://arxiv.org/abs/2605.11562"
    author: Ting-Chen Hsu
---

# LLM-based NPC score feedback model combining safety gate, difficulty multiplier and multi-component evaluation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A reusable scoring pattern for LLM-driven dialogue games: each round's score is computed as a safety gate (0 or 1) times a difficulty multiplier (0.8, 1, 1.2) times an evaluation score capped at 10, where the evaluation combines a base score, a penalty for off-topic responses, cognitive restructuring completion, engagement level, and progress versus the previous round. The author states the aim was "To improve the interpretability of NPC score feedback in the game", with component values in defined ranges and operational criteria per component.

## Design Implications

### Context
#### Requirements
- Operational scoring criteria for each component (Ct, Et, Pt) defined in advance
- Structured JSON output fields so the client can parse and update scores
#### Constraints
- Single-round evaluation scores are capped at 10 points to prevent excessively high single score bonuses from affecting the game's rhythm
- A minimum interval of 5 conversation rounds between mini-game invocations to prevent player fatigue

### Target Learners
- college students playing an LLM-driven dialogue game

### Learning Goals
- sustained engagement in CBT-informed stress-relief dialogue

### Claims
- 

## Related Designs
- Reverie Genai Cbt Serious Game

## Examples
-

## Key Sources
- Ting-Chen Hsu. (2026). A generative AI driven interactive narrative serious game for stress relief and its randomized controlled pilot study. https://arxiv.org/abs/2605.11562
