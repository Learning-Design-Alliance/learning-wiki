---
type: design
id: icub-llm-narrative-storytelling-system
title: iCub LLM-powered narrative HRI system architecture
description: A companion-like social robotic platform in which the iCub humanoid and a human partner co-create a story in turn from pictures on nine soft cubes, each story built on a sequence of three cubes.
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

# iCub LLM-powered narrative HRI system architecture

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A companion-like social robotic platform in which the iCub humanoid and a human partner co-create a story in turn from pictures on nine soft cubes, each story built on a sequence of three cubes. Perception modules run online from the robot's own eye camera: face recognition (OpenPose, FaceNet embeddings, an SVM classifier), mutual-gaze detection from 19 facial key-points, online-trainable object detection, and zero-shot sticker description via ChatGPT-4o as VLM. Story generation uses ChatGPT-4o as LLM with ad-hoc prompts, plus speech transcription and synthesis, all orchestrated by a finite state machine over the YARP middleware. The article states the design 'allows to change stimuli fast without training the system again, representing a future easily adaptive tool for therapists.'

## Design Implications

### Context
#### Requirements
- A local network connecting the robot to a GPU-equipped workstation and client laptop running the perception and generation modules
- Online-trainable perception so the system is not constrained to a pre-trained subset of partners or objects
#### Constraints
- All perception uses only RGB frames from iCub's eye, without external sensors
- Latency from external services such as ChatGPT and slow motor movement affected perceived efficiency

### Target Learners
- children under 10, including children diagnosed with autism spectrum disorder (intended end users)

### Learning Goals
- communication skills, turn taking, autonomy, and narrative expression through collaborative storytelling

### Claims
- [Icub Storytelling System Success Rates](../claims/icub-storytelling-system-success-rates.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505
