---
type: claim
title: Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts
description: Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts
id: awl-count-word-count-feature-importance-engagement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: gorgun-2022
    resource: "https://doi.org/10.5281/zenodo.6853149"
    title: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149"
    author: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Decision tree and random forest models identified the same top features (word count, AWL count, type-token ratio, Flesch-Kincaid grade level), while the SVM identified a different set led by second language readability. [→ Gorgun 2022](#gorgun-2022)

## Evidence

### Gorgun 2022

Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149

`q2 · i?` · `design · r2`

Feature importance analysis of the random forest classifier using mean decrease in Gini, compared with Gini-based importance from the decision tree. The decision tree's top predictor was AWL count, followed by whether a post is a reply, Flesch-Kincaid grade level, and word count.

> "Similar to the decision tree model, we found that the most important features were the number of words (i.e., DESWC), number of academic word list items (AWLCount), type-token ratio for all words (LDTTRa), and Flesch-Kincaid grade level (RDFKGL)."

## Discussion


## Learner Variables
- [Vocabulary](../learner-variables/vocabulary.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Discipline-general academic vocabulary (AWL use) supports cognitive engagement identification and may aid generalization across courses](awl-academic-vocabulary-supports-engagement-identification.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021 — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related
- [Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model](intensity-ratio-and-upsolving-habit-top-feature-importance.md) — related
- [SHAP analysis of the explainable model identifies production frequency and spelling difficulty as high-impact predictors of KVL difficulty, with spelling difficulty varying strongly by L1](shap-production-frequency-and-spelling-difficulty-importance.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences](sliding-window-controls-document-length-effects.md) — related
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
