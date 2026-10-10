---
type: claim
title: "Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall"
description: "Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall"
id: frontier-llms-best-balance-tm-detection
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
    kind: causal
    rigour: "?"
  - id: moiz-imran-and-sahan-bulathwela-2026-2
    resource: "https://arxiv.org/abs/2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925"
    author: Moiz Imran and Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q2`

## Subclaims
`q2 i?` Gemini 3 Flash reaches 83.6% TM recall with 94.0% TC recall, significantly better than fine-tuned T5 on TM detection. [→ Moiz Imran and Sahan Bulathwela 2026](#moiz-imran-and-sahan-bulathwela-2026)
`q2 i?` Fine-tuned T5 and BERT achieve under 58% TM recall despite near-perfect separation of correct and incorrect answers (FM recall at or above 98%). [→ Moiz Imran and Sahan Bulathwela 2026 (2)](#moiz-imran-and-sahan-bulathwela-2026-2)

## Evidence

### Moiz Imran and Sahan Bulathwela 2026

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `causal · r?`

Model comparison on the 61-case TM test set from the Eedi benchmark. The authors report Gemini 3 Flash "improves TM recall to 83.6% [72.4, 90.8]" with a significant McNemar's test over T5 (p= 0.005).

> "Gemini 3 Flash improves TM recall to 83.6% [72.4, 90.8] while maintaining 94.0% TC recall; the improvement over T5 is significant (McNemar's test,p= 0.005)."

### Moiz Imran and Sahan Bulathwela 2026 (2)

Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925

`q2 · i?` · `design · r?`

Evaluation of fine-tuned T5-small and BERT-base classifiers on the Eedi test data; both models detect few true-misconception cases among correct answers, with TM recall "under 58%".

> "Both achieve under 58% TM recall, showing that optimisation for domi- nant labels leaves rare TM cases under-detected."

## Discussion


## Related Claims
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [Mined misconception labels match personas' assigned misconceptions at F1 ≈ 0.56, a score that does not test whether generated questions elicit the named misconception](collearn-misconception-mining-f1.md) — related
- [At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own](false-alarms-make-standalone-screening-impractical.md) — related
- [Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification](fine-tuned-classifiers-miss-correct-answer-misconceptions.md) — possibly the same claim (merge candidate)
- [Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline](standard-ml-interventions-no-detection-gain.md) — related
- [A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1](reasoning-model-detection-false-alarm-tradeoff.md) — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
