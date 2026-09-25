---
type: element
id: mnemosyne-flashcard-review-logs
title: Mnemosyne Flashcard Review Log Data
description: Large-scale log data from the Mnemosyne flashcard software, used by the article to compare memory models.
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

# Mnemosyne Flashcard Review Log Data

> **Element** · [All elements](index.md)

## Description
Large-scale log data from the Mnemosyne flashcard software, used by the article to compare memory models. After filtering, the authors select a random subset that "contains 859 , 591 interactions, 2, 742 users, and 88 , 892 items". Each interaction carries a self-reported 0-5 grade, which the authors discretize into binary recall, and models are compared by ten-fold cross-validated AUC and a held-out test set.

## Design Implications

### Context
#### Requirements
- Filtering out users and items with fewer than five interactions.
- Discretizing self-reported grades into binary recall outcomes and scaling review intervals to days.
#### Constraints
- 

### Target Learners
- Users of the Mnemosyne flashcard software

### Target Learning Goals
- Validating memory models of recall as a function of reinforcement and delay

## Related Elements
- [Spaced Repetition](spaced-repetition.md)

## Examples
-

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
