---
type: claim
title: IRT-predicted partial credit provides a ground-truth-free, per-student-per-item uncertainty measure for AI grading judgements
description: IRT-predicted partial credit provides a ground-truth-free, per-student-per-item uncertainty measure for AI grading judgements
id: ground-truth-free-irt-grading-uncertainty
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

# IRT-predicted partial credit provides a ground-truth-free, per-student-per-item uncertainty measure for AI grading judgements

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Uncertainty was defined as the absolute difference between the IRT-predicted partial credit and the AI-assigned score for each student-item combination. [→ Gerd Kortemeyer and Julian Nöhl 2025](#gerd-kortemeyer-and-julian-nohl-2025)
`q2 i?` The uncertainty matrix was computed entirely from AI grading data, without any reference to ground truth. [→ Gerd Kortemeyer and Julian Nöhl 2025 (2)](#gerd-kortemeyer-and-julian-nohl-2025-2)

## Evidence

### Gerd Kortemeyer and Julian Nöhl 2025

Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)

`q2 · i?` · `design · r3`

Methodological definition in the uncertainty-determination section: 2PL-IRT predictions pi(θj), based on the student's latent ability and the item's difficulty and discrimination, are compared with the AI-assigned score to yield uij.

> "The absolute difference between the predicted partial credit and the AI-assigned score sij was then taken as a measure of uncertainty uij"

### Gerd Kortemeyer and Julian Nöhl 2025 (2)

Gerd Kortemeyer and Julian Nöhl. (2025). Assessing Confidence in AI-Assisted Grading of Physics Exams through Psychometrics: An Exploratory Study. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010136](https://doi.org/10.1103/physrevphyseducres.21.010136)

`q2 · i?` · `design · r3`

The article emphasizes that the uncertainty measure is computed before ground truth is consulted, supporting its second hypothesis that Bayesian predictive power can assess AI grading validity on a per-student-per-item basis.

> "Note that up to this point, no reference to ground truth is employed; the matrix uij is based completely on AI-grading."

## Discussion


## Related Claims
- [Psychometric measures can be used, without reference to ground truth, to iteratively improve an AI grading rubric by identifying outlier rubric items](psychometric-rubric-refinement-ai-grading.md) — a broader claim this one bears on
- [Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — related
- [Grading answers required weighted partial credit because responses varied in degrees of rightness](weighted-partial-credit-grading.md) — related
- [LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other](llm-short-answer-graders-can-reach-human-rater-agreement.md) — related
