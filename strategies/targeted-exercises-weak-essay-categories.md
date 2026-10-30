---
type: strategy
id: targeted-exercises-weak-essay-categories
title: Suggest targeted exercises from weak essay categories based on relative student performance
description: "The system identifies a student's potential weakness in summary writing from relative performance across essay categories (narrative, descriptive, analytical, situational, general)."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-30
sources:
  - id: automatic-summary-assessment-for-intelligent-tutoring-systems-2009
    resource: "https://doi.org/10.1016/j.compedu.2009.05.008"
    title: "Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008"
    author: Automatic Summary Assessment for Intelligent Tutoring Systems
---

# Suggest targeted exercises from weak essay categories based on relative student performance

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (1 review, 1 associational, 1 design), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The system identifies a student's potential weakness in summary writing from relative performance across essay categories (narrative, descriptive, analytical, situational, general). When a student's performance measure in a category falls below a pre-defined threshold, "the system will then suggest more essays from that category to the student in upcoming exercises". This implements adaptive sequencing within a scaffolding model.

## Design Implications

### Context
#### Requirements
- A student model recording per-category and overall performance measures and the number of exercises taken
#### Constraints
- Rests on the stated assumption that summary writing performance can be measured by assessment results

### Target Learners
- secondary school students

### Target Learning Goals
- summary writing skills across essay categories

## Claims

- [In a self-referential framework, LLMs, particularly GPT-4.1, tend to outperform a single operational human rater at identifying relative weaknesses (negative feedback) across several Language and Content aspects](../claims/llms-outperform-single-rater-negative-feedback.md) [+W]
- [Learning analytics tools can provide personalized feedback on students' academic writing by identifying mistakes and offering constructive suggestions (e.g., AcaWriter)](../claims/acawriter-personalized-writing-feedback.md) [+W]
- [ChatGPT-3.5 feedback on EAP argumentative essays aligns closely with human instructor scoring and identifies surface-level issues, but is less effective on rhetorical structure and contextual nuance](../claims/chatgpt-feedback-aligns-with-human-scoring-but-weak-on-rhetorical-structure.md) [~W]

## Related Strategies

- [Adaptive scenario generation: introduce training scenarios targeting weaknesses identified from real-time performance metrics](astra-adaptive-scenario-generation.md)
- [Combine inter-learner rankings with intra-learner diagnostics in assessment and feedback](combine-inter-learner-and-intra-learner-diagnostics.md)
- [Use automatic reflection classification for preliminary feedback and workload support, with final assessment retained by educators](automated-reflection-preliminary-feedback-educator-final.md)

## Examples
-

## Key Sources
- Automatic Summary Assessment for Intelligent Tutoring Systems. (2009). Preprint submitted to Elsevier February 26, 2009. https://doi.org/10.1016/j.compedu.2009.05.008
