---
type: claim
title: An on-premises LLM autograder graded a 200-student course at 1–3 minutes wall-clock time per submission across a full term
description: An on-premises LLM autograder graded a 200-student course at 1–3 minutes wall-clock time per submission across a full term
id: lata-onprem-autograder-throughput
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jesse-a-rodríguez-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05410"
    title: "Jesse A. Rodríguez. (2026). LaTA: A Drop-In, FERPA-Compliant Local-LLM Autograder for Upper-Division STEM Coursework. arXiv preprint. https://arxiv.org/abs/2605.05410 [doi:10.48550/arxiv.2605.05410](https://doi.org/10.48550/arxiv.2605.05410)"
    author: Jesse A. Rodríguez
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An on-premises LLM autograder graded a 200-student course at 1–3 minutes wall-clock time per submission across a full term

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across eight homework assignments, LaTA graded the 200-student roster in 1–3 minutes of wall-clock time per submission, with per-assignment totals driven by problem count and solution length rather than class size. [→ Jesse A. Rodríguez 2026](#jesse-a-rodriguez-2026)

## Evidence

### Jesse A. Rodríguez 2026

Jesse A. Rodríguez. (2026). LaTA: A Drop-In, FERPA-Compliant Local-LLM Autograder for Upper-Division STEM Coursework. arXiv preprint. https://arxiv.org/abs/2605.05410 [doi:10.48550/arxiv.2605.05410](https://doi.org/10.48550/arxiv.2605.05410)

`q2 · i?` · `design · r2`

Operational evidence collected by the instructor during the Winter 2026 term in ME 373, recorded as the standard output of each grading run. The quote reports the printed per-submission wall-clock time on the single Mac Studio host.

> "LaTA graded the 200-student roster in 1–3 minutes of wall-clock time per submission on the Mac Studio M3 Ultra described in §4.1, with the per-assignment total dominated by the number of problems and the length of the worked solutions rather than by class size."

## Discussion


## Related Claims
- [The between-cohort exam gain is attributable only to a composite intervention (autograding plus corrections plus expanded office hours), not to LaTA alone](composite-intervention-exam-confound.md) — related
- [Instructor-confirmed grading errors occurred at roughly 0.02–0.04% of rubric line items across the term](lata-instructor-confirmed-error-rate.md) — related
- [Student perceptions of the autograder were mixed, with the LaTeX workflow rated more positively than the grader itself](mixed-student-perception-lata.md) — related
- [Students reported first-pass false-positive deductions at a mean of 2.94 per term, normalising to about 0.6% of rubric items](student-reported-grading-errors-lata.md) — related
- [Student-reported LaTeX time overhead fell about 46% across the term, from 87 to 47 minutes per assignment](latex-ramp-down-cost-reduction.md) — related
- [A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time](ai-grading-workflow-feasibility-cost.md) — related
- [About 400 labeled proofs are sufficient for adequate autograding performance](400-proofs-sufficient-training.md) — related
