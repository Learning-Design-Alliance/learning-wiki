---
type: strategy
id: wac-central-hands-on-platform-strategy
title: Use a centrally administered hands-on platform with pre-installed software and real-time monitoring
description: For large-scale hands-on events, the team prefers a central platform with carefully tuned software environments and real-time staff monitoring over cloud, VM, or Docker environments, which push configuration responsib...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: john-urbanic-2023
    resource: "https://arxiv.org/abs/2402.03343"
    title: "John Urbanic, Thomas Maiden, Valerie Rossi. (2023). Evaluating the Wide Area Classroom After 24,000 HPC Students. Pittsburgh Supercomputing Center. https://arxiv.org/abs/2402.03343"
    author: John Urbanic, Thomas Maiden, Valerie Rossi
---

# Use a centrally administered hands-on platform with pre-installed software and real-time monitoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
For large-scale hands-on events, the team prefers a central platform with carefully tuned software environments and real-time staff monitoring over cloud, VM, or Docker environments, which push configuration responsibilities onto students. All software and examples "are in place when the students log on", so learners are never distracted by installation or configuration issues, and configuration errors can be corrected class-wide without student intervention.

## Design Implications

### Context
#### Requirements
- System administrators able to observe and correct any individual student's problem, and real-time monitoring of student status to eliminate system-wide issues and guide pacing
#### Constraints
- The WAC is platform-agnostic; the authors expect that as cloud resources evolve many issues may recede and cloud may eventually become the preferred platform

### Target Learners
- Hundreds of workshop students expected to begin hands-on exercises immediately after lecture

### Target Learning Goals
- Immediate hands-on practice on leading-edge hardware without setup delays

## Claims

- [The Wide Area Classroom delivered 106 events to just over 24,000 students at 90 different sites over ten years](../claims/wac-106-events-24000-students-90-sites.md) [+W]
- [Post-event evaluations show high satisfaction, with all survey ratings well over 4 out of 5 across the four rotating workshops](../claims/wac-evaluations-over-4-of-5.md) [+W]
- [Entrants in the follow-on hybrid computing challenge consistently demonstrate significant performance gains via parallelization](../claims/wac-hybrid-challenge-performance-gains.md) [+W]

## Related Strategies

- [Minimize platform-specific friction in workshop exercise materials](wac-content-design-guidelines-strategy.md)
- [Teach PennyLane through a Docker-based environment and the Xanadu Codebook with in-class codercises](pennylane-xanadu-codebook-strategy.md)

## Examples
-

## Key Sources
- John Urbanic, Thomas Maiden, Valerie Rossi. (2023). Evaluating the Wide Area Classroom After 24,000 HPC Students. Pittsburgh Supercomputing Center. https://arxiv.org/abs/2402.03343
