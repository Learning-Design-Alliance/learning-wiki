---
type: design
id: gpt-batch-grading-pipeline-pymupdf-tesseract
title: Rubric-driven batch AI grading pipeline combining PyMuPDF text extraction and Tesseract OCR
description: "An automated batch-grading pipeline implemented via the API using the GPT-5.4 model, configured with the course's own 10-point rubric, a structured checklist, and instructions requiring per-item scores, justifications..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: marcos-abreu-2026
    resource: "https://arxiv.org/abs/2603.20412v2"
    title: "Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2603.20412v2"
    author: Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti
---

# Rubric-driven batch AI grading pipeline combining PyMuPDF text extraction and Tesseract OCR

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An automated batch-grading pipeline implemented via the API using the GPT-5.4 model, configured with the course's own 10-point rubric, a structured checklist, and instructions requiring per-item scores, justifications, strengths and weaknesses, and an overall summary. Reports in uncompressed PDF format were processed with "the PyMuPDF Python library" for embedded digital text and "TesseractOCR" for characters in graphical elements, chosen over direct multimodal PDF submission for greater methodological stability and traceability.

## Design Implications

### Context
#### Requirements
- Reports submitted as PDFs with a standardized rubric; combined text-extraction and OCR processing; anonymized documents
#### Constraints
- Reliance on automatically extracted text and OCR limits access to equations, figures, and graphical representations, producing invalid evaluations when key evidence is not recovered

### Target Learners
- second-year engineering students in large-enrollment physics laboratory courses

### Learning Goals
- consistent rubric-based assessment and feedback on laboratory reports

### Claims
- [Invalid Ai Evaluations Evidence Accessibility](../claims/invalid-ai-evaluations-evidence-accessibility.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2603.20412v2
