---
type: claim
title: Choice of prompting technique (Zero Shot, In Context Learning, Confirmatory Check) shows no statistically significant effect on LLM Physics question performance at any academic level
description: Choice of prompting technique (Zero Shot, In Context Learning, Confirmatory Check) shows no statistically significant effect on LLM Physics question performance at any academic level
id: prompting-technique-no-significant-effect-physics-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
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

# Choice of prompting technique (Zero Shot, In Context Learning, Confirmatory Check) shows no statistically significant effect on LLM Physics question performance at any academic level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` ANOVA found no significant difference between prompting techniques at GCSE (p = 0.5429), A-Level (p = 0.1310), or introductory university level (p = 0.8828). [→ Will Yeadon 2024](#will-yeadon-2024)

## Evidence

### Will Yeadon 2024

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `causal · r2`

ANOVA of overall scores by prompting technique across the 1337-question evaluation, reported in the results section. The article reports the printed p-values and concludes "we fail to reject the null hypothesis for all three academic levels".

> "For the GCSE, A Level, and Introductory University levels, the p-values were 0.5429, 0.1310, and 0.8828, respectively, indicating that we fail to reject the null hypothesis for all three academic levels."

## Discussion


## Related Claims
- [Confirmatory Check prompting produces the most concise LLM answers, though refinement sometimes reduced quality](confirmatory-check-most-concise-answers.md) — related
- [LLM performance differs significantly across question types at GCSE and A-Level, but which type is best is inconsistent between levels](question-type-affects-llm-physics-accuracy-inconsistently.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
