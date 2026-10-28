---
type: claim
title: Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.
description: Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.
id: zero-shot-gpt4-effective-on-imbalanced-rare-labels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: spain-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4565500/v1"
    title: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1"
    author: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GPT-4 with zero-shot learning remains effective despite imbalanced training data because its performance on a label does not depend on the label's frequency in the data. [→ Spain 2024](#spain-2024)

## Evidence

### Spain 2024

Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1

`q2 · i?` · `design · r2`

Interpretive analysis of error patterns for rare dialogue act labels. The article states that "GPT-4 with zero-shot learning remains effective despite imbalanced training data because its performance on the label does not depend on the labels frequency in the data". This is the authors' explanation rather than a directly tested result.

> "GPT-4 with zero-shot learning remains effective despite imbalanced training data because its performance on the label does not depend on the labels frequency in the data; rather performance is driven by the ability to semantically map the prompt instruction to the utterance, utilizing various contextual clues."

## Discussion


## Related Claims
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.](gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines.md) — related
