---
type: claim
title: Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.
description: Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.
id: optimal-leitner-deck-allocation-depends-on-item-difficulty
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

# Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` Comparing optimal schedules for different item difficulties at the same budget (Fig. 12) suggests uniform deck time for easy items and more lower-deck time for harder items. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q1 · i?`

Optimization result from the item-difficulty extension of the model (Fig. 12). It "suggests that when items are generally easy, the user should spend a roughly uniform amount of time on each deck", and more on lower decks for harder items.

> "Fig. 12 suggests that when items are generally easy, the user should spend a roughly uniform amount of time on each deck; however, when items are of higher general diﬃculty, the user should spend more time on lower decks than higher decks."

## Discussion


## Related Claims
- [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](optimal-leitner-schedule-expands-intervals-between-reviews.md) — related
- [Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.](optimal-leitner-schedule-reviews-lower-decks-more-often.md) — a broader claim this one bears on
- [Under the mean-recall approximation, the maximum achievable learning rate is convex in the learner's review frequency budget, suggesting increasing returns at lower budgets.](leitner-learning-rate-shows-increasing-returns-to-review-budget.md) — related
