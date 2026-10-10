---
type: claim
title: Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline
description: Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline
id: standard-ml-interventions-no-detection-gain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: moiz-imran-2026-2
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Class-weighted sampling, data augmentation, focal loss, cross-encoder architecture, and NLI reformulation all perform within the baseline confidence interval for detecting correct-answer misconceptions. [→ Moiz Imran 2026](#moiz-imran-2026)
`q2 i?` Integrated gradients analysis indicates misclassified cases show answer-dominant attribution while correctly classified cases show explanation-dominant attribution. [→ Moiz Imran 2026 (2)](#moiz-imran-2026-2)

## Evidence

### Moiz Imran 2026

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `design · r2`

Model-variant experiments on the Eedi test set reported in Results. The paper states the five named interventions "all fall within the baseline confidence interval" of the BERT baseline for TM detection; no effect sizes are printed.

> "Several standard ML interventions (class-weighted sampling, data augmentation, focal loss, cross-encoder architecture, and NLI reformulation) all fall within the baseline confidence interval."

### Moiz Imran 2026 (2)

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `associational · r2`

An interpretability analysis of the fine-tuned classifier reported in Results. It shows "answer-dominant attribution" for misclassified cases versus "explanation-dominant attribution" for correct classifications, supporting the shortcut account.

> "Integrated gradients analysis confirms the mechanism: misclassified cases show answer-dominant attribution, while correctly classified cases show explanation-dominant attribution"

## Discussion


## Related Claims
- [Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification](fine-tuned-classifiers-miss-correct-answer-misconceptions.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
