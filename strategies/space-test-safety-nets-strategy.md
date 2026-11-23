---
type: strategy
id: space-test-safety-nets-strategy
title: Use space-specific safety nets — time-tagged recovery commands and passively safe RPO trajectories — to drive down risk in experimental space test
description: AFRL/RV uses safety nets regularly in experimental space test to drive down risk when executing procedures with uncertain outcomes.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: nayak-2020
    resource: "https://scholar.google.com"
    title: "Nayak, M., Straight, C., Kent, E., & Langhals, J. (2020). How to Train your Space Tester: Big Picture Challenges Facing Space Vehicle Test. https://scholar.google.com"
    author: "Nayak, M., Straight, C., Kent, E., & Langhals, J"
---

# Use space-specific safety nets — time-tagged recovery commands and passively safe RPO trajectories — to drive down risk in experimental space test

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (1 causal, 1 review, 1 associational), `q1`–`q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
AFRL/RV uses safety nets regularly in experimental space test to drive down risk when executing procedures with uncertain outcomes. One method is to upload time-tagged commands that "put the vehicle back to a known state" before higher-risk activities, so the crew can expect autonomous recovery and communication at a known time. Another is "passively safe" trajectories for Rendezvous and Proximity Operations, where guidance defaulting to off lets the vehicle naturally drift away from the other object.

## Design Implications

### Context
#### Requirements
- Methods must be baked into the test program and plan from the beginning
- Fault responses must be managed carefully by an experienced operator to work as intended
#### Constraints
- A triggered fault response may not be desirable when the test team intends the vehicle to be stretched to its limits
- Telemetry is intermittent due to limited ground antenna contact periods

### Target Learners
- space test operators
- spacecraft operations crews

### Target Learning Goals
- executing higher-risk test procedures safely
- managing fault detection systems during test

## Claims

- [Students perceived the gamified quizzes as a risk-free anonymous environment for practicing histology without fear of judgment](../claims/kahoot-risk-free-anonymous-practice-environment.md) [+W]
- [Virtual dissection tables allow students to practice procedures in a low-risk environment where errors can be recognized and virtually reverted without consequences](../claims/vdt-low-risk-error-recovery-practice.md) [+W]
- [For some students, AI-generated feedback reduces the perceived personal risk of exposing weaknesses, functioning as a psychologically safe space for feedback seeking](../claims/ai-feedback-reduces-perceived-personal-risk.md) [+W]

## Related Strategies

- [Build space test proficiency through simulators first, then shadowing by seasoned operators during high-tempo activities (the backseat IP model)](simulator-then-backseat-ip-space-test-training.md)

## Examples
-

## Key Sources
- Nayak, M., Straight, C., Kent, E., & Langhals, J. (2020). How to Train your Space Tester: Big Picture Challenges Facing Space Vehicle Test. https://scholar.google.com
