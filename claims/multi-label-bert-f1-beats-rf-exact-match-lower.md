---
type: claim
title: Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification
description: Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification
id: multi-label-bert-f1-beats-rf-exact-match-lower
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: yuanyuan-hu-2023
    resource: "https://doi.org/10.1007/s40593-022-00310-5"
    title: "Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5"
    author: Yuanyuan Hu
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On the testing AgreementSet, multi-label deep learning classifiers achieved slightly higher example-based F1 scores and lower fully incorrect ratios than single-label Random Forest baselines, but lower exact match ratios. [→ Yuanyuan Hu 2023](#yuanyuan-hu-2023)

## Evidence

### Yuanyuan Hu 2023

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Ten-fold cross-validated test on the AgreementSet of the LCT MOOC messages (Table 4), comparing multi-label BERT with and without data augmentation against Random Forest baselines with and without SMOTE. The article reports "the lower fully incorrect ratios but slightly higher example-based F1 scores" for the multi-label classifiers, while exact match ratios were lower.

> "The multi-label classifiers achieved the lower fully incorrect ratios but slightly higher example-based F1 scores than the single-label baselines."

## Discussion


## Related Claims
- [On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test](data-augmentation-improves-disagreementset-performance.md) — related
- [Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set](disagreementset-partially-correct-adjacent-predictions.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages](multi-label-predictions-adjacent-phases-only.md) — related
