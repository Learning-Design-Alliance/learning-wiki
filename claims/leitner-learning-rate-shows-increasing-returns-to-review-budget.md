---
type: claim
title: "Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets."
description: "Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets."
id: leitner-learning-rate-shows-increasing-returns-to-review-budget
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: weak
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T."
    q: 1
    i: "?"
---

# Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` The optimized learning rate plotted against review budget U (n = 5, θ = 0.01) is convex for low U, suggesting increasing returns as budget grows. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q1 · i?`

Optimization result under the mean-recall approximation (Fig. 11). The convexity "suggests that there are increasing returns (for lower U) as the user increases their budget".

> "The convexity of the latter plot is encouraging, as it suggests that there are increasing returns (for lower U) as the user increases their budget."

## Discussion


## Related Claims
- [In simulation, the mean-recall approximation matches the clocked-delay Leitner Queue Network for small arrival rates, and its phase-transition threshold appears to be a conservative lower bound.](mean-recall-approximation-matches-clocked-delay-simulation-at-low-arrival-rates.md) — related
- [Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.](optimal-leitner-schedule-reviews-lower-decks-more-often.md) — related
- [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](optimal-leitner-schedule-expands-intervals-between-reviews.md) — related
- [Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.](leitner-queue-network-phase-transition-in-learning-rate.md) — related
- [Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.](optimal-leitner-deck-allocation-depends-on-item-difficulty.md) — related
