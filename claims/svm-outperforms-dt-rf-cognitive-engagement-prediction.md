---
type: claim
title: A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts
description: A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts
id: svm-outperforms-dt-rf-cognitive-engagement-prediction
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: gorgun-2022
    resource: "https://doi.org/10.5281/zenodo.6853149"
    title: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149"
    author: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C."
    q: 2
    i: "?"
---

# A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` The SVM classifier achieved 71% accuracy (K = .61) on the full prediction task and significantly outperformed both the decision tree and random forest classifiers. [→ Gorgun 2022](#gorgun-2022)

## Evidence

### Gorgun 2022

Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149

`q2 · i?`

Test-set evaluation of three classifiers trained on 104 Coh-Metrix indicators plus three contextual features, using 10-fold cross-validation with accuracy, precision, recall, F1, and Cohen's Kappa. The SVM reached "substantial agreement between the predicted and human-assigned labels" with K = .61.

> "The support vector machine classifier outperformed both the decision tree (McNemar'sχ2 = 61.31, p< .001) and the random forest (McNemar'sχ2 = 19.04, p< .001) models on the full prediction task. The SVM model's Kappa value (.61) suggested substantial agreement between the predicted and human-assigned labels"

## Discussion


## Related Claims

- [Classifiers systematically confuse adjacent engagement levels: social with active, constructive with interactive, and interactive with active](adjacent-engagement-level-misclassification-patterns.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Discipline-general academic vocabulary (AWL use) supports cognitive engagement identification and may aid generalization across courses](awl-academic-vocabulary-supports-engagement-identification.md)
