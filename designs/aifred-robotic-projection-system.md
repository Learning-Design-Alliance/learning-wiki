---
type: design
id: aifred-robotic-projection-system
title: "AIfred: desk-based robotic arm with end-effector projector delivering spatially co-located generative AI assistance"
description: AIfred is a prototype combining a robotic arm with a mini projector at its end-effector, an OptiTrack motion-capture system tracking a desk object, and an overhead camera.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: gregorio-orlando-2026
    resource: "https://arxiv.org/abs/2609.38737"
    title: "Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737"
    author: Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer
---

# AIfred: desk-based robotic arm with end-effector projector delivering spatially co-located generative AI assistance

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
AIfred is a prototype combining a robotic arm with a mini projector at its end-effector, an OptiTrack motion-capture system tracking a desk object, and an overhead camera. It operates through a three-stage spatial assistance pipeline: workspace perception (MediaPipe gesture detection triggering a screenshot), context-aware content generation (Gemini models interpreting the scene under the active interaction mode), and robot-mediated projection onto the indicated desk location. Three interaction modes were programmed: math homework (scaffolding hints rather than answer replacement), generate image, and draw. All code and materials are publicly available in the article's stated repository.

## Design Implications

### Context
#### Requirements
- Requires workspace perception hardware: an overhead camera, a motion-capture system tracking the robot base and a trackable desk object, and an inverse kinematics solver to orient the projector
#### Constraints
- The OptiTrack motion-capture tracking limits deployment outside controlled lab settings, per the authors' limitations section
- The current design prioritizes functional projection over expressive robot behavior

### Target Learners
- university-campus adult participants across humanistic, social-science, business, and engineering backgrounds

### Learning Goals
- math problem solving on quadratic equations
- sketch-to-image generation
- drawing quality

### Claims
- [Aifred Higher Short Term Learning Transfer](../claims/aifred-higher-short-term-learning-transfer.md) [+M]
- [Aifred Drawing Quality Ranked First](../claims/aifred-drawing-quality-ranked-first.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737
