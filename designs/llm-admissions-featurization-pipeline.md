---
type: design
id: llm-admissions-featurization-pipeline
title: LLM-based pipeline converting unstructured application materials into structured measures, including a seven-dimension essay quality score validated against expert ratings
description: The authors built an LLM-based pipeline that converts unstructured application materials (transcripts, recommendation letters, resumes, essays) into structured measures, extracting 216 measures designed with admission...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: calvin-isley-2026
    resource: "https://arxiv.org/abs/2609.22549"
    title: "Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549"
    author: Calvin Isley, Johann D. Gaebler, and Sharad Goel
---

# LLM-based pipeline converting unstructured application materials into structured measures, including a seven-dimension essay quality score validated against expert ratings

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The authors built an LLM-based pipeline that converts unstructured application materials (transcripts, recommendation letters, resumes, essays) into structured measures, extracting 216 measures designed with admissions officers. Essay quality is scored along seven dimensions—"grammar, style, clarity, prompt responsiveness, voice, commitment to public service, and demonstrated leadership"—each graded on a five-point scale, then combined into a composite score fitted to predict expert ratings from five admissions officers. The automated and expert ratings correlate at 70%. The pipeline also produced 427 covariates used in the causal models.

## Design Implications

### Context
#### Requirements
- Requires LLM scoring prompts with concrete rubric criteria per dimension and expert calibration ratings from admissions officers to fit dimension weights
#### Constraints
- The authors state the automated quality measure is an imperfect proxy for expert judgment and may systematically miss dimensions of quality that matter in admissions

### Target Learners
- graduate program applicants

### Learning Goals
- accurate structured assessment of applicant writing quality and application materials

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549
