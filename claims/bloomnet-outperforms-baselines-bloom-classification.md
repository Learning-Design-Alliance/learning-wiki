---
type: claim
title: "BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes"
description: "BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes"
id: bloomnet-outperforms-baselines-bloom-classification
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

# BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BloomNet achieves higher accuracy and Macro-F1 than all considered baselines, including RoBERTa, on both the IID dataset and the OOD dataset. [→ Abdul Waheed 2021](#abdul-waheed-2021)

## Evidence

### Abdul Waheed 2021

Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)

`q2 · i?` · `design · r2`

Five-fold cross-validated comparison on two Bloom's taxonomy question datasets, with BloomNet trained on Dataset1 and evaluated on both datasets. BloomNet reached "87.50± 1.88" accuracy IID and "70.40± 2.52" OOD, exceeding the best baseline RoBERTa (82.00 and 68.65 accuracy).

> "As seen in Table 2 BloomNet outperforms the baseline models and achieves 87.50± 1.88 and 70.40± 2.52 and Macro-F1 score 87.23± 2.47 and 67.10± 2.43 on Dataset1(IID) and Dataset2(OOD) respectively."

## Discussion


## Related Claims
- [TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN](tfidf-random-forest-beats-strong-baselines.md) — related
- [Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone](linguistic-encapsulation-word-attention-improves-classification.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification](attention-models-beat-vanilla-neural-baselines.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance](pretrained-transformers-twenty-percent-ood-drop.md) — related
