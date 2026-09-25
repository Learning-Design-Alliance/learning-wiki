---
type: principle
id: maximize-learning-rate-when-calibrating-leitner-schedules
title: Maximize Learning Rate When Calibrating Leitner Review Schedules
description: "The article proposes the maximum speed of learning as the design target for spaced repetition software: its formalization \"suggests the maximum speed of learning as a natural design metric for spaced rep- etition soft..."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T"
---

# Maximize Learning Rate When Calibrating Leitner Review Schedules

> **Principle** · [All principles](index.md)

## Description
The article proposes the maximum speed of learning as the design target for spaced repetition software: its formalization "suggests the maximum speed of learning as a natural design metric for spaced rep- etition software". Deck review rates and the new-item rate are calibrated with a queueing-theory program rather than heuristics, and the new-item rate should stay below the phase-transition threshold.

## Design Implications

### Context
#### Requirements
- A model of recall as a function of deck position and delay, and estimates of item difficulty and the learner's review budget.
- Solving the static planning problem to set deck review rates and new-item arrival rate.
#### Constraints
- The authors call for better approximations of the Leitner Queue Network with rigorous performance guarantees, and policies for the transient regime such as cramming.
- The authors say more extensive experimentation is needed to understand how closely these models apply to real-world settings.
- In the experiment the authors could not optimize review rates ex ante because item difficulty and review budget were unknown.

### Target Learners
- Learners memorizing many items with spaced repetition software, e.g., foreign-language vocabulary

### Target Learning Objectives
- Maximizing the rate of mastered items in long-term learning

### Claims
- [Leitner Queue Network Phase Transition In Learning Rate](../claims/leitner-queue-network-phase-transition-in-learning-rate.md) [+M]
- [Excess New Item Rate Leaves Items Stuck In First Leitner Deck](../claims/excess-new-item-rate-leaves-items-stuck-in-first-leitner-deck.md) [+M]
- [Optimal Leitner Schedule Reviews Lower Decks More Often](../claims/optimal-leitner-schedule-reviews-lower-decks-more-often.md) [+W]

## Related Principles
- [Spaced Repetition Scheduling](../strategies/spaced-repetition-scheduling.md)
- [Spaced Learning](spaced-learning.md)
- [Leitner Queue Network](../theories/leitner-queue-network.md)

## Examples
-

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
