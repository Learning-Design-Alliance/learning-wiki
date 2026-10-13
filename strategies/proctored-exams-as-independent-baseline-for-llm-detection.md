---
type: strategy
id: proctored-exams-as-independent-baseline-for-llm-detection
title: Use proctored, closed-note in-person examinations as an independent baseline for validating LLM-use detections
description: "The article validates its detection scores against exams where \"the use of any external assistance is prohibited by course policy\", treating closed-note, written, proctored exams as \"an independent baseline of student..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: david-racovan-2026
    resource: "https://arxiv.org/abs/2609.36073"
    title: "David Racovan, Ajay Rawat, Christopher K. May, Jeffrey A. Turkstra. (2026). Argus: Academic Integrity in the Era of Generative AI. https://arxiv.org/abs/2609.36073"
    author: David Racovan, Ajay Rawat, Christopher K. May, Jeffrey A. Turkstra
---

# Use proctored, closed-note in-person examinations as an independent baseline for validating LLM-use detections

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article validates its detection scores against exams where "the use of any external assistance is prohibited by course policy", treating closed-note, written, proctored exams as "an independent baseline of student performance". Correlating flagged LLM-use indicators with these independent measures lets practitioners check whether detections have pedagogical significance rather than merely flagging stylistic differences. This is the validation design the authors recommend by example for other practitioners adopting such tools.

## Design Implications

### Context
#### Requirements
- Access to exam scores from assessments completed without external assistance, administered under the same course across offerings.
#### Constraints
- Spring 2020 analysis was limited because a project replaced exams beyond Midterm 1; final exams with less coding showed weaker correlations.

### Target Learners
- undergraduate students in programming courses

### Target Learning Goals
- validating academic-integrity detections against independent measures of learning

## Claims

- [Flagged Spring 2026 students scored lower on all three exams than non-flagged peers, with performance declining as flagged assignments increased](../claims/flagged-students-lower-exam-scores-dose-response.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- David Racovan, Ajay Rawat, Christopher K. May, Jeffrey A. Turkstra. (2026). Argus: Academic Integrity in the Era of Generative AI. https://arxiv.org/abs/2609.36073
