---
type: strategy
id: nlp-la-baseline-recipe-strategy
title: "Baseline recipe for NLP studies in learning analytics: datasets of at least 1,000 instances, Random Forest with interpretable feature sets, and BERT/LSTM evaluation"
description: The review distills its technical synthesis into a recommended baseline configuration for future NLP work in learning analytics.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: rafael-ferreira-mello-2024
    resource: "https://doi.org/10.18608/jla.2024.8403"
    title: "Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403"
    author: Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević
---

# Baseline recipe for NLP studies in learning analytics: datasets of at least 1,000 instances, Random Forest with interpretable feature sets, and BERT/LSTM evaluation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 against) · 5 studies (3 design, 1 review, 1 associational), `q2` · 0 of 5 report an effect size · 6 claims rest on one study

## Description
The review distills its technical synthesis into a recommended baseline configuration for future NLP work in learning analytics. It advises "using a dataset comprising a minimum of 1,000 instances", "combining the Random Forest algorithm with TF-IDF, Structural Features, LIWC, and Coh-Metrix as baseline models", and "evaluating word embeddings through BERT and LSTM classifiers". This gives researchers a comparable starting point grounded in what the field actually reports.

## Design Implications

### Context
#### Requirements
- Datasets should comprise a minimum of 1,000 instances per the review's summary recommendation
#### Constraints
- The review states its performance results are not intended to serve as a definitive benchmark but rather as an indication derived from this SLR

### Target Learners
- learning analytics researchers and practitioners analyzing student textual data

### Target Learning Goals
- building and evaluating NLP models for educational text analysis

## Claims

- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](../claims/mmla-k8-random-forest-best-performance.md) [+M]
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](../claims/rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) [+M]
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](../claims/random-forest-best-auc-flagged-problems.md) [+W]
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](../claims/svm-outperforms-dt-rf-cognitive-engagement-prediction.md) [-W]
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](../claims/lstm-strategy-temporal-analytics-outperforms-baselines.md) [+W]
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](../claims/awl-count-word-count-feature-importance-engagement.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403
