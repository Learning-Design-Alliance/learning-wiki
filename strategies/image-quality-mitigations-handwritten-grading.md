---
type: strategy
id: image-quality-mitigations-handwritten-grading
title: "Mitigate transcription failures through image-quality supports: quality review before submission, preview transcriptions, and multiple submission modes"
description: Because most grading errors stem from transcription rather than rubric misapplication, the article recommends mitigations targeting image capture and preprocessing.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: jacob-levine-2026
    resource: "https://arxiv.org/abs/2605.19043"
    title: "Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043"
    author: Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva
---

# Mitigate transcription failures through image-quality supports: quality review before submission, preview transcriptions, and multiple submission modes

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because most grading errors stem from transcription rather than rubric misapplication, the article recommends mitigations targeting image capture and preprocessing. These include "encouraging quality review before submission or providing preview transcriptions," adding direct screenshot uploads alongside webcam and mobile photo capture, and LLM-controllable rotation tools as future work. The article reports the team has already added direct screenshot uploads supporting three submission modes.

## Design Implications

### Context
#### Requirements
- Students must be able to preview their submission to ensure readability and crop the image to relevant work
#### Constraints
- LLM-controllable rotation tools increase token usage and computational cost
- Additional data collection is needed to assess improvements in transcription accuracy

### Target Learners
- university STEM students submitting photographed handwritten solutions

### Target Learning Goals
- reducing transcription errors in automated grading of handwritten mathematics

## Related Strategies

- [Mitigate extraction errors by requiring high-resolution PDFs, equation-editor equations, and legible graph axes, units, and legends](report-submission-practices-to-support-ai-evidence-retrieval.md)

## Examples
-

## Key Sources
- Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043
