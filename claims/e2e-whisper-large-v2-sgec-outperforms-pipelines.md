---
type: claim
title: "With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines"
description: "With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines"
id: e2e-whisper-large-v2-sgec-outperforms-pipelines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: mengjie-qian-2026
    resource: "https://doi.org/10.2139/ssrn.6588326"
    title: "Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)"
    author: Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The large-v2 end-to-end SGEC model surpasses both the cascaded and partial-cascaded baselines in transcription accuracy, achieving a 6.9% relative WER reduction on LNG and 5.6% on S&I versus the partial-cascaded system. [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

WER comparison of cascaded, partial-cascaded and end-to-end Whisper-based SGEC systems on the Linguaskill test set and S&I Dev set (Table 2). The article reports the large-v2 E2E model achieving "a 6.9% relative WER reduction on LNG and 5.6% on S&I compared to the partial-cascaded system".

> "Notably, the E2E model withlarge-v2 surpasses both baselines by a substantial margin, achieving a 6.9% relative WER reduction on LNG and 5.6% on S&I compared to the partial-cascaded system, and 8.3% and on LNG and 8.8% on S&I over the cascaded system."

## Discussion


## Related Claims
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
- [Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added](pseudo-labeled-data-sgec-model-size-moderates.md) — related
- [Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech](singakids-asr-finetuning-wer-gains.md) — related
- [The baseline Whisper-small ASR system transcribes L2 learner speech at a 10.4% WER on the S&I Dev set](s-i-2025-baseline-asr-wer-10-4.md) — related
