---
type: design
id: augmented-bow-hold-aid-force-mapping
title: Augmented bow hold aid with finger pressure force mapping
description: A bow-mounted augmentation preserving the geometry of a traditional frog, using thin-film pressure sensors (e.g., Velostat) to produce a spatial force map across finger contact points and an IMU to capture bow orienta...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: shi-shi-lingyun-chen-zitao
    resource: "https://arxiv.org/abs/2607.18598"
    title: "Shi Shi, Lingyun Chen, Zitao Zhang, Amanda R. Draper, and Eli Blevis. 2026. Designing for What Cannot Be Seen: Supporting Embodied String Learning for Musicians with Blindness and Low-Vision. The 28th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '26). https://arxiv.org/abs/2607.18598"
---

# Augmented bow hold aid with finger pressure force mapping

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (2 qualitative), `q2` · 0 of 2 report an effect size

## Description
A bow-mounted augmentation preserving the geometry of a traditional frog, using thin-film pressure sensors (e.g., Velostat) to produce a spatial force map across finger contact points and an IMU to capture bow orientation and kinematics. By mapping where pressure concentrates and shifts, the system could infer finger placement and over-gripping patterns and provide real-time, low-attention feedback indicating which contact region is too tense and which finger to relax or reposition. It is framed as a temporary, practice-oriented scaffold for habit-building rather than a permanent replacement for conventional bow hold training.

## Design Implications

### Context
#### Requirements
- Must preserve compatibility with existing bows and minimal disruption to established motor habits, per the article's design rationale.
#### Constraints
- The enlarged grip volume is a stated tradeoff: prolonged use may lead players to adapt to a larger grip and feel discomfort returning to an unaugmented bow; M2 cautioned the aid might not transfer when removed and could deform correct posture.

### Target Learners
- Violin and viola learners with blindness and low-vision

### Learning Goals
- Relaxed bow hold, balanced load distribution across fingers, and reduced over-gripping

### Claims
- [Blv Bow Drift Late Detection Over Gripping](../claims/blv-bow-drift-late-detection-over-gripping.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Shi Shi, Lingyun Chen, Zitao Zhang, Amanda R. Draper, and Eli Blevis. 2026. Designing for What Cannot Be Seen: Supporting Embodied String Learning for Musicians with Blindness and Low-Vision. The 28th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '26). https://arxiv.org/abs/2607.18598
