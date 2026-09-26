---
type: claim
title: "All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts"
description: "All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts"
id: classifiers-beat-zero-rule-baseline-engagement
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

# All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Decision tree (60%), random forest (66%), and SVM (71%) full-model accuracies all exceeded the 28.4% zero-rule baseline, and Cochran's Q showed significant differences between classifiers. [→ Gorgun 2022](#gorgun-2022)

## Evidence

### Gorgun 2022

Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149

`q2 · i?`

Results section comparison of the three classifiers against the zero-rule baseline on the 30% test split, with Cochran's Q (Q = 55.68, p < .001) comparing classification accuracies across models. All models "outperformed this simple baseline".

> "Note that the accuracy of the zero-rule classifier for the full model would be 28.4%. As can be seen in Table 4, all of the models outperformed this simple baseline. Moreover, Cochran's test revealed statistically significant differences between the classifiers we built, Q = 55.68, p < .001."

## Discussion


## Related Claims
- [Classifiers systematically confuse adjacent engagement levels: social with active, constructive with interactive, and interactive with active](adjacent-engagement-level-misclassification-patterns.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
