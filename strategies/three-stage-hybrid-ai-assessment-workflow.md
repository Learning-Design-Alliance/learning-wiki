---
type: strategy
id: three-stage-hybrid-ai-assessment-workflow
title: "Three-stage hybrid workflow: API batch review, identification of doubtful cases, focused conversational teacher review"
description: "For large courses, the article proposes a combined workflow in three stages: (1) a first AI-assisted review via batch API processing generating structured feedback by rubric criterion; (2) identification of cases requ..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: marcos-abreu-2026
    resource: "https://arxiv.org/abs/2609.22417"
    title: "Marcos Abreu, Cecilia Stari, Arturo C. Martí. (2026). AI-Assisted Assessment of Experimental Physics Laboratory Reports: Potential, Limitations, and Support for Teaching Practice. arXiv. https://arxiv.org/abs/2609.22417"
    author: Marcos Abreu, Cecilia Stari, Arturo C. Martí
---

# Three-stage hybrid workflow: API batch review, identification of doubtful cases, focused conversational teacher review

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For large courses, the article proposes a combined workflow in three stages: (1) a first AI-assisted review via batch API processing generating structured feedback by rubric criterion; (2) identification of cases requiring attention, such as superficial or invalid assessments or evidence with access or interpretation difficulties; (3) focused teacher review through conversational interaction, verifying evidence in the original report and, when needed, directing the model's attention to a specific equation, table, graph, or fragment. This concentrates teacher time on aspects requiring disciplinary and pedagogical expertise.

## Design Implications

### Context
#### Requirements
- Requires instructions, rubric, and output format defined in advance for the API stage, and teacher involvement for the conversational stage.
#### Constraints
- API processing is less flexible for unanticipated situations; conversational interaction is less efficient for large numbers of reports and its responses depend on question formulation.

### Target Learners
- higher education students in large experimental physics courses

### Target Learning Goals
- formative feedback and assessment of laboratory reports

### Affordances
- Evidence Present Versus Effectively Available Distinction

## Related Strategies

- [Use joint AI processing of report sets to identify recurring difficulties and guide collective feedback and teaching priorities](ai-cross-report-pattern-identification-for-teaching.md)
- [Mitigate extraction errors by requiring high-resolution PDFs, equation-editor equations, and legible graph axes, units, and legends](report-submission-practices-to-support-ai-evidence-retrieval.md)

## Examples
-

## Key Sources
- Marcos Abreu, Cecilia Stari, Arturo C. Martí. (2026). AI-Assisted Assessment of Experimental Physics Laboratory Reports: Potential, Limitations, and Support for Teaching Practice. arXiv. https://arxiv.org/abs/2609.22417
