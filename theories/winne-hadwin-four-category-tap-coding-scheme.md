---
type: theory
title: "Four-category operationalization of Winne and Hadwin's four-stage SRL model for tutored problem-solving verbalizations"
description: "The study operationalizes SRL in think-aloud transcripts as four categories grounded in Winne and Hadwin's four-stage model: \"processing information, planning, enacting, and realizing errors\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: conrad-borchers-2025
    resource: "https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    title: "Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    author: Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker
---

# Four-category operationalization of Winne and Hadwin's four-stage SRL model for tutored problem-solving verbalizations

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The study operationalizes SRL in think-aloud transcripts as four categories grounded in Winne and Hadwin's four-stage model: "processing information, planning, enacting, and realizing errors". Concatenated utterances between consecutive tutor transactions were annotated with a coding scheme (Table 1) specifying behaviors per category, such as assembling information, forming plans, verbalizing actions, and realizing mistakes. This subset of stage-relevant behaviors enables relating verbalized SRL to tutor action correctness.

## Design Implications

### Context
#### Requirements
- Think-aloud utterances segmented and synchronized with timestamped tutor transactions (no more than a 1-second error margin)
- Trained human coders establishing inter-rater reliability before coding the full sample
#### Constraints
- Categories represent a subset of SRL processes within each model stage, focusing on problem-solving learning environments

### Target Learners
- university students in chemistry and formal logic courses

### Target Learning Objectives
- self-regulated learning during tutored problem-solving

### Claims

- [Embedding Srl Classifiers Satisfactory Within Language German English](../claims/embedding-srl-classifiers-satisfactory-within-language-german-english.md) [+M]
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](../claims/llm-srl-classifiers-transfer-across-languages-within-domain.md) [+W]
- [Process and enact SRL categories transfer slightly better from German to English than English to German](../claims/srl-transfer-asymmetric-german-english-process-enact.md) [+W]
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](../claims/srl-transfer-degradation-tenth-auc-within-domain.md) [+W]
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](../claims/srl-transfer-errors-subject-specific-terminology.md) [+W]

## Related Theories
- 

## Examples

- [Multilingual SRL detection pipeline using OpenAI text-embedding-3-small embeddings with a single-hidden-layer neural network classifier](../research-methods/multilingual-embedding-based-automated-classification-of-self-regulated-learning-think-alo.md)

## Key Sources
- Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud
