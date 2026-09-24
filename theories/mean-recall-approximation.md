---
type: theory
title: Mean-Recall Approximation for the Leitner Queue Network
description: "The mean-recall approximation is the article's heuristic that treats each Leitner deck as an M/M/1 queue, replacing each item's true delay with an exponential draw so recall probability becomes a function of deck serv..."
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

# Mean-Recall Approximation for the Leitner Queue Network

> **Theory** · [All theories](index.md)

## Description
The mean-recall approximation is the article's heuristic that treats each Leitner deck as an M/M/1 queue, replacing each item's true delay with an exponential draw so recall probability becomes a function of deck service and input rates. Under it, "the problem of choosing an optimal review schedule reduces to a low-dimensional deter- ministic optimization problem" that a nonlinear solver can solve.

## Design Implications

### Context
#### Requirements
- Arrival and input rates below each deck's service rate so that queues are ergodic.
- Flow-balance equations linking deck input rates to recall probabilities.
- A known item difficulty θ and review budget U to solve the static planning problem.
#### Constraints
- The approximation is essentially a heuristic; more rigorous approximations are an open topic for future work.
- Simulations suggest it matches the clocked-delay model closely only for small arrival rates.
- If a deck's input rate is not below its service rate, that deck's size and review delays grow unbounded.

### Target Learners
- Learners using spaced repetition flashcard systems in the long-term learning regime

### Target Learning Objectives
- Optimizing flashcard review schedules to maximize the rate of learning

### Claims
- [Mean Recall Approximation Matches Clocked Delay Simulation At Low Arrival Rates](../claims/mean-recall-approximation-matches-clocked-delay-simulation-at-low-arrival-rates.md) [~W]
- [Optimal Leitner Schedule Reviews Lower Decks More Often](../claims/optimal-leitner-schedule-reviews-lower-decks-more-often.md) [+W]
- [Optimal Leitner Schedule Expands Intervals Between Reviews](../claims/optimal-leitner-schedule-expands-intervals-between-reviews.md) [+W]

## Related Theories
- [Leitner Queue Network](leitner-queue-network.md)

## Examples
-

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
