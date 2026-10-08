---
type: claim
title: Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini
description: Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini
id: verifier-models-raise-precision-reduce-recall
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

# Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both verifier variants (with and without chain-of-thought) achieved precision surpassing all five other models (0.8893 and 0.7600 overall), while their recall (0.8023 and 0.8648) was lower than the fine-tuned GPT-4o-mini model's. [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Benchmark evaluation in Section 4.1.5 and Table 7: Verifier Model I (Without CoT) reached the highest overall precision (0.8893) with recall 0.8023; Verifier Model II (With CoT) reached precision 0.7600 with recall 0.8648, described as "a more balanced trade-off".

> "Notably, the precision scores for both verifier models surpass that of all other five methods, aligning with our effort to improve precision. However, their recall is lower than that of the Fine-tuned GPT-4o-mini model"

## Discussion


## Related Claims
- [Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample](fine-tuned-gpt4o-mini-generalizes-tscc.md) — related
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](fine-tuned-gpt4o-mini-highest-recall-crapii.md) — related
- [Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it](low-precision-pii-detection-semantic-disruption.md) — related
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](no-single-pii-model-dominates-categories.md) — related
