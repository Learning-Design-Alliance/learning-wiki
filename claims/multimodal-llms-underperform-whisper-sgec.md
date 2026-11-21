---
type: claim
title: "Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus the 43.10 partial-cascaded baseline"
description: "Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus t..."
id: multimodal-llms-underperform-whisper-sgec
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

# Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus the 43.10 partial-cascaded baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Zero-shot Voxtral achieves an F0.5 feedback score of 23.69, substantially below the partial-cascaded baseline of 43.10. [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

Feedback-metric evaluation of zero-shot Voxtral on S&I Dev (Section 5.1). Voxtral "achieves an F0.5 score of 23.69, substantially below the partial-cascaded baseline (43.10)".

> "We additionally evaluated the zero-shot Voxtral outputs on the S&I Dev set using the feedback metrics adopted in this work. Voxtral achieves an F0.5 score of 23.69, substantially below the partial-cascaded baseline (43.10)."

## Discussion


## Related Claims
- [Fine-tuning Whisper on local Malay and Tamil speech data lowers WER, especially on children's speech](singakids-asr-finetuning-wer-gains.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
