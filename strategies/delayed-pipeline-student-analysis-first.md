---
type: strategy
id: delayed-pipeline-student-analysis-first
title: Delay the automated photometry pipeline so students analyse raw data first, then compare with the reference pipeline
description: "Within MIRA's reduction workflow, teachers can hold back the automatic photometry pipeline as a pedagogical sequencing device."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: pedersen-2026
    resource: "https://arxiv.org/abs/2607.14801"
    title: "Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D. (2026). MIRA: a data management and education platform connecting students to robotic telescopes. https://arxiv.org/abs/2607.14801"
    author: Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D
---

# Delay the automated photometry pipeline so students analyse raw data first, then compare with the reference pipeline

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Within MIRA's reduction workflow, teachers can hold back the automatic photometry pipeline as a pedagogical sequencing device. The article states that "The automatic photometry pipeline can be delayed by the teacher to allow students to analyse first before comparing to the reference pipeline." This lets students attempt calibration and aperture photometry on the archived FITS frames themselves before seeing the platform's automated products, supported by the interactive Python/Jupyter tutorials that walk through the same reduction and analysis steps.

## Design Implications

### Context
#### Requirements
- Access to the archived FITS frames and the Python/Jupyter analysis tutorials
- Teacher control over when the automated reduction products are released
#### Constraints
- 

### Target Learners
- Swiss secondary-school students
- ETH Zurich undergraduates

### Target Learning Goals
- Learning astronomical data reduction and photometric analysis through guided first-hand attempts

## Related Strategies

- Mira Robotic Astronomy Education Platform
- [Human-in-the-loop validation workflow: hold all AI-generated teaching content in unreviewed status until a teacher manually approves it](human-in-the-loop-teacher-validation-workflow.md)
- [Position the instructor as human-in-the-loop reviewer of AI-generated difficulty reports before any feedback reaches students](instructor-in-loop-ai-difficulty-reports.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)
- [Photometry procedure: raw-format capture, aperture photometry with background subtraction, and spreadsheet analysis](dslr-street-light-photometry-procedure.md)

## Examples
-

## Key Sources
- Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D. (2026). MIRA: a data management and education platform connecting students to robotic telescopes. https://arxiv.org/abs/2607.14801
