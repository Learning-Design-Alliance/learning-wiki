---
type: strategy
id: hybrid-grading-workflow-teacher-control
title: "Automated Grading Workflow: teachers evaluate the model on their own data, set a disagreement threshold, and choose which predictions to review"
description: "The proposed trust-building process lets teachers \"gauge the performance of a grading pipeline on their students' data, apply their own quality requirements and choose which automated grades to keep and which to review\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: ulrike-padó-2024
    resource: "https://doi.org/10.1007/s40593-023-00383-w"
    title: "Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w"
    author: Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner
---

# Automated Grading Workflow: teachers evaluate the model on their own data, set a disagreement threshold, and choose which predictions to review

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The proposed trust-building process lets teachers "gauge the performance of a grading pipeline on their students' data, apply their own quality requirements and choose which automated grades to keep and which to review". Steps are: define the maximum affordable disagreement between machine and human grader; collect a manually annotated data set; optionally fine-tune or use a public model; analyze performance per grade label; and decide which predictions to accept and which to revise. Automated grades are treated as suggestions subject to human review, keeping teachers in control while saving effort.

## Design Implications

### Context
#### Requirements
- Teachers define a maximum acceptable disagreement threshold adapted to their use case (formative or summative)
- A data set of manually annotated student answers comparable to the intended use case
#### Constraints
- The workflow acknowledges the imperfection of current SAG models; performance on new data sets cannot be reliably predicted from benchmarks

### Target Learners
- teachers grading constructed short answers

### Target Learning Goals
- saving grading effort while keeping grade disagreement below the teacher's threshold

### Affordances
- Three Challenges Sag Adoption Framework

## Claims

- [Six expert teachers completed grading tasks in ASYST with 100% effectiveness, median 2:15 minutes, and an average SUS score of 88.8](../claims/asyst-usability-study-high-sus.md) [+W]
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](../claims/sag-performance-varies-across-corpora.md) [+W]

## Related Strategies

- [Set difficulty-specific intervention times based on when prediction quality exceeds a fixed threshold](difficulty-specific-intervention-times.md)
- [Human-in-the-loop generative pipeline for synthetic classroom training data with domain-expert validation](generative-synthetic-classroom-data-pipeline-strategy.md)

## Examples
-

## Key Sources
- Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w
