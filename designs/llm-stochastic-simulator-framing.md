---
type: design
id: llm-stochastic-simulator-framing
title: "LLMs as stochastic simulators: the secret object is emergent, not a fixed hidden variable"
description: "Building on Murray Shanahan's framing of LLMs as \"stochastic simulators rather than symbolic reasoners\", the article characterizes LLM answers as a random variable sampled from a conditional probability distribution a..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: tufino-2026
    resource: "https://github.com/etufino/AI-20-questions-game"
    title: "Tufino, E. (2026). Demystifying the oracle: A \"20 Questions\" game to promote AI ethics and literacy. https://github.com/etufino/AI-20-questions-game"
    author: Tufino, E
---

# LLMs as stochastic simulators: the secret object is emergent, not a fixed hidden variable

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Building on Murray Shanahan's framing of LLMs as "stochastic simulators rather than symbolic reasoners", the article characterizes LLM answers as a random variable sampled from a conditional probability distribution a ~ P(a|H, q, T), dependent on interaction history H, the current question q, and temperature T. In the game, the system prompt says the model is "thinking of an object" yet no object is fixed at initialization, so the secret object is an emergent property of the conversation trajectory rather than a hidden variable to be uncovered. This mirrors Wheeler's "surprise version" of 20 Questions, where reality emerges constructively from the questions asked.

## Design Implications

### Context
#### Requirements
- Understanding requires observing behavior under identical histories, which the app's re-sample and restart functions make possible; standard chat interfaces mask uncertainty and present a coherent single stream of text.
#### Constraints
- The authors caution that "frontier models can display behaviors that resemble reasoning or agency", so the framing should not be overextended.

### Target Learners
- high school and undergraduate physics students

### Learning Goals
- understanding LLM generation mechanics
- replacing the retrieval/oracle mental model with a generative probabilistic model

### Claims
- [Llm Resampling Reveals Stochastic Flips](../claims/llm-resampling-reveals-stochastic-flips.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Tufino, E. (2026). Demystifying the oracle: A "20 Questions" game to promote AI ethics and literacy. https://github.com/etufino/AI-20-questions-game
