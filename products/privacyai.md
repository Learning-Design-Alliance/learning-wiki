---
type: product
id: privacyai
title: PrivacyAI
description: PrivacyAI is an open-source GPT-4o-mini-based pipeline released by the authors for detecting, labeling, extracting, and verifying personally identifiable information in educational text.
product_kind: software
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: zilyu-ji-2025
    resource: "https://github.com/AnonJD/PrivacyAI"
    title: "Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI"
    author: Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin
---

# PrivacyAI

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
PrivacyAI is an open-source GPT-4o-mini-based pipeline released by the authors for detecting, labeling, extracting, and verifying personally identifiable information in educational text.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Fine-tuned GPT-4o-mini PII detection pipeline with special-identifier labeling and verifier models (code released on GitHub)**: A PII detection pipeline for educational text in which GPT-4o-mini is either prompted with few-shot examples or fine-tuned to surround detected entities with category-specific special identifiers (e.g., @@@Text### for student names), which are then extracted via regular expressions to ensure accurate positioning. Optional fine-tuned verifier models (with or without chain-of-thought) re-check detected entities in context to remove false positives. The article reports that "Our code is available on GitHub: https://github.com/AnonJD/PrivacyAI". (Zilyu Ji et al. (2025))

### Claims

- [Ablations show removing the strategy selector substantially increases leakage and replacing the NLI verifier with same-model self-check reduces performance](../claims/eduguard-ablation-component-removal.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI

<!-- merged 2026-10-10 from elements/fine-tuned-gpt4o-mini-pii-detection-pipeline ("Fine-tuned GPT-4o-mini PII detection pipeline with special-identifier labeling and verifier models (code released on GitHub)"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Elements
- 

## Examples
-

## Key Sources
- Zilyu Ji, Yuntian Shen, Kenneth R. Koedinger, Jionghao Lin. (2025). Enhancing the De-identification of Personally Identifiable Information in Educational Data. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/AnonJD/PrivacyAI
-->
