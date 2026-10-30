---
type: strategy
id: ml-item-selection-strategy
title: Sequence practice items with an ML algorithm that prioritizes questions by predicted recall probability rather than fixing the rate of study
description: "The article's implementable recipe is to let a machine learning algorithm determine which questions to include in a learner's study sessions over time, while leaving review timing to the learner."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
sources:
  - id: utkarsh-upadhyay-2021
    resource: "https://doi.org/10.1038/s41539-021-00105-8"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez
---

# Sequence practice items with an ML algorithm that prioritizes questions by predicted recall probability rather than fixing the rate of study

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article's implementable recipe is to let a machine learning algorithm determine which questions to include in a learner's study sessions over time, while leaving review timing to the learner. In the 'select' group, "as long as there were questions that the learner has not reviewed at least once, these were chosen ﬁrst in order of initial difﬁculty, i.e., easier question ﬁrst", after which the SELECT algorithm's selection probabilities order the questions. This preserved learners' freedom to choose their review times.

## Design Implications

### Context
#### Requirements
- An app or platform in which learners are tested each session and review/recall data can be logged to estimate the memory model
#### Constraints
- The article acknowledges results may not generalize to different populations of learners, different materials, or other tasks without more research

### Target Learners
- Adult self-directed learners using spaced-repetition study apps

### Target Learning Goals
- Improving memorization and retention of large sets of paired-associate items

### Affordances
- [Spaced Selection Framework](../theories/exponential-forgetting-curve-with-item-difficulty.md)

## Claims

- [The selection algorithm affects engagement: select and difficulty groups were more likely to return within 4–7 days than the random group, but select-group learners were more likely to stop using the app in the initial 2 days](../claims/select-algorithm-engagement-effects.md) [~W]
- [ML-based question selection (SELECT) lowers learners' normalized empirical forgetting rate relative to difficulty-ordered and random selection after controlling for review time and number of reviews](../claims/select-algorithm-lower-forgetting-rate-rct.md) [+W]
- [Algorithm-selected learners remember content over ~69% longer, with median half-life increases of ~92% vs random and ~40% vs difficulty groups](../claims/select-group-longer-retention-half-life.md) [+W]
- [Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews](../claims/spacing-effect-and-advantage-grows-with-reviews.md) [+W]

## Related Strategies

- [Spaced Retrieval Practice](spaced-retrieval-practice.md)
- [Item allocation rules: start easy, increase difficulty with grade, and re-select past incorrect and old material with some probability](item-allocation-rules-difficulty-with-grade.md)

## Examples
-

## Key Sources
- Utkarsh Upadhyay, Graham Lancashire, Christoph Moser and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiments reveals that machine learning-based instruction helps people memorize more effectively. npj Science of Learning 6:26. https://doi.org/10.1038/s41539-021-00105-8
