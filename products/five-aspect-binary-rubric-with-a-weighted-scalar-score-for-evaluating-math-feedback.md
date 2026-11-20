---
type: product
id: five-aspect-binary-rubric-with-a-weighted-scalar-score-for-evaluating-math-feedback
title: Five-aspect binary rubric with a weighted scalar score for evaluating math feedback
description: A rubric introduced by Scarlatos et al.
product_kind: assessment
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Five-aspect binary rubric with a weighted scalar score for evaluating math feedback

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A rubric introduced by Scarlatos et al. for rating middle-school mathematics feedback on correctness, revealingness, suggestions, diagnosis, and positivity relative to a specific student error.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **A five-aspect binary rubric with a weighted scalar score for evaluating math feedback on correctness and pedagogical alignment**: The article defines a rubric function that labels any feedback given a question, correct answer, solution explanation, and incorrect student answer on "ﬁve diﬀerent aspects, each of them resulting in a bina ry-valued label": Correct, Revealing, Suggestion, Diagnostic, and Positive. Correctness gates the score: the final rubric score is 0 if the feedback is incorrect, and otherwise "increases by increments of 0.2 for every rubric aspect the feedback satisﬁes", with correctness double-weighted. GPT-4 with zero-shot chain-of-thought prompting defines an estimated version of the rubric function used both for evaluation and for constructing training preferences. (Alexander Scarlatos et al. (2024))

### Claims
- [GPT-4 achieves moderate-to-high agreement with human annotations when applying the five-aspect math feedback rubric, with 76% average label accuracy and a 0.56 average correlation of rubric scores.](../claims/gpt4-rubric-agreement-math-feedback.md) [+M]
- [GPT-4 tends to assume feedback is correct when it sounds convincing but incorrectly identifies the student error or provides an invalid suggestion, and has a high false positive rate on the diagnostic label.](../claims/gpt4-feedback-evaluation-shortcomings.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. https://arxiv.org/abs/2403.01304
