---
type: strategy
id: instructor-verified-llm-feedback-uncovered-errors
title: Extend feedback coverage by having instructors verify LLM-generated feedback for uncovered error patterns ad hoc
description: "The article recommends incorporating LLM-based feedback generation specifically for errors not represented in instructor-authored examples, so that instructors \"spend less time ensuring the most critical misconception..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: muntasir-hoq-2026
    resource: "https://arxiv.org/abs/2606.12425"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
---

# Extend feedback coverage by having instructors verify LLM-generated feedback for uncovered error patterns ad hoc

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends incorporating LLM-based feedback generation specifically for errors not represented in instructor-authored examples, so that instructors "spend less time ensuring the most critical misconceptions are reliably covered" through verified feedback while other errors are covered by an LLM. Instructors verify unseen error patterns and LLM-generated feedback ad hoc and add them to the repository of verified feedback, expanding coverage while preserving instructional control.

## Design Implications

### Context
#### Requirements
- instructors must verify unseen error patterns and LLM-generated feedback before adding them to the repository of verified feedback
#### Constraints
- the current framework delivers feedback only for instructor-identified error patterns, so uncovered errors currently receive no automated feedback

### Target Learners
- novice students in introductory programming courses

### Target Learning Goals
- covering a broader range of student logical errors while keeping instructor-verified reliability for critical misconceptions

### Affordances
- [Instructor Ai Feedback Propagation Framework](../designs/instructor-ai-feedback-propagation-framework.md)

## Claims

- [A GPT-4o verification layer reduced the rate of incorrect feedback from 23% to 1.2% in the feedback-matching pipeline](../claims/gpt4o-verification-reduces-incorrect-feedback.md) [+W]
- [Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness](../claims/insight-feedback-beats-gpt4o-selectivity-suitability.md) [+W]
- [Feedback matching achieved 97.62% precision and recall on the focal problem and remained effective across three additional topic problems](../claims/feedback-matching-precision-recall-falconcode.md) [+W]
- [In a preliminary classroom deployment, students rated Insight's feedback neutral-to-somewhat-agreeable, with 53.6% wanting to continue using it](../claims/insight-classroom-survey-positive-perceptions.md) [+W]

## Related Strategies

- [Instructors should review and edit all AI-generated feedback before sending it to students](human-in-the-loop-review-of-ai-feedback.md)

## Examples
-

## Key Sources
- Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. https://arxiv.org/abs/2606.12425
