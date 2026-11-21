---
type: claim
title: Psychometric measures can be used, without reference to ground truth, to iteratively improve an AI grading rubric by identifying outlier rubric items
description: Psychometric measures can be used, without reference to ground truth, to iteratively improve an AI grading rubric by identifying outlier rubric items
id: psychometric-rubric-refinement-ai-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gerd-kortemeyer-and-julian-nöhl-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010136"
    title: "Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)"
    author: Gerd Kortemeyer and Julian Nöhl
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: gerd-kortemeyer-and-julian-nöhl-2025-2
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010136"
    title: "Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)"
    author: Gerd Kortemeyer and Julian Nöhl
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Psychometric measures can be used, without reference to ground truth, to iteratively improve an AI grading rubric by identifying outlier rubric items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rubric items identified as outliers via standard deviation across repeated AI gradings, IRT item parameters, and inter-item correlations were refined and the affected problem parts regraded. [→ Gerd Kortemeyer and Julian Nöhl 2025](#gerd-kortemeyer-and-julian-nohl-2025)
`q2 i?` Because each item was graded ten times independently, the standard deviation of assigned partial credit served as a proxy for the clarity of a rubric item. [→ Gerd Kortemeyer and Julian Nöhl 2025 (2)](#gerd-kortemeyer-and-julian-nohl-2025-2)

## Evidence

### Gerd Kortemeyer and Julian Nöhl 2025

Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)

`q2 · i?` · `design · r3`

Rubric-refinement procedure in the methodology: three measures (spread across runs, IRT item parameters, correlations) flagged suspect items, which were then refined and regraded. The article states the outliers were "subjectively identified," so the refinement step itself involved researcher judgment.

> "The formulations of rubric items that based on these three measures were subjectively identified as outliers were refined, and the problem parts that they belonged to were regraded by the AI."

### Gerd Kortemeyer and Julian Nöhl 2025 (2)

Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)

`q2 · i?` · `design · r3`

Each rubric item was graded in ten independent GPT-4-Turbo runs; the article proposes the "standard deviation of the assigned partial-credit percentages" as a proxy for rubric-item clarity, analogous to inter-rater reliability.

> "As each item is graded ten times, the standard deviation of the assigned partial-credit percentages could be considered as a measure of the clarity of the rubric item."

## Discussion


## Related Claims
- [IRT-predicted partial credit provides a ground-truth-free, per-student-per-item uncertainty measure for AI grading judgements](ground-truth-free-irt-grading-uncertainty.md) — a narrower finding that bears on this claim
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers](pooling-repeated-llm-grades-does-not-improve-agreement.md) — related
- [Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — related
- [The TA ground truth was produced under a one-rater-per-item design with co-grading, an exceptions log, instructor audit, and student review, with an estimated grading-error rate of about 0.1% in the student-inspected subsample](ta-ground-truth-one-rater-per-item-error-rate.md) — related
