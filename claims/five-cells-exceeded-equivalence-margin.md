---
type: claim
title: Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions
description: Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions
id: five-cells-exceeded-equivalence-margin
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pedro-c-mendonça-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100663"
    title: "Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663"
    author: Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Five rubric-assignment combinations exceeded the ±5-point equivalence threshold, concentrated in code questions in Assignments 1 and 2, with the largest deviations about 9.19 and −9.11 points. [→ Pedro C. Mendonça 2026](#pedro-c-mendonca-2026)

## Evidence

### Pedro C. Mendonça 2026

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q3 · i?` · `causal · r2`

Disaggregated analysis of human-evaluator scores by assignment and question type (Table 4). The article reports the largest differences, for DeepSeek Free, as "9.19 and  9.11 points", approximately 9% of the maximum score; Holm-corrected testing left the five cells non-equivalent.

> "The exceptions were confined to five assignment by question-type cells, four of them on code questions in Assignments 1 and 2."

## Discussion


## Related Claims

- [When applied by human evaluators, all four AI-generated rubrics met pooled scoring equivalence with a human-created baseline within a ±5-point margin](ai-rubrics-pooled-equivalence-human-evaluators.md) — related
- [Human inter-rater reliability with a single rubric exceeded the ±5-point equivalence margin used for rubric-source comparisons](human-inter-rater-disagreement-exceeds-margin.md) — related
- [In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline](llm-evaluator-equivalence-depends-on-model.md) — related
- [Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form](open-weight-proprietary-rubric-equivalence.md) — related
- [Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern](structured-free-form-llm-deviation-contrast.md)
