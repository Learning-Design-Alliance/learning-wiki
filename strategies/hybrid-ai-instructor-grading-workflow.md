---
type: strategy
id: hybrid-ai-instructor-grading-workflow
title: Use a hybrid AI-then-instructor grading workflow with immutable override history
description: "The system implements grading as a two-stage workflow: \"Firstly, AI scores the initial score, and then the teacher confirms whether the score is reasonable\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: fuan-xiao-2026
    resource: "https://doi.org/10.1186/s41239-026-00618-5"
    title: "Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5"
    author: Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li
---

# Use a hybrid AI-then-instructor grading workflow with immutable override history

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The system implements grading as a two-stage workflow: "Firstly, AI scores the initial score, and then the teacher confirms whether the score is reasonable". The teacher can overwrite the AI's grade, and both the original and overwritten transactions remain visible in the chain history so scoring can be traced back. Instructors grade manually through the LMS, which calls the blockchain recordGrade function with the teacher's signature instead of the AI's input.

## Design Implications

### Context
#### Requirements
- Instructors must hold blockchain identities enabling them to approve grades and initiate certificate issuance through smart contracts
#### Constraints
- 

### Target Learners
- higher education students
- online course instructors

### Target Learning Goals
- reliable and auditable assessment of student work

### Affordances
- Llm Consortium Blockchain Online Education Architecture

## Related Strategies

- [Three-stage hybrid workflow: API batch review, identification of doubtful cases, focused conversational teacher review](three-stage-hybrid-ai-assessment-workflow.md)

## Examples
-

## Key Sources
- Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5
