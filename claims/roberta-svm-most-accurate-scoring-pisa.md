---
type: claim
title: SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations
description: SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations
id: roberta-svm-most-accurate-scoring-pisa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: nico-andersen-2025
    resource: "https://doi.org/10.1007/s40593-025-00495-5"
    title: "Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5"
    author: Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across four feature–classifier combinations, SVM trained on RoBERTa sentence embeddings achieved the highest agreement with human scoring (κ = .82) and a better average false positive rate than its closest competitors. [→ Nico Andersen 2025](#nico-andersen-2025)

## Evidence

### Nico Andersen 2025

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `design · r2`

Numerical comparison of four trained scoring models (unigram decision tree, unigram random forest, word2vec SVM, RoBERTa SVM) evaluated with five-fold cross-validation on all responses across 37 PISA items. The RoBERTa-SVM reached "κ = .82"; the unigram decision tree was lowest at κ = .28.

> "The best fit was achieved using SVM with RoBERTa sentence embeddings (κ = .82), tying for the highest average true positive rate alongside unigrams with random forest and word2vec with SVM, but offering a better average false positive rate compared to its closest competitors, except for the unigram with decision tree combination."

## Discussion


## Related Claims
- [The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers](language-bias-favors-foreign-speakers-roberta-svm.md) — related
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](random-forest-slightly-better-for-answer-classification.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%](eeg-stage-classification-over-80.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
