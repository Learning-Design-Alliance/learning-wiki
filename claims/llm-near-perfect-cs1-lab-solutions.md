---
type: claim
title: "Frontier LLMs produced near-perfect solutions to CS1 labs, with mean hidden-instructor-test scores of 98.93–99.99% across model–year combinations"
description: "Frontier LLMs produced near-perfect solutions to CS1 labs, with mean hidden-instructor-test scores of 98.93–99.99% across model–year combinations"
id: llm-near-perfect-cs1-lab-solutions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: runlong-ye-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00863"
    title: "Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)"
    author: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Frontier LLMs produced near-perfect solutions to CS1 labs, with mean hidden-instructor-test scores of 98.93–99.99% across model–year combinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Across LLM–year combinations, mean instructor-test scores for generated solutions ranged from 98.93% to 99.99%, far above student means of 76.37–88.03%, and LLM full-pass rates ranged from 86.97% to 99.95%. [→ Runlong Ye 2026](#runlong-ye-2026)

## Evidence

### Runlong Ye 2026

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)

`q2 · i?` · `associational · r2`

Retrospective grading of 90,000 LLM attempts (three frontier models, 1,000 per lab per cohort year) and 29,970 student submissions against each year's hidden instructor pytest suite. The article reports LLM means of "98.93% to 99.99%" versus student means of 76.37%, 80.76%, and 88.03% (Table 1).

> "Across LLM–year combinations, with labs pooled within each combination, mean instructor-test scores ranged from 98.93% to 99.99%, compared with 76.37%, 80.76%, and 88.03% for student submissions in 2021, 2023, and 2025, respectively (Table 1)."

## Discussion


## Related Claims
- [Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10](cross-llm-convergence-task-dependent.md) — related
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
- [On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions](exact-ast-form-convergence-constrained-functions.md) — related
- [Student submissions matched the LLM-generated reference bank more often in later cohorts, with 2025 incidence 1.76–2.12 times the 2021 rate, persisting among full-pass submissions](student-llm-match-incidence-rose-across-cohorts.md) — related
