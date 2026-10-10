---
type: claim
title: "Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification"
description: "Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification"
id: fine-tuned-classifiers-miss-correct-answer-misconceptions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A BERT-base classifier fine-tuned on Eedi responses detects only 57.4% of true-misconception (correct answer, flawed reasoning) cases while achieving 100% recall on wrong-answer cases. [→ Moiz Imran 2026](#moiz-imran-2026)

## Evidence

### Moiz Imran 2026

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `design · r2`

Evaluation of a fine-tuned BERT-base classifier on a held-out test set of 3,702 Eedi responses containing 61 TM cases. The paper reports "57% of correct-answer misconceptions" detected with "FM recall 100%"; Table 1 prints TM detection 57.4 [44.5, 69.4].

> "BERT detects only 57% of correct-answer misconceptions despite near-perfect wrong-answer classification (FM recall 100%)."

## Discussion


## Related Claims
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — possibly the same claim (merge candidate)
- [Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline](standard-ml-interventions-no-detection-gain.md) — related
- [A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1](reasoning-model-detection-false-alarm-tradeoff.md) — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
