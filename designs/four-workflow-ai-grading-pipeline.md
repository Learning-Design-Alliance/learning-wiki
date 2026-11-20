---
type: design
id: four-workflow-ai-grading-pipeline
title: Four-workflow AI-assisted grading pipeline for handwritten exams
description: A pipeline for AI-assisted grading of handwritten exam solutions, starting with scanning exam sheets, making them machine-readable with MathPix and GPT-4V, and grading them using GPT-4-32k.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: gerd-kortemeyer-2024
    resource: "https://arxiv.org/abs/2406.17859"
    title: "Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. https://arxiv.org/abs/2406.17859"
    author: Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk
---

# Four-workflow AI-assisted grading pipeline for handwritten exams

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A pipeline for AI-assisted grading of handwritten exam solutions, starting with scanning exam sheets, making them machine-readable with MathPix and GPT-4V, and grading them using GPT-4-32k. Four workflows (WF1–WF4) vary the OCR method (MathPix+GPT-4V versus GPT-4V only) and grading granularity (rubric items, problem parts, or whole problems). Multiple grading cycles compute mean scores with standard deviations as confidence measures, per the article's assumption that "grading by LLMs should be viewed probabilistically."

## Design Implications

### Context
#### Requirements
- Handwritten solutions must be converted to machine-readable LaTeX format before grading
- The LLM must return point values within the available range for each grading item, with failed attempts regraded
#### Constraints
- Students received no instructions on preparing work for OCR, so manual fixes (redaction, page rotation, problem-separation markers) were needed
- Graph transcription proved unreliable, and the workflow was studied on a single high-stakes thermodynamics exam at one institution

### Target Learners
- undergraduate engineering students

### Learning Goals
- summative assessment of thermodynamics problem-solving

### Claims
- [Mathpix Gpt4V Ocr More Reliable Than Gpt4V Alone](../claims/mathpix-gpt4v-ocr-more-reliable-than-gpt4v-alone.md) [+M]
- [Rubric Granularity Affects Ai Grading Reliability](../claims/rubric-granularity-affects-ai-grading-reliability.md) [+M]
- [Wf1 Wf2 Outperform Wf3 Grading](../claims/wf1-wf2-outperform-wf3-grading.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. https://arxiv.org/abs/2406.17859
