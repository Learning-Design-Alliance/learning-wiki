---
type: design
id: role-engineering-llm-paradigm
title: "Role engineering: providing an LLM a role and script rather than programming it"
description: Role engineering is the paradigm of customizing a general-purpose LLM by assigning it a role to perform, with instructions acting as a script.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2025
    resource: "https://arxiv.org/abs/2507.05795"
    title: "Eugenio Tufino, Bor Gregorcic. (2025). Creating a customisable Socratic AI physics tutor. https://arxiv.org/abs/2507.05795"
    author: Eugenio Tufino, Bor Gregorcic
---

# Role engineering: providing an LLM a role and script rather than programming it

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Role engineering is the paradigm of customizing a general-purpose LLM by assigning it a role to perform, with instructions acting as a script. As the authors put it, "rather than programming an AI, we are providing it with a role to perform", exploiting the LLM's ability to generate text statistically consistent with an expert character. The paper applies this by scripting a collaborative Socratic physics tutor within Google's Gemini Gems feature, and cites evidence that expert personas enhance zero-shot performance. The authors interpret the resulting step-by-step Socratic guidance as an implicit activation of the model's reasoning process.

## Design Implications

### Context
#### Requirements
- A detailed instruction script defining the role and persona, iteratively refined via a test window
#### Constraints
- The AI's performance should be interpreted as a convincing simulation of understanding, not genuine cognition
- A persistent rate of factual inaccuracy remains, so the tutor may occasionally provide flawed reasoning

### Target Learners
- physics students at secondary or university level

### Learning Goals
- Socratic conceptual reasoning and problem-solving in physics

### Claims
- [Role Engineered Gem Socratic Vs Standard Gemini](../claims/role-engineered-gem-socratic-vs-standard-gemini.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Eugenio Tufino, Bor Gregorcic. (2025). Creating a customisable Socratic AI physics tutor. https://arxiv.org/abs/2507.05795
