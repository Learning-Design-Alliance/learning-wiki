---
type: claim
title: "Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification"
description: "Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification"
id: attention-models-beat-vanilla-neural-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: abdul-waheed-2021
    resource: "https://doi.org/10.48550/arXiv.2108.07249"
    title: "Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)"
    author: Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Seq2Seq-Attention and Self-Attention models classified questions better than vanilla models such as VDCNN, CNN, LSTM and RCNN. [→ Abdul Waheed 2021](#abdul-waheed-2021)

## Evidence

### Abdul Waheed 2021

Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)

`q2 · i?` · `design · r2`

Cross-model comparison over the same five-fold cross-validated runs on both datasets. For example, Self-Attention reached 70.17 IID accuracy versus 60.67 for CNN and 58.50 for LSTM, while VDCNN scored lowest at 32.00. No effect size is printed for this contrast.

> "We also observe that Attention based models like Seq2Seq-Attention and Self-Attention show better classiﬁcation performance than vanilla mod- els (like VDCNN, CNN, LSTM, and RCNN)."

## Discussion


## Related Claims
- [TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN](tfidf-random-forest-beats-strong-baselines.md) — related
- [CNN models almost always outperform LSTM models for argument component classification in classroom discussions, with character-level LSTMs near random chance](cnn-outperforms-lstm-argument-component-classification.md) — related
- [Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features](handcrafted-features-improve-neural-argument-classifiers.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes](bloomnet-outperforms-baselines-bloom-classification.md) — related
- [Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone](linguistic-encapsulation-word-attention-improves-classification.md) — related
