---
type: element
id: duolingo-review-exercises
title: "Review Exercises: injected review items sampled from earlier skills for scalable, fine-grained assessment"
description: Review Exercises are assessment items inserted into randomly selected Level 0 lessons of skills beyond the first five in a course, sampled from the exercise pools of skills three or five skills earlier.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: lucy-portnoff-2021
    resource: "https://educationaldatamining.org/edm2021/"
    title: "Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson. (2021). Methods for Language Learning Assessment at Scale: Duolingo Case Study. Proceedings of The 14th International Conference on Educational Data Mining (EDM21). https://educationaldatamining.org/edm2021/"
    author: Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson
---

# Review Exercises: injected review items sampled from earlier skills for scalable, fine-grained assessment

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study, `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Review Exercises are assessment items inserted into randomly selected Level 0 lessons of skills beyond the first five in a course, sampled from the exercise pools of skills three or five skills earlier. They come in two forms: assisted recall and translation between L1 and L2. The article lists their advantages: they are "available in all courses", allow measurement "at every skill in a course, rather than just at unit-terminal Checkpoints", and "provide an order of magnitude more data than Checkpoint Quizzes". Their disadvantages are overlapping items with lessons (reduced test validity), unassessed item quality, and no tagging for grammatical concepts or communicative components.

## Design Implications

### Context
#### Requirements
- Skills beyond the first five in the course, so source material exists to sample from
- Insertion in a random lesson position not among the first two or last two exercises
#### Constraints
- Items overlap with lesson items, sacrificing some test validity
- Sentences used have not been assessed for quality as measures of learning
- Data is not tagged for grammatical concepts or communicative components, limiting curriculum-design insights

### Target Learners
- Duolingo language learners in all courses

### Target Learning Goals
- Retention and recall of vocabulary and grammar from previously studied skills

## Claims

- [Leveling up lessons preceding the source lesson improves Review Exercise accuracy, indicating transfer of learning benefits across lessons within a skill](../claims/leveling-up-benefit-transfers-across-lessons.md) [+W]
- [A regression discontinuity design on Review Exercise data supports a causal link between leveling up and higher assessment accuracy, at least for the first level-up](../claims/rdd-review-exercises-causal-leveling-up.md) [+W]

## Related Elements

- [Checkpoint Quiz: a unit-terminal achievement test with embedded pre-test/post-test design](duolingo-checkpoint-quiz.md)

## Examples

- [Cumulative Quizzing](../strategies/cumulative-quizzing.md)
- [Cumulative Review](../strategies/cumulative-review.md)

## Key Sources
- Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson. (2021). Methods for Language Learning Assessment at Scale: Duolingo Case Study. Proceedings of The 14th International Conference on Educational Data Mining (EDM21). https://educationaldatamining.org/edm2021/
