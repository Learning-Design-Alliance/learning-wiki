---
type: design
id: qookies-ai-npc-rl-llm-architecture
title: AI NPC architecture combining reinforcement learning and an LLM via an embodiment interface
description: "The game's non-player character is controlled by two AI models: a generative chatbot (Llama 3.1 70B) prompted with the level's underlying concepts but not its solution, and a visual scaffolding model based on one-shot..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: caroline-wermann-2026
    resource: "https://arxiv.org/abs/2602.08893"
    title: "Caroline Wermann, Karina E. Avila, Sebastian André, Julia C. Draeger, Alvar Goetze, Jochen Kuhn, Maite Maurer, Sascha Mehlhase, Nikola Merkas, Fabian Schrodt, and Stefan Küchemann. (2026). AI-based Verbal and Visual Scaffolding in a Serious Game: Effects on Learning and Cognitive Load. arXiv preprint. https://arxiv.org/abs/2602.08893"
    author: Caroline Wermann, Karina E. Avila, Sebastian André, Julia C. Draeger, Alvar Goetze, Jochen Kuhn, Maite Maurer, Sascha Mehlhase, Nikola Merkas, Fabian Schrodt, and Stefan Küchemann
---

# AI NPC architecture combining reinforcement learning and an LLM via an embodiment interface

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The game's non-player character is controlled by two AI models: a generative chatbot (Llama 3.1 70B) prompted with the level's underlying concepts but not its solution, and a visual scaffolding model based on one-shot reinforcement learning. The architecture "combines reinforcement learning and a large language model via an embodiment interface, grounding dialogue and action generation in the current game state", which the authors state reduces hallucination risk and keeps dialogue aligned with game mechanics.

## Design Implications

### Context
#### Requirements
- The reinforcement learning component is initialized without prior task-specific knowledge and learns from gameplay observation, so it cannot help in new situations
#### Constraints
- Because the action AI must first learn from the player, it cannot help in new situations, which the authors note may discourage first-time users

### Target Learners
- school students
- university students
- general public players of Qookies

### Learning Goals
- quantum technology concepts supported through verbal explanation and visual action demonstration

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Caroline Wermann, Karina E. Avila, Sebastian André, Julia C. Draeger, Alvar Goetze, Jochen Kuhn, Maite Maurer, Sascha Mehlhase, Nikola Merkas, Fabian Schrodt, and Stefan Küchemann. (2026). AI-based Verbal and Visual Scaffolding in a Serious Game: Effects on Learning and Cognitive Load. arXiv preprint. https://arxiv.org/abs/2602.08893
