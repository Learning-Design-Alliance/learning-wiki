---
type: element
id: text-embedding-3-small-srl-detection-pipeline
title: Multilingual SRL detection pipeline using OpenAI text-embedding-3-small embeddings with a single-hidden-layer neural network classifier
description: "The pipeline vectorizes English and German think-aloud utterances with OpenAI's text-embedding-3-small, \"a pre- trained sentence embedding model that converts textual input into a high-dimensional vector with a length..."
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

# Multilingual SRL detection pipeline using OpenAI text-embedding-3-small embeddings with a single-hidden-layer neural network classifier

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The pipeline vectorizes English and German think-aloud utterances with OpenAI's text-embedding-3-small, "a pre- trained sentence embedding model that converts textual input into a high-dimensional vector with a length of 1,536". A single-hidden-layer ReLU neural network (28 intermediate units, sigmoid output, Adam optimizer, learning rate 0.01, 30 epochs, batch size 10) performs binary classification of each SRL category, evaluated with student-level 5-fold cross-validation using AUC. All analysis code is released in a public GitHub repository.

## Design Implications

### Context
#### Requirements
- Manually coded presence/absence labels for the four SRL categories in each utterance
- Multilingual embedding coverage of the target languages
#### Constraints
- German audio was hand-transcribed because Whisper's recognition accuracy was unsuitable given poor audio quality

### Target Learners
- university students working with intelligent tutoring systems

### Target Learning Goals
- automated detection of SRL processes from think-aloud verbalizations

### Affordances
- [Winne Hadwin Four Category Tap Coding Scheme](../theories/winne-hadwin-four-category-tap-coding-scheme.md)

## Claims

- [OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German](../claims/embedding-srl-classifiers-satisfactory-within-language-german-english.md) [+W]
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](../claims/llm-srl-classifiers-transfer-across-languages-within-domain.md) [+W]
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](../claims/srl-transfer-degradation-tenth-auc-within-domain.md) [~W]
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](../claims/srl-transfer-errors-subject-specific-terminology.md) [~W]

## Related Elements
- 

## Examples
-

## Key Sources
- Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud
