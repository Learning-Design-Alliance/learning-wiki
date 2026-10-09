---
type: claim
title: Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample
description: Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample
id: fine-tuned-gpt4o-mini-generalizes-tscc
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

# Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When tested on the TSCC dataset after fine-tuning on a small sample from that domain, the model achieved high accuracy (Precision 0.9708, Recall 0.9895, F1 0.9801), indicating adaptability across educational contexts. [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Generalizability evaluation on the Teacher-Student Chatroom Corpus (260 chatroom sessions, 41.4K conversational turns), whose name placeholders were replaced with synthetic names sampled by gender-culture group to enable a realistic cross-domain test.

> "The model proves to be adaptable, achieving high accuracy (Precision of 0.9708, Recall of 0.9895, and F1 Score of 0.9801) on the new domain after fine-tuning on a small sample, confirming its suitability for deployment across varied educational contexts."

## Discussion


## Related Claims
- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) — related
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](fine-tuned-gpt4o-mini-highest-recall-crapii.md) — related
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](verifier-models-raise-precision-reduce-recall.md) — related
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](no-single-pii-model-dominates-categories.md) — related
- [AI tools collected and organized a previously unavailable granularity of data, including individual student exchanges and classroom discussion data, to generate actionable recommendations](ai-granular-data-collection-actionable-recommendations.md) — related
