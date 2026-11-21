---
type: claim
title: GPT-4 grading shows high score variability across repeated rounds, especially for numerical correctness
description: GPT-4 grading shows high score variability across repeated rounds, especially for numerical correctness
id: gpt4-grading-score-variability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: gerd-kortemeyer-2023
    resource: "https://doi.org/10.48550/arXiv.2304.11221"
    title: "Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)"
    author: Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 grading shows high score variability across repeated rounds, especially for numerical correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across an average of 15 grading rounds, many rubric scores have more than one point of standard deviation, particularly numerical correctness for 18 of 25 solutions. [→ Gerd Kortemeyer 2023](#gerd-kortemeyer-2023)

## Evidence

### Gerd Kortemeyer 2023

Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)

`q2 · i?` · `design · r2`

Analysis of rubric grading tables (Tables I–III) from an average of 15 AI grading rounds per solution in batches of five. The author reports large standard deviations for numerical correctness across "18 out of the 25 problems altogether".

> "The correctness of the numerical results, in particular for Solutions 2, 3, 4, 6, 7, etc. — 18 out of the 25 problems altogether: 8 of these solutions actually have the correct numerical answer, 4 are wrong by one or more orders of magnitude, and 6 of the problems have a completely diﬀerent numerical answers due to various reasons."

## Discussion


## Related Claims
- [GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores](gpt4-total-score-correlation-manual-grading.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — a broader claim this one bears on
- [GPT-4o sometimes incorrectly judges non-standard but correct solution approaches as wrong, flagging correct solutions as incorrect in five of 25 tasks](gpt4o-flags-non-standard-correct-approaches-incorrect.md) — related
