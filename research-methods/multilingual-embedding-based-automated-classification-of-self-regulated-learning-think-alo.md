---
type: research-method
id: multilingual-embedding-based-automated-classification-of-self-regulated-learning-think-alo
moved_from: [element/text-embedding-3-small-srl-detection-pipeline]
title: Multilingual embedding-based automated classification of self-regulated-learning think-aloud utterances
description: "The pipeline vectorizes English and German think-aloud utterances with OpenAI's text-embedding-3-small, \"a pre- trained sentence embedding model that converts textual input into a high-dimensional vector with a length of 1,536\"."
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: conrad-borchers-2025
    resource: "https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    title: "Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    author: Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker
---

# Multilingual embedding-based automated classification of self-regulated-learning think-aloud utterances

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The pipeline vectorizes English and German think-aloud utterances with OpenAI's text-embedding-3-small, "a pre- trained sentence embedding model that converts textual input into a high-dimensional vector with a length of 1,536". A single-hidden-layer ReLU neural network (28 intermediate units, sigmoid output, Adam optimizer, learning rate 0.01, 30 epochs, batch size 10) performs binary classification of each SRL category, evaluated with student-level 5-fold cross-validation using AUC. All analysis code is released in a public GitHub repository.

## Accounts
<!-- How each source describes or uses the method -->
- **Multilingual SRL detection pipeline using OpenAI text-embedding-3-small embeddings with a single-hidden-layer neural network classifier**: The pipeline vectorizes English and German think-aloud utterances with OpenAI's text-embedding-3-small, "a pre- trained sentence embedding model that converts textual input into a high-dimensional vector with a length of 1,536". A single-hidden-layer ReLU neural network (28 intermediate units, sigmoid output, Adam optimizer, learning rate 0.01, 30 epochs, batch size 10) performs binary classification of each SRL category, evaluated with student-level 5-fold cross-validation using AUC. All analysis code is released in a public GitHub repository. (Conrad Borchers et al. (2025))

### Claims

- [Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat](../claims/classifier-error-patterns-and-abstention-f1.md) [+W]

## Related Research Methods

- [Transformer attention-based semantic representation for automated constructed response scoring](transformer-attention-based-semantic-representation-for-automated-constructed-response-sco.md)

## Key Sources
- Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

<!-- merged 2026-10-10 from elements/text-embedding-3-small-srl-detection-pipeline ("Multilingual SRL detection pipeline using OpenAI text-embedding-3-small embeddings with a single-hidden-layer neural network classifier"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Elements
- 

## Examples
-

## Key Sources
- Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud
-->
