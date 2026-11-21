---
type: design
id: instructor-ai-feedback-propagation-framework
title: Triangulated feedback propagation framework combining explainable code analysis, instructor-verified feedback, and constrained LLM support
description: The framework integrates instructor expertise, LLMs, and an explainable AI model (SANN) to deliver reliable, instructor-verified feedback at scale.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: muntasir-hoq-2026
    resource: "https://arxiv.org/abs/2606.12425"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
---

# Triangulated feedback propagation framework combining explainable code analysis, instructor-verified feedback, and constrained LLM support

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The framework integrates instructor expertise, LLMs, and an explainable AI model (SANN) to deliver reliable, instructor-verified feedback at scale. It has three stages: model preparation (SANN pretrained on historical submissions then fine-tuned on synthetic data for a newly authored problem), error localization (the fine-tuned SANN identifies influential AST subtrees via an attention mechanism), and feedback matching (error subtrees matched by cosine similarity against instructor-authored examples, with feedback delivered only above a 50% similarity threshold). LLMs play constrained roles in authoring support, synthetic code generation, and verification of out-of-coverage errors.

## Design Implications

### Context
#### Requirements
- a library of instructor-authored incorrect examples with annotated error regions, misconception labels, and associated feedback for each problem
- a pretrained SANN model that can be fine-tuned on synthetic data for each new problem
#### Constraints
- effectiveness depends strongly on the quality and coverage of instructor-authored incorrect solutions, creating a trade-off between instructor authoring time and comprehensive coverage of logical errors

### Target Learners
- novice students in introductory programming courses

### Learning Goals
- delivering reliable, instructor-aligned feedback on logical errors and misconceptions during active learning sessions

### Claims
- [Fine Tuned Sann Outperforms Baselines Unseen Problem](../claims/fine-tuned-sann-outperforms-baselines-unseen-problem.md) [+M]
- [Feedback Matching Precision Recall Falconcode](../claims/feedback-matching-precision-recall-falconcode.md) [+M]
- [Gpt4O Verification Reduces Incorrect Feedback](../claims/gpt4o-verification-reduces-incorrect-feedback.md) [+M]

## Related Designs
- Insight Classroom Assistant

## Examples
-

## Key Sources
- Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425
