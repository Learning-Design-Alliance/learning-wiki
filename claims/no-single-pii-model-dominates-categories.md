---
type: claim
title: "No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection"
description: "No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection"
id: no-single-pii-model-dominates-categories
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

# No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Category-level results show each model has distinct strengths: Azure AI Language performed best for email detection, Verifier Model II (With CoT) was most effective for phone number detection, and for names and URLs the fine-tuned GPT-4o-mini and Verifier Model I present a recall-precision trade-off. [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Entity-category analysis in Section 4.2 across NAME STUDENT, URL PERSONAL, EMAIL, and PHONE NUM. For example, fine-tuned GPT-4o-mini achieved the highest name recall (0.9605) and F5 (0.9398), while Verifier Model I achieved the highest URL precision (0.9877).

> "Overall, no single model dominates across all tested categories, as each exhibits distinct strengths. Azure AI Language performs best for email detection, while Verifier Model II (With CoT) is more effective for phone number detection."

## Discussion


## Related Claims
- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) — related
- [Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample](fine-tuned-gpt4o-mini-generalizes-tscc.md) — related
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](fine-tuned-gpt4o-mini-highest-recall-crapii.md) — related
- [Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it](low-precision-pii-detection-semantic-disruption.md) — related
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](verifier-models-raise-precision-reduce-recall.md) — related
