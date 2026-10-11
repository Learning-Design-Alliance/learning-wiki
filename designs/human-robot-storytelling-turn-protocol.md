---
type: design
id: human-robot-storytelling-turn-protocol
title: Six-phase turn-taking narrative interaction protocol for human-robot story co-creation
description: "A reusable interaction structure for a joint human-robot storytelling session, organised in six phases: introduction (task explanation and partner detection), iCub turn (robot asks for, grasps and identifies the first..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: maria-lombardi-2025
    resource: "https://arxiv.org/abs/2508.02505"
    title: "Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505"
    author: Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska
---

# Six-phase turn-taking narrative interaction protocol for human-robot story co-creation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A reusable interaction structure for a joint human-robot storytelling session, organised in six phases: introduction (task explanation and partner detection), iCub turn (robot asks for, grasps and identifies the first cube and starts the story), human turn (participant chooses the second cube and continues the story while listened to), a further iCub turn for the final cube and ending, a wrap-up phase in which iCub recaps the jointly generated story, and a closure phase in which iCub greets the participant, expressing joy. Phases 2-5 repeat for each trial, so the pattern scales to multiple stories per session.

## Design Implications

### Context
#### Requirements
- Perception modules for face recognition, cube detection and sticker identification so the robot can track turns and respond to the chosen image
- Speech-to-text and text-to-speech modules so the robot can listen to and narrate story pieces
#### Constraints
- The protocol was validated with adult participants as a feasibility step before deployment with children

### Target Learners
- children under 10 in educational and rehabilitation protocols, including autistic children

### Learning Goals
- turn taking, collaborative narrative creation, and communication skills

### Claims
- [Icub Stories Liked And Coherent Ratings](../claims/icub-stories-liked-and-coherent-ratings.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505
