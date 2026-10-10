---
type: claim
title: "A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)"
description: "A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)"
id: task-specific-prompt-beats-pedcot-prompting
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
    kind: causal
    rigour: "?"
---

# A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` The task-specific prompt significantly outperformed literature-based PedCoT prompting on the 61 TM test cases (84% vs 59% accuracy, McNemar's p <0.01). [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `causal · r?`

Prompt validation experiment comparing the paper's task-specific prompt against PedCoT literature-based prompting on the 61 TM test cases. The task-specific prompt reached 84% versus 59% accuracy, significant by McNemar's test (p <0.01).

> "We validated this prompt against PedCoT [11] on the 61 TM test cases, finding our task-specific prompt significantly outperforms literature-based prompting (84% vs 59% accuracy, McNemar'sp <0.01)."

## Discussion


## Related Claims
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification](fine-tuned-classifiers-miss-correct-answer-misconceptions.md) — related
- [Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students](mark-scheme-reduces-false-positives.md) — related
- [Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases](cat-failures-concentrate-in-two-question-types.md) — related
