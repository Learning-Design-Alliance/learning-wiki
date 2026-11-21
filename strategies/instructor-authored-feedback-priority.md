---
type: strategy
id: instructor-authored-feedback-priority
title: Structure AI-assisted feedback to prioritize instructor-authored content, then instructor-edited AI suggestions, with pure AI comments only filling gaps
description: "When generating student feedback in a human-AI grading system, compile metric grades, comments, and instructor annotations so that the instructor's own content leads the feedback."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zixin-chen-2025
    resource: "https://doi.org/10.1145/3746059.3747670"
    title: "Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu. (2025). CoGrader: Transforming Instructors' Assessment of Project Reports through Collaborative LLM Integration. UIST '25. https://doi.org/10.1145/3746059.3747670"
    author: Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu
---

# Structure AI-assisted feedback to prioritize instructor-authored content, then instructor-edited AI suggestions, with pure AI comments only filling gaps

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
When generating student feedback in a human-AI grading system, compile metric grades, comments, and instructor annotations so that the instructor's own content leads the feedback. The article states "The feedback is structured to prioritize instructor-authored content, followed by instructor-edited AI suggestions, with pure AI-generated comments used only to fill remaining gaps (R5)". Instructors remain free to review and revise the output before exporting it to students.

## Design Implications

### Context
#### Requirements
- The system must capture instructor highlights, annotations, and edited comments during grading so they can lead the generated feedback
#### Constraints
- Applied to personalized per-report feedback in project report grading, not to other feedback formats

### Target Learners
- university students receiving project report feedback

### Target Learning Goals
- receiving clear, personalized, pedagogically grounded feedback on project work

## Claims

- [Instructors engage LLM-generated suggestions as a controllable refinement process](../claims/instructors-use-llm-suggestions-as-controllable-refinement.md) [+W]
- [All AI-generated outputs in the project underwent mandatory human-in-the-loop review, positioning AI as augmentative rather than substitutive](../claims/mandatory-human-in-the-loop-review-ai-outputs.md) [+W]

## Related Strategies

- [Instructors should review and edit all AI-generated feedback before sending it to students](human-in-the-loop-review-of-ai-feedback.md)
- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Add human-in-the-loop capabilities so practitioners can edit or choose among LLM-generated tutoring script components](human-in-the-loop-cts-authoring-strategy.md)

## Examples
-

## Key Sources
- Zixin Chen, Jiachen Wang, Yumeng Li, Haobo Li, Chuhan Shi, Rong Zhang, and Huamin Qu. (2025). CoGrader: Transforming Instructors' Assessment of Project Reports through Collaborative LLM Integration. UIST '25. https://doi.org/10.1145/3746059.3747670
