---
type: claim
title: Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added
description: Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added
id: pseudo-labeled-data-sgec-model-size-moderates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
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

# Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the large-v2 model, pseudo-labeling converges close to training on labeled data alone after fine-tuning (11.00% vs 11.10% on LNG), indicating limited benefit. [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

Same Section 5.2 evaluation for large-v2: after fine-tuning on manual annotations, pseudo-labeling converges "close to the performance of training on the labeled data alone", with 11.00% vs 11.10% WER on LNG and 13.20% vs 13.21% on S&I.

> "However, after subsequent fine-tuning on the manually annotated LNGlbl set, both pseudo-labeling settings converge close to the performance of training on the labeled data alone (11.00% vs. 11.10% on LNG, and 13.20% vs. 13.21% on S&I)."

## Discussion


## Related Claims
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
- [With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines](e2e-whisper-large-v2-sgec-outperforms-pipelines.md) — related
- [Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech](singakids-asr-finetuning-wer-gains.md) — related
