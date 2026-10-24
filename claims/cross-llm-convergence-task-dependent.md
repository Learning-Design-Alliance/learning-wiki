---
type: claim
title: "Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10"
description: "Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10"
id: cross-llm-convergence-task-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Pooled across the ten labs, 87.79–88.14% of cross-LLM pairs matched after docstring removal, only 3.40–3.61 percentage points below within-LLM rates; across Labs 1–9 cross-LLM rates were 95.48–96.08%, but on Lab 10 they were 13.18–22.11%. [→ Runlong Ye 2026](#runlong-ye-2026)

## Evidence

### Runlong Ye 2026

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)

`q2 · i?` · `associational · r2`

MOSS similarity analysis of 3,000 attempts per cohort (1,000 per model) with starter files registered as base files and docstrings removed. The article reports cross-LLM rates of 95.48–96.08% on Labs 1–9 versus 13.18–22.11% on Lab 10 (Table 3).

> "Using all 1,000 attempts from each LLM and pooling the ten labs within each cohort, 87.79–88.14% of cross-LLM pairs matched after docstring removal. The corresponding within-LLM rates were 91.35–91.72%, only 3.40–3.61 percentage points higher (Table 3)."

## Discussion


## Related Claims
- [Frontier LLMs produced near-perfect solutions to CS1 labs, with mean hidden-instructor-test scores of 98.93–99.99% across model–year combinations](llm-near-perfect-cs1-lab-solutions.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions](exact-ast-form-convergence-constrained-functions.md) — related
