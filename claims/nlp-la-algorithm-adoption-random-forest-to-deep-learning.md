---
type: claim
title: Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021
description: Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021
id: nlp-la-algorithm-adoption-random-forest-to-deep-learning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: rafael-ferreira-mello-2024
    resource: "https://doi.org/10.18608/jla.2024.8403"
    title: "Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403"
    author: Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević
    q: 3
    i: "?"
    kind: review
    rigour: 2
  - id: rafael-ferreira-mello-2024-2
    resource: "https://doi.org/10.18608/jla.2024.8403"
    title: "Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403"
    author: Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević
    q: 3
    i: "?"
    kind: review
    rigour: 3
---

# Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2`–`r3` · `q3`

## Subclaims
`q3 i?` The Random Forest classifier was the most commonly used algorithm (N = 30), with Logistic Regression and SVM second (N = 16). [→ Rafael Ferreira Mello 2024](#rafael-ferreira-mello-2024)
`q3 i?` Since 2021, LSTM and BERT have been widely used, and word embeddings (particularly BERT) became the predominant feature approach, used in 28 studies in 2021–2023. [→ Rafael Ferreira Mello 2024 (2)](#rafael-ferreira-mello-2024-2)

## Evidence

### Rafael Ferreira Mello 2024

Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403

`q3 · i?` · `review · r2`

Algorithm-frequency analysis over the 156 papers (Figure 6, RQ6). The review reports Random Forest most common with Logistic Regression and SVM second, and notes the authors "widely adopted the white-box models" for more straightforward interpretability of prediction results.

> "Regarding specific machine learning algorithms, the Random Forest classifier was the most commonly used (N = 30), whereas Logistic Regression and SVM were second in this list (N = 16)."

### Rafael Ferreira Mello 2024 (2)

Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403

`q3 · i?` · `review · r3`

Feature-adoption analysis over time (Figure 7, RQ6): in 2021–2023 word embeddings, particularly BERT, were the predominant feature approach in 28 studies, more than TF-IDF and structural features combined in the same period. TF-IDF (N = 40) remained the most used feature overall.

> "However, it is crucial to emphasize that, over the past three years (2021–2023), word embeddings, particularly BERT (Del Gobbo et al., 2023; Dood et al., 2022; Liu et al., 2023), have been the predominant approach, used in 28 studies."

## Discussion


## Related Claims
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees](lstm-early-qlg-prediction-70-percent.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [Collaborative learning is the most prominent educational task addressed with NLP in learning analytics research, followed by assessment and feedback](nlp-la-collaborative-learning-most-prominent-task.md) — related
- [NLP-for-LA research is heavily biased toward English-language texts and small datasets, with almost no open datasets](nlp-la-english-small-dataset-bias.md) — related
- [Most NLP-for-LA studies (89.10%) never apply their models in real educational settings, revealing a gap between model development and practical use](nlp-la-gap-model-development-practical-use.md) — related
- [Online discussions are the predominant textual product analyzed with NLP in learning analytics, followed by essays](nlp-la-online-discussions-predominant-textual-resource.md) — related
