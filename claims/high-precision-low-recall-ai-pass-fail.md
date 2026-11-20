---
type: claim
title: AI-assisted grading achieves high precision for identifying passing exams but low recall, meaning failing grades still require human grading
description: AI-assisted grading achieves high precision for identifying passing exams but low recall, meaning failing grades still require human grading
id: high-precision-low-recall-ai-pass-fail
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# AI-assisted grading achieves high precision for identifying passing exams but low recall, meaning failing grades still require human grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The AI grading workflow has very high precision (0.9468 without and 0.9589 with threshold criteria) but low recall (0.4972 and 0.4698 respectively) for pass/fail decisions. [→ Gerd Kortemeyer 2024](#gerd-kortemeyer-2024)

## Evidence

### Gerd Kortemeyer 2024

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Contingency-table analysis of AI versus TA pass/fail decisions for all 252 students using WF2 with a passing threshold of 24 points. High precision means AI-assigned passing grades are usually correct; low recall means many TA-passing students are AI-failed.

> "The workflow has very high precision, (0.9468 and 0.9589 without and with threshold criteria, respectively), but low recall (0.4972 and 0.4698, respectively)."

## Discussion


## Related Claims
- [Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions](ethel-grading-reliability-format-precision-recall.md) — possibly the same claim (merge candidate)
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point](confidence-flags-triage-human-review.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
