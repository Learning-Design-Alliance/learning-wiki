---
type: theory
title: Exponential Forgetting Curve with Item Difficulty
description: The article adopts a variant of the exponential forgetting curve, in which recall is binary and recall probability decays exponentially with time since last review at a rate reduced by memory strength.
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

# Exponential Forgetting Curve with Item Difficulty

> **Theory** · [All theories](index.md)

## Description
The article adopts a variant of the exponential forgetting curve, in which recall is binary and recall probability decays exponentially with time since last review at a rate reduced by memory strength. It adds that "there is a constant, item-speciﬁc component of the memory decay rate" through a difficulty parameter, and its final form uses Leitner deck position as strength with a global difficulty.

## Design Implications

### Context
#### Requirements
- Log data giving the delay since last review and the item's Leitner deck position (or review count) for each interaction.
- Recall outcomes discretized to binary; in the Mnemosyne data, self-reported grades of 2 or higher count as recall.
#### Constraints
- The authors say the choice between item-specific and global difficulty is less clear from the data; the global form is chosen for practicality and tractability.
- The authors call for more sophisticated memory models that more accurately predict the effect of a review schedule on retention.

### Target Learners
- Users of flashcard software such as Mnemosyne

### Target Learning Objectives
- Predicting recall of flashcard items
- Retention of reviewed items over time

### Claims
- [Delay Term Improves Exponential Forgetting Curve Recall Prediction](../claims/delay-term-improves-exponential-forgetting-curve-recall-prediction.md) [+M]
- [Leitner Deck Position Predicts Recall Better Than Review Count](../claims/leitner-deck-position-predicts-recall-better-than-review-count.md) [+M]
- [Exponential Forgetting Models With Delay Perform Comparably To 1Pl Irt](../claims/exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) [+M]
- [Item Specific Difficulty Helps Only At Low And High Leitner Decks](../claims/item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) [~M]

## Related Theories
- [Spaced Repetition](../elements/spaced-repetition.md)

## Examples
-

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
