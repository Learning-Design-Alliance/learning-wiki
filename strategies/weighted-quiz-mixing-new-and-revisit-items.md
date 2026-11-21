---
type: strategy
id: weighted-quiz-mixing-new-and-revisit-items
title: Mix new and previously solved questions in short mobile quizzes using weighted selection favoring less-recent, previously incorrect, and marked items
description: Each LingoQuiz session delivers a 10-question quiz that balances new material with targeted review.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: yeonsun-yang-2026
    resource: "https://doi.org/10.1145/3772318.3791342"
    title: "Yeonsun Yang, Sang Won Lee, Jean Y. Song, Sangdoo Yun, and Young-Ho Kim. 2026. LingoQ: Bridging the Gap between EFL Learning and Work through AI-Generated Work-Related Quizzes. In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3791342"
    author: Yeonsun Yang, Sang Won Lee, Jean Y. Song, Sangdoo Yun, and Young-Ho Kim
---

# Mix new and previously solved questions in short mobile quizzes using weighted selection favoring less-recent, previously incorrect, and marked items

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Each LingoQuiz session delivers a 10-question quiz that balances new material with targeted review. The article states: "Each quiz contains 10 questions: 7 are selected from newly generated questions, and the remaining 3 are randomly drawn from the pool of questions that a user has solved previously using weighted probability." Weights are higher for questions repeated less frequently, answered incorrectly in the past, marked with the star icon, or not practiced recently, so each quiz revisits items the worker needs to practice while keeping most content new.

## Design Implications

### Context
#### Requirements
- A question pool of validated generated questions per user
- Log data on prior answers, repetition counts, star marks, and recency of practice
#### Constraints
- Implemented within LingoQ's 10-question multiple-choice quiz format on a smartphone app

### Target Learners
- EFL information workers practicing work-related English on mobile devices

### Target Learning Goals
- retention of work-related vocabulary and grammar through retrieval practice

## Claims

- [Beginner-level EFL workers showed notable learning gains on a TOEIC-based proficiency test after using LingoQ](../claims/lingoq-beginner-toeic-learning-gains.md) [+M]
- [Using LingoQ for three weeks significantly increased EFL workers' self-efficacy in English skills (9.5% average gain, p < 0.001)](../claims/lingoq-self-efficacy-gain-deployment.md) [+M]
- [EFL workers consistently engaged with LingoQ over three weeks and perceived its review practice as more sustainable than prior study methods](../claims/lingoq-sustained-engagement-deployment.md) [+M]

## Related Strategies

- [Cumulative Quizzing](cumulative-quizzing.md)
- [Cumulative Review Quizzes](cumulative-review-quizzes.md)
- [Cumulative Review](cumulative-review.md)
- [Grade-dependent item allocation that shifts quiz question difficulty upward as student grades rise](grade-dependent-item-allocation-scheme.md)

## Examples
-

## Key Sources
- Yeonsun Yang, Sang Won Lee, Jean Y. Song, Sangdoo Yun, and Young-Ho Kim. 2026. LingoQ: Bridging the Gap between EFL Learning and Work through AI-Generated Work-Related Quizzes. In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3791342
