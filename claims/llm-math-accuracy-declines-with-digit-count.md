---
type: claim
title: LLM mathematical accuracy decreases as the number of digits increases, and varies by operation type
description: LLM mathematical accuracy decreases as the number of digits increases, and varies by operation type
id: llm-math-accuracy-declines-with-digit-count
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
    kind: design
    rigour: 2
  - id: will-yeadon-2024-2
    resource: "https://doi.org/10.1088/1361-6552/ad1fa2"
    title: "Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)"
    author: Will Yeadon, Tom Hardy
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM mathematical accuracy decreases as the number of digits increases, and varies by operation type

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly
> **Design limits** · Will Yeadon 2023 (2): no comparison group (read from the study by two models, 2026-11-19)

## Subclaims
`q2 i?` On 5000 generated mathematical operations the LLM achieved 52.3% exact accuracy on two-integer operations (75.8% within 5% tolerance) and 38.1% exact accuracy on single-operand functions, with performance diminishing as digit count increased. [→ Will Yeadon 2024](#will-yeadon-2024)
`q2 i?` Multiplication and division were less reliable than addition and subtraction, especially with higher-digit numbers, and the LLM struggled with trigonometric functions beyond single digits. [→ Will Yeadon 2024 (2)](#will-yeadon-2024-2)

## Evidence

### Will Yeadon 2024

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `design · r2`

Generated dataset of 2,500 integer-pair arithmetic operations stratified by digit length, assessed by perfect match and tolerance criteria. The article prints "an exact accuracy rate of 52.3%" rising to 75.8% with a 5% tolerance.

> "For the two-integer operations, the LLM achieved an exact accuracy rate of 52.3% across all questions. When a tolerance of ±5% of the exact answer was considered, the accuracy rate climbed to 75.8%."

### Will Yeadon 2024 (2)

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `causal · r1`

Operation-type breakdown of the same arithmetic dataset, illustrated in Figure 5. The article reports high addition/subtraction accuracy but less reliable "multiplication and division ... especially with higher-digit numbers".

> "While the model demonstrated high accuracy in addition and subtraction across all levels of numerical complexity, its performance in multiplication and division was less reliable, especially with higher-digit numbers."

## Discussion


## Related Claims
- [Working memory demand increases with the complexity of arithmetic and math problems, including operand size and number of solution steps](working-memory-demand-increases-with-math-problem-complexity.md) — a broader claim this one bears on
- [RAN correlates more strongly with single-digit than multi-digit calculation and with fluency than accuracy outcomes](ran-single-digit-fluency-moderators.md) — related
