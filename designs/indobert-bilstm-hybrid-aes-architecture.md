---
type: design
id: indobert-bilstm-hybrid-aes-architecture
title: Hybrid IndoBERT–BiLSTM automated essay scoring architecture with per-dimension classifiers
description: "The IB-BiLSTM architecture \"combines IndoBERT as a contextual encoder with a two -layer Bidirectional LSTM (BiLSTM) as a sequential classifier.\" IndoBERT produces token-level embeddings of shape (batch × 128 × 768) fe..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: firdausi-2026
    resource: "https://doi.org/10.22266/ijies2026.0831.09"
    title: "Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09"
    author: Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R
---

# Hybrid IndoBERT–BiLSTM automated essay scoring architecture with per-dimension classifiers

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The IB-BiLSTM architecture "combines IndoBERT as a contextual encoder with a two -layer Bidirectional LSTM (BiLSTM) as a sequential classifier." IndoBERT produces token-level embeddings of shape (batch × 128 × 768) fed to the BiLSTM, followed by Dense layers (256 and 128 units, ReLU) and a four-unit softmax for score levels 1–4. Six independent classification models were built, one per FRISCO dimension, rather than a single multi-label classifier, and all IndoBERT parameters were trainable for joint fine-tuning.

## Design Implications

### Context
#### Requirements
- Pretrained IndoBERT (indobert-base-p1) with WordPiece tokenization; balanced class-weighted loss; hyperparameter tuning via 5-fold CV on macro-F1
#### Constraints
- Evaluated on a small dataset (83 training / 23 test students); the article reports that accuracy alone is insufficient for ordinal AES evaluation because high-accuracy variants can show majority-class collapse

### Target Learners
- Indonesian high school physics students

### Learning Goals
- Automated multidimensional assessment of critical thinking in physics essays

### Claims
- [Aes Frisco Qwk Varies By Dimension](../claims/aes-frisco-qwk-varies-by-dimension.md) [+M]
- [Svm Outperforms Bilstm Reason Dimension](../claims/svm-outperforms-bilstm-reason-dimension.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09
