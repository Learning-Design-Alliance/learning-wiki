---
type: claim
title: "SVM classification of fNIRS activation patterns distinguishes RD with 60–90% accuracy, with left MTG channels the most consistent discriminative features"
description: "SVM classification of fNIRS activation patterns distinguishes RD with 60–90% accuracy, with left MTG channels the most consistent discriminative features"
id: fnirs-mvpa-classifies-reading-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: yang-fu-2024
    resource: "https://doi.org/10.1038/s41539-024-00266-2"
    title: "Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao. (2024). Abnormal brain activation during speech perception and production in children and adults with reading difficulty. npj Science of Learning. https://doi.org/10.1038/s41539-024-00266-2"
    author: "Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yang-fu-2024-2
    resource: "https://doi.org/10.1038/s41539-024-00266-2"
    title: "Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao. (2024). Abnormal brain activation during speech perception and production in children and adults with reading difficulty. npj Science of Learning. https://doi.org/10.1038/s41539-024-00266-2"
    author: "Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# SVM classification of fNIRS activation patterns distinguishes RD with 60–90% accuracy, with left MTG channels the most consistent discriminative features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LOOCV SVM classifiers using 48-channel fNIRS beta values achieved 60–90% accuracy classifying RD in children, adults, or all participants across speech tasks, with five classifications significantly above permutation-test chance. [→ Yang Fu 2024](#yang-fu-2024)
`q2 i?` Left MTG channels appeared in the optimum feature set of all five significant classifications, and left premotor cortex, left SMA and left IFG had high weights in three classifications. [→ Yang Fu 2024 (2)](#yang-fu-2024-2)

## Evidence

### Yang Fu 2024

Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao. (2024). Abnormal brain activation during speech perception and production in children and adults with reading difficulty. npj Science of Learning. https://doi.org/10.1038/s41539-024-00266-2

`q2 · i?` · `associational · r2`

Machine-learning analysis with RBF-SVM, recursive feature elimination, and LOOCV on fNIRS beta values (1 × 48 feature vectors) from 87 participants; permutation testing (1000 iterations) evaluated significance, with printed p-values such as 0.002–0.031 for the significant classifications. No effect size is printed, so impact is null.

> "Using LOOCV, the SVM classi ﬁer yielded an accuracy ranging from 60% to 90% when classifying children, adults , or all participants across the two fNIRS tasks (Table 2)."

### Yang Fu 2024 (2)

Yang Fu, Xiaohui Yan, Jiaqi Mao, Haibin Su & Fan Cao. (2024). Abnormal brain activation during speech perception and production in children and adults with reading difficulty. npj Science of Learning. https://doi.org/10.1038/s41539-024-00266-2

`q2 · i?` · `associational · r2`

Feature-weight analysis across cross-validation folds for the five classifications exceeding permutation tests. The quote reports left MTG channels appearing in all five classifications and left premotor, SMA, and IFG in three; channel 22 is anterior MTG and channel 24 posterior MTG.

> "channels located in the left MTG were the most consistent region with high weights, because they appeared in allﬁve clas- siﬁcations, and the left premotor cortex, left SMA, and the left IFG had high w e i g h t si n t h r e e c l a s s iﬁcations."

## Discussion


## Related Claims
- [RD readers show reduced deactivation of left MTG (channel 22) during Spanish compared to Chinese speech production](rd-reduced-left-mtg-deactivation-spanish-production.md) — related
- [Feedback types elicit distinct fNIRS activation patterns: frontopolar and middle temporal gyrus higher under metacognitive feedback, supramarginal gyrus under affective feedback, DLPFC under neutral feedback](chatbot-feedback-type-brain-activation-patterns.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — a broader claim this one bears on
