---
type: claim
title: On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data
description: On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data
id: cat-extends-to-prm800k-validation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: moiz-imran-and-sahan-bulathwela-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On PRM800K, the best model's detection rates dropped by 10.5 percentage points when final answers were correct (83% vs 93.5%, Fisher's exact p <0.003). [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925 [doi:10.48550/arxiv.2605.23925](https://doi.org/10.48550/arxiv.2605.23925)

`q2 · i?` · `associational · r?`

Validation on PRM800K, a process supervision dataset with human-labelled reasoning errors in model-generated competition mathematics, sampling 200 correct-answer error cases and 200 matched wrong-answer cases. Detection dropped "by 10.5 percentage points" for correct-answer cases.

> "Detection rates dropped by 10.5 percentage points when final answers were correct (83% vs 93.5%, Fisher's exactp <0.003), consistent with our primary findings."

## Discussion


## Related Claims
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification — related
- [Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases](cat-failures-concentrate-in-two-question-types.md) — related
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size](step-level-supervision-essential-misconception-acquisition.md) — related
- [The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%](rhythm-error-detection-recall-91-2.md) — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
