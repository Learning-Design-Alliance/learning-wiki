---
type: design
id: ai-assisted-grading-workflow-kortemeyer
title: "AI-assisted grading workflow: scan, OCR-transcribe, and AI-grade handwritten physics solutions in multiple rounds"
description: "The article proposes a multi-step workflow for AI-assisted grading of handwritten physics-problem solutions: papers are scanned into PDF, processed by AI-based optical character recognition into a machine-readable for..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: gerd-kortemeyer-2023
    resource: "https://arxiv.org/abs/2304.11221"
    title: "Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course? https://arxiv.org/abs/2304.11221"
    author: Gerd Kortemeyer
---

# AI-assisted grading workflow: scan, OCR-transcribe, and AI-grade handwritten physics solutions in multiple rounds

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes a multi-step workflow for AI-assisted grading of handwritten physics-problem solutions: papers are scanned into PDF, processed by AI-based optical character recognition into a machine-readable format such as LaTeX, then graded by an AI-tool (GPT-4) in several independent rounds that are subsequently summarized. Variations include "flagging solutions where grading results diverge for subsequent human arbitration, or categorizing the solutions into similarity classes as a preliminary step to more rapid human grading."

## Design Implications

### Context
#### Requirements
- Access to the GPT-4 API for image input (unavailable at study time, so OCR steps were simulated)
- Cloud-based AI service, raising privacy and data-security concerns for mandatory assignments
#### Constraints
- Due to the token limit, not all 25 solutions could be graded at once; they were processed in batches of five
- ChatGPT often did not provide tables in the requested CSV-format, requiring manual reformatting

### Target Learners
- introductory physics students submitting handwritten solutions

### Learning Goals
- assessment of solution paths and derivations in physics problem solving

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course? https://arxiv.org/abs/2304.11221
