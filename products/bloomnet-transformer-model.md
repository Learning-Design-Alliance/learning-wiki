---
type: product
id: bloomnet-transformer-model
title: BloomNet transformer model
description: BloomNet is a RoBERTa-, POS-, NER-, and GRU-attention-based classifier developed by Abdul Waheed et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# BloomNet transformer model

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
BloomNet is a RoBERTa-, POS-, NER-, and GRU-attention-based classifier developed by Abdul Waheed et al. for institutions and administrators to assign course learning outcomes and examination questions to Bloom’s taxonomy levels.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **BloomNet transformer model for Bloom's taxonomy learning outcome classification**: BloomNet is a transformer-based classifier for course learning outcomes that fuses four representations: a pretrained RoBERTa encoder, two frozen POS and NER encoders, and a GRU-based hierarchical word attention module, concatenated before a linear softmax classifier. As the article states, "In BloomNet , we encapsulate the linguistic information along with generic input representation and we also explicitly model word level attention." It was trained with 5-fold cross validation, learning rate 2e-5, 50 epochs, batch size 32 and early stopping. (Abdul Waheed et al. (2021))

### Claims
- [BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes](../claims/bloomnet-outperforms-baselines-bloom-classification.md) [+M]
- [Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone](../claims/linguistic-encapsulation-word-attention-improves-classification.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. https://arxiv.org/abs/2108.07249
