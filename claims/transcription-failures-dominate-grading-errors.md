---
type: claim
title: "Most AI grading errors (87% for the best model) were attributable to transcription failures rather than rubric misapplication"
description: "Most AI grading errors (87% for the best model) were attributable to transcription failures rather than rubric misapplication"
id: transcription-failures-dominate-grading-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jacob-levine-2026
    resource: "https://doi.org/10.48550/arxiv.2605.19043"
    title: "Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043 [doi:10.48550/arxiv.2605.19043](https://doi.org/10.48550/arxiv.2605.19043)"
    author: Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Most AI grading errors (87% for the best model) were attributable to transcription failures rather than rubric misapplication

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Disagreements between AI and human grading were dominated by transcription failures rather than rubric misapplication, with 87% of errors in the best model attributable to transcription. [→ Jacob Levine 2026](#jacob-levine-2026)

## Evidence

### Jacob Levine 2026

Jacob Levine, Miguel Aenlle, Craig Zilles, Matthew West, and Mariana Silva. (2026). Automated Grading of Handwritten Mathematics Using Vision-Capable LLMs. https://arxiv.org/abs/2605.19043 [doi:10.48550/arxiv.2605.19043](https://doi.org/10.48550/arxiv.2605.19043)

`q2 · i?` · `design · r2`

Complete categorization of each rubric item with AI–human disagreement across five questions in two courses, classifying errors as transcription errors or rubric application errors. The article reports disagreements "were dominated by transcription failures rather than rubric misapplication"; the abstract states 87% in the best model. No effect size is printed.

> "As shown in Table 1, disagreements were dominated by transcription failures rather than rubric misapplication, suggesting image capture and preprocessing improvements may yield larger gains than prompt-level refinements."

## Discussion


## Related Claims

- [Gemini frequently corrects board-written math errors with correction logs, but still shows case-consistency and notation-substitution failures](gemini-error-correction-with-case-consistency-failures.md) — related
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](explicit-rubric-conditions-reduce-ai-disagreement.md) — related
- [In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)](vision-llm-letter-recognition-98-84-percent.md)
- [AI self-reported confidence flags identify parts with smaller grading differences, but some high-confidence parts still differ from official scores by more than one point](confidence-flags-triage-human-review.md) — related
- [Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review](llm-chart-extraction-accuracy-failure-modes.md) — related
