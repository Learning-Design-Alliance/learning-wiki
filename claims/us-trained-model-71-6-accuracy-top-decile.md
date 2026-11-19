---
type: claim
title: "A random forest model trained on U.S. PISA data identifies top-decile U.S. science achievers with 71.6% accuracy"
description: A random forest model trained on U.S.
id: us-trained-model-71-6-accuracy-top-decile
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: xingyu-li-2021
    resource: "https://doi.org/10.48550/arXiv.2103.15212"
    title: "Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec. (2021). On the limits of algorithmic prediction across the globe. Originally published 2020. [doi:10.48550/arXiv.2103.15212](https://doi.org/10.48550/arXiv.2103.15212)"
    author: Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# A random forest model trained on U.S. PISA data identifies top-decile U.S. science achievers with 71.6% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The U.S.-trained random forest classifier correctly identifies top students in the U.S. with 71.6% accuracy on a holdout test set. [→ Xingyu Li 2021](#xingyu-li-2021)

## Evidence

### Xingyu Li 2021

Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec. (2021). On the limits of algorithmic prediction across the globe. Originally published 2020. [doi:10.48550/arXiv.2103.15212](https://doi.org/10.48550/arXiv.2103.15212)

`q2 · i?` · `associational · r3`

Cross-validated random forest classifier trained on 165 PISA variables from a nationally representative U.S. sample (N = 5,712) to identify top-decile science achievers, evaluated on a holdout set. The article reports "71.6% accuracy" in the U.S. No effect size is printed.

> "We found that the U.S.-trained model correctly identifies top students in the U.S. with 71.6% accuracy. This high level of accuracy is expected from a model that is trained and tested in the same population."

## Discussion


## Related Claims
- [Default random forest settings classify only 16% of DFW students correctly in Sample 1, and tuning the decision threshold raises DFW accuracy to 43%](default-rf-poor-dfw-tuning-raises-43-percent.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
