---
type: claim
title: Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset
description: Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset
id: fine-tuned-gpt4o-mini-highest-recall-crapii
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: zilyu-ji-2025
    resource: "https://github.com/AnonJD/PrivacyAI"
    title: "Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI"
    author: Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the CRAPII test set, the fine-tuned GPT-4o-mini model achieved the highest overall recall of all seven tested models (0.9589) with precision of 0.6042 and the highest F5 score (0.9377). [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Benchmark evaluation of seven PII detection models on the CRAPII test set (13,613 files, 2,889 true entities), reported in Table 7 and Section 4.1.4. The fine-tuned model's "highest recall among all models at 0.9589" exceeded Azure AI Language (0.9212); its precision of 0.6042 and F5 of 0.9377 were also reported.

> "The fine-tuned GPT-4o-mini model demonstrates strong overall performance, achieving the highest recall among all models at 0.9589. This high recall ensures that nearly all PII entities are identified"

## Discussion


## Related Claims
- [Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample](fine-tuned-gpt4o-mini-generalizes-tscc.md) — related
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](verifier-models-raise-precision-reduce-recall.md) — related
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](no-single-pii-model-dominates-categories.md) — related
