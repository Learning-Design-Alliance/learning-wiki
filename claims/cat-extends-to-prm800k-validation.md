---
type: claim
title: On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data
description: On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data
id: cat-extends-to-prm800k-validation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: moiz-imran-and-sahan-bulathwela-2026
    resource: "https://arxiv.org/abs/2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` On PRM800K, the best model's detection rates dropped by 10.5 percentage points when final answers were correct (83% vs 93.5%, Fisher's exact p <0.003). [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `associational · r?`

Validation on PRM800K, a process supervision dataset with human-labelled reasoning errors in model-generated competition mathematics, sampling 200 correct-answer error cases and 200 matched wrong-answer cases. Detection dropped "by 10.5 percentage points" for correct-answer cases.

> "Detection rates dropped by 10.5 percentage points when final answers were correct (83% vs 93.5%, Fisher's exactp <0.003), consistent with our primary findings."

## Discussion


## Related Claims
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification](fine-tuned-classifiers-miss-correct-answer-misconceptions.md) — related
- [Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases](cat-failures-concentrate-in-two-question-types.md) — related
