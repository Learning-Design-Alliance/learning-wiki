---
type: claim
title: TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN
description: TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN
id: tfidf-random-forest-beats-strong-baselines
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

# TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A simple TF-IDF random forest was the third best performing model, beating LSTM, HAN, CNN and RCNN on both datasets. [→ Abdul Waheed 2021](#abdul-waheed-2021)

## Evidence

### Abdul Waheed 2021

Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)

`q2 · i?` · `design · r2`

Comparative evaluation of baselines on the two question datasets with five-fold cross validation. The TF-IDF random forest scored "70.66± 2.52" IID accuracy, above attention and neural baselines such as Self-Attention (70.17), though below DistilRoBERTa and RoBERTa.

> "It is the third best performing baseline model that achieves 70.66± 2.52 and 62.12± 1.38 accuracy and Macro-F1 70.50± 2.75 and 58.04± 1.73 on Dataset1(IID) and Dataset2(OOD) respectively."

## Discussion


## Related Claims
- [Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification](attention-models-beat-vanilla-neural-baselines.md) — related
- [BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes](bloomnet-outperforms-baselines-bloom-classification.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set](decision-tree-explanation-quality-f1-80.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [A Random Forest regressor with question_only text encoding performed best for estimating both IRT latent traits in cross-validated model choice](r2de-random-forest-question-only-best.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
