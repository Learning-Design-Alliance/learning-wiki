---
type: strategy
id: identifier-in-file-path-submission-storage
title: Store submissions with student identifiers embedded in regular file paths to enable automated retrieval and iteration
description: "To automate retrieving, opening and closing submissions, gradetools assumes each student has a unique identifier, specified in the roster, that appears in the student's assignment file path and is the only part unique..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: federica-zoe-ricci-2024
    resource: "https://arxiv.org/abs/2309.12924"
    title: "Federica Zoe Ricci, Catalina Mari Medina, Mine Dogucu. (2024). Automated grading workflows for providing personalized feedback to open-ended data science assignments. arXiv preprint. https://arxiv.org/abs/2309.12924"
    author: Federica Zoe Ricci, Catalina Mari Medina, Mine Dogucu
---

# Store submissions with student identifiers embedded in regular file paths to enable automated retrieval and iteration

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To automate retrieving, opening and closing submissions, gradetools assumes each student has a unique identifier, specified in the roster, that appears in the student's assignment file path and is the only part unique to that path. Given one example student identifier and assignment path, the package infers a template and iterates through all submissions. The same convention lets graders target specific students for grading or regrading.

## Design Implications

### Context
#### Requirements
- A roster with unique student identifiers and submissions stored with those identifiers present in file paths
#### Constraints
- Some assumption must be made on the way students' assignments are collected or stored; the article notes instructors downloading from an LMS might need string manipulation for filing name consistency

### Target Learners
- data science and statistics students submitting computational assignments

### Target Learning Goals
- efficient handling of multi-file and GitHub-managed assignment submissions

## Related Strategies

- [Mitigate extraction errors by requiring high-resolution PDFs, equation-editor equations, and legible graph axes, units, and legends](report-submission-practices-to-support-ai-evidence-retrieval.md)
- [Combine autograded frequent quizzes with few gradetools-graded open-ended assignments when teaching staff is limited](combine-autograded-quizzes-with-few-open-ended-assignments.md)
- [Four-step anonymization balancing disclosure risk and data utility](four-step-anonymization-engagement-data.md)

## Examples
-

## Key Sources
- Federica Zoe Ricci, Catalina Mari Medina, Mine Dogucu. (2024). Automated grading workflows for providing personalized feedback to open-ended data science assignments. arXiv preprint. https://arxiv.org/abs/2309.12924
