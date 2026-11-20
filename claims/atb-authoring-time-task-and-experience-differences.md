---
type: claim
title: Average authoring time was higher for the Fraction Arithmetic task (11.85 min) than the Square 25 task (7.12 min), with programming experience moderating interface-building and agent-training times in opposite directions across tasks.
description: Average authoring time was higher for the Fraction Arithmetic task (11.85 min) than the Square 25 task (7.12 min), with programming experience moderating interface-building and agent-training times in opposite directi...
id: atb-authoring-time-task-and-experience-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: glen-smith-2024
    resource: "https://doi.org/10.48550/arXiv.2404.07883"
    title: "Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)"
    author: Glen Smith, Adit Gupta, and Chris MacLellan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: glen-smith-2024-2
    resource: "https://doi.org/10.48550/arXiv.2404.07883"
    title: "Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)"
    author: Glen Smith, Adit Gupta, and Chris MacLellan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Average authoring time was higher for the Fraction Arithmetic task (11.85 min) than the Square 25 task (7.12 min), with programming experience moderating interface-building and agent-training times in opposite directions across tasks.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Overall authoring time was higher for the Fraction Arithmetic task (Avg: 11.85 min) than the Square 25 task (Avg: 7.12 min). [→ Glen Smith 2024](#glen-smith-2024)
`q2 i?` For the FR tutor the Low experience group spent less time training the expert model than the High group (10.9 vs 16 min), but for the S25 tutor the Low group spent more time training (7 vs 4.2 min). [→ Glen Smith 2024 (2)](#glen-smith-2024-2)

## Evidence

### Glen Smith 2024

Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)

`q2 · i?` · `design · r2`

Quantitative analysis of user logs from the 14-participant study, reported in the User Log Analysis subsection. The article notes the fractions task takes longer because it requires teaching the agent multiple problem types; "Overall authoring time is higher for the Fractions Arithmetic (FR) task".

> "Overall authoring time is higher for the Fractions Arithmetic (FR) task (Avg: 11.85 min) compared to the Square 25 (S25) task (Avg: 7.12 min)"

### Glen Smith 2024 (2)

Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)

`q2 · i?` · `design · r2`

User log analysis grouping participants by programming experience (Low vs High). For the S25 tutor the pattern reversed, with the Low group spending more time training the expert model (Avg: 7 min vs. 4.2 min).

> "For the FR tutor, those in the Low group spent slightly more time building the interface than the High group (Avg: 6.2 min vs. 5.5 min), but spent significantly less time training the expert model than the High group (Avg. 10.9 min vs. 16 min)."

## Discussion


## Related Claims
- [In a user study, all 14 instructor participants recreated both tutor interfaces with the builder and 13 of 14 authored expert models that could solve both tasks.](atb-14-instructors-built-tutors-13-authored-models.md) — related
- [Validation-problem counts moved in opposite directions for the two experience groups: the Low group's average rose from 0.33 to 1.0 across tasks while the High group's fell from 2.25 to 0.15.](atb-validation-problems-group-trends.md) — related
- [The Low programming-experience group had a higher incidence of delete actions during interface building (Avg: 7.1 vs 3.4), explaining their longer S25 interface authoring time.](atb-delete-actions-explain-interface-time-gap.md) — related
