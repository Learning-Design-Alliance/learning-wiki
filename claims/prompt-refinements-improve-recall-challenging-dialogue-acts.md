---
type: claim
title: Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).
description: Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs.
id: prompt-refinements-improve-recall-challenging-dialogue-acts
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

# Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Adding Command label clarification and training context raised the Command label's F1 score to 0.75 for GPT-3.5, and GPT-4 achieved higher recall than T5 on the Other label (0.67 vs. 0.54) and Action-Statement label (0.73 vs. 0.46). [→ Spain 2024](#spain-2024)

## Evidence

### Spain 2024

Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1

`q2 · i?` · `design · r2`

Error analysis of the highest-performing models using confusion matrices. The article reports that adding Command clarification and context "raised the Command labels F1 score to 0.75 for GPT-3.5", and separately notes GPT-4's recall of 0.67 on Other vs. T5's 0.54, and 0.73 vs. 0.46 on Action-Statement.

> "This clarication, along with the new Context section detailing the training scenario and team roles, and including the speaker's role in the utterances, notably enhanced the accuracy to 0.6 and raised the Command labels F1 score to 0.75 for GPT-3.5."

## Discussion


## Related Claims
- [GPT-4 outperforms fine-tuned T5 by a normalized accuracy improvement of 5.73% for dialogue act recognition on the same held-out test set.](gpt4-normalized-accuracy-improvement-5-73-percent-over-t5.md) — related
- [Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.](iterative-prompt-engineering-improves-gpt-dialogue-act-accuracy.md) — related
- [Provide-Info, Request-Info, and Other are the dialogue act labels most commonly confused by both GPT-4 and T5 classifiers.](provide-info-request-info-other-most-confused-labels.md) — related
- [Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.](gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines.md) — a broader claim this one bears on
