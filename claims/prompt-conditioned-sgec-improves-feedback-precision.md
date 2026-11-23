---
type: claim
title: "Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model"
description: "Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model"
id: prompt-conditioned-sgec-improves-feedback-precision
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

# Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prompting with fluent transcriptions outperforms the non-prompted end-to-end model on all feedback metrics, with Precision rising by 3.54 on LNG and 3.69 on S&I, and both E2E models significantly beat the partial-cascaded system (p < 0.001). [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

Feedback evaluation of prompted versus non-prompted large-v2 E2E models on LNG test and S&I Dev (Table 5, Section 5.3). Prompting raises "Precision, rising by 3.54 on LNG and 3.69 on S&I"; WER gains are modest (11.08% vs 11.10% on LNG).

> "Whispergec+pt outperforms Whispergec across all metrics, with a particularly notable increase in Precision, rising by 3.54 on LNG and 3.69 on S&I. F0.5 scores also increase, indicating that prompting with fluent transcriptions enables the model to better identify and express corrections aligned with learner errors."

## Discussion


## Related Claims
- [With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines](e2e-whisper-large-v2-sgec-outperforms-pipelines.md) — related
- [Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline](edit-confidence-filtering-improves-feedback-f05.md) — related
- [Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality](reference-alignment-boosts-sgec-feedback-f05.md) — related
- [Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added](pseudo-labeled-data-sgec-model-size-moderates.md) — related
- [Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus the 43.10 partial-cascaded baseline](multimodal-llms-underperform-whisper-sgec.md) — related
- [The baseline SGECF system detects and labels learner error types at an overall ERRANT F0.5 of 0.22, with preposition replacement errors best detected](s-i-2025-baseline-sgecf-f05-0-22.md) — related
