---
type: claim
title: Rubric-based and parts-based grading workflows outperform problem-based grading, possibly because GPT-4-32k cannot reliably add numbers
description: Rubric-based and parts-based grading workflows outperform problem-based grading, possibly because GPT-4-32k cannot reliably add numbers
id: wf1-wf2-outperform-wf3-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: gerd-kortemeyer-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.020144"
    title: "Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)"
    author: Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Rubric-based and parts-based grading workflows outperform problem-based grading, possibly because GPT-4-32k cannot reliably add numbers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Workflows WF1 (rubric-based) and WF2 (parts-based) clearly outperform WF3 (problem-based) in agreement with TA grades. [→ Gerd Kortemeyer 2024](#gerd-kortemeyer-2024)

## Evidence

### Gerd Kortemeyer 2024

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Comparison of workflows on Problem 1 (252 exams). WF3 achieved R²=0.43 versus R²=0.58 (WF1) and R²=0.56 (WF2). The model was unable to correctly add five point values, reporting 11.5 instead of 11.

> "Workflows WF1 and WF2 clearly outperform WF3 (possibly simply be- cause GPT-4-32k cannot add numbers)."

## Discussion


## Related Claims
- [Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances](rubric-granularity-affects-ai-grading-reliability.md) — a narrower finding that bears on this claim
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores](gpt4-total-score-correlation-manual-grading.md) — related
