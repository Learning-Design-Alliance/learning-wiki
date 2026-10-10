---
type: claim
title: "Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases"
description: "Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases"
id: cat-failures-concentrate-in-two-question-types
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` In the Eedi dataset, the top two question types alone account for 71% of all true-misconception (TM) cases, rather than failures distributing uniformly across questions. [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `associational · r?`

Analysis of the Eedi benchmark of 20,964 real student responses, with 343 TM cases labelled by expert raters. The authors report that "The top two question types alone account for 71% of all TM cases", visualised in Fig. 1.

> "Table 1 shows that TM cases concentrate in specific question types rather than distribute uniformly. The top two question types alone account for 71% of all TM cases."

## Discussion


## Related Claims
- [CAT concentration is item-driven, not category-driven: removing the two vulnerable items collapses the procedural/conceptual odds ratio from 5.6 to 1.0](cat-vulnerability-item-driven-not-category-driven.md) — related
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
