---
type: claim
title: "All High-experience participants authored expert models with 100% correctness on both tasks, while one Low-experience participant's model dropped to 20% on fraction multiplication."
description: "All High-experience participants authored expert models with 100% correctness on both tasks, while one Low-experience participant's model dropped to 20% on fraction multiplication."
id: atb-model-correctness-by-experience-group
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

# All High-experience participants authored expert models with 100% correctness on both tasks, while one Low-experience participant's model dropped to 20% on fraction multiplication.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` All participants in the High programming-experience group authored models with 100% model correctness for both tasks, and all participants in both groups achieved 100% for the S25 tutor. [→ Glen Smith 2024](#glen-smith-2024)
`q2 i?` One Low-group participant's model correctness rate decreased to 20% on fraction multiplication problems in the FR tutor. [→ Glen Smith 2024 (2)](#glen-smith-2024-2)

## Evidence

### Glen Smith 2024

Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)

`q2 · i?` · `design · r2`

Model correctness was measured as the successful solve rate of 20 randomly generated FR problems (10 multiplication, 10 addition) and 10 S25 problems; all models were tested with the same 30 problems. "All participants in the High group" reached 100% on both tasks.

> "All participants in the High group (moderate to high exp.) were able to author a model with 100% model correctness for both tasks."

### Glen Smith 2024 (2)

Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. [doi:10.48550/arXiv.2404.07883](https://doi.org/10.48550/arXiv.2404.07883)

`q2 · i?` · `design · r2`

Log analysis of the same correctness test. The article attributes the failure to the participant training only with problems containing at least one 1 in the numerators, so the agent learned only that edge case, which "does not generalize to problems where neither of the numerators contains a 1".

> "However, for one participant in the Low group, the model correctness rate decreased to 20% when solving fraction multiplication problems in the FR tutor."

## Discussion


## Related Claims
- [In a user study, all 14 instructor participants recreated both tutor interfaces with the builder and 13 of 14 authored expert models that could solve both tasks.](atb-14-instructors-built-tutors-13-authored-models.md) — related
