---
type: strategy
id: sst-question-design-six-answers-negative-points
title: Design multiple-choice self-training questions with at least six answers, distractor groups based on common mistakes, and negative points for wrong answers
description: To make guessing unprofitable and reinforce confidence in personal work, each SST question proposes a minimum of at least 6 answers, with one group containing the correct answer(s) plus small variations and at least a...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: gl-lippi-2018
    resource: "https://arxiv.org/abs/1809.04968"
    title: "G.L. Lippi. (2018). Multiple choice homework as a cost-effective and efficient tool for student self-training. arXiv. https://arxiv.org/abs/1809.04968"
    author: G.L. Lippi
---

# Design multiple-choice self-training questions with at least six answers, distractor groups based on common mistakes, and negative points for wrong answers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (6 for, 1 mixed, 1 against) · 7 studies (2 causal, 2 associational, 2 design, 1 review), `q2`–`q3` · 0 of 7 report an effect size · 8 claims rest on one study

## Description
To make guessing unprofitable and reinforce confidence in personal work, each SST question proposes a minimum of at least 6 answers, with one group containing the correct answer(s) plus small variations and at least a second group based on common mistakes. Occasionally a question has no correct answer at all, so students do not bend calculations to find one. Negative points are assigned to incorrect answers, sanctioning entirely wrong answers more strongly than slight variations of the correct one.

## Design Implications

### Context
#### Requirements
- Instructor time to prepare sufficiently large numbers of incorrect answers for each question
- Per-answer point values set by the instructor when generating the code
#### Constraints
- This design was implemented with the AMC multiple-correct-answers option; answer scrambling and randomization were not used

### Target Learners
- undergraduate Physics students doing unsupervised homework

### Target Learning Goals
- accurate execution of full calculations down to the final detail; resistance to guessing

### Affordances
- [Sst Sigmoid Bonus Self Training Scheme](../designs/sst-sigmoid-bonus-self-training-scheme.md)

## Claims

- [LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them](../claims/llm-distractor-likelihood-moderately-tracks-student-choices.md) [+W]
- [LLM-generated distractors for math multiple-choice questions are judged mathematically valid more often than plausible to students, and rarely reproduce the full set of human-written distractors](../claims/llm-math-distractors-more-valid-than-plausible.md) [+W]
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](../claims/llm-distractor-prediction-asymmetry.md) [+W]
- [Fear that reducing MCQ options increases correct answers by guessing is unfounded, because examinees engage in educated rather than blind guessing](../claims/mcq-option-reduction-guessing-concern-unfounded.md) [+W]
- [Multiple-choice testing increases the later production of multiple-choice lures as answers on cued recall tests, even under warning against guessing](../claims/mc-testing-increases-lure-production.md) [-W]
- [Students who returned the optional multiple-choice homework gained 0.13 points between level test and final grade, while non-participants lost 0.02](../claims/sst-homework-participants-gain-013-nonparticipants-002.md) [+W]
- [Homework participants scored sensibly higher on the initial level test (0.39 vs 0.31), suggesting self-selection into the scheme](../claims/sst-level-test-self-selection-039-vs-031.md) [~W]
- [A majority of answer options chosen in long-menu questions were not offered as distractors in the corresponding Type A questions](../claims/long-menu-chosen-options-outside-type-a-distractors.md) [+M]

## Related Strategies

- [Build multiple-choice distractors from coded free-response student answers, with partial credit for partially correct reasoning](cmr-design-from-fr-response-data.md)

## Examples
-

## Key Sources
- G.L. Lippi. (2018). Multiple choice homework as a cost-effective and efficient tool for student self-training. arXiv. https://arxiv.org/abs/1809.04968
