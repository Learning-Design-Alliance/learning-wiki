---
type: strategy
id: spaced-review-day2-day5-strategy
title: Re-test unmastered skills at spaced intervals (day 2 and day 5) after a block is passed
description: "When a learner passes a block with performance below 100%, the system logs the specific unmastered skills and vocabulary and instantiates a per-block review lesson group."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: nicy-scaria-2026
    resource: "https://arxiv.org/abs/2604.22770"
    title: "Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani. (2026). Learning in Blocks: A Multi Agent Debate Assisted Personalized Adaptive Learning Framework for Language Learning. Preprint, to appear in International Conference on Artificial Intelligence in Education (LNAI). https://arxiv.org/abs/2604.22770"
    author: Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani
---

# Re-test unmastered skills at spaced intervals (day 2 and day 5) after a block is passed

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
When a learner passes a block with performance below 100%, the system logs the specific unmastered skills and vocabulary and instantiates a per-block review lesson group. These carried-forward review groups are appended to subsequent blocks and re-tested at spaced intervals to counter the forgetting curve: "the carried-forward review groups are re-tested at spaced intervals, specifically on day 2 and day 5 after a block is passed." Review scores contribute to the current block's mastery percentage and update the review set, so earlier weaknesses are continuously revisited until full mastery is demonstrated.

## Design Implications

### Context
#### Requirements
- Conversation-derived scoring must identify the specific unmastered skills and vocabulary responsible for missed percentage
- Review groups must be appended to subsequent blocks and assessed at block start
#### Constraints
- Re-test intervals are fixed at day 2 and day 5 in this implementation; the article names optimal individualized review scheduling as future work

### Target Learners
- English learners working toward CEFR A2 proficiency

### Target Learning Goals
- Retention and maintenance of grammar skills and vocabulary over time

### Affordances
- [Learning In Blocks Framework](../designs/learning-in-blocks-framework.md)

## Claims

- [In an 8-week study, the Learning in Blocks cohort showed significant pre-post gains across all dimensions and significantly outperformed both feedback-only cohorts](../claims/learning-in-blocks-cohort-largest-gains.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani. (2026). Learning in Blocks: A Multi Agent Debate Assisted Personalized Adaptive Learning Framework for Language Learning. Preprint, to appear in International Conference on Artificial Intelligence in Education (LNAI). https://arxiv.org/abs/2604.22770
