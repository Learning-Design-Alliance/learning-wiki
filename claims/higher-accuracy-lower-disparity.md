---
type: claim
title: Methods with higher scoring accuracy showed lower demographic disparity across the tested model combinations
description: Methods with higher scoring accuracy showed lower demographic disparity across the tested model combinations
id: higher-accuracy-lower-disparity
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
    kind: associational
    rigour: 2
---

# Methods with higher scoring accuracy showed lower demographic disparity across the tested model combinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across the four feature–classifier combinations, higher-scoring-accuracy methods exhibited lower average demographic disparity for both gender and language groupings. [→ Nico Andersen 2025](#nico-andersen-2025)

## Evidence

### Nico Andersen 2025

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `associational · r2`

Cross-method comparison (Table 5) of κ, accuracy, TPR, FPR, scoring bias D, and demographic disparity DD for gender and language. The unigram decision tree (κ = .28) showed the largest disparities (DDG = −.030, DDL = −.062); RoBERTa-SVM the smallest.

> "Methods with a higher scoring accuracy showed a lower disparity. Thus, SVM with RoBERTa embeddings as the features showed a demographic disparity of DD = −.011 for native speakers, meaning that comparing the automatic scoring bias of both groups revealed a gap of 1.1% towards non-native speakers."

## Discussion


## Related Claims
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Bias in predicting learning productivity, measured as accuracy differences across gender and parental educational background, was highly dependent on the ML method used](bias-dependent-on-ml-method.md) — related
- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](ews-and-algorithm-less-accurate-black-students.md) — related
- [The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers](language-bias-favors-foreign-speakers-roberta-svm.md) — a narrower finding that bears on this claim
