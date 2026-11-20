---
type: claim
title: "ChatGPT scores 100% on most database-course labs but fails UML/ER diagram tasks, scoring 28.5/30 on midterm 1 and 17/30 on midterm 2"
description: "ChatGPT scores 100% on most database-course labs but fails UML/ER diagram tasks, scoring 28.5/30 on midterm 1 and 17/30 on midterm 2"
id: chatgpt-database-course-variable-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kevin-wang-2023
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: kevin-wang-2023-2
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT scores 100% on most database-course labs but fails UML/ER diagram tasks, scoring 28.5/30 on midterm 1 and 17/30 on midterm 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT achieved excellent marks on relational algebra, SQL, and XML/JSON labs in an upper-year database course, but scored 0% on UML modeling labs A4 and A5. [→ Kevin Wang 2023](#kevin-wang-2023)
`q2 i?` ChatGPT obtained 28.5/30 on midterm 1 but only 17/30 on midterm 2, losing 10 points allocated to ER diagrams. [→ Kevin Wang 2023 (2)](#kevin-wang-2023-2)

## Evidence

### Kevin Wang 2023

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `design · r2`

Evaluation of ChatGPT 3.5 on the database course's 10 assignments using prompts with template code, DDL, and rubrics. The study reports "very high performance with excellent marks" for labs 1, 2, 3, and 9, while labs 4 and 5 (UML/ER diagrams) received 0% because ChatGPT does not draw diagrams as required.

> "ChatGPT has very high performance with excellent marks (see Table III) for labs 1, 2, 3, and 9 on relational algebra, SQL, and XML/JSON."

### Kevin Wang 2023 (2)

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `design · r2`

Evaluation of ChatGPT 3.5 on two computer-based database midterms, with questions and context (e.g., DDL) copied as prompts and graded. The study reports midterm 1 at 28.5/30 (95%) and midterm 2 at 17/30 (57%), attributing the midterm 2 loss to the 10 ER-diagram points.

> "ChatGPT tested extremely well in midterm 1, obtaining a 28.5/30, while getting only 17/30 on midterm 2 due to the 10 points allocated to ER diagrams."

## Discussion


## Related Claims
- [Assessments more resistant to ChatGPT are open-ended, involve images or student-specific outputs, or do not specify expected output in detail](assessment-features-resistant-to-chatgpt.md) — a broader claim this one bears on
- [On descriptive analytical tasks ChatGPT produced logically structured work but lacked deep contextualization, domain-specific insights, and visual elements](chatgpt-descriptive-tasks-generic-outputs.md) — related
- [ChatGPT performs poorly on health database SQL programming tasks, with the best AI version scoring 56% against a top student score of 100%](chatgpt-sql-programming-weak.md) — related
- [ChatGPT performs best on objective health classification quiz items (88%) but scores only 7% on scenario-based clinical coding, far below the top student (87%)](chatgpt-objective-strong-scenario-coding-weak.md) — related
- [ChatGPT scores rose from V1 to V3 across assessment types in one uncontrolled pre-post study, with V3 achieving the highest average scores](rubric-integration-improves-chatgpt-scores.md) — related
- [The advanced o1 Preview model did not consistently outperform GPT-4, underperforming V3 on descriptive tasks](o1-preview-no-consistent-advantage.md) — related
