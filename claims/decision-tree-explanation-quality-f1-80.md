---
type: claim
title: "A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set"
description: "A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set"
id: decision-tree-explanation-quality-f1-80
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: kochmar-2022
    resource: "https://doi.org/10.1007/s40593-021-00267-x"
    title: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x"
    author: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Among several classifiers tested on NLP features of Wikipedia explanations, the Decision Tree performed best at binary classification of explanation quality. [→ Kochmar 2022](#kochmar-2022)

## Evidence

### Kochmar 2022

Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x

`q1 · i?` · `design · r2`

Machine-learning classification experiment on a 2GB in-domain Wikipedia-crawled dataset re-sampled with SMOTE; data split 60% training, 10% validation, 30% test. Features included length-based measures, co-reference resolution score, LSTM language model score, entailment relations, TF-IDF, and named entity classes.

> "Among those, the Decision Tree classifier performed best, yielding an F1 score of 80.32% in distinguishing between high and low-quality explanations on the validation set."

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Students rate pairs of extracted and generated Wikipedia-based explanations as helpful 83.33% of the time, more than either type alone](wikipedia-explanations-both-types-preferred.md) — related
