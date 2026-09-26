---
type: claim
title: Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.
description: Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.
id: optimal-leitner-schedule-expands-intervals-between-reviews
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

# Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` Under the optimal schedule, expected delay between subsequent reviews increases as an item moves to higher decks (Fig. 8). [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q1 · i?`

Optimization result under the mean-recall approximation (Fig. 8, n = 20, U = 1, θ = 0.01). The network "increases the ex- pected delay between subsequent reviews as an item moves up through the system".

> "However, in Fig. 8 we ob- serve that the Leitner Queue Network also increases the ex- pected delay between subsequent reviews as an item moves up through the system."

## Discussion


## Related Claims
- [Spaced Practice Improves Long Term Retention](spaced-practice-improves-retention.md)
- [Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets.](leitner-learning-rate-shows-increasing-returns-to-review-budget.md) — related
- [Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.](optimal-leitner-deck-allocation-depends-on-item-difficulty.md) — related
- [Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.](optimal-leitner-schedule-reviews-lower-decks-more-often.md) — related
- [Over eight weeks, university learners receiving reinforcement learning-optimized oral practice sequencing attained normalized learning gains approximately 2.2 times higher than learners following fixed curricula](rl-sequencing-beats-fixed-oral-curriculum.md) — related
