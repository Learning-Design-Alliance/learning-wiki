---
type: theory
title: Leitner Queue Network
description: "The Leitner Queue Network is the article's stochastic model of a spaced repetition system, embedding an exponential forgetting curve in a network of queues, one per Leitner deck; it is \"based on ideas from queueing th..."
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

# Leitner Queue Network

> **Theory** · [All theories](index.md)

## Description
The Leitner Queue Network is the article's stochastic model of a spaced repetition system, embedding an exponential forgetting curve in a network of queues, one per Leitner deck; it is "based on ideas from queueing theory and job scheduling". New items enter deck 1, recalled items move up, forgotten items move down, and a static schedule chooses an arrival rate and per-deck review rates to maximize the rate of mastered items.

## Design Implications

### Context
#### Requirements
- A review frequency budget U divided between new items and deck reviews, with review instances following a Poisson process.
- Restriction to static scheduling policies: an arrival rate for new items and a service rate per deck.
- The exponential forgetting curve with deck position as memory strength to set recall probabilities.
#### Constraints
- The article focuses on the long-term learning regime, where available items far outnumber the learner's time to memorize them.
- It assumes a single global item difficulty for simplicity; item-specific difficulty is handled by discretizing into bins and running parallel networks.
- The time-inhomogeneous Markov chain does not admit a closed-form program for optimizing the review schedule without an approximation.

### Target Learners
- Learners memorizing a very large set of items with flashcard software, e.g., foreign-language vocabulary

### Target Learning Objectives
- Long-term retention and mastery of many flashcard items
- Designing review schedules for spaced repetition software

### Claims
- [Leitner Queue Network Phase Transition In Learning Rate](../claims/leitner-queue-network-phase-transition-in-learning-rate.md) [+M]
- [Mean Recall Approximation Matches Clocked Delay Simulation At Low Arrival Rates](../claims/mean-recall-approximation-matches-clocked-delay-simulation-at-low-arrival-rates.md) [~W]

## Related Theories
- [Spaced Repetition](../elements/spaced-repetition.md)
- [Spaced Repetition Scheduling](../strategies/spaced-repetition-scheduling.md)
- [Flashcards](../strategies/flashcards.md)

## Examples
-

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
