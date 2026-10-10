---
type: strategy
id: iterate-and-three-level-validation-ar-simulation-strategy
title: Iterate the prompt in plain language and validate the simulation on technical, physical, and pedagogical levels
description: "After generating a simulation from the four-element prompt, the teacher runs it, notices incorrect behavior, describes the problem in plain language, and sends a correction prompt; the article notes \"The loop itself i..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: ofek-levy-2026
    resource: "https://www.google.com/search?q=%22From+Prompt+to+Embodied+Simulation%22"
    title: "Ofek Levy, Joshua Glazer, Noah D. Finkelstein, and Yossi Ben-Zion. (2026). From Prompt to Embodied Simulation: Using Generative AI to Create AR Physics Learning Tools. https://www.google.com/search?q=%22From+Prompt+to+Embodied+Simulation%22"
    author: Ofek Levy, Joshua Glazer, Noah D. Finkelstein, and Yossi Ben-Zion
---

# Iterate the prompt in plain language and validate the simulation on technical, physical, and pedagogical levels

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
After generating a simulation from the four-element prompt, the teacher runs it, notices incorrect behavior, describes the problem in plain language, and sends a correction prompt; the article notes "The loop itself is short: run, notice what behaves incorrectly, describe the problem in plain language, and send a correction prompt." The result is then checked on three levels: a technical check (tracking and smooth mirrored motion), a physical check (correct relations between quantities, such as color ordering in the visible spectrum), and a pedagogical check (the gesture is natural and does not compete with the physics for attention).

## Design Implications

### Context
#### Requirements
- Willingness to run several prompt-and-correction iterations; two of the prompt's sentences were added this way, such as the phase-continuity requirement added after the wave shook with every wavelength change
#### Constraints
- AR simulations are especially sensitive to edge cases that appear only when a real hand moves in front of a real camera
- In class it helps to keep the hand at a roughly constant distance from the camera, where tracking is most stable

### Target Learners
- teachers designing physics demonstrations
- students generating their own simulations

### Target Learning Goals
- producing physically correct, stable, and pedagogically usable AR simulations of physics phenomena

## Related Strategies

- [Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives](ai-nocode-lab-software-development.md)

## Examples
-

## Key Sources
- Ofek Levy, Joshua Glazer, Noah D. Finkelstein, and Yossi Ben-Zion. (2026). From Prompt to Embodied Simulation: Using Generative AI to Create AR Physics Learning Tools. https://www.google.com/search?q=%22From+Prompt+to+Embodied+Simulation%22
