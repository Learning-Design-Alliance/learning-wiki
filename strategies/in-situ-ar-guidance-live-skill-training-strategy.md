---
type: strategy
id: in-situ-ar-guidance-live-skill-training-strategy
title: "Deliver real-time, parameter-specific feedback at the learner's line of sight during live physical-skill practice, then test unassisted"
description: "The article's implications point to AR systems that support in-situ, embodied skill training: overlay real-time feedback on the four core motor parameters directly at the welder's line of sight, scaffold parameters on..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: chuhan-franklin-xu-2026
    resource: "https://doi.org/10.1145/3772318.3791913"
    title: "Chuhan (Franklin) Xu, Lia Sparingga Purnamasari, Zhenfang Chen, Daragh Byrne, Dina El-Zanfaly. (2026). WeldAR: Augmenting Live Hands-On Training with In-Situ Guidance for Novice Learners. CHI 2026. https://doi.org/10.1145/3772318.3791913"
    author: Chuhan (Franklin) Xu, Lia Sparingga Purnamasari, Zhenfang Chen, Daragh Byrne, Dina El-Zanfaly
---

# Deliver real-time, parameter-specific feedback at the learner's line of sight during live physical-skill practice, then test unassisted

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article's implications point to AR systems that support in-situ, embodied skill training: overlay real-time feedback on the four core motor parameters directly at the welder's line of sight, scaffold parameters one at a time before combining them, and include an unassisted mode for benchmarking transfer. The study showed AR guidance improved both assisted practice and unassisted test performance, primarily driven by gains in travel speed and work angle, supporting novices in carrying embodied knowledge into independent tasks.

## Design Implications

### Context
#### Requirements
- Head-tracked, low-latency pass-through AR with sensing of the target skill parameters in real time
- Target ranges defined from domain standards to drive feedback triggers and proficiency evaluation
#### Constraints
- Benefits were parameter-specific: CTWD showed no significant effects and travel angle only a marginal trend in the unassisted test
- Some participants experienced visual information overload when four indicators appeared at once and physical fatigue from headset weight

### Target Learners
- Novices in vocational trades training, such as beginner MIG welding students

### Target Learning Goals
- Embodied motor-skill parameters (tool distance, angles, speed) and their transfer to unassisted performance

## Claims

- [AR guidance during live welding produced significantly better unassisted test performance than video instruction, driven by work angle and travel speed](../claims/ar-guidance-better-unassisted-test-performance.md) [+M]
- [AR guidance produced significantly better assisted combination-session performance than video, with travel speed and work angle as primary drivers](../claims/ar-better-assisted-combination-performance.md) [+M]
- [Interviews identified AR's real-time guidance as improving accessibility and confidence, while noting visual overload and game-like distance as trade-offs](../claims/ar-interview-accessibility-confidence-tradeoffs.md) [+W]
- [Participants trained under AR guidance acquired correct welding skills more rapidly, with a significantly steeper learning curve](../claims/ar-steeper-learning-curve.md) [+M]

## Related Strategies

- [Provide real-time multimodal feedback during early training, then withdraw guidance for unassisted assessment to prevent over-reliance](guided-practice-then-unassisted-assessment.md)
- [Provide real-time visual warnings when grip force exceeds a threshold during instrument practice](real-time-grip-force-warning-strategy.md)
- [Deliver real-time multi-dimensional AI scores with explanatory feedback during counselor practice on resistance moments](realtime-ai-feedback-counselor-resistance-practice.md)
- [Embed immediate corrective feedback in virtual simulation practice sessions](real-time-corrective-feedback-virtual-simulation.md)

## Examples
-

## Key Sources
- Chuhan (Franklin) Xu, Lia Sparingga Purnamasari, Zhenfang Chen, Daragh Byrne, Dina El-Zanfaly. (2026). WeldAR: Augmenting Live Hands-On Training with In-Situ Guidance for Novice Learners. CHI 2026. https://doi.org/10.1145/3772318.3791913
