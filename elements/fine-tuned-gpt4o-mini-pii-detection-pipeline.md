---
type: element
id: fine-tuned-gpt4o-mini-pii-detection-pipeline
title: Fine-tuned GPT-4o-mini PII detection pipeline with special-identifier labeling and verifier models (code released on GitHub)
description: "A PII detection pipeline for educational text in which GPT-4o-mini is either prompted with few-shot examples or fine-tuned to surround detected entities with category-specific special identifiers (e.g., @@@Text### for..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: zilyu-ji-2025
    resource: "https://github.com/AnonJD/PrivacyAI"
    title: "Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI"
    author: Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin
---

# Fine-tuned GPT-4o-mini PII detection pipeline with special-identifier labeling and verifier models (code released on GitHub)

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A PII detection pipeline for educational text in which GPT-4o-mini is either prompted with few-shot examples or fine-tuned to surround detected entities with category-specific special identifiers (e.g., @@@Text### for student names), which are then extracted via regular expressions to ensure accurate positioning. Optional fine-tuned verifier models (with or without chain-of-thought) re-check detected entities in context to remove false positives. The article reports that "Our code is available on GitHub: https://github.com/AnonJD/PrivacyAI".

## Design Implications

### Context
#### Requirements
- Requires labeled PII training data (the CRAPII dataset with seven direct-identifier categories) and, for verifiers, a dedicated Verifier Train Set of (entity, context) pairs labeled true or false PII.
#### Constraints
- Applying a verifier will not increase recall, as false negatives remain unchanged; the verifier reduces false positives, potentially at the expense of some true positives.
- No further hyperparameter tuning was performed due to OpenAI platform constraints (epochs = 2, batch size = 1, learning rate multiplier = 1.8).

### Target Learners
- Educational data mining researchers and learning-technology practitioners anonymizing student and teacher interaction data

### Target Learning Goals
- Protecting student and teacher privacy (PII removal) while preserving the utility of educational data for research and pedagogical analysis

## Claims

- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](../claims/fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) [+W]
- [Fine-tuned GPT-4o-mini generalizes to the TSCC chatroom domain, achieving precision 0.9708, recall 0.9895, and F1 0.9801 after fine-tuning on a small sample](../claims/fine-tuned-gpt4o-mini-generalizes-tscc.md) [+W]
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](../claims/fine-tuned-gpt4o-mini-highest-recall-crapii.md) [+W]
- [Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it](../claims/low-precision-pii-detection-semantic-disruption.md) [+W]
- [No single PII detection model dominates across entity categories: Azure AI Language performs best for email detection and Verifier Model II (With CoT) for phone number detection](../claims/no-single-pii-model-dominates-categories.md) [+W]
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](../claims/verifier-models-raise-precision-reduce-recall.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI
