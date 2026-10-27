---
type: research-method
id: multi-label-bert-classification-of-cognitive-presence-in-mooc-discussion-messages
title: Multi-label BERT classification of cognitive presence in MOOC discussion messages
description: "The article builds a multi-label classifier by revising \"the standard BERT model from a class-independent model to five binary BERT classifiers for each category\", one per cognitive presence category."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Multi-label BERT classification of cognitive presence in MOOC discussion messages

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article builds a multi-label classifier by revising "the standard BERT model from a class-independent model to five binary BERT classifiers for each category", one per cognitive presence category. Messages are pre-processed (emojis and URLs replaced, abbreviations expanded, stop words removed), tokenised with BertTokenizer, and passed through a bert-base-uncased model with 12 transformer layers and 768 dimensions, followed by a linear classification layer and a sigmoid function outputting five probability scores between 0 and 1. Because the sigmoid layer "can allow more than one phase to reach a score of over 0.5", multiple labels may attach to one message; predictions above a 0.33 threshold, chosen because a human coder's weight over three coders' decisions was equivalent to around 0.33, become labels. Training used tenfold cross-validation with data augmentation and over-sampling performed after the dataset splits, Binary Cross-Entropy loss, batch size 8, 10 epochs, and a learning rate of 2 × 10−5.

## Accounts
<!-- How each source describes or uses the method -->
- **Multi-label, fine-tuned BERT classifier architecture of five binary BERT classifiers with sigmoid outputs**: The article builds a multi-label classifier by revising "the standard BERT model from a class-independent model to five binary BERT classifiers for each category", one per cognitive presence category. Messages are pre-processed (emojis and URLs replaced, abbreviations expanded, stop words removed), tokenised with BertTokenizer, and passed through a bert-base-uncased model with 12 transformer layers and 768 dimensions, followed by a linear classification layer and a sigmoid function outputting five probability scores between 0 and 1. Because the sigmoid layer "can allow more than one phase to reach a score of over 0.5", multiple labels may attach to one message; predictions above a 0.33 threshold, chosen because a human coder's weight over three coders' decisions was equivalent to around 0.33, become labels. Training used tenfold cross-validation with data augmentation and over-sampling performed after the dataset splits, Binary Cross-Entropy loss, batch size 8, 10 epochs, and a learning rate of 2 × 10−5. (Yuanyuan Hu (2023))

### Claims
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](../claims/multi-label-bert-f1-beats-rf-exact-match-lower.md) [+M]
- [Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages](../claims/multi-label-predictions-adjacent-phases-only.md) [+M]

## Related Research Methods
-

## Key Sources
- Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-6
