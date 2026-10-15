---
type: strategy
id: human-in-the-loop-teacher-validation-workflow
title: "Human-in-the-loop validation workflow: hold all AI-generated teaching content in unreviewed status until a teacher manually approves it"
description: "The strategy places teachers as essential validators in the content pipeline: AI-generated materials and quizzes are created automatically but held in unreviewed status, and teachers use a built-in Markdown editor to..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: anna-ostrowska-2026
    resource: "https://tinyurl.com/mrytc2dr"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
---

# Human-in-the-loop validation workflow: hold all AI-generated teaching content in unreviewed status until a teacher manually approves it

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The strategy places teachers as essential validators in the content pipeline: AI-generated materials and quizzes are created automatically but held in unreviewed status, and teachers use a built-in Markdown editor to refine questions before approving release to students. Validated assessments can then be exported in Moodle XML format into the institutional Question Bank. The article frames this as maintaining teacher control while reducing the burden of manual content creation, since "every AI-generated quiz or study guide must be manually approved before students receive it".

## Design Implications

### Context
#### Requirements
- Educators with access to the Teaching Assistant tab to manage course context and review content
- A review status mechanism that blocks unreviewed AI-generated content from reaching students
#### Constraints
- Applies to AI-generated materials and quizzes within the Moodle-integrated system; the article does not claim it removes hallucination risk entirely

### Target Learners
- university instructors
- higher education students

### Target Learning Goals
- accurate, teacher-verified learning content
- reduced misinformation exposure

## Related Strategies

- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)
- [Center co-design with teachers and students throughout AI tool R&D, using human-in-the-loop workflows as a primary risk mitigation](co-design-human-in-the-loop-ai-edtech-strategy.md)
- [Position the instructor as human-in-the-loop reviewer of AI-generated difficulty reports before any feedback reaches students](instructor-in-loop-ai-difficulty-reports.md)
- [Generative-AI-assisted content creation with domain-expert validation for adaptive tutoring systems](genai-assisted-content-creation-expert-validation.md)

## Examples
-

## Key Sources
- Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr
