---
type: claim
title: LLM performance differs significantly across question types at GCSE and A-Level, but which type is best is inconsistent between levels
description: LLM performance differs significantly across question types at GCSE and A-Level, but which type is best is inconsistent between levels
id: question-type-affects-llm-physics-accuracy-inconsistently
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: will-yeadon-2024
    resource: "https://doi.org/10.1088/1361-6552/ad1fa2"
    title: "Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)"
    author: Will Yeadon, Tom Hardy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM performance differs significantly across question types at GCSE and A-Level, but which type is best is inconsistent between levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ANOVA by question type (Multiple Choice, Numerical, Word-based) showed statistically significant differences at GCSE and A-Level, with the LLM best on numerical questions at GCSE but best on word-based questions at A-Level. [→ Will Yeadon 2024](#will-yeadon-2024)

## Evidence

### Will Yeadon 2024

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `causal · r2`

Question-type ANOVA within the same 1337-question evaluation, with F-statistics printed in Table 2 (e.g. GCSE Confirmatory Check F = 92.3540). The article reports the level-inconsistent pattern: "best on numerical questions at GCSE but best on word based at A-Level".

> "the ANOV A test results for the GCSE and A Level, as showcased in Table 2, indicate a statistically significant difference in the performance of the three prompting techniques across the various question types. Yet the differences are not consistent between academic levels with the LLM performing best on numerical questions at GCSE but best on word based at A-Level."

## Discussion


## Related Claims
- [Choice of prompting technique (Zero Shot, In Context Learning, Confirmatory Check) shows no statistically significant effect on LLM Physics question performance at any academic level](prompting-technique-no-significant-effect-physics-questions.md) — related
- [Question type affects accuracy: feature-to-concept questions are answered best and applied questions worst](question-type-accuracy-ordering.md) — related
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — related
