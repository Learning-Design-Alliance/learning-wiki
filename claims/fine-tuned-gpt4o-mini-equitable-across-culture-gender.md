---
type: claim
title: Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models
description: Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models
id: fine-tuned-gpt4o-mini-equitable-across-culture-gender
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
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

# Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In name-based subgroup analysis on the TSCC dataset, the fine-tuned GPT-4o-mini model delivered equitable performance across cultural and gender groups, reducing the cultural biases observed in established baseline models. [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Cultural and gender bias analysis using name-based subgroup analysis in the TSCC dataset, where names were replaced according to cultural and gender distributions; fairness was evaluated via Equality of Opportunity (true positive rates per subgroup). Detailed subgroup results lie beyond the provided text.

> "Our results reveal that the fine-tuned GPT-4o-mini delivers equitable performance, reducing the cultural biases present in established baseline models."

## Discussion


## Related Claims
- [Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample](fine-tuned-gpt4o-mini-generalizes-tscc.md) — related
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](no-single-pii-model-dominates-categories.md) — related
- [Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it](low-precision-pii-detection-semantic-disruption.md) — related
