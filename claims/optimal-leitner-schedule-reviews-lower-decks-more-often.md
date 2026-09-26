---
type: claim
title: Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.
description: Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.
id: optimal-leitner-schedule-reviews-lower-decks-more-often
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

# Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` Optimizing the static planning problem (n = 20, U = 1, θ = 0.01 in Fig. 7) yields a schedule that spends more time on lower decks than higher decks. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q1 · i?`

Optimization result under the mean-recall approximation, shown for one parameter setting (Fig. 7). "the optimal schedule spends more time on lower decks than on higher decks".

> "In Fig. 7, we see that the optimal schedule spends more time on lower decks than on higher decks"

## Discussion


## Related Claims
- [Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets.](leitner-learning-rate-shows-increasing-returns-to-review-budget.md) — related
- [Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.](optimal-leitner-deck-allocation-depends-on-item-difficulty.md) — a narrower finding that bears on this claim
- [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](optimal-leitner-schedule-expands-intervals-between-reviews.md) — related
- [Over eight weeks, university learners receiving reinforcement learning-optimized oral practice sequencing attained normalized learning gains approximately 2.2 times higher than learners following fixed curricula](rl-sequencing-beats-fixed-oral-curriculum.md) — related
