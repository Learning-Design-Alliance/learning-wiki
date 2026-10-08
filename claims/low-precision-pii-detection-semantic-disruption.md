---
type: claim
title: "Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it"
description: "Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it"
id: low-precision-pii-detection-semantic-disruption
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

# Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In three worked examples, Presidio and Azure AI Language incorrectly flagged non-PII entities (e.g., historical and famous names, sentence boundaries read as URLs) as PII, producing replacements that altered the data's intended meaning, while all GPT-based models correctly identified these cases as non-PII. [→ Zilyu Ji 2025](#zilyu-ji-2025)

## Evidence

### Zilyu Ji 2025

Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

`q2 · i?` · `design · r2`

Qualitative example analysis in Section 4.3 of false positives from Presidio and Azure AI Language, including replacement of "Jesus Christ, Mary, Joseph, and Jesus" and of famous entrepreneurs, and mislabeling of sentence boundaries as URLs; GPT-based models preserved these as true negatives.

> "These examples demonstrate cases where Presidio and Azure AI Language incorrectly identify non-PII entities as PII (false positives), resulting in unnecessary replacements that alter the intended meaning of the data."

## Discussion


## Related Claims
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](no-single-pii-model-dominates-categories.md) — related
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](verifier-models-raise-precision-reduce-recall.md) — related
- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — reports the opposite
