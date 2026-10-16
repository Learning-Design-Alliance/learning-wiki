---
type: claim
title: gpt-4o graded student submissions most correctly in almost all assignments, but gemini-1.0-pro graded the boolean-algebra assignment most correctly
description: gpt-4o graded student submissions most correctly in almost all assignments, but gemini-1.0-pro graded the boolean-algebra assignment most correctly
id: grader-llm-correctness-comparison-socrates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: xinming-yang-2025
    resource: "https://doi.org/10.48550/arxiv.2508.05979"
    title: "Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979 [doi:10.48550/arxiv.2508.05979](https://doi.org/10.48550/arxiv.2508.05979)"
    author: Xinming Yang, Haasil Pujara, Jun Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: xinming-yang-2025-2
    resource: "https://arxiv.org/abs/2508.05979"
    title: "Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979"
    author: Xinming Yang, Haasil Pujara, Jun Li
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# gpt-4o graded student submissions most correctly in almost all assignments, but gemini-1.0-pro graded the boolean-algebra assignment most correctly

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` Across the four assignments, gpt-4o showed the highest grader correctness in almost all assignments except A3. [→ Xinming Yang 2025](#xinming-yang-2025)
`q2 i?` For assignment A3 on boolean algebra transformations, gemini-1.0-pro achieved much higher correctness than both gpt-3.5-turbo and gpt-4o. [→ Xinming Yang 2025 (2)](#xinming-yang-2025-2)

## Evidence

### Xinming Yang 2025

Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979 [doi:10.48550/arxiv.2508.05979](https://doi.org/10.48550/arxiv.2508.05979)

`q2 · i?` · `design · r2`

Log-based observational analysis of grader correctness on the four assignments' submissions, comparing grader results with manual grading and combining true positives and true negatives. The article reports "In almost all assignments (except A3), gpt-4o demonstrates the highest correctness." No effect size is printed.

> "In almost all assignments (except A3), gpt-4o demonstrates the highest correctness."

### Xinming Yang 2025 (2)

Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979

`q2 · i?` · `causal · r1`

Same grader-correctness log analysis, assignment A3. The article calls this "a tentative observation specific to our test cases" suggesting a potential strength of gemini-1.0-pro on this type of logical reasoning problem. No effect size is printed.

> "for assignment A3, which focused on applying transformations in boolean algebra, gemini-1.0-pro achieved much higher correctness than both gpt-3.5-turbo and gpt-4o."

## Discussion


## Related Claims
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
- [Gemini and Gemini Pro show the highest internal grading consistency across file upload volumes, with no clear monotonic lost-in-the-middle effect](gemini-highest-consistency-across-file-volumes.md) — related
- [Running the Socrates playground and grader incurred low cost, with even gpt-4o consuming only $169.90](socrates-low-operational-cost.md) — related
