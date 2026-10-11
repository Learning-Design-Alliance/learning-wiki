---
type: design
id: prairielearn-vision-llm-handwritten-math-grader
title: PrairieLearn-integrated AI grading tool for handwritten mathematics with single-call transcription and rubric evaluation
description: The article presents a prototype AI-assisted grading tool integrated into PrairieLearn, an open-source online assessment platform, that evaluates open-ended mathematical responses submitted as handwritten photographs.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: jacob-levine-2026
    resource: "https://arxiv.org/abs/2605.19043"
    title: "Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043"
    author: Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva
---

# PrairieLearn-integrated AI grading tool for handwritten mathematics with single-call transcription and rubric evaluation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article presents a prototype AI-assisted grading tool integrated into PrairieLearn, an open-source online assessment platform, that evaluates open-ended mathematical responses submitted as handwritten photographs. It extends a prior typed-response pipeline by introducing an image-based grading pipeline and prompt structure that jointly perform transcription and rubric-based evaluation. The prompt includes the problem statement, rubric, optional reference solutions, and explicit directives for both transcription and assessment. Human graders may review and override AI evaluations, and human-assigned grades always take precedence.

## Design Implications

### Context
#### Requirements
- The LLM prompt includes the problem statement, rubric, optional reference solutions and instructions, and explicit directives for both transcription and assessment
- The grader operates asynchronously, executing only after submissions close and the grading configuration is finalized
#### Constraints
- Only the final uploaded image is graded
- Randomized problem instances preclude retrieval-augmented grading, as the variability across problem instances prevents reliable reuse of previously graded examples

### Target Learners
- university STEM students in numerical methods and introductory dynamics courses

### Learning Goals
- grading of multi-step handwritten mathematical derivations against instructor-defined rubrics

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043
