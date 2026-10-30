---
type: claim
title: Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.
description: Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.
id: iterative-prompt-engineering-improves-gpt-dialogue-act-accuracy
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
    rigour: 3
---

# Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding training context and Command label clarification raised GPT-3.5 accuracy from 0.369 (coding sheet alone) to 0.600, and adding inter-class clarification further raised it to 0.631. [→ Spain 2024](#spain-2024)

## Evidence

### Spain 2024

Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1

`q2 · i?` · `design · r3`

Iterative prompt refinement on the training dataset across four stages. The article reports the initial coding-sheet prompt "yielded an accuracy of 0.369" and that adding few-shot examples "led to an improved system accuracy of approximately 0.425". Table 5 further shows 0.600 with Command clarification plus training context and 0.631 with inter-class clarification.

> "This initial setup yielded an accuracy of 0.369. To improve on these results, we integrated examples from the training set into the prompt—specically, four examples per class with their corresponding labels (i.e., few-shot learning), as shown in Stage 2 in Table 4. This modication led to an improved system accuracy of approximately 0.425."

## Discussion


## Related Claims
- [Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.](gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines.md) — related
- [Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).](prompt-refinements-improve-recall-challenging-dialogue-acts.md) — related
