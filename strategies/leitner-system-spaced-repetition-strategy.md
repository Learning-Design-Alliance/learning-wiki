---
type: strategy
id: leitner-system-spaced-repetition-strategy
title: Implement the Leitner system to skew flashcard exposure toward unknown diagnoses
description: The Leitner system is a spaced repetition algorithm the platform implements to schedule review.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
sources:
  - id: morin-ce-2019
    resource: "https://doi.org/10.1007/s00247-019-04415-3"
    title: "Morin CE, Hostetter JM, Jeudy J, Kim WG, McCabe JA, Merrow AC, Ropp AM, Shet NS, Sidhu AS, Kim JS. (2019). Spaced radiology: encouraging durable memory using spaced testing in pediatric radiology. Pediatric Radiology. https://doi.org/10.1007/s00247-019-04415-3"
    author: Morin CE, Hostetter JM, Jeudy J, Kim WG, McCabe JA, Merrow AC, Ropp AM, Shet NS, Sidhu AS, Kim JS
---

# Implement the Leitner system to skew flashcard exposure toward unknown diagnoses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The Leitner system is a spaced repetition algorithm the platform implements to schedule review. As the article describes it, it "sorts flashcards into five piles according to how well the learner knows each diagnosis": each correct answer advances a card to the next, less frequent pile, while incorrect answers return it to the first pile, forcing review of incorrect material at higher frequencies than known diagnoses.

## Design Implications

### Context
#### Requirements
- Flashcards must be sortable into piles by learner performance
- Repeated testing sessions over time to realize the spacing
#### Constraints
- The authors plan to refine the spacing algorithm using collected outcomes data

### Target Learners
- radiology residents

### Target Learning Goals
- long-term retention of diagnoses through spaced retrieval

## Claims

- [Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.](../claims/leitner-queue-network-phase-transition-in-learning-rate.md) [+M]
- [In a Mechanical Turk flashcard experiment, raising the new-item arrival rate first increases mastered items, but past the optimum fewer items are mastered and more get stuck in deck 1.](../claims/excess-new-item-rate-leaves-items-stuck-in-first-leitner-deck.md) [~M]

## Related Strategies

- [Flashcard Drill](flashcard-drill.md)
- [Flashcards](flashcards.md)
- [Spaced Retrieval Practice](spaced-retrieval-practice.md)
- [Spaced Repetition Scheduling](spaced-repetition-scheduling.md)
- [Spaced Practice Scheduling](spaced-practice-scheduling.md)

## Examples
-

## Key Sources
- Morin CE, Hostetter JM, Jeudy J, Kim WG, McCabe JA, Merrow AC, Ropp AM, Shet NS, Sidhu AS, Kim JS. (2019). Spaced radiology: encouraging durable memory using spaced testing in pediatric radiology. Pediatric Radiology. https://doi.org/10.1007/s00247-019-04415-3
