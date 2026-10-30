---
type: claim
title: "Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set."
description: "Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set."
id: gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 with zero-shot learning and inter-class clarification prompts achieved 77.30% dialogue act recognition accuracy on the held-out test set, surpassing T5 (75.92%), CRF (69.42%), and BLSTM (64.61%). [→ Spain 2024](#spain-2024)

## Evidence

### Spain 2024

Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1

`q2 · i?` · `design · r2`

Evaluation of the team communication analysis framework on a held-out test set from a U.S. Army squad training exercise. The article reports that "GPT-4, augmented with inter-class clarication based on zero-shot learning, achieved the highest dialogue act recognition accuracy at 77.30%". Table 7 lists test accuracy rates of 75.92% for T5, 69.42% for CRF, and 64.61% for BLSTM.

> "GPT-4, augmented with inter-class clarication based on zero-shot learning, achieved the highest dialogue act recognition accuracy at 77.30%, surpassing three competitive baselines."

## Discussion


## Related Claims
- [GPT-4 outperforms fine-tuned T5 by a normalized accuracy improvement of 5.73% for dialogue act recognition on the same held-out test set.](gpt4-normalized-accuracy-improvement-5-73-percent-over-t5.md) — possibly the same claim (merge candidate)
- [Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.](iterative-prompt-engineering-improves-gpt-dialogue-act-accuracy.md) — related
- [Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).](prompt-refinements-improve-recall-challenging-dialogue-acts.md) — a narrower finding that bears on this claim
- [Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.](zero-shot-gpt4-effective-on-imbalanced-rare-labels.md) — related
